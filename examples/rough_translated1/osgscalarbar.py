#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgscalarbar"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgSim
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgscalarbar.cpp'

# OpenSceneGraph example, osgscalarbar.
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

#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Material>
#include <osg/Texture2D>
#include <osg/MatrixTransform>
#include <osg/PositionAttitudeTransform>
#include <osg/BlendFunc>
#include <osg/ClearNode>
#include <osg/Projection>

#include <osgUtil/CullVisitor>

#include <osgGA/TrackballManipulator>
#include <osgViewer/Viewer>
#include <osgDB/ReadFile>

#include <osgSim/ScalarsToColors>
#include <osgSim/ColorRange>
#include <osgSim/ScalarBar>

#include <sstream>
#include <iostream>
#include <math.h>

using namespace osgSim
using osgSim.ScalarBar

#if defined(_MSC_VER)
# not have to have this pathway for just VS6.0 as its unable to handle the full
# ScalarBar.ScalarPrinter.printScalar scoping.

# Create a custom scalar printer
class MyScalarPrinter (ScalarBar.ScalarPrinter) :
def printScalar(scalar):
    
        print "In MyScalarPrinter.printScalar"
        if scalar==0.0 : return ScalarPrinter.printScalar(scalar)+" Bottom"
        elif scalar==0.5 : return ScalarPrinter.printScalar(scalar)+" Middle"
        elif scalar==1.0 : return ScalarPrinter.printScalar(scalar)+" Top"
        else : return ScalarPrinter.printScalar(scalar)

#else :
# Create a custom scalar printer
class MyScalarPrinter (ScalarBar.ScalarPrinter) :
def printScalar(scalar):
    
        print "In MyScalarPrinter.printScalar"
        if scalar==0.0 : return ScalarBar.ScalarPrinter.printScalar(scalar)+" Bottom"
        elif scalar==0.5 : return ScalarBar.ScalarPrinter.printScalar(scalar)+" Middle"
        elif scalar==1.0 : return ScalarBar.ScalarPrinter.printScalar(scalar)+" Top"
        else : return ScalarBar.ScalarPrinter.printScalar(scalar)

#endif

def createScalarBar():

    
#if 1
    #ScalarsToColors* stc = ScalarsToColors(0.0,1.0)
    #ScalarBar* sb = ScalarBar(2,3,stc,"STC_ScalarBar")

    # Create a custom color set
    cs = std.vector<osg.Vec4>()
    cs.push_back(osg.Vec4(1.0,0.0,0.0,1.0))   # R
    cs.push_back(osg.Vec4(0.0,1.0,0.0,1.0))   # G
    cs.push_back(osg.Vec4(1.0,1.0,0.0,1.0))   # G
    cs.push_back(osg.Vec4(0.0,0.0,1.0,1.0))   # B
    cs.push_back(osg.Vec4(0.0,1.0,1.0,1.0))   # R


    cr = ColorRange(0.0,1.0,cs)
    sb = ScalarBar(20, 11, cr, "ScalarBar", ScalarBar.VERTICAL, 0.1, MyScalarPrinter)()
    sb.setScalarPrinter(MyScalarPrinter)()

    return sb
#else :
    sb = ScalarBar()
    tp = ScalarBar.TextProperties()
    tp._fontFile = "fonts/times.ttf"

    sb.setTextProperties(tp)

    return sb
#endif


def createScalarBar_HUD():

    
    geode = osgSim.ScalarBar()
    tp = osgSim.ScalarBar.TextProperties()
    tp._fontFile = "fonts/times.ttf"
    geode.setTextProperties(tp)
    stateset = geode.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING, osg.StateAttribute.OFF)

    stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
    stateset.setRenderBinDetails(11, "RenderBin")

    modelview = osg.MatrixTransform()
    modelview.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    matrix = osg.Matrixd(osg.Matrixd.scale(1000,1000,1000) * osg.Matrixd.translate(120,10,0)) # I've played with these values a lot and it seems to work, but I have no idea why
    modelview.setMatrix(matrix)
    modelview.addChild(geode)

    projection = osg.Projection()
    projection.setMatrix(osg.Matrix.ortho2D(0,1280,0,1024)) # or whatever the OSG window res is
    projection.addChild(modelview)

    return projection #make sure you delete the return sb line

int main(int , char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    group = osg.Group()
    group.addChild(createScalarBar())
    group.addChild(createScalarBar_HUD())

    # add model to viewer.
    viewer.setSceneData( group )

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
