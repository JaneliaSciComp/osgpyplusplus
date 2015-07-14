#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetmenu"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgWidget


# Translated from file 'osgwidgetmenu.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetmenu.cpp 66 2008-07-14 21:54:09Z cubicool $

#include <iostream>
#include <osgDB/ReadFile>
#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Box>
#include <osgWidget/Label>

# For now this is just an example, but osgWidget.Menu will later be it's own Window.
# I just wanted to get this out there so that people could see it was possible.

MASK_2D = 0xF0000000
MASK_3D = 0x0F000000

class ColorLabel (osgWidget.Label) :
ColorLabel( char* label):
    osgWidget.Label("", "") 
        setFont("fonts/Vera.ttf")
        setFontSize(14)
        setFontColor(1.0, 1.0, 1.0, 1.0)
        setColor(0.3, 0.3, 0.3, 1.0)
        addHeight(18.0)
        setCanFill(True)
        setLabel(label)
        setEventMask(osgWidget.EVENT_MOUSE_PUSH | osgWidget.EVENT_MASK_MOUSE_MOVE)

    bool mousePush(double, double,  osgWidget.WindowManager*) 
        return True

    bool mouseEnter(double, double,  osgWidget.WindowManager*) 
        setColor(0.6, 0.6, 0.6, 1.0)
        
        return True

    bool mouseLeave(double, double,  osgWidget.WindowManager*) 
        setColor(0.3, 0.3, 0.3, 1.0)
        
        return True


class ColorLabelMenu (ColorLabel) :
_window = osgWidget.Window()
    ColorLabelMenu( char* label):
    ColorLabel(label) 
        _window = osgWidget.Box(
            str("Menu_") + label,
            osgWidget.Box.VERTICAL,
            True
        )

        _window.addWidget(ColorLabel("Open Some Stuff"))
        _window.addWidget(ColorLabel("Do It Now"))
        _window.addWidget(ColorLabel("Hello, How Are U?"))
        _window.addWidget(ColorLabel("Hmmm..."))
        _window.addWidget(ColorLabel("Option 5"))

        _window.resize()

        setColor(0.8, 0.8, 0.8, 0.8)

    def managed(wm):

        
        osgWidget.Label.managed(wm)

        wm.addChild(_window)

        _window.hide()

    def positioned():

        
        osgWidget.Label.positioned()

        _window.setOrigin(getX(), getHeight())
        _window.resize(getWidth())

    bool mousePush(double, double,  osgWidget.WindowManager*) 
        if  not _window.isVisible() : _window.show()

        else _window.hide()

        return True

    bool mouseLeave(double, double,  osgWidget.WindowManager*) 
        if  not _window.isVisible() : setColor(0.8, 0.8, 0.8, 0.8)

        return True


def main(argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )

    menu = osgWidget.Box("menu", osgWidget.Box.HORIZONTAL)

    menu.addWidget(ColorLabelMenu("Pick me not "))
    menu.addWidget(ColorLabelMenu("No, wait, pick me not "))
    menu.addWidget(ColorLabelMenu("Don't pick them..."))
    menu.addWidget(ColorLabelMenu("Grarar not ? not "))

    wm.addChild(menu)
    
    menu.getBackground().setColor(1.0, 1.0, 1.0, 0.0)
    menu.resizePercent(100.0)

    model = osgDB.readNodeFile("osgcool.osgt")

    model.setNodeMask(MASK_3D)

    return osgWidget.createExample(viewer, wm, model)


if __name__ == "__main__":
    main(sys.argv)
