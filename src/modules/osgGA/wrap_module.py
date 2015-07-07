from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *

class OsgGAWrapper(BaseWrapper):
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgGA.h",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        if True:
            self.mb.register_module_dependency('../osgUtil/generated_code/')
            self.mb.register_module_dependency('../osgDB/generated_code/')
            self.mb.register_module_dependency('../osg/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgGA = mb.namespace("osgGA")
        osgGA.include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osgGA')).include()
        
        hide_nonpublic(mb)

        wrap_call_policies(self.mb)

        self.wrap_all_osg_referenced(osgGA)

        self.wrap_guieventadapter()
        self.wrap_cameramanipulator()
        self.wrap_standardmanipulator()
        # self.wrap_firstpersonmanipulator()
        self.wrap_manipulators()
        hack_osg_arg(
            self.mb.namespace("osgGA").class_("Device"),
            "sendEvent", "ea")

        for cls_name in [
                "GUIEventHandler",
                ]:
            for fn in osgGA.class_(cls_name).member_functions(lambda f: f.name.startswith("handle")):
                pass
                # fn.exclude()
                fn.add_transformation(FT.modify_type(0, remove_const_from_reference))
                # avoid ugly alias
                fn.transformations[-1].alias = fn.alias

        hack_osg_arg(osgGA.class_("Device"), "sendEvent", 0)

        fn = osgGA.class_("StateSetManipulator").member_function("handle")
        fn.add_transformation(FT.modify_type(0, remove_const_from_reference))

        # Write results
        self.generate_module_code("_osgGA")

    def wrap_cameramanipulator(self):
        for cls_name in ["CameraManipulator",]:
            cls = self.mb.namespace("osgGA").class_(cls_name)
            # Proof of concept for transforming all those compile errors
            # for const reference arguments with protected destructors
            hack_osg_arg(cls, "init", "arg0")
            hack_osg_arg(cls, "handle", "ea")
            hack_osg_arg(cls, "home", "arg0")

    def wrap_standardmanipulator(self):
        for cls_name in ["StandardManipulator",]:
            cls = self.mb.namespace("osgGA").class_(cls_name)
            cls.member_functions().include() # even protected ones...
            # Proof of concept for transforming all those compile errors
            # for const reference arguments with protected destructors
            hack_osg_arg(cls, "init", "ea")
            hack_osg_arg(cls, "handle", "ea")
            hack_osg_arg(cls, "home", "ea")
            # hack_osg_arg(cls, "performAnimationMovement", "ea")
            # hack_osg_arg(cls, "centerMousePointer", "ea")
            # hack_osg_arg(cls, "addMouseEvent", "ea")
            for cls_name in [
                    "addMouseEvent",
                    "centerMousePointer",
                    "handleFrame",
                    "handleKeyUp",
                    "handleKeyDown",
                    "handleMouseDeltaMovement",
                    "handleMouseDrag",
                    "handleMouseMove",
                    "handleMousePush",
                    "handleMouseRelease",
                    "handleMouseWheel",
                    "handleResize",
                    "performAnimationMovement",  
                    "performMouseDeltaMovement",
                    "performMovement", 
                    "setCenterByMousePointerIntersection", 
                    "startAnimationByMousePointerIntersection", 
                    ]:
                cls.member_function(cls_name).exclude()
            expose_overridable_ref_ptr_class(cls)

    def wrap_firstpersonmanipulator(self):
        fpm = self.mb.namespace("osgGA").class_("FirstPersonManipulator")
        fpm.add_declaration_code("""
            static int DEFAULT_SETTINGS = osgGA::FirstPersonManipulator::DEFAULT_SETTINGS;
            """)
        for cls_name in ["FirstPersonManipulator",]:
            cls = self.mb.namespace("osgGA").class_(cls_name)
            cls.member_functions().include() # even protected ones...
            # Proof of concept for transforming all those compile errors
            # for const reference arguments with protected destructors
            hack_osg_arg(cls, "init", "ea")
            # hack_osg_arg(cls, "handleMouseWheel", "ea")
            hack_osg_arg(cls, "handle", "ea")
            hack_osg_arg(cls, "home", "ea")
            # hack_osg_arg(cls, "centerMousePointer", "ea")
            # hack_osg_arg(cls, "addMouseEvent", "ea")        
            # hack_osg_arg(cls, "startAnimationByMousePointerIntersection", "ea")
            #
            cls.member_function("handleMouseWheel").exclude()
            # cls.member_function("addMouseEvent").exclude()
            cls.member_function("startAnimationByMousePointerIntersection").exclude()
            # Make class overridable, including callbacks from C++
            expose_overridable_ref_ptr_class(cls)

    def wrap_manipulators(self):
        # Avoid DEFAULT_SETTINGS compile error
        for cls_name in [
                "FirstPersonManipulator", 
                "FlightManipulator",
                "MultiTouchTrackballManipulator",
                "NodeTrackerManipulator",
                "OrbitManipulator", 
                "TerrainManipulator",
                "TrackballManipulator", 
                ]:
            cls = self.mb.namespace("osgGA").class_(cls_name)
            cls.add_declaration_code("""
                static int DEFAULT_SETTINGS = osgGA::%s::DEFAULT_SETTINGS;
                """ % cls_name)
        for cls_name in [
                "AnimationPathManipulator",
                "CameraViewSwitchManipulator",
                "DriveManipulator",
                "FirstPersonManipulator", 
                "FlightManipulator",
                "KeySwitchMatrixManipulator",
                "MultiTouchTrackballManipulator",
                "NodeTrackerManipulator",
                "OrbitManipulator", 
                "SphericalManipulator",
                "TerrainManipulator",
                "TrackballManipulator", 
                "UFOManipulator", 
                ]:
            cls = self.mb.namespace("osgGA").class_(cls_name)
            cls.member_functions().include() # even protected ones...
            # Proof of concept for transforming all those compile errors
            # for const reference arguments with protected destructors
            for fn_name in [
                    "init", 
                    "handle", 
                    "home", 
                    ]:
                hack_osg_arg(cls, fn_name, "ea")
                hack_osg_arg(cls, fn_name, "ee")
                hack_osg_arg(cls, fn_name, "arg0")
            for fn_name in [
                    "_frame",
                    "_keyDown",
                    "_keyUp",
                    "addMouseEvent", 
                    "flightHandleEvent", 
                    "handleFrame", 
                    "handleKeyDown", 
                    "handleMouseDrag",
                    "handleMouseMove",
                    "handleMousePush",
                    "handleMouseRelease",
                    "handleMouseWheel",
                    # "getUsage",  
                    "startAnimationByMousePointerIntersection", 
                    ]:
                cls.member_functions(fn_name, allow_empty=True).exclude()
            # Make class overridable, including callbacks from C++
            expose_overridable_ref_ptr_class(cls)

    def wrap_guieventadapter(self):
        cls = self.mb.class_("GUIEventAdapter")
        for ctor in cls.constructors():
            ctor.allow_implicit_conversion = False
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_function("copyPointerDataFrom").exclude()
        
        td = cls.class_("TouchData")
        expose_ref_ptr_class(td)
        td.constructors(arg_types=[None, None]).exclude()
        # td.member_function("libraryName").exclude()
        
if __name__ == "__main__":
    wrapper = OsgGAWrapper()
    wrapper.wrap()
