"""
osgAnimation module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgAnimation library provides general purpose utility classes for animation. 
"""

# dependencies
from . import osgViewer

# delegate to binary module, created with pyplusplus and boost::python
from _osgAnimation import *
