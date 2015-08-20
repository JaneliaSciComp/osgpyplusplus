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

class OsgParticleWrapper(BaseWrapper):
    "Class that knows how to generate code for osgParticle python module"
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgParticle.h",])
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
            self.mb.register_module_dependency('../osgFX/generated_code/') # Included to linearize dependency chain
            self.mb.register_module_dependency('../osgVolume/generated_code/') # Included to linearize dependency chain
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgParticle = mb.namespace("osgParticle")
        osgParticle.include()

        # mb.free_functions(lambda f: f.name.startswith("osgParticle")).include() # no free functions!

        wrap_call_policies(self.mb)

        self.wrap_all_osg_referenced(osgParticle)
            
        hide_nonpublic(mb)
                
        
        # 2>c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\include\utility(35) : error C2512: 'osgParticle::PrecipitationEffect::PrecipitationDrawable::Cell::Cell' : no appropriate default constructor available
        mb.class_(lambda c: c.alias == "CellMatrixMap").exclude()
        mb.class_("PrecipitationEffect").member_functions("getCurrentCellMatrixMap").exclude()
        mb.class_("PrecipitationEffect").member_functions("getPreviousCellMatrixMap").exclude()
        
        
        self.generate_module_code('_osgParticle')

if __name__ == "__main__":
    wrapper = OsgParticleWrapper()
    wrapper.wrap()
