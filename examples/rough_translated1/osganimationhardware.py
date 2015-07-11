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

#  -*-c++-*- 
 *  Copyright (C) 2009 Cedric Pinson <cedric.pinson@plopbyte.net>
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


osg.ref_ptr<osg.Program> program
# show how to override the default RigTransformHardware for customized usage
struct MyRigTransformHardware : public osgAnimation.RigTransformHardware

    void operator()(osgAnimation.RigGeometry geom)
        if _needInit :
            if !init(geom) :
                return
        computeMatrixPaletteUniform(geom.getMatrixFromSkeletonToGeometry(), geom.getInvMatrixFromSkeletonToGeometry())

    def init(geom):
        pos =  dynamic_cast<osg.Vec3Array*>(geom.getVertexArray())
        if !pos : 
            osg.notify(osg.WARN), "RigTransformHardware no vertex array in the geometry ", geom.getName()
            false = return()

        if !geom.getSkeleton() : 
            osg.notify(osg.WARN), "RigTransformHardware no skeleting set in geometry ", geom.getName()
            false = return()

        mapVisitor = osgAnimation.BoneMapVisitor()
        geom.getSkeleton().accept(mapVisitor)
        bm =  mapVisitor.getBoneMap()

        if !createPalette(pos.size(),bm, geom.getVertexInfluenceSet().getVertexToBoneList()) :
            false = return()

        attribIndex =  11
        nbAttribs =  getNumVertexAttrib()

        # use a global program for all avatar
        if !program.valid() : 
            program = new osg.Program
            program.setName("HardwareSkinning")
            if !_shader.valid() :
                _shader = osg.Shader.readShaderFile(osg.Shader.VERTEX,"shaders/skinning.vert")

            if !_shader.valid() : 
                osg.notify(osg.WARN), "RigTransformHardware can't load VertexShader"
                false = return()

            # replace max matrix by the value from uniform
                str =  _shader.getShaderSource()
                toreplace =  str("MAX_MATRIX")
                start =  str.find(toreplace)
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

        osg.ref_ptr<osg.StateSet> ss = new osg.StateSet
        ss.addUniform(getMatrixPaletteUniform())
        ss.addUniform(new osg.Uniform("nbBonesPerVertex", getNumBonesPerVertex()))
        ss.setAttributeAndModes(program.get())
        geom.setStateSet(ss.get())
        _needInit = false
        true = return()




struct SetupRigGeometry : public osg.NodeVisitor
    _hardware = bool()
    SetupRigGeometry( bool hardware = true) : osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN), _hardware(hardware) 
    
    def apply(geode):
        for (unsigned int i = 0 i < geode.getNumDrawables() i++)
            apply(*geode.getDrawable(i))
    def apply(geom):
        if _hardware : 
            rig =  dynamic_cast<osgAnimation.RigGeometry*>(geom)
            if rig :
                rig.setRigTransformImplementation(new MyRigTransformHardware)

#if 0
        if geom.getName() != str("BoundingBox") : # we disable compute of bounding box for all geometry except our bounding box
            geom.setComputeBoundingBoxCallback(new osg.Drawable.ComputeBoundingBoxCallback)
#            geom.setInitialBound(new osg.Drawable.ComputeBoundingBoxCallback)
#endif


def createCharacterInstance(character, hardware):
    osg.ref_ptr<osg.Group> c 
    if hardware :
        c = osg.clone(character, osg.CopyOp.DEEP_COPY_ALL  ~osg.CopyOp.DEEP_COPY_PRIMITIVES  ~osg.CopyOp.DEEP_COPY_ARRAYS)
    c =  osg.clone(character, osg.CopyOp.DEEP_COPY_ALL)

    animationManager =  dynamic_cast<osgAnimation.AnimationManagerBase*>(c.getUpdateCallback())

    anim =  dynamic_cast<osgAnimation.BasicAnimationManager*>(animationManager)
    list =  animationManager.getAnimationList()
    v =  getRandomValueinRange(list.size())
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

    hardware =  true
    maxChar =  10
    while psr.read("--software") :  hardware = false 
    while psr.read("--number", maxChar) : 


    osg.ref_ptr<osg.Group> root = dynamic_cast<osg.Group*>(osgDB.readNodeFiles(psr))
    if !root : 
        print psr.getApplicationName(), ": No data loaded"
        return 1

        animationManager =  dynamic_cast<osgAnimation.AnimationManagerBase*>(root.getUpdateCallback())
        if !animationManager : 
            osg.notify(osg.FATAL), "no AnimationManagerBase found, updateCallback need to animate elements"
            return 1


    osg.ref_ptr<osg.Group> scene = new osg.Group

    # add the state manipulator
    viewer.addEventHandler( new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    
    # add the thread model handler
    viewer.addEventHandler(new osgViewer.ThreadingHandler)

    # add the window size toggle handler
    viewer.addEventHandler(new osgViewer.WindowSizeHandler)
        
    # add the stats handler
    viewer.addEventHandler(new osgViewer.StatsHandler)

    # add the help handler
    viewer.addEventHandler(new osgViewer.HelpHandler(psr.getApplicationUsage()))

    # add the LOD Scale handler
    viewer.addEventHandler(new osgViewer.LODScaleHandler)

    # add the screen capture handler
    viewer.addEventHandler(new osgViewer.ScreenCaptureHandler)

    viewer.setSceneData(scene.get())

    viewer.realize()

    xChar =  maxChar
    yChar =  xChar * 9.0/16
    for (double  i = 0.0 i < xChar i++) 
        for (double  j = 0.0 j < yChar j++) 

            osg.ref_ptr<osg.Group> c = createCharacterInstance(root.get(), hardware)
            tr =  new osg.MatrixTransform
            tr.setMatrix(osg.Matrix.translate( 2.0 * (i - xChar * .5),
                                                  0.0,
                                                  2.0 * (j - yChar * .5)))
            tr.addChild(c.get())
            scene.addChild(tr)
    print "created ", xChar * yChar, " instance"


    return viewer.run()




if __name__ == "__main__":
    main(sys.argv)
