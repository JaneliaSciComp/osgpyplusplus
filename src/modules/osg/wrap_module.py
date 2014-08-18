from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import re

class OsgWrapper:
    def __init__(self):
        self.mb = module_builder.module_builder_t(
            files = ["wrap_osg.h",],
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",],
            define_symbols=["BOOST_PYTHON_MAX_ARITY=18"],
        )
        self.mb.BOOST_PYTHON_MAX_ARITY = 18 # Prevents warnings on 10-18 argument methods
            
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
        mb.member_functions("releaseGLObjects").exclude() # Because I don't want to wrap State yet...
        for cls in mb.classes():
            # Exclude non-public attributes
            for var in cls.variables(lambda v: v.access_type != declarations.ACCESS_TYPES.PUBLIC, allow_empty=True):
                var.exclude()
            # Exclude "_v" attribute in vectors
            cls.variables('_v', allow_empty=True).exclude()

        for cls in mb.classes(lambda c: c.name.startswith('ref_ptr<')):
            cls.exclude()
        for cls in mb.classes(lambda c: c.name.startswith('vector<')):
            cls.exclude()
        for cls in mb.classes(lambda c: c.name.startswith('BoundingSphereImpl<')):
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

        # Manage classes maintained by osg::ref_ptr<>
        for cls_name in ["Referenced", 
                "Object",
                "StateSet",
                "Uniform",
                "Node",
                "Shader",
                "DisplaySettings",
                "BufferObject",
                "AtomicCounterBufferObject",
                "RefMatrixf",
                "RefMatrixd",
                ]:
            cls = self.mb.class_(cls_name)
            self.expose_ref_ptr_class(cls)

        # Many of those ref_ptr classes have a troublesome two-argument copy constructor
        for cls_name in [
                "Node", 
                "Object",
                "Shader",
                "BufferData",
                "AtomicCounterBufferObject",
                "BufferObject",
                ]:
            cls = self.mb.class_(cls_name)
            cls.constructors(arg_types=[None, None]).exclude()
            
        # Many of those ref_ptr classes have a troublesome one-argument copy constructor
        for cls_name in [
                "RefMatrixf",
                "RefMatrixd",
                ]:
            cls = self.mb.class_(cls_name)
            for ctor in cls.constructors():
                if ctor.is_copy_constructor:
                    ctor.exclude()

        # TODO confusing protected destructor compile errors, associated with comparison operators
        for cls_name in ["StateSet", "Uniform"]:
            cls = self.mb.class_(cls_name)
            for fn_name in ["compare", 
                    "compareData", 
                    "copyData",
                    "merge"]: # TODO confusing protected destructor compile errors
                cls.member_functions(fn_name, allow_empty=True).exclude()
            for op_name in ["operator<", "operator==", "operator!="]:
                cls.member_operator(op_name).exclude() # TODO confusing protected destructor compile errors            

        # Set return value policy for getter methods
        # [override any exceptions LATER in this method]
        for fn in self.mb.member_functions():
            if not declarations.is_pointer(fn.return_type):
                continue
            if fn.return_type.decl_string == "char const *":
                continue
            if fn.return_type.decl_string == "void const *":
                continue
            if fn.return_type.decl_string == "::GLvoid const *":
                continue
            if re.search(r'^get[A-Z]', fn.demangled_name):
                fn.call_policies = return_internal_reference()
            elif re.search(r'^as[A-Z]', fn.demangled_name):
                fn.call_policies = return_internal_reference()

        # Call custom methods to wrap individual classes
        self.wrap_node()
        self.wrap_quaternion()
        self.wrap_observerset()
        self.wrap_referenced()
        self.wrap_stats()
        self.wrap_copyop()
        self.wrap_userdatacontainer()
        self.wrap_vbo()
        self.wrap_array()
        self.wrap_uniform()
        self.wrap_stateset()
        self.wrap_displaysettings()
        
        # Exclude classes I'm too lazy to wrap right now
        self.mb.class_("StateAttributeCallback").exclude()
        self.mb.class_("StateAttribute").exclude()
        self.mb.class_("vector<osg::Group*>").exclude()
        self.mb.class_("ShaderComponent").exclude()
        self.mb.class_("ShaderBinary").exclude()
        self.mb.class_("Shader").exclude()
        self.mb.class_("PixelDataBufferObject").exclude()
        self.mb.class_("PixelBufferObject").exclude()
        self.mb.class_("NodeCallback").exclude()
        self.mb.class_("IndexArray").exclude()
        self.mb.class_("GLBufferObjectSet").exclude()
        self.mb.class_("GLBufferObjectManager").exclude()
        self.mb.class_("GLBufferObject").exclude()
        self.mb.class_("GL2Extensions").exclude()
        self.mb.class_("ElementBufferObject").exclude()
        self.mb.class_("ConstArrayVisitor").exclude()
        # self.mb.class_("std_vector_osgGroupPtr").exclude()
        
        # Wrap Free functions
        mb.free_function("getNotifyHandler").call_policies = return_value_policy(reference_existing_object)
        for fn in mb.free_functions("notify"):
            fn.call_policies = return_value_policy(reference_existing_object)
        
        # Write results
        self.mb.build_code_creator(module_name='osg')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
    
    def wrap_node(self):
        cls = self.mb.class_("Node")
        # Avoid wrapping NodeVisitor for the moment...
        for fn_name in ["accept", 
                "ascend", 
                "traverse",
                "asTransform", # TODO wrap Transform
                "asTerrain", # TODO wrap Terrain
                "asSwitch", # TODO wrap Switch
                "asGroup", # TODO wrap Group
                "getParent", 
                "asGeode", # TODO wrap Geode
                "asCamera", # TODO wrap Camera
                "getParents", # TODO wrap Group
                ]:
            cls.member_functions(fn_name).exclude()
        cls.class_("ComputeBoundingSphereCallback").exclude()
    
    def wrap_displaysettings(self):
        cls = self.mb.class_("DisplaySettings")
        cls.member_operators().exclude()
        cls.member_functions("merge").exclude()
        cls.member_functions("setDisplaySettings").exclude()
        cls.constructors().exclude()
        cls.noncopyable = True
    
    def wrap_stateset(self):
        cls = self.mb.class_("StateSet")
        # work around scope problem with default arguments
        cls.add_declaration_code("""
            static int ON = ::osg::StateAttribute::ON;
            static int OFF = ::osg::StateAttribute::OFF;
        """)
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_operators("operator()").exclude()
    
    def wrap_uniform(self):
        unif = self.mb.class_("Uniform")
        unif.constructors(arg_types=[None, None]).exclude() # copy constructor
        unif.member_operators("operator()").exclude() # because I don't want to wrap NodeVisitor yet...
        
    def wrap_array(self):
        arr = self.mb.class_("Array")
        self.expose_ref_ptr_class(arr)
        for fn in arr.member_functions("getVertexBufferObject"):
            fn.call_policies = return_internal_reference()
        for fn in arr.member_functions("asArray"):
            fn.call_policies = return_self()
        arr.constructors(arg_types=[None, None]).exclude() # avoid copy constructor
        bd = self.mb.class_("BufferData")
        for fn_name in ["asImage", "asPrimitiveSet"]:
            for fn in bd.member_functions(fn_name):
                fn.call_policies = return_internal_reference()
                fn.exclude() # avoid wrapping Image and Privitive set, for the moment
    
    def wrap_vbo(self):
        vbo = self.mb.class_("VertexBufferObject")
        self.expose_ref_ptr_class(vbo)
        vbo.member_functions("getArray").call_policies = return_internal_reference()
        vbo.constructors(arg_types=[None, None]).exclude()
        ubo = self.mb.class_("UniformBufferObject")
        self.expose_ref_ptr_class(ubo)
        ubo.constructors(arg_types=[None, None]).exclude()
    
    def wrap_userdatacontainer(self):
        udc = self.mb.class_("UserDataContainer")
        dudc = self.mb.class_("DefaultUserDataContainer")
        for cls in [udc, dudc]:
            self.expose_ref_ptr_class(cls)
            cls.member_functions("getDescriptions").exclude()
            cls.member_functions("getUserObject", allow_empty=True).exclude()
            cls.constructors(arg_types=[None, None]).exclude() # No implicit copy constructor
        udc.constructors().exclude() # Abstract class
        
    def wrap_copyop(self):
        copyop = self.mb.class_("CopyOp")
        for op in copyop.member_operators("operator()"):
            op.call_policies = return_value_policy(reference_existing_object)
            op.exclude() # Avoid wrapping all those other classes, for the moment
        
    def wrap_observerset(self):
        os = self.mb.class_("ObserverSet")
        self.expose_ref_ptr_class(os)
        for fn_name in ["getObserverdObject", "addRefLock"]:
            for fn in os.member_functions(fn_name):
                fn.call_policies = return_value_policy(reference_existing_object)
        for fn in os.member_functions("getObserverSetMutex"):
            fn.call_policies = return_internal_reference()
    
    def wrap_stats(self):
        stats = self.mb.class_("Stats")
        self.expose_ref_ptr_class(stats)
        for fn_name in ['getAttribute', 'getAveragedAttribute']:
            for fn in stats.member_functions(fn_name):
                fn.exclude() # TODO compile error hidden destructor
                # fn.add_transformation(FT.output('value'))
                # avoid ugly alias
                # fn.transformations[-1].alias = fn.alias   
    
    def expose_ref_ptr_class(self, cls):
        cls.held_type = 'osg::ref_ptr< %s >' % cls.wrapper_alias
        cls.add_declaration_code("""
            // Tell boost::python that osg::ref_ptr is a smart pointer class
            namespace boost { namespace python {
              template <class T> struct pointee< osg::ref_ptr<T> >
              { typedef T type; };
            } } // namespace boost::python
        """)
    
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
