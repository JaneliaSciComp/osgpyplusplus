#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgpick"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgpick.cpp'

# OpenSceneGraph example, osgpick.
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

# osgpick sample
#* demonstrate use of osgUtil/PickVisitor for picking in a HUD or
#* in a 3d scene,
#

#include <osgUtil/Optimizer>
#include <osgDB/ReadFile>
#include <osgViewer/Viewer>
#include <osgViewer/CompositeViewer>

#include <osgGA/TerrainManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <osg/Material>
#include <osg/Geode>
#include <osg/BlendFunc>
#include <osg/Depth>
#include <osg/Projection>
#include <osg/MatrixTransform>
#include <osg/Camera>
#include <osg/io_utils>
#include <osg/ShapeDrawable>

#include <osgText/Text>

#include <sstream>

# class to handle events with a pick
class PickHandler (osgGA.GUIEventHandler) :

    PickHandler(osgText.Text* updateText):
        _updateText(updateText) 

    ~PickHandler() 

    handle = bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa)

    pick = virtual void(osgViewer.View* view,  osgGA.GUIEventAdapter ea)

    def setLabel(name):

        
        if _updateText.get() : _updateText.setText(name)

    _updateText = osgText.Text()


bool PickHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.PUSH):
            view = dynamic_cast<osgViewer.View*>(aa)
            if view : pick(view,ea)
            return False
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()=='c' :
                view = dynamic_cast<osgViewer.View*>(aa)
                event = osgGA.GUIEventAdapter(ea)
                event.setX((ea.getXmin()+ea.getXmax())*0.5)
                event.setY((ea.getYmin()+ea.getYmax())*0.5)
                if view : pick(view,*event)
            return False
        default:
            return False

void PickHandler.pick(osgViewer.View* view,  osgGA.GUIEventAdapter ea)
    intersections = osgUtil.LineSegmentIntersector.Intersections()

    gdlist = ""

    if view.computeIntersections(ea,intersections) :
        for(osgUtil.LineSegmentIntersector.Intersections.iterator hitr = intersections.begin()
            hitr != intersections.end()
            ++hitr)
            os = std.ostringstream()
            if !hitr.nodePath.empty()  !(hitr.nodePath.back().getName().empty()) :
                # the geodes are identified by name.
                os, "Object \"", hitr.nodePath.back().getName(), "\""
            elif hitr.drawable.valid() :
                os, "Object \"", hitr.drawable.className(), "\""

            os, "        local coords vertex(", hitr.getLocalIntersectPoint(), ")", "  normal(", hitr.getLocalIntersectNormal(), ")"
            os, "        world coords vertex(", hitr.getWorldIntersectPoint(), ")", "  normal(", hitr.getWorldIntersectNormal(), ")"
            vil = hitr.indexList
            for(unsigned int i=0i<vil.size()++i)
                os, "        vertex indices [", i, "] = ", vil[i]

            gdlist += os.str()
    setLabel(gdlist)

def createHUD(updateText):

    

    # create the hud. derived from osgHud.cpp
    # adds a set of quads, each in a separate Geode - which can be picked individually
    # eg to be used as a menuing/help system!
    # Can pick texts too!

    hudCamera = osg.Camera()
    hudCamera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    hudCamera.setProjectionMatrixAsOrtho2D(0,1280,0,1024)
    hudCamera.setViewMatrix(osg.Matrix.identity())
    hudCamera.setRenderOrder(osg.Camera.POST_RENDER)
    hudCamera.setClearMask(GL_DEPTH_BUFFER_BIT)

    timesFont = str("fonts/times.ttf")

    # turn lighting off for the text and disable depth test to ensure its always ontop.
    position = osg.Vec3(150.0,800.0,0.0)
    delta = osg.Vec3(0.0,-60.0,0.0)

        geode = osg.Geode()
        stateset = geode.getOrCreateStateSet()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
        geode.setName("simple")
        hudCamera.addChild(geode)

        text = osgText.Text()
        geode.addDrawable( text )

        text.setFont(timesFont)
        text.setText("Picking in Head Up Displays is simple!")
        text.setPosition(position)

        position += delta


    for (int i=0 i<5 i++) 
        dy = osg.Vec3(0.0,-30.0,0.0)
        dx = osg.Vec3(120.0,0.0,0.0)
        geode = osg.Geode()
        stateset = geode.getOrCreateStateSet()
         char *opts[]="One", "Two", "Three", "January", "Feb", "2003"
        quad = osg.Geometry()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
        name = "subOption"
        name += " "
        name += str(opts[i])
        geode.setName(name)
        vertices = osg.Vec3Array(4) # 1 quad
        colors = osg.Vec4Array()
        colors = osg.Vec4Array()
        colors.push_back(osg.Vec4(0.8-0.1*i,0.1*i,0.2*i, 1.0))
        quad.setColorArray(colors, osg.Array.BIND_OVERALL)
        (*vertices)[0]=position
        (*vertices)[1]=position+dx
        (*vertices)[2]=position+dx+dy
        (*vertices)[3]=position+dy
        quad.setVertexArray(vertices)
        quad.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4))
        geode.addDrawable(quad)
        hudCamera.addChild(geode)

        position += delta



     # this displays what has been selected
        geode = osg.Geode()
        stateset = geode.getOrCreateStateSet()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
        geode.setName("The text label")
        geode.addDrawable( updateText )
        hudCamera.addChild(geode)

        updateText.setCharacterSize(20.0)
        updateText.setFont(timesFont)
        updateText.setColor(osg.Vec4(1.0,1.0,0.0,1.0))
        updateText.setText("")
        updateText.setPosition(position)
        updateText.setDataVariance(osg.Object.DYNAMIC)

        position += delta

    return hudCamera


def main(argc, argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # read the scene from the list of file specified commandline args.
    scene = osgDB.readNodeFiles(arguments)

    if !scene  arguments.read("--relative-camera-scene") :
        # Create a test scene with a camera that has a relative reference frame.
        group = osg.Group()

        sphere = osg.Geode()
        sphere.setName("Sphere")
        sphere.addDrawable(osg.ShapeDrawable(osg.Sphere()))

        cube = osg.Geode()
        cube.setName("Cube")
        cube.addDrawable(osg.ShapeDrawable(osg.Box()))

        camera = osg.Camera()
        camera.setRenderOrder(osg.Camera.POST_RENDER)
        camera.setClearMask(GL_DEPTH_BUFFER_BIT)
        camera.setReferenceFrame(osg.Transform.RELATIVE_RF)
        camera.setViewMatrix(osg.Matrix.translate(-2, 0, 0))

        xform = osg.MatrixTransform(osg.Matrix.translate(1, 1, 1))
        xform.addChild(camera)

        group.addChild(sphere)
        group.addChild(xform)
        camera.addChild(cube)

        scene = group

    # if not loaded assume no arguments passed in, try use default mode instead.
    if !scene : scene = osgDB.readNodeFile("fountain.osgt")

    group = dynamic_cast<osg.Group*>(scene.get())
    if !group :
        group = osg.Group()
        group.addChild(scene.get())

    updateText = osgText.Text()

    # add the HUD subgraph.
    group.addChild(createHUD(updateText.get()))

    if arguments.read("--CompositeViewer") :
        view = osgViewer.View()
        # add the handler for doing the picking
        view.addEventHandler(PickHandler(updateText.get()))

        # set the scene to render
        view.setSceneData(group.get())

        view.setUpViewAcrossAllScreens()

        viewer = osgViewer.CompositeViewer()
        viewer.addView(view.get())

        return viewer.run()

    else :
        viewer = osgViewer.Viewer()


        # add all the camera manipulators
            keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

            keyswitchManipulator.addMatrixManipulator( '1', "Trackball", osgGA.TrackballManipulator() )
            keyswitchManipulator.addMatrixManipulator( '2', "Flight", osgGA.FlightManipulator() )
            keyswitchManipulator.addMatrixManipulator( '3', "Drive", osgGA.DriveManipulator() )

            num = keyswitchManipulator.getNumMatrixManipulators()
            keyswitchManipulator.addMatrixManipulator( '4', "Terrain", osgGA.TerrainManipulator() )

            pathfile = str()
            keyForAnimationPath = '5'
            while arguments.read("-p",pathfile) :
                apm = osgGA.AnimationPathManipulator(pathfile)
                if apm || !apm.valid() :
                    num = keyswitchManipulator.getNumMatrixManipulators()
                    keyswitchManipulator.addMatrixManipulator( keyForAnimationPath, "Path", apm )
                    ++keyForAnimationPath

            keyswitchManipulator.selectMatrixManipulator(num)

            viewer.setCameraManipulator( keyswitchManipulator.get() )

        # add the handler for doing the picking
        viewer.addEventHandler(PickHandler(updateText.get()))

        # set the scene to render
        viewer.setSceneData(group.get())

        return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
