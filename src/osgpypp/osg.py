"""
osg module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The core osg library provides the basic scene graph classes such as Nodes, 
State and Drawables, and maths and general helper classes. 
"""

# delegate to binary module, created with pyplusplus and boost::python
from _osg import *
