"""
osgSim module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgSim library is a NodeKit that extends the core scene graph 
to support nodes and drawables that specific to the visual simulation, 
such a navigational light point support and OpenFlight style degrees 
of freedom transform. 
"""

# osgSim depends on osg, osgText, osgUtil, osgDB
# dependencies
from . import osgText

# delegate to binary module, created with pyplusplus and boost::python
from _osgSim import *
