#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgtexturerectangle"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgViewer

# OpenSceneGraph example, osgtexturerectangle.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


#
 * demonstrates usage of osg.TextureRectangle.
 *
 * Actually there isn't much difference to the rest of the osg.Texture*
 * bunch only this:
 * - texture coordinates for texture rectangles must be in image
 *   coordinates instead of normalized coordinates (0-1). So for a 500x250
 *   image the coordinates for the entire image would be
 *   0,250 0,0 500,0 500,250 instead of 0,1 0,0 1,0 1,1
 * - only the following wrap modes are supported (but not enforced)
 *   CLAMP, CLAMP_TO_EDGE, CLAMP_TO_BORDER
 * - a border is not supported
 * - mipmap is not supported
 

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
 *
 * Texture pan animation callback
 *
 *********************************************************************

class TexturePanCallback : public osg.NodeCallback
public:
    TexturePanCallback(osg.TexMat* texmat,
                       delay =  0.05) :
        _texmat(texmat),
        _phaseS(35.0f),
        _phaseT(18.0f),
        _phaseScale(5.0f),
        _delay(delay),
        _prevTime(0.0)

    virtual void operator()(osg.Node*, osg.NodeVisitor* nv)
        if !_texmat :
            return

        if nv.getFrameStamp() : 
            currTime =  nv.getFrameStamp().getSimulationTime()
            if currTime - _prevTime > _delay : 

                rad =  osg.DegreesToRadians(currTime)

                # zoom scale (0.2 - 1.0)
                scale =  sin(rad * _phaseScale) * 0.4f + 0.6f
                scaleR =  1.0f - scale

                # calculate new texture coordinates
                float s, t
                s = ((sin(rad * _phaseS) + 1) * 0.5f) * (scaleR)
                t = ((sin(rad * _phaseT) + 1) * 0.5f) * (scaleR)


                _texmat.setMatrix(osg.Matrix.translate(s,t,1.0)*osg.Matrix.scale(scale,scale,1.0))

                # record time
                _prevTime = currTime

private:
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
    geom =  new osg.Geometry

    vertices =  new osg.Vec3Array(4)
    (*vertices)[0] = top_left
    (*vertices)[1] = bottom_left
    (*vertices)[2] = bottom_right
    (*vertices)[3] = top_right
    geom.setVertexArray(vertices)

    texcoords =  new osg.Vec2Array(4)
    (*texcoords)[0].set(0.0f, 0.0f)
    (*texcoords)[1].set(1.0f, 0.0f)
    (*texcoords)[2].set(1.0f, 1.0f)
    (*texcoords)[3].set(0.0f, 1.0f)
    geom.setTexCoordArray(0,texcoords)

    normals =  new osg.Vec3Array(1)
    (*normals)[0].set(0.0f,-1.0f,0.0f)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

    colors =  new osg.Vec4Array(1)
    (*colors)[0].set(1.0f,1.0f,1.0f,1.0f)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(new osg.DrawArrays(GL_QUADS, 0, 4))

    # disable display list so our modified tex coordinates show up
    geom.setUseDisplayList(false)

    # load image
    img =  osgDB.readImageFile(filename)

    # setup texture
    texture =  new osg.TextureRectangle(img)

    texmat =  new osg.TexMat
    texmat.setScaleByTextureRectangleSize(true)

    # setup state
    state =  geom.getOrCreateStateSet()
    state.setTextureAttributeAndModes(0, texture, osg.StateAttribute.ON)
    state.setTextureAttributeAndModes(0, texmat, osg.StateAttribute.ON)

    # turn off lighting
    state.setMode(GL_LIGHTING, osg.StateAttribute.OFF)

    # install 'update' callback
    geode =  new osg.Geode
    geode.addDrawable(geom)
    geode.setUpdateCallback(new TexturePanCallback(texmat))

    geode = return()


def createText(str, pos):
    static str font("fonts/arial.ttf")

    geode =  new osg.Geode

    text =  new osgText.Text
    geode.addDrawable(text)

    text.setFont(font)
    text.setPosition(pos)
    text.setText(str)

    geode = return()


def createHUD():
    group =  new osg.Group

    # turn off lighting and depth test
    state =  group.getOrCreateStateSet()
    state.setMode(GL_LIGHTING, osg.StateAttribute.OFF)
    state.setMode(GL_DEPTH_TEST, osg.StateAttribute.OFF)

    # add text
    pos = osg.Vec3(120.0f, 800.0f, 0.0f)
    delta =  osg.Vec3(0.0f, -80.0f, 0.0f)

     char* text[] = 
        "TextureRectangle Mini-HOWTO",
        "- essentially behaves like Texture2D, *except* that:",
        "- tex coords must be non-normalized (0..pixel) instead of (0..1),\nalternatively you can use osg.TexMat to scale normal non dimensional texcoords.",
        "- wrap modes must be CLAMP, CLAMP_TO_EDGE, or CLAMP_TO_BORDER\n  repeating wrap modes are not supported",
        "- filter modes must be NEAREST or LINEAR since\n  mipmaps are not supported",
        "- texture borders are not supported",
        "- defaults should be fine",
        NULL
    
    t =  text
    while *t : 
        group.addChild(createText(*t++, pos))
        pos += delta

    # create HUD
    modelview_abs =  new osg.MatrixTransform
    modelview_abs.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    modelview_abs.setMatrix(osg.Matrix.identity())
    modelview_abs.addChild(group)

    projection =  new osg.Projection
    projection.setMatrix(osg.Matrix.ortho2D(0,1280,0,1024))
    projection.addChild(modelview_abs)

    projection = return()


def createModel(filename):
    root =  new osg.Group

    if filename != "X" : 
        bb = osg.BoundingBox(0.0f,0.0f,0.0f,1.0f,1.0f,1.0f)
        root.addChild(createRectangle(bb, filename)) # XXX

    root.addChild(createHUD())

    root = return()


def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # create a model from the images.
    rootNode =  createModel((arguments.argc() > 1 ? arguments[1] : "Images/lz.rgb"))

    # add model to viewer.
    viewer.setSceneData(rootNode)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
