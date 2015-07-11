#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetnotebook"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgGA
from osgpypp import osgViewer
from osgpypp import osgWidget


# Translated from file 'osgwidgetnotebook.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetnotebook.cpp 45 2008-04-23 16:46:11Z cubicool $

#include <osg/io_utils>
#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgViewer/ViewerEventHandlers>
#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Box>
#include <osgWidget/Canvas>
#include <osgWidget/Label>
#include <osgWidget/Label>
#include <osgWidget/ViewerEventHandlers>

MASK_2D = 0xF0000000
MASK_3D = 0x0F000000

class Notebook (osgWidget.Box) :
_tabs = osgWidget.Box()
    _windows = osgWidget.Canvas()
    # NOTE: This whole thing is just a hack to demonstrate a concept. The real
    # implementation would need to be much cleaner.
    def callbackTabPressed(ev):
        
        objs = _windows.getObjects()

        for(unsigned int i = 0 i < objs.size() i++) objs[i].setLayer(
            osgWidget.Widget.LAYER_MIDDLE,
            i * 2
        )

        _windows.getByName(ev.getWidget().getName()).setLayer(
            osgWidget.Widget.LAYER_MIDDLE,
            objs.size() * 2
        )

        _windows.resize()

        return True

    Notebook( str name):
    osgWidget.Box(name, osgWidget.Box.VERTICAL) 
        _tabs    = osgWidget.Box("tabs", osgWidget.Box.HORIZONTAL)
        _windows = osgWidget.Canvas("canvas")

        for(unsigned int i = 0 i < 4 i++) 
            ss = strstream()

            # Setup everything for our Tab...
            ss, "Tab_", i

            label1 = osgWidget.Label(ss.str())

            label1.setFont("fonts/VeraMono.ttf")
            label1.setFontSize(20)
            label1.setFontColor(1.0, 1.0, 1.0, 1.0)
            label1.setColor(0.0, i / 4.0, 0.3, 1.0)
            label1.setLabel(ss.str())
            label1.addSize(20.0, 20.0)
            label1.setShadow(0.1)
            label1.setCanFill(True)

            _tabs.addWidget(label1)

            # Setup everything for the Window corresponding to the Tab
            # in the Canvas down below.
            descr = strstream()

            descr, "This is some text", "for the Tab_", i, " tab.", "Press the button up top", "And this should go to the next Window!"
            

            label2 = osgWidget.Label(ss.str())

            label2.setFont("fonts/Vera.ttf")
            label2.setFontSize(15)
            label2.setFontColor(1.0, 1.0, 1.0, 1.0)
            label2.setColor(0.0, i / 4.0, 0.3, 1.0)
            label2.setLabel(descr.str())
            label2.setLayer(osgWidget.Widget.LAYER_MIDDLE, i * 2)
            label2.addSize(50.0, 50.0)

            _windows.addWidget(label2, 0.0, 0.0)

            label1.setEventMask(osgWidget.EVENT_MOUSE_PUSH)
            label1.addCallback(osgWidget.Callback(
                Notebook.callbackTabPressed,
                this,
                osgWidget.EVENT_MOUSE_PUSH
            ))

        label = osgWidget.Label("label")

        label.setFont("fonts/arial.ttf")
        label.setFontSize(15)
        label.setFontColor(1.0, 1.0, 1.0, 1.0)
        label.setLabel("Drag the window here...")
        label.addSize(20.0, 20.0)
        label.setShadow(0.08)
        label.setCanFill(True)
   
        addWidget(label)
        addWidget(_tabs.embed())
        addWidget(_windows.embed())


def bound(node):

    
    bs = node.getBound()

    osgWidget.warn(), "center: ", bs.center(), " radius: ", bs.radius()

def main(argc, argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        720.0,
        MASK_2D #,
        #osgWidget.WindowManager.WM_USE_RENDERBINS
    )

    notebook1 = Notebook("notebook1")
    notebook2 = Notebook("notebook2")

    notebook2.setOrigin(100.0, 100.0)

    notebook1.attachMoveCallback()
    notebook2.attachMoveCallback()

    wm.addChild(notebook1)
    wm.addChild(notebook2)

    return osgWidget.createExample(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
