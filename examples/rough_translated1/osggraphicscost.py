#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osggraphicscost"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgViewer


# Translated from file 'osggraphicscost.cpp'

# OpenSceneGraph example, osgterrain.
#*
#*  Permission is hereby granted, free of charge, to any person obtaining a copy
#*  of this software and associated documentation files (the "Software"), to deal
#*  in the Software without restriction, including without limitation the rights
#*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#*  copies of the Software, and to permit persons to whom the Software is
#*  furnished to do so, subject to the following conditions:
#*
#*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#*  THE SOFTWARE.
#


#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgDB/ReadFile>

#include <osg/GraphicsCostEstimator>

class CalibrateCostEsimator (osg.GraphicsOperation) :

    CalibrateCostEsimator(osg.GraphicsCostEstimator* gce):
        osg.GraphicsOperation("CalbirateCostEstimator",False),
        _gce(gce) 

    virtual void operator () (osg.GraphicsContext* context)
        renderInfo = osg.RenderInfo(context.getState(), 0)
        _gce.calibrate(renderInfo)

    _gce = osg.GraphicsCostEstimator()




def main(argv):


    
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)


    node = osgDB.readNodeFiles(arguments)
    if  not node : return 0

    gce = osg.GraphicsCostEstimator()

    viewer.setSceneData(node)

    viewer.realize()

    compileCost = gce.estimateCompileCost(node)
    drawCost = gce.estimateDrawCost(node)

    OSG_NOTICE, "estimateCompileCost(", node.getName(), "), CPU=", compileCost.first, " GPU=", compileCost.second
    OSG_NOTICE, "estimateDrawCost(", node.getName(), "), CPU=", drawCost.first, " GPU=", drawCost.second

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
