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

# OpenSceneGraph example, osgtext.
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


def main(argc, argv):
    arguments = osg.ArgumentParser(argc, argv)

    viewer = osgViewer.Viewer(arguments)

    fontFile = str("arial.ttf")
    while arguments.read("-f",fontFile) : 

    osg.ref_ptr<osgText.Font> font = osgText.readFontFile(fontFile)
    if !font : return 1
    OSG_NOTICE, "Read font ", fontFile, " font=", font.get()

    word = str("This is a new test.")
    while arguments.read("-w",word) : 

    osg.ref_ptr<osgText.Style> style = new osgText.Style

    thickness =  0.1f
    while arguments.read("--thickness",thickness) : 
    style.setThicknessRatio(thickness)

    # set up any bevel if required
    r = float()
    osg.ref_ptr<osgText.Bevel> bevel
    while arguments.read("--rounded",r) :  bevel = new osgText.Bevel bevel.roundedBevel2(r) 
    while arguments.read("--rounded") :  bevel = new osgText.Bevel bevel.roundedBevel2(0.25) 
    while arguments.read("--flat",r) :  bevel = new osgText.Bevel bevel.flatBevel(r) 
    while arguments.read("--flat") :  bevel = new osgText.Bevel bevel.flatBevel(0.25) 
    while arguments.read("--bevel-thickness",r) :  if bevel.valid() : bevel.setBevelThickness(r) 

    style.setBevel(bevel.get())

    # set up outline.
    while arguments.read("--outline",r) :  style.setOutlineRatio(r) 


    viewer.addEventHandler( new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    viewer.addEventHandler(new osgViewer.StatsHandler)

#if 1
    osg.ref_ptr<osg.Group> group = new osg.Group

    characterSize =  1.0f
    while arguments.read("--size",characterSize) : 

    if arguments.read("--2d") :
        text2D =  new osgText.Text
        text2D.setFont(font.get())
        text2D.setCharacterSize(characterSize)
        text2D.setFontResolution(256,256)
        text2D.setDrawMode(osgText.Text.TEXT | osgText.Text.BOUNDINGBOX)
        text2D.setAxisAlignment(osgText.Text.XZ_PLANE)
        text2D.setText(word)
        geode =  new osg.Geode
        geode.addDrawable(text2D)
        group.addChild(geode)

    if arguments.read("--TextNode") :
        # experimental text node
        text =  new osgText.TextNode
        text.setFont(font.get())
        text.setStyle(style.get())
        text.setTextTechnique(new osgText.TextTechnique)
        text.setText(word)
        text.update()

        group.addChild(text)
    else: if !arguments.read("--no-3d") :
        text3D =  new osgText.Text3D
        text3D.setFont(font.get())
        text3D.setStyle(style.get())
        text3D.setCharacterSize(characterSize)
        text3D.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
        text3D.setAxisAlignment(osgText.Text3D.XZ_PLANE)
        text3D.setText(word)

        geode =  new osg.Geode
        geode.addDrawable(text3D)
        group.addChild(geode)

        color = osg.Vec4(1.0f, 1.0f, 1.0f, 1.0f)
        while arguments.read("--color",color.r(),color.g(),color.b(),color.a()) :
            OSG_NOTICE, "--color ", color
            text3D.setColor(color)

        imageFilename = str()
        while arguments.read("--image",imageFilename) :
            OSG_NOTICE, "--image ", imageFilename
            osg.ref_ptr<osg.Image> image = osgDB.readImageFile(imageFilename)
            if image.valid() :
                OSG_NOTICE, "  loaded image ", imageFilename
                stateset =  text3D.getOrCreateStateSet()
                stateset.setTextureAttributeAndModes(0, new osg.Texture2D(image.get()), osg.StateAttribute.ON)

        while arguments.read("--wall-color",color.r(),color.g(),color.b(),color.a()) :
            stateset =  text3D.getOrCreateWallStateSet()
            material =  new osg.Material
            material.setDiffuse(osg.Material.FRONT_AND_BACK, color)
            stateset.setAttribute(material)

        while arguments.read("--wall-image",imageFilename) :
            osg.ref_ptr<osg.Image> image = osgDB.readImageFile(imageFilename)
            if image.valid() :
                stateset =  text3D.getOrCreateWallStateSet()
                stateset.setTextureAttributeAndModes(0, new osg.Texture2D(image.get()), osg.StateAttribute.ON)

        while arguments.read("--back-color",color.r(),color.g(),color.b(),color.a()) :
            stateset =  text3D.getOrCreateBackStateSet()
            material =  new osg.Material
            material.setDiffuse(osg.Material.FRONT_AND_BACK, color)
            stateset.setAttribute(material)

        while arguments.read("--back-image",imageFilename) :
            osg.ref_ptr<osg.Image> image = osgDB.readImageFile(imageFilename)
            if image.valid() :
                stateset =  text3D.getOrCreateBackStateSet()
                stateset.setTextureAttributeAndModes(0, new osg.Texture2D(image.get()), osg.StateAttribute.ON)

        if arguments.read("--size-quad") :
            geode.addDrawable( osg.createTexturedQuadGeometry(osg.Vec3(0.0f,characterSize*thickness,0.0f),osg.Vec3(characterSize,0.0,0.0),osg.Vec3(0.0f,0.0,characterSize), 0.0, 0.0, 1.0, 1.0) )

    
    viewer.setSceneData(group.get())

#endif

    return viewer.run()
# OpenSceneGraph example, osgtext.
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
    geode =  new osg.Geode

####################################################
#    
# Examples of how to set up axis/orientation alignments
#

    characterSize = radius*0.2f
    characterDepth = characterSize*0.2f
    
    pos = osg.Vec3(center.x()-radius*.5f,center.y()-radius*.5f,center.z()-radius*.5f)

    text1 =  new osgText.Text3D
    text1.setFont("fonts/arial.ttf")
    text1.setCharacterSize(characterSize)
    text1.setCharacterDepth(characterDepth)
    text1.setPosition(pos)
    text1.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text1.setAxisAlignment(osgText.Text3D.XY_PLANE)
    text1.setText("XY_PLANE")
    geode.addDrawable(text1)

    text2 =  new osgText.Text3D
    text2.setFont("fonts/times.ttf")
    text2.setCharacterSize(characterSize)
    text2.setCharacterDepth(characterDepth)
    text2.setPosition(pos)
    text2.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text2.setAxisAlignment(osgText.Text3D.YZ_PLANE)
    text2.setText("YZ_PLANE")
    geode.addDrawable(text2)

    text3 =  new osgText.Text3D
    text3.setFont("fonts/dirtydoz.ttf")
    text3.setCharacterSize(characterSize)
    text3.setCharacterDepth(characterDepth)
    text3.setPosition(pos)
    text3.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text3.setAxisAlignment(osgText.Text3D.XZ_PLANE)
    text3.setText("XZ_PLANE")
    geode.addDrawable(text3)

    osg.ref_ptr<osgText.Style> style = new osgText.Style
    osg.ref_ptr<osgText.Bevel> bevel = new osgText.Bevel
    bevel.roundedBevel2(0.25)
    style.setBevel(bevel.get())
    style.setWidthRatio(0.4f)

    text7 =  new osgText.Text3D
    text7.setFont("fonts/times.ttf")
    text7.setStyle(style.get())
    text7.setCharacterSize(characterSize)
    text7.setCharacterDepth(characterSize*0.2f)
    text7.setPosition(center - osg.Vec3(0.0, 0.0, 0.6))
    text7.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text7.setAxisAlignment(osgText.Text3D.SCREEN)
    text7.setCharacterSizeMode(osgText.Text3D.OBJECT_COORDS)
    text7.setText("CharacterSizeMode OBJECT_COORDS (default)")
    geode.addDrawable(text7)

    shape =  new osg.ShapeDrawable(new osg.Sphere(center,characterSize*0.2f))
    shape.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.ON)
    geode.addDrawable(shape)

    rootNode =  new osg.Group
    rootNode.addChild(geode)

    front =  new osg.Material
    front.setAlpha(osg.Material.FRONT_AND_BACK,1)
    front.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(0.2,0.2,0.2,1.0))
    front.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(.0,.0,1.0,1.0))
    rootNode.getOrCreateStateSet().setAttributeAndModes(front)
    
    
    rootNode = return()    

int main_orig(int, char**)
    viewer = osgViewer.Viewer()

    center = osg.Vec3(0.0f,0.0f,0.0f)
    radius =  1.0f
    
    root =  new osg.Group
    root.addChild(create3DText(center, radius))

    viewer.setSceneData(root)
    viewer.setCameraManipulator(new osgGA.TrackballManipulator())
    viewer.addEventHandler( new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    viewer.addEventHandler(new osgViewer.ThreadingHandler)
    viewer.addEventHandler(new osgViewer.WindowSizeHandler)
    viewer.addEventHandler(new osgViewer.StatsHandler)


    viewer.run()
    
    return 0



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
    geode =  new osg.Geode

    characterSize = radius*0.2f
    characterDepth = characterSize*0.2f
    
    pos = osg.Vec3(center.x()-radius*.5f,center.y()-radius*.5f,center.z()-radius*.5f)
#define SHOW_INTESECTION_CEASH
#ifdef SHOW_INTESECTION_CEASH
    text3 =  new osgText.Text3D
    text3.setFont("fonts/dirtydoz.ttf")
    text3.setCharacterSize(characterSize)
    text3.setCharacterDepth(characterDepth)
    text3.setPosition(pos)
    text3.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text3.setAxisAlignment(osgText.Text3D.XZ_PLANE)
    text3.setText("CRAS H") #intersection crash
    geode.addDrawable(text3)
#else:
    text7 =  new osgText.Text3D
    text7.setFont("fonts/times.ttf")
    text7.setCharacterSize(characterSize)
    text7.setCharacterDepth(characterSize*2.2f)
    text7.setPosition(center - osg.Vec3(0.0, 0.0, 0.6))
    text7.setDrawMode(osgText.Text3D.TEXT | osgText.Text3D.BOUNDINGBOX)
    text7.setAxisAlignment(osgText.Text3D.SCREEN)
    text7.setCharacterSizeMode(osgText.Text3D.OBJECT_COORDS)
    text7.setText("ABCDE") #wrong intersection
    geode.addDrawable(text7)
#endif

    shape =  new osg.ShapeDrawable(new osg.Sphere(center,characterSize*0.2f))
    shape.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.ON)
    geode.addDrawable(shape)

    rootNode =  new osg.Group
    rootNode.addChild(geode)

#define SHOW_WRONG_NORMAL
#ifdef SHOW_WRONG_NORMAL
    front =  new osg.Material #
    front.setAlpha(osg.Material.FRONT_AND_BACK,1)
    front.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(0.2,0.2,0.2,1.0))
    front.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(.0,.0,1.0,1.0))
    rootNode.getOrCreateStateSet().setAttributeAndModes(front)
#else:
    stateset =  new osg.StateSet #Show wireframe
    polymode =  new osg.PolygonMode
    polymode.setMode(osg.PolygonMode.FRONT_AND_BACK,osg.PolygonMode.LINE)
    stateset.setAttributeAndModes(polymode,osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)
    rootNode.setStateSet(stateset)
#endif
    
    
    rootNode = return()    

#####################################
#include <osg/PositionAttitudeTransform>
#include <osg/ShapeDrawable>
class CInputHandler : public osgGA.GUIEventHandler 
public:
  CInputHandler( osg.PositionAttitudeTransform* pPatSphere )
    m_rPatSphere = pPatSphere
  virtual bool handle(  osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter aa, osg.Object* pObject, osg.NodeVisitor* pNodeVisitor )
    pViewer =  dynamic_cast<osgViewer.Viewer*>(aa)
    if  !pViewer  :
      false = return()

    if  ea.getEventType()==osgGA.GUIEventAdapter.PUSH  :
      cams = osgViewer.ViewerBase.Cameras()
      pViewer.getCameras( cams )

      x =  ea.getXnormalized()
      y =  ea.getYnormalized()

      picker =  new osgUtil.LineSegmentIntersector( osgUtil.Intersector.PROJECTION, x, y )
      iv = osgUtil.IntersectionVisitor( picker )
      cams[0].accept( iv )

      if  picker.containsIntersections()  :
        intersection =  picker.getFirstIntersection()
        v =  intersection.getWorldIntersectPoint()
        m_rPatSphere.setPosition( v )

      true = return() # return true, event handled

    false = return()

private:
  osg.ref_ptr<osg.PositionAttitudeTransform> m_rPatSphere

#####################################
int main_test(int, char**)
    viewer = osgViewer.Viewer()
    viewer.setUpViewInWindow(99,99,666,666, 0)
    osg.ref_ptr<osg.PositionAttitudeTransform> rPat = new osg.PositionAttitudeTransform
    # add the handler to the viewer
    viewer.addEventHandler( new CInputHandler(rPat.get()) )
    # create a group to contain our scene and sphere
    pGroup =  new osg.Group
    # create sphere
    pGeodeSphere =  new osg.Geode
    pGeodeSphere.addDrawable( new osg.ShapeDrawable( new osg.Sphere(osg.Vec3(0.0f,0.0f,0.0f),0.01f) ) )
    rPat.addChild( pGeodeSphere )
    pGroup.addChild( rPat.get() )

    center = osg.Vec3(0.0f,0.0f,0.0f)
    radius =  1.0f

    root =  new osg.Group
    root.addChild(test_create3DText(center, radius))

    #viewer.setSceneData(root)
    pGroup.addChild(root)
    viewer.setSceneData(pGroup)
    viewer.setCameraManipulator(new osgGA.TrackballManipulator())
    viewer.addEventHandler( new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    viewer.addEventHandler(new osgViewer.ThreadingHandler)
    viewer.addEventHandler(new osgViewer.WindowSizeHandler)
    viewer.addEventHandler(new osgViewer.StatsHandler)

    return viewer.run()


# -*-c++-*- OpenSceneGraph - Copyright (C) 1998-2010 Robert Osfield
 *
 * This library is open source and may be redistributed and/or modified under
 * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or
 * (at your option) any later version.  The full license is in LICENSE file
 * included with this distribution, and on the openscenegraph.org website.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * OpenSceneGraph Public License for more details.


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

osg.ref_ptr<Layout> Layout.getDefaultLayout()
    static OpenThreads.Mutex s_DefaultLayoutMutex
    OpenThreads.ScopedLock<OpenThreads.Mutex> lock(s_DefaultLayoutMutex)

    static osg.ref_ptr<Layout> s_defaultLayout = new Layout
    s_defaultLayout = return()

void Layout.layout(TextNode text) 
    OSG_NOTICE, "Layout.layout"

    font =  text.getActiveFont()
    style =  text.getActiveStyle()
    technique =  text.getTextTechnique()
    str =  text.getText()

    if !text.getTextTechnique() :
        OSG_NOTICE, "Warning: no TextTechnique assigned to Layout"
        return

    pos = osg.Vec3(0.0f,0.0f,0.0f)
    characterSize =  text.getCharacterSize()
    size = osg.Vec3(characterSize, characterSize, 0.0)
    if style :
        size.y() = characterSize
        size.z() = characterSize


    resolution = osgText.FontResolution(32,32)
    if style :
        resolution.first = static_cast<unsigned int>(static_cast<float>(resolution.first)*style.getSampleDensity())
        resolution.second = static_cast<unsigned int>(static_cast<float>(resolution.second)*style.getSampleDensity())

    characterWidthScale =  1.0f

    textIs3D =  (style  style.getThicknessRatio()!=0.0)
    if !textIs3D :
        characterWidthScale = 1.0f/static_cast<float>(resolution.first)

    kerningType =  osgText.KERNING_DEFAULT

    technique.start()

    unsigned int previousCharcode = 0
    for(unsigned int i=0 i<str.size() ++i)
        unsigned int charcode = str[i]

        if size.z()==0.0f :
            glyph =  font.getGlyph(resolution, charcode)
            if glyph :
                technique.addCharacter(pos, size, glyph, style)
                pos += osg.Vec3(size.x()*(glyph.getHorizontalAdvance()*characterWidthScale), 0.0f ,0.0f)
        else:
            glyph =  font.getGlyph3D(charcode)
            OSG_NOTICE, "pos = ", pos, ", charcode=", charcode, ", glyph=", glyph
            if glyph :
                local_scale = osg.Vec3( size )
                technique.addCharacter(pos, local_scale, glyph, style)
                pos += osg.Vec3(size.x()*glyph.getWidth(), 0.0f ,0.0f)

        if previousCharcode!=0  charcode!=0 :
            offset =  font.getKerning(previousCharcode, charcode, kerningType)
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

osg.ref_ptr<TextTechnique> TextTechnique.getDefaultTextTechinque()
    static OpenThreads.Mutex s_DefaultTextTechniqueMutex
    OpenThreads.ScopedLock<OpenThreads.Mutex> lock(s_DefaultTextTechniqueMutex)

    static osg.ref_ptr<TextTechnique> s_defaultTextTechnique = new TextTechnique
    s_defaultTextTechnique = return()

void TextTechnique.start()
    OSG_NOTICE, "TextTechnique.start()"

void TextTechnique.addCharacter( osg.Vec3 position,  osg.Vec3 size, Glyph* glyph, Style* style)
    OSG_NOTICE, "TextTechnique.addCharacter 2D(", position, ", ", size, ", ", glyph, ", ", style, ")"

void TextTechnique.addCharacter( osg.Vec3 position,  osg.Vec3 size, Glyph3D* glyph, Style* style)
    OSG_NOTICE, "TextTechnique.addCharacter 3D(", position, ", ", size, ", ", glyph, ", ", style, ")"

    osg.ref_ptr<osg.PositionAttitudeTransform> transform = new osg.PositionAttitudeTransform
    transform.setPosition(position)
    transform.setAttitude(osg.Quat(osg.inDegrees(90.0),osg.Vec3d(1.0,0.0,0.0)))
    transform.setScale(size)

    osg.ref_ptr<osg.Geode> geode = new osg.Geode

    bevel =  style ? style.getBevel() : 0
    outline =  style ? style.getOutlineRatio()>0.0f : false
    width =  style.getThicknessRatio()
    creaseAngle =  30.0f
    smooth =  true

    if bevel :
        thickness =  bevel.getBevelThickness()

        osg.ref_ptr<osg.Geometry> glyphGeometry = osgText.computeGlyphGeometry(glyph, thickness, width)
        osg.ref_ptr<osg.Geometry> textGeometry = osgText.computeTextGeometry(glyphGeometry.get(), *bevel, width)
        osg.ref_ptr<osg.Geometry> shellGeometry = outline ? osgText.computeShellGeometry(glyphGeometry.get(), *bevel, width) : 0
        if textGeometry.valid() : geode.addDrawable(textGeometry.get())
        if shellGeometry.valid() : geode.addDrawable(shellGeometry.get())

        # create the normals
        if smooth  textGeometry.valid() :
            osgUtil.SmoothingVisitor.smooth(*textGeometry, osg.DegreesToRadians(creaseAngle))
    else:
        osg.ref_ptr<osg.Geometry> textGeometry = osgText.computeTextGeometry(glyph, width)
        if textGeometry.valid() : geode.addDrawable(textGeometry.get())

        # create the normals
        if smooth  textGeometry.valid() :
            osgUtil.SmoothingVisitor.smooth(*textGeometry, osg.DegreesToRadians(creaseAngle))

    transform.addChild(geode.get())

    _textNode.addChild(transform.get())

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
        _characterSize(1.0f)


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
        technique = new TextTechnique(*TextTechnique.getDefaultTextTechinque())

    _technique = technique

    if _technique.valid() : _technique.setTextNode(this)


void TextNode.update()
    getActiveLayout().layout(*this)

void TextNode.setText( str str)
    _string.set(str)
# -*-c++-*- OpenSceneGraph - Copyright (C) 1998-2010 Robert Osfield
 *
 * This library is open source and may be redistributed and/or modified under
 * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or
 * (at your option) any later version.  The full license is in LICENSE file
 * included with this distribution, and on the openscenegraph.org website.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * OpenSceneGraph Public License for more details.


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
    public:

        Layout()
        Layout( Layout layout,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY)

        META_Object(osgText,Layout)

        #/ default Layout implementation used if no other is specified on TextNode
        static osg.ref_ptr<Layout> getDefaultLayout()

        virtual void layout(TextNode text) 

    protected:


class #OSGTEXT_EXPORT TextTechnique : public osg.Object
    public:

        TextTechnique()
        TextTechnique( TextTechnique technique,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY)

        META_Object(osgText, TextTechnique)

        TextNode* getTextNode()  return _textNode 
         TextNode* getTextNode()   return _textNode 

        #/ default TextTechnique implementation used if no other is specified on TextNode
        static osg.ref_ptr<TextTechnique> getDefaultTextTechinque()

        #/ start building a new charater layout
        virtual void start()

        #/ called by Layout engine to place individual characters
        virtual void addCharacter( osg.Vec3 position,  osg.Vec3 size, Glyph* glyph, Style* style)

        #/ called by Layout engine to place individual characters
        virtual void addCharacter( osg.Vec3 position,  osg.Vec3 size, Glyph3D* glyph, Style* style)

        #/ finish building new charater layout
        virtual void finish()

        #/ provide traversal control
        virtual void traverse(osg.NodeVisitor nv)

    protected:

        friend class TextNode

        void setTextNode(TextNode* textNode)  _textNode = textNode 

        _textNode = TextNode*()


class #OSGTEXT_EXPORT TextNode : public osg.Group
    public:

        TextNode()
        TextNode( TextNode text,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY)

        META_Node(osgText, TextNode)

        virtual void traverse(osg.NodeVisitor nv)

        void setFont(Font* font)  _font = font 
        Font* getFont()  return _font.get() 
         Font* getFont()   return _font.get() 
        Font* getActiveFont()  return _font.valid() ? _font.get() : Font.getDefaultFont().get() 
         Font* getActiveFont()   return _font.valid() ? _font.get() : Font.getDefaultFont().get() 

        void setStyle(Style* style)  _style = style 
        Style* getStyle()  return _style.get() 
         Style* getStyle()   return _style.get() 
        Style* getActiveStyle()  return _style.valid() ? _style.get() : Style.getDefaultStyle().get() 
         Style* getActiveStyle()   return _style.valid() ? _style.get() : Style.getDefaultStyle().get() 

        void setLayout(Layout* layout)  _layout = layout 
        Layout* getLayout()  return _layout.get() 
         Layout* getLayout()   return _layout.get() 
         Layout* getActiveLayout()   return _layout.valid() ? _layout.get() : Layout.getDefaultLayout().get() 

        setTextTechnique = void(TextTechnique* technique)
        TextTechnique* getTextTechnique()  return _technique.get() 
         TextTechnique* getTextTechnique()   return _technique.get() 

        setText = void( str str)
        void setText( String str)  _string = str 
        String getText()  return _string 
         String getText()   return _string 

        void setPosition( osg.Vec3d position)  _position  = position 
         osg.Vec3d getPosition()   return _position 

        void setRotation( osg.Quat rotation)  _rotation  = rotation 
         osg.Quat getRotation()   return _rotation 

        void setCharacterSize(float characterSize)  _characterSize = characterSize 
        float getCharacterSize()   return _characterSize 

        #/ force a regeneration of the rendering backend required to represent the text.
        virtual void update()

    protected:

        virtual ~TextNode()

        osg.ref_ptr<Font>              _font
        osg.ref_ptr<Style>             _style
        osg.ref_ptr<Layout>            _layout
        osg.ref_ptr<TextTechnique>     _technique

        _string = String()
        _position = osg.Vec3d()
        _rotation = osg.Quat()
        _characterSize = float()



#endif


if __name__ == "__main__":
    main(sys.argv)
