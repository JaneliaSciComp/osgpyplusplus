from pyplusplus import function_transformers as FT
from pyplusplus import module_builder
from pygccxml import declarations
from pygccxml.declarations import type_traits
from pygccxml.declarations import cpptypes
from pyplusplus.module_builder.call_policies import *
import re

class BaseWrapper:
    def __init__(self, files):
        self.mb = module_builder.module_builder_t(
            files = files,
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",],
            define_symbols=["BOOST_PYTHON_MAX_ARITY=18"],
        )
        self.mb.BOOST_PYTHON_MAX_ARITY = 18 # Prevents warnings on 10-18 argument methods

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

def expose_ref_ptr_class(cls):
    # Compute nested wrapper class name
    decl = [cls.wrapper_alias,]
    p = cls.parent
    while hasattr(p, "wrapper_alias"):
        decl.append(p.wrapper_alias)
        p = p.parent
    decl.reverse()
    wrapper_decl_string = "::".join(decl)
    # cls.held_type = 'osg::ref_ptr< %s >' % wrapper_decl_string # TODO wrapper class? or regular osg class in ref_ptr?
    cls.held_type = 'osg::ref_ptr< %s >' % cls.decl_string
    cls.include_files.append('wrap_referenced.h')
    
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
    for fn in cls.member_functions(fn_name):
        fn.add_transformation(FT.modify_type(arg_name, remove_const_from_reference))

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
    if fn.return_type.decl_string == "const *":
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