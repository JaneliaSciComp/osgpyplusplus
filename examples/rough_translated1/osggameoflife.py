#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osggameoflife"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'GameOfLifePass.cpp'

# OpenSceneGraph example, osggameoflife.
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

#include "GameOfLifePass.h"
#include <osgDB/FileUtils>
#include <iostream>

ProcessPass.ProcessPass(osg.TextureRectangle *in_tex,
                         osg.TextureRectangle *out_tex,
                         int width, int height):
    _TextureWidth(width),
    _TextureHeight(height)
    _RootGroup = osg.Group()

    _InTexture = in_tex
    _OutTexture = out_tex

    _Camera = osg.Camera()
    setupCamera()
    _Camera.addChild(createTexturedQuad())

    _RootGroup.addChild(_Camera)

    setShader("shaders/gameoflife.frag")

ProcessPass.~ProcessPass()

osg.Group ProcessPass.createTexturedQuad()
    top_group = osg.Group()

    quad_geode = osg.Geode()

    quad_coords = osg.Vec3Array() # vertex coords
    # counter-clockwise
    quad_coords.push_back(osg.Vec3d(0, 0, -1))
    quad_coords.push_back(osg.Vec3d(1, 0, -1))
    quad_coords.push_back(osg.Vec3d(1, 1, -1))
    quad_coords.push_back(osg.Vec3d(0, 1, -1))

    quad_tcoords = osg.Vec2Array() # texture coords
    quad_tcoords.push_back(osg.Vec2(0, 0))
    quad_tcoords.push_back(osg.Vec2(_TextureWidth, 0))
    quad_tcoords.push_back(osg.Vec2(_TextureWidth, _TextureHeight))
    quad_tcoords.push_back(osg.Vec2(0, _TextureHeight))

    quad_geom = osg.Geometry()
    quad_da = osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4)

    quad_colors = osg.Vec4Array()
    quad_colors.push_back(osg.Vec4(1.0,1.0,1.0,1.0))

    quad_geom.setVertexArray(quad_coords)
    quad_geom.setTexCoordArray(0, quad_tcoords)
    quad_geom.addPrimitiveSet(quad_da)
    quad_geom.setColorArray(quad_colors, osg.Array.BIND_OVERALL)

    _StateSet = quad_geom.getOrCreateStateSet()
    _StateSet.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
    _StateSet.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)

    _StateSet.setTextureAttributeAndModes(0, _InTexture, osg.StateAttribute.ON)

    _StateSet.addUniform(osg.Uniform("textureIn", 0))

    quad_geode.addDrawable(quad_geom)

    top_group.addChild(quad_geode)

    return top_group

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

    _Camera.attach(osg.Camera.BufferComponent(osg.Camera.COLOR_BUFFER), _OutTexture)

void ProcessPass.setShader(str filename)
    foundFile = osgDB.findDataFile(filename)
    if foundFile.empty() :
        osg.notify(osg.NOTICE), "Could not file shader file: ", filename
        return

    fshader = osg.Shader( osg.Shader.FRAGMENT )
    fshader.loadShaderSourceFromFile(foundFile)

    _FragmentProgram = 0
    _FragmentProgram = osg.Program()

    _FragmentProgram.addShader(fshader)

    _StateSet.setAttributeAndModes(_FragmentProgram, osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )

####################################

GameOfLifePass.GameOfLifePass(osg.Image *in_image)
    _TextureWidth = in_image.s()
    _TextureHeight = in_image.t()

    _RootGroup = osg.Group()

    _BranchSwith[0] = osg.Switch()
    _BranchSwith[1] = osg.Switch()

    _RootGroup.addChild(_BranchSwith[0])
    _RootGroup.addChild(_BranchSwith[1])

    _ActiveBranch = 0
    activateBranch()

    createOutputTextures()
    _InOutTextureLife[0].setImage(in_image)

    _ProcessPass[0] = ProcessPass(_InOutTextureLife[0],
                                      _InOutTextureLife[1],
                                      _TextureWidth, _TextureHeight)

    # For the other pass, the input/output textures are flipped
    _ProcessPass[1] = ProcessPass(_InOutTextureLife[1],
                                      _InOutTextureLife[0],
                                      _TextureWidth, _TextureHeight)

    _BranchSwith[0].addChild(_ProcessPass[0].getRoot())
    _BranchSwith[1].addChild(_ProcessPass[1].getRoot())

GameOfLifePass.~GameOfLifePass()
    delete _ProcessPass[0]
    delete _ProcessPass[1]

osg.TextureRectangle GameOfLifePass.getOutputTexture()
    out_tex =  1 if ((_ActiveBranch == 0)) else  0
    return _ProcessPass[out_tex].getOutputTexture()

void GameOfLifePass.activateBranch()
    onb = _ActiveBranch
    offb =  0 if ((onb == 1)) else  1

    _BranchSwith[onb].setAllChildrenOn()
    _BranchSwith[offb].setAllChildrenOff()

void GameOfLifePass.flip()
    _ActiveBranch =  0 if ((_ActiveBranch == 1)) else  1
    activateBranch()

void GameOfLifePass.createOutputTextures()
    for (int i=0 i<2 i++) 
        _InOutTextureLife[i] = osg.TextureRectangle()

        _InOutTextureLife[i].setTextureSize(_TextureWidth, _TextureHeight)
        _InOutTextureLife[i].setInternalFormat(GL_RGBA)
        _InOutTextureLife[i].setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.NEAREST)
        _InOutTextureLife[i].setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.NEAREST)


# Translated from file 'GameOfLifePass.h'

# OpenSceneGraph example, osggameoflife.
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

class ProcessPass :
    ProcessPass(osg.TextureRectangle *in_tex,
                osg.TextureRectangle *out_tex,
                int width, int height)
    ~ProcessPass()
    def getRoot():
         return _RootGroup 
    def getOutputTexture():
         return _OutTexture 
    setShader = void(str filename)
    createTexturedQuad = osg.Group()
    setupCamera = void()

    _RootGroup = osg.Group()
    _Camera = osg.Camera()
    _InTexture = osg.TextureRectangle()
    _OutTexture = osg.TextureRectangle()
    _TextureWidth = int()
    _TextureHeight = int()
    _FragmentProgram = osg.Program()
    _StateSet = osg.StateSet()


class GameOfLifePass :
    GameOfLifePass(osg.Image *in_image)
    ~GameOfLifePass()
    def getRoot():
         return _RootGroup 
    getOutputTexture = osg.TextureRectangle()
    setShader = void(str filename)
    # Switch branches so we flip textures
    flip = void()
    createTexturedQuad = osg.Group()
    setupCamera = void()
    createOutputTextures = void()
    activateBranch = void()
    
    _RootGroup = osg.Group()
    _Camera = osg.Camera()
    osg.TextureRectangle _InOutTextureLife[2]
    _TextureWidth = int()
    _TextureHeight = int()
    _ActiveBranch = int()
    _FragmentProgram = osg.Program()
    _StateSet = osg.StateSet()
    osg.Switch _BranchSwith[2]
    ProcessPass *_ProcessPass[2]


#endif #GAMEOFLIFEPASS_H

# Translated from file 'osggameoflife.cpp'

# OpenSceneGraph example, osggameoflife.
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
geomss = osg.StateSet() # stateset where we can attach textures

def createScene(start_im):

    
    width = start_im.s()
    height = start_im.t()

    topnode = osg.Group()

    # create quad to display image on
    geode = osg.Geode()

    # each geom will contain a quad
    da = osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4)

    colors = osg.Vec4Array()
    colors.push_back(osg.Vec4(1.0,1.0,1.0,1.0))

    tcoords = osg.Vec2Array() # texture coords
    tcoords.push_back(osg.Vec2(0, 0))
    tcoords.push_back(osg.Vec2(width, 0))
    tcoords.push_back(osg.Vec2(width, height))
    tcoords.push_back(osg.Vec2(0, height))

    vcoords = osg.Vec3Array() # vertex coords
    geom = osg.Geometry()

    # initial viewer camera looks along y
    vcoords.push_back(osg.Vec3d(0, 0, 0))
    vcoords.push_back(osg.Vec3d(width, 0, 0))
    vcoords.push_back(osg.Vec3d(width, 0, height))
    vcoords.push_back(osg.Vec3d(0, 0, height))

    geom.setVertexArray(vcoords)
    geom.setTexCoordArray(0,tcoords)
    geom.addPrimitiveSet(da)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)
    geomss = geom.getOrCreateStateSet()
    geomss.setMode(GL_LIGHTING, osg.StateAttribute.OFF)

    geode.addDrawable(geom)

    topnode.addChild(geode)

    # create the ping pong processing passes
    golpass = GameOfLifePass(start_im)
    topnode.addChild(golpass.getRoot())

    # attach the output of the processing to the geom
    geomss.setTextureAttributeAndModes(0,
                                        golpass.getOutputTexture(),
                                        osg.StateAttribute.ON)
    return topnode

int main(int argc, char *argv[])
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates ping pong rendering with FBOs and mutliple rendering branches. It uses Conway's Game of Life to illustrate the concept.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] --startim start_image")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--startim","The initial image to seed the game of life with.")

    # if user request help write it out to cout.
    if arguments.read("-h")  or  arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    startName = str("")
    while arguments.read("--startim", startName) : 

    if startName == "" : 
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # load the image
    startIm = osgDB.readImageFile(startName)

    if  not startIm : 
        print "Could not load start image.\n"
        return(1)

    scene = createScene(startIm)

    # construct the viewer.
    viewer = osgViewer.Viewer()
    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    viewer.setSceneData(scene)

    viewer.realize()
    viewer.setCameraManipulator( osgGA.TrackballManipulator )()

    while  not viewer.done() :
        viewer.frame()
        # flip the textures after we've completed a frame
        golpass.flip()
        # attach the proper output to view
        geomss.setTextureAttributeAndModes(0,
                                            golpass.getOutputTexture(),
                                            osg.StateAttribute.ON)

    return 0


if __name__ == "__main__":
    main(sys.argv)
