#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetbox"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgWidget


# Translated from file 'osgwidgetbox.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetbox.cpp 59 2008-05-15 20:55:31Z cubicool $

# NOTE: You'll find this example very similar to osgwidgetwindow. However, here we
# demonstrate a bit of subclassing of Widget so that we can respond to events
# such as mouseEnter and mouseLeave. We also demonstrate the use of padding, though
# fill and alignment should be working too.

#include <osg/io_utils>
#include <osgDB/ReadFile>
#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Box>

MASK_2D = 0xF0000000
MASK_3D = 0x0F000000

class ColorWidget (osgWidget.Widget) :
ColorWidget():
    osgWidget.Widget("", 256.0, 256.0) 
        setEventMask(osgWidget.EVENT_ALL)

    bool mouseEnter(double, double,  osgWidget.WindowManager*) 
        addColor(-osgWidget.Color(0.4, 0.4, 0.4, 0.0))
        
        # osgWidget.warn(), "enter: ", getColor()

        return True

    bool mouseLeave(double, double,  osgWidget.WindowManager*) 
        addColor(osgWidget.Color(0.4, 0.4, 0.4, 0.0))
        
        # osgWidget.warn(), "leave: ", getColor()
        
        return True

    bool mouseOver(double x, double y,  osgWidget.WindowManager*) 
        
        c = getImageColorAtPointerXY(x, y)

        if c.a() < 0.001 : 
            # osgWidget.warn(), "Transparent Pixel: ", x, " ", y

            return False
        return True

    bool keyUp(int key, int keyMask, osgWidget.WindowManager*) 
        # osgWidget.warn(), "...", key, " - ", keyMask

        return True


def createBox(name, bt):

    
    box = osgWidget.Box(name, bt, True)
    widget1 = osgWidget.Widget(name + "_widget1", 100.0, 100.0)
    widget2 = osgWidget.Widget(name + "_widget2", 100.0, 100.0)
    widget3 = ColorWidget()

    widget1.setColor(0.3, 0.3, 0.3, 1.0)
    widget2.setColor(0.6, 0.6, 0.6, 1.0)

    widget3.setImage("osgWidget/natascha.png")
    widget3.setTexCoord(0.0, 0.0, osgWidget.Widget.LOWER_LEFT)
    widget3.setTexCoord(1.0, 0.0, osgWidget.Widget.LOWER_RIGHT)
    widget3.setTexCoord(1.0, 1.0, osgWidget.Widget.UPPER_RIGHT)
    widget3.setTexCoord(0.0, 1.0, osgWidget.Widget.UPPER_LEFT)

    box.addWidget(widget1)
    box.addWidget(widget2)
    box.addWidget(widget3)

    return box

def main(argc, argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )
    
    wm.setPointerFocusMode(osgWidget.WindowManager.PFM_SLOPPY)

    box1 = createBox("HBOX", osgWidget.Box.HORIZONTAL)
    box2 = createBox("VBOX", osgWidget.Box.VERTICAL)
    box3 = createBox("HBOX2", osgWidget.Box.HORIZONTAL)
    box4 = createBox("VBOX2", osgWidget.Box.VERTICAL)

    box1.getBackground().setColor(1.0, 0.0, 0.0, 0.8)
    box1.attachMoveCallback()

    box2.getBackground().setColor(0.0, 1.0, 0.0, 0.8)
    box2.attachMoveCallback()

    box3.getBackground().setColor(0.0, 0.0, 1.0, 0.8)
    box3.attachMoveCallback()

    wm.addChild(box1)
    wm.addChild(box2)
    wm.addChild(box3)
    wm.addChild(box4)

    box4.hide()

    model = osgDB.readNodeFile("spaceship.osgt")

    model.setNodeMask(MASK_3D)

    return osgWidget.createExample(viewer, wm, model)


if __name__ == "__main__":
    main(sys.argv)
