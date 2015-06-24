#!/bin/env python

"""
File: setup.py

Build script for osgpyplusplus python bindings for OpenSceneGraph.

Requires that boost.python and OpenSceneGraph be installed.
On windows, these dependencies must have been built with MSVC9/2008
(or whatever your python distribution was built with).

If necessary, regenerate the binding source code using CMake.
(For example, if you have added features to the bindings).
"""

from distutils.core import setup
from distutils.extension import Extension
from glob import glob
import os
import sys

# Populate build parameters shared by all modules
include_dirs = ['src/modules',]
library_dirs = []
libraries = ['OpenThreads'] # OSG library is used by all modules
cflags = [
    # Constructor for Matrixd takes more than 15 arguments...
    '-DBOOST_PYTHON_MAX_ARITY=18',]
if sys.platform == 'win32' :
    # TODO - find or set these values more generally
    include_dirs.extend( [
        'C:/boost/include/boost-1_56',
        'C:/Program Files (x86)/OpenSceneGraph321vs2008/include',
        ] )
    library_dirs.extend([
        'C:/Program Files (x86)/OpenSceneGraph321vs2008/lib',
        'C:/boost/lib',
        ])
    libraries.extend(['boost_python-vc90-mt-1_56',])
    cflags.append('/EHsc') # Avoid compiler warning about exception handling

# Per-module parameters
# Create one python module for each OpenSceneGraph namespace
moduleInfo = dict()
for module_name in ['osg', 'osgUtil', 'osgGA', 'osgDB', 'osgText', 'osgViewer']:
    moduleInfo[module_name] = dict()
    mi = moduleInfo[module_name]
    mi["source_files"] = glob(os.path.join('src','modules',module_name,'generated_code','*.cpp'))
    mi["includes"] = [
        'src/modules/%s' % module_name,
        'src/modules/%s/generated_code' % module_name,
        ]
    mi["includes"].extend(include_dirs)
    mi["libraries"] = [module_name] # assume osg C++ library has same name
    mi["libraries"].extend(libraries)
# Append module specific libraries
for module_name in ['osgUtil', 'osgGA', 'osgDB', 'osgText', 'osgViewer']:
    moduleInfo[module_name]["libraries"].append('osg')
# TODO - build other modules: osgGA, osgViewer, etc.

# Create final list of extension modules
extension_modules = []
for module_name in ['osgUtil']:
    extension_modules.append(Extension(
        'osgpypp.%s' % module_name,
        moduleInfo[module_name]["source_files"],
        include_dirs=moduleInfo[module_name]["includes"],
        library_dirs=library_dirs,
        libraries=moduleInfo[module_name]["libraries"],
        extra_compile_args=cflags,        
        ))

setup(name='osgpyplusplus',
      version='3.2.1.1',
      description='python bindings for OpenSceneGraph API, created using Boost.Python and pyplusplus',
      author='Christopher Bruns',
      author_email='brunsc@janelia.hhmi.org',
      packages=['osgpypp',],
      package_dir={'osgpypp': 'src/osgpypp'},
      ext_package='osgpypp',
      ext_modules=extension_modules,
     )