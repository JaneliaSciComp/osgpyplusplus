#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgmultitexture"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgmultitexture.cpp'

# OpenSceneGraph example, osgmultitexture.
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

#include <osgViewer/Viewer>

#include <osg/Notify>

#include <osg/Texture2D>
#include <osg/TexEnv>
#include <osg/TexGen>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>

#include <osgUtil/Optimizer>

#include <iostream>

def main(argc, argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)
   
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # load the nodes from the commandline arguments.
    rootnode = osgDB.readNodeFiles(arguments)
    
    # if not loaded assume no arguments passed in, try use default mode instead.
    if !rootnode : rootnode = osgDB.readNodeFile("cessnafire.osgt")
    
    if !rootnode :
        osg.notify(osg.NOTICE), "Please specify a model filename on the command line."
        return 1
    
    image = osgDB.readImageFile("Images/reflect.rgb")
    if image :
        texture = osg.Texture2D()
        texture.setImage(image)

        texgen = osg.TexGen()
        texgen.setMode(osg.TexGen.SPHERE_MAP)

        texenv = osg.TexEnv()
        texenv.setMode(osg.TexEnv.BLEND)
        texenv.setColor(osg.Vec4(0.3,0.3,0.3,0.3))

        stateset = osg.StateSet()
        stateset.setTextureAttributeAndModes(1,texture,osg.StateAttribute.ON)
        stateset.setTextureAttributeAndModes(1,texgen,osg.StateAttribute.ON)
        stateset.setTextureAttribute(1,texenv)
        
        rootnode.setStateSet(stateset)
    else :
        osg.notify(osg.NOTICE), "unable to load reflect map, model will not be mutlitextured"

    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(rootnode)
     
    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData( rootnode )
    
    # create the windows and run the threads.
    viewer.realize()

    for(unsigned int contextID = 0 
        contextID<osg.DisplaySettings.instance().getMaxNumberOfGraphicsContexts()
        ++contextID)
        textExt = osg.Texture.getExtensions(contextID,False)
        if textExt :
            if !textExt.isMultiTexturingSupported() :
                print "Warning: multi-texturing not supported by OpenGL drivers, unable to run application."
                return 1

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
