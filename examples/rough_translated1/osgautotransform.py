#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgautotransform"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgautotransform.
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


#include <osgUtil/Optimizer>
#include <osgDB/ReadFile>
#include <osgViewer/Viewer>

#include <osg/Material>
#include <osg/Geode>
#include <osg/BlendFunc>
#include <osg/Depth>
#include <osg/Projection>
#include <osg/AutoTransform>
#include <osg/Geometry>

#include <osgDB/WriteFile>

#include <osgText/Text>

#include <iostream>

def createLabel(pos, size, label, axisAlignment):
    geode =  new osg.Geode()

    timesFont = str("fonts/arial.ttf")

        text =  new  osgText.Text
        geode.addDrawable( text )

        text.setFont(timesFont)
        text.setPosition(pos)
        text.setCharacterSize(size)
        text.setAxisAlignment(axisAlignment)
        text.setAlignment(osgText.Text.CENTER_CENTER)
        text.setText(label)


    geode = return()


def createLabel3(pos, size, label):
    geode =  new osg.Geode()

    timesFont = str("fonts/arial.ttf")

        text =  new  osgText.Text
        geode.addDrawable( text )

        text.setFont(timesFont)
        text.setPosition(pos)
        text.setFontResolution(40,40)
        text.setCharacterSize(size)
        text.setAlignment(osgText.Text.CENTER_CENTER)
        text.setAutoRotateToScreen(true)
        text.setCharacterSizeMode(osgText.Text.OBJECT_COORDS_WITH_MAXIMUM_SCREEN_SIZE_CAPPED_BY_FONT_HEIGHT)
        text.setText(label)


    geode = return()

def createAxis(s, e, numReps, autoRotateMode, axisAlignment, str):
    group =  new osg.Group

    dv =  e-s
    dv /= float(numReps-1)

    pos =  s

    useAuto =  true
    if useAuto :
        vertices =  new osg.Vec3Array

        for(int i=0i<numReps++i)
            at =  new osg.AutoTransform
            at.setPosition(pos)
            at.setAutoRotateMode(autoRotateMode)
            at.addChild(createLabel(osg.Vec3(0.0f,0.0f,0.0f),dv.length()*0.2f,str, axisAlignment))
            vertices.push_back(pos)
            pos += dv


            group.addChild(at)

        colors =  new osg.Vec4Array
        colors.push_back(osg.Vec4(1.0f,1.0f,1.0f,1.0f))

        geom =  new osg.Geometry
        geom.setVertexArray(vertices)
        geom.setColorArray(colors, osg.Array.BIND_OVERALL)
        geom.addPrimitiveSet(new osg.DrawArrays(GL_LINE_STRIP,0,vertices.size()))

        geode =  new osg.Geode
        geode.addDrawable(geom)

        group.addChild(geode)
    else:
        vertices =  new osg.Vec3Array

        for(int i=0i<numReps++i)
            group.addChild(createLabel3(osg.Vec3(pos),dv.length()*0.5f,str))
            vertices.push_back(pos)
            pos += dv



        colors =  new osg.Vec4Array
        colors.push_back(osg.Vec4(1.0f,1.0f,1.0f,1.0f))

        geom =  new osg.Geometry
        geom.setVertexArray(vertices)
        geom.setColorArray(colors, osg.Array.BIND_OVERALL)
        geom.addPrimitiveSet(new osg.DrawArrays(GL_LINE_STRIP,0,vertices.size()))

        geode =  new osg.Geode
        geode.addDrawable(geom)

        group.addChild(geode)

    group = return()

def createAutoScale(position, characterSize, message, minScale, maxScale):
    timesFont = str("fonts/arial.ttf")

    text =  new osgText.Text
    text.setCharacterSize(characterSize)
    text.setText(message)
    text.setFont(timesFont)
    text.setAlignment(osgText.Text.CENTER_CENTER)

    geode =  new osg.Geode
    geode.addDrawable(text)
    geode.getOrCreateStateSet().setMode(GL_LIGHTING, osg.StateAttribute.OFF)

    at =  new osg.AutoTransform
    at.addChild(geode)

    at.setAutoRotateMode(osg.AutoTransform.ROTATE_TO_SCREEN)
    at.setAutoScaleToScreen(true)
    at.setMinimumScale(minScale)
    at.setMaximumScale(maxScale)
    at.setPosition(position)

    at = return()

def createScene():
    root =  new osg.Group

#    int numReps = 3333
    numReps =  10
    root.addChild(createAxis(osg.Vec3(0.0,0.0,0.0),osg.Vec3(1000.0,0.0,0.0),numReps,osg.AutoTransform.ROTATE_TO_CAMERA,osgText.Text.XY_PLANE, "ROTATE_TO_CAMERA"))
    root.addChild(createAxis(osg.Vec3(0.0,0.0,0.0),osg.Vec3(0.0,1000.0,0.0),numReps,osg.AutoTransform.ROTATE_TO_SCREEN,osgText.Text.XY_PLANE, "ROTATE_TO_SCREEN"))
    root.addChild(createAxis(osg.Vec3(0.0,0.0,0.0),osg.Vec3(0.0,0.0,1000.0),numReps,osg.AutoTransform.NO_ROTATION,osgText.Text.XZ_PLANE, "NO_ROTATION"))

    root.addChild(createAutoScale(osg.Vec3(500.0,500.0,500.0), 25.0, "AutoScale with no min, max limits"))
    root.addChild(createAutoScale(osg.Vec3(500.0,500.0,300.0), 25.0, "AutoScale with minScale = 1, maxScale = 2.0 ", 1, 2.0))
    root.addChild(createAutoScale(osg.Vec3(500.0,500.0,700.0), 25.0, "AutoScale with minScale = 0.0, maxScale = 5.0 ", 0.0, 5.0))
    root = return()

int main(int, char**)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # set the scene to render
    viewer.setSceneData(createScene())

    # run the viewers frame loop
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
