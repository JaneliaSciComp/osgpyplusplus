#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgkeystone"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osgkeystone.cpp'

# OpenSceneGraph example, osganimate.
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

#include <osg/Notify>
#include <osg/io_utils>
#include <osg/TextureRectangle>
#include <osg/TexMat>
#include <osg/Stencil>
#include <osg/PolygonStipple>
#include <osg/ValueObject>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgGA/StateSetManipulator>
#include <osgGA/TrackballManipulator>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgViewer/config/SingleWindow>
#include <osgViewer/config/SingleScreen>
#include <osgViewer/config/WoWVxDisplay>


def main(argv):


    
    arguments = osg.ArgumentParser(argv)
    
    # initialize the viewer.
    viewer = osgViewer.Viewer(arguments)
    
    ds =  viewer.getDisplaySettings() : osg.DisplaySettings: if (viewer.getDisplaySettings()) else instance()
    ds.readCommandLine(arguments)

    model = osgDB.readNodeFiles(arguments)

    if  not model :
        OSG_NOTICE, "No models loaded, please specify a model file on the command line"
        return 1


    OSG_NOTICE, "Stereo ", ds.getStereo()
    OSG_NOTICE, "StereoMode ", ds.getStereoMode()

    viewer.setSceneData(model)
    
    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add camera manipulator
    viewer.setCameraManipulator(osgGA.TrackballManipulator())

    OSG_NOTICE, "KeystoneFileNames.size()=", ds.getKeystoneFileNames().size()
    for(osg.DisplaySettings.FileNames.iterator itr = ds.getKeystoneFileNames().begin()
        not = ds.getKeystoneFileNames().end()
        ++itr)
        OSG_NOTICE, "   keystone filename = ", *itr

    ds.setKeystoneHint(True)
    
    if  not ds.getKeystoneFileNames().empty() :
        for(osg.DisplaySettings.Objects.iterator itr = ds.getKeystones().begin()
            not = ds.getKeystones().end()
            ++itr)
            keystone = dynamic_cast<osgViewer.Keystone*>(itr)
            if keystone : 
                filename = str()
                keystone.getUserValue("filename",filename)
                OSG_NOTICE, "Loaded keystone ", filename, ", ", keystone
                
                ds.getKeystones().push_back(keystone)
    
    viewer.apply(osgViewer.SingleScreen(0))
    
    viewer.realize()

    while  not viewer.done() :
        viewer.advance()
        viewer.eventTraversal()
        viewer.updateTraversal()
        viewer.renderingTraversals()
    return 0


if __name__ == "__main__":
    main(sys.argv)
