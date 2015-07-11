#!/bin/env python

# This is a C++ example from the OpenSceneGraph source code, converted to python

# /* OpenSceneGraph example, osgterrain.
# *
# *  Permission is hereby granted, free of charge, to any person obtaining a copy
# *  of this software and associated documentation files (the "Software"), to deal
# *  in the Software without restriction, including without limitation the rights
# *  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# *  copies of the Software, and to permit persons to whom the Software is
# *  furnished to do so, subject to the following conditions:
# *
# *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# *  THE SOFTWARE.
# */

from osgpypp import osg, osgDB, osgViewer
import sys


class CalibrateCostEstimator(osg.GraphicsOperation):
    def __init__(self, gce):
        osg.GraphicsOperation.__init__(self, osg.GraphicsOperation("CalibrateCostEstimator", False))
        self._gce = gce

    def __call__(self, context):
        renderInfo = osg.RenderInfo(context.getState(), 0)
        self._gce.calibrate(renderInfo)


def main(argv):
    arguments = osg.ArgumentParser(argv)
    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)
    node = osgDB.readNodeFiles(arguments)
    if node is None:
        sys.exit(0)
    gce = osg.GraphicsCostEstimator()
    viewer.setSceneData(node)
    viewer.realize()
    compileCost = gce.estimateCompileCost(node)
    drawCost = gce.estimateDrawCost(node)
    print "estimateCompileCost(", node.getName(), "), CPU=", compileCost.first, " GPU=", compileCost.second
    print "estimateDrawCost(", node.getName(), "), CPU=", drawCost.first, " GPU=", drawCost.second
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
