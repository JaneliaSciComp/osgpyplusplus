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


# Translated from file 'osgimpostor.cpp'

# OpenSceneGraph example, osgimpostor.
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
typedef osg.Node    NodePtr
typedef std.list<NodePtr>        NodeContainer
typedef NodeContainer.iterator    NodeIterator

nodes = NodeContainer()

#
Root = 0

HOUSES_SIZE = 25000        # total number of houses
XDim = 5000.0                # area dimension +/- XDim
ZDim = 5000.0                # area dimension +/- YDim

GridX = 20                        # number of grids in x direction
GridY = 20                        # number of grids in y direction

UseImpostor = True            # use impostor (or do not use)

Threshold = 3000.0            # distance where impostor are shown

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
    colors = osg.Vec4Array(1)
    (*colors)[0] = osg.Vec4(1.0, 1.0, 1.0, 1.0)

    # normals
    normals = osg.Vec3Array(16)
    (*normals)[0] = osg.Vec3( 0.0,  -0.0, -1.0)
    (*normals)[1] = osg.Vec3( 0.0,  -0.0, -1.0)
    (*normals)[2] = osg.Vec3( 0.0,  -1.0,  0.0)
    (*normals)[3] = osg.Vec3( 0.0,  -1.0,  0.0)
    (*normals)[4] = osg.Vec3( 1.0,  -0.0,  0.0)
    (*normals)[5] = osg.Vec3( 1.0,  -0.0,  0.0)
    (*normals)[6] = osg.Vec3( 0.0, 1.0,  0.0)
    (*normals)[7] = osg.Vec3( 0.0, 1.0,  0.0)
    (*normals)[8] = osg.Vec3(-1.0,  -0.0,  0.0)
    (*normals)[9] = osg.Vec3(-1.0,  -0.0,  0.0)
    (*normals)[10] = osg.Vec3( 0.0,  -0.928477, 0.371391)
    (*normals)[11] = osg.Vec3( 0.0, 0.928477, 0.371391)
    (*normals)[12] = osg.Vec3( 0.707107,  0.0, 0.707107)
    (*normals)[13] = osg.Vec3( 0.707107,  0.0, 0.707107)
    (*normals)[14] = osg.Vec3(-0.707107,  0.0, 0.707107)
    (*normals)[15] = osg.Vec3(-0.707107,  0.0, 0.707107)

    # coordIndices
    coordIndices = osg.UByteArray(48,indices)

    # share the primitive set.
    primitives = osg.DrawArrays(osg.PrimitiveSet.TRIANGLES,0,48)

    for (int q = 0 q < HOUSES_SIZE q++)
        xPos = ((static_cast<double> (rand()) /
                      static_cast<double> (RAND_MAX))
                     * 2.0 * XDim) - XDim

        yPos = ((static_cast<double> (rand()) /
                      static_cast<double> (RAND_MAX))
                     * 2 * ZDim) - ZDim

        scale = 10.0

        offset = osg.Vec3(xPos,yPos,0.0)

        # coords
        coords = osg.Vec3Array(10)
        (*coords)[0] = osg.Vec3( 0.5, -0.7, 0.0)
        (*coords)[1] = osg.Vec3( 0.5,  0.7, 0.0)
        (*coords)[2] = osg.Vec3(-0.5, 0.7, 0.0)
        (*coords)[3] = osg.Vec3(-0.5, -0.7, 0.0)
        (*coords)[4] = osg.Vec3( 0.5, -0.7, 1.0)
        (*coords)[5] = osg.Vec3( 0.5,  0.7, 1.0)
        (*coords)[6] = osg.Vec3(-0.5,  0.7, 1.0)
        (*coords)[7] = osg.Vec3(-0.5, -0.7, 1.0)
        (*coords)[8] = osg.Vec3( 0.0, -0.5, 1.5)
        (*coords)[9] = osg.Vec3( 0.0,  0.5, 1.5)

        for (i = 0 i < 10 i++)
            (*coords)[i] = (*coords)[i] * scale + offset


        # create geometry
        geometry = deprecated_osg.Geometry()

        geometry.addPrimitiveSet(primitives)

        geometry.setVertexArray(coords)
        geometry.setVertexIndices(coordIndices)

        geometry.setColorArray(colors)
        geometry.setColorBinding(deprecated_osg.Geometry.BIND_OVERALL)

        geometry.setNormalArray(normals)
        geometry.setNormalBinding(deprecated_osg.Geometry.BIND_PER_PRIMITIVE)

        geode = osg.Geode()
        geode.addDrawable(geometry)

        nodes.push_back(geode)

def LayoutAsGrid():

    
    # calculate bounding box
    bbox = osg.BoundingBox()
    for (NodeIterator node = nodes.begin() node  not = nodes.end() ++node)
        bbox.expandBy((*node).getBound())

    # setup grid information
    groups = osg.Group*[GridX * GridY]()
        i = int()
    for (i = 0 i < GridX * GridY i++)
        groups[i] = osg.Group()

    xGridStart = bbox.xMin()
    xGridSize = (bbox.xMax() - bbox.xMin()) / GridX

    yGridStart = bbox.yMin()
    yGridSize = (bbox.yMax() - bbox.yMin()) / GridY

    # arrange buildings into right grid
    for (NodeIterator nodeIter = nodes.begin() nodeIter  not = nodes.end() ++nodeIter)
        node = nodeIter
        center = node.getBound().center()

        x = (int)floor((center.x() - xGridStart) / xGridSize)
        z = (int)floor((center.y() - yGridStart) / yGridSize)

        groups[z * GridX + x].addChild(node)

    # add nodes to building root
    for (i = 0 i < GridX * GridY i++)
        stateset = osg.StateSet()

        material = osg.Material()
        color = osg.Vec4(
            0.5 + (static_cast<double> (rand()) / (2.0*static_cast<double> (RAND_MAX))),
            0.5 + (static_cast<double> (rand()) / (2.0*static_cast<double> (RAND_MAX))),
            0.5 + (static_cast<double> (rand()) / ( 2.0*static_cast<double>(RAND_MAX))),
            1.0)

        material.setAmbient(osg.Material.FRONT_AND_BACK, color)
        material.setDiffuse(osg.Material.FRONT_AND_BACK, color)
        stateset.setAttributeAndModes(material, osg.StateAttribute.ON)

        groups[i].setStateSet(stateset)

        if UseImpostor :
            impostor = osgSim.Impostor()
            impostor.setImpostorThreshold(static_cast<float> (Threshold))
            impostor.addChild(groups[i])
            impostor.setRange(0, 0.0, 1e7f)
            impostor.setCenter(groups[i].getBound().center())
            Root.addChild(impostor)
        else:
            Root.addChild(groups[i])

    delete[] groups


def main(argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # add local test manipulator more suitable for testing impostors.
    viewer.setCameraManipulator(TestManipulator)()


    # load the nodes from the commandline arguments.
    model = osgDB.readNodeFiles(arguments)
    if model :
        # the osgSim.InsertImpostorsVisitor used lower down to insert impostors
        # only operators on subclass of Group's, if the model top node is not
        # a group then it won't be able to insert an impostor.  We therefore
        # manually insert an impostor above the model.
        if dynamic_cast<osg.Group*>(model)==0 :
            bs = model.getBound()
            if bs.valid() :

                impostor = osgSim.Impostor()

                # standard LOD settings
                impostor.addChild(model)
                impostor.setRange(0,0.0,1e7f)
                impostor.setCenter(bs.center())

                # impostor specfic settings.
                impostor.setImpostorThresholdToBound(5.0)

                model = impostor


        # we insert an impostor node above the model, so we keep a handle
        # on the rootnode of the model, the is required since the
        # InsertImpostorsVisitor can add a root in automatically and
        # we would know about it, other than by following the parent path
        # up from model.  This is really what should be done, but I'll pass
        # on it right now as it requires a getRoots() method to be added to
        # osg.Node, and we're about to make a release so no features not 
        rootnode = osg.Group()
        rootnode.addChild(model)


        # now insert impostors in the model using the InsertImpostorsVisitor.
        ov = osgSim.InsertImpostorsVisitor()

        # traverse the model and collect all osg.Group's and osg.LOD's.
        # however, don't traverse the rootnode since we want to keep it as
        # the start of traversal, otherwise the insertImpostor could insert
        # and Impostor above the current root, making it nolonger a root not 
        model.accept(ov)

        # insert the Impostors above groups and LOD's
        ov.insertImpostors()
    else:
        # no user model so we'll create our own world.
        model = Root = osg.Group()
        CreateHouses()
        LayoutAsGrid()

    # add model to viewer.
    viewer.setSceneData(model)

    return viewer.run()

# Translated from file 'TestManipulator.cpp'

# OpenSceneGraph example, osgimpostor.
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

#include "TestManipulator.h"
#include <osg/Notify>

using namespace osg
using namespace osgGA

TestManipulator.TestManipulator()
    _modelScale = 0.01
    _minimumZoomScale = 0.05
    _thrown = False

    _distance = 1.0


TestManipulator.~TestManipulator()


void TestManipulator.setNode(osg.Node* node)
    _node = node
    if _node :
        boundingSphere = _node.getBound()
        _modelScale = boundingSphere._radius


 osg.Node* TestManipulator.getNode() 
    return _node


osg.Node* TestManipulator.getNode()
    return _node


                                 #ea
void TestManipulator.home( GUIEventAdapter ,GUIActionAdapter us)
    if _node :

        boundingSphere = _node.getBound()

        computePosition(boundingSphere.center()+osg.Vec3(0.0, 0.0, 20.0),
                        osg.Vec3(0.0, 1.0, 0.0),
                        osg.Vec3(0.0,  0.0,  1.0))

        us.requestRedraw()


void TestManipulator.init( GUIEventAdapter ,GUIActionAdapter )
    flushMouseEventStack()

bool TestManipulator.handle( GUIEventAdapter ea,GUIActionAdapter us)
    switch(ea.getEventType())
        case(GUIEventAdapter.PUSH):
            flushMouseEventStack()
            addMouseEvent(ea)
            if calcMovement() : us.requestRedraw()
            us.requestContinuousUpdate(False)
            _thrown = False
            return True

        case(GUIEventAdapter.RELEASE):
            if ea.getButtonMask()==0 :

                if isMouseMoving() :
                    if calcMovement() :
                        us.requestRedraw()
                        us.requestContinuousUpdate(True)
                        _thrown = True
                else:
                    flushMouseEventStack()
                    addMouseEvent(ea)
                    if calcMovement() : us.requestRedraw()
                    us.requestContinuousUpdate(False)
                    _thrown = False

            else:
                flushMouseEventStack()
                addMouseEvent(ea)
                if calcMovement() : us.requestRedraw()
                us.requestContinuousUpdate(False)
                _thrown = False
            return True

        case(GUIEventAdapter.DRAG):
            addMouseEvent(ea)
            if calcMovement() : us.requestRedraw()
            us.requestContinuousUpdate(False)
            _thrown = False
            return True

        case(GUIEventAdapter.MOVE):
            return False

        case(GUIEventAdapter.KEYDOWN):
            if ea.getKey()==ord(" ") :
                flushMouseEventStack()
                _thrown = False
                home(ea,us)
                us.requestRedraw()
                us.requestContinuousUpdate(False)
                return True
            return False
        case(GUIEventAdapter.FRAME):
            if _thrown :
                if calcMovement() : us.requestRedraw()
                return True
            return False
        default:
            return False


bool TestManipulator.isMouseMoving()
    if _ga_t0==NULL  or  _ga_t1==NULL : return False

    static  float velocity = 0.1

    dx = _ga_t0.getXnormalized()-_ga_t1.getXnormalized()
    dy = _ga_t0.getYnormalized()-_ga_t1.getYnormalized()
    len = sqrtf(dx*dx+dy*dy)
    dt = _ga_t0.getTime()-_ga_t1.getTime()

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
    _distance = 1.0

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
    
    rotation_matrix = osg.Matrixd(s[0],     u[0],     -f[0],     0.0,
                                s[1],     u[1],     -f[1],     0.0,
                                s[2],     u[2],     -f[2],     0.0,
                                0.0,     0.0,     0.0,      1.0)
                   
    _center = eye+lv
    _distance = lv.length()
    _rotation = rotation_matrix.getRotate().inverse()


bool TestManipulator.calcMovement()

    # return if less then two events have been added.
    if _ga_t0==NULL  or  _ga_t1==NULL : return False

    dx = _ga_t0.getXnormalized()-_ga_t1.getXnormalized()
    dy = _ga_t0.getYnormalized()-_ga_t1.getYnormalized()


    # return if there is no movement.
    if dx==0  and  dy==0 : return False

    buttonMask = _ga_t1.getButtonMask()
    if buttonMask==GUIEventAdapter.LEFT_MOUSE_BUTTON :

        # rotate camera.

        new_rotate = osg.Quat()
        new_rotate.makeRotate(dx / 3.0, osg.Vec3(0.0, 0.0, 1.0))
        
        _rotation = _rotation*new_rotate

        return True

    elif buttonMask==GUIEventAdapter.MIDDLE_MOUSE_BUTTON :

        # pan model.

        dv = osg.Vec3(0.0, 0.0, -500.0) * dy

        _center += dv
        
        return True

    elif buttonMask==GUIEventAdapter.RIGHT_MOUSE_BUTTON :
        rotation_matrix = osg.Matrixd(_rotation)
    
                        
        uv = osg.Vec3(0.0,1.0,0.0)*rotation_matrix
        sv = osg.Vec3(1.0,0.0,0.0)*rotation_matrix
        fv = uv ^ sv
        dv = fv*(dy*-500.0)-sv*(dx*500.0)

        _center += dv

        return True

    return False

# Translated from file 'TestManipulator.h'

# -*-c++-*- 
#*
#*  OpenSceneGraph example, osgimpostor.
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

#ifndef OSGGA_TESTMANIPULATOR
#define OSGGA_TESTMANIPULATOR 1

#include <osgGA/CameraManipulator>
#include <osg/Quat>

class TestManipulator (osgGA.CameraManipulator) :

        TestManipulator()
        virtual ~TestManipulator()

        #* set the position of the matrix manipulator using a 4x4 Matrix.
        setByMatrix = virtual void( osg.Matrixd matrix)

        #* set the position of the matrix manipulator using a 4x4 Matrix.
        def setByInverseMatrix(matrix):
             setByMatrix(osg.Matrixd.inverse(matrix)) 

        #* get the position of the manipulator as 4x4 Matrix.
        virtual osg.Matrixd getMatrix() 

        #* get the position of the manipulator as a inverse matrix of the manipulator, typically used as a model view matrix.
        virtual osg.Matrixd getInverseMatrix() 

        #* Attach a node to the manipulator. 
#            Automatically detaches previously attached node.
#            setNode(NULL) detaches previously nodes.
#            Is ignored by manipulators which do not require a reference model.
        setNode = virtual void(osg.Node*)

        #* Return node if attached.
        virtual  osg.Node* getNode() 

        #* Return node if attached.
        getNode = virtual osg.Node*()

        #* Move the camera to the default position. 
#            May be ignored by manipulators if home functionality is not appropriate.
        home = virtual void( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter us)
        
        #* Start/restart the manipulator.
        init = virtual void( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter us)


        #* handle events, return True if handled, False otherwise.
        handle = virtual bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter us)

        #* Reset the internal GUIEvent stack.
        flushMouseEventStack = void()
        #* Add the current mouse GUIEvent to internal stack.
        addMouseEvent = void( osgGA.GUIEventAdapter ea)

        computePosition = void( osg.Vec3 eye, osg.Vec3 lv, osg.Vec3 up)

        #* For the give mouse movement calculate the movement of the camera.
#            Return True is camera has moved and a redraw is required.
        calcMovement = bool()
        
        #* Check the speed at which the mouse is moving.
#            If speed is below a threshold then return False, otherwise return True.
        isMouseMoving = bool()

        # Internal event stack comprising last three mouse events.
        _ga_t1 =  osgGA.GUIEventAdapter()
        _ga_t0 =  osgGA.GUIEventAdapter()

        _node = osg.Node()

        _modelScale = float()
        _minimumZoomScale = float()

        _thrown = bool()
        
        _center = osg.Vec3()
        _rotation = osg.Quat()
        _distance = float()



#endif


if __name__ == "__main__":
    main(sys.argv)
