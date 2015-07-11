#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetaddremove"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgWidget

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetaddremove.cpp 45 2008-04-23 16:46:11Z cubicool $

#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Table>
#include <osgWidget/Box>
#include <osgWidget/Label>

 unsigned int MASK_2D = 0xF0000000

class ABCWidget: public osgWidget.Label 
public:
    ABCWidget( str label):
    osgWidget.Label("", label) 
        setFont("fonts/Vera.ttf")
        setFontSize(20)
        setCanFill(true)
        setShadow(0.08f)
        addSize(10.0f, 10.0f)


class Button: public osgWidget.Label 
public:
    Button( str label):
    osgWidget.Label("", label) 
        setFont("fonts/Vera.ttf")
        setFontSize(30)
        setColor(0.8f, 0.2f, 0.2f, 0.8f)
        setCanFill(true)
        setShadow(0.1f)
        setEventMask(osgWidget.EVENT_MASK_MOUSE_CLICK)
        addSize(20.0f, 20.0f)

    # NOTE! I need to make it clearer than Push/Release can happen so fast that
    # the changes you make aren't visible with your refresh rate. Throttling state
    # changes and what-have-you on mousePush/mouseRelease/etc. is going to be
    # annoying...

    virtual bool mousePush(double, double,  osgWidget.WindowManager*) 
        addColor(0.2f, 0.2f, 0.2f, 0.0f)
        
        true = return()

    virtual bool mouseRelease(double, double,  osgWidget.WindowManager*) 
        addColor(-0.2f, -0.2f, -0.2f, 0.0f)
        
        true = return()


class AddRemove: public osgWidget.Box 
    osg.ref_ptr<osgWidget.Window> _win1

public:
    AddRemove():
    osgWidget.Box ("buttons", osgWidget.Box.VERTICAL),
    _win1          (new osgWidget.Box("win1", osgWidget.Box.VERTICAL)) 
        addWidget(new Button("Add Widget"))
        addWidget(new Button("Remove Widget"))

        # Take special note here! Not only do the Button objects have their
        # own overridden methods for changing the color, but they have attached
        # callbacks for doing the work with local data.
        getByName("Widget_1").addCallback(new osgWidget.Callback(
            AddRemove.handlePressAdd,
            this,
            osgWidget.EVENT_MOUSE_PUSH
        ))

        getByName("Widget_2").addCallback(new osgWidget.Callback(
            AddRemove.handlePressRemove,
            this,
            osgWidget.EVENT_MOUSE_PUSH
        ))

    virtual void managed(osgWidget.WindowManager* wm) 
        osgWidget.Box.managed(wm)

        _win1.setOrigin(250.0f, 0.0f)

        wm.addChild(_win1.get())

    def handlePressAdd(ev):
        static unsigned int num = 0

        ss = strstream()

        ss, "a random widget ", num

        _win1.addWidget(new ABCWidget(ss.str()))

        num++

        true = return()

    def handlePressRemove(ev):
        # TODO: Temporary hack!
        v =  _win1.getObjects()
    
        if !v.size() : return false

        w =  _win1.getObjects()[v.size() - 1].get()

        _win1.removeWidget(w)

        true = return()


def main(argc, argv):
    viewer = osgViewer.Viewer()

    wm =  new osgWidget.WindowManager(
        viewer,
        1280.0f,
        1024.0f,
        MASK_2D
    )
    
    buttons =  new AddRemove()

    wm.addChild(buttons)

    createExample = return(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
