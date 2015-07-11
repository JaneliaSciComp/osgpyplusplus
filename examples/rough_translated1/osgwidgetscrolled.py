#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetscrolled"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgWidget


# Translated from file 'osgwidgetscrolled.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetframe.cpp 34 2008-04-07 03:12:41Z cubicool $

#include <osgDB/ReadFile>

#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Frame>
#include <osgWidget/Box>

MASK_2D = 0xF0000000

# NOTE: THIS IS JUST A TEMPORARY HACK! :) This functionality will all eventually be
# encapsulate into another class in osgWidget proper.
def scrollWindow(ev):
    
    # The first thing we need to do is make sure we have a Frame object...
    frame = dynamic_cast<osgWidget.Frame*>(ev.getWindow())

    if !frame : return False

    # And now we need to make sure our Frame has a valid internal EmbeddedWindow widget.
    ew = dynamic_cast<osgWidget.Window.EmbeddedWindow*>(frame.getEmbeddedWindow())
    
        
    if !ew : return False
    
    # Lets get the visible area so that we can use it to make sure our scrolling action
    # is necessary in the first place.
    va = ew.getWindow().getVisibleArea()

    # The user wants to scroll up make sure that the visible area's Y origin isn't already
    # at 0.0, 0.0.
    if ev.getWindowManager().isMouseScrollingUp()  va[1] != 0.0 :
        ew.getWindow().addVisibleArea(0, -20)
    
    
    elif va[1] <= (ew.getWindow().getHeight() - ew.getHeight()) :
        ew.getWindow().addVisibleArea(0, 20)
    

    # We need to manually call update to make sure the visible area scissoring is done
    # properly.
    frame.update()

    return True

def changeTheme(ev):

    
    theme = str()

    if ev.key == osgGA.GUIEventAdapter.KEY_Right :
        theme = "osgWidget/theme-1.png"
    

    elif ev.key == osgGA.GUIEventAdapter.KEY_Left :
        theme = "osgWidget/theme-2.png"
    

    else : return False

    frame = dynamic_cast<osgWidget.Frame*>(ev.getWindow())

    if !frame : return False

    # This is just one way to access all our Widgets we could just as well have used:
    #
    # for(osgWidget.Frame.Iterator i = frame.begin() i != frame.end() i++) 
    #
    # ...and it have worked, too.
    for(unsigned int row = 0 row < 3 row++) 
        for(unsigned int col = 0 col < 3 col++) 
            frame.getByRowCol(row, col).setImage(theme)

    return True

def main(argc, argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
        #osgWidget.WindowManager.WM_NO_INVERT_Y
    )
    
    frame = osgWidget.Frame.createSimpleFrameFromTheme(
        "frame",
        osgDB.readImageFile("osgWidget/theme.png"),
        40.0,
        40.0,
	osgWidget.Frame.FRAME_ALL
    )

    frame.getBackground().setColor(0.0, 0.0, 0.0, 0.0)

    # This is our Transformers box. :)
    box = osgWidget.Box("images", osgWidget.Box.VERTICAL)
    img1 = osgWidget.Widget("im1", 512.0, 512.0)
    img2 = osgWidget.Widget("im2", 512.0, 512.0)
    img3 = osgWidget.Widget("im3", 512.0, 512.0)
    img4 = osgWidget.Widget("im4", 512.0, 512.0)

    img1.setImage("osgWidget/scrolled1.jpg", True)
    img2.setImage("osgWidget/scrolled2.jpg", True)
    img3.setImage("osgWidget/scrolled3.jpg", True)
    img4.setImage("osgWidget/scrolled4.jpg", True)

    img1.setMinimumSize(10.0, 10.0)
    img2.setMinimumSize(10.0, 10.0)
    img3.setMinimumSize(10.0, 10.0)
    img4.setMinimumSize(10.0, 10.0)

    box.addWidget(img1)
    box.addWidget(img2)
    box.addWidget(img3)
    box.addWidget(img4)
    box.setEventMask(osgWidget.EVENT_NONE)

    #frame.getEmbeddedWindow().setWindow(box)
    frame.setWindow(box)
    frame.getEmbeddedWindow().setColor(1.0, 1.0, 1.0, 1.0)
    frame.resize(300.0, 300.0)
    frame.addCallback(osgWidget.Callback(scrollWindow, osgWidget.EVENT_MOUSE_SCROLL))
    frame.addCallback(osgWidget.Callback(changeTheme, osgWidget.EVENT_KEY_DOWN))

    wm.addChild(frame)

    return osgWidget.createExample(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
