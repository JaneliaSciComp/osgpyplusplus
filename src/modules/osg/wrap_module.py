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
        for fn in mb.constructors(lambda f: f.access_type != declarations.ACCESS_TYPES.PUBLIC):
            fn.exclude()
        
        self.expose_increment_operators()
        
        # Avoid all methods that return raw pointers
        mb.member_functions("ptr").exclude()

        # Rules that apply to all classes
        for cls in mb.classes():
            # Exclude non-public attributes
            for var in cls.variables(lambda v: v.access_type != declarations.ACCESS_TYPES.PUBLIC, allow_empty=True):
                var.exclude()
            # Exclude "_v" attribute in vectors
            cls.variables('_v', allow_empty=True).exclude()

        for cls in mb.classes(lambda c: c.name.startswith('ref_ptr<')):
            cls.exclude()
        
        self.wrap_call_policies()

        # Common treatment for all derived classes of Object
        for fn_name in ["cloneType", "clone"]:
            for fn in self.mb.member_functions(fn_name):
                # manage_new_object causes compile errors because of protected destructor
                fn.call_policies = return_value_policy(reference_existing_object)
        for fn_name in ["getUserDataContainer", "getOrCreateUserDataContainer", "getUserData"]:
            for fn in self.mb.member_functions(fn_name):
                fn.call_policies = return_internal_reference()
        for fn_name in ["getUserObject",]:
            for fn in self.mb.member_functions(fn_name):
                fn.call_policies = return_internal_reference()
                fn.exclude()

        # Call custom methods to wrap individual classes
        self.wrap_quaternion()
        self.wrap_observerset()
        self.wrap_referenced()
        self.wrap_stats()
        self.wrap_copyop()
        self.wrap_object()
        self.wrap_userdatacontainer()
        
        # Wrap Free functions
        mb.free_function("getNotifyHandler").call_policies = return_value_policy(reference_existing_object)
        for fn in mb.free_functions("notify"):
            fn.call_policies = return_value_policy(reference_existing_object)
        
        # Write results
        self.mb.build_code_creator(module_name='osg')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
    
    def wrap_userdatacontainer(self):
        for class_name in ["UserDataContainer", "DefaultUserDataContainer"]:
            udc = self.mb.class_(class_name)
            # udc.member_functions("getDescriptions").exclude()
            # udc.member_functions("clone", allow_empty=True).exclude()
            # udc.member_functions("cloneType", allow_empty=True).exclude()
            # udc.member_functions("getUserObject", allow_empty=True).exclude()
            udc.constructors().exclude()
            # udc.noncopyable = True
            # udc.no_init = True
    
    def wrap_object(self):
        ob = self.mb.class_("Object")
        ob.constructors(arg_types=[None, None]).exclude()
        ob.member_functions("releaseGLObjects").exclude() # Because I don't want to wrap State yet...
        ob.constructors().exclude()
        
    def wrap_copyop(self):
        copyop = self.mb.class_("CopyOp")
        for op in copyop.member_operators("operator()"):
            op.call_policies = return_value_policy(manage_new_object)
        
    def wrap_observerset(self):
        os = self.mb.class_("ObserverSet")
        for fn_name in ["getObserverdObject", "addRefLock"]:
            for fn in os.member_functions(fn_name):
                fn.call_policies = return_value_policy(reference_existing_object)
        for fn in os.member_functions("getObserverSetMutex"):
            fn.call_policies = return_internal_reference()
    
    def wrap_stats(self):
        stats = self.mb.class_("Stats")
        for fn_name in ['getAttribute', 'getAveragedAttribute']:
            for fn in stats.member_functions(fn_name):
                fn.exclude() # TODO compile error hidden destructor
                # fn.add_transformation(FT.output('value'))
                # avoid ugly alias
                # fn.transformations[-1].alias = fn.alias   
        
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
        # Protected destuctor means compile errors on copy operations
        ref.noncopyable = True
        ref.member_operators("operator=").exclude() # Avoid protected destructor compile error
        ref.constructors(arg_types=[None]).exclude() # remove non-compiling copy constructor
        
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
