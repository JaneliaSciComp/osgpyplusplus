"""
osgWidget module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgVolume library is a NodeKit that extends the core scene 
graph to support volume rendering. 
"""

# osgUtil depends on upstream modules, so always load these
from . import osgGA

# delegate to binary module, created with pyplusplus and boost::python
from _osgVolume import *
