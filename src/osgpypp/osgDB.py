"""
osgDB module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgDB library provides support for reading and writing scene graphs, 
providing a plugin framework and file utility classes.

The plugin framework in centered around the osgDB::Registry, and allows 
plugins which provide specific file format support to be dynamically 
loaded on demand.
"""

# osgDB depends on upstream modules, so always load these
from . import osgUtil

# delegate to binary module, created with pyplusplus and boost::python
from _osgDB import *

# Translate C++ typedefs into python
Registry.FindFileCallback = FindFileCallback
Registry.ReadFileCallback = ReadFileCallback
Registry.WriteFileCallback = WriteFileCallback
Registry.FileLocationCallback = FileLocationCallback
