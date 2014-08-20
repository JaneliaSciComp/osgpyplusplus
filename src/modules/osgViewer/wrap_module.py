from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *

class OsgViewerWrapper:
    "Class that knows how to generate code for osgViewer python module"
    def __init__(self):
        self.mb = module_builder.module_builder_t(
            files = ["wrap_osgViewer.h",],
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        self.mb.register_module_dependency('../osg/generated_code/')
        self.mb.register_module_dependency('../osgGA/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgViewer = mb.namespace("osgViewer")
        osgViewer.include()

        mb.free_functions(lambda f: f.name.startswith("osgViewer")).include()
        
        # osgViewer.classes().exclude() # TODO - wrap more classes

        wrap_call_policies(self.mb)

        # Use ref_ptr<> held-type for classes derived from osg::Referenced
        for cls_name in ["ViewerBase", 
                "Viewer", 
                "View", 
                "Keystone", 
                "ViewConfig", 
                "CompositeViewer",]:
            cls = self.mb.namespace("osgViewer").class_(cls_name)
            expose_ref_ptr_class(cls)
        for cls in mb.classes(lambda c: c.name.endswith("Handler")):
            expose_ref_ptr_class(cls)
            cls.member_functions("handle", allow_empty=True).exclude()
            cls.noncopyable = True
            
        self.wrap_viewerbase()
        self.wrap_view()
        self.wrap_keystone()
        self.wrap_screencapturehandler()
            
        hide_nonpublic(mb)
        
        self.mb.build_code_creator(module_name='osgViewer')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()

    def wrap_screencapturehandler(self):
        cls = self.mb.class_("ScreenCaptureHandler")
        cls.member_operators("operator()").exclude()
        co = cls.class_("CaptureOperation")
        co.exclude()
        
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


if __name__ == "__main__":
    wrapper = OsgViewerWrapper()
    wrapper.wrap()
