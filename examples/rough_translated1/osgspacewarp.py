#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgspacewarp"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgspacewarp.cpp'

# OpenSceneGraph example, osgspacewarp.
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

#include <osg/Group>
#include <osg/Geometry>

#include <osgDB/ReadFile>
#include <osgUtil/Optimizer>
#include <osgViewer/Viewer>

def random(min, max):

     return min + (max-min)*(float)rand()/(float)RAND_MAX 


class DrawCallback (osg.Drawable.DrawCallback) :
DrawCallback():
        _firstTime(True) 

    def drawImplementation(renderInfo, drawable):

        
        state = *renderInfo.getState()

        if  not _firstTime :
            _previousModelViewMatrix = _currentModelViewMatrix
            _currentModelViewMatrix = state.getModelViewMatrix()
            _inverseModelViewMatrix.invert(_currentModelViewMatrix)

            T = osg.Matrix(_previousModelViewMatrix*_inverseModelViewMatrix)

            geometry = dynamic_cast<osg.Geometry*>(const_cast<osg.Drawable*>(drawable))
            vertices = dynamic_cast<osg.Vec3Array*>(geometry.getVertexArray())
            for(unsigned int i=0i+1<vertices.size()i+=2)
                (*vertices)[i+1] = (*vertices)[i]*T
        else:
            _currentModelViewMatrix = state.getModelViewMatrix()

        _firstTime = False

        drawable.drawImplementation(renderInfo)

    mutable bool _firstTime
    mutable osg.Matrix _currentModelViewMatrix
    mutable osg.Matrix _inverseModelViewMatrix
    mutable osg.Matrix _previousModelViewMatrix





def createScene(noStars):




    

    geometry = osg.Geometry()

    # set up vertices
    vertices = osg.Vec3Array(noStars*2)
    geometry.setVertexArray(vertices)

    min = -1.0
    max = 1.0
    j = 0
    i = 0
    for(i=0i<noStars++i,j+=2)
        (*vertices)[j].set(random(min,max),random(min,max),random(min,max))
        (*vertices)[j+1] = (*vertices)[j]+osg.Vec3(0.0,0.0,0.001)

    # set up colours
    colours = osg.Vec4Array(1)
    geometry.setColorArray(colours, osg.Array.BIND_OVERALL)
    (*colours)[0].set(1.0,1.0,1.0,1.0)

    # set up the primitive set to draw lines
    geometry.addPrimitiveSet(osg.DrawArrays(GL_LINES,0,noStars*2))

    # set up the points for the stars.
    points = osg.DrawElementsUShort(GL_POINTS,noStars)
    geometry.addPrimitiveSet(points)
    for(i=0i<noStars++i)
        (*points)[i] = i*2

    geometry.setUseDisplayList(False)
    geometry.setDrawCallback(DrawCallback)()

    geode = osg.Geode()
    geode.addDrawable(geometry)
    geode.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)

    group = osg.Group()
    group.addChild(geode)

    return group

int main(int , char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # set the scene to render
    viewer.setSceneData(createScene(50000))

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
