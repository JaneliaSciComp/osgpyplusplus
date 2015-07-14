#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgpdf"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgViewer
from osgpypp import osgWidget


# Translated from file 'osgpdf.cpp'

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgWidget/PdfReader>

def main(argv):

    
    arguments = osg.ArgumentParser(argv)
    viewer = osgViewer.Viewer(arguments)

    hints = osgWidget.GeometryHints(osg.Vec3(0.0,0.0,0.0),
                                   osg.Vec3(1.0,0.0,0.0),
                                   osg.Vec3(0.0,0.0,1.0),
                                   osg.Vec4(1.0,1.0,1.0,1.0),
                                   osgWidget.GeometryHints.RESIZE_HEIGHT_TO_MAINTAINCE_ASPECT_RATIO)

    group = osg.Group()

    for(int i=1 i<arguments.argc() ++i)
        if  not arguments.isOption(i) :
            pdfReader = osgWidget.PdfReader()
            if pdfReader.open(arguments[i], hints) :
                group.addChild(pdfReader)
                
                hints.position.x() += 1.1

    viewer.setSceneData(group)

    viewer.addEventHandler(osgViewer.StatsHandler)()

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
