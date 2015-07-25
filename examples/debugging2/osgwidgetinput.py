#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetinput_"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgViewer
from osgpypp import osgWidget

# Translated from file 'osgwidgetinput_.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetinput_.cpp 50 2008-05-06 05:06:36Z cubicool $


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
    box = osgWidget.Box("vbox", osgWidget.Box.VERTICAL)
    input_ = osgWidget.Input("input", "", 50)
    input_.setFont("fonts/VeraMono.ttf")
    input_.setFontColor(0.0, 0.0, 0.0, 1.0)
    input_.setFontSize(15)
    input_.setYOffset(input_.calculateBestYOffset("y"))
    input_.setSize(400.0, input_.getText().getCharacterHeight())
    box.addWidget(input_)
    box.setOrigin(200.0, 200.0)
    wm.addChild(box)
    viewer.setUpViewInWindow(
        50,
        50,
        int(wm.getWidth()),
        int(wm.getHeight())
    )
    camera = wm.createParentOrthoCamera()
    viewer.addEventHandler(osgWidget.MouseHandler(wm))
    viewer.addEventHandler(osgWidget.KeyboardHandler(wm))
    viewer.addEventHandler(osgWidget.ResizeHandler(wm, camera))
    viewer.addEventHandler(osgWidget.CameraSwitchHandler(wm, camera))
    viewer.addEventHandler(osgViewer.WindowSizeHandler())
    wm.resizeAllWindows()
    viewer.setSceneData(camera)
    return viewer.run()

if __name__ == "__main__":
    main(sys.argv)
