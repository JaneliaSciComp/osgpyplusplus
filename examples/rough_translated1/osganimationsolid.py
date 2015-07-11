#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganimationsolid"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osganimationsolid.cpp'

#  -*-c++-*-
# *  Copyright (C) 2008 Cedric Pinson <cedric.pinson@plopbyte.net>
# *
# * This library is open source and may be redistributed and/or modified under
# * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or
# * (at your option) any later version.  The full license is in LICENSE file
# * included with this distribution, and on the openscenegraph.org website.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * OpenSceneGraph Public License for more details.
#

#include <iostream>
#include <osg/Geometry>
#include <osg/Shape>
#include <osg/ShapeDrawable>
#include <osgViewer/Viewer>
#include <osgGA/TrackballManipulator>
#include <osg/MatrixTransform>

#include <osgAnimation/BasicAnimationManager>
#include <osgAnimation/Channel>
#include <osgAnimation/UpdateMatrixTransform>
#include <osgAnimation/StackedTranslateElement>
#include <osgAnimation/StackedRotateAxisElement>

using namespace osgAnimation

def createAxis():

    
    geode = osg.Geode(osg.Geode())
    geometry = osg.Geometry(osg.Geometry())

    vertices = osg.Vec3Array(osg.Vec3Array())
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 10.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 10.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 10.0))
    geometry.setVertexArray (vertices.get())

    colors = osg.Vec4Array(osg.Vec4Array())
    colors.push_back (osg.Vec4 (1.0, 0.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (1.0, 0.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 1.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 1.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 0.0, 1.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 0.0, 1.0, 1.0))
    geometry.setColorArray (colors.get(), osg.Array.BIND_PER_VERTEX)
    geometry.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINES,0,6))

    geode.addDrawable( geometry.get() )
    geode.getOrCreateStateSet().setMode(GL_LIGHTING, False)
    return geode


int main (int argc, char* argv[])
    arguments = osg.ArgumentParser(argc, argv)
    viewer = osgViewer.Viewer(arguments)

    viewer.setCameraManipulator(osgGA.TrackballManipulator())

    root = osg.Group()

    axe = createAxis()
    geode = osg.Geode()
    geode.addDrawable(osg.ShapeDrawable(osg.Box(osg.Vec3(0.0,0.0,0.0),0.5)))

    #Tranformation to be manipulated by the animation
    trans = osg.MatrixTransform()
    trans.setName("AnimatedNode")
    #Dynamic object, has to be updated during update traversal
    trans.setDataVariance(osg.Object.DYNAMIC)
    #Animation callback for Matrix transforms, name is targetName for Channels
    updatecb = osgAnimation.UpdateMatrixTransform("AnimatedCallback")
    #add manipulator Stack, names must match with channel names
    #elements are applied in LIFO order
    #The first element modifies the position component of the matrix
    #The second element modifies the rotation around x-axis
    updatecb.getStackedTransforms().push_back(osgAnimation.StackedTranslateElement("position"))
    updatecb.getStackedTransforms().push_back(osgAnimation.StackedRotateAxisElement("euler",osg.Vec3(1,0,0),0))
    #connect the UpdateMatrixTransform callback to the MatrixTRanform
    trans.setUpdateCallback(updatecb)
    #initialize MatrixTranform
    trans.setMatrix(osg.Matrix.identity())
    #append geometry node
    trans.addChild (geode.get())

    root.addChild (axe.get())
    root.addChild (trans.get())

    # Define a scheduler for our animations
    grp = osg.Group()
    #add the animation manager to the scene graph to get it called during update traversals
    mng = osgAnimation.BasicAnimationManager()
    grp.setUpdateCallback(mng)
    #add the rest of the scene to the grp node
    grp.addChild(root)

    # And we finaly define our channel for linear Vector interpolation
    channelAnimation1 = osgAnimation.Vec3LinearChannel()
    #name of the AnimationUpdateCallback
    channelAnimation1.setTargetName("AnimatedCallback")
    #name of the StackedElementTransform for position modification
    channelAnimation1.setName("position")
    #Create keyframes for (in this case linear) interpolation of a osg.Vec3
    channelAnimation1.getOrCreateSampler().getOrCreateKeyframeContainer().push_back(osgAnimation.Vec3Keyframe(0, osg.Vec3(0,0,0)))
    channelAnimation1.getOrCreateSampler().getOrCreateKeyframeContainer().push_back(osgAnimation.Vec3Keyframe(2, osg.Vec3(1,1,0)))
    anim1 = osgAnimation.Animation()
    anim1.addChannel(channelAnimation1)
    anim1.setPlayMode(osgAnimation.Animation.PPONG)


    #define the channel for interpolation of a float angle value
    channelAnimation2 = osgAnimation.FloatLinearChannel()
    #name of the AnimationUpdateCallback
    channelAnimation2.setTargetName("AnimatedCallback")
    #name of the StackedElementTransform for position modification
    channelAnimation2.setName("euler")
    #Create keyframes for (in this case linear) interpolation of a osg.Vec3
    channelAnimation2.getOrCreateSampler().getOrCreateKeyframeContainer().push_back(osgAnimation.FloatKeyframe(0, 0))
    channelAnimation2.getOrCreateSampler().getOrCreateKeyframeContainer().push_back(osgAnimation.FloatKeyframe(1.5, 2*osg.PI))
    anim2 = osgAnimation.Animation()
    anim2.addChannel(channelAnimation2)
    anim2.setPlayMode(osgAnimation.Animation.LOOP)


    # We register all animation inside the scheduler
    mng.registerAnimation(anim1)
    mng.registerAnimation(anim2)

    #start the animation
    mng.playAnimation(anim1)
    mng.playAnimation(anim2)

    #set the grp-Group with the scene and the AnimationManager as viewer's scene data
    viewer.setSceneData( grp )
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
