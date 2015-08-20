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

class OsgSimWrapper(BaseWrapper):
    "Class that knows how to generate code for osgSim python module"
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgSim.h",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        # For base classes to be properly referenced, we really need to register all of the dependencies...
        self.mb.register_module_dependency('../osg/generated_code/')
        self.mb.register_module_dependency('../osgText/generated_code/') # vector<Vec4f>
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
        osgSim = mb.namespace("osgSim")
        osgSim.include()

        # mb.free_functions(lambda f: f.name.startswith("osgSim")).include() # no free functions!

        wrap_call_policies(self.mb)

        self.wrap_all_osg_referenced(osgSim)
            
        hide_nonpublic(mb)
        
        
        # 1>C:\boost\include\boost-1_56\boost/python/detail/destroy.hpp(33) : error C2248: 'osgSim::ShapeAttributeList::~ShapeAttributeList' : cannot access protected member declared in class 'osgSim::ShapeAttributeList'
        cls = osgSim.class_("ShapeAttributeList")
        cls.member_functions("compare").exclude()
        # hack_osg_arg(cls, "compare", "inst")
        
        # 1>..\..\..\..\src\modules\osgSim\generated_code\ImpostorSpriteManager.pypp.cpp(12) : error C2065: 'ImpostorSpriteManager_wrapper' : undeclared identifier
        for cls_name in ["GeographicLocation", "ImpostorSpriteManager", ]:
            cls = osgSim.class_(cls_name)
            cls.held_type = 'osg::ref_ptr< %s >' % cls.decl_string # no wrapper class...
            
        # 2>F:\Users\cmbruns\git\osgpyplusplus\src\modules\osgSim\generated_code\vector_less__osg_scope_ref_ptr_less_osg_scope_TemplateArray_less_osg_scope_Vec3f_comma__Vec3ArrayType_comma__3_comma__5126_greater___greater___greater_.pypp.cpp(13) : error C2065: 'Vec3ArrayType' : undeclared identifier
        for fn in osgSim.class_("SphereSegment").member_functions("computeIntersection"):
            fn.exclude()
        
        # 1>..\..\..\..\src\modules\osgSim\generated_code\ScalarBar.pypp.cpp(54) : error C2059: syntax error : '<'
        osgSim.class_("ScalarBar").constructors(arg_types=[None]*7).exclude()
        
        # 1>C:\boost\include\boost-1_56\boost/python/object/make_instance.hpp(27) : error C2664: 'boost::mpl::assertion_failed' : cannot convert parameter 1 from 'boost::mpl::failed ************boost::mpl::or_<T1,T2>::* ***********' to 'boost::mpl::assert<false>::type'
        # osgSim.class_("GeographicLocation").no_init = True
        # osgSim.class_("GeographicLocation").constructors().exclude()
        osgSim.class_("GeographicLocation").exclude()
        
        # 1>..\..\..\..\src\modules\osgSim\generated_code\vector_vector_bool.pypp.cpp(7) : fatal error C1083: Cannot open include file: '_vector_bool__value_traits.pypp.hpp': No such file or directory
        for fn_name in ["getSwitchSetList", "getValueList", "setSwitchSetList", "setValueList", ]:
            osgSim.class_("MultiSwitch").member_functions(fn_name).exclude()
            
        # 1>..\..\..\..\src\modules\osgSim\generated_code\DistanceHeightList.pypp.cpp(7) : fatal error C1083: Cannot open include file: '_pair_double_double__value_traits.pypp.hpp': No such file or directory
        osgSim.class_("ElevationSlice").member_function("getDistanceHeightIntersections").exclude()

        
        self.generate_module_code('_osgSim')

if __name__ == "__main__":
    wrapper = OsgSimWrapper()
    wrapper.wrap()
