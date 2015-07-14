#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgdatabaserevisions"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgdatabaserevisions.cpp'

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
#include <osgUtil/Optimizer>
#include <osg/CoordinateSystemNode>

#include <osg/Switch>
#include <osgText/Text>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>
#include <osgGA/SphericalManipulator>

#include <iostream>

def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the standard OpenSceneGraph example which loads and visualises 3d models.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("--image <filename>","Load an image and render it on a quad")
    arguments.getApplicationUsage().addCommandLineOption("--dem <filename>","Load an image/DEM and render it on a HeightField")
    arguments.getApplicationUsage().addCommandLineOption("--login <url> <username> <password>","Provide authentication information for http file access.")

    viewer = osgViewer.Viewer(arguments)

    helpType = 0
    if helpType = arguments.readHelpType() : :
        arguments.getApplicationUsage().write(std.cout, helpType)
        return 1
    
    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

#if 0
    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1
#endif

    # set up the camera manipulators.
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( ord("1"), "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("2"), "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("3"), "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("4"), "Terrain", osgGA.TerrainManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("5"), "Spherical", osgGA.SphericalManipulator() )

        pathfile = str()
        keyForAnimationPath = ord("6")
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

    file = "http:#www.openscenegraph.org/data/earth_bayarea/earth.ive"

    fileCache = osgDB.Registry.instance().getFileCache()
    if fileCache :
        fileCache.loadDatabaseRevisionsForFile(file)

        # fileCache.loadDatabaseRevisionsForFile(file) # test to make sure that repeated loads of same revision file doesn't cause problems


    # load the data
    loadedModel = osgDB.readNodeFile(file)
    if  not loadedModel : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    # optimize the scene graph, remove redundant nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel)

    viewer.setSceneData( loadedModel )

    viewer.realize()

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
