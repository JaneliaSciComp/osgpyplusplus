"""
osgFX module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgFX library is a NodeKit that extends the core scene graph
to provide a special effects framework.

osgFX's framework allows multiple rendering techniques to be provide 
for each effect, thereby provide the use appropriate rendering 
techniques for each different class of graphics hardware, i.e. 
support for both modern programmable graphics hardware and still 
have standard OpenGL 1.1 support as a fallback.
"""

# Load dependent modules
from . import osgUtil, osgDB

# delegate to binary module, created with pyplusplus and boost::python
from _osgFX import *
