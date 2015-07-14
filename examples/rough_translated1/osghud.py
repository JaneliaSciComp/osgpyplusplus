#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osghud"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osghud.cpp'

# OpenSceneGraph example, osghud.
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

#include <osgUtil/Optimizer>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>
#include <osgViewer/CompositeViewer>

#include <osgGA/TrackballManipulator>

#include <osg/Material>
#include <osg/Geode>
#include <osg/BlendFunc>
#include <osg/Depth>
#include <osg/PolygonOffset>
#include <osg/MatrixTransform>
#include <osg/Camera>
#include <osg/RenderInfo>

#include <osgDB/WriteFile>

#include <osgText/Text>


def createHUD():


    
    # create a camera to set up the projection and model view matrices, and the subgraph to draw in the HUD
    camera = osg.Camera()

    # set the projection matrix
    camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1280,0,1024))

    # set the view matrix
    camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    camera.setViewMatrix(osg.Matrix.identity())

    # only clear the depth buffer
    camera.setClearMask(GL_DEPTH_BUFFER_BIT)

    # draw subgraph after main camera view.
    camera.setRenderOrder(osg.Camera.POST_RENDER)

    # we don't want the camera to grab event focus from the viewers main camera(s).
    camera.setAllowEventFocus(False)



    # add to this camera a subgraph to render

        geode = osg.Geode()

        timesFont = str("fonts/arial.ttf")

        # turn lighting off for the text and disable depth test to ensure it's always ontop.
        stateset = geode.getOrCreateStateSet()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

        position = osg.Vec3(150.0,800.0,0.0)
        delta = osg.Vec3(0.0,-120.0,0.0)

            text = osgText.Text()
            geode.addDrawable( text )

            text.setFont(timesFont)
            text.setPosition(position)
            text.setText("Head Up Displays are simple :-)")

            position += delta


            text = osgText.Text()
            geode.addDrawable( text )

            text.setFont(timesFont)
            text.setPosition(position)
            text.setText("All you need to do is create your text in a subgraph.")

            position += delta


            text = osgText.Text()
            geode.addDrawable( text )

            text.setFont(timesFont)
            text.setPosition(position)
            text.setText("Then place an osg.Camera above the subgraph\n"
                          "to create an orthographic projection.\n")

            position += delta

            text = osgText.Text()
            geode.addDrawable( text )

            text.setFont(timesFont)
            text.setPosition(position)
            text.setText("Set the Camera's ReferenceFrame to ABSOLUTE_RF to ensure\n"
                          "it remains independent from any external model view matrices.")

            position += delta

            text = osgText.Text()
            geode.addDrawable( text )

            text.setFont(timesFont)
            text.setPosition(position)
            text.setText("And set the Camera's clear mask to just clear the depth buffer.")

            position += delta

            text = osgText.Text()
            geode.addDrawable( text )

            text.setFont(timesFont)
            text.setPosition(position)
            text.setText("And finally set the Camera's RenderOrder to POST_RENDER\n"
                          "to make sure it's drawn last.")

            position += delta


            bb = osg.BoundingBox()
            for(unsigned int i=0i<geode.getNumDrawables()++i)
                bb.expandBy(geode.getDrawable(i).getBound())

            geom = osg.Geometry()

            vertices = osg.Vec3Array()
            depth = bb.zMin()-0.1
            vertices.push_back(osg.Vec3(bb.xMin(),bb.yMax(),depth))
            vertices.push_back(osg.Vec3(bb.xMin(),bb.yMin(),depth))
            vertices.push_back(osg.Vec3(bb.xMax(),bb.yMin(),depth))
            vertices.push_back(osg.Vec3(bb.xMax(),bb.yMax(),depth))
            geom.setVertexArray(vertices)

            normals = osg.Vec3Array()
            normals.push_back(osg.Vec3(0.0,0.0,1.0))
            geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

            colors = osg.Vec4Array()
            colors.push_back(osg.Vec4(1.0,1.0,0.8,0.2))
            geom.setColorArray(colors, osg.Array.BIND_OVERALL)

            geom.addPrimitiveSet(osg.DrawArrays(GL_QUADS,0,4))

            stateset = geom.getOrCreateStateSet()
            stateset.setMode(GL_BLEND,osg.StateAttribute.ON)
            #stateset.setAttribute(osg.PolygonOffset(1.0,1.0),osg.StateAttribute.ON)
            stateset.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)

            geode.addDrawable(geom)

        camera.addChild(geode)

    return camera

class SnapImage (osg.Camera.DrawCallback) :
SnapImage( str filename):
        _filename(filename),
        _snapImage(False)
        _image = osg.Image()

    virtual void operator () (osg.RenderInfo renderInfo) 

        if  not _snapImage : return

        osg.notify(osg.NOTICE), "Camera callback"

        camera = renderInfo.getCurrentCamera()
        viewport =  camera.getViewport() if (camera) else  0

        osg.notify(osg.NOTICE), "Camera callback ", camera, " ", viewport

        if viewport  and  _image.valid() :
            _image.readPixels(int(viewport.x()),int(viewport.y()),int(viewport.width()),int(viewport.height()),
                               GL_RGBA,
                               GL_UNSIGNED_BYTE)
            osgDB.writeImageFile(*_image, _filename)

            osg.notify(osg.NOTICE), "Taken screenshot, and written to '", _filename, "'"

        _snapImage = False

    _filename = str()
    mutable bool                        _snapImage
    mutable osg.Image    _image


class SnapeImageHandler (osgGA.GUIEventHandler) :
SnapeImageHandler(int key,SnapImage* si):
        _key(key),
        _snapImage(si) 

    bool handle( osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter)
        if ea.getHandled() : return False

        switch(ea.getEventType())
            case(osgGA.GUIEventAdapter.KEYUP):
                if ea.getKey() == _key :
                    osg.notify(osg.NOTICE), "event handler"
                    _snapImage._snapImage = True
                    return True

                break
        default:
            break

        return False

    _key = int()
    _snapImage = SnapImage()



def main(argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)


    # read the scene from the list of file specified commandline args.
    scene = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default model instead.
    if  not scene : scene = osgDB.readNodeFile("dumptruck.osgt")


    if  not scene :
        osg.notify(osg.NOTICE), "No model loaded"
        return 1


    if arguments.read("--Viewer") :
        # construct the viewer.
        viewer = osgViewer.Viewer()

        # create a HUD as slave camera attached to the master view.

        viewer.setUpViewAcrossAllScreens()

        windows = osgViewer.Viewer.Windows()
        viewer.getWindows(windows)

        if windows.empty() : return 1

        hudCamera = createHUD()

        # set up cameras to render on the first window available.
        hudCamera.setGraphicsContext(windows[0])
        hudCamera.setViewport(0,0,windows[0].getTraits().width, windows[0].getTraits().height)

        viewer.addSlave(hudCamera, False)

        # set the scene to render
        viewer.setSceneData(scene)

        return viewer.run()

    if arguments.read("--CompositeViewer") :
        # construct the viewer.
        viewer = osgViewer.CompositeViewer()

        # create the main 3D view
        view = osgViewer.View()
        viewer.addView(view)

        view.setSceneData(scene)
        view.setUpViewAcrossAllScreens()
        view.setCameraManipulator(osgGA.TrackballManipulator)()

        # now create the HUD camera's view

        windows = osgViewer.Viewer.Windows()
        viewer.getWindows(windows)

        if windows.empty() : return 1

        hudCamera = createHUD()

        # set up cameras to render on the first window available.
        hudCamera.setGraphicsContext(windows[0])
        hudCamera.setViewport(0,0,windows[0].getTraits().width, windows[0].getTraits().height)

        hudView = osgViewer.View()
        hudView.setCamera(hudCamera)

        viewer.addView(hudView)

        return viewer.run()

    else:
        # construct the viewer.
        viewer = osgViewer.Viewer()

        postDrawCallback = SnapImage("PostDrawCallback.png")
        viewer.getCamera().setPostDrawCallback(postDrawCallback)
        viewer.addEventHandler(SnapeImageHandler(ord("p"),postDrawCallback))

        finalDrawCallback = SnapImage("FinalDrawCallback.png")
        viewer.getCamera().setFinalDrawCallback(finalDrawCallback)
        viewer.addEventHandler(SnapeImageHandler(ord("f"),finalDrawCallback))

        group = osg.Group()

        # add the HUD subgraph.
        if scene.valid() : group.addChild(scene)
        group.addChild(createHUD())

        # set the scene to render
        viewer.setSceneData(group)

        return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
