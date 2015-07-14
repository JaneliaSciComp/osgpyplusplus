#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgtext3D"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgtext3D.cpp'

# OpenSceneGraph example, osgtext.
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

#include <osg/ArgumentParser>
#include <osg/Material>
#include <osg/PositionAttitudeTransform>
#include <osg/io_utils>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgGA/StateSetManipulator>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgText/Text3D>

#include "TextNode.h"


def main(argv):


    
    arguments = osg.ArgumentParser(argv)

    viewer = osgViewer.Viewer(arguments)

    fontFile = str("arial.ttf")
    while arguments.read("-f",fontFile) : 

    font = osgText.readFontFile(fontFile)
    if  not font : return 1
    OSG_NOTICE, "Read font ", fontFile, " font=", font

    word = str("This is a test.")()
    while arguments.read("-w",word) : 

    style = osgText.Style()

    thickness = 0.1
    while arguments.read("--thickness",thickness) : 
    style.setThicknessRatio(thickness)

    # set up any bevel if required
    r = float()
    bevel = osgText.Bevel()
    while arguments.read("--rounded",r) :  bevel = osgText.Bevel() bevel.roundedBevel2(r) 
    while arguments.read("--rounded") :  bevel = osgText.Bevel() bevel.roundedBevel2(0.25) 
    while arguments.read("--flat",r) :  bevel = osgText.Bevel() bevel.flatBevel(r) 
    while arguments.read("--flat") :  bevel = osgText.Bevel() bevel.flatBevel(0.25) 
    while arguments.read("--bevel-thickness",r) :  if bevel.valid() : bevel.setBevelThickness(r) 

    style.setBevel(bevel)

    # set up outline.
    while arguments.read("--outline",r) :  style.setOutlineRatio(r) 


    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    viewer.addEventHandler(osgViewer.StatsHandler)()

#if 1
    group = osg.Group()

    characterSize = 1.0
    while arguments.read("--size",characterSize) : 

    if arguments.read("--2d") :
        text2D = osgText.Text()
        text2D.setFont(font)
        text2D.setCharacterSize(characterSize)
        text2D.setFontResolution(256,256)
        text2D.setDrawMode(osgText.Text.TEXT | osgText.Text.BOUNDINGBOX)
        text2D.setAxisAlignment(osgText.Text.XZ_PLANE)
        text2D.setText(word)
        geode = osg.Geode()
        geode.addDrawable(text2D)
        group.addChild(geode)

    if arguments.read("--TextNode") :
        # experimental text node
        text = osgText.TextNode()
        text.setFont(font)
        text.setStyle(style)
        text.setTextTechnique(osgText.TextTechnique)()
        text.setText(word)
        text.update()

        group.addChild(text)
    elif  not arguments.read("--no-3d") :
        text3D = osgText.Text3D()
        text3D.setFont(font)
        text3D.setStyle(style)
        text3D.setCharacterSize(characterSize)
        text3D.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
        text3D.setAxisAlignment(osgText.Text3D.XZ_PLANE)
        text3D.setText(word)

        geode = osg.Geode()
        geode.addDrawable(text3D)
        group.addChild(geode)

        color = osg.Vec4(1.0, 1.0, 1.0, 1.0)
        while arguments.read("--color",color.r(),color.g(),color.b(),color.a()) :
            OSG_NOTICE, "--color ", color
            text3D.setColor(color)

        imageFilename = str()
        while arguments.read("--image",imageFilename) :
            OSG_NOTICE, "--image ", imageFilename
            image = osgDB.readImageFile(imageFilename)
            if image.valid() :
                OSG_NOTICE, "  loaded image ", imageFilename
                stateset = text3D.getOrCreateStateSet()
                stateset.setTextureAttributeAndModes(0, osg.Texture2D(image), osg.StateAttribute.ON)

        while arguments.read("--wall-color",color.r(),color.g(),color.b(),color.a()) :
            stateset = text3D.getOrCreateWallStateSet()
            material = osg.Material()
            material.setDiffuse(osg.Material.FRONT_AND_BACK, color)
            stateset.setAttribute(material)

        while arguments.read("--wall-image",imageFilename) :
            image = osgDB.readImageFile(imageFilename)
            if image.valid() :
                stateset = text3D.getOrCreateWallStateSet()
                stateset.setTextureAttributeAndModes(0, osg.Texture2D(image), osg.StateAttribute.ON)

        while arguments.read("--back-color",color.r(),color.g(),color.b(),color.a()) :
            stateset = text3D.getOrCreateBackStateSet()
            material = osg.Material()
            material.setDiffuse(osg.Material.FRONT_AND_BACK, color)
            stateset.setAttribute(material)

        while arguments.read("--back-image",imageFilename) :
            image = osgDB.readImageFile(imageFilename)
            if image.valid() :
                stateset = text3D.getOrCreateBackStateSet()
                stateset.setTextureAttributeAndModes(0, osg.Texture2D(image), osg.StateAttribute.ON)

        if arguments.read("--size-quad") :
            geode.addDrawable( osg.createTexturedQuadGeometry(osg.Vec3(0.0,characterSize*thickness,0.0),osg.Vec3(characterSize,0.0,0.0),osg.Vec3(0.0,0.0,characterSize), 0.0, 0.0, 1.0, 1.0) )

    
    viewer.setSceneData(group)

#endif

    return viewer.run()

# Translated from file 'osgtext3D_orig.cpp'

# OpenSceneGraph example, osgtext.
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

#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>

#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Material>
#include <osg/Shape>
#include <osg/ShapeDrawable>
#include <osgText/Text3D>

#include <iostream>
#include <sstream>



# create text which sits in 3D space such as would be inserted into a normal model
def create3DText(center, radius):
    

    geode = osg.Geode()

####################################################
#    
# Examples of how to set up axis/orientation alignments
#

    characterSize = radius*0.2
    characterDepth = characterSize*0.2
    
    pos = osg.Vec3(center.x()-radius*.5,center.y()-radius*.5,center.z()-radius*.5)

    text1 = osgText.Text3D()
    text1.setFont("fonts/arial.ttf")
    text1.setCharacterSize(characterSize)
    text1.setCharacterDepth(characterDepth)
    text1.setPosition(pos)
    text1.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text1.setAxisAlignment(osgText.Text3D.XY_PLANE)
    text1.setText("XY_PLANE")
    geode.addDrawable(text1)

    text2 = osgText.Text3D()
    text2.setFont("fonts/times.ttf")
    text2.setCharacterSize(characterSize)
    text2.setCharacterDepth(characterDepth)
    text2.setPosition(pos)
    text2.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text2.setAxisAlignment(osgText.Text3D.YZ_PLANE)
    text2.setText("YZ_PLANE")
    geode.addDrawable(text2)

    text3 = osgText.Text3D()
    text3.setFont("fonts/dirtydoz.ttf")
    text3.setCharacterSize(characterSize)
    text3.setCharacterDepth(characterDepth)
    text3.setPosition(pos)
    text3.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text3.setAxisAlignment(osgText.Text3D.XZ_PLANE)
    text3.setText("XZ_PLANE")
    geode.addDrawable(text3)

    style = osgText.Style()
    bevel = osgText.Bevel()
    bevel.roundedBevel2(0.25)
    style.setBevel(bevel)
    style.setWidthRatio(0.4)

    text7 = osgText.Text3D()
    text7.setFont("fonts/times.ttf")
    text7.setStyle(style)
    text7.setCharacterSize(characterSize)
    text7.setCharacterDepth(characterSize*0.2)
    text7.setPosition(center - osg.Vec3(0.0, 0.0, 0.6))
    text7.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text7.setAxisAlignment(osgText.Text3D.SCREEN)
    text7.setCharacterSizeMode(osgText.Text3D.OBJECT_COORDS)
    text7.setText("CharacterSizeMode OBJECT_COORDS (default)")
    geode.addDrawable(text7)

    shape = osg.ShapeDrawable(osg.Sphere(center,characterSize*0.2))
    shape.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.ON)
    geode.addDrawable(shape)

    rootNode = osg.Group()
    rootNode.addChild(geode)

    front = osg.Material()
    front.setAlpha(osg.Material.FRONT_AND_BACK,1)
    front.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(0.2,0.2,0.2,1.0))
    front.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(.0,.0,1.0,1.0))
    rootNode.getOrCreateStateSet().setAttributeAndModes(front)
    
    
    return rootNode    

int main_orig(int, char**)
    viewer = osgViewer.Viewer()

    center = osg.Vec3(0.0,0.0,0.0)
    radius = 1.0
    
    root = osg.Group()
    root.addChild(create3DText(center, radius))

    viewer.setSceneData(root)
    viewer.setCameraManipulator(osgGA.TrackballManipulator())
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    viewer.addEventHandler(osgViewer.ThreadingHandler)()
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()
    viewer.addEventHandler(osgViewer.StatsHandler)()


    viewer.run()
    
    return 0



# Translated from file 'osgtext3D_test.cpp'


#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgDB/ReadFile>

#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>

#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Material>
#include <osg/Shape>
#include <osg/ShapeDrawable>
#include <osgText/Text3D>

#include <iostream>
#include <sstream>



def test_create3DText(center, radius):



    

    geode = osg.Geode()

    characterSize = radius*0.2
    characterDepth = characterSize*0.2
    
    pos = osg.Vec3(center.x()-radius*.5,center.y()-radius*.5,center.z()-radius*.5)
#define SHOW_INTESECTION_CEASH
#ifdef SHOW_INTESECTION_CEASH
    text3 = osgText.Text3D()
    text3.setFont("fonts/dirtydoz.ttf")
    text3.setCharacterSize(characterSize)
    text3.setCharacterDepth(characterDepth)
    text3.setPosition(pos)
    text3.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text3.setAxisAlignment(osgText.Text3D.XZ_PLANE)
    text3.setText("CRAS H") #intersection crash
    geode.addDrawable(text3)
#else:
    text7 = osgText.Text3D()
    text7.setFont("fonts/times.ttf")
    text7.setCharacterSize(characterSize)
    text7.setCharacterDepth(characterSize*2.2)
    text7.setPosition(center - osg.Vec3(0.0, 0.0, 0.6))
    text7.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text7.setAxisAlignment(osgText.Text3D.SCREEN)
    text7.setCharacterSizeMode(osgText.Text3D.OBJECT_COORDS)
    text7.setText("ABCDE") #wrong intersection
    geode.addDrawable(text7)
#endif

    shape = osg.ShapeDrawable(osg.Sphere(center,characterSize*0.2))
    shape.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.ON)
    geode.addDrawable(shape)

    rootNode = osg.Group()
    rootNode.addChild(geode)

#define SHOW_WRONG_NORMAL
#ifdef SHOW_WRONG_NORMAL
    front = osg.Material() #
    front.setAlpha(osg.Material.FRONT_AND_BACK,1)
    front.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(0.2,0.2,0.2,1.0))
    front.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(.0,.0,1.0,1.0))
    rootNode.getOrCreateStateSet().setAttributeAndModes(front)
#else:
    stateset = osg.StateSet() #Show wireframe
    polymode = osg.PolygonMode()
    polymode.setMode(osg.PolygonMode.FRONT_AND_BACK,osg.PolygonMode.LINE)
    stateset.setAttributeAndModes(polymode,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
    rootNode.setStateSet(stateset)
#endif
    
    
    return rootNode    

#####################################
#include <osg/PositionAttitudeTransform>
#include <osg/ShapeDrawable>
class CInputHandler (osgGA.GUIEventHandler) :
  CInputHandler( osg.PositionAttitudeTransform* pPatSphere )
    m_rPatSphere = pPatSphere
  def handle(ea, aa, pObject, pNodeVisitor):
      
    pViewer = dynamic_cast<osgViewer.Viewer*>(aa)
    if   not pViewer  :
      return False

    if  ea.getEventType()==osgGA.GUIEventAdapter.PUSH  :
      cams = osgViewer.ViewerBase.Cameras()
      pViewer.getCameras( cams )

      x = ea.getXnormalized()
      y = ea.getYnormalized()

      picker = osgUtil.LineSegmentIntersector( osgUtil.Intersector.PROJECTION, x, y )
      iv = osgUtil.IntersectionVisitor( picker )
      cams[0].accept( iv )

      if  picker.containsIntersections()  :
        intersection = picker.getFirstIntersection()
        v = intersection.getWorldIntersectPoint()
        m_rPatSphere.setPosition( v )

      return True # return True, event handled

    return False
  m_rPatSphere = osg.PositionAttitudeTransform()

#####################################
int main_test(int, char**)
    viewer = osgViewer.Viewer()
    viewer.setUpViewInWindow(99,99,666,666, 0)
    rPat = osg.PositionAttitudeTransform()
    # add the handler to the viewer
    viewer.addEventHandler( CInputHandler(rPat) )
    # create a group to contain our scene and sphere
    pGroup = osg.Group()
    # create sphere
    pGeodeSphere = osg.Geode()
    pGeodeSphere.addDrawable( osg.ShapeDrawable( osg.Sphere(osg.Vec3(0.0,0.0,0.0),0.01) ) )
    rPat.addChild( pGeodeSphere )
    pGroup.addChild( rPat )

    center = osg.Vec3(0.0,0.0,0.0)
    radius = 1.0

    root = osg.Group()
    root.addChild(test_create3DText(center, radius))

    #viewer.setSceneData(root)
    pGroup.addChild(root)
    viewer.setSceneData(pGroup)
    viewer.setCameraManipulator(osgGA.TrackballManipulator())
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    viewer.addEventHandler(osgViewer.ThreadingHandler)()
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()
    viewer.addEventHandler(osgViewer.StatsHandler)()

    return viewer.run()



# Translated from file 'TextNode.cpp'

# -*-c++-*- OpenSceneGraph - Copyright (C) 1998-2010 Robert Osfield
# *
# * This library is open source and may be redistributed and/or modified under
# * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or
# * (at your option) any later version.  The full license is in LICENSE file
# * included with this distribution, and on the openscenegraph.org website.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * OpenSceneGraph Public License for more details.
#

#include "TextNode.h"
#include "../../src/osgText/GlyphGeometry.h"

#include <osg/PositionAttitudeTransform>
#include <osg/Geode>
#include <osgUtil/SmoothingVisitor>

#include <osg/io_utils>

using namespace osgText

############################################/
#
# Layout
#
Layout.Layout()

Layout.Layout( Layout layout,  osg.CopyOp copyop):
    osg.Object(layout,copyop)

Layout Layout.getDefaultLayout()
    static OpenThreads.Mutex s_DefaultLayoutMutex
    lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(s_DefaultLayoutMutex)

    static Layout s_defaultLayout = Layout()
    return s_defaultLayout

void Layout.layout(TextNode text) 
    OSG_NOTICE, "Layout.layout"

    font = text.getActiveFont()
    style = text.getActiveStyle()
    technique = text.getTextTechnique()
    str = text.getText()

    if  not text.getTextTechnique() :
        OSG_NOTICE, "Warning: no TextTechnique assigned to Layout"
        return

    pos = osg.Vec3(0.0,0.0,0.0)
    characterSize = text.getCharacterSize()
    size = osg.Vec3(characterSize, characterSize, 0.0)
    if style :
        size.y() = characterSize
        size.z() = characterSize


    resolution = osgText.FontResolution(32,32)
    if style :
        resolution.first = static_cast<unsigned int>(static_cast<float>(resolution.first)*style.getSampleDensity())
        resolution.second = static_cast<unsigned int>(static_cast<float>(resolution.second)*style.getSampleDensity())

    characterWidthScale = 1.0

    textIs3D = (style  and  style.getThicknessRatio() not =0.0)
    if  not textIs3D :
        characterWidthScale = 1.0/static_cast<float>(resolution.first)

    kerningType = osgText.KERNING_DEFAULT

    technique.start()

    previousCharcode = 0
    for(unsigned int i=0 i<str.size() ++i)
        charcode = str[i]

        if size.z()==0.0 :
            glyph = font.getGlyph(resolution, charcode)
            if glyph :
                technique.addCharacter(pos, size, glyph, style)
                pos += osg.Vec3(size.x()*(glyph.getHorizontalAdvance()*characterWidthScale), 0.0 ,0.0)
        else:
            glyph = font.getGlyph3D(charcode)
            OSG_NOTICE, "pos = ", pos, ", charcode=", charcode, ", glyph=", glyph
            if glyph :
                local_scale = osg.Vec3( size )
                technique.addCharacter(pos, local_scale, glyph, style)
                pos += osg.Vec3(size.x()*glyph.getWidth(), 0.0 ,0.0)

        if previousCharcode not =0  and  charcode not =0 :
            offset = font.getKerning(previousCharcode, charcode, kerningType)
            OSG_NOTICE, "  offset = ", offset
            pos.x() += offset.x()
            pos.y() += offset.y()

        previousCharcode = charcode

    technique.finish()


############################################/
#
# TextTechnique
#
TextTechnique.TextTechnique():
    _textNode(0)


TextTechnique.TextTechnique( TextTechnique technique,  osg.CopyOp copyop):
    osg.Object(technique, copyop),
    _textNode(0)

TextTechnique TextTechnique.getDefaultTextTechinque()
    static OpenThreads.Mutex s_DefaultTextTechniqueMutex
    lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(s_DefaultTextTechniqueMutex)

    static TextTechnique s_defaultTextTechnique = TextTechnique()
    return s_defaultTextTechnique

void TextTechnique.start()
    OSG_NOTICE, "TextTechnique.start()"

void TextTechnique.addCharacter( osg.Vec3 position,  osg.Vec3 size, Glyph* glyph, Style* style)
    OSG_NOTICE, "TextTechnique.addCharacter 2D(", position, ", ", size, ", ", glyph, ", ", style, ")"

void TextTechnique.addCharacter( osg.Vec3 position,  osg.Vec3 size, Glyph3D* glyph, Style* style)
    OSG_NOTICE, "TextTechnique.addCharacter 3D(", position, ", ", size, ", ", glyph, ", ", style, ")"

    transform = osg.PositionAttitudeTransform()
    transform.setPosition(position)
    transform.setAttitude(osg.Quat(osg.inDegrees(90.0),osg.Vec3d(1.0,0.0,0.0)))
    transform.setScale(size)

    geode = osg.Geode()

    bevel =  style.getBevel() if (style) else  0
    outline =  style.getOutlineRatio()>0.0 if (style) else  False
    width = style.getThicknessRatio()
    creaseAngle = 30.0
    smooth = True

    if bevel :
        thickness = bevel.getBevelThickness()

        glyphGeometry = osgText.computeGlyphGeometry(glyph, thickness, width)
        textGeometry = osgText.computeTextGeometry(glyphGeometry, *bevel, width)
        shellGeometry =  osgText.computeShellGeometry(glyphGeometry, *bevel, width) if (outline) else  0
        if textGeometry.valid() : geode.addDrawable(textGeometry)
        if shellGeometry.valid() : geode.addDrawable(shellGeometry)

        # create the normals
        if smooth  and  textGeometry.valid() :
            osgUtil.SmoothingVisitor.smooth(*textGeometry, osg.DegreesToRadians(creaseAngle))
    else:
        textGeometry = osgText.computeTextGeometry(glyph, width)
        if textGeometry.valid() : geode.addDrawable(textGeometry)

        # create the normals
        if smooth  and  textGeometry.valid() :
            osgUtil.SmoothingVisitor.smooth(*textGeometry, osg.DegreesToRadians(creaseAngle))

    transform.addChild(geode)

    _textNode.addChild(transform)

    transform.getOrCreateStateSet().setMode(GL_NORMALIZE, osg.StateAttribute.ON)


void TextTechnique.finish()
    OSG_NOTICE, "TextTechnique.finish()"

void TextTechnique.traverse(osg.NodeVisitor nv)
    # OSG_NOTICE, "TextTechnique.traverse()"
    if _textNode : _textNode.osg.Group.traverse(nv)

############################################/
#
# TextNode
#
TextNode.TextNode():
        _characterSize(1.0)


TextNode.TextNode( TextNode text,  osg.CopyOp copyop):
    osg.Group(text, copyop)

TextNode.~TextNode()
    setTextTechnique(0)

void TextNode.traverse(osg.NodeVisitor nv)
    if _technique.valid() :
        _technique.traverse(nv)
    else:
        Group.traverse(nv)

void TextNode.setTextTechnique(TextTechnique* technique)
    if _technique==technique : return

    if _technique.valid() : _technique.setTextNode(0)

    if TextTechnique.getDefaultTextTechinque()==technique :
        OSG_NOTICE, "Warning: Attempt to assign DefaultTextTechnique() prototype to TextNode.setTextTechnique(..), assigning a clone() of it instead."
        technique = TextTechnique(*TextTechnique.getDefaultTextTechinque())

    _technique = technique

    if _technique.valid() : _technique.setTextNode(this)


void TextNode.update()
    getActiveLayout().layout(*this)

void TextNode.setText( str str)
    _string.set(str)

# Translated from file 'TextNode.h'

# -*-c++-*- OpenSceneGraph - Copyright (C) 1998-2010 Robert Osfield
# *
# * This library is open source and may be redistributed and/or modified under
# * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or
# * (at your option) any later version.  The full license is in LICENSE file
# * included with this distribution, and on the openscenegraph.org website.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * OpenSceneGraph Public License for more details.
#

#ifndef OSGTEXT_TEXTNODE
#define OSGTEXT_TEXTNODE 1


#include <osg/Group>
#include <osg/Quat>
#include <osgUtil/CullVisitor>

#include <osgText/Font>
#include <osgText/String>
#include <osgText/Glyph>
#include <osgText/Style>

namespace osgText 

# forward declare
TextNode = class()

class #OSGTEXT_EXPORT Layout : public osg.Object

        Layout()
        Layout( Layout layout,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY)

        META_Object(osgText,Layout)

        #/ default Layout implementation used if no other is specified on TextNode
        static Layout getDefaultLayout()

        virtual void layout(TextNode text) 


class #OSGTEXT_EXPORT TextTechnique : public osg.Object

        TextTechnique()
        TextTechnique( TextTechnique technique,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY)

        META_Object(osgText, TextTechnique)

        def getTextNode():

             return _textNode 
        def getTextNode():
             return _textNode 

        #/ default TextTechnique implementation used if no other is specified on TextNode
        static TextTechnique getDefaultTextTechinque()

        #/ start building a charater layout
        start = virtual void()

        #/ called by Layout engine to place individual characters
        addCharacter = virtual void( osg.Vec3 position,  osg.Vec3 size, Glyph* glyph, Style* style)

        #/ called by Layout engine to place individual characters
        addCharacter = virtual void( osg.Vec3 position,  osg.Vec3 size, Glyph3D* glyph, Style* style)

        #/ finish building charater layout
        finish = virtual void()

        #/ provide traversal control
        traverse = virtual void(osg.NodeVisitor nv)

        friend class TextNode

        def setTextNode(textNode):

             _textNode = textNode 

        _textNode = TextNode*()


class #OSGTEXT_EXPORT TextNode : public osg.Group

        TextNode()
        TextNode( TextNode text,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY)

        META_Node(osgText, TextNode)

        traverse = virtual void(osg.NodeVisitor nv)

        def setFont(font):

             _font = font 
        def getFont():
             return _font 
        def getFont():
             return _font 
        def getActiveFont():
             return  _font : Font: if (_font.valid()) else getDefaultFont() 
        def getActiveFont():
             return  _font : Font: if (_font.valid()) else getDefaultFont() 

        def setStyle(style):

             _style = style 
        def getStyle():
             return _style 
        def getStyle():
             return _style 
        def getActiveStyle():
             return  _style : Style: if (_style.valid()) else getDefaultStyle() 
        def getActiveStyle():
             return  _style : Style: if (_style.valid()) else getDefaultStyle() 

        def setLayout(layout):

             _layout = layout 
        def getLayout():
             return _layout 
        def getLayout():
             return _layout 
        def getActiveLayout():
             return  _layout : Layout: if (_layout.valid()) else getDefaultLayout() 

        setTextTechnique = void(TextTechnique* technique)
        def getTextTechnique():
             return _technique 
        def getTextTechnique():
             return _technique 

        setText = void( str str)
        def setText(str):
             _string = str 
        def getText():
             return _string 
        def getText():
             return _string 

        def setPosition(position):

             _position  = position 
        def getPosition():
             return _position 

        def setRotation(rotation):

             _rotation  = rotation 
        def getRotation():
             return _rotation 

        def setCharacterSize(characterSize):

             _characterSize = characterSize 
        def getCharacterSize():
             return _characterSize 

        #/ force a regeneration of the rendering backend required to represent the text.
        update = virtual void()

        virtual ~TextNode()

        _font = Font()
        _style = Style()
        _layout = Layout()
        _technique = TextTechnique()

        _string = String()
        _position = osg.Vec3d()
        _rotation = osg.Quat()
        _characterSize = float()



#endif


if __name__ == "__main__":
    main(sys.argv)
