# Copyright (c) 2014, Howard Hughes Medical Institute, All rights reserved.
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright notice, 
#   this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation 
#   and/or other materials provided with the distribution.
#   * Neither the name of the Howard Hughes Medical Institute nor the names of 
#   its contributors may be used to endorse or promote products derived from 
#   this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, ANY 
# IMPLIED WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, OR FITNESS FOR A 
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# REASONABLE ROYALTIES; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pyplusplus import function_transformers as FT
from pyplusplus import module_builder
from pygccxml import declarations
from pygccxml.declarations import type_traits
from pygccxml.declarations import cpptypes
from pyplusplus.module_builder.call_policies import *
from doxygen_doc_extractor import doxygen_doc_extractor
import re
import os


class DerivedClasses(set):
    def __init__(self, base_class):
        set.__init__(self)
        self.base_class = base_class

    def include_module(self, module):
        for cls in module.classes(allow_empty=True):
            self.walk_bases(cls, cls)

    def walk_bases(self, cls, base_class):
        if cls in self:
            return
        if base_class == self.base_class:
            self.add(cls)
            # print cls.alias
        for base in base_class.bases:
            self.walk_bases(cls, base.related_class)


class BaseWrapper:
    "Base class for each OSG module wrapper"
    def __init__(self, files):
        self.max_arity = 18
        self.mb = module_builder.module_builder_t(
            files = files,
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",],
            define_symbols=["_HAS_TR1=0", "BOOST_PYTHON_MAX_ARITY=%d" % self.max_arity, ],
            indexing_suite_version=2,
            compiler='msvc9',
        )
        self.mb.BOOST_PYTHON_MAX_ARITY = self.max_arity # Prevents warnings on 10-18 argument methods

    def generate_module_code(self, module_name):
        extractor = doxygen_doc_extractor()
        self.mb.build_code_creator(module_name=module_name , doc_extractor=extractor)
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()

    def wrap_all_osg_referenced(self, namespace):
        # Identify all classes derived from osg::Referenced, 
        # and set their boost::python held_type to "osg::ref_ptr<class>"
        osg = self.mb.namespace("osg")
        referenced = osg.class_("Referenced")
        referenced_derived = DerivedClasses(referenced)
        referenced_derived.include_module(namespace)
        copyop = osg.class_("CopyOp")
        # We are interested in constructors that take an argument of type "const osg::CopyOp&""
        copyop_arg_t = declarations.reference_t(declarations.const_t(declarations.declarated_t(copyop)))
        for cls in referenced_derived:
            expose_ref_ptr_class(cls)
            # These copy constructors consistently cause trouble
            for ctor in cls.constructors(arg_types=[None, copyop_arg_t], allow_empty=True):
                ctor.exclude()


def expose_increment_operators(mb):
    "Wrap C++ operator++() and operator()-- methods as python incr() and decr() methods"
    for op in mb.member_operators('operator++', arg_types=[]):
        op.exclude()
        try: 
            op.parent.has_wrapped_increment
        except AttributeError:
            # Create less ambiguous increment/decrement function names, since there might be more than one in the file
            incr_fn_name = "wrap_increment_%s" % op.parent.alias
            op.parent.add_declaration_code('static void %s(%s& val) {++val;}' % (incr_fn_name, op.parent.demangled) )
            op.parent.add_registration_code('def("increment", &%s)' % incr_fn_name)
            op.parent.has_wrapped_increment = True
    for op in mb.member_operators('operator--', arg_types=[]):
        op.exclude()
        try: 
            op.parent.has_wrapped_decrement
        except AttributeError:
            decr_fn_name = "wrap_decrement_%s" % op.parent.alias
            op.parent.add_declaration_code('static void %s(%s& val) {--val;}' % (decr_fn_name, op.parent.demangled) )
            op.parent.add_registration_code('def("decrement", &%s)' % decr_fn_name)

def expose_nonoverridable_ref_ptr_class(cls):
    "Wrap a class that derives from osg::Referenced, using osg::ref_ptr<class_name>"
    # Derivable overridable class need to wrap a pointer to the wrapped type
    # Only for those classes with trouble, should we use the decl_string
    cls.held_type = 'osg::ref_ptr< %s >' % cls.decl_string # Insufficient for calling overridden python methods from C++
    # cls.held_type = 'osg::ref_ptr< %s >' % cls.wrapper_alias # wrapper_alias, not decl_string
    cls.include_files.append('wrap_referenced.h')
    cls.member_operators("operator=", allow_empty=True).exclude()
    if cls.is_abstract:
        # print cls.alias
        cls.noncopyable = True
        cls.no_init = True
        cls.constructors().exclude()
    
def expose_ref_ptr_class(cls):
    """
    Wrap a class that derives from osg::Referenced, using osg::ref_ptr<class_name>
    Version where python virtual method callbacks are callable from C++.
    Causes multithreading trouble maybe.
    """
    # Compute nested wrapper class name, which is needed for classes having
    # virtual methods that can be overidden in python, and need to be callable from C++,
    # such as NodeVisitors
    decl = [cls.wrapper_alias,]
    p = cls.parent
    while hasattr(p, "wrapper_alias"):
        decl.append(p.wrapper_alias)
        p = p.parent
    decl.reverse()
    wrapper_decl_string = "::".join(decl)
    cls.held_type = 'osg::ref_ptr< %s >' % wrapper_decl_string # Use wrapper class in ref_ptr, for maximum extensibility
    # cls.held_type = 'osg::ref_ptr< %s >' % cls.decl_string # Insufficient for calling overridden python methods from C++
    cls.include_files.append('wrap_referenced.h')
    cls.member_operators("operator=", allow_empty=True).exclude()
    if cls.is_abstract:
        # print cls.alias
        cls.noncopyable = True
        cls.no_init = True
        cls.constructors().exclude()
    
def hide_nonpublic(mb):
    for fn in mb.member_functions(lambda f: f.access_type != declarations.ACCESS_TYPES.PUBLIC):
        fn.exclude()
    for fn in mb.constructors(lambda f: f.access_type != declarations.ACCESS_TYPES.PUBLIC):
        fn.exclude()
    for cls in mb.classes():
        # Exclude non-public attributes
        for var in cls.variables(lambda v: v.access_type != declarations.ACCESS_TYPES.PUBLIC, allow_empty=True):
            var.exclude()
    
# https://mail.python.org/pipermail/cplusplus-sig/2009-September/014828.html
def remove_const_from_reference(type):
    "Helper to avoid compile errors with const-reference-protected-destructor argument types"
    if not type_traits.is_reference(type):
        return type
    nonref = declarations.remove_reference(type)
    if not type_traits.is_const(nonref):
        return type
    nonconst = declarations.remove_const(nonref)
    return cpptypes.reference_t(nonconst)

def hack_osg_arg(cls, fn_name, arg_name):
    "Convert one const reference function argument to non-const reference"
    for fn in cls.member_functions(fn_name, allow_empty=True):
        found_arg = False
        for arg in fn.arguments:
            if arg.name == arg_name:
                found_arg = True
                break
        if not found_arg:
            continue
        fn.add_transformation(FT.modify_type(arg_name, remove_const_from_reference))
        # avoid ugly alias
        fn.transformations[-1].alias = fn.alias

def wrap_call_policies(mb):
    "Set function and operator call policies to sensible defaults"
    for fn in mb.member_functions():
        wrap_one_call_policy(fn)
    for op in mb.member_operators():
        wrap_one_call_policy(op)

def wrap_one_call_policy(fn):
    rt = fn.return_type
    if fn.return_type.decl_string == "char const *":
        return # use default for strings
    if fn.return_type.decl_string == "char *":
        return # use default for strings
    elif fn.return_type.decl_string == "void *":
        return # use default for void pointers
    elif fn.return_type.decl_string == "::GLvoid const *":
        return # use default for void pointers
    parent_ref = declarations.reference_t(declarations.declarated_t(fn.parent))
    if declarations.is_reference(rt):
        # Need type without reference for next type checks
        nonref_rt = rt.base
        if declarations.is_arithmetic(nonref_rt) or declarations.is_enum(nonref_rt):
            # returning const& double can cause compile trouble if return_internal_reference is used
            if declarations.is_const(nonref_rt):
                fn.call_policies = return_value_policy(copy_const_reference)
                return
            # int& might need to be copy_non_const_reference...
            else:
                fn.call_policies = return_value_policy(copy_non_const_reference)
                return
        # Const string references should be copied to python strings
        if declarations.is_std_string(nonref_rt) and declarations.is_const(nonref_rt):
            fn.call_policies = return_value_policy(copy_const_reference)
            return
        # Returning reference to this same class looks like return_self() [does this always work?]
        if declarations.is_same(parent_ref, rt):
            fn.call_policies = return_self()
            return
    elif declarations.is_pointer(rt):
        # Clone methods
        if re.search(r'^clone', fn.name):
            fn.call_policies = return_value_policy(reference_existing_object)
            return
    else:
        return
    # Everything else probably returns an internal reference
    fn.call_policies = return_internal_reference()
    return
