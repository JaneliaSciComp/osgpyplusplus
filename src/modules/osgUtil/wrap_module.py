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
            
    def wrap(self):
        mb = self.mb
        
        # Wrap everything in the "osg" namespace
        osgUtil = mb.namespace("osgUtil")
        osgUtil.include()

        # Wrap methods that begin with "osg", even if not in osg namespace
        mb.free_functions(lambda f: f.name.startswith('osgUtil')).include()
        
        wrap_call_policies(self.mb)

        self.wrap_all_osg_referenced(osgUtil)

        hide_nonpublic(mb)

        self.mb.classes(lambda c: c.name.startswith("map<")).exclude()

        cullVisitor = osgUtil.class_("CullVisitor")
        for fn_name in [
                "computeFurthestPointInFrustum",
                "computeNearestPointInFrustum",
                "updateCalculatedNearFar",
                ]:
            cullVisitor.member_functions(fn_name).exclude()
        cullVisitor.constructors(arg_types=[None]).exclude()
        cullVisitor.noncopyable = True

        self.mb.class_("IncrementalCompileOperation").variables("_compileMap").exclude()
        self.mb.class_("Optimizer").variables("_billboards").exclude()
        self.mb.class_("StateGraph").variables("_children").exclude()

        for cls_name in [
                "IntersectorGroup", 
                "Intersector", 
                "LineSegmentIntersector", 
                "PlaneIntersector", 
                "PolytopeIntersector", 
                ]:
            cls = self.mb.class_(cls_name)
            hack_osg_arg(cls, "enter", "node")

        for fn_name in [
                "create3DNoiseImage", 
                "create3DNoiseTexture",
                ]:
            for fn in self.mb.free_functions(fn_name):
                # Because "manage_new_object" causes trouble with protected destructors, so let's leak this memory
                fn.call_policies = return_value_policy(reference_existing_object)

        self.mb.build_code_creator(module_name='_osgUtil')
        self.mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))
        # Create a file to indicate completion of wrapping script
        open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
        
if __name__ == "__main__":
    wrapper = OsgUtilWrapper()
    wrapper.wrap()
