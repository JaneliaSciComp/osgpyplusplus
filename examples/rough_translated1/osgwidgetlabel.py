#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetlabel"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgWidget


# Translated from file 'osgwidgetlabel.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetlabel.cpp 66 2008-07-14 21:54:09Z cubicool $

#include <osg/io_utils>
#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Box>
#include <osgWidget/Label>

MASK_2D = 0xF0000000

LABEL1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed\n"
    "do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n"
    "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in..."


LABEL2 = "...reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla\n"
    "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \n"
    "culpa qui officia deserunt mollit anim id est laborum. BBBBB"


def createLabel(l, size):

    
    label = osgWidget.Label("", "")

    label.setFont("fonts/Vera.ttf")
    label.setFontSize(size)
    label.setFontColor(1.0, 1.0, 1.0, 1.0)
    label.setLabel(l)

    #
#    text.setBackdropType(osgText.Text.DROP_SHADOW_BOTTOM_RIGHT)
#    text.setBackdropImplementation(osgText.Text.NO_DEPTH_BUFFER)
#    text.setBackdropOffset(0.2)
#    

    return label

def main(argc, argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        # osgWidget.WindowManager.WM_USE_RENDERBINS |
        osgWidget.WindowManager.WM_PICK_DEBUG
    )
    
    box = osgWidget.Box("HBOX", osgWidget.Box.HORIZONTAL)
    vbox = osgWidget.Box("vbox", osgWidget.Box.VERTICAL)
    label1 = createLabel(LABEL1)
    label2 = createLabel(LABEL2)

    # Setup the labels for horizontal box.
    label1.setPadding(10.0)
    label2.setPadding(10.0)

    label1.addSize(21.0, 22.0)
    label2.addSize(21.0, 22.0)

    label1.setColor(1.0, 0.5, 0.0, 0.0)
    label2.setColor(1.0, 0.5, 0.0, 0.5)

    label2.setImage("Images/Brick-Norman-Brown.TGA", True)

    box.addWidget(label1)
    box.addWidget(label2)
    box.attachMoveCallback()
    box.attachScaleCallback()
    box.attachRotateCallback()

    # Setup the labels for the vertical box.
    label3 = createLabel("Label 3", 80)
    label4 = createLabel("Label 4", 60)
    label5 = createLabel("ABCDEFGHIJK", 93)

    label3.setPadding(3.0)
    label4.setPadding(3.0)
    label5.setPadding(3.0)

    label3.setColor(0.0, 0.0, 0.5, 0.5)
    label4.setColor(0.0, 0.0, 0.5, 0.5)
    label5.setColor(0.0, 0.0, 0.5, 0.5)
    
    #label5.setAlignHorizontal(osgWidget.Widget.HA_LEFT)
    #label5.setAlignVertical(osgWidget.Widget.VA_BOTTOM)

    # Test our label copy construction...
    label6 = osg.clone(label5, "label6", osg.CopyOp.DEEP_COPY_ALL)

    label6.setLabel("abcdefghijklmnopqrs")

    vbox.addWidget(label3)
    vbox.addWidget(label4)
    vbox.addWidget(label5)
    vbox.addWidget(label6)
    vbox.attachMoveCallback()
    vbox.attachScaleCallback()

    vbox.resize()

    # vbox.setVisibilityMode(osgWidget.Window.VM_ENTIRE)
    # vbox.setVisibleArea(50, 50, 500, 200)
    # vbox.setAnchorVertical(osgWidget.Window.VA_TOP)
    # vbox.setAnchorHorizontal(osgWidget.Window.HA_RIGHT)

    # Test our label-in-window copy construction...
    clonedBox = osg.clone(box, "HBOX-", osg.CopyOp.DEEP_COPY_ALL)()
    
    clonedBox.getBackground().setColor(0.0, 1.0, 0.0, 0.5)

    wm.addChild(box)
    wm.addChild(vbox)
    wm.addChild(clonedBox)

    return osgWidget.createExample(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
