#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osggameoflife"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer

# OpenSceneGraph example, osggameoflife.
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


#include "GameOfLifePass.h"
#include <osgDB/FileUtils>
#include <iostream>

ProcessPass.ProcessPass(osg.TextureRectangle *in_tex,
                         osg.TextureRectangle *out_tex,
                         int width, int height):
    _TextureWidth(width),
    _TextureHeight(height)
    _RootGroup = new osg.Group

    _InTexture = in_tex
    _OutTexture = out_tex

    _Camera = new osg.Camera
    setupCamera()
    _Camera.addChild(createTexturedQuad().get())

    _RootGroup.addChild(_Camera.get())

    setShader("shaders/gameoflife.frag")

ProcessPass.~ProcessPass()

osg.ref_ptr<osg.Group> ProcessPass.createTexturedQuad()
    osg.ref_ptr<osg.Group> top_group = new osg.Group

    osg.ref_ptr<osg.Geode> quad_geode = new osg.Geode

    osg.ref_ptr<osg.Vec3Array> quad_coords = new osg.Vec3Array # vertex coords
    # counter-clockwise
    quad_coords.push_back(osg.Vec3d(0, 0, -1))
    quad_coords.push_back(osg.Vec3d(1, 0, -1))
    quad_coords.push_back(osg.Vec3d(1, 1, -1))
    quad_coords.push_back(osg.Vec3d(0, 1, -1))

    osg.ref_ptr<osg.Vec2Array> quad_tcoords = new osg.Vec2Array # texture coords
    quad_tcoords.push_back(osg.Vec2(0, 0))
    quad_tcoords.push_back(osg.Vec2(_TextureWidth, 0))
    quad_tcoords.push_back(osg.Vec2(_TextureWidth, _TextureHeight))
    quad_tcoords.push_back(osg.Vec2(0, _TextureHeight))

    osg.ref_ptr<osg.Geometry> quad_geom = new osg.Geometry
    osg.ref_ptr<osg.DrawArrays> quad_da = new osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4)

    osg.ref_ptr<osg.Vec4Array> quad_colors = new osg.Vec4Array
    quad_colors.push_back(osg.Vec4(1.0f,1.0f,1.0f,1.0f))

    quad_geom.setVertexArray(quad_coords.get())
    quad_geom.setTexCoordArray(0, quad_tcoords.get())
    quad_geom.addPrimitiveSet(quad_da.get())
    quad_geom.setColorArray(quad_colors.get(), osg.Array.BIND_OVERALL)

    _StateSet = quad_geom.getOrCreateStateSet()
    _StateSet.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
    _StateSet.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)

    _StateSet.setTextureAttributeAndModes(0, _InTexture.get(), osg.StateAttribute.ON)

    _StateSet.addUniform(new osg.Uniform("textureIn", 0))

    quad_geode.addDrawable(quad_geom.get())

    top_group.addChild(quad_geode.get())

    top_group = return()

void ProcessPass.setupCamera()
    # clearing
    _Camera.setClearMask(GL_DEPTH_BUFFER_BIT)

    # projection and view
    _Camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1,0,1))
    _Camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    _Camera.setViewMatrix(osg.Matrix.identity())

    # viewport
    _Camera.setViewport(0, 0, _TextureWidth, _TextureHeight)

    _Camera.setRenderOrder(osg.Camera.PRE_RENDER)
    _Camera.setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

    _Camera.attach(osg.Camera.BufferComponent(osg.Camera.COLOR_BUFFER), _OutTexture.get())

void ProcessPass.setShader(str filename)
    foundFile =  osgDB.findDataFile(filename)
    if foundFile.empty() :
        osg.notify(osg.NOTICE), "Could not file shader file: ", filename
        return

    osg.ref_ptr<osg.Shader> fshader = new osg.Shader( osg.Shader.FRAGMENT )
    fshader.loadShaderSourceFromFile(foundFile)

    _FragmentProgram = 0
    _FragmentProgram = new osg.Program

    _FragmentProgram.addShader(fshader.get())

    _StateSet.setAttributeAndModes(_FragmentProgram.get(), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )

####################################

GameOfLifePass.GameOfLifePass(osg.Image *in_image)
    _TextureWidth = in_image.s()
    _TextureHeight = in_image.t()

    _RootGroup = new osg.Group

    _BranchSwith[0] = new osg.Switch
    _BranchSwith[1] = new osg.Switch

    _RootGroup.addChild(_BranchSwith[0].get())
    _RootGroup.addChild(_BranchSwith[1].get())

    _ActiveBranch = 0
    activateBranch()

    createOutputTextures()
    _InOutTextureLife[0].setImage(in_image)

    _ProcessPass[0] = new ProcessPass(_InOutTextureLife[0].get(),
                                      _InOutTextureLife[1].get(),
                                      _TextureWidth, _TextureHeight)

    # For the other pass, the input/output textures are flipped
    _ProcessPass[1] = new ProcessPass(_InOutTextureLife[1].get(),
                                      _InOutTextureLife[0].get(),
                                      _TextureWidth, _TextureHeight)

    _BranchSwith[0].addChild(_ProcessPass[0].getRoot().get())
    _BranchSwith[1].addChild(_ProcessPass[1].getRoot().get())

GameOfLifePass.~GameOfLifePass()
    delete _ProcessPass[0]
    delete _ProcessPass[1]

osg.ref_ptr<osg.TextureRectangle> GameOfLifePass.getOutputTexture()
    out_tex =  (_ActiveBranch == 0) ? 1 : 0
    return _ProcessPass[out_tex].getOutputTexture()

void GameOfLifePass.activateBranch()
    onb =  _ActiveBranch
    offb =  (onb == 1) ? 0 : 1

    _BranchSwith[onb].setAllChildrenOn()
    _BranchSwith[offb].setAllChildrenOff()

void GameOfLifePass.flip()
    _ActiveBranch = (_ActiveBranch == 1) ? 0 : 1
    activateBranch()

void GameOfLifePass.createOutputTextures()
    for (int i=0 i<2 i++) 
        _InOutTextureLife[i] = new osg.TextureRectangle

        _InOutTextureLife[i].setTextureSize(_TextureWidth, _TextureHeight)
        _InOutTextureLife[i].setInternalFormat(GL_RGBA)
        _InOutTextureLife[i].setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.NEAREST)
        _InOutTextureLife[i].setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.NEAREST)

# OpenSceneGraph example, osggameoflife.
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


#ifndef GAMEOFLIFEPASS_H
#define GAMEOFLIFEPASS_H 1

#include <osg/ref_ptr>
#include <osg/Group>
#include <osg/Switch>
#include <osg/Camera>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Texture2D>
#include <osg/TextureRectangle>

class ProcessPass 
  public:
    ProcessPass(osg.TextureRectangle *in_tex,
                osg.TextureRectangle *out_tex,
                int width, int height)
    ~ProcessPass()
    osg.ref_ptr<osg.Group> getRoot()  return _RootGroup 
    osg.ref_ptr<osg.TextureRectangle> getOutputTexture()  return _OutTexture 
    setShader = void(str filename)
    
  private:
    osg.ref_ptr<osg.Group> createTexturedQuad()
    setupCamera = void()

    osg.ref_ptr<osg.Group> _RootGroup
    osg.ref_ptr<osg.Camera> _Camera
    osg.ref_ptr<osg.TextureRectangle> _InTexture
    osg.ref_ptr<osg.TextureRectangle> _OutTexture
    _TextureWidth = int()
    _TextureHeight = int()
    osg.ref_ptr<osg.Program> _FragmentProgram
    osg.ref_ptr<osg.StateSet> _StateSet


class GameOfLifePass 
  public:
    GameOfLifePass(osg.Image *in_image)
    ~GameOfLifePass()
    osg.ref_ptr<osg.Group> getRoot()  return _RootGroup 
    osg.ref_ptr<osg.TextureRectangle> getOutputTexture()
    setShader = void(str filename)
    # Switch branches so we flip textures
    flip = void()

  private:
    osg.ref_ptr<osg.Group> createTexturedQuad()
    setupCamera = void()
    createOutputTextures = void()
    activateBranch = void()
    
    osg.ref_ptr<osg.Group> _RootGroup
    osg.ref_ptr<osg.Camera> _Camera
    osg.ref_ptr<osg.TextureRectangle> _InOutTextureLife[2]
    _TextureWidth = int()
    _TextureHeight = int()
    _ActiveBranch = int()
    osg.ref_ptr<osg.Program> _FragmentProgram
    osg.ref_ptr<osg.StateSet> _StateSet
    osg.ref_ptr<osg.Switch> _BranchSwith[2]
    ProcessPass *_ProcessPass[2]


#endif #GAMEOFLIFEPASS_H
# OpenSceneGraph example, osggameoflife.
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


#include <osg/Vec3>
#include <osg/Vec4>
#include <osg/Geometry>
#include <osg/Geode>
#include <osg/TextureRectangle>

#include <osgDB/FileUtils>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>

#include <iostream>

#include "GameOfLifePass.h"

*golpass = GameOfLifePass()
osg.ref_ptr<osg.StateSet> geomss # stateset where we can attach textures

def createScene(start_im):
    width =  start_im.s()
    height =  start_im.t()

    topnode =  new osg.Group

    # create quad to display image on
    osg.ref_ptr<osg.Geode> geode = new osg.Geode()

    # each geom will contain a quad
    osg.ref_ptr<osg.DrawArrays> da = new osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4)

    osg.ref_ptr<osg.Vec4Array> colors = new osg.Vec4Array
    colors.push_back(osg.Vec4(1.0f,1.0f,1.0f,1.0f))

    osg.ref_ptr<osg.Vec2Array> tcoords = new osg.Vec2Array # texture coords
    tcoords.push_back(osg.Vec2(0, 0))
    tcoords.push_back(osg.Vec2(width, 0))
    tcoords.push_back(osg.Vec2(width, height))
    tcoords.push_back(osg.Vec2(0, height))

    osg.ref_ptr<osg.Vec3Array> vcoords = new osg.Vec3Array # vertex coords
    osg.ref_ptr<osg.Geometry> geom = new osg.Geometry

    # initial viewer camera looks along y
    vcoords.push_back(osg.Vec3d(0, 0, 0))
    vcoords.push_back(osg.Vec3d(width, 0, 0))
    vcoords.push_back(osg.Vec3d(width, 0, height))
    vcoords.push_back(osg.Vec3d(0, 0, height))

    geom.setVertexArray(vcoords.get())
    geom.setTexCoordArray(0,tcoords.get())
    geom.addPrimitiveSet(da.get())
    geom.setColorArray(colors.get(), osg.Array.BIND_OVERALL)
    geomss = geom.getOrCreateStateSet()
    geomss.setMode(GL_LIGHTING, osg.StateAttribute.OFF)

    geode.addDrawable(geom.get())

    topnode.addChild(geode.get())

    # create the ping pong processing passes
    golpass = new GameOfLifePass(start_im)
    topnode.addChild(golpass.getRoot().get())

    # attach the output of the processing to the geom
    geomss.setTextureAttributeAndModes(0,
                                        golpass.getOutputTexture().get(),
                                        osg.StateAttribute.ON)
    topnode = return()

int main(int argc, char *argv[])
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates ping pong rendering with FBOs and mutliple rendering branches. It uses Conway's Game of Life to illustrate the concept.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] --startim start_image")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--startim","The initial image to seed the game of life with.")

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    startName = str("")
    while arguments.read("--startim", startName) : 

    if startName == "" : 
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # load the image
    osg.ref_ptr<osg.Image> startIm = osgDB.readImageFile(startName)

    if !startIm : 
        print "Could not load start image.\n"
        return(1)

    scene =  createScene(startIm.get())

    # construct the viewer.
    viewer = osgViewer.Viewer()
    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # add the stats handler
    viewer.addEventHandler(new osgViewer.StatsHandler)

    viewer.setSceneData(scene)

    viewer.realize()
    viewer.setCameraManipulator( new osgGA.TrackballManipulator )

    while !viewer.done() :
        viewer.frame()
        # flip the textures after we've completed a frame
        golpass.flip()
        # attach the proper output to view
        geomss.setTextureAttributeAndModes(0,
                                            golpass.getOutputTexture().get(),
                                            osg.StateAttribute.ON)

    return 0


if __name__ == "__main__":
    main(sys.argv)
