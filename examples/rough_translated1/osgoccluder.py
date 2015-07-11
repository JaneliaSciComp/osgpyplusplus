#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgoccluder"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgoccluder.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


#include <osgViewer/Viewer>

#include <osg/MatrixTransform>
#include <osg/Billboard>
#include <osg/Geode>
#include <osg/Group>
#include <osg/Notify>
#include <osg/io_utils>

#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>

#include <osgUtil/Optimizer>

#include <osg/OccluderNode>
#include <osg/Geometry>
#include <osg/ShapeDrawable>

#include <iostream>

class OccluderEventHandler : public osgGA.GUIEventHandler
    public:

        OccluderEventHandler(osgViewer.Viewer* viewer):_viewer(viewer) 

        virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)

        addPoint = void( osg.Vec3 pos)

        endOccluder = void()

        osg.Group* rootNode()  return dynamic_cast<osg.Group*>(_viewer.getSceneData()) 


        _viewer = osgViewer.Viewer*()
        osg.ref_ptr<osg.Group>                _occluders
        osg.ref_ptr<osg.ConvexPlanarOccluder> _convexPlanarOccluder


bool OccluderEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()=='a' :

                view =  dynamic_cast<osgViewer.View*>(aa)
                intersections = osgUtil.LineSegmentIntersector.Intersections()
                if view  view.computeIntersections(ea, intersections) :
                    hit =  *(intersections.begin())
                    if hit.matrix.valid() : addPoint(hit.localIntersectionPoint * (*hit.matrix))
                    addPoint = else:(hit.localIntersectionPoint)

                true = return()
            else: if ea.getKey()=='e' :
                endOccluder()
                true = return()
            else: if ea.getKey()=='O' :
                if _occluders.valid() :

                    if osgDB.writeNodeFile(*_occluders,"saved_occluders.osgt") :
                        print "saved occluders to 'saved_occluders.osgt'"
                else:
                    print "no occluders to save"
                true = return()
            false = return()

        default:
            false = return()

void OccluderEventHandler.addPoint( osg.Vec3 pos)
    print "add point ", pos

    if !_convexPlanarOccluder.valid() : _convexPlanarOccluder = new osg.ConvexPlanarOccluder

    occluder =  _convexPlanarOccluder.getOccluder()
    occluder.add(pos)

#
#     osg.BoundingSphere bs = rootNode().getBound()
#
#     osg.ShapeDrawable* sd = new osg.ShapeDrawable(new osg.Sphere(pos,bs.radius()*0.001f))
#     geode =  new osg.Geode
#     geode.addDrawable(sd)
#
#     rootNode().addChild(geode)
#


void OccluderEventHandler.endOccluder()
    if _convexPlanarOccluder.valid() :
        if _convexPlanarOccluder.getOccluder().getVertexList().size()>=3 :
            occluderNode =  new osg.OccluderNode
            occluderNode.setOccluder(_convexPlanarOccluder.get())

            if !_occluders.valid() :
                _occluders = new osg.Group
                if rootNode() : rootNode().addChild(_occluders.get())
            _occluders.addChild(occluderNode)

            print "created occluder"
        else:
            print "Occluder requires at least 3 points to create occluder."
    else:
        print "No occluder points to create occluder with."

    # reset current occluder.
    _convexPlanarOccluder = NULL


def createOccluder(v1, v2, v3, v4, holeRatio):
   # create an occluder which will sit alongside the loaded model.
    occluderNode =  new osg.OccluderNode

    # create the convex planar occluder
    cpo =  new osg.ConvexPlanarOccluder

    # attach it to the occluder node.
    occluderNode.setOccluder(cpo)
    occluderNode.setName("occluder")

    # set the occluder up for the front face of the bounding box.
    occluder =  cpo.getOccluder()
    occluder.add(v1)
    occluder.add(v2)
    occluder.add(v3)
    occluder.add(v4)

    # create a hole at the center of the occluder if needed.
    if holeRatio>0.0f :
        # create hole.
        ratio =  holeRatio
        one_minus_ratio =  1-ratio
        center =  (v1+v2+v3+v4)*0.25f
        v1dash =  v1*ratio + center*one_minus_ratio
        v2dash =  v2*ratio + center*one_minus_ratio
        v3dash =  v3*ratio + center*one_minus_ratio
        v4dash =  v4*ratio + center*one_minus_ratio

        hole = osg.ConvexPlanarPolygon()
        hole.add(v1dash)
        hole.add(v2dash)
        hole.add(v3dash)
        hole.add(v4dash)

        cpo.addHole(hole)


   # create a drawable for occluder.
    geom =  new osg.Geometry

    coords =  new osg.Vec3Array(occluder.getVertexList().begin(),occluder.getVertexList().end())
    geom.setVertexArray(coords)

    colors =  new osg.Vec4Array(1)
    (*colors)[0].set(1.0f,1.0f,1.0f,0.5f)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(new osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4))

    geode =  new osg.Geode
    geode.addDrawable(geom)

    stateset =  new osg.StateSet
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
    stateset.setMode(GL_BLEND,osg.StateAttribute.ON)
    stateset.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)

    geom.setStateSet(stateset)

    # add the occluder geode as a child of the occluder,
    # as the occluder can't self occlude its subgraph the
    # geode will never be occluded by this occluder.
    occluderNode.addChild(geode)

    occluderNode = return()


def createOccludersAroundModel(model):
    scene =  new osg.Group
    scene.setName("rootgroup")


    # add the loaded model into a the scene group.
    scene.addChild(model)
    model.setName("model")

    # get the bounding volume of the model.
    bs =  model.getBound()

    # create a bounding box around the sphere.
    bb = osg.BoundingBox()
    bb.expandBy(bs)

   # front
   scene.addChild(createOccluder(bb.corner(0),
                                  bb.corner(1),
                                  bb.corner(5),
                                  bb.corner(4)))

   # right side
   scene.addChild(createOccluder(bb.corner(1),
                                  bb.corner(3),
                                  bb.corner(7),
                                  bb.corner(5)))

   # left side
   scene.addChild(createOccluder(bb.corner(2),
                                  bb.corner(0),
                                  bb.corner(4),
                                  bb.corner(6)))

   # back side
   scene.addChild(createOccluder(bb.corner(3),
                                  bb.corner(2),
                                  bb.corner(6),
                                  bb.corner(7),
                                  0.5f)) # create a hole half the size of the occluder.

    scene = return()


def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use of convex planer occluders.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("-m","Mannually create occluders")

    # initialize the viewer.
    viewer = osgViewer.Viewer()

    manuallyCreateOccluders =  false
    while arguments.read("-m") :  manuallyCreateOccluders = true 

    if manuallyCreateOccluders :
        viewer.addEventHandler(new OccluderEventHandler(viewer))

    # if user requests help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # load the nodes from the commandline arguments.
    loadedmodel =  osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try using default mode instead.
    if !loadedmodel : loadedmodel = osgDB.readNodeFile("glider.osgt")

    if !loadedmodel :
        osg.notify(osg.NOTICE), "Please specify a model filename on the command line."
        return 1

    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(loadedmodel)

    # add the occluders to the loaded model.
    osg.ref_ptr<osg.Group> rootnode

    if manuallyCreateOccluders :
        rootnode = new osg.Group
        rootnode.addChild(loadedmodel)
    else:
        rootnode = createOccludersAroundModel(loadedmodel)


    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData( rootnode.get() )

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
