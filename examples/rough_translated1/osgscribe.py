#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgscribe"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgscribe.cpp'

# OpenSceneGraph example, osgscribe.
#*
#*  Permission is hereby granted, free of charge, to any person obtaining a copy
#*  of this software and associated documentation files (the "Software"), to deal
#*  in the Software without restriction, including without limitation the rights
#*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#*  copies of the Software, and to permit persons to whom the Software is
#*  furnished to do so, subject to the following conditions:
#*
#*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#*  THE SOFTWARE.
#

#include <osg/Geode>
#include <osg/Group>
#include <osg/Notify>
#include <osg/Material>
#include <osg/PolygonOffset>
#include <osg/PolygonMode>
#include <osg/LineStipple>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>

#include <osgUtil/Optimizer>

def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # load the nodes from the commandline arguments.
    loadedModel = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default mode instead.
    if  not loadedModel : loadedModel = osgDB.readNodeFile("cow.osgt")
    
    if  not loadedModel :
        osg.notify(osg.NOTICE), "Please specifiy a model filename on the command line."
        return 1
  
    # to do scribe mode we create a top most group to contain the
    # original model, and then a second group contains the same model
    # but overrides various state attributes, so that the second instance
    # is rendered as wireframe.
    
    rootnode = osg.Group()

    decorator = osg.Group()
    
    rootnode.addChild(loadedModel)
    
    
    rootnode.addChild(decorator)
    
    decorator.addChild(loadedModel)  

    # set up the state so that the underlying color is not seen through
    # and that the drawing mode is changed to wireframe, and a polygon offset
    # is added to ensure that we see the wireframe itself, and turn off 
    # so texturing too.
    stateset = osg.StateSet()
    polyoffset = osg.PolygonOffset()
    polyoffset.setFactor(-1.0)
    polyoffset.setUnits(-1.0)
    polymode = osg.PolygonMode()
    polymode.setMode(osg.PolygonMode.FRONT_AND_BACK,osg.PolygonMode.LINE)
    stateset.setAttributeAndModes(polyoffset,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
    stateset.setAttributeAndModes(polymode,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)

#if 1
    material = osg.Material()
    stateset.setAttributeAndModes(material,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE|osg.StateAttribute.OFF)
#else:
    # version which sets the color of the wireframe.
    material = osg.Material()
    material.setColorMode(osg.Material.OFF) # switch glColor usage off
    # turn all lighting off 
    material.setAmbient(osg.Material.FRONT_AND_BACK, osg.Vec4(0.0,0.0,0.0,1.0))
    material.setDiffuse(osg.Material.FRONT_AND_BACK, osg.Vec4(0.0,0.0,0.0,1.0))
    material.setSpecular(osg.Material.FRONT_AND_BACK, osg.Vec4(0.0,0.0,0.0,1.0))
    # except emission... in which we set the color we desire
    material.setEmission(osg.Material.FRONT_AND_BACK, osg.Vec4(0.0,1.0,0.0,1.0))
    stateset.setAttributeAndModes(material,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
#endif

    stateset.setTextureMode(0,GL_TEXTURE_2D,osg.StateAttribute.OVERRIDE|osg.StateAttribute.OFF)
    
#     osg.LineStipple* linestipple = osg.LineStipple()
#     linestipple.setFactor(1)
#     linestipple.setPattern(0xf0f0)
#     stateset.setAttributeAndModes(linestipple,osg.StateAttribute.OVERRIDE_ON)
    
    decorator.setStateSet(stateset)
  
    
    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(rootnode)
     
    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData( rootnode )
    
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
