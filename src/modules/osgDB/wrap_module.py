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

class OsgDBWrapper(BaseWrapper):
    def __init__(self):
        BaseWrapper.__init__(self, files=["wrap_osgdb.h",])
        # Don't rewrap anything already wrapped by osg etc.
        # See http://www.language-binding.net/pyplusplus/documentation/multi_module_development.html
        self.mb.register_module_dependency('../osg/generated_code/')
        self.mb.register_module_dependency('../osgUtil/generated_code/')
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgDB = mb.namespace("osgDB")
        osgDB.include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osgDB')).include()
        
        wrap_call_policies(self.mb)

        hide_nonpublic(self.mb)
        
        self.wrap_all_osg_referenced(osgDB)

        self.wrap_options()
        self.wrap_input()
        self.wrap_imagepager()
        self.wrap_databasepager()
        
        osgDB.class_("Output").member_function("writeObject").exclude()
        osgDB.class_("BaseSerializer").member_function("write").exclude()
        osgDB.class_("ObjectWrapper").member_function("write").exclude()
        osgDB.class_("Field").member_function("takeStr").exclude()

        hack_osg_arg(osgDB.class_("ExternalFileWriter"), "write", "obj")

        for fn_name in [
                "getDataFilePathList",
                "getLibraryFilePathList",
                "openArchive",
                "readHeightFieldFile", 
                "readImageFile", 
                "readNodeFile", 
                "readNodeFiles", 
                "readObjectFile", 
                "readShaderFile", 
                "readXmlFile", 
                "readXmlStream", 
                ]:
            for fn in mb.free_functions(fn_name):
                fn.call_policies = return_value_policy(reference_existing_object)
        mb.free_functions("fopen").exclude()
        mb.free_functions("writeShaderFile").exclude()
        mb.free_functions("writeImageFile").exclude()
        mb.free_functions("writeNodeFile").exclude()
        mb.free_functions("writeObjectFile").exclude()
        mb.free_functions("writeShaderFile").exclude()
        mb.free_functions("writeHeightFieldFile").exclude()
        
        # Exclude difficult classe for now
        for cls_name in [
                "Archive",
                "DatabaseRevision",
                "DatabaseRevisions",
                "DeprecatedDotOsgWrapperManager",
                "FileCache",
                "FileList",
                "ReaderWriter",
                "Registry",
                "SharedStateManager",
                "WriteFileCallback",
                ]:
            osgDB.classes(cls_name).exclude()
        osgDB.classes(lambda c: c.name.startswith("TemplateSerializer<")).exclude()
        
        self.mb.build_code_creator(module_name='_osgDB')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
    
    def wrap_databasepager(self):
        databasepager = self.mb.class_("DatabasePager")
        databasepager.constructors(arg_types=[None]).exclude()
        databasepager.noncopyable = True
        databasethread = databasepager.class_("DatabaseThread")
        expose_ref_ptr_class(databasethread)
        databasethread.constructors(arg_types=[None, None]).exclude()
        databasepager.member_functions("removeExpiredChildren").exclude()
    
    def wrap_imagepager(self):
        imagepager = self.mb.class_("ImagePager")
        imagethread = imagepager.class_("ImageThread")
        expose_ref_ptr_class(imagethread)
        imagethread.constructors(arg_types=[None, None]).exclude()
    
    def wrap_input(self):
        for cls in self.mb.classes("Input"):
            for fn_name in [
                    "getObjectForUniqueID",
                    "readObject",
                    "readObjectOfType",
                    "registerUniqueIDForObject",
                        ]:
                cls.member_functions(fn_name, allow_empty=True).exclude()
    
    def wrap_options(self):
        cls = self.mb.class_("Options")
        for ctor in cls.constructors():
            ctor.allow_implicit_conversion = False
        cls.constructors(arg_types=[None, None]).exclude()
        cls.member_functions("getPluginData").exclude()
        cls.member_functions("className").exclude()

if __name__ == "__main__":
    wrapper = OsgDBWrapper()
    wrapper.wrap()
