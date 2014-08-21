from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import re
import sys

sys.path.append("..")
from wrap_helpers import *

class OsgWrapper(BaseWrapper):
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osg.h",])
            
    def wrap(self):
        mb = self.mb
        
        # for debugging only...
        if False:
            print mb.class_("Thread").member_function("getImplementation").return_type.decl_string
            exit(0)
        
        # Wrap everything in the "osg" namespace
        osg = mb.namespace("osg")
        osg.include()
        mb.namespace("OpenThreads").include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osg')).include()
        
        for fn in mb.free_functions("createGeodeForImage"):
            fn.call_policies = return_value_policy(reference_existing_object)
        
        hide_nonpublic(self.mb)
        
        expose_increment_operators(self.mb)
        
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
        
        wrap_call_policies(self.mb)

        # Manage classes maintained by osg::ref_ptr<>
        # Look for "error C2065: 'SHALLOW_COPY' : undeclared identifier"
        # TODO - write a method to identify all these descendants of "Referenced"
        for cls_name in [
                "AtomicCounterBufferObject",
                "Box",
                "BufferObject",
                "Camera",
                "Capsule",
                "ClearNode",
                "ColorMask",
                "CompositeShape",
                "Cone",
                "ConvexHull",
                "Cylinder",
                "DisplaySettings",
                "Drawable",
                "DrawArrays",
                "DrawArrayLengths",
                "DrawElements",
                "DrawElementsUShort",
                "DrawElementsUInt",
                "DrawElementsUByte",
                "Geode",
                "Geometry",
                "Group",
                "HeightField",
                "Image",
                "InfinitePlane",
                "Light",
                "Object",
                "Node",
                "PrimitiveSet",
                "Program",
                "Referenced", 
                "RefMatrixf",
                "RefMatrixd",
                "ShaderComposer",
                "Shader",
                "Shape",
                "Sphere",
                "State",
                "StateSet",
                "Texture",
                "Transform",
                "TriangleMesh",
                "Uniform",
                "View",
                "Viewport",
                ]:
            cls = osg.class_(cls_name)
            expose_ref_ptr_class(cls)

        # Many ref_ptr classes have trouble with implicit conversion operators
        for cls_name in [
                "Box",
                "Camera",
                "Capsule",
                "ClearNode",
                "ColorMask",
                "CompositeShape",
                "Cone",
                "ConvexHull",
                "Cylinder",
                "DrawArrays",
                "DrawArrayLengths",
                "DrawElementsUShort",
                "DrawElementsUInt",
                "DrawElementsUByte",
                "Geode",
                "Geometry",
                "Group",
                "HeightField",
                "Image",
                "InfinitePlane",
                "Light",
                "Program",
                "ShaderComposer",
                "Sphere",
                "Transform",
                "TriangleMesh",
                "View",
                "Viewport",
                ]:
            osg.class_(cls_name).constructors().allow_implicit_conversion = False

        # Many of those ref_ptr classes have a troublesome two-argument copy constructor
        # Look for mention of two argument constructor, with CopyOp second, in compiler error message
        for cls_name in [
                "AtomicCounterBufferObject",
                "Box",
                "Camera",
                "Capsule",
                "BufferData",
                "BufferObject",
                "ClearNode",
                "ColorMask",
                "CompositeShape",
                "Cone",
                "ConvexHull",
                "Cylinder",
                "DrawArrayLengths",
                "DrawArrays",
                "DrawElementsUShort",
                "DrawElementsUInt",
                "DrawElementsUByte",
                "Geode",
                "Geometry",
                "Group",
                "HeightField",
                "Image",
                "InfinitePlane",
                "Light",
                "Node", 
                "Object",
                "Program",
                "Shader",
                "ShaderComposer",
                "Sphere",
                "TriangleMesh",
                "Viewport",
                "View",
                ]:
            cls = osg.class_(cls_name)
            cls.constructors(arg_types=[None, None]).exclude()
            
        # Many of those ref_ptr classes have a troublesome one-argument copy constructor
        for cls_name in [
                "RefMatrixf",
                "RefMatrixd",
                ]:
            cls = osg.class_(cls_name)
            for ctor in cls.constructors():
                if ctor.is_copy_constructor:
                    ctor.exclude()

        # Abstract classes with virtual destructors cannot be copied
        # Avoids compile error "error C2259: '' : cannot instantiate abstract class"
        for cls_name in [
                "Array",
                "BufferObject",
                "DisplaySettings",
                "Drawable",
                "DrawElements",
                "Object",
                "PrimitiveSet",
                "Referenced",
                "Shape",
                "Texture",
                "Viewport",
                ]:
            cls = osg.class_(cls_name)
            cls.noncopyable = True
            cls.no_init = True
            cls.member_operators("operator=", allow_empty=True).exclude()
            cls.constructors().exclude()

        # TODO confusing protected destructor compile errors, associated with comparison operators
        for cls_name in [
                "ColorMask",
                "Image", 
                "Light", 
                "Program",
                "StateAttribute",
                "StateSet",
                "Texture",
                "Uniform", 
                "Viewport",
                ]:
            cls = osg.class_(cls_name)
            for fn_name in [
                    "compare", 
                    "compareData", 
                    "copyData",
                    "merge"]: # TODO confusing protected destructor compile errors
                cls.member_functions(fn_name, allow_empty=True).exclude()
            for op_name in ["operator<", "operator==", "operator!="]:
                cls.member_operators(op_name, allow_empty=True).exclude() # TODO confusing protected destructor compile errors

        # Call custom methods to wrap individual classes
        self.wrap_camera()
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
        self.wrap_state()
        self.wrap_program()
        self.wrap_image()
        self.wrap_drawable()

        self.mb.class_("ConstShapeVisitor").member_functions("apply").exclude()
        
        # Exclude classes I'm too lazy to wrap right now
        for cls_name in [
                "StateAttributeCallback", 
                "StateAttribute", 
                "vector<osg::Group*>", 
                "ShaderComponent", 
                "ShaderBinary", 
                "Shader", 
                "PixelDataBufferObject", 
                "PixelBufferObject", 
                "NodeCallback", 
                "IndexArray", 
                "GLBufferObjectSet", 
                "GLBufferObjectManager", 
                "GLBufferObject", 
                "GL2Extensions", 
                "ElementBufferObject", 
                "ConstArrayVisitor", 
                "NodeVisitor", 
                "vector<osg::VertexAttribAlias>",
                "VertexAttribAlias",
                "GraphicsContext",
                "Texture",
                "Transform",
                ]:
            self.mb.class_(cls_name).exclude()
            self.mb.class_(lambda c: c.alias == "VertexAttribAliasList").exclude()
            self.mb.classes(lambda c: c.name.startswith("observer_ptr<")).exclude()
            self.mb.classes(lambda c: c.name.startswith("MixinVector<")).exclude()
            self.mb.classes(lambda c: c.name.startswith("TemplateArray<")).exclude()
            self.mb.class_("Texture").class_("TextureObject").exclude()
        
        # Wrap Free functions
        mb.free_function("getNotifyHandler").call_policies = return_value_policy(reference_existing_object)
        for fn in mb.free_functions("notify"):
            fn.call_policies = return_value_policy(reference_existing_object)
        # TODO createTexturedQuadGeometry should create a ref_ptr object?
        mb.free_functions("createTexturedQuadGeometry").call_policies = return_value_policy(reference_existing_object)
        
        # Write results
        self.mb.build_code_creator(module_name='osg')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
    
    def wrap_drawable(self):
        drawable = self.mb.class_("Drawable")
        de = drawable.class_("Extensions")
        expose_ref_ptr_class(de)
        de.member_functions("glMapBuffer").exclude()
        de.exclude()
        cbb = drawable.class_("ComputeBoundingBoxCallback")
        expose_ref_ptr_class(cbb)
        cbb.constructors().exclude()
        cbb.exclude()
    
    def wrap_image(self):
        image = self.mb.class_("Image")
        image.member_functions("data").exclude()
        image.member_functions("getMipmapData").exclude()
    
    def wrap_program(self):
        program = self.mb.class_("Program")
        program.member_functions("apply").exclude()
        pb = program.class_("ProgramBinary")
        expose_ref_ptr_class(pb)
        pb.member_functions("getData").exclude()
    
    def wrap_state(self):
        state = self.mb.class_("State")
        # Avoid troublesome VertexAttribAliasList class
        state.member_functions(lambda f: f.name.endswith("AliasList")).exclude()
    
    def wrap_camera(self):
        camera = self.mb.class_("Camera")
        dc = camera.class_("DrawCallback")
        expose_ref_ptr_class(dc)
        dc.constructors().exclude()
        dc.exclude()
    
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
    
    def wrap_stateset(self):
        cls = self.mb.class_("StateSet")
        # work around scope problem with default arguments
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_operators("operator()").exclude()
    
    def wrap_uniform(self):
        unif = self.mb.class_("Uniform")
        unif.constructors(arg_types=[None, None]).exclude() # copy constructor
        unif.member_operators("operator()").exclude() # because I don't want to wrap NodeVisitor yet...
        
    def wrap_array(self):
        arr = self.mb.class_("Array")
        expose_ref_ptr_class(arr)
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
        expose_ref_ptr_class(vbo)
        vbo.member_functions("getArray").call_policies = return_internal_reference()
        vbo.constructors(arg_types=[None, None]).exclude()
        ubo = self.mb.class_("UniformBufferObject")
        expose_ref_ptr_class(ubo)
        ubo.constructors(arg_types=[None, None]).exclude()
    
    def wrap_userdatacontainer(self):
        udc = self.mb.class_("UserDataContainer")
        dudc = self.mb.class_("DefaultUserDataContainer")
        for cls in [udc, dudc]:
            expose_ref_ptr_class(cls)
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
        expose_ref_ptr_class(os)
        for fn_name in ["getObserverdObject", "addRefLock"]:
            for fn in os.member_functions(fn_name):
                fn.call_policies = return_value_policy(reference_existing_object)
        for fn in os.member_functions("getObserverSetMutex"):
            fn.call_policies = return_internal_reference()
    
    def wrap_stats(self):
        stats = self.mb.class_("Stats")
        expose_ref_ptr_class(stats)
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
        ref.constructors(arg_types=[None]).exclude() # remove non-compiling copy constructor

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

if __name__ == "__main__":
    wrapper = OsgWrapper()
    wrapper.wrap()
