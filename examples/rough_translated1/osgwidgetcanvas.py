#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetcanvas"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgWidget


# Translated from file 'osgwidgetcanvas.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetcanvas.cpp 33 2008-04-04 19:03:12Z cubicool $

#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Canvas>

MASK_2D = 0xF0000000

def colorWidgetEnter(event):

    
    event.getWidget().addColor(0.5, 0.2, 0.3, 0.0)

    # osgWidget.warn(), "WIDGET mouseEnter ", event.getWidget().getName()
    
    return False

def colorWidgetLeave(event):

    
    event.getWidget().addColor(-0.5, -0.2, -0.3, 0.0)

    # osgWidget.warn(), "WIDGET mouseLeave"
    
    return True

bool windowMouseOver(osgWidget.Event #event) 
    #osgWidget.XYCoord xy = event.getWindow().localXY(event.x, event.y)
    # osgWidget.warn(), "WINDOW ", xy.x(), " - ", xy.y()

    return True

bool widgetMouseOver(osgWidget.Event #event) 
    # osgWidget.XYCoord xy = event.getWidget().localXY(event.x, event.y)
    # osgWidget.warn(), "WIDGET mouseOver ", xy.x(), " - ", xy.y()

    return True

def createWidget(name, col, layer):

    
    widget = osgWidget.Widget(name, 200.0, 200.0)

    widget.setEventMask(osgWidget.EVENT_ALL)
    widget.addCallback(osgWidget.Callback(colorWidgetEnter, osgWidget.EVENT_MOUSE_PUSH))
    widget.addCallback(osgWidget.Callback(colorWidgetLeave, osgWidget.EVENT_MOUSE_RELEASE))
    widget.addCallback(osgWidget.Callback(colorWidgetEnter, osgWidget.EVENT_MOUSE_ENTER))
    widget.addCallback(osgWidget.Callback(colorWidgetLeave, osgWidget.EVENT_MOUSE_LEAVE))
    widget.addCallback(osgWidget.Callback(widgetMouseOver, osgWidget.EVENT_MOUSE_OVER))
    widget.setColor(col, col, col, 0.5)
    widget.setLayer(layer)
    
    return widget

def main(argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )
    
    canvas = osgWidget.Canvas("canvas")

    canvas.addCallback(osgWidget.Callback(windowMouseOver, osgWidget.EVENT_MOUSE_OVER))
    canvas.attachMoveCallback()
    canvas.attachRotateCallback()
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

    # Add a child and then resize it relatively to the size of the parent Window.
    relWidget = osgWidget.Widget("relative")

    relWidget.setLayer(osgWidget.Widget.LAYER_LOW, 1)
    relWidget.setCoordinateMode(osgWidget.Widget.CM_RELATIVE)
    relWidget.setSize(0.2, 0.2)
    relWidget.setColor(0.5, 0.5, 0.1, 0.9)

    osgWidget.warn(), canvas.getWidth()

    canvas.addWidget(relWidget, 0.4, 0.4)
    
    relWidget.addOrigin(0.1, 0.1)
    relWidget.addSize(0.2, 0.2)

    canvas.resize()

    # Finally, add the whole thing to the WindowManager.
    wm.addChild(canvas)

    return osgWidget.createExample(viewer, wm)

#
#def main(argv):
#    
#    viewer = osgViewer.Viewer()
#
#    wm = osgWidget.WindowManager(
#        viewer,
#        1280.0,
#        1024.0,
#        MASK_2D,
#        osgWidget.WindowManager.WM_PICK_DEBUG
#    )
#    
#    canvas = osgWidget.Canvas("canvas")
#
#    canvas.addWidget(osgWidget.Widget("spacer", 2.0, 300.0), 1280.0, 0.0)
#
#    canvas.setOrigin(0.0, 300.0)
#
#    wm.addChild(canvas)
#
#    return osgWidget.createExample(viewer, wm)
#
#


if __name__ == "__main__":
    main(sys.argv)
