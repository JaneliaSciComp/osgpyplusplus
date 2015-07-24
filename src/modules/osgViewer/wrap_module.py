from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *


class OsgViewerWrapper(BaseWrapper):
    "Class that knows how to generate code for osgViewer python module"
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgViewer.h",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        # For base classes to be properly referenced, we really need to register all of the dependencies...
        if True:
            self.mb.register_module_dependency('../osgText/generated_code/')
            self.mb.register_module_dependency('../osgUtil/generated_code/')
            self.mb.register_module_dependency('../osgGA/generated_code/')
            self.mb.register_module_dependency('../osgDB/generated_code/')
            self.mb.register_module_dependency('../osg/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgViewer = mb.namespace("osgViewer")
        osgViewer.include()

        mb.free_functions(lambda f: f.name.startswith("osgViewer")).include()

        wrap_call_policies(self.mb)

        # self.wrap_all_osg_referenced_noderive(osgViewer)
        self.wrap_all_osg_referenced(osgViewer)
        
        # Avoid infinite recursion runtime error by making some classes
        # non-overridable
        for cls_name in ["GraphicsWindowEmbedded", "Viewer", ]:
            expose_nonoverridable_ref_ptr_class(osgViewer.class_(cls_name))

        for cls in mb.classes(lambda c: c.name.endswith("Handler")):
            cls.member_functions("handle", allow_empty=True).exclude()
            cls.noncopyable = True
            
        self.wrap_viewerbase()
        self.wrap_view()
        self.wrap_keystone()
        self.wrap_screencapturehandler()
        
        # Handles all remaining W1009 warnings.
        # execution error W1009: The function takes as argument...
        osgViewer.class_("GraphicsWindow").member_function(
                "getWindowRectangle").add_transformation(
                    FT.output("x"),
                    FT.output("y"),
                    FT.output("width"),
                    FT.output("height"))
        osgViewer.class_("GraphicsWindow").member_function(
                "getSwapGroup").add_transformation(
                    FT.output("on"),
                    FT.output("group"),
                    FT.output("barrier"))
        osgViewer.class_("View").member_function(
                "getCameraContainingPosition").exclude()
                # .add_transformation(FT.output("local_x"), FT.output("local_y"))
        osgViewer.class_("DepthPartitionSettings").member_function(
                "getDepthRange").add_transformation(
                    # FT.output("view"),
                    FT.output("zNear"),
                    FT.output("zFar"))

        hide_nonpublic(mb)
        
        self.mb.build_code_creator(module_name='_osgViewer')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()

    def wrap_screencapturehandler(self):
        cls = self.mb.class_("ScreenCaptureHandler")
        # cls.member_operators("operator()").exclude()
        # co = cls.class_("CaptureOperation")
        # co.exclude()
        for cls_name in ["CaptureOperation", "WriteToFile", ]:
            wtf = cls.class_(cls_name)
            call_op = wtf.member_operator("operator()")
            call_op.add_transformation(FT.modify_type("image", remove_const_from_reference))
            xform = call_op.transformations[-1]
            xform.alias = "__call__"
            xform.unique_name = xform.unique_name.replace("operator()", "operator_call")
        
    def wrap_keystone(self):
        ks = self.mb.class_("Keystone")
        ks.member_operator("operator=").exclude()
        ks.constructors(arg_types=[None, None]).exclude()
        
        ksh = self.mb.class_("KeystoneHandler")
        for fn_name in ["handle", "computeRegion", "incrementScale"]:
            ksh.member_functions(fn_name).exclude()
        # 1>..\..\..\..\src\modules\osgViewer\generated_code\KeystoneHandler.pypp.cpp(13) : error C2065: 'KeystoneHandler_wrapper' : undeclared identifier
        expose_nonoverridable_ref_ptr_class(ksh)
    
    def wrap_viewerbase(self):
        vb = self.mb.class_("ViewerBase")
        vb.constructors().exclude()
        vb.noncopyable = True
        vb.no_init = True
        vb.member_function("getWindows").add_transformation(FT.output("windows"))
        vb.member_function("getViews").add_transformation(FT.output("views"))
        
    def wrap_view(self):
        cls = self.mb.namespace("osgViewer").class_("View")
        for ctor in cls.constructors():
            ctor.allow_implicit_conversion = False
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_functions("computeIntersections").exclude()
        # RuntimeWarning: to-Python converter for class osg::ref_ptr<struct View_wrapper> already registered; second conversion method ignored.
        expose_nonoverridable_ref_ptr_class(cls)
        inner = cls.class_("StereoSlaveCallback")
        inner.member_function("updateSlave").exclude() # link error
        # 1>..\..\..\..\src\modules\osgViewer\generated_code\View.pypp.cpp(171) : error C2039: 'StereoSlaveCallback_wrapper' : is not a member of 'View_wrapper'
        expose_nonoverridable_ref_ptr_class(inner)
        # Move output arguments to return value tuple
        if False: # TODO - transformation does not seem to work with protected destructor classes
            gccp = cls.member_function("getCameraContainingPosition")
            gccp.add_transformation(FT.output('local_x'), FT.output('local_y'),)
        # Avoid premature destruction of manipulator
        # WEIRD movie maker crashes when I use (2, 1) here but not (1, 2)
        # BUT also crashes when osg.Camera.setFinalDrawCallback() uses (1, 2) but not (2, 1).
        # Whatever
        cls.member_function("setCameraManipulator").call_policies = with_custodian_and_ward(1, 2) # not crash
        # cls.member_function("setCameraManipulator").call_policies = with_custodian_and_ward(2, 1) # crashes at runtime


if __name__ == "__main__":
    wrapper = OsgViewerWrapper()
    wrapper.wrap()
