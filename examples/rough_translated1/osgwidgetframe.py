#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetframe"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgWidget


# Translated from file 'osgwidgetframe.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetframe.cpp 40 2008-04-11 14:05:11Z cubicool $

#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Frame>
#include <osgWidget/Box>
#include <osgDB/ReadFile>

MASK_2D = 0xF0000000

def main(argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )
    
    frame = osgWidget.Frame.createSimpleFrame(
        "frame",
        32.0,
        32.0,
        300.0,
        300.0
    )

    frame2 = osgWidget.Frame.createSimpleFrameFromTheme(
        "frameTheme",
        osgDB.readImageFile("osgWidget/theme-1.png"),
        300.0,
        300.0,
        osgWidget.Frame.FRAME_ALL
        )
    frame2.setPosition(300,100,0)
    frame2.getBackground().setColor(1.0, 1.0, 1.0, 0.0)

    frame22 = osgWidget.Frame.createSimpleFrameFromTheme(
        "frameTheme",
        osgDB.readImageFile("osgWidget/theme-2.png"),
        300.0,
        300.0,
        osgWidget.Frame.FRAME_ALL
        )
    frame22.setPosition(300,100,0)
    frame22.getBackground().setColor(1.0, 1.0, 1.0, 0.0)


    frame3 = osgWidget.Frame.createSimpleFrameFromTheme(
        "frameTheme",
        osgDB.readImageFile("osgWidget/theme-2.png"),
        300.0,
        300.0,
        osgWidget.Frame.FRAME_ALL
        )
    frame3.setPosition(300,100,0)
    frame3.getBackground().setColor(0.0, 0.0, 0.0, 1.0)
    
    table = osgWidget.Table("table", 2, 2)
    bottom = osgWidget.Box("panel", osgWidget.Box.HORIZONTAL)

    table.addWidget(osgWidget.Widget("red", 300.0, 300.0), 0, 0)
    table.addWidget(osgWidget.Widget("white", 300.0, 300.0), 0, 1)
    table.addWidget(osgWidget.Widget("yellow", 300.0, 300.0), 1, 0)
    table.addWidget(osgWidget.Widget("purple", 300.0, 300.0), 1, 1)
    table.getByRowCol(0, 0).setColor(1.0, 0.0, 0.0, 1.0)
    table.getByRowCol(0, 1).setColor(1.0, 1.0, 1.0, 1.0)
    table.getByRowCol(1, 0).setColor(1.0, 1.0, 0.0, 1.0)
    table.getByRowCol(1, 1).setColor(1.0, 0.0, 1.0, 1.0)
    table.getByRowCol(0, 0).setMinimumSize(100.0, 100.0)
    table.getByRowCol(0, 1).setMinimumSize(100.0, 100.0)
    table.getByRowCol(1, 0).setMinimumSize(100.0, 100.0)
    table.getByRowCol(1, 1).setMinimumSize(100.0, 100.0)

    frame.setWindow(table)

    # Give frame some nice textures.
    # TODO: This has to be done after setWindow() wtf?
    frame.getBackground().setColor(0.0, 0.0, 0.0, 0.0)

    l = frame.getBorder(osgWidget.Frame.BORDER_LEFT)
    r = frame.getBorder(osgWidget.Frame.BORDER_RIGHT)
    t = frame.getBorder(osgWidget.Frame.BORDER_TOP)
    b = frame.getBorder(osgWidget.Frame.BORDER_BOTTOM)

    l.setImage("osgWidget/border-left.tga", True)
    r.setImage("osgWidget/border-right.tga", True)
    t.setImage("osgWidget/border-top.tga", True)
    b.setImage("osgWidget/border-bottom.tga", True)

    l.setTexCoordWrapVertical()
    r.setTexCoordWrapVertical()
    t.setTexCoordWrapHorizontal()
    b.setTexCoordWrapHorizontal()

    # Create the bottom, XArt panel.
    left = osgWidget.Widget("left", 512.0, 256.0)
    center = osgWidget.Widget("center", 256.0, 256.0)
    right = osgWidget.Widget("right", 512.0, 256.0)

    left.setImage("osgWidget/panel-left.tga", True)
    center.setImage("osgWidget/panel-center.tga", True)
    right.setImage("osgWidget/panel-right.tga", True)

    center.setTexCoordWrapHorizontal()

    bottom.addWidget(left)
    bottom.addWidget(center)
    bottom.addWidget(right)
    bottom.getBackground().setColor(0.0, 0.0, 0.0, 0.0)
    bottom.setOrigin(0.0, 1024.0 - 256.0)

    # Add everything to the WindowManager.
    wm.addChild(frame)
    wm.addChild(frame2)
    wm.addChild(frame22)
    wm.addChild(frame3)
    wm.addChild(bottom)

    return osgWidget.createExample(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
