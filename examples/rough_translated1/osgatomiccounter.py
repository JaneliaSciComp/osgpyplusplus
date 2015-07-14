#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgatomiccounter"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgatomiccounter.cpp'

# -*-c++-*- OpenSceneGraph - Copyright (C) 2012-2012 David Callu
# *
# * This application is open source and may be redistributed and/or modified
# * freely and without restriction, both in commercial and non commercial applications,
# * as long as this copyright notice is maintained.
# *
# * This application is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

#include <osg/BufferIndexBinding>
#include <osg/BufferObject>
#include <osg/Camera>
#include <osg/Program>

#include <osgDB/ReadFile>
#include <osgUtil/Optimizer>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>
#include <osgGA/SphericalManipulator>

#include <iostream>


class AdaptNumPixelUniform (osg.Camera.DrawCallback) :
        AdaptNumPixelUniform()
            _atomicCounterArray = osg.UIntArray()
            _atomicCounterArray.push_back(0)

        virtual void operator () (osg.RenderInfo renderInfo) 
            _acbb.readData(*renderInfo.getState(), *_atomicCounterArray)
            numPixel = osg.maximum(1u, _atomicCounterArray.front())

            if renderInfo.getView().getFrameStamp().getFrameNumber() % 10 : == 0 :
                OSG_INFO, "osgatomiccounter : draw ", numPixel, " pixels."

            _invNumPixelUniform.set( 1.0 / static_cast<float>(numPixel) )

        _invNumPixelUniform = osg.Uniform()
        _atomicCounterArray = osg.UIntArray()
        _acbb = osg.AtomicCounterBufferBinding()



def createProgram():


    

  vp = strstream()
  vp, "#version 420 compatibility\n", "\n", "void main(void)\n", "\n", "    gl_Position = ftransform()\n", "\n"
  vpShader = osg.Shader( osg.Shader.VERTEX, vp.str() )



  fp = strstream()
  fp, "#version 420 compatibility\n", "\n", "layout(binding = 0) uniform atomic_uint acRed\n", "layout(binding = 0, offset = 4) uniform atomic_uint acGreen\n", "layout(binding = 2) uniform atomic_uint acBlue\n", "\n", "uniform float invNumPixel\n", "\n", "void main(void)\n", "\n", "    float r = float(atomicCounterIncrement(acRed)) * invNumPixel\n", "    float g = float(atomicCounterIncrement(acGreen)) * invNumPixel\n", "    float b = float(atomicCounterIncrement(acBlue)) * invNumPixel\n", "    gl_FragColor = vec4(r, g, b, 1.0)\n", "\n", "\n"
  fpShader = osg.Shader( osg.Shader.FRAGMENT, fp.str() )

  program = osg.Program()
  program.addShader(vpShader)
  program.addShader(fpShader)

  return program

class ResetAtomicCounter (osg.StateAttributeCallback) :
        virtual void operator () (osg.StateAttribute* sa, osg.NodeVisitor*)
            acbb = dynamic_cast<osg.AtomicCounterBufferBinding *>(sa)
            if acbb :
                acbo = dynamic_cast<osg.AtomicCounterBufferObject*>(acbb.getBufferObject())
                if acbo  and  acbo.getBufferData(0) :
                    acbo.getBufferData(0).dirty()



def main(argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is a simple example which show draw order of pixel.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")

    viewer = osgViewer.Viewer(arguments)

    helpType = 0
    if helpType = arguments.readHelpType() : :
        arguments.getApplicationUsage().write(std.cout, helpType)
        return 1

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    # set up the camera manipulators.
    viewer.setCameraManipulator( osgGA.TrackballManipulator() )

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    # add the thread model handler
    viewer.addEventHandler(osgViewer.ThreadingHandler)()

    # add the window size toggle handler
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add the help handler
    viewer.addEventHandler(osgViewer.HelpHandler(arguments.getApplicationUsage()))

    # add the screen capture handler
    viewer.addEventHandler(osgViewer.ScreenCaptureHandler)()

    # load the data
    loadedModel = osgDB.readNodeFiles(arguments)
    if  not loadedModel :
        quad = osg.createTexturedQuadGeometry(osg.Vec3f(-2.0, 0.0, -2.0),
                                                          osg.Vec3f(2.0, 0.0, 0.0),
                                                          osg.Vec3f(0.0, 0.0, 2.0) )

        geode = osg.Geode()
        geode.addDrawable(quad)
        loadedModel = geode

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1


    ss = loadedModel.asGeode().getDrawable(0).getOrCreateStateSet()
    ss.setAttributeAndModes( createProgram(), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE | osg.StateAttribute.PROTECTED )

    ss = loadedModel.getOrCreateStateSet()
    atomicCounterArrayRedAndGreen = osg.UIntArray()
    atomicCounterArrayRedAndGreen.push_back(0)
    atomicCounterArrayRedAndGreen.push_back(0)

    atomicCounterArrayBlue = osg.UIntArray()
    atomicCounterArrayBlue.push_back(0)

    acboRedAndGreen = osg.AtomicCounterBufferObject()
    acboRedAndGreen.setUsage(GL_STREAM_COPY)
    atomicCounterArrayRedAndGreen.setBufferObject(acboRedAndGreen)

    acboBlue = osg.AtomicCounterBufferObject()
    acboBlue.setUsage(GL_STREAM_COPY)
    atomicCounterArrayBlue.setBufferObject(acboBlue)

    acbbRedAndGreen = osg.AtomicCounterBufferBinding(0, acboRedAndGreen, 0, sizeof(GLuint)*3)
    ss.setAttributeAndModes(acbbRedAndGreen)

    acbbBlue = osg.AtomicCounterBufferBinding(2, acboBlue, 0, sizeof(GLuint))
    ss.setAttributeAndModes(acbbBlue)

    acbbRedAndGreen.setUpdateCallback(ResetAtomicCounter)()
    acbbBlue.setUpdateCallback(ResetAtomicCounter)()

    invNumPixelUniform = osg.Uniform("invNumPixel", 1.0/(800.0*600.0))
    ss.addUniform( invNumPixelUniform )

    drawCallback = AdaptNumPixelUniform()
    drawCallback._invNumPixelUniform = invNumPixelUniform
    drawCallback._acbb = acbbBlue

    viewer.getCamera().setFinalDrawCallback(drawCallback)

    # optimize the scene graph, remove redundant nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel)

    viewer.setSceneData( loadedModel )

    viewer.realize()

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
