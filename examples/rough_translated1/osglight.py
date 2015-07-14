#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osglight"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osglight.cpp'

# OpenSceneGraph example, osglight.
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

#include <osg/Group>
#include <osg/Node>

#include <osg/Light>
#include <osg/LightSource>
#include <osg/StateAttribute>
#include <osg/Geometry>
#include <osg/Point>

#include <osg/MatrixTransform>
#include <osg/PositionAttitudeTransform>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgUtil/Optimizer>
#include <osgUtil/SmoothingVisitor>

#include "stdio.h"


# callback to make the loaded model oscilate up and down.
class ModelTransformCallback (osg.NodeCallback) :

        ModelTransformCallback( osg.BoundingSphere bs)
            _firstTime = 0.0
            _period = 4.0
            _range = bs.radius()*0.5

        virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
            pat = dynamic_cast<osg.PositionAttitudeTransform*>(node)
            frameStamp = nv.getFrameStamp()
            if pat  and  frameStamp :
                if _firstTime==0.0 :
                    _firstTime = frameStamp.getSimulationTime()

                phase = (frameStamp.getSimulationTime()-_firstTime)/_period
                phase -= floor(phase)
                phase *= (2.0 * osg.PI)

                rotation = osg.Quat()
                rotation.makeRotate(phase,1.0,1.0,1.0)

                pat.setAttitude(rotation)

                pat.setPosition(osg.Vec3(0.0,0.0,sin(phase))*_range)

            # must traverse the Node's subgraph
            traverse(node,nv)

        _firstTime = double()
        _period = double()
        _range = double()




def createLights(bb, rootStateSet):


    
    lightGroup = osg.Group()

    modelSize = bb.radius()

    # create a spot light.
    myLight1 = osg.Light()
    myLight1.setLightNum(0)
    myLight1.setPosition(osg.Vec4(bb.corner(4),1.0))
    myLight1.setAmbient(osg.Vec4(1.0,0.0,0.0,1.0))
    myLight1.setDiffuse(osg.Vec4(1.0,0.0,0.0,1.0))
    myLight1.setSpotCutoff(20.0)
    myLight1.setSpotExponent(50.0)
    myLight1.setDirection(osg.Vec3(1.0,1.0,-1.0))

    lightS1 = osg.LightSource()
    lightS1.setLight(myLight1)
    lightS1.setLocalStateSetModes(osg.StateAttribute.ON)

    lightS1.setStateSetModes(*rootStateSet,osg.StateAttribute.ON)
    lightGroup.addChild(lightS1)


    # create a local light.
    myLight2 = osg.Light()
    myLight2.setLightNum(1)
    myLight2.setPosition(osg.Vec4(0.0,0.0,0.0,1.0))
    myLight2.setAmbient(osg.Vec4(0.0,1.0,1.0,1.0))
    myLight2.setDiffuse(osg.Vec4(0.0,1.0,1.0,1.0))
    myLight2.setConstantAttenuation(1.0)
    myLight2.setLinearAttenuation(2.0/modelSize)
    myLight2.setQuadraticAttenuation(2.0/osg.square(modelSize))

    lightS2 = osg.LightSource()
    lightS2.setLight(myLight2)
    lightS2.setLocalStateSetModes(osg.StateAttribute.ON)

    lightS2.setStateSetModes(*rootStateSet,osg.StateAttribute.ON)

    mt = osg.MatrixTransform()
        # set up the animation path
        animationPath = osg.AnimationPath()
        animationPath.insert(0.0,osg.AnimationPath.ControlPoint(bb.corner(0)))
        animationPath.insert(1.0,osg.AnimationPath.ControlPoint(bb.corner(1)))
        animationPath.insert(2.0,osg.AnimationPath.ControlPoint(bb.corner(2)))
        animationPath.insert(3.0,osg.AnimationPath.ControlPoint(bb.corner(3)))
        animationPath.insert(4.0,osg.AnimationPath.ControlPoint(bb.corner(4)))
        animationPath.insert(5.0,osg.AnimationPath.ControlPoint(bb.corner(5)))
        animationPath.insert(6.0,osg.AnimationPath.ControlPoint(bb.corner(6)))
        animationPath.insert(7.0,osg.AnimationPath.ControlPoint(bb.corner(7)))
        animationPath.insert(8.0,osg.AnimationPath.ControlPoint(bb.corner(0)))
        animationPath.setLoopMode(osg.AnimationPath.SWING)

        mt.setUpdateCallback(osg.AnimationPathCallback(animationPath))

    # create marker for point light.
    marker = osg.Geometry()
    vertices = osg.Vec3Array()
    vertices.push_back(osg.Vec3(0.0,0.0,0.0))
    marker.setVertexArray(vertices)
    marker.addPrimitiveSet(osg.DrawArrays(GL_POINTS,0,1))

    stateset = osg.StateSet()
    point = osg.Point()
    point.setSize(4.0)
    stateset.setAttribute(point)

    marker.setStateSet(stateset)

    markerGeode = osg.Geode()
    markerGeode.addDrawable(marker)

    mt.addChild(lightS2)
    mt.addChild(markerGeode)

    lightGroup.addChild(mt)

    return lightGroup

def createWall(v1, v2, v3, stateset):

    

   # create a drawable for occluder.
    geom = osg.Geometry()

    geom.setStateSet(stateset)

    noXSteps = 100
    noYSteps = 100

    coords = osg.Vec3Array()
    coords.reserve(noXSteps*noYSteps)


    dx = (v2-v1)/((float)noXSteps-1.0)
    dy = (v3-v1)/((float)noYSteps-1.0)

    row = unsigned int()
    vRowStart = v1
    for(row=0row<noYSteps++row)
        v = vRowStart
        for(unsigned int col=0col<noXSteps++col)
            coords.push_back(v)
            v += dx
        vRowStart+=dy

    geom.setVertexArray(coords)

    colors = osg.Vec4Array(1)
    (*colors)[0].set(1.0,1.0,1.0,1.0)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)


    for(row=0row<noYSteps-1++row)
        quadstrip = osg.DrawElementsUShort(osg.PrimitiveSet.QUAD_STRIP)
        quadstrip.reserve(noXSteps*2)
        for(unsigned int col=0col<noXSteps++col)
            quadstrip.push_back((row+1)*noXSteps+col)
            quadstrip.push_back(row*noXSteps+col)
        geom.addPrimitiveSet(quadstrip)

    # create the normals.
    osgUtil.SmoothingVisitor.smooth(*geom)

    return geom



def createRoom(loadedModel):


    
    # default scale for this model.
    bs = osg.BoundingSphere(osg.Vec3(0.0,0.0,0.0),1.0)

    root = osg.Group()

    if loadedModel :
        loaded_bs = loadedModel.getBound()

        pat = osg.PositionAttitudeTransform()
        pat.setPivotPoint(loaded_bs.center())

        pat.setUpdateCallback(ModelTransformCallback(loaded_bs))
        pat.addChild(loadedModel)

        bs = pat.getBound()

        root.addChild(pat)


    bs.radius()*=1.5

    # create a bounding box, which we'll use to size the room.
    bb = osg.BoundingBox()
    bb.expandBy(bs)


    # create statesets.
    rootStateSet = osg.StateSet()
    root.setStateSet(rootStateSet)

    wall = osg.StateSet()
    wall.setMode(GL_CULL_FACE,osg.StateAttribute.ON)

    floor = osg.StateSet()
    floor.setMode(GL_CULL_FACE,osg.StateAttribute.ON)

    roof = osg.StateSet()
    roof.setMode(GL_CULL_FACE,osg.StateAttribute.ON)

    geode = osg.Geode()

    # create front side.
    geode.addDrawable(createWall(bb.corner(0),
                                  bb.corner(4),
                                  bb.corner(1),
                                  wall))

    # right side
    geode.addDrawable(createWall(bb.corner(1),
                                  bb.corner(5),
                                  bb.corner(3),
                                  wall))

    # left side
    geode.addDrawable(createWall(bb.corner(2),
                                  bb.corner(6),
                                  bb.corner(0),
                                  wall))
    # back side
    geode.addDrawable(createWall(bb.corner(3),
                                  bb.corner(7),
                                  bb.corner(2),
                                  wall))

    # floor
    geode.addDrawable(createWall(bb.corner(0),
                                  bb.corner(1),
                                  bb.corner(2),
                                  floor))

    # roof
    geode.addDrawable(createWall(bb.corner(6),
                                  bb.corner(7),
                                  bb.corner(4),
                                  roof))

    root.addChild(geode)

    root.addChild(createLights(bb,rootStateSet))

    return root


def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # load the nodes from the commandline arguments.
    loadedModel = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default mode instead.
    if  not loadedModel : loadedModel = osgDB.readNodeFile("glider.osgt")

    # create a room made of foor walls, a floor, a roof, and swinging light fitting.
    rootnode = createRoom(loadedModel)

    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(rootnode)

    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData( rootnode )


    # create the windows and run the threads.
    viewer.realize()

    viewer.getCamera().setCullingMode( viewer.getCamera().getCullingMode()  ~osg.CullStack.SMALL_FEATURE_CULLING)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
