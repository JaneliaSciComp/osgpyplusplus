#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgtexturerectangle"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osgtexturerectangle.cpp'

# OpenSceneGraph example, osgtexturerectangle.
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

#
# * demonstrates usage of osg.TextureRectangle.
# *
# * Actually there isn't much difference to the rest of the osg.Texture*
# * bunch only this:
# * - texture coordinates for texture rectangles must be in image
# *   coordinates instead of normalized coordinates (0-1). So for a 500x250
# *   image the coordinates for the entire image would be
# *   0,250 0,0 500,0 500,250 instead of 0,1 0,0 1,0 1,1
# * - only the following wrap modes are supported (but not enforced)
# *   CLAMP, CLAMP_TO_EDGE, CLAMP_TO_BORDER
# * - a border is not supported
# * - mipmap is not supported
# 

#include <osg/Notify>
#include <osg/TextureRectangle>
#include <osg/Geometry>
#include <osg/Geode>
#include <osg/TexMat>

#include <osg/Group>
#include <osg/Projection>
#include <osg/MatrixTransform>
#include <osgText/Text>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>


#*********************************************************************
# *
# * Texture pan animation callback
# *
# *********************************************************************

class TexturePanCallback (osg.NodeCallback) :
    TexturePanCallback(osg.TexMat* texmat,
                       delay = 0.05) :
        _texmat(texmat),
        _phaseS(35.0),
        _phaseT(18.0),
        _phaseScale(5.0),
        _delay(delay),
        _prevTime(0.0)

    virtual void operator()(osg.Node*, osg.NodeVisitor* nv)
        if !_texmat :
            return

        if nv.getFrameStamp() : 
            currTime = nv.getFrameStamp().getSimulationTime()
            if currTime - _prevTime > _delay : 

                rad = osg.DegreesToRadians(currTime)

                # zoom scale (0.2 - 1.0)
                scale = sin(rad * _phaseScale) * 0.4 + 0.6
                scaleR = 1.0 - scale

                # calculate texture coordinates
                float s, t()
                s = ((sin(rad * _phaseS) + 1) * 0.5) * (scaleR)
                t = ((sin(rad * _phaseT) + 1) * 0.5) * (scaleR)


                _texmat.setMatrix(osg.Matrix.translate(s,t,1.0)*osg.Matrix.scale(scale,scale,1.0))

                # record time
                _prevTime = currTime
    _texmat = osg.TexMat*()

    float _phaseS, _phaseT, _phaseScale

    _delay = double()
    _prevTime = double()



def createRectangle(bb, filename):


    
    top_left = osg.Vec3(bb.xMin(),bb.yMax(),bb.zMax())
    bottom_left = osg.Vec3(bb.xMin(),bb.yMax(),bb.zMin())
    bottom_right = osg.Vec3(bb.xMax(),bb.yMax(),bb.zMin())
    top_right = osg.Vec3(bb.xMax(),bb.yMax(),bb.zMax())

    # create geometry
    geom = osg.Geometry()

    vertices = osg.Vec3Array(4)
    (*vertices)[0] = top_left
    (*vertices)[1] = bottom_left
    (*vertices)[2] = bottom_right
    (*vertices)[3] = top_right
    geom.setVertexArray(vertices)

    texcoords = osg.Vec2Array(4)
    (*texcoords)[0].set(0.0, 0.0)
    (*texcoords)[1].set(1.0, 0.0)
    (*texcoords)[2].set(1.0, 1.0)
    (*texcoords)[3].set(0.0, 1.0)
    geom.setTexCoordArray(0,texcoords)

    normals = osg.Vec3Array(1)
    (*normals)[0].set(0.0,-1.0,0.0)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

    colors = osg.Vec4Array(1)
    (*colors)[0].set(1.0,1.0,1.0,1.0)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(osg.DrawArrays(GL_QUADS, 0, 4))

    # disable display list so our modified tex coordinates show up
    geom.setUseDisplayList(False)

    # load image
    img = osgDB.readImageFile(filename)

    # setup texture
    texture = osg.TextureRectangle(img)

    texmat = osg.TexMat()
    texmat.setScaleByTextureRectangleSize(True)

    # setup state
    state = geom.getOrCreateStateSet()
    state.setTextureAttributeAndModes(0, texture, osg.StateAttribute.ON)
    state.setTextureAttributeAndModes(0, texmat, osg.StateAttribute.ON)

    # turn off lighting
    state.setMode(GL_LIGHTING, osg.StateAttribute.OFF)

    # install 'update' callback
    geode = osg.Geode()
    geode.addDrawable(geom)
    geode.setUpdateCallback(TexturePanCallback(texmat))

    return geode


def createText(str, pos):


    
    static str font("fonts/arial.ttf")

    geode = osg.Geode()

    text = osgText.Text()
    geode.addDrawable(text)

    text.setFont(font)
    text.setPosition(pos)
    text.setText(str)

    return geode


def createHUD():


    
    group = osg.Group()

    # turn off lighting and depth test
    state = group.getOrCreateStateSet()
    state.setMode(GL_LIGHTING, osg.StateAttribute.OFF)
    state.setMode(GL_DEPTH_TEST, osg.StateAttribute.OFF)

    # add text
    pos = osg.Vec3(120.0, 800.0, 0.0)
    delta =  osg.Vec3(0.0, -80.0, 0.0)

     char* text[] = 
        "TextureRectangle Mini-HOWTO",
        "- essentially behaves like Texture2D, *except* that:",
        "- tex coords must be non-normalized (0..pixel) instead of (0..1),\nalternatively you can use osg.TexMat to scale normal non dimensional texcoords.",
        "- wrap modes must be CLAMP, CLAMP_TO_EDGE, or CLAMP_TO_BORDER\n  repeating wrap modes are not supported",
        "- filter modes must be NEAREST or LINEAR since\n  mipmaps are not supported",
        "- texture borders are not supported",
        "- defaults should be fine",
        NULL
    
    t = text
    while *t : 
        group.addChild(createText(*t++, pos))
        pos += delta

    # create HUD
    modelview_abs = osg.MatrixTransform()
    modelview_abs.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    modelview_abs.setMatrix(osg.Matrix.identity())
    modelview_abs.addChild(group)

    projection = osg.Projection()
    projection.setMatrix(osg.Matrix.ortho2D(0,1280,0,1024))
    projection.addChild(modelview_abs)

    return projection


def createModel(filename):


    
    root = osg.Group()

    if filename != "X" : 
        bb = osg.BoundingBox(0.0,0.0,0.0,1.0,1.0,1.0)
        root.addChild(createRectangle(bb, filename)) # XXX

    root.addChild(createHUD())

    return root


def main(argc, argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # create a model from the images.
    rootNode = createModel((arguments.argc() > 1 ? arguments[1] : "Images/lz.rgb"))

    # add model to viewer.
    viewer.setSceneData(rootNode)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
