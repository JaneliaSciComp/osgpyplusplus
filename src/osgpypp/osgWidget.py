"""
osgWidget module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgWidget library is a NodeKit that extends the core scene 
graph to support a 2D (and eventually 3D) GUI widget set. 
"""

# osgUtil depends on upstream modules, so always load these
from . import osgViewer

# delegate to binary module, created with pyplusplus and boost::python
from _osgWidget import *
