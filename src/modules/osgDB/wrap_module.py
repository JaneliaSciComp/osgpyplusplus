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
                ]:
            for fn in mb.free_functions(fn_name):
                fn.call_policies = return_value_policy(reference_existing_object)
        mb.free_functions("fopen").exclude()
        
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
        
        self.mb.build_code_creator(module_name='osgDB')
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
        input = self.mb.class_("Input")
        for fn_name in [
                "getObjectForUniqueID",
                "readObject",
                "readObjectOfType",
                "registerUniqueIDForObject",
                    ]:
            input.member_functions(fn_name).exclude()
    
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
