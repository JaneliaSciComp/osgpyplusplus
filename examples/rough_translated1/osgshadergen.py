#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgshadergen"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgshadergen.cpp'

# -*-c++-*- OpenSceneGraph - Copyright (C) 1998-2006 Robert Osfield 
# *
# * This application is open source and may be redistributed and/or modified   
# * freely and without restriction, both in commercial and non commercial applications,
# * as long as this copyright notice is maintained.
# * 
# * This application is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

#include <osgDB/ReadFile>
#include <osgUtil/ShaderGen>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <iostream>


class ShaderGenReadFileCallback (osgDB.Registry.ReadFileCallback) :
    ShaderGenReadFileCallback()

    def readNode(filename, options):

        
        result = osgDB.Registry.ReadFileCallback.readNode(filename, options)
        if osg.Node *node = result.getNode() :
            _visitor.reset()
            node.accept(_visitor)
        return result

    def setRootStateSet(stateSet):

         _visitor.setRootStateSet(stateSet) 
    osg.StateSet *getRootStateSet()   return _visitor.getRootStateSet() 
    _visitor = osgUtil.ShaderGenVisitor()



def main(argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+
            " is an example of conversion of fixed function pipeline to GLSL")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")

    viewer = osgViewer.Viewer(arguments)

    helpType = 0
    if helpType = arguments.readHelpType() : :
        arguments.getApplicationUsage().write(std.cout, helpType)
        return 1
    
    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1
    
    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    # set up the camera manipulators.
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( ord("1"), "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("2"), "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("3"), "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("4"), "Terrain", osgGA.TerrainManipulator() )

        pathfile = str()
        keyForAnimationPath = ord("5")
        while arguments.read("-p",pathfile) :
            apm = osgGA.AnimationPathManipulator(pathfile)
            if apm  or   not apm.valid() : 
                num = keyswitchManipulator.getNumMatrixManipulators()
                keyswitchManipulator.addMatrixManipulator( keyForAnimationPath, "Path", apm )
                keyswitchManipulator.selectMatrixManipulator(num)
                ++keyForAnimationPath

        viewer.setCameraManipulator( keyswitchManipulator )

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    
    # add the thread model handler
    viewer.addEventHandler(osgViewer.ThreadingHandler)()

    # add the window size toggle handler
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()
        
    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add the help handler
    viewer.addEventHandler(osgViewer.HelpHandler(arguments.getApplicationUsage()))

    # add the record camera path handler
    viewer.addEventHandler(osgViewer.RecordCameraPathHandler)()

    # add the LOD Scale handler
    viewer.addEventHandler(osgViewer.LODScaleHandler)()

    # add the screen capture handler
    viewer.addEventHandler(osgViewer.ScreenCaptureHandler)()
    
    # Register shader generator callback
    readFileCallback = ShaderGenReadFileCallback()
    # All read nodes will inherit root state set.
    readFileCallback.setRootStateSet(viewer.getCamera().getStateSet())
    osgDB.Registry.instance().setReadFileCallback(readFileCallback)

    # load the data
    loadedModel = osgDB.readNodeFiles(arguments)
    if  not loadedModel : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    viewer.setSceneData( loadedModel )

    viewer.realize()

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
