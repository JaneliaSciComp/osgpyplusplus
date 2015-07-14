#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgdepthpartition"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgdepthpartition.cpp'

# OpenSceneGraph example, osgdepthpartion.
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

#include <osgUtil/UpdateVisitor>

#include <osgDB/ReadFile>

#include <osg/ShapeDrawable>
#include <osg/PositionAttitudeTransform>

#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

r_earth = 6378.137
r_sun = 695990.0
AU = 149697900.0

def createScene():

    
    # Create the Earth, in blue
    earth_sd = osg.ShapeDrawable()
    earth_sphere = osg.Sphere()
    earth_sphere.setName("EarthSphere")
    earth_sphere.setRadius(r_earth)
    earth_sd.setShape(earth_sphere)
    earth_sd.setColor(osg.Vec4(0, 0, 1.0, 1.0))

    earth_geode = osg.Geode()
    earth_geode.setName("EarthGeode")
    earth_geode.addDrawable(earth_sd)

    # Create the Sun, in yellow
    sun_sd = osg.ShapeDrawable()
    sun_sphere = osg.Sphere()
    sun_sphere.setName("SunSphere")
    sun_sphere.setRadius(r_sun)
    sun_sd.setShape(sun_sphere)
    sun_sd.setColor(osg.Vec4(1.0, 0.0, 0.0, 1.0))

    sun_geode = osg.Geode()
    sun_geode.setName("SunGeode")
    sun_geode.addDrawable(sun_sd)

    # Move the sun behind the earth
    pat = osg.PositionAttitudeTransform()
    pat.setPosition(osg.Vec3d(0.0, AU, 0.0))
    pat.addChild(sun_geode)

    unitCircle = osg.Geometry()
      colours = osg.Vec4Array(1)
      (*colours)[0] = osg.Vec4d(1.0,1.0,1.0,1.0)
      unitCircle.setColorArray(colours, osg.Array.BIND_OVERALL)
      n_points = 1024
      coords = osg.Vec3Array(n_points)
      dx = 2.0*osg.PI/n_points
      double s,c
      for (unsigned int j=0 j<n_points ++j) 
    s = sin(dx*j)
    c = cos(dx*j)
    (*coords)[j].set(osg.Vec3d(c,s,0.0))
      unitCircle.setVertexArray(coords)
      unitCircle.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)
      unitCircle.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_LOOP,0,n_points))

    axes = osg.Geometry()
      colours = osg.Vec4Array(1)
      (*colours)[0] = osg.Vec4d(1.0,0.0,0.0,1.0)
      axes.setColorArray(colours, osg.Array.BIND_OVERALL)
      coords = osg.Vec3Array(6)
      (*coords)[0].set(osg.Vec3d(0.0, 0.0, 0.0))
      (*coords)[1].set(osg.Vec3d(0.5, 0.0, 0.0))
      (*coords)[2].set(osg.Vec3d(0.0, 0.0, 0.0))
      (*coords)[3].set(osg.Vec3d(0.0, 0.5, 0.0))
      (*coords)[4].set(osg.Vec3d(0.0, 0.0, 0.0))
      (*coords)[5].set(osg.Vec3d(0.0, 0.0, 0.5))
      axes.setVertexArray(coords)
      axes.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)
      axes.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINES,0,6))

    # Earth orbit
    earthOrbitGeode = osg.Geode()
    earthOrbitGeode.addDrawable(unitCircle)
    earthOrbitGeode.addDrawable(axes)
    earthOrbitGeode.setName("EarthOrbitGeode")

    earthOrbitPAT = osg.PositionAttitudeTransform()
    earthOrbitPAT.setScale(osg.Vec3d(AU,AU,AU))
    earthOrbitPAT.setPosition(osg.Vec3d(0.0, AU, 0.0))
    earthOrbitPAT.addChild(earthOrbitGeode)
    earthOrbitPAT.setName("EarthOrbitPAT")

    scene = osg.Group()
    scene.setName("SceneGroup")
    scene.addChild(earth_geode)
    scene.addChild(pat)
    scene.addChild(earthOrbitPAT)

    return scene

def main(argv):

    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    # add stats
    viewer.addEventHandler( osgViewer.StatsHandler() )

    needToSetHomePosition = False

    # read the scene from the list of file specified commandline args.
    scene = osgDB.readNodeFiles(arguments)

    # if one hasn't been loaded create an earth and sun test model.
    if  not scene :
        scene = createScene()
        needToSetHomePosition = True
    # pass the loaded scene graph to the viewer.
    viewer.setSceneData(scene)

    viewer.setCameraManipulator(osgGA.TrackballManipulator)()

    if needToSetHomePosition :
        viewer.getCameraManipulator().setHomePosition(osg.Vec3d(0.0,-5.0*r_earth,0.0),osg.Vec3d(0.0,0.0,0.0),osg.Vec3d(0.0,0.0,1.0))

    zNear = 1.0, zMid=10.0, zFar=1000.0
    if arguments.read("--depth-partition",zNear, zMid, zFar) :
        # set up depth partitioning
        dps = osgViewer.DepthPartitionSettings()
        dps._mode = osgViewer.DepthPartitionSettings.FIXED_RANGE
        dps._zNear = zNear
        dps._zMid = zMid
        dps._zFar = zFar
        viewer.setUpDepthPartition(dps)
    else:
        # set up depth partitioning with default settings
        viewer.setUpDepthPartition()


    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
