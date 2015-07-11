#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgoutline"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgFX
from osgpypp import osgViewer

# -*-c++-*-

#
 * Draw an outline around a model.
 

#include <osg/Group>
#include <osg/PositionAttitudeTransform>

#include <osgDB/ReadFile>
#include <osgViewer/Viewer>

#include <osgFX/Outline>


def main(argc, argv):
    arguments = osg.ArgumentParser(argc,argv)
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] <file>")
    arguments.getApplicationUsage().addCommandLineOption("--testOcclusion","Test occlusion by other objects")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")

    testOcclusion =  false
    while arguments.read("--testOcclusion") :  testOcclusion = true 

    # load outlined object
    modelFilename =  arguments.argc() > 1 ? arguments[1] : "dumptruck.osgt"
    osg.ref_ptr<osg.Node> outlineModel = osgDB.readNodeFile(modelFilename)
    if !outlineModel :
        osg.notify(osg.FATAL), "Unable to load model '", modelFilename, "'\n"
        return -1

    # create scene
    osg.ref_ptr<osg.Group> root = new osg.Group

        # create outline effect
        osg.ref_ptr<osgFX.Outline> outline = new osgFX.Outline
        root.addChild(outline.get())

        outline.setWidth(8)
        outline.setColor(osg.Vec4(1,1,0,1))
        outline.addChild(outlineModel.get())

    if testOcclusion :
        # load occluder
        occludedModelFilename =  "cow.osgt"
        osg.ref_ptr<osg.Node> occludedModel = osgDB.readNodeFile(occludedModelFilename)
        if !occludedModel :
            osg.notify(osg.FATAL), "Unable to load model '", occludedModelFilename, "'\n"
            return -1

        # occluder offset
        bsphere =  outlineModel.getBound()
        occluderOffset =  osg.Vec3(0,1,0) * bsphere.radius() * 1.2f

        # occluder behind outlined model
        osg.ref_ptr<osg.PositionAttitudeTransform> modelTransform0 = new osg.PositionAttitudeTransform
        modelTransform0.setPosition(bsphere.center() + occluderOffset)
        modelTransform0.addChild(occludedModel.get())
        root.addChild(modelTransform0.get())

        # occluder in front of outlined model
        osg.ref_ptr<osg.PositionAttitudeTransform> modelTransform1 = new osg.PositionAttitudeTransform
        modelTransform1.setPosition(bsphere.center() - occluderOffset)
        modelTransform1.addChild(occludedModel.get())
        root.addChild(modelTransform1.get())

    # must have stencil buffer...
    osg.DisplaySettings.instance().setMinimumNumStencilBits(1)

    # construct the viewer
    viewer = osgViewer.Viewer()
    viewer.setSceneData(root.get())

    # must clear stencil buffer...
    unsigned int clearMask = viewer.getCamera().getClearMask()
    viewer.getCamera().setClearMask(clearMask | GL_STENCIL_BUFFER_BIT)
    viewer.getCamera().setClearStencil(0)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)