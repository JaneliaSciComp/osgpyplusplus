#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgspheresegment"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgParticle
from osgpypp import osgSim
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgspheresegment.cpp'

# OpenSceneGraph example, osgspheresegment.
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

#include <osg/Group>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Texture2D>
#include <osg/PositionAttitudeTransform>
#include <osg/MatrixTransform>
#include <osg/Geometry>

#include <osgUtil/SmoothingVisitor>

#include <osgDB/ReadFile>

#include <osgText/Text>

#include <osgSim/SphereSegment>
#include <osgSim/OverlayNode>

#include <osgParticle/ExplosionEffect>
#include <osgParticle/SmokeEffect>
#include <osgParticle/FireEffect>
#include <osgParticle/ParticleSystemUpdater>

#include <osg/io_utils>

#include <iostream>

# for the grid data..
#include "../osghangglide/terrain_coords.h"

def createAnimationPath(center, radius, looptime):

    
    # set up the animation path
    animationPath = osg.AnimationPath()
    animationPath.setLoopMode(osg.AnimationPath.LOOP)

    numSamples = 40
    yaw = 0.0
    yaw_delta = 2.0*osg.PI/((float)numSamples-1.0)
    roll = osg.inDegrees(30.0)

    time = 0.0
    time_delta = looptime/(double)numSamples
    for(int i=0i<numSamples++i)
        position = osg.Vec3(center+osg.Vec3(sinf(yaw)*radius,cosf(yaw)*radius,0.0))
        rotation = osg.Quat(osg.Quat(roll,osg.Vec3(0.0,1.0,0.0))*osg.Quat(-(yaw+osg.inDegrees(90.0)),osg.Vec3(0.0,0.0,1.0)))

        animationPath.insert(time,osg.AnimationPath.ControlPoint(position,rotation))

        yaw += yaw_delta
        time += time_delta

    return animationPath



class IntersectionUpdateCallback (osg.NodeCallback) :
virtual void operator()(osg.Node* #node, osg.NodeVisitor* nv)
            if !root_ || !terrain_ || !ss_ || !intersectionGroup_ :
                osg.notify(osg.NOTICE), "IntersectionUpdateCallback not set up correctly."
                return

            #traverse(node,nv)
            frameCount_++
            if frameCount_ > 200 :
                # first we need find the transformation matrix that takes
                # the terrain into the coordinate frame of the sphere segment.
                terrainLocalToWorld = osg.Matrixd()
                terrain_worldMatrices = terrain_.getWorldMatrices(root_.get())
                if terrain_worldMatrices.empty() : terrainLocalToWorld.makeIdentity()
                elif terrain_worldMatrices.size()==1 : terrainLocalToWorld = terrain_worldMatrices.front()
                else :
                    osg.notify(osg.NOTICE), "IntersectionUpdateCallback: warning cannot interestect with multiple terrain instances, just uses first one."
                    terrainLocalToWorld = terrain_worldMatrices.front()

                # sphere segment is easier as this callback is attached to the node, so the node visitor has the unique path to it already.
                ssWorldToLocal = osg.computeWorldToLocal(nv.getNodePath())

                # now we can compute the terrain to ss transform
                possie = terrainLocalToWorld*ssWorldToLocal

                lines = ss_.computeIntersection(possie, terrain_.get())
                if !lines.empty() :
                    if intersectionGroup_.valid() :
                        # now we need to place the intersections which are in the SphereSegmenet's coordinate frame into
                        # to the final position.
                        mt = osg.MatrixTransform()
                        mt.setMatrix(osg.computeLocalToWorld(nv.getNodePath()))
                        intersectionGroup_.addChild(mt)

                        # print "matrix = ", mt.getMatrix()

                        geode = osg.Geode()
                        mt.addChild(geode)

                        geode.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)

                        for(osgSim.SphereSegment.LineList.iterator itr=lines.begin()
                           itr!=lines.end()
                           ++itr)
                            geom = osg.Geometry()
                            geode.addDrawable(geom)

                            vertices = itr.get()
                            geom.setVertexArray(vertices)
                            geom.addPrimitiveSet(osg.DrawArrays(GL_LINE_STRIP, 0, vertices.getNumElements()))
                else :
                       osg.notify(osg.NOTICE), "No intersections found"


                frameCount_ = 0
    root_ = osg.observer_ptr<osg.Group>()
    terrain_ = osg.observer_ptr<osg.Geode>()
    ss_ = osg.observer_ptr<osgSim.SphereSegment>()
    intersectionGroup_ = osg.observer_ptr<osg.Group>()
    frameCount_ = unsigned()


class RotateUpdateCallback (osg.NodeCallback) :
    RotateUpdateCallback()  i=0
        virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
            ss = dynamic_cast<osgSim.SphereSegment *>(node)
            if ss :
                ss.setArea(osg.Vec3(cos(i/(2*osg.PI)),sin(i/(2*osg.PI)),0), osg.PI_2, osg.PI_2)

                i += 0.1

    i = float()


def createMovingModel(center, radius, terrainGeode, root, createMovingRadar):

    
    animationLength = 10.0

    animationPath = createAnimationPath(center,radius,animationLength)

    model = osg.Group()

    glider = osgDB.readNodeFile("glider.osgt")
    if glider :
        bs = glider.getBound()

        size = radius/bs.radius()*0.3
        positioned = osg.MatrixTransform()
        positioned.setDataVariance(osg.Object.STATIC)
        positioned.setMatrix(osg.Matrix.translate(-bs.center())*
                                     osg.Matrix.scale(size,size,size)*
                                     osg.Matrix.rotate(osg.inDegrees(-90.0),0.0,0.0,1.0))

        positioned.addChild(glider)

        xform = osg.PositionAttitudeTransform()
        xform.getOrCreateStateSet().setMode(GL_NORMALIZE, osg.StateAttribute.ON)
        xform.setUpdateCallback(osg.AnimationPathCallback(animationPath,0.0,1.0))
        xform.addChild(positioned)
        model.addChild(xform)

    if createMovingRadar :
        # The IntersectionUpdateCallback has to have a safe place to put all its generated geometry into,
        # and this group can't be in the parental chain of the callback otherwise we will end up invalidating
        # traversal iterators.
        intersectionGroup = osg.Group()
        root.addChild(intersectionGroup)

        xform = osg.PositionAttitudeTransform()
        xform.setUpdateCallback(osg.AnimationPathCallback(animationPath,0.0,1.0))

        ss = osgSim.SphereSegment(osg.Vec3d(0.0,0.0,0.0),
                                700.0, # radius
                                osg.DegreesToRadians(135.0),
                                osg.DegreesToRadians(240.0),
                                osg.DegreesToRadians(-60.0),
                                osg.DegreesToRadians(-40.0),
                                60)

        iuc = IntersectionUpdateCallback()
        iuc.frameCount_ = 0
        iuc.root_ = root
        iuc.terrain_ = terrainGeode
        iuc.ss_ = ss
        iuc.intersectionGroup_ = intersectionGroup
        ss.setUpdateCallback(iuc)
        ss.setAllColors(osg.Vec4(1.0,1.0,1.0,0.5))
        ss.setSideColor(osg.Vec4(0.5,1.0,1.0,0.1))
        xform.addChild(ss)
        model.addChild(xform)

    cessna = osgDB.readNodeFile("cessna.osgt")
    if cessna :
        bs = cessna.getBound()

        text = osgText.Text()
        size = radius/bs.radius()*0.3

        text.setPosition(bs.center())
        text.setText("Cessna")
        text.setAlignment(osgText.Text.CENTER_CENTER)
        text.setAxisAlignment(osgText.Text.SCREEN)
        text.setCharacterSize(40.0)
        text.setCharacterSizeMode(osgText.Text.OBJECT_COORDS)

        geode = osg.Geode()
        geode.addDrawable(text)

        lod = osg.LOD()
        lod.setRangeMode(osg.LOD.PIXEL_SIZE_ON_SCREEN)
        lod.setRadius(cessna.getBound().radius())
        lod.addChild(geode,0.0,100.0)
        lod.addChild(cessna,100.0,10000.0)


        positioned = osg.MatrixTransform()
        positioned.getOrCreateStateSet().setMode(GL_NORMALIZE, osg.StateAttribute.ON)
        positioned.setDataVariance(osg.Object.STATIC)
        positioned.setMatrix(osg.Matrix.translate(-bs.center())*
                                     osg.Matrix.scale(size,size,size)*
                                     osg.Matrix.rotate(osg.inDegrees(180.0),0.0,0.0,1.0))

        #positioned.addChild(cessna)
        positioned.addChild(lod)

        xform = osg.MatrixTransform()
        xform.setUpdateCallback(osg.AnimationPathCallback(animationPath,0.0,2.0))
        xform.addChild(positioned)

        model.addChild(xform)

    return model

def createOverlay(center, radius):

    
    group = osg.Group()

    # create a grid of lines.
        geom = osg.Geometry()

        num_rows = 10

        left = center+osg.Vec3(-radius,-radius,0.0)
        right = center+osg.Vec3(radius,-radius,0.0)
        delta_row = osg.Vec3(0.0,2.0*radius/float(num_rows-1),0.0)

        top = center+osg.Vec3(-radius,radius,0.0)
        bottom = center+osg.Vec3(-radius,-radius,0.0)
        delta_column = osg.Vec3(2.0*radius/float(num_rows-1),0.0,0.0)

        vertices = osg.Vec3Array()
        for(unsigned int i=0 i<num_rows ++i)
            vertices.push_back(left)
            vertices.push_back(right)
            left += delta_row
            right += delta_row

            vertices.push_back(top)
            vertices.push_back(bottom)
            top += delta_column
            bottom += delta_column

        geom.setVertexArray(vertices)

        color = *(osg.Vec4ubArray(1))
        color[0].set(0,0,0,255)
        geom.setColorArray(color, osg.Array.BIND_OVERALL)

        geom.addPrimitiveSet(osg.DrawArrays(GL_LINES,0,vertices.getNumElements()))

        geom.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)

        geode = osg.Geode()
        geode.addDrawable(geom)
        group.addChild(geode)

    return group

def computeTerrainIntersection(subgraph, x, y):

    
    bs = subgraph.getBound()
    zMax = bs.center().z()+bs.radius()
    zMin = bs.center().z()-bs.radius()

    intersector = osgUtil.LineSegmentIntersector(osg.Vec3(x,y,zMin),osg.Vec3(x,y,zMax))

    iv = osgUtil.IntersectionVisitor(intersector.get())

    subgraph.accept(iv)

    if intersector.containsIntersections() :
        return intersector.getFirstIntersection().getWorldIntersectPoint()

    return osg.Vec3(x,y,0.0)


#######################################
# MAIN SCENE GRAPH BUILDING FUNCTION
#######################################

def build_world(root, testCase, useOverlay, technique):

    

    # create terrain
    terrainGeode = 0
        terrainGeode = osg.Geode()

        stateset = osg.StateSet()
        image = osgDB.readImageFile("Images/lz.rgb")
        if image :
            texture = osg.Texture2D()
            texture.setImage(image)
            stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

        terrainGeode.setStateSet( stateset )


            numColumns = 38
            numRows = 39
            unsigned int r, c

            origin = osg.Vec3(0.0,0.0,0.0)
            size = osg.Vec3(1000.0,1000.0,250.0)

            geometry = osg.Geometry()

            v = *(osg.Vec3Array(numColumns*numRows))
            tc = *(osg.Vec2Array(numColumns*numRows))
            color = *(osg.Vec4ubArray(1))

            color[0].set(255,255,255,255)

            rowCoordDelta = size.y()/(float)(numRows-1)
            columnCoordDelta = size.x()/(float)(numColumns-1)

            rowTexDelta = 1.0/(float)(numRows-1)
            columnTexDelta = 1.0/(float)(numColumns-1)

            # compute z range of z values of grid data so we can scale it.
            min_z = FLT_MAX
            max_z = -FLT_MAX
            for(r=0r<numRows++r)
                for(c=0c<numColumns++c)
                    min_z = osg.minimum(min_z,vertex[r+c*numRows][2])
                    max_z = osg.maximum(max_z,vertex[r+c*numRows][2])

            scale_z = size.z()/(max_z-min_z)

            pos = origin
            tex = osg.Vec2(0.0,0.0)
            vi = 0
            for(r=0r<numRows++r)
                pos.x() = origin.x()
                tex.x() = 0.0
                for(c=0c<numColumns++c)
                    v[vi].set(pos.x(),pos.y(),pos.z()+(vertex[r+c*numRows][2]-min_z)*scale_z)
                    tc[vi] = tex
                    pos.x()+=columnCoordDelta
                    tex.x()+=columnTexDelta
                    ++vi
                pos.y() += rowCoordDelta
                tex.y() += rowTexDelta

            geometry.setVertexArray(v)
            geometry.setTexCoordArray(0, tc)
            geometry.setColorArray(color, osg.Array.BIND_OVERALL)

            for(r=0r<numRows-1++r)
                drawElements = *(osg.DrawElementsUShort(GL_QUAD_STRIP,2*numColumns))
                geometry.addPrimitiveSet(drawElements)
                ei = 0
                for(c=0c<numColumns++c)
                    drawElements[ei++] = (r+1)*numColumns+c
                    drawElements[ei++] = (r)*numColumns+c

            smoother = osgUtil.SmoothingVisitor()
            smoother.smooth(*geometry)

            terrainGeode.addDrawable(geometry)



    # create sphere segment
    ss = 0

        terrainToSS = osg.Matrix()

        switch(testCase)
            case(0):
                ss = osgSim.SphereSegment(
                                computeTerrainIntersection(terrainGeode.get(),550.0,780.0), # center
                                510.0, # radius
                                osg.DegreesToRadians(135.0),
                                osg.DegreesToRadians(240.0),
                                osg.DegreesToRadians(-10.0),
                                osg.DegreesToRadians(30.0),
                                60)
                root.addChild(ss.get())
                break
            case(1):
                ss = osgSim.SphereSegment(
                                computeTerrainIntersection(terrainGeode.get(),550.0,780.0), # center
                                510.0, # radius
                                osg.DegreesToRadians(45.0),
                                osg.DegreesToRadians(240.0),
                                osg.DegreesToRadians(-10.0),
                                osg.DegreesToRadians(30.0),
                                60)
                root.addChild(ss.get())
                break
            case(2):
                ss = osgSim.SphereSegment(
                                computeTerrainIntersection(terrainGeode.get(),550.0,780.0), # center
                                510.0, # radius
                                osg.DegreesToRadians(5.0),
                                osg.DegreesToRadians(355.0),
                                osg.DegreesToRadians(-10.0),
                                osg.DegreesToRadians(30.0),
                                60)
                root.addChild(ss.get())
                break
            case(3):
                ss = osgSim.SphereSegment(
                                computeTerrainIntersection(terrainGeode.get(),550.0,780.0), # center
                                510.0, # radius
                                osg.DegreesToRadians(0.0),
                                osg.DegreesToRadians(360.0),
                                osg.DegreesToRadians(-10.0),
                                osg.DegreesToRadians(30.0),
                                60)
                root.addChild(ss.get())
                break
            case(4):
                ss = osgSim.SphereSegment(osg.Vec3d(0.0,0.0,0.0),
                                700.0, # radius
                                osg.DegreesToRadians(135.0),
                                osg.DegreesToRadians(240.0),
                                osg.DegreesToRadians(-60.0),
                                osg.DegreesToRadians(-40.0),
                                60)

                mt = osg.MatrixTransform()

                mt.setMatrix(osg.Matrix(-0.851781, 0.156428, -0.5, 0,
                                          -0.180627, -0.983552, -6.93889e-18, 0,
                                          -0.491776, 0.0903136, 0.866025, 0,
                                          598.217, 481.957, 100, 1))
                mt.addChild(ss.get())

                terrainToSS.invert(mt.getMatrix())

                root.addChild(mt.get())
                break
            case(5):
                ss = osgSim.SphereSegment(osg.Vec3d(0.0,0.0,0.0),
                                700.0, # radius
                                osg.DegreesToRadians(35.0),
                                osg.DegreesToRadians(135.0),
                                osg.DegreesToRadians(-60.0),
                                osg.DegreesToRadians(-40.0),
                                60)

                mt = osg.MatrixTransform()

                mt.setMatrix(osg.Matrix(-0.851781, 0.156428, -0.5, 0,
                                          -0.180627, -0.983552, -6.93889e-18, 0,
                                          -0.491776, 0.0903136, 0.866025, 0,
                                          598.217, 481.957, 100, 1))
                mt.addChild(ss.get())

                terrainToSS.invert(mt.getMatrix())

                root.addChild(mt.get())
                break
            case(6):
                ss = osgSim.SphereSegment(osg.Vec3d(0.0,0.0,0.0),
                                700.0, # radius
                                osg.DegreesToRadians(-45.0),
                                osg.DegreesToRadians(45.0),
                                osg.DegreesToRadians(-60.0),
                                osg.DegreesToRadians(-40.0),
                                60)

                mt = osg.MatrixTransform()

                mt.setMatrix(osg.Matrix(-0.851781, 0.156428, -0.5, 0,
                                          -0.180627, -0.983552, -6.93889e-18, 0,
                                          -0.491776, 0.0903136, 0.866025, 0,
                                          598.217, 481.957, 100, 1))
                mt.addChild(ss.get())

                terrainToSS.invert(mt.getMatrix())

                root.addChild(mt.get())
                break
            case(7):
                ss = osgSim.SphereSegment(
                                computeTerrainIntersection(terrainGeode.get(),550.0,780.0), # center
                                510.0, # radius
                                osg.DegreesToRadians(-240.0),
                                osg.DegreesToRadians(-135.0),
                                osg.DegreesToRadians(-10.0),
                                osg.DegreesToRadians(30.0),
                                60)
                ss.setUpdateCallback(RotateUpdateCallback())
                root.addChild(ss.get())
                break
        

        if ss.valid() :
            ss.setAllColors(osg.Vec4(1.0,1.0,1.0,0.5))
            ss.setSideColor(osg.Vec4(0.0,1.0,1.0,0.1))

            if !ss.getParents().empty() :
                ss.getParent(0).addChild(ss.computeIntersectionSubgraph(terrainToSS, terrainGeode.get()))



    if useOverlay :
        overlayNode = osgSim.OverlayNode(technique)
        overlayNode.getOrCreateStateSet().setTextureAttribute(1, osg.TexEnv(osg.TexEnv.DECAL))

        bs = terrainGeode.getBound()
        overlaySubgraph = createOverlay(bs.center(), bs.radius()*0.5)
        overlaySubgraph.addChild(ss.get())
        overlayNode.setOverlaySubgraph(overlaySubgraph)
        overlayNode.setOverlayTextureSizeHint(1024)
        overlayNode.setOverlayBaseHeight(0.0)
        overlayNode.addChild(terrainGeode.get())

        root.addChild(overlayNode)
    else :
      root.addChild(terrainGeode.get())

    # create particle effects
        position = computeTerrainIntersection(terrainGeode.get(),100.0,100.0)

        explosion = osgParticle.ExplosionEffect(position, 10.0)
        smoke = osgParticle.SmokeEffect(position, 10.0)
        fire = osgParticle.FireEffect(position, 10.0)

        root.addChild(explosion)
        root.addChild(smoke)
        root.addChild(fire)

    # create particle effects
        position = computeTerrainIntersection(terrainGeode.get(),200.0,100.0)

        explosion = osgParticle.ExplosionEffect(position, 1.0)
        smoke = osgParticle.SmokeEffect(position, 1.0)
        fire = osgParticle.FireEffect(position, 1.0)

        root.addChild(explosion)
        root.addChild(smoke)
        root.addChild(fire)


    createMovingRadar = True

    # create the moving models.
        root.addChild(createMovingModel(osg.Vec3(500.0,500.0,500.0),100.0, terrainGeode.get(), root, createMovingRadar))


#######################################
# main()
#######################################


def main(argc, argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use of particle systems.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] image_file_left_eye image_file_right_eye")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")


    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    # if user request help write it out to cout.
    testCase = 0
    while arguments.read("-t", testCase) : 

    useOverlay = False
    technique = osgSim.OverlayNode.OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY
    while arguments.read("--object") :  useOverlay = True technique = osgSim.OverlayNode.OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY 
    while arguments.read("--ortho") || arguments.read("--orthographic") :  useOverlay = True technique = osgSim.OverlayNode.VIEW_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY 
    while arguments.read("--persp") || arguments.read("--perspective") :  useOverlay = True technique = osgSim.OverlayNode.VIEW_DEPENDENT_WITH_PERSPECTIVE_OVERLAY 


    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    root = osg.Group()
    build_world(root, testCase, useOverlay, technique)

    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData(root)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
