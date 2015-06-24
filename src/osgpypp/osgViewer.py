"""
osgViewer module
Part of osgpyplusplus python bindings for OpenSceneGraph C++ library
https://github.com/JaneliaSciComp/osgpyplusplus

The osgViewer library provides high level viewer functionality designed to 
make it easier to write a range of different types of viewers, from viewers 
embedded in existing windows via SimpleViewer, through to highly scalable 
and flexible Viewer and Composite classes.

A set of event handlers add functionality to these viewers so that you can 
rapidly compose the viewer functionality tailored to your needs. Finally 
the viewer classes can be adapted to work with a range of different window 
toolkit API's via GraphicsWindow implementations, with native Win32, X11 
and Carbon implementations on Windows, Unices and OSX respectively, and 
other window toolkits such as WxWidgets, Qt etc.
"""

# osgUtil depends on upstream modules, so always load these
from . import osgGA
from . import osgText

# delegate to binary module, created with pyplusplus and boost::python
from _osgViewer import *
