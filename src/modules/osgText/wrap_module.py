from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *

class OsgTextWrapper(BaseWrapper):
    "Class that knows how to generate code for osgText python module"
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgText.h",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        # For base classes to be properly referenced, we really need to register all of the dependencies...
        self.mb.register_module_dependency('../osgDB/generated_code/')
        self.mb.register_module_dependency('../osg/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgText = mb.namespace("osgText")
        osgText.include()

        mb.free_functions(lambda f: f.name.startswith("osgText")).include()

        wrap_call_policies(self.mb)

        self.wrap_all_osg_referenced(osgText)
            
        hide_nonpublic(mb)

        osgText.free_function("readFontFile").call_policies = return_value_policy(reference_existing_object)
        osgText.free_function("readFontStream").call_policies = return_value_policy(reference_existing_object)
        osgText.class_("GlyphTexture").member_functions("compare").exclude()
        
        self.generate_module_code('osgText')

if __name__ == "__main__":
    wrapper = OsgTextWrapper()
    wrapper.wrap()
