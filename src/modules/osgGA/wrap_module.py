from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *

class OsgGAWrapper:
    def __init__(self):
        self.mb = module_builder.module_builder_t(
            files = ["wrap_osgGA.h",],
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        self.mb.register_module_dependency('../osg/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgGA = mb.namespace("osgGA")
        osgGA.include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osgGA')).include()
        
        wrap_call_policies(self.mb)
        hide_nonpublic(mb)

        for cls_name in ["PointerData", "GUIEventAdapter"]:
            expose_ref_ptr_class(mb.class_(cls_name))
            
        self.wrap_guieventadapter()

        self.mb.build_code_creator(module_name='osgGA')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()

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
