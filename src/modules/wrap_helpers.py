from pygccxml import declarations
from pyplusplus.module_builder.call_policies import *
import re

def expose_ref_ptr_class(cls):
    cls.held_type = 'osg::ref_ptr< %s >' % cls.wrapper_alias
    cls.add_declaration_code("""
        // Tell boost::python that osg::ref_ptr is a smart pointer class
        namespace boost { namespace python {
          template <class T> struct pointee< osg::ref_ptr<T> >
          { typedef T type; };
        } } // namespace boost::python
    """)
    
def hide_nonpublic(mb):
    for fn in mb.member_functions(lambda f: f.access_type != declarations.ACCESS_TYPES.PUBLIC):
        fn.exclude()
    for fn in mb.constructors(lambda f: f.access_type != declarations.ACCESS_TYPES.PUBLIC):
        fn.exclude()
    for cls in mb.classes():
        # Exclude non-public attributes
        for var in cls.variables(lambda v: v.access_type != declarations.ACCESS_TYPES.PUBLIC, allow_empty=True):
            var.exclude()
    
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