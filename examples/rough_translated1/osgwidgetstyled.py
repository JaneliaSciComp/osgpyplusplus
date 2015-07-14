#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetstyled"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgWidget


# Translated from file 'osgwidgetstyled.cpp'

# -*-c++-*- osgWidget - Code by: Jeremy Moles (cubicool) 2007-2008
# $Id: osgwidgetshader.cpp 28 2008-03-26 15:26:48Z cubicool $

#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/StyleManager>
#include <osgWidget/Box>

MASK_2D = 0xF0000000

STYLE1 = "color 0 0 0 128\n"
    "padding 5\n"


STYLE2 = "color 1.0 0.5 0.0\n"


STYLE3 = "fill True\n"


STYLE4 = "pos 100.0 100.0\n"
    "size 600 600\n"


class CustomStyled (osgWidget.Widget) :


class CustomStyle (osgWidget.Style) :
def applyStyle(w, r):
    
        cs = dynamic_cast<CustomStyled*>(w)

        if  not cs : return False

        osgWidget.warn(), "Here, okay."

        return True


def main(argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D
    )

    box = osgWidget.Box("box", osgWidget.Box.VERTICAL)

    widget1 = osgWidget.Widget("w1", 200.0, 200.0)
    widget2 = osgWidget.Widget("w2", 100.0, 100.0)
    widget3 = osgWidget.Widget("w3", 0.0, 0.0)
    # CustomStyled*      cs      = CustomStyled()

    # Yep.
    wm.getStyleManager().addStyle(osgWidget.Style("widget.style1", STYLE1))
    wm.getStyleManager().addStyle(osgWidget.Style("widget.style2", STYLE2))
    wm.getStyleManager().addStyle(osgWidget.Style("spacer", STYLE3))
    wm.getStyleManager().addStyle(osgWidget.Style("window", STYLE4))
    # wm.getStyleManager().addStyle(CustomStyle("widget", ""))

    widget1.setStyle("widget.style1")
    widget2.setStyle("widget.style2")
    widget3.setStyle("spacer")

    box.setStyle("window")

    box.addWidget(widget1)
    box.addWidget(widget2)
    box.addWidget(widget3)

    wm.addChild(box)

    # box.resizePercent(0.0, 100.0)

    return osgWidget.createExample(viewer, wm)


if __name__ == "__main__":
    main(sys.argv)
