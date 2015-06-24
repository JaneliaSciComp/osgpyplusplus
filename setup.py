#!/bin/env python

"""
File: setup.py

Build script for osgpyplusplus python bindings for OpenSceneGraph.

Requires that boost.python and OpenSceneGraph be installed.
On windows, these dependencies must have been built with MSVC9/2008
(or whatever your python distribution was built with).

This script takes the generated code under src/<module_name>/generated_code
as given. This script is not capable of regenerating those binding
codes.

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
libraries = ['OpenThreads'] # OpenThreads library is used by all modules
package_data = []
cflags = [
    # Constructor for Matrixd takes more than 15 arguments...
    '-DBOOST_PYTHON_MAX_ARITY=18',]
if sys.platform == 'win32' :
    # TODO - find or set these values more generally
    OSG_DIR = "C:/Program Files (x86)/OpenSceneGraph321vs2008"
    include_dirs.extend( [
        'C:/boost/include/boost-1_56',
        OSG_DIR + '/include',
        ] )
    library_dirs.extend([
        OSG_DIR + '/lib',
        'C:/boost/lib',
        ])
    libraries.extend(['boost_python-vc90-mt-1_56',])
    # package_data.extend(glob(OSG_DIR + '/bin/osg*.dll')) # OpenSceneGraph libraries
    package_data.append(r'C:\\Program\ Files\ (x86)\\OpenSceneGraph321vs2008\\bin\\ot20-OpenThreads.dll') # OpenThreads libraries
    # package_data.extend(glob(os.path.join(OSG_DIR, 'bin', 'osgPlugins-3.2.1','osgdb*.dll'))) # File format plugins
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
for module_name in ['osgGA', 'osgDB', 'osgText', 'osgViewer']:
    moduleInfo[module_name]["libraries"].append('osgUtil')
for module_name in ['osgText', 'osgViewer']:
    moduleInfo[module_name]["libraries"].append('osgDB')
moduleInfo['osgViewer']["libraries"].append('osgGA')

# Create final list of extension modules
extension_modules = []
for module_name in ['osg', 'osgUtil', 'osgGA', 'osgDB', 'osgText', 'osgViewer']:
    extension_modules.append(Extension(
        # binary module name begins with underscore "_", so we can wrap module with a python file
        'osgpypp._%s' % module_name,
        moduleInfo[module_name]["source_files"],
        include_dirs=moduleInfo[module_name]["includes"],
        library_dirs=library_dirs,
        libraries=moduleInfo[module_name]["libraries"],
        extra_compile_args=cflags,        
        ))

print package_data

setup(name='osgpyplusplus',
      version='3.2.1.1',
      description='python bindings for OpenSceneGraph API, created using Boost.Python and pyplusplus',
      author='Christopher Bruns',
      author_email='brunsc@janelia.hhmi.org',
      maintainer='Christopher Bruns',
      maintainer_email='brunsc@janelia.hhmi.org',
      url='https://github.com/JaneliaSciComp/osgpyplusplus',
      # download_url='https://github.com/JaneliaSciComp/osgpyplusplus/releases',
      packages=['osgpypp',],
      package_dir={'osgpypp': 'src/osgpypp'},
      # package_data={'osgpypp': [r'C:/Program Files (x86)/OpenSceneGraph321vs2008/bin/ot*.dll',],},
      # data_files installs files right into Python27 folder...
      # data_files = [('osgpypp', glob(r'C:/Program Files (x86)/OpenSceneGraph321vs2008/bin/ot*.dll'))],
      ext_package='',
      ext_modules=extension_modules,
     )