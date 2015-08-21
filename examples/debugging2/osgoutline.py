#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgoutline"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgFX
from osgpypp import osgViewer


# Translated from file 'osgoutline.cpp'

# -*-c++-*-

#
# * Draw an outline around a model.
# 

#include <osg/Group>
#include <osg/PositionAttitudeTransform>

#include <osgDB/ReadFile>
#include <osgViewer/Viewer>

#include <osgFX/Outline>


def main(argv):


    
    arguments = osg.ArgumentParser(argv)
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] <file>")
    arguments.getApplicationUsage().addCommandLineOption("--testOcclusion","Test occlusion by other objects")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")

    testOcclusion = False
    while arguments.read("--testOcclusion") :  testOcclusion = True 

    # load outlined object
    modelFilename = "dumptrick.osgt"
    if arguments.argc() > 2:
         modelFileName = arguments[2]
    outlineModel = osgDB.readNodeFile(modelFilename)
    if  not outlineModel :
        osg.notify(osg.FATAL) << "Unable to load model '" <<  modelFilename << "'\n"
        return -1

    # create scene
    root = osg.Group()

    # create outline effect
    outline = osgFX.Outline()
    root.addChild(outline)

    outline.setWidth(8)
    outline.setColor(osg.Vec4(1,1,0,1))
    outline.addChild(outlineModel)

    if testOcclusion :
        # load occluder
        occludedModelFilename = "cow.osgt"
        occludedModel = osgDB.readNodeFile(occludedModelFilename)
        if  not occludedModel :
            osg.notify(osg.FATAL), "Unable to load model '", occludedModelFilename, "'\n"
            return -1

        # occluder offset
        bsphere = outlineModel.getBound()
        occluderOffset = osg.Vec3(0,1,0) * bsphere.radius() * 1.2

        # occluder behind outlined model
        modelTransform0 = osg.PositionAttitudeTransform()
        modelTransform0.setPosition(bsphere.center() + occluderOffset)
        modelTransform0.addChild(occludedModel)
        root.addChild(modelTransform0)

        # occluder in front of outlined model
        modelTransform1 = osg.PositionAttitudeTransform()
        modelTransform1.setPosition(bsphere.center() - occluderOffset)
        modelTransform1.addChild(occludedModel)
        root.addChild(modelTransform1)

    # must have stencil buffer...
    osg.DisplaySettings.instance().setMinimumNumStencilBits(1)

    # construct the viewer
    viewer = osgViewer.Viewer()
    viewer.setSceneData(root)

    # must clear stencil buffer...
    clearMask = viewer.getCamera().getClearMask()
    viewer.getCamera().setClearMask(clearMask | GL_STENCIL_BUFFER_BIT)
    viewer.getCamera().setClearStencil(0)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
