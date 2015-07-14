#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetprogress"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgWidget


# Translated from file 'osgwidgetprogress.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id$

#include <osgDB/ReadFile>
#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Canvas>

MASK_2D = 0xF0000000

class UpdateProgressNode (osg.NodeCallback) :
start = float()
    done = float()

    UpdateProgressNode():
    start (0.0),
    done  (5.0) 

    virtual void operator()(osg.Node* node, osg.NodeVisitor* nv) 
        fs = nv.getFrameStamp()

        t = fs.getSimulationTime()

        if start == 0.0 : start = t

        width = ((t - start) / done) * 512.0
        percent = (width / 512.0) * 100.0
    
        if width < 1.0  or  width > 512.0 : return

        window = dynamic_cast<osgWidget.Window*>(node)

        if  not window : return

        w = window.getByName("pMeter")
        l = dynamic_cast<osgWidget.Label*>(window.getByName("pLabel"))

        if  not w  or   not l : return

        w.setWidth(width)
        w.setTexCoordRegion(0.0, 0.0, width, 64.0)

        ss = std.ostringstream()

        ss, osg.round(percent), "% Done"

        l.setLabel(ss.str())


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
    pOutline = osgWidget.Widget("pOutline", 512.0, 64.0)
    pMeter = osgWidget.Widget("pMeter", 0.0, 64.0)
    pLabel = osgWidget.Label("pLabel", "0% Done")

    pOutline.setImage("osgWidget/progress-outline.png", True)
    pOutline.setLayer(osgWidget.Widget.LAYER_MIDDLE, 2)
    
    pMeter.setImage("osgWidget/progress-meter.png")
    pMeter.setColor(0.7, 0.1, 0.1, 0.7)
    pMeter.setLayer(osgWidget.Widget.LAYER_MIDDLE, 1)

    pLabel.setFont("fonts/VeraMono.ttf")
    pLabel.setFontSize(20)
    pLabel.setFontColor(1.0, 1.0, 1.0, 1.0)
    pLabel.setSize(512.0, 64.0)
    pLabel.setLayer(osgWidget.Widget.LAYER_MIDDLE, 3)

    canvas.setOrigin(300.0, 300.0)
    canvas.addWidget(pMeter, 0.0, 0.0)
    canvas.addWidget(pOutline, 0.0, 0.0)
    canvas.addWidget(pLabel, 0.0, 0.0)
    canvas.getBackground().setColor(0.0, 0.0, 0.0, 0.0)
    canvas.setUpdateCallback(UpdateProgressNode())

    wm.addChild(canvas)

    return osgWidget.createExample(viewer, wm, osgDB.readNodeFile("cow.osgt"))


if __name__ == "__main__":
    main(sys.argv)
