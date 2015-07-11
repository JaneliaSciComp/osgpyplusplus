#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetprogress"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgWidget

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id$

#include <osgDB/ReadFile>
#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Canvas>

 unsigned int MASK_2D = 0xF0000000

struct UpdateProgressNode: public osg.NodeCallback 
    start = float()
    done = float()

    UpdateProgressNode():
    start (0.0f),
    done  (5.0f) 

    virtual void operator()(osg.Node* node, osg.NodeVisitor* nv) 
        fs =  nv.getFrameStamp()

        t =  fs.getSimulationTime()

        if start == 0.0f : start = t

        width =  ((t - start) / done) * 512.0f
        percent =  (width / 512.0f) * 100.0f
    
        if width < 1.0f || width > 512.0f : return

        window =  dynamic_cast<osgWidget.Window*>(node)

        if !window : return

        w =  window.getByName("pMeter")
        l =  dynamic_cast<osgWidget.Label*>(window.getByName("pLabel"))

        if !w || !l : return

        w.setWidth(width)
        w.setTexCoordRegion(0.0f, 0.0f, width, 64.0f)

        ss = std.ostringstream()

        ss, osg.round(percent), "% Done"

        l.setLabel(ss.str())


def main(argc, argv):
    viewer = osgViewer.Viewer()

    wm =  new osgWidget.WindowManager(
        viewer,
        1280.0f,
        1024.0f,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )
    
    canvas =  new osgWidget.Canvas("canvas")
    pOutline =  new osgWidget.Widget("pOutline", 512.0f, 64.0f)
    pMeter =  new osgWidget.Widget("pMeter", 0.0f, 64.0f)
    pLabel =  new osgWidget.Label("pLabel", "0% Done")

    pOutline.setImage("osgWidget/progress-outline.png", true)
    pOutline.setLayer(osgWidget.Widget.LAYER_MIDDLE, 2)
    
    pMeter.setImage("osgWidget/progress-meter.png")
    pMeter.setColor(0.7f, 0.1f, 0.1f, 0.7f)
    pMeter.setLayer(osgWidget.Widget.LAYER_MIDDLE, 1)

    pLabel.setFont("fonts/VeraMono.ttf")
    pLabel.setFontSize(20)
    pLabel.setFontColor(1.0f, 1.0f, 1.0f, 1.0f)
    pLabel.setSize(512.0f, 64.0f)
    pLabel.setLayer(osgWidget.Widget.LAYER_MIDDLE, 3)

    canvas.setOrigin(300.0f, 300.0f)
    canvas.addWidget(pMeter, 0.0f, 0.0f)
    canvas.addWidget(pOutline, 0.0f, 0.0f)
    canvas.addWidget(pLabel, 0.0f, 0.0f)
    canvas.getBackground().setColor(0.0f, 0.0f, 0.0f, 0.0f)
    canvas.setUpdateCallback(new UpdateProgressNode())

    wm.addChild(canvas)

    return osgWidget.createExample(viewer, wm, osgDB.readNodeFile("cow.osgt"))


if __name__ == "__main__":
    main(sys.argv)
