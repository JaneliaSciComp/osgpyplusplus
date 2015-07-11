#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgclip"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgclip.cpp'

# OpenSceneGraph example, osgclip.
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

#include <osg/MatrixTransform>
#include <osg/ClipNode>
#include <osg/Billboard>
#include <osg/Geode>
#include <osg/Group>
#include <osg/Notify>
#include <osg/Material>
#include <osg/PolygonOffset>
#include <osg/PolygonMode>
#include <osg/LineStipple>
#include <osg/AnimationPath>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>

#include <osgViewer/Viewer>

#include <osgUtil/Optimizer>


def decorate_with_clip_node(subgraph):


    
    rootnode = osg.Group()
    

    # create wireframe view of the model so the user can see
    # what parts are being culled away.
    stateset = osg.StateSet()
    #osg.Material* material = osg.Material()
    polymode = osg.PolygonMode()
    polymode.setMode(osg.PolygonMode.FRONT_AND_BACK,osg.PolygonMode.LINE)
    stateset.setAttributeAndModes(polymode,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
    
    wireframe_subgraph = osg.Group()
    wireframe_subgraph.setStateSet(stateset)
    wireframe_subgraph.addChild(subgraph)
    rootnode.addChild(wireframe_subgraph)

#
#    # simple approach to adding a clipnode above a subrgaph.
#
#    # create clipped part.
#    clipped_subgraph = osg.ClipNode()
#
#    bs = subgraph.getBound()
#    bs.radius()*= 0.4
#
#    bb = osg.BoundingBox()
#    bb.expandBy(bs)
#
#
#    clipped_subgraph.createClipBox(bb)
#    clipped_subgraph.addChild(subgraph)
#    rootnode.addChild(clipped_subgraph)
#


    # more complex approach to managing ClipNode, allowing
    # ClipNode node to be transformed independantly from the subgraph
    # that it is clipping.
    
    transform = osg.MatrixTransform()

    nc = osg.AnimationPathCallback(subgraph.getBound().center(),osg.Vec3(0.0,0.0,1.0),osg.inDegrees(45.0))
    transform.setUpdateCallback(nc)

    clipnode = osg.ClipNode()
    bs = subgraph.getBound()
    bs.radius()*= 0.4

    bb = osg.BoundingBox()
    bb.expandBy(bs)

    clipnode.createClipBox(bb)
    clipnode.setCullingActive(False)

    transform.addChild(clipnode)
    rootnode.addChild(transform)


    # create clipped part.
    clipped_subgraph = osg.Group()

    clipped_subgraph.setStateSet(clipnode.getStateSet())
    clipped_subgraph.addChild(subgraph)
    rootnode.addChild(clipped_subgraph)

    return rootnode


def main(argc, argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # load the nodes from the commandline arguments.
    loadedModel = osgDB.readNodeFiles(arguments)


    # if not loaded assume no arguments passed in, try use default mode instead.
    if !loadedModel : loadedModel = osgDB.readNodeFile("cow.osgt")


    if !loadedModel :
        osg.notify(osg.NOTICE), "Please specifiy a filename and the command line"
        return 1
  
    # decorate the scenegraph with a clip node.
    rootnode = decorate_with_clip_node(loadedModel)
      
    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(rootnode)
    
    viewer = osgViewer.Viewer()
     
    # set the scene to render
    viewer.setSceneData(rootnode)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
