#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganimationskinning"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osganimationskinning.cpp'

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
#include <osg/MatrixTransform>
#include <osg/Geode>
#include <osgViewer/Viewer>
#include <osgGA/TrackballManipulator>
#include <osgDB/WriteFile>
#include <osgUtil/SmoothingVisitor>
#include <osg/io_utils>

#include <osgAnimation/Bone>
#include <osgAnimation/Skeleton>
#include <osgAnimation/RigGeometry>
#include <osgAnimation/BasicAnimationManager>
#include <osgAnimation/UpdateMatrixTransform>
#include <osgAnimation/UpdateBone>
#include <osgAnimation/StackedTransform>
#include <osgAnimation/StackedTranslateElement>
#include <osgAnimation/StackedRotateAxisElement>

def createAxis():

    
    geode = osg.Geode*(osg.Geode())
    geometry = osg.Geometry*(osg.Geometry())

    vertices = osg.Vec3Array*(osg.Vec3Array())
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 1.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 1.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 0.0))
    vertices.push_back (osg.Vec3 ( 0.0, 0.0, 1.0))
    geometry.setVertexArray (vertices)

    colors = osg.Vec4Array*(osg.Vec4Array())
    colors.push_back (osg.Vec4 (1.0, 0.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (1.0, 0.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 1.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 1.0, 0.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 0.0, 1.0, 1.0))
    colors.push_back (osg.Vec4 (0.0, 0.0, 1.0, 1.0))
    geometry.setColorArray (colors, osg.Array.BIND_PER_VERTEX)
    geometry.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINES,0,6))

    geode.addDrawable( geometry )
    return geode

def createTesselatedBox(nsplit, size):

    
    riggeometry = osgAnimation.RigGeometry()

    geometry = osg.Geometry()
    vertices = osg.Vec3Array(osg.Vec3Array())
    colors = osg.Vec3Array(osg.Vec3Array())
    geometry.setVertexArray (vertices)
    geometry.setColorArray (colors, osg.Array.BIND_PER_VERTEX)

    step = size / static_cast<float>(nsplit)
    s = 0.5/4.0
    for (int i = 0 i < nsplit i++)
        x = -1.0 + static_cast<float>(i) * step
        print x
        vertices.push_back (osg.Vec3 ( x, s, s))
        vertices.push_back (osg.Vec3 ( x, -s, s))
        vertices.push_back (osg.Vec3 ( x, -s, -s))
        vertices.push_back (osg.Vec3 ( x, s, -s))
        c = osg.Vec3(0.0,0.0,0.0)
        c[i%3] = 1.0
        colors.push_back (c)
        colors.push_back (c)
        colors.push_back (c)
        colors.push_back (c)

    array = osg.UIntArray()
    for (int i = 0 i < nsplit - 1 i++)
        base = i * 4
        array.push_back(base)
        array.push_back(base+1)
        array.push_back(base+4)
        array.push_back(base+1)
        array.push_back(base+5)
        array.push_back(base+4)

        array.push_back(base+3)
        array.push_back(base)
        array.push_back(base+4)
        array.push_back(base+7)
        array.push_back(base+3)
        array.push_back(base+4)

        array.push_back(base+5)
        array.push_back(base+1)
        array.push_back(base+2)
        array.push_back(base+2)
        array.push_back(base+6)
        array.push_back(base+5)

        array.push_back(base+2)
        array.push_back(base+3)
        array.push_back(base+7)
        array.push_back(base+6)
        array.push_back(base+2)
        array.push_back(base+7)

    geometry.addPrimitiveSet(osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, array.size(), array.front()))
    geometry.setUseDisplayList( False )
    riggeometry.setSourceGeometry(geometry)
    return riggeometry


def initVertexMap(b0, b1, b2, geom, array):


    
    vertexesInfluences = osgAnimation.VertexInfluenceSet()
    vim = osgAnimation.VertexInfluenceMap()

    (*vim)[b0.getName()].setName(b0.getName())
    (*vim)[b1.getName()].setName(b1.getName())
    (*vim)[b2.getName()].setName(b2.getName())

    for (int i = 0 i < (int)array.size() i++)
        val = (*array)[i][0]
        print val
        if val >= -1.0  and  val <= 0.0 :
            (*vim)[b0.getName()].push_back(osgAnimation.VertexIndexWeight(i,1.0))
        elif  val > 0.0  and  val <= 1.0 :
            (*vim)[b1.getName()].push_back(osgAnimation.VertexIndexWeight(i,1.0))
        elif  val > 1.0 :
            (*vim)[b2.getName()].push_back(osgAnimation.VertexIndexWeight(i,1.0))

    geom.setInfluenceMap(vim)



int main (int argc, char* argv[])
    arguments = osg.ArgumentParser(argv)
    viewer = osgViewer.Viewer(arguments)

    viewer.setCameraManipulator(osgGA.TrackballManipulator())

    skelroot = osgAnimation.Skeleton()
    skelroot.setDefaultUpdateCallback()
    root = osgAnimation.Bone()
    root.setInvBindMatrixInSkeletonSpace(osg.Matrix.inverse(osg.Matrix.translate(-1.0,0.0,0.0)))
    root.setName("root")
    pRootUpdate = osgAnimation.UpdateBone("root")
    pRootUpdate.getStackedTransforms().push_back(osgAnimation.StackedTranslateElement("translate",osg.Vec3(-1.0,0.0,0.0)))
    root.setUpdateCallback(pRootUpdate)

    right0 = osgAnimation.Bone()
    right0.setInvBindMatrixInSkeletonSpace(osg.Matrix.inverse(osg.Matrix.translate(0.0,0.0,0.0)))
    right0.setName("right0")
    pRight0Update = osgAnimation.UpdateBone("right0")
    pRight0Update.getStackedTransforms().push_back(osgAnimation.StackedTranslateElement("translate", osg.Vec3(1.0,0.0,0.0)))
    pRight0Update.getStackedTransforms().push_back(osgAnimation.StackedRotateAxisElement("rotate", osg.Vec3(0.0,0.0,1.0), 0.0))
    right0.setUpdateCallback(pRight0Update)

    right1 = osgAnimation.Bone()
    right1.setInvBindMatrixInSkeletonSpace(osg.Matrix.inverse(osg.Matrix.translate(1.0,0.0,0.0)))
    right1.setName("right1")
    pRight1Update = osgAnimation.UpdateBone("right1")
    pRight1Update.getStackedTransforms().push_back(osgAnimation.StackedTranslateElement("translate", osg.Vec3(1.0,0.0,0.0)))
    pRight1Update.getStackedTransforms().push_back(osgAnimation.StackedRotateAxisElement("rotate", osg.Vec3(0.0,0.0,1.0), 0.0))
    right1.setUpdateCallback(pRight1Update)

    root.addChild(right0)
    right0.addChild(right1)
    skelroot.addChild(root)

    scene = osg.Group()
    manager = osgAnimation.BasicAnimationManager()
    scene.setUpdateCallback(manager)

    anim = osgAnimation.Animation()
        keys0 = osgAnimation.FloatKeyframeContainer()
        keys0.push_back(osgAnimation.FloatKeyframe(0.0,0.0))
        keys0.push_back(osgAnimation.FloatKeyframe(3.0,osg.PI_2))
        keys0.push_back(osgAnimation.FloatKeyframe(6.0,osg.PI_2))
        sampler = osgAnimation.FloatLinearSampler()
        sampler.setKeyframeContainer(keys0)
        channel = osgAnimation.FloatLinearChannel(sampler)
        channel.setName("rotate")
        channel.setTargetName("right0")
        anim.addChannel(channel)

        keys1 = osgAnimation.FloatKeyframeContainer()
        keys1.push_back(osgAnimation.FloatKeyframe(0.0,0.0))
        keys1.push_back(osgAnimation.FloatKeyframe(3.0,0.0))
        keys1.push_back(osgAnimation.FloatKeyframe(6.0,osg.PI_2))
        sampler = osgAnimation.FloatLinearSampler()
        sampler.setKeyframeContainer(keys1)
        channel = osgAnimation.FloatLinearChannel(sampler)
        channel.setName("rotate")
        channel.setTargetName("right1")
        anim.addChannel(channel)
    manager.registerAnimation(anim)
    manager.buildTargetReference()

    # let's start  not 
    manager.playAnimation(anim)

    # we will use local data from the skeleton
    rootTransform = osg.MatrixTransform()
    rootTransform.setMatrix(osg.Matrix.rotate(osg.PI_2,osg.Vec3(1.0,0.0,0.0)))
    right0.addChild(createAxis())
    right0.setDataVariance(osg.Object.DYNAMIC)
    right1.addChild(createAxis())
    right1.setDataVariance(osg.Object.DYNAMIC)
    trueroot = osg.MatrixTransform()
    trueroot.setMatrix(osg.Matrix(root.getMatrixInBoneSpace().ptr()))
    trueroot.addChild(createAxis())
    trueroot.addChild(skelroot)
    trueroot.setDataVariance(osg.Object.DYNAMIC)
    rootTransform.addChild(trueroot)
    scene.addChild(rootTransform)

    geom = createTesselatedBox(4, 4.0)
    geode = osg.Geode()
    geode.addDrawable(geom)
    skelroot.addChild(geode)
    src = dynamic_cast<osg.Vec3Array*>(geom.getSourceGeometry().getVertexArray())
    geom.getOrCreateStateSet().setMode(GL_LIGHTING, False)
    geom.setDataVariance(osg.Object.DYNAMIC)

    initVertexMap(root, right0, right1, geom, src)

    # let's run  not 
    viewer.setSceneData( scene )
    viewer.realize()

    while  not viewer.done() :
        viewer.frame()

    osgDB.writeNodeFile(*scene, "skinning.osg")
    return 0




if __name__ == "__main__":
    main(sys.argv)
