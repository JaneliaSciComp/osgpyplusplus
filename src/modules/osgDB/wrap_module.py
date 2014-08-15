from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os

class OsgDBWrapper:
    def __init__(self):
        self.mb = module_builder.module_builder_t(
            files = ["wrap_osgdb.h",],
            gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe",
            include_paths = ["C:/Program Files (x86)/OpenSceneGraph321vs2008/include",])
        # Don't rewrap anything already wrapped by simtk.common etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        self.mb.register_module_dependency('../osg/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgDB = mb.namespace("osgDB")
        osgDB.include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osgDB')).include()
        
        self.mb.build_code_creator(module_name='osgDB')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()

if __name__ == "__main__":
    wrapper = OsgDBWrapper()
    wrapper.wrap()
