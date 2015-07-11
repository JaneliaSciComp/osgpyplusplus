#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osglogo"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osglogo.cpp'

# OpenSceneGraph example, osglogo.
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
#include <osg/Geometry>
#include <osg/MatrixTransform>
#include <osg/PositionAttitudeTransform>
#include <osg/BlendFunc>
#include <osg/ClearNode>
#include <osg/Version>

#include <osgUtil/Tessellator>
#include <osgUtil/CullVisitor>

#include <osgText/Text>

#include <osgGA/TrackballManipulator>

#include <osgViewer/Viewer>

#include <osgDB/ReadFile>

#include <iostream>

class MyBillboardTransform (osg.PositionAttitudeTransform) :

        MyBillboardTransform():
            _axis(0.0,0.0,1.0),
            _normal(0.0,-1.0,0.0)

        def computeLocalToWorldMatrix(matrix, nv):

            
            billboardRotation = osg.Quat()
            cullvisitor = dynamic_cast<osgUtil.CullVisitor*>(nv)
            if cullvisitor :
                eyevector = cullvisitor.getEyeLocal()-_position
                eyevector.normalize()

                side = _axis^_normal
                side.normalize()

                angle = atan2(eyevector*_normal,eyevector*side)
                billboardRotation.makeRotate(osg.PI_2-angle,_axis)


            matrix.preMultTranslate(_position)
            matrix.preMultRotate(billboardRotation)
            matrix.preMultRotate(_attitude)
            matrix.preMultTranslate(-_pivotPoint)
            return True



        def setAxis(axis):



             _axis = axis 

        def setNormal(normal):

             _normal = normal 

        virtual ~MyBillboardTransform() 

        _axis = osg.Vec3()
        _normal = osg.Vec3()



def createWing(left, nose, right, chordRatio, color):


    
    geom = osg.Geometry()

    normal = (nose-right)^(left-nose)
    normal.normalize()

    left_to_right = right-left
    mid = (right+left)*0.5
    mid_to_nose = (nose-mid)*chordRatio*0.5

    vertices = osg.Vec3Array()
    vertices.push_back(left)
    #vertices.push_back(mid+mid_to_nose)

    noSteps = 40
    for(unsigned int i=1i<noSteps++i)
        ratio = (float)i/(float)noSteps
        vertices.push_back(left + left_to_right*ratio + mid_to_nose* (cosf((ratio-0.5)*osg.PI*2.0)+1.0))

    vertices.push_back(right)
    vertices.push_back(nose)

    geom.setVertexArray(vertices)


    normals = osg.Vec3Array()
    normals.push_back(normal)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)


    colors = osg.Vec4Array()
    colors.push_back(color)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)


    geom.addPrimitiveSet(osg.DrawArrays(GL_POLYGON,0,vertices.getNumElements()))

    tessellator = osgUtil.Tessellator()
    tessellator.retessellatePolygons(*geom)

    return geom


osg. Node* createTextBelow( osg.BoundingBox bb,  str label,  str)
    geode = osg.Geode()

    font = str("fonts/arial.ttf")

    text = osgText.Text()

    text.setFont(font)
    text.setFontResolution(64,64)
    text.setAlignment(osgText.Text.CENTER_CENTER)
    text.setAxisAlignment(osgText.Text.XZ_PLANE)
    text.setPosition(bb.center()-osg.Vec3(0.0,0.0,(bb.zMax()-bb.zMin())))
    text.setColor(osg.Vec4(0.37,0.48,0.67,1.0))
    text.setText(label)

    geode.addDrawable( text )

    return geode

osg. Node* createTextLeft( osg.BoundingBox bb,  str label,  str subscript)
    geode = osg.Geode()


    stateset = geode.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)


    #str font("fonts/times.ttf")
    font = str("fonts/arial.ttf")

    text = osgText.Text()

    text.setFont(font)
    text.setFontResolution(110,120)
    text.setAlignment(osgText.Text.RIGHT_CENTER)
    text.setAxisAlignment(osgText.Text.XZ_PLANE)
    text.setCharacterSize((bb.zMax()-bb.zMin())*1.0)
    text.setPosition(bb.center()-osg.Vec3((bb.xMax()-bb.xMin()),-(bb.yMax()-bb.yMin())*0.5,(bb.zMax()-bb.zMin())*0.1))
    #text.setColor(osg.Vec4(0.37,0.48,0.67,1.0)) # Neil's original OSG colour
    text.setColor(osg.Vec4(0.20,0.45,0.60,1.0)) # OGL logo colour
    text.setText(label)

#if 1
    text.setBackdropType(osgText.Text.OUTLINE)
#   text.setBackdropType(osgText.Text.DROP_SHADOW_BOTTOM_RIGHT)

    text.setBackdropImplementation(osgText.Text.POLYGON_OFFSET)
#    text.setBackdropImplementation(osgText.Text.NO_DEPTH_BUFFER)
#    text.setBackdropImplementation(osgText.Text.DEPTH_RANGE)
#    text.setBackdropImplementation(osgText.Text.STENCIL_BUFFER)

    text.setBackdropOffset(0.05)
    text.setBackdropColor(osg.Vec4(0.0, 0.0, 0.5, 1.0))
#endif


#if 1
    text.setColorGradientMode(osgText.Text.OVERALL)
    lightblue = osg.Vec4(0.30,0.6,0.90,1.0)
    blue = osg.Vec4(0.10,0.30,0.40,1.0)
    text.setColorGradientCorners(lightblue, blue, blue, lightblue)
#else :
    text.setColorGradientMode(osgText.Text.OVERALL)
    light = osg.Vec4(0.0, 1.0, 1.0, 1.0)
    dark = osg.Vec4(0.0, 0.0, 0.5, 1.0)
    text.setColorGradientCorners(light, dark, dark, light)
#    text.setColorGradientCorners(dark, light, light, dark)
#endif

    geode.addDrawable( text )


    if !subscript.empty() :
        #osgText.Text* subscript = osgText.Text(osgText.TextureFont(font,45))

        subscriptText = osgText.Text()
        subscriptText.setFont(font)
        subscriptText.setText(subscript)
        subscriptText.setAlignment(osgText.Text.RIGHT_CENTER)
        subscriptText.setAxisAlignment(osgText.Text.XZ_PLANE)
        subscriptText.setPosition(bb.center()-osg.Vec3((bb.xMax()-bb.xMin())*4.3,-(bb.yMax()-bb.yMin())*0.5,(bb.zMax()-bb.zMin())*0.6))
        subscriptText.setColor(osg.Vec4(0.0,0.0,0.0,1.0)) # black

        geode.addDrawable( subscriptText )

    return geode

osg. Node* createGlobe( osg.BoundingBox bb,float ratio,  str filename)
    xform = osg.MatrixTransform()
    xform.setUpdateCallback(osg.AnimationPathCallback(bb.center(),osg.Vec3(0.0,0.0,1.0),osg.inDegrees(10.0)))

    bluemarble = filename.empty() ? 0 : osgDB.readNodeFile(filename.c_str())
    if bluemarble :
        bs = bluemarble.getBound()
        s = 1.2*bb.radius()/bs.radius()
        positioner = osg.MatrixTransform()
        positioner.setMatrix(osg.Matrix.translate(-bs.center())*osg.Matrix.scale(s,s,s)*osg.Matrix.translate(bb.center()))
        positioner.addChild(bluemarble)

        xform.addChild(positioner)
    else :

        geode = osg.Geode()

        stateset = geode.getOrCreateStateSet()

        image = osgDB.readImageFile("Images/land_shallow_topo_2048.jpg")
        if image :
            texture = osg.Texture2D()
            texture.setImage(image)
            texture.setMaxAnisotropy(8)
            stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

        material = osg.Material()
        stateset.setAttribute(material)

        # the globe
        geode.addDrawable(osg.ShapeDrawable(osg.Sphere(bb.center(),bb.radius()*ratio)))

        xform.addChild(geode)

    return xform

osg. Node* createBox( osg.BoundingBox bb,float chordRatio)
    geode = osg.Geode()

    white = osg.Vec4(1.0,1.0,1.0,1.0)

    # front faces.
    geode.addDrawable(createWing(bb.corner(4),bb.corner(6),bb.corner(7),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(7),bb.corner(5),bb.corner(4),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(4),bb.corner(5),bb.corner(1),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(1),bb.corner(0),bb.corner(4),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(1),bb.corner(5),bb.corner(7),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(7),bb.corner(3),bb.corner(1),chordRatio,white))

    # back faces
    geode.addDrawable(createWing(bb.corner(2),bb.corner(0),bb.corner(1),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(1),bb.corner(3),bb.corner(2),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(2),bb.corner(3),bb.corner(7),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(7),bb.corner(6),bb.corner(2),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(2),bb.corner(6),bb.corner(4),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(4),bb.corner(0),bb.corner(2),chordRatio,white))

    return geode

osg. Node* createBoxNo5( osg.BoundingBox bb,float chordRatio)
    geode = osg.Geode()

    white = osg.Vec4(1.0,1.0,1.0,1.0)

    # front faces.
    geode.addDrawable(createWing(bb.corner(4),bb.corner(6),bb.corner(7),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(1),bb.corner(0),bb.corner(4),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(7),bb.corner(3),bb.corner(1),chordRatio,white))

    # back faces
    geode.addDrawable(createWing(bb.corner(2),bb.corner(0),bb.corner(1),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(1),bb.corner(3),bb.corner(2),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(2),bb.corner(3),bb.corner(7),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(7),bb.corner(6),bb.corner(2),chordRatio,white))

    geode.addDrawable(createWing(bb.corner(2),bb.corner(6),bb.corner(4),chordRatio,white))
    geode.addDrawable(createWing(bb.corner(4),bb.corner(0),bb.corner(2),chordRatio,white))

    return geode

osg. Node* createBoxNo5No2( osg.BoundingBox bb,float chordRatio)
    geode = osg.Geode()

#    osg.Vec4 red(1.0,0.0,0.0,1.0)
#    osg.Vec4 green(0.0,1.0,0.0,1.0)
#    osg.Vec4 blue(0.0,0.0,1.0,1.0)

    red = osg.Vec4(1.0,0.12,0.06,1.0)
    green = osg.Vec4(0.21,0.48,0.03,1.0)
    blue = osg.Vec4(0.20,0.45,0.60,1.0)

    # front faces.
    geode.addDrawable(createWing(bb.corner(4),bb.corner(6),bb.corner(7),chordRatio,red))

    geode.addDrawable(createWing(bb.corner(1),bb.corner(0),bb.corner(4),chordRatio,green))

    geode.addDrawable(createWing(bb.corner(7),bb.corner(3),bb.corner(1),chordRatio,blue))

    return geode

osg. Node* createBackdrop( osg.Vec3 corner, osg.Vec3 top, osg.Vec3 right)



    geom = osg.Geometry()

    normal = (corner-top)^(right-corner)
    normal.normalize()

    vertices = osg.Vec3Array()
    vertices.push_back(top)
    vertices.push_back(corner)

    vertices.push_back(right)
    vertices.push_back(right+(top-corner))

    geom.setVertexArray(vertices)

    normals = osg.Vec3Array()
    normals.push_back(normal)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

    colors = osg.Vec4Array()
    colors.push_back(osg.Vec4(1.0,1.0,1.0,1.0))
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(osg.DrawArrays(GL_QUADS,0,vertices.getNumElements()))

    geode = osg.Geode()
    geode.addDrawable(geom)

    return geode

def createLogo(filename, label, subscript):

    
    bb = osg.BoundingBox(osg.Vec3(0.0,0.0,0.0),osg.Vec3(100.0,100.0,100.0))
    chordRatio = 0.5
    sphereRatio = 0.6

    # create a group to hold the whole model.
    logo_group = osg.Group()

    osg.Quat r1,r2
    r1.makeRotate(-osg.inDegrees(45.0),0.0,0.0,1.0)
    r2.makeRotate(osg.inDegrees(45.0),1.0,0.0,0.0)


    xform = MyBillboardTransform()
    xform.setPivotPoint(bb.center())
    xform.setPosition(bb.center())
    xform.setAttitude(r1*r2)


#     # create a transform to orientate the box and globe.
#     osg.MatrixTransform* xform = osg.MatrixTransform()
#     xform.setDataVariance(osg.Object.STATIC)
#     xform.setMatrix(osg.Matrix.translate(-bb.center())*
#                      osg.Matrix.rotate(-osg.inDegrees(45.0),0.0,0.0,1.0)*
#                      osg.Matrix.rotate(osg.inDegrees(45.0),1.0,0.0,0.0)*
#                      osg.Matrix.translate(bb.center()))

    # add the box and globe to it.
    #xform.addChild(createBox(bb,chordRatio))
    #xform.addChild(createBoxNo5(bb,chordRatio))
    xform.addChild(createBoxNo5No2(bb,chordRatio))
    # add the transform to the group.
    logo_group.addChild(xform)

    logo_group.addChild(createGlobe(bb,sphereRatio,filename))

    # add the text to the group.
    #group.addChild(createTextBelow(bb))
    logo_group.addChild(createTextLeft(bb, label, subscript))


    # create the backdrop to render the shadow to.
    corner = osg.Vec3(-900.0,150.0,-100.0)
    top = osg.Vec3(0.0,0.0,300.0) top += corner
    right = osg.Vec3(1100.0,0.0,0.0) right += corner


#     osg.Group* backdrop = osg.Group()
#     backdrop.addChild(createBackdrop(corner,top,right))

    backdrop = osg.ClearNode()
    backdrop.setClearColor(osg.Vec4(1.0,1.0,1.0,0.0))

    #osg.Vec3 lightPosition(-500.0,-2500.0,500.0)
    #osg.Node* scene = createShadowedScene(logo_group,backdrop,lightPosition,0.0,0)

    scene = osg.Group()

    stateset = scene.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE|osg.StateAttribute.OFF)


    scene.addChild(logo_group)
    scene.addChild(backdrop)

    return scene

def main(argc, argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    osg.DisplaySettings.instance().setMinimumNumAlphaBits(8)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    label = "OpenSceneGraph"
    subscript = ""

    showVersion = False
    while arguments.read("--version") :  showVersion = True 
    if  showVersion  :
        label += " "
        label += osgGetVersion()

    while arguments.read("--label", label) : 
    while arguments.read("--subscript", subscript) : 

    node = osg.Node()

    if arguments.argc()>1 : node = createLogo(arguments[1], label, subscript)
    node = createLogo("", label, subscript)

    # add model to viewer.
    viewer.setSceneData( node.get() )

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
