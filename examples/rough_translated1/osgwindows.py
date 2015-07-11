#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwindows"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgwindows.cpp'

# OpenSceneGraph example, osgwindows.
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

#include <osgDB/ReadFile>
#include <osgUtil/Optimizer>
#include <osgViewer/Viewer>


#include <iostream>

def main(argc, argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # read the scene from the list of file specified commandline args.
    loadedModel = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default mode instead.
    if !loadedModel : loadedModel = osgDB.readNodeFile("cow.osgt")
    
    # if no model has been successfully loaded report failure.
    if !loadedModel : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # construct the viewer.
    viewer = osgViewer.Viewer()

    xoffset = 40
    yoffset = 40

    # left window + left slave camera
        traits = osg.GraphicsContext.Traits()
        traits.x = xoffset + 0
        traits.y = yoffset + 0
        traits.width = 600
        traits.height = 480
        traits.windowDecoration = True
        traits.doubleBuffer = True
        traits.sharedContext = 0

        gc = osg.GraphicsContext.createGraphicsContext(traits.get())

        camera = osg.Camera()
        camera.setGraphicsContext(gc.get())
        camera.setViewport(osg.Viewport(0,0, traits.width, traits.height))
        buffer = traits.doubleBuffer ? GL_BACK : GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        # add this slave camera to the viewer, with a shift left of the projection matrix
        viewer.addSlave(camera.get(), osg.Matrixd.translate(1.0,0.0,0.0), osg.Matrixd())
    
    # right window + right slave camera
        traits = osg.GraphicsContext.Traits()
        traits.x = xoffset + 600
        traits.y = yoffset + 0
        traits.width = 600
        traits.height = 480
        traits.windowDecoration = True
        traits.doubleBuffer = True
        traits.sharedContext = 0

        gc = osg.GraphicsContext.createGraphicsContext(traits.get())

        camera = osg.Camera()
        camera.setGraphicsContext(gc.get())
        camera.setViewport(osg.Viewport(0,0, traits.width, traits.height))
        buffer = traits.doubleBuffer ? GL_BACK : GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        # add this slave camera to the viewer, with a shift right of the projection matrix
        viewer.addSlave(camera.get(), osg.Matrixd.translate(-1.0,0.0,0.0), osg.Matrixd())


    # optimize the scene graph, remove rendundent nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel.get())

    # set the scene to render
    viewer.setSceneData(loadedModel.get())

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
