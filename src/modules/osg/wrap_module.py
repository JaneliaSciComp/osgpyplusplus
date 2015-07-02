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

from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import textwrap
import os
import re
import sys

sys.path.append("..")
from wrap_helpers import *


# This hack tweaks class registration order, to avoid runtime module load error
# see https://www.mail-archive.com/cplusplus-sig@python.org/msg01538.html
import pyplusplus
pypp_sort_classes = pyplusplus.creators_factory.sort_algorithms.sort_classes
def my_sort_classes(classes, include_vars=False):
    sorted = pypp_sort_classes(classes, include_vars)
    # Place Object immediately after Referenced
    obj = [x for x in sorted if x.alias == "Object"]
    ref = [x for x in sorted if x.alias == "Referenced"]
    if len(obj) > 0 and len(ref) > 0:
        # print len(obj), len(ref)
        object_ix = sorted.index(obj[0])
        referenced_ix = sorted.index(ref[0])
        if object_ix > referenced_ix + 1:
            # print object_ix, referenced_ix
            sorted.remove(obj[0])
            sorted.insert(referenced_ix + 1, obj[0])
            # exit(0)
    return sorted
pyplusplus.creators_factory.sort_algorithms.sort_classes = my_sort_classes


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

        openthreads = mb.namespace("OpenThreads")
        openthreads.include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osg')).include()
        
        hide_nonpublic(self.mb)
        
        # Identify all classes derived from osg::Referenced, 
        # and set their boost::python held_type to "osg::ref_ptr<class>"
        self.wrap_all_osg_referenced(osg)
        self.wrap_all_osg_referenced(openthreads)

        # Special treatment for classes that need to be called back from C++
        expose_overridable_ref_ptr_class(mb.class_("NodeVisitor"))

        for fn in mb.free_functions("createGeodeForImage"):
            fn.call_policies = return_value_policy(reference_existing_object)
        
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
        # for cls in mb.classes(lambda c: c.name.startswith('BoundingSphereImpl<')):
        #     cls.exclude()
        
        wrap_call_policies(self.mb)
        
        # mb.member_functions("getName").call_policies = return_value_policy(copy_const_reference)

        # Many of those ref_ptr classes have a troublesome one-argument copy constructor
        for cls_name in [
                "RefMatrixf",
                "RefMatrixd",
                ]:
            cls = osg.class_(cls_name)
            for ctor in cls.constructors():
                if ctor.is_copy_constructor:
                    ctor.exclude()

        # TODO confusing protected destructor compile errors, associated with comparison operators
        # TODO need to remove const from both argument type, AND from wrapped function source object type
        for cls_name in [
                "ClipPlane",
                "ColorMask",
                "Image", 
                "Light", 
                "Program",
                "StateAttribute",
                "StateSet",
                "Texture",
                "Texture2D",
                "TexGen",
                "Uniform", 
                "VertexProgram",
                "Viewport",
                ]:
            cls = osg.class_(cls_name)
            self.ignore_protected_destructor_problem_fns(cls)

        cls = osg.class_("VertexProgram").class_("Extensions")
        hack_osg_arg(cls, "lowestCommonDenominator", "rhs")
        self.ignore_protected_destructor_problem_fns(cls)
        cls.constructors(arg_types=[None]).exclude() # copy constructor

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
        self.wrap_gl_symbols()

        self.mb.class_("ConstShapeVisitor").member_functions("apply").exclude()
        self.mb.class_("NodeVisitor").member_functions("validNodeMask").exclude()
        # osg.class_("Texture").member_functions("compare").exclude()
        osg.class_("CoordinateSystemNode").member_functions("set").exclude()
        osg.class_("Texture2D").class_("SubloadCallback").exclude()
        osg.class_("Timer").member_functions("instance").call_policies = return_value_policy(reference_existing_object)

        osg.class_("Fog").member_function("compare").exclude()

        # Transform vector x(), y(), z() methods into properties
        for cls in osg.classes(lambda c: c.name.startswith("Vec")):
            for fn_name in ["x", "y", "z", "w", "r", "g", "b", "a"]:
                for fn in cls.member_functions(fn_name, allow_empty=True):
                    fn.exclude()
                    cls.add_property(fn_name, fn) # TODO setter
                    # expose __str__ method

        # Expose __str__ methods for Vec*, Matrix*, Quat, based on ostream helpers
        for cls_prefix in ["Vec", "Matrix", "RefMatrix", "Quat"]:
            for cls in osg.classes(lambda c: c.name.startswith(cls_prefix)):
                if cls.alias.endswith("Transform"): # MatrixTransform
                    continue
                if cls.alias.endswith("i"): # Vec4ui, Vec4i compile errors
                    continue
                if cls.alias.endswith("us"):
                    continue
                if cls.alias.endswith("ub"):
                    continue
                # Expose a method that converts vec to string
                cls.add_registration_code("def( bp::self_ns::str(bp::self) )")

        # Pure virtual "compare" method causes compile error
        texture = osg.class_("Texture")
        # print dir(texture)
        for fn in texture.redefined_funcs():
            if "compare" in fn.alias:
                # print fn
                texture.redefined_funcs().remove(fn)
        # exit(0)
        
        # Exclude classes I'm too lazy to wrap right now
        for cls_name in [
                "StateAttributeCallback", 
                # "StateAttribute", 
                # "vector<osg::Group*>", 
                "ShaderComponent", 
                "ShaderBinary", 
                "Shader", 
                "PixelDataBufferObject", 
                "PixelBufferObject", 
                # "NodeCallback", 
                "IndexArray", 
                "GLBufferObjectSet", 
                "GLBufferObjectManager", 
                "GLBufferObject", 
                "GL2Extensions", 
                "ElementBufferObject", 
                "ConstArrayVisitor", 
                # "NodeVisitor", 
                "vector<osg::VertexAttribAlias>",
                "VertexAttribAlias",
                # "GraphicsContext",
                # "Texture",
                # "Transform",
                ]:
            self.mb.class_(cls_name).exclude()
            self.mb.class_(lambda c: c.alias == "VertexAttribAliasList").exclude()
            self.mb.classes(lambda c: c.name.startswith("observer_ptr<")).exclude()
            self.mb.classes(lambda c: c.name.startswith("MixinVector<")).exclude()
            # self.mb.classes(lambda c: c.name.startswith("TemplateArray<")).exclude()
            self.mb.class_("Texture").class_("TextureObject").exclude()
        
        # Wrap Free functions
        for fn_name in [
                "createTexturedQuadGeometry",
                "getNotifyHandler",
                "notify",
                ]:
            mb.free_functions(fn_name).call_policies = return_value_policy(reference_existing_object)
        for fn_name in [
                "initOQState", # link error
                "initOQDebugState", # link error
                ]:
            mb.free_functions(fn_name).exclude()
        
        # TODO - This is how to wrap one array type: Wrap more
        for alias in ["Vec3Array", "Vec4Array"]:
            arr = osg.classes(lambda c: c.alias == alias)[0]
            arr.include_files.append("indexing_helpers.h")
            t = arr.demangled
            arr.add_registration_code("""
                def(bp::indexing::container_suite<
                        %s, 
                        bp::indexing::all_methods, 
                        list_algorithms<OsgArray_container_traits<%s, %s::ElementDataType, int> > >())
                """ % (t, t, t) )
        # exit(0)

        # Create alias for Matrix, just like in <osg/Matrix> header
        self.mb.add_registration_code(textwrap.dedent("""

            #ifdef OSG_USE_FLOAT_MATRIX
                boost::python::scope().attr("Matrix") = boost::python::scope().attr("Matrixf");
                boost::python::scope().attr("RefMatrix") = boost::python::scope().attr("RefMatrixf");
            #else
                boost::python::scope().attr("Matrix") = boost::python::scope().attr("Matrixd");
                boost::python::scope().attr("RefMatrix") = boost::python::scope().attr("RefMatrixd");
            #endif

            boost::python::scope().attr("Vec4") = boost::python::scope().attr("Vec4f");
            boost::python::scope().attr("Vec3") = boost::python::scope().attr("Vec3f");
            boost::python::scope().attr("Vec2") = boost::python::scope().attr("Vec2f");
            """))

        # Write results
        self.generate_module_code("_osg")

    def ignore_protected_destructor_problem_fns(self, cls):
        for fn_name in [
                "compare", 
                "compareData", 
                "copyData",
                "merge"]: # TODO confusing protected destructor compile errors
            cls.member_functions(fn_name, allow_empty=True).exclude()
        for op_name in ["operator<", "operator==", "operator!="]:
            cls.member_operators(op_name, allow_empty=True).exclude() # TODO confusing protected destructor compile errors
    
    def wrap_nodevisitor(self):
        cls = self.mb.class_("NodeVisitor")


    def wrap_gl_symbols(self):
        # Manually export #define constants
        # expose GL_ constants TODO - more of them
        for symbol in [ 
                "GL_ALPHA_TEST", 
                "GL_AUTO_NORMAL", 
                "GL_BLEND", 
                "GL_CLIP_PLANE0", 
                "GL_CLIP_PLANE1", 
                "GL_CLIP_PLANE2", 
                "GL_CLIP_PLANE3", 
                "GL_CLIP_PLANE4", 
                "GL_CLIP_PLANE5", 
                "GL_COLOR_LOGIC_OP", 
                "GL_COLOR_MATERIAL", 
                "GL_CULL_FACE", 
                "GL_DEPTH_TEST", 
                "GL_DITHER", 
                "GL_FOG", 
                "GL_INDEX_LOGIC_OP", 
                "GL_LIGHT0", 
                "GL_LIGHT1", 
                "GL_LIGHT2", 
                "GL_LIGHT3", 
                "GL_LIGHT4", 
                "GL_LIGHT5", 
                "GL_LIGHT6", 
                "GL_LIGHT7", 
                "GL_LIGHTING", 
                "GL_LINE_SMOOTH", 
                "GL_LINE_STIPPLE", 
                "GL_MAP1_COLOR_4", 
                "GL_MAP1_INDEX", 
                "GL_MAP1_NORMAL", 
                "GL_MAP1_TEXTURE_COORD_1", 
                "GL_MAP1_TEXTURE_COORD_2", 
                "GL_MAP1_TEXTURE_COORD_3", 
                "GL_MAP1_TEXTURE_COORD_4", 
                "GL_MAP1_VERTEX_3", 
                "GL_MAP1_VERTEX_4", 
                "GL_MAP2_COLOR_4", 
                "GL_MAP2_INDEX", 
                "GL_MAP2_NORMAL", 
                "GL_MAP2_TEXTURE_COORD_1", 
                "GL_MAP2_TEXTURE_COORD_2", 
                "GL_MAP2_TEXTURE_COORD_3", 
                "GL_MAP2_TEXTURE_COORD_4", 
                "GL_MAP2_VERTEX_3", 
                "GL_MAP2_VERTEX_4", 
                "GL_NORMALIZE", 
                "GL_POINT_SMOOTH", 
                "GL_POLYGON_OFFSET_FILL", 
                "GL_POLYGON_OFFSET_LINE", 
                "GL_POLYGON_OFFSET_POINT", 
                "GL_POLYGON_SMOOTH", 
                "GL_POLYGON_STIPPLE", 
                "GL_SCISSOR_TEST", 
                "GL_STENCIL_TEST", 
                "GL_TEXTURE_1D", 
                "GL_TEXTURE_2D", 
                "GL_TEXTURE_GEN_Q", 
                "GL_TEXTURE_GEN_R", 
                "GL_TEXTURE_GEN_S", 
                "GL_TEXTURE_GEN_T", 
                ]:
            self.mb.add_registration_code('''
                boost::python::scope().attr("%s") = %s;''' % (symbol, symbol))

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
        for fn_name in [
                # "accept", 
                # "ascend", 
                # "traverse",
                # "asTransform", # TODO wrap Transform
                "asTerrain", # TODO wrap Terrain
                # "asSwitch", # TODO wrap Switch
                # "asGroup", # TODO wrap Group
                # "getParent", 
                # "asGeode", # TODO wrap Geode
                # "asCamera", # TODO wrap Camera
                # "getParents", # TODO wrap Group
                ]:
            cls.member_functions(fn_name).exclude()
        cls.add_property( "stateSet", 
            cls.member_function("getOrCreateStateSet"),
            cls.member_function("setStateSet") )
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
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_operators("operator()").exclude()
    
    def wrap_uniform(self):
        unif = self.mb.class_("Uniform")
        unif.constructors(arg_types=[None, None]).exclude() # copy constructor
        # unif.member_operators("operator()").exclude() # because I don't want to wrap NodeVisitor yet...
        
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
        ref.noncopyable = True
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

if __name__ == "__main__":
    wrapper = OsgWrapper()
    wrapper.wrap()
