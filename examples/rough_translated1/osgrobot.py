#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgrobot"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgViewer

# OpenSceneGraph example, osgrobot.cpp.
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
    The code below is to show how a heirarchy of objects can be made within a scenegraph.
    In other words, how there can be a parent/child relationship between objects such
    that when a parent is rotated or translated, the children move is respect to it's
    parent movement.  A robotic arm is used in this example because this is what I'm
    using OSG for.
 
    To rotate the joints use the following table to rotate each respective joint.
 
    joint    key        rotation
    1        q        + 1 degree
    1        a        - 1 degree
    2        w        + 1 degree
    2        s        - 1 degree
    3        e        + 1 degree
    3        d        - 1 degree
    4        r        + 1 degree
    4        f        - 1 degree
    5        t        + 1 degree
    5        g        - 1 degree
    6        y        + 1 degree
    6        h        - 1 degree
  
    In many robotics projects, the x and z axis are only used to define the positions
    of the joints of a robotic arm.  By not using the y-axis, the mathematics of
    inverse kinematics becomes easier (and in some cases possible).  All joint rotations
    are rotated about the z-axis.  If you toggle the variable 'showAxis' to true, an
    x (color red), y (color green), and z (color blue) axis will display.  Using the
    thumb of the right hand to point in the same direction of the z-axis, use the right
    hand rule to define a positive angle of rotation.
 
    The robotic arm in general follows the algorithm
    rotate about the x axis, translate along the x-axis, translate along the z axis,
    and then rotate about the z-axis. There is 1 exception in the method buildJoint3(...)
    where it was necessary to add a 'cheat' to get the joints to align properly.  In a
    real robotics project such as this, the tube (see buildTube2(...) method) would not
    be a part of the mathematics and thus, not have to be drawn and would not require
    the cheat.  To learn moue about positioning joints using only the x and z axis,
    web search 'Denavit-Hartenberg'.  wikipedia has comments at the URL...
    http:#en.wikipedia.org/wiki/Robotics_conventions#Denavit-Hartenberg_link_frame_convention_.28DH.29
 
    Lessons learned with osg...
    When starting this work I was very new to OSG.  When I first placed a cylinder
    in a scene and rotated the cylinder about the z and x axis, I noticed that the rotation
    is about the barycenter of the object for both axis.  I wanted a rotation about the z-axis
    to be along the length of the tube (which OSG gives for free -- not always true with
    all scenegraphs) while the rotation about the x and y axis about the
    beginning (or start position) of the tube.  Knowing what I know about barycenters
    I positioned the shape along the -height/2 (see example 1 below)
    -- believing the offset -height/2 would place the axis of rotation at the start of
    the tube.  I was certainly wrong about this and found out the equation needs to
    be height/2.
 
    ...
    example 1
    joint.addDrawable(new osg.ShapeDrawable(new osg.Capsule(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints))
    ...
    
 
 
    author: James Moliere
    date written: 10/12/2008


#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Material>
#include <osg/Texture2D>

#include <osgViewer/Viewer>
#include <iostream>
#include <osgDB/ReadFile>
#include <osg/Math>
#include <osg/Matrixd>
#include <osg/MatrixTransform>
#include <osg/Vec3d>
#include <iostream>
#include <osg/PositionAttitudeTransform>



jointAngle1 = float()
jointAngle2 = float()
jointAngle3 = float()
jointAngle4 = float()
jointAngle5 = float()
jointAngle6 = float()
EndEffector = float()

createAxis = void(osg.Transform* previousJoint)

joint1 = osg.MatrixTransform*()
joint2 = osg.MatrixTransform*()
joint3 = osg.MatrixTransform*()
joint4 = osg.MatrixTransform*()
joint5 = osg.MatrixTransform*()
joint6 = osg.MatrixTransform*()

buildJoint1 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildJoint2 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildTube2 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildJoint3 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildJoint4 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildTube5 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildJoint5 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildJoint6 = osg.MatrixTransform*(osg.MatrixTransform* previousJoint)
buildEndEffector = osg.MatrixTransform*()
hints =  new osg.TessellationHints

showAxis = bool()

class KeyboardEventHandler : public osgGA.GUIEventHandler
public:

    KeyboardEventHandler()
    


    static void rotate(float angle,osg.MatrixTransform *joint)
        zRot = osg.Matrix()
        zRot.makeRotate(angle, 0.0,0.0,1.0)
        joint.setMatrix(zRot*joint.getMatrix())

    virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
        switch (ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
                switch (ea.getKey())
                case 'q':
                    rotate(osg.PI/180, joint1) 
                    true = return()
                case 'a':
                    rotate(-osg.PI/180, joint1) 
                    true = return()
                case 'w':
                    rotate(osg.PI/180, joint2) 
                    true = return()
                case 's':
                    rotate(-osg.PI/180, joint2) 
                    true = return()
                case 'e':
                    rotate(osg.PI/180, joint3) 
                    true = return()
                case 'd':
                    rotate(-osg.PI/180, joint3) 
                    true = return()
                case 'r':
                    rotate(osg.PI/180, joint4) 
                    true = return()
                case 'f':
                    rotate(-osg.PI/180, joint4) 
                    true = return()
                case 't':
                    rotate(osg.PI/180, joint5) 
                    true = return()
                case 'g':
                    rotate(-osg.PI/180, joint5) 
                    true = return()
                case 'y':
                    rotate(osg.PI/180, joint6) 
                    true = return()
                case 'h':
                    rotate(-osg.PI/180, joint6) 
                    true = return()
        default:
            break

        #return false to allow mouse manipulation
        false = return()



def createShapes():
    group =  new osg.Group()
    transform = new osg.MatrixTransform()
    group.addChild(transform)

    joint1 = buildJoint1(transform)
    joint2 = buildJoint2(joint1)
    tube2 =  buildTube2(joint2)
    joint3 = buildJoint3(tube2)
    joint4 = buildJoint4(joint3)
    tube5 =  buildTube5(joint4)
    joint5 = buildJoint5(tube5)
    joint6= buildJoint6(joint5)
    joint6.addChild( buildEndEffector())
    group = return()

def buildJoint1(previousJoint):
    xTransform = new osg.MatrixTransform()
    previousJoint.addChild(xTransform)
    radius =  6.7640f
    height =  45.0f
    joint =  new osg.Geode()
    xTransform.addChild(joint)
    joint.addDrawable(new osg.ShapeDrawable(new osg.Cylinder(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints))

    zTransform =  new osg.MatrixTransform()
    xTransform.addChild(zTransform)
    zTrans = osg.Matrix.translate(0.0, 0.0, height)
    zRot =  osg.Matrix.rotate(jointAngle1, 0.0, 0.0, 1.0)
    zTransform.setMatrix(zTrans*zRot)
    zTransform = return()

def buildJoint2(previousJoint):
    if showAxis :
        createAxis(previousJoint)
    height =  17.6
    radius =  4.45633
    xTransform =  new osg.MatrixTransform()
    previousJoint.addChild(xTransform)
    xRot =  osg.Matrix.rotate(osg.PI_2, 1.0, 0.0, 0.0)
    xTransform.setMatrix(xRot)
    joint =  new osg.Geode()
    joint.addDrawable(new osg.ShapeDrawable(new osg.Capsule(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints))
    xTransform.addChild(joint)

    zTransform =  new osg.MatrixTransform()
    zTrans =  osg.Matrix.translate( 0.0, 0.0, height)
    zRot =  osg.Matrix.rotate(osg.PI_2+jointAngle2, 0.0,0.0,1.0)
    zTransform.setMatrix(zTrans*zRot)
    xTransform.addChild(zTransform)
    zTransform = return()

def buildTube2(previousJoint):
    if showAxis :
        createAxis(previousJoint)
    height =  17.6
    radius =  4.45633
    xTransform =  new osg.MatrixTransform()
    previousJoint.addChild(xTransform)
    xRot =  osg.Matrix.rotate(osg.PI_2, 1.0,0.0,0.0)
    xTransform.setMatrix(xRot)
    tube3 =  new osg.Geode()
    xTransform.addChild(tube3)
    tube3.addDrawable(new osg.ShapeDrawable(new osg.Capsule(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints))

    zTransform =  new osg.MatrixTransform()
    xTransform.addChild(zTransform)
    zTrans =  osg.Matrix.translate(0,0,height)
    zTransform.setMatrix(zTrans)
    zTransform = return()

def buildJoint3(previousJoint):
    height = 7.5
    radius =  4.45633
    joint =  new osg.Geode()
    xTransform =  new osg.MatrixTransform()
    previousJoint.addChild(xTransform)
    xRot =  osg.Matrix.rotate(-osg.PI_2, 1.0, 0.0, 0.0)
    xTransform.setMatrix(xRot)


    zCheat =  new osg.MatrixTransform()
    zTransCheat =  osg.Matrix.translate(0.0,0.0,-height)
    zCheat.setMatrix(zTransCheat)
    xTransform.addChild(zCheat)
    
    shape =  new osg.ShapeDrawable(new osg.Capsule(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints)
    joint.addDrawable(shape)
    zCheat.addChild(joint)

    zTransform =  new osg.MatrixTransform()
    zCheat.addChild(zTransform)
    zRot =  osg.Matrix.rotate((float)jointAngle3, 0.0f, 0.0f, 1.0f)
    zTrans =  osg.Matrix.translate(0,0,0)
    zTransform.setMatrix(zTrans*zRot)
    if showAxis :
        createAxis(zTransform)
    zTransform = return()
def buildJoint4(previousJoint):
    height =  17.5
    radius =  2.86479
    tube4 =  new osg.Geode()
    tube4.addDrawable(new osg.ShapeDrawable(new osg.Capsule(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints))
    xTransform =  new osg.MatrixTransform()
    #if showAxis :
    #
        #createAxis(xTransform)
    #
    previousJoint.addChild(xTransform)
    xTransform.addChild(tube4)
    xRot =  osg.Matrix.rotate(osg.PI_2, 1,0,0)
    xTransform.setMatrix(xRot)
    height = 7.5
    zTrans =  osg.Matrix.translate(0,0,17.5)
    zRot =  osg.Matrix.rotate(jointAngle4-osg.PI_2, 0,0,1)

    zTransform =  new osg.MatrixTransform()
    zTransform.setMatrix(zTrans*zRot)
    xTransform.addChild(zTransform)
    zTransform = return()


def buildTube5(previousJoint):
    if showAxis :
        createAxis(previousJoint)
    height =  7.5
    radius =  2.86479

    height = 15.0
    joint =  new osg.Geode()
    shape = new osg.ShapeDrawable(new osg.Cylinder(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints)
    joint.addDrawable(shape)
    xTransform =  new osg.MatrixTransform()
    previousJoint.addChild(xTransform)
    xTransform.addChild(joint)

    zTransform =  new osg.MatrixTransform()
    zTrans =  osg.Matrix.translate(0,0,height)
    zTransform.setMatrix(zTrans)
    xTransform.addChild(zTransform)
    zTransform = return()

def buildJoint5(previousJoint):
    radius =  2.86479
    height =  2.86479*2
    joint =  new osg.Geode()
    shape =  new osg.ShapeDrawable(new osg.Cylinder(osg.Vec3(0.0f,0.0f,0.0f),radius,height),hints)
    joint.addDrawable(shape)
    xTransform =  new osg.MatrixTransform()
    previousJoint.addChild(xTransform)
    xRot =  osg.Matrix.rotate(-osg.PI_2, 1.0,0,0)
    xTransform.setMatrix(xRot)
    xTransform.addChild(joint)
    if showAxis :
        createAxis(xTransform)

    zTransform =  new osg.MatrixTransform()
    zRot =  osg.Matrix.rotate(jointAngle5, 0,0,1)
    zTrans =  osg.Matrix.translate(0,0,0)
    zTransform.setMatrix(zTrans*zRot)
    xTransform.addChild(zTransform)
    zTransform = return()

def buildJoint6(previousJoint):
    height =  3.0
    radius =  1.0
    joint =  new osg.Geode()
    joint.addDrawable(new osg.ShapeDrawable(new osg.Cylinder(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints))
    xTransform =  new osg.MatrixTransform()
    xRot =  osg.Matrix.rotate(osg.PI_2, 1.0, 0.0, 0.0)
    xTransform.setMatrix(xRot)
    xTransform.addChild(joint)
    previousJoint.addChild(xTransform)
    if showAxis :
        createAxis(xTransform)
    xTransform = return()

def buildEndEffector():
    mt =  new osg.MatrixTransform()
    m = osg.Matrix()
    length =  17.0
    m.makeTranslate(0,0,length/2)
    mt.setMatrix(m)
    geode_3 =  new osg.Geode
    shape1 =  new osg.ShapeDrawable(new osg.Box(osg.Vec3(-EndEffector, 0.0f, 0.0f), .5, 1.5f, length), hints)
    shape2 =  new osg.ShapeDrawable(new osg.Box(osg.Vec3( EndEffector, 0.0f, 0.0f), .5, 1.5f, length), hints)
    shape1.setColor(osg.Vec4(0.8f, 0.8f, 0.4f, 1.0f))
    shape2.setColor(osg.Vec4(0.8f, 0.8f, 0.4f, 1.0f))
    geode_3.addDrawable(shape1)
    geode_3.addDrawable(shape2)
    mt.addChild(geode_3)
    mt = return()

def createAxis(previousJoint):
    height =  12.0
    radius =  .5

    zmt =  new osg.MatrixTransform()

    previousJoint.addChild(zmt)
    zShape =  new osg.ShapeDrawable(new osg.Cylinder(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints)
    zCone =  new osg.ShapeDrawable(new osg.Cone(osg.Vec3(0.0f,0.0f,1.0),radius+1.0,2.0),hints)

    zmtCone =  new osg.MatrixTransform()
    zgCone =  new osg.Geode

    zmtCone.setMatrix( osg.Matrix.translate(0.0,0.0,height))
    previousJoint.addChild(zmtCone)

    zShape.setColor(osg.Vec4(0.0f, 0.0f, 1.0f, 1.0f))
    zCone.setColor(osg.Vec4(0.0f, 0.0f, 1.0f, 1.0f))
    z =  new osg.Geode
    z.addDrawable(zShape)
    zgCone.addDrawable(zCone)
    zmtCone.addChild(zgCone)
    zmt.addChild(z)

    mt =  new osg.MatrixTransform()
    previousJoint.addChild(mt)

    xMatrix =  osg.Matrix.rotate(-osg.PI_2, 0.0, 1.0, 0.0)
    mt.setMatrix(xMatrix)


    xShape =  new osg.ShapeDrawable(new osg.Cylinder(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints)
    xShape.setColor(osg.Vec4(1.0f, 0.0f, 0.0f, 1.0f))
    x =  new osg.Geode
    x.addDrawable(xShape)
    mt.addChild(x)


    yMt =  new osg.MatrixTransform()
    previousJoint.addChild(yMt)
    yMatrix =  osg.Matrix.rotate(osg.PI_2, 1.0, 0.0, 0.0)
    yMt.setMatrix(yMatrix)

    yShape =  new osg.ShapeDrawable(new osg.Cylinder(osg.Vec3(0.0f,0.0f,height/2),radius,height),hints)
    yShape.setColor(osg.Vec4(0.0f, 1.0f, 0.0f, 1.0f))
    y =  new osg.Geode
    y.addDrawable(yShape)
    yMt.addChild(y)

int main(int, char **)
    hints.setDetailRatio(0.5f)
    showAxis = true
    jointAngle1=0.0
    jointAngle2=0.0
    jointAngle3=0.0
    jointAngle4=0.0
    jointAngle5=0.0
    jointAngle6=0.0
    EndEffector=1.0
    viewer = osgViewer.Viewer()
    viewer.addEventHandler(new KeyboardEventHandler())

    # add model to viewer.
    viewer.setSceneData( createShapes() )
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
