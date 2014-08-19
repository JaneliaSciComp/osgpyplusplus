from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *

class OsgDBWrapper:
    def __init__(self):
        self.mb = module_builder.module_builder_t(
            files = ["wrap_osgdb.h",],
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        self.mb.register_module_dependency('../osg/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgDB = mb.namespace("osgDB")
        osgDB.include()

        osgDB.classes().exclude() # TODO - wrap more classes
        
        osgDB.free_functions().exclude()

        wrap_call_policies(self.mb)
        
        # Call policies for clone methods
        for fn in mb.member_functions(lambda f: re.search(r'^clone', f.name)):
            rt = fn.return_type
            if not declarations.is_pointer(fn.return_type):
                continue
            fn.call_policies = return_value_policy(reference_existing_object)
        # Call policies for getter methods
        for fn in mb.member_functions(lambda f: re.search(r'^get[A-Z]', f.name)):
            rt = fn.return_type
            if fn.return_type.decl_string == "char const *":
                continue # use default for strings
            if declarations.is_pointer(fn.return_type):
                pass
            elif declarations.is_reference(fn.return_type):
                pass
            else:
                continue # use default for non-reference/pointer
            fn.call_policies = return_internal_reference()

        self.wrap_options()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osgDB')).include()
        
        for fn in mb.free_functions("readNodeFile"):
            fn.include()
            fn.call_policies = return_value_policy(reference_existing_object)
        
        self.mb.build_code_creator(module_name='osgDB')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
    
    def wrap_options(self):
        cls = self.mb.class_("Options")
        cls.include()
        expose_ref_ptr_class(cls)
        for ctor in cls.constructors():
            ctor.allow_implicit_conversion = False
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_functions("getPluginData").exclude()
        cls.member_functions("className").exclude()

if __name__ == "__main__":
    wrapper = OsgDBWrapper()
    wrapper.wrap()
