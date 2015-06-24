"""
osgText module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgText library is a NodeKit that extends the core scene graph to support 
high quality text. 
"""

# osgUtil depends on upstream modules, so always load these
from . import osgDB

# delegate to binary module, created with pyplusplus and boost::python
from _osgText import *
