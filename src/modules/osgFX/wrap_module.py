# Copyright (c) 2014, Howard Hughes Medical Institute, All rights reserved.
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright notice, 
#   this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation 
#   and/or other materials provided with the distribution.
#   * Neither the name of the Howard Hughes Medical Institute nor the names of 
#   its contributors may be used to endorse or promote products derived from 
#   this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, ANY 
# IMPLIED WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, OR FITNESS FOR A 
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# REASONABLE ROYALTIES; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pyplusplus import module_builder
from pyplusplus.module_builder.call_policies import *
from pyplusplus import function_transformers as FT
from pygccxml import declarations
import os
import sys
import re

sys.path.append("..")
from wrap_helpers import *

class OsgFXWrapper(BaseWrapper):
    "Class that knows how to generate code for osgFX python module"
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgFX.h",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        # For base classes to be properly referenced, we really need to register all of the dependencies...
        self.mb.register_module_dependency('../osg/generated_code/')
        if False: # Temporarily set to False for faster iterations during initial development
            self.mb.register_module_dependency('../osgUtil/generated_code/')
            self.mb.register_module_dependency('../osgDB/generated_code/')
            self.mb.register_module_dependency('../osgGA/generated_code/') # Included to linearize dependency chain
            self.mb.register_module_dependency('../osgViewer/generated_code/') # Included to linearize dependency chain
            self.mb.register_module_dependency('../osgManipulator/generated_code/') # Included to linearize dependency chain
            self.mb.register_module_dependency('../osgWidget/generated_code/') # Included to linearize dependency chain
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgFX = mb.namespace("osgFX")
        osgFX.include()

        mb.free_functions(lambda f: f.name.startswith("osgFX")).include()

        wrap_call_policies(self.mb)

        self.wrap_all_osg_referenced(osgFX)
            
        hide_nonpublic(mb)

        cls = osgFX.class_("Validator").member_function("compare").exclude()

        # RuntimeWarning: to-Python converter for class osg::ref_ptr<struct Registry_wrapper> already registered; second conversion method ignored.
        osgFX.class_("Registry").exclude()

        self.generate_module_code('_osgFX')

if __name__ == "__main__":
    wrapper = OsgFXWrapper()
    wrapper.wrap()
