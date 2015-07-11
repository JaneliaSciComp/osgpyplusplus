#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgterrain"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgTerrain
from osgpypp import osgViewer


# Translated from file 'osgterrain.cpp'

# OpenSceneGraph example, osgterrain.
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

#include <osg/ArgumentParser>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <osgTerrain/Terrain>
#include <osgTerrain/TerrainTile>
#include <osgTerrain/GeometryTechnique>
#include <osgTerrain/Layer>

#include <iostream>

template<class T>
class FindTopMostNodeOfTypeVisitor (osg.NodeVisitor) :
    FindTopMostNodeOfTypeVisitor():
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _foundNode(0)
    

    def apply(node):

        
        result = dynamic_cast<T*>(node)
        if result :
            _foundNode = result
        else :
            traverse(node)

    _foundNode = T*()


template<class T>
def findTopMostNodeOfType(node):
    
    if !node : return 0

    fnotv = FindTopMostNodeOfTypeVisitor<T>()
    node.accept(fnotv)

    return fnotv._foundNode

# class to handle events with a pick
class TerrainHandler (osgGA.GUIEventHandler) :

    TerrainHandler(osgTerrain.Terrain* terrain):
        _terrain(terrain) 

    def handle(ea, aa):

        
        switch(ea.getEventType())
            case(osgGA.GUIEventAdapter.KEYDOWN):
                if ea.getKey()=='r' :
                    _terrain.setSampleRatio(_terrain.getSampleRatio()*0.5)
                    osg.notify(osg.NOTICE), "Sample ratio ", _terrain.getSampleRatio()
                    return True
                elif ea.getKey()=='R' :
                    _terrain.setSampleRatio(_terrain.getSampleRatio()/0.5)
                    osg.notify(osg.NOTICE), "Sample ratio ", _terrain.getSampleRatio()
                    return True
                elif ea.getKey()=='v' :
                    _terrain.setVerticalScale(_terrain.getVerticalScale()*1.25)
                    osg.notify(osg.NOTICE), "Vertical scale ", _terrain.getVerticalScale()
                    return True
                elif ea.getKey()=='V' :
                    _terrain.setVerticalScale(_terrain.getVerticalScale()/1.25)
                    osg.notify(osg.NOTICE), "Vertical scale ", _terrain.getVerticalScale()
                    return True

                return False
            default:
                return False

    ~TerrainHandler() 

    _terrain = osgTerrain.Terrain()


def main(argc, argv):

    
    arguments = osg.ArgumentParser(argc, argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    # set up the camera manipulators.
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( '1', "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( '2', "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( '3', "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( '4', "Terrain", osgGA.TerrainManipulator() )

        pathfile = str()
        keyForAnimationPath = '5'
        while arguments.read("-p",pathfile) :
            apm = osgGA.AnimationPathManipulator(pathfile)
            if apm || !apm.valid() : 
                num = keyswitchManipulator.getNumMatrixManipulators()
                keyswitchManipulator.addMatrixManipulator( keyForAnimationPath, "Path", apm )
                keyswitchManipulator.selectMatrixManipulator(num)
                ++keyForAnimationPath

        viewer.setCameraManipulator( keyswitchManipulator.get() )


    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add the record camera path handler
    viewer.addEventHandler(osgViewer.RecordCameraPathHandler)()

    # add the window size toggle handler
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()

    # obtain the vertical scale
    verticalScale = 1.0
    while arguments.read("-v",verticalScale) : 

    # obtain the sample ratio
    sampleRatio = 1.0
    while arguments.read("-r",sampleRatio) : 

    blendingPolicy = osgTerrain.TerrainTile.INHERIT
    strBlendingPolicy = str()
    while arguments.read("--blending-policy", strBlendingPolicy) :
        if strBlendingPolicy == "INHERIT" : blendingPolicy = osgTerrain.TerrainTile.INHERIT
        elif strBlendingPolicy == "DO_NOT_SET_BLENDING" : blendingPolicy = osgTerrain.TerrainTile.DO_NOT_SET_BLENDING
        elif strBlendingPolicy == "ENABLE_BLENDING" : blendingPolicy = osgTerrain.TerrainTile.ENABLE_BLENDING
        elif strBlendingPolicy == "ENABLE_BLENDING_WHEN_ALPHA_PRESENT" : blendingPolicy = osgTerrain.TerrainTile.ENABLE_BLENDING_WHEN_ALPHA_PRESENT

    # load the nodes from the commandline arguments.
    rootnode = osgDB.readNodeFiles(arguments)

    if !rootnode :
        osg.notify(osg.NOTICE), "Warning: no valid data loaded, please specify a database on the command line."
        return 1

    terrain = findTopMostNodeOfType<osgTerrain.Terrain>(rootnode.get())
    if !terrain :
        # no Terrain node present insert one above the loaded model.
        terrain = osgTerrain.Terrain()

        # if CoordinateSystemNode is present copy it's contents into the Terrain, and discard it.
        csn = findTopMostNodeOfType<osg.CoordinateSystemNode>(rootnode.get())
        if csn :
            terrain.set(*csn)
            for(unsigned int i=0 i<csn.getNumChildren()++i)
                terrain.addChild(csn.getChild(i))
        else :
            terrain.addChild(rootnode.get())

        rootnode = terrain.get()

    terrain.setSampleRatio(sampleRatio)
    terrain.setVerticalScale(verticalScale)
    terrain.setBlendingPolicy(blendingPolicy)

    # register our custom handler for adjust Terrain settings
    viewer.addEventHandler(TerrainHandler(terrain.get()))

    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData( rootnode.get() )


    # run the viewers main loop
    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
