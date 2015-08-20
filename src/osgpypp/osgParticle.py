"""
osgParticle module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgParticle library is a NodeKit that extends the core scene graph 
to support particle effects. 
"""

# osgParticle depends on osg, osgUtil, osgDB
# dependencies
from . import osgDB

# delegate to binary module, created with pyplusplus and boost::python
from _osgParticle import *
