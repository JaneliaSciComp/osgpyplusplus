#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetperformance"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgWidget

#include <iostream>
#include <osg/ArgumentParser>
#include <osgDB/ReadFile>
#include <osgWidget/Canvas>
#include <osgWidget/WindowManager>
#include <osgWidget/Util>

def setupArguments(args):
    args.getApplicationUsage().setDescription(
        args.getApplicationName() + " is a performance testing application for osgWidget."
    )

    args.getApplicationUsage().setCommandLineUsage(
        args.getApplicationName() + " [options] widgets"
    )

    args.getApplicationUsage().addCommandLineOption(
        "--width <int>",
        "The WindowManager width."
    )

    args.getApplicationUsage().addCommandLineOption(
        "--height <int>",
        "The WindowManager height."
    )

    args.getApplicationUsage().addCommandLineOption(
        "--size <int>",
        "The size of the square Widgets."
    )

    args.getApplicationUsage().addCommandLineOption(
        "--single-window",
        "All widgets are put inside a single Window."
    )

    args.getApplicationUsage().addCommandLineOption(
        "--multi-window",
        "All widgets are in their own Windows."
    )

void readSize(osg.ArgumentParser args,  char* opt, unsigned int val) 
    size = str()

    while args.read(opt, size) : 
        s =  std.atoi(size.c_str())

        if s > 0 : val = s

def doError(errorMsg):
    osgWidget.warn(), errorMsg

    return 1

int doApp(osgViewer.Viewer viewer, osg.Node* node, unsigned int width, unsigned int height) 
    wm =  new osgWidget.WindowManager(viewer, width, height, 0x12)

    wm.addChild(node)

    return osgWidget.createExample(viewer, wm)

def main(argc, argv):
    args = osg.ArgumentParser(argc, argv)

    setupArguments(args)

    viewer = osgViewer.Viewer(args)

    while args.read("--help") : 
        args.getApplicationUsage().write(
            std.cout,
            osg.ApplicationUsage.COMMAND_LINE_OPTION
        )

        return 0

    size = str()

    unsigned int width        = 1280
    unsigned int height       = 1024
    unsigned int wSize        = 10
    singleWindow =  false
    multiWindow =  false

    readSize(args, "--width", width)
    readSize(args, "--height", height)
    readSize(args, "--size", wSize)

    while args.read("--single-window") : singleWindow = true
    
    while args.read("--multi-window") : multiWindow = true

    unsigned int numWidgets = 0

    if args.argc() >= 2 : numWidgets = std.atoi(args[1])

    else: return doError("Please specify the number of Widgets to use.")

    if numWidgets <= 0 : return doError("Please specify one or more Widgets to use.")

    if !singleWindow  !multiWindow : return doError(
        "Please specify one of --single-window or --multi-window."
    )

    if singleWindow : 
        canvas =  new osgWidget.Canvas("canvas")

        canvas.getBackground().setColor(0.0f, 0.0f, 0.0f, 0.0f)

        unsigned int rows = height / (wSize + 2)
        unsigned int cols = (numWidgets / rows) + 1
        unsigned int w    = 0

        #
        image =  osgDB.readImageFile("osgWidget/natascha.png")
        texture =  new osg.Texture2D()

        texture.setImage(0, image)
        

        for(unsigned int c = 0 c < cols c++) 
            for(unsigned int r = 0 r < rows r++) 
                if w >= numWidgets : break

                widget =  new osgWidget.Widget(
                    "",
                    wSize,
                    wSize
                )

                col =  static_cast<float>(w) / static_cast<float>(numWidgets)

                widget.setColor(col, col, col, 0.9f)
                # widget.setTexture(texture, true)

                canvas.addWidget(widget, c * (wSize + 2), r * (wSize + 2))

                w++

        doApp = return(viewer, canvas, width, height)

    doError = else:("Not supported yet.")

    return 1


if __name__ == "__main__":
    main(sys.argv)
