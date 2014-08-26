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
        self.mb.register_module_dependency('../osgDB/generated_code/')
            
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

        for cls_name in [
                "GUIEventHandler",
                ]:
            osgGA.class_(cls_name).member_functions(
                lambda f: f.name.startswith("handle")).exclude()

        hack_osg_arg(osgGA.class_("Device"), "sendEvent", 0)

        self.mb.build_code_creator(module_name='osgGA')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()

    def wrap_cameramanipulator(self):
        cm = self.mb.namespace("osgGA").class_("CameraManipulator")
        # Proof of concept for transforming all those compile errors
        # for const reference arguments with protected destructors
        hack_osg_arg(cm, "init", "arg0")
        hack_osg_arg(cm, "handle", "ea")
        hack_osg_arg(cm, "home", "arg0")

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
