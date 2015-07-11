#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetstyled"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgWidget

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetshader.cpp 28 2008-03-26 15:26:48Z cubicool $

#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/StyleManager>
#include <osgWidget/Box>

 unsigned int MASK_2D = 0xF0000000

STYLE1 = 
    "color 0 0 0 128\n"
    "padding 5\n"


STYLE2 = 
    "color 1.0 0.5 0.0\n"


STYLE3 = 
    "fill true\n"


STYLE4 = 
    "pos 100.0 100.0\n"
    "size 600 600\n"


class CustomStyled: public osgWidget.Widget 


class CustomStyle: public osgWidget.Style 
    virtual bool applyStyle(osgWidget.Widget* w, osgWidget.Reader r) 
        cs =  dynamic_cast<CustomStyled*>(w)

        if !cs : return false

        osgWidget.warn(), "Here, okay."

        true = return()


def main(argc, argv):
    viewer = osgViewer.Viewer()

    wm =  new osgWidget.WindowManager(
        viewer,
        1280.0f,
        1024.0f,
        MASK_2D
    )

    box =  new osgWidget.Box("box", osgWidget.Box.VERTICAL)

    widget1 =  new osgWidget.Widget("w1", 200.0f, 200.0f)
    widget2 =  new osgWidget.Widget("w2", 100.0f, 100.0f)
    widget3 =  new osgWidget.Widget("w3", 0.0f, 0.0f)
    # CustomStyled*      cs      = new CustomStyled()

    # Yep.
    wm.getStyleManager().addStyle(new osgWidget.Style("widget.style1", STYLE1))
    wm.getStyleManager().addStyle(new osgWidget.Style("widget.style2", STYLE2))
    wm.getStyleManager().addStyle(new osgWidget.Style("spacer", STYLE3))
    wm.getStyleManager().addStyle(new osgWidget.Style("window", STYLE4))
    # wm.getStyleManager().addStyle(new CustomStyle("widget", ""))

    widget1.setStyle("widget.style1")
    widget2.setStyle("widget.style2")
    widget3.setStyle("spacer")

    box.setStyle("window")

    box.addWidget(widget1)
    box.addWidget(widget2)
    box.addWidget(widget3)

    wm.addChild(box)

    # box.resizePercent(0.0f, 100.0f)

    return osgWidget.createExample(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
