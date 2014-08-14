from pyplusplus import module_builder
import os

mb = module_builder.module_builder_t(
    files = ["greet.h",],
    gccxml_path = "C:/Program Files (x86)/gccxml/bin/gccxml.exe")
mb.build_code_creator(module_name='greet')
mb.split_module(os.path.join(os.path.abspath('.'), 'generated_code'))

# Create a file to indicate completion of wrapping script
open(os.path.join(os.path.abspath('.'), 'generated_code', 'generate_module.stamp'), "w").close()
