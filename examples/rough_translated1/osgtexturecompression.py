#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgtexturecompression"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osgtexturecompression.cpp'

# OpenSceneGraph example, osgtexture3D.
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

#include <osg/Node>
#include <osg/Geometry>
#include <osg/Notify>
#include <osg/Texture2D>
#include <osg/TexGen>
#include <osg/Geode>

#include <osgDB/ReadFile>

#include <osgText/Text>

#include <osgGA/TrackballManipulator>
#include <osgViewer/CompositeViewer>

#include <iostream>

def createHUD(label):

    
    # create a camera to set up the projection and model view matrices, and the subgraph to drawn in the HUD
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

        font = str("fonts/arial.ttf")

        # turn lighting off for the text and disable depth test to ensure its always ontop.
        stateset = geode.getOrCreateStateSet()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

        position = osg.Vec3(150.0,150.0,0.0)

        text = osgText.Text()
        geode.addDrawable( text )

        text.setFont(font)
        text.setPosition(position)
        text.setCharacterSize(100.0)
        text.setText(label)

        camera.addChild(geode)

    return camera

def creatQuad(name, image, formatMode, minFilter):

    

    group = osg.Group()
    
        geode = osg.Geode()

        geode.addDrawable(createTexturedQuadGeometry(
                osg.Vec3(0.0,0.0,0.0),
                osg.Vec3(float(image.s()),0.0,0.0),
                osg.Vec3(0.0,0.0,float(image.t()))))

        geode.setName(name)

        stateset = geode.getOrCreateStateSet()

        texture = osg.Texture2D(image)
        texture.setInternalFormatMode(formatMode)
        texture.setFilter(osg.Texture.MIN_FILTER, minFilter)
        stateset.setTextureAttributeAndModes(0, texture, osg.StateAttribute.ON)
        
        group.addChild(geode)
    
        group.addChild(createHUD(name))
    
    return group

def main(argv):

    
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.CompositeViewer(arguments)
    
    if arguments.argc()<=1 :
        print "Please supply an image filename on the commnand line."
        return 1
    
    filename = arguments[1]
    image = osgDB.readImageFile(filename)
    
    if  not image :
        print "Error: unable able to read image from ", filename
        return 1

    wsi = osg.GraphicsContext.getWindowingSystemInterface()
    if  not wsi : 
        osg.notify(osg.NOTICE), "Error, no WindowSystemInterface available, cannot create windows."
        return 1


    unsigned int width, height
    wsi.getScreenResolution(osg.GraphicsContext.ScreenIdentifier(0), width, height)

    traits = osg.GraphicsContext.Traits()
    traits.x = 0
    traits.y = 0
    traits.width = width
    traits.height = height
    traits.windowDecoration = False
    traits.doubleBuffer = True
    
    gc = osg.GraphicsContext.createGraphicsContext(traits)
    if  not gc :
        print "Error: GraphicsWindow has not been created successfully."

    gc.setClearColor(osg.Vec4(0.0,0.0,0.0,1.0))
    gc.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    trackball = osgGA.TrackballManipulator()
    
    typedef std.vector< osg.Node > Models
    
    models = Models()
    models.push_back(creatQuad("no compression", image, osg.Texture.USE_IMAGE_DATA_FORMAT, osg.Texture.LINEAR))
    models.push_back(creatQuad("ARB compression", image, osg.Texture.USE_ARB_COMPRESSION, osg.Texture.LINEAR))
    models.push_back(creatQuad("DXT1 compression", image, osg.Texture.USE_S3TC_DXT1_COMPRESSION, osg.Texture.LINEAR))
    models.push_back(creatQuad("DXT3 compression", image, osg.Texture.USE_S3TC_DXT3_COMPRESSION, osg.Texture.LINEAR))
    models.push_back(creatQuad("DXT5 compression", image, osg.Texture.USE_S3TC_DXT5_COMPRESSION, osg.Texture.LINEAR))
    
    numX = 1
    numY = 1

    # compute the number of views up and across that are need
        aspectRatio = float(width)/float(height)
        multiplier = sqrtf(float(models.size())/aspectRatio)
        multiplier_x = multiplier*aspectRatio
        multiplier_y = multiplier


        if multiplier_x/ceilf(multiplier_x) : > (multiplier_y/ceilf(multiplier_y)) :
            numX = int(ceilf(multiplier_x))
            numY = int(ceilf(float(models.size())/float(numX)))
        else:
            numY = int(ceilf(multiplier_y))
            numX = int(ceilf(float(models.size())/float(numY)))

    # populate the view with the required view to view each model.
    for(unsigned int i=0 i<models.size() ++i)
        view = osgViewer.View()
        
        xCell = i % numX
        yCell = i / numX
    
        vx = int((float(xCell)/float(numX)) * float(width))
        vy = int((float(yCell)/float(numY)) * float(height))
        vw = int(float(width) / float(numX))
        vh = int(float(height) / float(numY))

        view.setSceneData(models[i])
        view.getCamera().setProjectionMatrixAsPerspective(30.0, double(vw) / double(vh), 1.0, 1000.0)
        view.getCamera().setViewport(osg.Viewport(vx, vy, vw, vh))    
        view.getCamera().setGraphicsContext(gc)
        view.getCamera().setClearMask(0)
        view.setCameraManipulator(trackball)

        viewer.addView(view)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
