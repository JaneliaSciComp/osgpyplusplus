#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganimationhardware"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osganimationhardware.cpp'

#  -*-c++-*- 
# *  Copyright (C) 2009 Cedric Pinson <cedric.pinson@plopbyte.net>
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

#include <iostream>
#include <osgDB/ReadFile>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>
#include <osg/Drawable>
#include <osg/MatrixTransform>

#include <osgAnimation/BasicAnimationManager>
#include <osgAnimation/RigGeometry>
#include <osgAnimation/RigTransformHardware>
#include <osgAnimation/AnimationManagerBase>
#include <osgAnimation/BoneMapVisitor>

#include <sstream>


static unsigned int getRandomValueinRange(unsigned int v)
    return static_cast<unsigned int>((rand() * 1.0 * v)/(RAND_MAX-1))


program = osg.Program()
# show how to override the default RigTransformHardware for customized usage
class MyRigTransformHardware (osgAnimation.RigTransformHardware) :
void operator()(osgAnimation.RigGeometry geom)
        if _needInit :
            if !init(geom) :
                return
        computeMatrixPaletteUniform(geom.getMatrixFromSkeletonToGeometry(), geom.getInvMatrixFromSkeletonToGeometry())

    def init(geom):

        
        pos = dynamic_cast<osg.Vec3Array*>(geom.getVertexArray())
        if !pos : 
            osg.notify(osg.WARN), "RigTransformHardware no vertex array in the geometry ", geom.getName()
            return False

        if !geom.getSkeleton() : 
            osg.notify(osg.WARN), "RigTransformHardware no skeleting set in geometry ", geom.getName()
            return False

        mapVisitor = osgAnimation.BoneMapVisitor()
        geom.getSkeleton().accept(mapVisitor)
        bm = mapVisitor.getBoneMap()

        if !createPalette(pos.size(),bm, geom.getVertexInfluenceSet().getVertexToBoneList()) :
            return False

        attribIndex = 11
        nbAttribs = getNumVertexAttrib()

        # use a global program for all avatar
        if !program.valid() : 
            program = osg.Program()
            program.setName("HardwareSkinning")
            if !_shader.valid() :
                _shader = osg.Shader.readShaderFile(osg.Shader.VERTEX,"shaders/skinning.vert")

            if !_shader.valid() : 
                osg.notify(osg.WARN), "RigTransformHardware can't load VertexShader"
                return False

            # replace max matrix by the value from uniform
                str = _shader.getShaderSource()
                toreplace = str("MAX_MATRIX")
                start = str.find(toreplace)
                ss = strstream()
                ss, getMatrixPaletteUniform().getNumElements()
                str.replace(start, toreplace.size(), ss.str())
                _shader.setShaderSource(str)
                osg.notify(osg.INFO), "Shader ", str

            program.addShader(_shader.get())

            for (int i = 0 i < nbAttribs i++)
                ss = strstream()
                ss, "boneWeight", i
                program.addBindAttribLocation(ss.str(), attribIndex + i)

                osg.notify(osg.INFO), "set vertex attrib ", ss.str()
        for (int i = 0 i < nbAttribs i++)
            ss = strstream()
            ss, "boneWeight", i
            geom.setVertexAttribArray(attribIndex + i, getVertexAttrib(i))

        ss = osg.StateSet()
        ss.addUniform(getMatrixPaletteUniform())
        ss.addUniform(osg.Uniform("nbBonesPerVertex", getNumBonesPerVertex()))
        ss.setAttributeAndModes(program.get())
        geom.setStateSet(ss.get())
        _needInit = False
        return True




class SetupRigGeometry (osg.NodeVisitor) :
_hardware = bool()
    SetupRigGeometry( bool hardware = True) : osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN), _hardware(hardware) 
    
    def apply(geode):
    
        
        for (unsigned int i = 0 i < geode.getNumDrawables() i++)
            apply(*geode.getDrawable(i))
    def apply(geom):
        
        if _hardware : 
            rig = dynamic_cast<osgAnimation.RigGeometry*>(geom)
            if rig :
                rig.setRigTransformImplementation(MyRigTransformHardware)()

#if 0
        if geom.getName() != str("BoundingBox") : # we disable compute of bounding box for all geometry except our bounding box
            geom.setComputeBoundingBoxCallback(osg.Drawable.ComputeBoundingBoxCallback)()
#            geom.setInitialBound(osg.Drawable.ComputeBoundingBoxCallback)()
#endif


def createCharacterInstance(character, hardware):

    
    c = osg.Group()
    if hardware :
        c = osg.clone(character, osg.CopyOp.DEEP_COPY_ALL  ~osg.CopyOp.DEEP_COPY_PRIMITIVES  ~osg.CopyOp.DEEP_COPY_ARRAYS)
    c = osg.clone(character, osg.CopyOp.DEEP_COPY_ALL)

    animationManager = dynamic_cast<osgAnimation.AnimationManagerBase*>(c.getUpdateCallback())

    anim = dynamic_cast<osgAnimation.BasicAnimationManager*>(animationManager)
    list = animationManager.getAnimationList()
    v = getRandomValueinRange(list.size())
    if list[v].getName() == str("MatIpo_ipo") : 
        anim.playAnimation(list[v].get())
        v = (v + 1)%list.size()
        
    anim.playAnimation(list[v].get())

    switcher = SetupRigGeometry(hardware)
    c.accept(switcher)

    return c.release()


int main (int argc, char* argv[])
    std.cerr, "This example works better with nathan.osg"

    psr = osg.ArgumentParser(argc, argv)

    viewer = osgViewer.Viewer(psr)

    hardware = True
    maxChar = 10
    while psr.read("--software") :  hardware = False 
    while psr.read("--number", maxChar) : 


    root = dynamic_cast<osg.Group*>(osgDB.readNodeFiles(psr))
    if !root : 
        print psr.getApplicationName(), ": No data loaded"
        return 1

        animationManager = dynamic_cast<osgAnimation.AnimationManagerBase*>(root.getUpdateCallback())
        if !animationManager : 
            osg.notify(osg.FATAL), "no AnimationManagerBase found, updateCallback need to animate elements"
            return 1


    scene = osg.Group()

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    
    # add the thread model handler
    viewer.addEventHandler(osgViewer.ThreadingHandler)()

    # add the window size toggle handler
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()
        
    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add the help handler
    viewer.addEventHandler(osgViewer.HelpHandler(psr.getApplicationUsage()))

    # add the LOD Scale handler
    viewer.addEventHandler(osgViewer.LODScaleHandler)()

    # add the screen capture handler
    viewer.addEventHandler(osgViewer.ScreenCaptureHandler)()

    viewer.setSceneData(scene.get())

    viewer.realize()

    xChar = maxChar
    yChar = xChar * 9.0/16
    for (double  i = 0.0 i < xChar i++) 
        for (double  j = 0.0 j < yChar j++) 

            c = createCharacterInstance(root.get(), hardware)
            tr = osg.MatrixTransform()
            tr.setMatrix(osg.Matrix.translate( 2.0 * (i - xChar * .5),
                                                  0.0,
                                                  2.0 * (j - yChar * .5)))
            tr.addChild(c.get())
            scene.addChild(tr)
    print "created ", xChar * yChar, " instance"


    return viewer.run()




if __name__ == "__main__":
    main(sys.argv)
