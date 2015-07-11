"""
osgManipulator module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgManipulator library is a NodeKit that extends the core 
scene graph to support 3D interactive manipulators. 
"""

# osgManipulator depends on osgViewer, and its dependencies
from . import osgViewer

# delegate to binary module, created with pyplusplus and boost::python
from _osgManipulator import *
