#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganimationmorph"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer

#  -*-c++-*- 
 *  Copyright (C) 2008 Cedric Pinson <mornifle@plopbyte.net>
 *
 * This library is open source and may be redistributed and/or modified under  
 * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or 
 * (at your option) any later version.  The full license is in LICENSE file
 * included with this distribution, and on the openscenegraph.org website.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
 * OpenSceneGraph Public License for more details.


#include <iostream>
#include <osg/Geometry>
#include <osg/MatrixTransform>
#include <osg/Geode>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgUtil/SmoothingVisitor>
#include <osg/io_utils>

#include <osgAnimation/MorphGeometry>
#include <osgAnimation/BasicAnimationManager>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

struct GeometryFinder : public osg.NodeVisitor
    osg.ref_ptr<osg.Geometry> _geom
    GeometryFinder() : osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN) 
    def apply(geode):
        if _geom.valid() :
            return
        for (unsigned int i = 0 i < geode.getNumDrawables() i++) 
            geom =  dynamic_cast<osg.Geometry*>(geode.getDrawable(i))
            if geom : 
                _geom = geom
                return


osg.ref_ptr<osg.Geometry> getShape( str name)
    osg.ref_ptr<osg.Node> shape0 = osgDB.readNodeFile(name)
    if shape0 :
        finder = GeometryFinder()
        shape0.accept(finder)
        return finder._geom
    else:
        NULL = return()


int main (int argc, char* argv[])
    arguments = osg.ArgumentParser(argc, argv)
    viewer = osgViewer.Viewer(arguments)

    animation =  new osgAnimation.Animation
    channel0 =  new osgAnimation.FloatLinearChannel
    channel0.getOrCreateSampler().getOrCreateKeyframeContainer().push_back(osgAnimation.FloatKeyframe(0,0.0))
    channel0.getOrCreateSampler().getOrCreateKeyframeContainer().push_back(osgAnimation.FloatKeyframe(1,1.0))
    channel0.setTargetName("MorphNodeCallback")
    channel0.setName("0")

    animation.addChannel(channel0)
    animation.setName("Morph")
    animation.computeDuration()
    animation.setPlayMode(osgAnimation.Animation.PPONG)
    bam =  new osgAnimation.BasicAnimationManager
    bam.registerAnimation(animation)

    osg.ref_ptr<osg.Geometry> geom0 = getShape("morphtarget_shape0.osg")
    if !geom0 : 
        std.cerr, "can't read morphtarget_shape0.osg"
        return 0

    osg.ref_ptr<osg.Geometry> geom1 = getShape("morphtarget_shape1.osg")
    if !geom1 : 
        std.cerr, "can't read morphtarget_shape1.osg"
        return 0

    # initialize with the first shape
    morph =  new osgAnimation.MorphGeometry(*geom0)
    morph.addMorphTarget(geom1.get())

    viewer.setCameraManipulator(new osgGA.TrackballManipulator())


    scene =  new osg.Group
    scene.addUpdateCallback(bam)
    
    geode =  new osg.Geode
    geode.addDrawable(morph)
    geode.addUpdateCallback(new osgAnimation.UpdateMorph("MorphNodeCallback"))
    scene.addChild(geode)

    viewer.addEventHandler(new osgViewer.StatsHandler())
    viewer.addEventHandler(new osgViewer.WindowSizeHandler())
    viewer.addEventHandler(new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()))

    # let's run !
    viewer.setSceneData( scene )
    viewer.realize()

    bam.playAnimation(animation)


    while !viewer.done() :
        viewer.frame()

    osgDB.writeNodeFile(*scene, "morph_scene.osg")

    return 0




if __name__ == "__main__":
    main(sys.argv)
