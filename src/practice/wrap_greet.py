from pyplusplus import module_builder
import os

gccxml_executable = "C:/Program Files (x86)/gccxml/bin/gccxml.exe"
include_dir = "F:/Users/cmbruns/git/osgpyplusplus/src/practice"
includes = ["greet.h",]
mb = module_builder.module_builder_t(
    files = includes,
    gccxml_path = gccxml_executable,
    include_paths = [include_dir])
mb.build_code_creator(module_name='greet')
mb.write_module(os.path.join(os.path.abspath('.'), 'generated_code', 'greet_wrapped.cpp'))

print dir(mb)
