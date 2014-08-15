from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os

class OsgWrapper:
    def __init__(self):
        self.mb = module_builder.module_builder_t(
            files = ["wrap_osg.h",],
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",])
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        mb.namespace("osg").include()
        mb.namespace("OpenThreads").include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osg')).include()
        
        # But don't export non-public member functions
        for fn in mb.member_functions(lambda f: f.access_type != declarations.ACCESS_TYPES.PUBLIC):
            fn.exclude()
        
        self.expose_increment_operators()
        
        # Avoid all methods that return raw pointers
        mb.member_functions("ptr").exclude()
        
        # Don't use internal array member TODO - make osg::VecWhatever into excellent python sequences, with slices and all
        for cls in mb.classes():
            # Exclude non-public attributes
            for var in cls.variables(lambda v: v.access_type != declarations.ACCESS_TYPES.PUBLIC, allow_empty=True):
                var.exclude()
            # Exclude "_v" attribute in vectors
            cls.variables('_v', allow_empty=True).exclude()
        
        self.wrap_call_policies()
        
        self.wrap_quaternion()
        # self.wrap_referenced()
        self.mb.class_("Referenced").exclude() # protected destructor...
        
        self.mb.build_code_creator(module_name='osg')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
        
    def wrap_referenced(self):
        ref = self.mb.class_("Referenced")
        for fn_name in ['getRefMutex', # TODO might be existing object, depending on compile flags
                'getObserverSet', 
                'getOrCreateObserverSet',
                'getDeleteHandler']: 
            for fn in ref.member_functions(fn_name):
                fn.call_policies = return_internal_reference()
        for fn_name in ['getGlobalReferencedMutex', ]:
            for fn in ref.member_functions(fn_name):
                fn.call_policies = return_value_policy(reference_existing_object)
        
    def expose_increment_operators(self):
        "Wrap C++ operator++() and operator()-- methods as python incr() and decr() methods"
        mb = self.mb
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

    def wrap_quaternion(self):
        quat = self.mb.class_("Quat")
        have_getRotate = False # Just wrap one version
        for fn in quat.member_functions("getRotate"):
            if len(fn.arguments) != 2: # ignore 4-argument versions
                fn.exclude()
            elif have_getRotate: # only accept the very first 2-argument version
                fn.exclude()
            else:
                # Only expose this one version of getRotate
                fn.add_transformation(FT.output('angle'), FT.output('vec'))
                # avoid ugly alias
                fn.transformations[-1].alias = fn.alias
                have_getRotate = True
        # Avoid refering to Matrix types for now... TODO - remove this
        for fn in quat.member_functions("set"):
            arg = fn.argument_types[0].decl_string
            if "Matrix" in arg:
                fn.exclude()
    
    def wrap_call_policies(self):
        "Set function and operator call policies to sensible defaults"
        mb = self.mb
        for fn in mb.member_functions():
            self.wrap_one_call_policy(fn)
        for op in mb.member_operators():
            self.wrap_one_call_policy(op)

    def wrap_one_call_policy(self, fn):
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
    wrapper = OsgWrapper()
    wrapper.wrap()
