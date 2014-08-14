from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pygccxml import declarations
import os

def wrap_osg():
    mb = module_builder.module_builder_t(
        files = ["wrap_osg.h",],
        gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
        include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",])
    osg = mb.namespace("osg")
    
    osg.include()
    # Avoid all methods that return pointers
    osg.member_functions("ptr").exclude()
    wrap_call_policies(mb)
    
    mb.build_code_creator(module_name='osg')
    mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
    # Create a file to indicate completion of wrapping script
    open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
    
def wrap_call_policies(module_builder):
    "Set function and operator call policies to sensible defaults"
    mb = module_builder
    for fn in mb.member_functions():
        wrap_one_call_policy(fn, module_builder)
    for op in mb.member_operators():
        wrap_one_call_policy(op, module_builder)

def wrap_one_call_policy(fn, module_builder):
    rt = fn.return_type
    parent_ref = declarations.reference_t(declarations.declarated_t(fn.parent))
    # If return type is not a reference, I have no opinion about the call policies
    if not declarations.is_reference(rt):
        return
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
    # Everything else probably returns an internal reference
    fn.call_policies = return_internal_reference()
    return

if __name__ == "__main__":
    wrap_osg()
