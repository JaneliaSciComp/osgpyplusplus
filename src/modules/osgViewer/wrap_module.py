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
    def __init__(self):
        self.mb = module_builder.module_builder_t(
            files = ["wrap_osgViewer.h",],
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        self.mb.register_module_dependency('../osg/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgViewer = mb.namespace("osgViewer")
        osgViewer.include()

        mb.free_functions(lambda f: f.name.startswith("osgViewer")).include()
        
        osgViewer.classes().exclude() # TODO - wrap more classes

        wrap_call_policies(self.mb)

        self.wrap_viewer()
        self.wrap_view()
            
        hide_nonpublic(mb)
        
        self.mb.build_code_creator(module_name='osgViewer')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
    
    def wrap_viewer(self):
        cls = self.mb.class_("Viewer")
        cls.include()
        expose_ref_ptr_class(cls)

    def wrap_view(self):
        cls = self.mb.namespace("osgViewer").class_("View")
        cls.include()
        expose_ref_ptr_class(cls)
        for ctor in cls.constructors():
            ctor.allow_implicit_conversion = False
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_functions("computeIntersections").exclude()
        cls.class_("StereoSlaveCallback").member_function("updateSlave").exclude() # link error

if __name__ == "__main__":
    wrapper = OsgViewerWrapper()
    wrapper.wrap()
