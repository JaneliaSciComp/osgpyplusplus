from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *

class OsgUtilWrapper(BaseWrapper):
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgUtil.h",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        self.mb.register_module_dependency('../osg/generated_code/')
        self.mb.register_module_dependency('../osgDB/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgUtil = mb.namespace("osgUtil")
        osgUtil.include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osgUtil')).include()
        
        wrap_call_policies(self.mb)
        hide_nonpublic(mb)

        for cls_name in [
                ]:
            expose_ref_ptr_class(mb.class_(cls_name))
            

        for cls_name in [
                ]:
            ctor = mb.class_(cls_name).constructors(arg_types=[None, None])
            ctor.exclude()
            # ctor.add_transformation(FT.modify_type(1, remove_const_from_reference))

        self.mb.classes(lambda c: c.name.startswith("map<")).exclude()

        self.mb.build_code_creator(module_name='osgUtil')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
        
if __name__ == "__main__":
    wrapper = OsgUtilWrapper()
    wrapper.wrap()
