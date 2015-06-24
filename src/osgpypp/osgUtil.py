"""
osgUtil module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgUtil library provides general purpose utility classes such as update, 
cull and draw traverses, scene graph operators such a scene graph optimisation, 
tri stripping, and tessellation. 
"""

# osgUtil depends on upstream modules, so always load these
from . import osg

# delegate to binary module, created with pyplusplus and boost::python
from _osgUtil import *
