#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetshader"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgWidget


# Translated from file 'osgwidgetshader.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetshader.cpp 28 2008-03-26 15:26:48Z cubicool $

#include <osgDB/FileUtils>
#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Canvas>

MASK_2D = 0xF0000000

def createWidget(name, col, layer):

    
    widget = osgWidget.Widget(name, 200.0, 200.0)

    widget.setColor(col, col, col, 0.2)
    widget.setLayer(layer)

    return widget

def main(argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D
    )
    
    canvas = osgWidget.Canvas("canvas")

    canvas.attachMoveCallback()
    canvas.attachScaleCallback()

    canvas.addWidget(
        createWidget("w1", 0.2, osgWidget.Widget.LAYER_LOW),
        0.0,
        0.0
    )
    
    canvas.addWidget(
        createWidget("w2", 0.4, osgWidget.Widget.LAYER_MIDDLE),
        200.0,
        0.0
    )

    canvas.addWidget(
        createWidget("w3", 0.6, osgWidget.Widget.LAYER_HIGH),
        400.0,
        0.0
    )


    wm.addChild(canvas)

    program = osg.Program()

    program.addShader(osg.Shader.readShaderFile(
        osg.Shader.VERTEX,
        osgDB.findDataFile("osgWidget/osgwidgetshader-vert.glsl")
    ))
    
    program.addShader(osg.Shader.readShaderFile(
        osg.Shader.FRAGMENT,
        osgDB.findDataFile("osgWidget/osgwidgetshader-frag.glsl")
    ))

    canvas.getGeode().getOrCreateStateSet().setAttribute(program)

    return osgWidget.createExample(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
