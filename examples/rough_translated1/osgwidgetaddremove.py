#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetaddremove"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgWidget


# Translated from file 'osgwidgetaddremove.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetaddremove.cpp 45 2008-04-23 16:46:11Z cubicool $

#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Table>
#include <osgWidget/Box>
#include <osgWidget/Label>

MASK_2D = 0xF0000000

class ABCWidget (osgWidget.Label) :
    ABCWidget( str label):
    osgWidget.Label("", label) 
        setFont("fonts/Vera.ttf")
        setFontSize(20)
        setCanFill(True)
        setShadow(0.08)
        addSize(10.0, 10.0)


class Button (osgWidget.Label) :
    Button( str label):
    osgWidget.Label("", label) 
        setFont("fonts/Vera.ttf")
        setFontSize(30)
        setColor(0.8, 0.2, 0.2, 0.8)
        setCanFill(True)
        setShadow(0.1)
        setEventMask(osgWidget.EVENT_MASK_MOUSE_CLICK)
        addSize(20.0, 20.0)

    # NOTE! I need to make it clearer than Push/Release can happen so fast that
    # the changes you make aren't visible with your refresh rate. Throttling state
    # changes and what-have-you on mousePush/mouseRelease/etc. is going to be
    # annoying...

    virtual bool mousePush(double, double,  osgWidget.WindowManager*) 
        addColor(0.2, 0.2, 0.2, 0.0)
        
        return True

    virtual bool mouseRelease(double, double,  osgWidget.WindowManager*) 
        addColor(-0.2, -0.2, -0.2, 0.0)
        
        return True


class AddRemove (osgWidget.Box) :
_win1 = osgWidget.Window()
    AddRemove():
    osgWidget.Box ("buttons", osgWidget.Box.VERTICAL),
    _win1          (osgWidget.Box("win1", osgWidget.Box.VERTICAL)) 
        addWidget(Button("Add Widget"))
        addWidget(Button("Remove Widget"))

        # Take special note here! Not only do the Button objects have their
        # own overridden methods for changing the color, but they have attached
        # callbacks for doing the work with local data.
        getByName("Widget_1").addCallback(osgWidget.Callback(
            AddRemove.handlePressAdd,
            this,
            osgWidget.EVENT_MOUSE_PUSH
        ))

        getByName("Widget_2").addCallback(osgWidget.Callback(
            AddRemove.handlePressRemove,
            this,
            osgWidget.EVENT_MOUSE_PUSH
        ))

    def managed(wm):

        
        osgWidget.Box.managed(wm)

        _win1.setOrigin(250.0, 0.0)

        wm.addChild(_win1.get())

    def handlePressAdd(ev):

        
        static unsigned int num = 0

        ss = strstream()

        ss, "a random widget ", num

        _win1.addWidget(ABCWidget(ss.str()))

        num++

        return True

    def handlePressRemove(ev):

        
        # TODO: Temporary hack!
        v = _win1.getObjects()
    
        if !v.size() : return False

        w = _win1.getObjects()[v.size() - 1].get()

        _win1.removeWidget(w)

        return True


def main(argc, argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D
    )
    
    buttons = AddRemove()

    wm.addChild(buttons)

    createExample = return(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
