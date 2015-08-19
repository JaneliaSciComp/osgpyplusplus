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
    "Class that knows how to generate code for osgVolume python module"
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgVolume.h",])
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
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgVolume = mb.namespace("osgVolume")
        osgVolume.include()

        mb.free_functions(lambda f: f.name.startswith("osgVolume")).include()

        wrap_call_policies(self.mb)

        self.wrap_all_osg_referenced(osgVolume)
            
        hide_nonpublic(mb)

        # 1>C:\boost\include\boost-1_56\boost/python/detail/caller.hpp(223) : error C2027: use of undefined type 'boost::python::detail::specify_a_return_value_policy_to_wrap_functions_returning<T>'
        # I would prefer to use "manage_new_object", but that results in another error:
        # 2>c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\include\memory(718) : error C2248: 'osg::Image::~Image' : cannot access protected member declared in class 'osg::Image'
        for fn_name in ["applyTransferFunction", "createNormalMapTexture", ]:
            osgVolume.free_functions(fn_name).call_policies = return_value_policy(reference_existing_object)

        # 1>C:\boost\include\boost-1_56\boost/python/detail/destroy.hpp(33) : error C2248: 'osgGA::GUIEventAdapter::~GUIEventAdapter' : cannot access protected member declared in class 'osgGA::GUIEventAdapter'
        cls = osgVolume.class_("PropertyAdjustmentCallback")
        hack_osg_arg(cls, "handle", "ea")

        self.generate_module_code('_osgVolume')

if __name__ == "__main__":
    wrapper = OsgFXWrapper()
    wrapper.wrap()
