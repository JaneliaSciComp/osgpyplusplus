#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetinput"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgViewer
from osgpypp import osgWidget

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetinput.cpp 50 2008-05-06 05:06:36Z cubicool $

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgViewer/ViewerEventHandlers>
#include <osgWidget/WindowManager>
#include <osgWidget/Box>
#include <osgWidget/Input>
#include <osgWidget/ViewerEventHandlers>

 unsigned int MASK_2D = 0xF0000000

def main(argc, argv):
    viewer = osgViewer.Viewer()

    wm =  new osgWidget.WindowManager(
        viewer,
        1280.0f,
        1024.0f,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )
    
    box =  new osgWidget.Box("vbox", osgWidget.Box.VERTICAL)
    input =  new osgWidget.Input("input", "", 50)

    input.setFont("fonts/VeraMono.ttf")
    input.setFontColor(0.0f, 0.0f, 0.0f, 1.0f)
    input.setFontSize(15)
    input.setYOffset(input.calculateBestYOffset("y"))
    input.setSize(400.0f, input.getText().getCharacterHeight())

    box.addWidget(input)
    box.setOrigin(200.0f, 200.0f)

    wm.addChild(box)

    viewer.setUpViewInWindow(
        50,
        50,
        static_cast<int>(wm.getWidth()),
        static_cast<int>(wm.getHeight())
    )

    camera =  wm.createParentOrthoCamera()

    viewer.addEventHandler(new osgWidget.MouseHandler(wm))
    viewer.addEventHandler(new osgWidget.KeyboardHandler(wm))
    viewer.addEventHandler(new osgWidget.ResizeHandler(wm, camera))
    viewer.addEventHandler(new osgWidget.CameraSwitchHandler(wm, camera))
    viewer.addEventHandler(new osgViewer.WindowSizeHandler())

    wm.resizeAllWindows()

    viewer.setSceneData(camera)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
