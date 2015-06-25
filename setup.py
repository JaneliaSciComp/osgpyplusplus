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
from shutil import copy
from glob import glob
import os
import sys

# Populate build parameters shared by all modules
include_dirs = ['src/modules',]
library_dirs = []
libraries = ['OpenThreads'] # OpenThreads library is used by all modules
shared_libraries = []
plugin_libraries = []
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
    #
    debug_libs = set(glob(OSG_DIR+'/bin/o*d.dll'))
    release_libs = set(glob(OSG_DIR+'/bin/ot*.dll')) - debug_libs # OpenThreads shared libraries
    shared_libraries.extend(release_libs)
    release_libs = set(glob(OSG_DIR+'/bin/osg*.dll')) - debug_libs # OpenThreads shared libraries
    shared_libraries.extend(release_libs)
    # 
    debug_libs = set(glob(OSG_DIR+'/bin/osgPlugins*/osgdb*d.dll'))
    release_libs = set(glob(OSG_DIR+'/bin/osgPlugins*/osgdb*.dll')) - debug_libs # File format plugins
    plugin_libraries.extend(release_libs)    
    # shared_libraries.append(r'C:/Program Files (x86)/OpenSceneGraph321vs2008/bin/ot20-OpenThreads.dll') # OpenThreads libraries
    # shared_libraries.extend(glob(os.path.join(OSG_DIR, 'bin', 'osgPlugins-3.2.1','osgdb*.dll'))) # File format plugins
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
# for module_name in ['osgText',]: # osgText module only, just for quick testing
    extension_modules.append(Extension(
        # binary module name begins with underscore "_", so we can wrap module with a python file
        'osgpypp._%s' % module_name,
        moduleInfo[module_name]["source_files"],
        include_dirs=moduleInfo[module_name]["includes"],
        library_dirs=library_dirs,
        libraries=moduleInfo[module_name]["libraries"],
        extra_compile_args=cflags,        
        ))

# Temporarily copy shared libraries into source folder, because I cannot figure out any other
# way to get them into a bdist package.
print "Temporarily copying shared libraries into osgpypp source folder"
for fname in shared_libraries:
    copy(fname, "src/osgpypp/")
    # print fname
if not os.path.exists("src/osgpypp/osgPlugins-3.2.1/"):
    os.makedirs("src/osgpypp/osgPlugins-3.2.1/")
for fname in plugin_libraries:
    copy(fname, "src/osgpypp/osgPlugins-3.2.1/")
    # print fname

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
      package_data={'osgpypp': ['*.dll', "osgPlugins-3.2.1/*.dll"],},
      # data_files installs files right into Python27 folder...
      # data_files = [('osgpypp', glob(r'C:/Program Files (x86)/OpenSceneGraph321vs2008/bin/ot*.dll'))],
      ext_package='',
      ext_modules=extension_modules,
     )

print "removing copies of shared libraries"
for fname in shared_libraries:
    temp_fname = os.path.join("src", "osgpypp", os.path.basename(fname))
    # print "removing %s" % temp_fname
    os.remove(temp_fname)
for fname in plugin_libraries:
    temp_fname = os.path.join("src", "osgpypp", "osgPlugins-3.2.1", os.path.basename(fname))
    # print "removing %s" % temp_fname
    os.remove(temp_fname)
try:
    os.rmdir("src/osgpypp/osgPlugins-3.2.1/")
except:
    pass
