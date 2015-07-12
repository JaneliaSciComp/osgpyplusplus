#!/bin/env python

# OpenSceneGraph example program "osgpdf"
# Translated from file 'osgpdf.cpp'

import sys

from osgpypp import osg
from osgpypp import osgViewer
from osgpypp import osgWidget

def main(argv):
    arguments = osg.ArgumentParser(argv)
    viewer = osgViewer.Viewer(arguments)
    hints = osgWidget.GeometryHints(osg.Vec3(0.0,0.0,0.0),
                                   osg.Vec3(1.0,0.0,0.0),
                                   osg.Vec3(0.0,0.0,1.0),
                                   osg.Vec4(1.0,1.0,1.0,1.0),
                                   osgWidget.GeometryHints.RESIZE_HEIGHT_TO_MAINTAINCE_ASPECT_RATIO)
    group = osg.Group()
    for i in range(len(argv)):
        if not arguments.isOption(i) :
            pdfReader = osgWidget.PdfReader()
            if pdfReader.open(arguments[i], hints) :
                group.addChild(pdfReader.get())
                hints.position.x += 1.1
    viewer.setSceneData(group)
    viewer.addEventHandler(osgViewer.StatsHandler())
    return viewer.run()

if __name__ == "__main__":
    main(sys.argv)
