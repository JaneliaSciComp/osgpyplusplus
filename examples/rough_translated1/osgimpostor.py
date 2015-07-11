#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgimpostor"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgSim
from osgpypp import osgViewer

# OpenSceneGraph example, osgimpostor.
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


#include <osg/Geometry>
#include <osg/Material>
#include <osg/MatrixTransform>
#include <osg/Quat>
#include <osg/Geode>

#include <osgSim/Impostor>
#include <osgSim/InsertImpostorsVisitor>

#include <osgDB/ReadFile>

#include <osgViewer/Viewer>

#include "TestManipulator.h"


#include <iostream>
#include <list>

# container storing all house nodes
typedef osg.ref_ptr<osg.Node>    NodePtr
typedef std.list<NodePtr>        NodeContainer
typedef NodeContainer.iterator    NodeIterator

nodes = NodeContainer()

#
osg.ref_ptr<osg.Group> Root = 0

HOUSES_SIZE =  25000        # total number of houses
XDim =  5000.0f                # area dimension +/- XDim
ZDim =  5000.0f                # area dimension +/- YDim

GridX =  20                        # number of grids in x direction
GridY =  20                        # number of grids in y direction

UseImpostor =  true            # use impostor (or do not use)

Threshold =  3000.0f            # distance where impostor are shown

# create houses and store nodes in container
def CreateHouses():
    i = int()

    GLubyte indices[48] = 
        0, 2, 1,
        3, 2, 0,
        0, 4, 7,
        7, 3, 0,
        0, 1, 5,
        5, 4, 0,
        1, 6, 5,
        2, 6, 1,
        2, 3, 7,
        2, 7, 6,
        4, 8, 7,
        5, 6, 9,
        4, 5, 8,
        8, 5, 9,
        6, 7, 8,
        8, 9, 6
    

    # use the same color, normal and indices for all houses.
    osg.ref_ptr<osg.Vec4Array> colors = new osg.Vec4Array(1)
    (*colors)[0] = osg.Vec4(1.0f, 1.0f, 1.0f, 1.0f)

    # normals
    osg.ref_ptr<osg.Vec3Array> normals = new osg.Vec3Array(16)
    (*normals)[0] = osg.Vec3( 0.0f,  -0.0f, -1.0f)
    (*normals)[1] = osg.Vec3( 0.0f,  -0.0f, -1.0f)
    (*normals)[2] = osg.Vec3( 0.0f,  -1.0f,  0.0f)
    (*normals)[3] = osg.Vec3( 0.0f,  -1.0f,  0.0f)
    (*normals)[4] = osg.Vec3( 1.0f,  -0.0f,  0.0f)
    (*normals)[5] = osg.Vec3( 1.0f,  -0.0f,  0.0f)
    (*normals)[6] = osg.Vec3( 0.0f, 1.0f,  0.0f)
    (*normals)[7] = osg.Vec3( 0.0f, 1.0f,  0.0f)
    (*normals)[8] = osg.Vec3(-1.0f,  -0.0f,  0.0f)
    (*normals)[9] = osg.Vec3(-1.0f,  -0.0f,  0.0f)
    (*normals)[10] = osg.Vec3( 0.0f,  -0.928477f, 0.371391f)
    (*normals)[11] = osg.Vec3( 0.0f, 0.928477f, 0.371391f)
    (*normals)[12] = osg.Vec3( 0.707107f,  0.0f, 0.707107f)
    (*normals)[13] = osg.Vec3( 0.707107f,  0.0f, 0.707107f)
    (*normals)[14] = osg.Vec3(-0.707107f,  0.0f, 0.707107f)
    (*normals)[15] = osg.Vec3(-0.707107f,  0.0f, 0.707107f)

    # coordIndices
    osg.ref_ptr<osg.UByteArray> coordIndices = new osg.UByteArray(48,indices)

    # share the primitive set.
    primitives =  new osg.DrawArrays(osg.PrimitiveSet.TRIANGLES,0,48)

    for (int q = 0 q < HOUSES_SIZE q++)
        xPos =  ((static_cast<double> (rand()) /
                      static_cast<double> (RAND_MAX))
                     * 2.0 * XDim) - XDim

        yPos =  ((static_cast<double> (rand()) /
                      static_cast<double> (RAND_MAX))
                     * 2 * ZDim) - ZDim

        scale =  10.0f

        offset = osg.Vec3(xPos,yPos,0.0f)

        # coords
        osg.ref_ptr<osg.Vec3Array> coords = new osg.Vec3Array(10)
        (*coords)[0] = osg.Vec3( 0.5f, -0.7f, 0.0f)
        (*coords)[1] = osg.Vec3( 0.5f,  0.7f, 0.0f)
        (*coords)[2] = osg.Vec3(-0.5f, 0.7f, 0.0f)
        (*coords)[3] = osg.Vec3(-0.5f, -0.7f, 0.0f)
        (*coords)[4] = osg.Vec3( 0.5f, -0.7f, 1.0f)
        (*coords)[5] = osg.Vec3( 0.5f,  0.7f, 1.0f)
        (*coords)[6] = osg.Vec3(-0.5f,  0.7f, 1.0f)
        (*coords)[7] = osg.Vec3(-0.5f, -0.7f, 1.0f)
        (*coords)[8] = osg.Vec3( 0.0f, -0.5f, 1.5f)
        (*coords)[9] = osg.Vec3( 0.0f,  0.5f, 1.5f)

        for (i = 0 i < 10 i++)
            (*coords)[i] = (*coords)[i] * scale + offset


        # create geometry
        osg.ref_ptr<deprecated_osg.Geometry> geometry = new deprecated_osg.Geometry()

        geometry.addPrimitiveSet(primitives)

        geometry.setVertexArray(coords.get())
        geometry.setVertexIndices(coordIndices.get())

        geometry.setColorArray(colors.get())
        geometry.setColorBinding(deprecated_osg.Geometry.BIND_OVERALL)

        geometry.setNormalArray(normals.get())
        geometry.setNormalBinding(deprecated_osg.Geometry.BIND_PER_PRIMITIVE)

        osg.ref_ptr<osg.Geode> geode = new osg.Geode()
        geode.addDrawable(geometry.get())

        nodes.push_back(geode.get())

def LayoutAsGrid():
    # calculate bounding box
    bbox = osg.BoundingBox()
    for (NodeIterator node = nodes.begin() node != nodes.end() ++node)
        bbox.expandBy((*node).getBound())

    # setup grid information
    groups =  new osg.Group*[GridX * GridY]
        i = int()
    for (i = 0 i < GridX * GridY i++)
        groups[i] = new osg.Group()

    xGridStart =  bbox.xMin()
    xGridSize =  (bbox.xMax() - bbox.xMin()) / GridX

    yGridStart =  bbox.yMin()
    yGridSize =  (bbox.yMax() - bbox.yMin()) / GridY

    # arrange buildings into right grid
    for (NodeIterator nodeIter = nodes.begin() nodeIter != nodes.end() ++nodeIter)
        node =  nodeIter.get()
        center =  node.getBound().center()

        x =  (int)floor((center.x() - xGridStart) / xGridSize)
        z =  (int)floor((center.y() - yGridStart) / yGridSize)

        groups[z * GridX + x].addChild(node)

    # add nodes to building root
    for (i = 0 i < GridX * GridY i++)
        stateset =  new osg.StateSet()

        material =  new osg.Material()
        color =  osg.Vec4(
            0.5f + (static_cast<double> (rand()) / (2.0*static_cast<double> (RAND_MAX))),
            0.5f + (static_cast<double> (rand()) / (2.0*static_cast<double> (RAND_MAX))),
            0.5f + (static_cast<double> (rand()) / ( 2.0*static_cast<double>(RAND_MAX))),
            1.0f)

        material.setAmbient(osg.Material.FRONT_AND_BACK, color)
        material.setDiffuse(osg.Material.FRONT_AND_BACK, color)
        stateset.setAttributeAndModes(material, osg.StateAttribute.ON)

        groups[i].setStateSet(stateset)

        if UseImpostor :
            impostor =  new osgSim.Impostor()
            impostor.setImpostorThreshold(static_cast<float> (Threshold))
            impostor.addChild(groups[i])
            impostor.setRange(0, 0.0f, 1e7f)
            impostor.setCenter(groups[i].getBound().center())
            Root.addChild(impostor)
        else:
            Root.addChild(groups[i])

    delete[] groups


def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # add local test manipulator more suitable for testing impostors.
    viewer.setCameraManipulator(new TestManipulator)


    # load the nodes from the commandline arguments.
    osg.ref_ptr<osg.Node> model = osgDB.readNodeFiles(arguments)
    if model :
        # the osgSim.InsertImpostorsVisitor used lower down to insert impostors
        # only operators on subclass of Group's, if the model top node is not
        # a group then it won't be able to insert an impostor.  We therefore
        # manually insert an impostor above the model.
        if dynamic_cast<osg.Group*>(model.get())==0 :
            bs =  model.getBound()
            if bs.valid() :

                impostor =  new osgSim.Impostor

                # standard LOD settings
                impostor.addChild(model.get())
                impostor.setRange(0,0.0f,1e7f)
                impostor.setCenter(bs.center())

                # impostor specfic settings.
                impostor.setImpostorThresholdToBound(5.0f)

                model = impostor


        # we insert an impostor node above the model, so we keep a handle
        # on the rootnode of the model, the is required since the
        # InsertImpostorsVisitor can add a new root in automatically and
        # we would know about it, other than by following the parent path
        # up from model.  This is really what should be done, but I'll pass
        # on it right now as it requires a getRoots() method to be added to
        # osg.Node, and we're about to make a release so no new features!
        osg.ref_ptr<osg.Group> rootnode = new osg.Group
        rootnode.addChild(model.get())


        # now insert impostors in the model using the InsertImpostorsVisitor.
        ov = osgSim.InsertImpostorsVisitor()

        # traverse the model and collect all osg.Group's and osg.LOD's.
        # however, don't traverse the rootnode since we want to keep it as
        # the start of traversal, otherwise the insertImpostor could insert
        # and Impostor above the current root, making it nolonger a root!
        model.accept(ov)

        # insert the Impostors above groups and LOD's
        ov.insertImpostors()
    else:
        # no user model so we'll create our own world.
        model = Root = new osg.Group()
        CreateHouses()
        LayoutAsGrid()

    # add model to viewer.
    viewer.setSceneData(model.get())

    return viewer.run()
# OpenSceneGraph example, osgimpostor.
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


#include "TestManipulator.h"
#include <osg/Notify>

using namespace osg
using namespace osgGA

TestManipulator.TestManipulator()
    _modelScale = 0.01f
    _minimumZoomScale = 0.05f
    _thrown = false

    _distance = 1.0f


TestManipulator.~TestManipulator()


void TestManipulator.setNode(osg.Node* node)
    _node = node
    if _node.get() :
        boundingSphere = _node.getBound()
        _modelScale = boundingSphere._radius


 osg.Node* TestManipulator.getNode() 
    return _node.get()


osg.Node* TestManipulator.getNode()
    return _node.get()


                                 #ea
void TestManipulator.home( GUIEventAdapter ,GUIActionAdapter us)
    if _node.get() :

        boundingSphere = _node.getBound()

        computePosition(boundingSphere.center()+osg.Vec3(0.0f, 0.0f, 20.0f),
                        osg.Vec3(0.0f, 1.0f, 0.0f),
                        osg.Vec3(0.0f,  0.0f,  1.0f))

        us.requestRedraw()


void TestManipulator.init( GUIEventAdapter ,GUIActionAdapter )
    flushMouseEventStack()

bool TestManipulator.handle( GUIEventAdapter ea,GUIActionAdapter us)
    switch(ea.getEventType())
        case(GUIEventAdapter.PUSH):
            flushMouseEventStack()
            addMouseEvent(ea)
            if calcMovement() : us.requestRedraw()
            us.requestContinuousUpdate(false)
            _thrown = false
            true = return()

        case(GUIEventAdapter.RELEASE):
            if ea.getButtonMask()==0 :

                if isMouseMoving() :
                    if calcMovement() :
                        us.requestRedraw()
                        us.requestContinuousUpdate(true)
                        _thrown = true
                else:
                    flushMouseEventStack()
                    addMouseEvent(ea)
                    if calcMovement() : us.requestRedraw()
                    us.requestContinuousUpdate(false)
                    _thrown = false

            else:
                flushMouseEventStack()
                addMouseEvent(ea)
                if calcMovement() : us.requestRedraw()
                us.requestContinuousUpdate(false)
                _thrown = false
            true = return()

        case(GUIEventAdapter.DRAG):
            addMouseEvent(ea)
            if calcMovement() : us.requestRedraw()
            us.requestContinuousUpdate(false)
            _thrown = false
            true = return()

        case(GUIEventAdapter.MOVE):
            false = return()

        case(GUIEventAdapter.KEYDOWN):
            if ea.getKey()==' ' :
                flushMouseEventStack()
                _thrown = false
                home(ea,us)
                us.requestRedraw()
                us.requestContinuousUpdate(false)
                true = return()
            false = return()
        case(GUIEventAdapter.FRAME):
            if _thrown :
                if calcMovement() : us.requestRedraw()
                true = return()
            false = return()
        default:
            false = return()


bool TestManipulator.isMouseMoving()
    if _ga_t0.get()==NULL || _ga_t1.get()==NULL : return false

    static  float velocity = 0.1f

    dx =  _ga_t0.getXnormalized()-_ga_t1.getXnormalized()
    dy =  _ga_t0.getYnormalized()-_ga_t1.getYnormalized()
    len =  sqrtf(dx*dx+dy*dy)
    dt =  _ga_t0.getTime()-_ga_t1.getTime()

    return (len>dt*velocity)


void TestManipulator.flushMouseEventStack()
    _ga_t1 = NULL
    _ga_t0 = NULL


void TestManipulator.addMouseEvent( GUIEventAdapter ea)
    _ga_t1 = _ga_t0
    _ga_t0 = ea

void TestManipulator.setByMatrix( osg.Matrixd matrix)
    _center = matrix.getTrans()
    _rotation = matrix.getRotate()
    _distance = 1.0f

osg.Matrixd TestManipulator.getMatrix() 
    return osg.Matrixd.rotate(_rotation)*osg.Matrixd.translate(_center)

osg.Matrixd TestManipulator.getInverseMatrix() 
    return osg.Matrixd.translate(-_center)*osg.Matrixd.rotate(_rotation.inverse())

void TestManipulator.computePosition( osg.Vec3 eye, osg.Vec3 lv, osg.Vec3 up)
    f = osg.Vec3(lv)
    f.normalize()
    s = osg.Vec3(f^up)
    s.normalize()
    u = osg.Vec3(s^f)
    u.normalize()
    
    rotation_matrix = osg.Matrixd(s[0],     u[0],     -f[0],     0.0f,
                                s[1],     u[1],     -f[1],     0.0f,
                                s[2],     u[2],     -f[2],     0.0f,
                                0.0f,     0.0f,     0.0f,      1.0f)
                   
    _center = eye+lv
    _distance = lv.length()
    _rotation = rotation_matrix.getRotate().inverse()


bool TestManipulator.calcMovement()

    # return if less then two events have been added.
    if _ga_t0.get()==NULL || _ga_t1.get()==NULL : return false

    dx =  _ga_t0.getXnormalized()-_ga_t1.getXnormalized()
    dy =  _ga_t0.getYnormalized()-_ga_t1.getYnormalized()


    # return if there is no movement.
    if dx==0  dy==0 : return false

    unsigned int buttonMask = _ga_t1.getButtonMask()
    if buttonMask==GUIEventAdapter.LEFT_MOUSE_BUTTON :

        # rotate camera.

        new_rotate = osg.Quat()
        new_rotate.makeRotate(dx / 3.0f, osg.Vec3(0.0f, 0.0f, 1.0f))
        
        _rotation = _rotation*new_rotate

        true = return()

    else: if buttonMask==GUIEventAdapter.MIDDLE_MOUSE_BUTTON :

        # pan model.

        dv =  osg.Vec3(0.0f, 0.0f, -500.0f) * dy

        _center += dv
        
        true = return()

    else: if buttonMask==GUIEventAdapter.RIGHT_MOUSE_BUTTON :
        rotation_matrix = osg.Matrixd(_rotation)
    
                        
        uv =  osg.Vec3(0.0f,1.0f,0.0f)*rotation_matrix
        sv =  osg.Vec3(1.0f,0.0f,0.0f)*rotation_matrix
        fv =  uv ^ sv
        dv =  fv*(dy*-500.0f)-sv*(dx*500.0f)

        _center += dv

        true = return()

    false = return()
# -*-c++-*- 
*
*  OpenSceneGraph example, osgimpostor.
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


#ifndef OSGGA_TESTMANIPULATOR
#define OSGGA_TESTMANIPULATOR 1

#include <osgGA/CameraManipulator>
#include <osg/Quat>

class TestManipulator : public osgGA.CameraManipulator
    public:

        TestManipulator()
        virtual ~TestManipulator()

        #* set the position of the matrix manipulator using a 4x4 Matrix.
        virtual void setByMatrix( osg.Matrixd matrix)

        #* set the position of the matrix manipulator using a 4x4 Matrix.
        virtual void setByInverseMatrix( osg.Matrixd matrix)  setByMatrix(osg.Matrixd.inverse(matrix)) 

        #* get the position of the manipulator as 4x4 Matrix.
        virtual osg.Matrixd getMatrix() 

        #* get the position of the manipulator as a inverse matrix of the manipulator, typically used as a model view matrix.
        virtual osg.Matrixd getInverseMatrix() 

        #* Attach a node to the manipulator. 
            Automatically detaches previously attached node.
            setNode(NULL) detaches previously nodes.
            Is ignored by manipulators which do not require a reference model.
        virtual void setNode(osg.Node*)

        #* Return node if attached.
        virtual  osg.Node* getNode() 

        #* Return node if attached.
        virtual osg.Node* getNode()

        #* Move the camera to the default position. 
            May be ignored by manipulators if home functionality is not appropriate.
        virtual void home( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter us)
        
        #* Start/restart the manipulator.
        virtual void init( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter us)


        #* handle events, return true if handled, false otherwise.
        virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter us)

    private:

        #* Reset the internal GUIEvent stack.
        flushMouseEventStack = void()
        #* Add the current mouse GUIEvent to internal stack.
        addMouseEvent = void( osgGA.GUIEventAdapter ea)

        computePosition = void( osg.Vec3 eye, osg.Vec3 lv, osg.Vec3 up)

        #* For the give mouse movement calculate the movement of the camera.
            Return true is camera has moved and a redraw is required.
        calcMovement = bool()
        
        #* Check the speed at which the mouse is moving.
            If speed is below a threshold then return false, otherwise return true.
        isMouseMoving = bool()

        # Internal event stack comprising last three mouse events.
        osg.ref_ptr< osgGA.GUIEventAdapter> _ga_t1
        osg.ref_ptr< osgGA.GUIEventAdapter> _ga_t0

        osg.ref_ptr<osg.Node>       _node

        _modelScale = float()
        _minimumZoomScale = float()

        _thrown = bool()
        
        _center = osg.Vec3()
        _rotation = osg.Quat()
        _distance = float()



#endif


if __name__ == "__main__":
    main(sys.argv)
