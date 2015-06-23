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

        self.wrap_all_osg_referenced(osgViewer)

        for cls in mb.classes(lambda c: c.name.endswith("Handler")):
            cls.member_functions("handle", allow_empty=True).exclude()
            cls.noncopyable = True
            
        self.wrap_viewerbase()
        self.wrap_view()
        self.wrap_keystone()
        self.wrap_screencapturehandler()

        # Should not be needed, due to register_module_dependency...
        # mb.namespace("osgGA").class_("GUIEventHandler").already_exposed = True
            
        hide_nonpublic(mb)
        
        self.mb.build_code_creator(module_name='osgViewer')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()

    def wrap_screencapturehandler(self):
        cls = self.mb.class_("ScreenCaptureHandler")
        cls.member_operators("operator()").exclude()
        co = cls.class_("CaptureOperation")
        # co.exclude()
        
    def wrap_keystone(self):
        ks = self.mb.class_("Keystone")
        ks.member_operator("operator=").exclude()
        ks.constructors(arg_types=[None, None]).exclude()
        
        ksh = self.mb.class_("KeystoneHandler")
        for fn_name in ["handle", "computeRegion", "incrementScale"]:
            ksh.member_functions(fn_name).exclude()
    
    def wrap_viewerbase(self):
        vb = self.mb.class_("ViewerBase")
        vb.constructors().exclude()
        vb.noncopyable = True
        vb.no_init = True
        
    def wrap_view(self):
        cls = self.mb.namespace("osgViewer").class_("View")
        for ctor in cls.constructors():
            ctor.allow_implicit_conversion = False
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_functions("computeIntersections").exclude()
        cls.class_("StereoSlaveCallback").member_function("updateSlave").exclude() # link error
        # Move output arguments to return value tuple
        if False: # TODO - transformation does not seem to work with protected destructor classes
            gccp = cls.member_function("getCameraContainingPosition")
            gccp.add_transformation(FT.output('local_x'), FT.output('local_y'),)
        # Avoid premature destruction of manipulator
        cls.member_function("setCameraManipulator").call_policies = with_custodian_and_ward(1, 2)


if __name__ == "__main__":
    wrapper = OsgViewerWrapper()
    wrapper.wrap()
