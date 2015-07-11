#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgstereomatch"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgViewer

# OpenSceneGraph example, osgstereomatch.
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
#include <osg/Quat>
#include <osg/Matrix>
#include <osg/ShapeDrawable>
#include <osg/Geometry>
#include <osg/Geode>
#include <osg/TextureRectangle>

#include <osgDB/FileUtils>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <iostream>

#include "StereoPass.h"
#include "StereoMultipass.h"

osg.Node* createScene(osg.Image *left, osg.Image *right, unsigned int min_disp, unsigned int max_disp, unsigned int window_size, bool single_pass)
    width =  left.s()
    height =  left.t()

    topnode =  new osg.Group

    # create four quads so we can display up to four images

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

    osg.ref_ptr<osg.StateSet> geomss[4] # stateset where we can attach textures
    osg.ref_ptr<osg.TextureRectangle> texture[4]

    for (int i=0i<4i++) 
	osg.ref_ptr<osg.Vec3Array> vcoords = new osg.Vec3Array # vertex coords
	osg.ref_ptr<osg.Geometry> geom = new osg.Geometry

	# tile the quads on the screen
	# 2 3
	# 0 1
	int xoff, zoff
	xoff = (i%2)
	zoff = i>1 ? 1 : 0

	# initial viewer camera looks along y
	vcoords.push_back(osg.Vec3d(0+(xoff * width), 0, 0+(zoff * height)))
	vcoords.push_back(osg.Vec3d(width+(xoff * width), 0, 0+(zoff * height)))
	vcoords.push_back(osg.Vec3d(width+(xoff * width), 0, height+(zoff * height)))
	vcoords.push_back(osg.Vec3d(0+(xoff * width), 0, height+(zoff * height)))

	geom.setVertexArray(vcoords.get())
	geom.setTexCoordArray(0,tcoords.get())
	geom.addPrimitiveSet(da.get())
	geom.setColorArray(colors.get(), osg.Array.BIND_OVERALL)
	geomss[i] = geom.getOrCreateStateSet()
	geomss[i].setMode(GL_LIGHTING, osg.StateAttribute.OFF)

	texture[i] = new osg.TextureRectangle
	texture[i].setResizeNonPowerOfTwoHint(false)
	texture[i].setFilter(osg.Texture.MIN_FILTER, osg.Texture.LINEAR)
	texture[i].setFilter(osg.Texture.MAG_FILTER, osg.Texture.LINEAR)

	geode.addDrawable(geom.get())

    # attach the input images to the bottom textures of the view
    texture[0].setImage(left)
    texture[1].setImage(right)
    geomss[0].setTextureAttributeAndModes(0, texture[0].get(), osg.StateAttribute.ON)
    geomss[1].setTextureAttributeAndModes(0, texture[1].get(), osg.StateAttribute.ON)

    topnode.addChild(geode.get())

    # create the processing passes
    if single_pass : 
	stereopass =  new StereoPass(texture[0].get(), texture[1].get(),
						width, height,
						min_disp, max_disp, window_size)

	topnode.addChild(stereopass.getRoot().get())

	# attach the output of the processing to the top left geom
	geomss[2].setTextureAttributeAndModes(0,
					       stereopass.getOutputTexture().get(),
					       osg.StateAttribute.ON)
     else: 
	stereomp =  new StereoMultipass(texture[0].get(), texture[1].get(),
						width, height,
						min_disp, max_disp, window_size)
	topnode.addChild(stereomp.getRoot().get())
	# attach the output of the processing to the top left geom
	geomss[2].setTextureAttributeAndModes(0,
					       stereomp.getOutputTexture().get(),
					       osg.StateAttribute.ON)

    topnode = return()

int main(int argc, char *argv[])
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates a stereo matching algorithm. It uses multiple render targets and multiple passes with texture ping-pong.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] --left left_image --right right_image --min min_disparity --max max_disparity --window window_size")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--left","The left image of the stereo pair to load.")
    arguments.getApplicationUsage().addCommandLineOption("--right","The right image of the stereo pair to load.")
    arguments.getApplicationUsage().addCommandLineOption("--min","The minimum disparity to start matching pixels.")
    arguments.getApplicationUsage().addCommandLineOption("--max","The maximum disparity to stop matching pixels.")
    arguments.getApplicationUsage().addCommandLineOption("--window","The window size used to match areas around pixels.")
    arguments.getApplicationUsage().addCommandLineOption("--single","Use a single pass instead on multiple passes.")

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    leftName = str("")
    while arguments.read("--left", leftName) : 

    rightName = str("")
    while arguments.read("--right", rightName) : 

    unsigned int minDisparity = 0
    while arguments.read("--min", minDisparity) : 

    unsigned int maxDisparity = 31
    while arguments.read("--max", maxDisparity) : 

    unsigned int windowSize = 5
    while arguments.read("--window", windowSize) : 

    useSinglePass =  false
    while arguments.read("--single") :  useSinglePass = true 

    if leftName == "" || rightName=="" : 
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # load the images
    osg.ref_ptr<osg.Image> leftIm = osgDB.readImageFile(leftName)
    osg.ref_ptr<osg.Image> rightIm = osgDB.readImageFile(rightName)

    scene =  createScene(leftIm.get(), rightIm.get(), minDisparity, maxDisparity, windowSize, useSinglePass)

    # construct the viewer.
    viewer = osgViewer.Viewer()
    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # add the stats handler
    viewer.addEventHandler(new osgViewer.StatsHandler)

    viewer.setSceneData(scene)

    return viewer.run()
# -*- Mode: C++ tab-width: 4 indent-tabs-mode: t c-basic-offset: 4 -*- 

# OpenSceneGraph example, osgstereomatch.
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


#include "StereoMultipass.h"
#include <osgDB/FileUtils>
#include <iostream>

SubtractPass.SubtractPass(osg.TextureRectangle *left_tex,
						   osg.TextureRectangle *right_tex,
						   int width, int height,
						   int start_disparity) :
    _TextureWidth(width),
    _TextureHeight(height),
    _StartDisparity(start_disparity)
    _RootGroup = new osg.Group
    _InTextureLeft = left_tex
    _InTextureRight = right_tex

    createOutputTextures()

    _Camera = new osg.Camera
    setupCamera()
    _Camera.addChild(createTexturedQuad().get())

    _RootGroup.addChild(_Camera.get())

    setShader("shaders/stereomatch_subtract.frag")

SubtractPass.~SubtractPass()

osg.ref_ptr<osg.Group> SubtractPass.createTexturedQuad()
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
    _StateSet.setTextureAttributeAndModes(0, _InTextureLeft.get(), osg.StateAttribute.ON)
    _StateSet.setTextureAttributeAndModes(1, _InTextureRight.get(), osg.StateAttribute.ON)

    _StateSet.addUniform(new osg.Uniform("textureLeft", 0))
    _StateSet.addUniform(new osg.Uniform("textureRight", 1))
    _StateSet.addUniform(new osg.Uniform("start_disparity", _StartDisparity))

    quad_geode.addDrawable(quad_geom.get())

    top_group.addChild(quad_geode.get())

    top_group = return()

void SubtractPass.setupCamera()
    # clearing
    _Camera.setClearColor(osg.Vec4(0.1f,0.1f,0.3f,1.0f))
    _Camera.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # projection and view
    _Camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1,0,1))
    _Camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    _Camera.setViewMatrix(osg.Matrix.identity())

    # viewport
    _Camera.setViewport(0, 0, _TextureWidth, _TextureHeight)

    _Camera.setRenderOrder(osg.Camera.PRE_RENDER)
    _Camera.setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

    # attach the 4 textures
    for (int i=0 i<4 i++) 
		_Camera.attach(osg.Camera.BufferComponent(osg.Camera.COLOR_BUFFER0+i), _OutTexture[i].get())

void SubtractPass.createOutputTextures()
    for (int i=0 i<4 i++) 
		_OutTexture[i] = new osg.TextureRectangle

		_OutTexture[i].setTextureSize(_TextureWidth, _TextureHeight)
		_OutTexture[i].setInternalFormat(GL_RGBA)
		_OutTexture[i].setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
		_OutTexture[i].setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)

void SubtractPass.setShader(str filename)
    osg.ref_ptr<osg.Shader> fshader = new osg.Shader( osg.Shader.FRAGMENT )
    fshader.loadShaderSourceFromFile(osgDB.findDataFile(filename))

    _FragmentProgram = 0
    _FragmentProgram = new osg.Program

    _FragmentProgram.addShader(fshader.get())

    _StateSet.setAttributeAndModes(_FragmentProgram.get(), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

AggregatePass.AggregatePass(osg.TextureRectangle *diff_tex0,
							 osg.TextureRectangle *diff_tex1,
							 osg.TextureRectangle *diff_tex2,
							 osg.TextureRectangle *diff_tex3,
							 osg.TextureRectangle *agg_tex_in,
							 osg.TextureRectangle *agg_tex_out,
							 int width, int height,
							 int start_disparity, int window_size):
    _TextureWidth(width),
    _TextureHeight(height),
    _StartDisparity(start_disparity),
    _WindowSize(window_size)
    _RootGroup = new osg.Group

    _InTextureDifference[0] = diff_tex0
    _InTextureDifference[1] = diff_tex1
    _InTextureDifference[2] = diff_tex2
    _InTextureDifference[3] = diff_tex3

    _InTextureAggregate = agg_tex_in
    _OutTextureAggregate = agg_tex_out

    _OutTexture = _OutTextureAggregate

    _Camera = new osg.Camera
    setupCamera()
    _Camera.addChild(createTexturedQuad().get())

    _RootGroup.addChild(_Camera.get())

    setShader("shaders/stereomatch_aggregate.frag")


AggregatePass.~AggregatePass()

osg.ref_ptr<osg.Group> AggregatePass.createTexturedQuad()
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
    _StateSet.setTextureAttributeAndModes(0, _InTextureDifference[0].get(), osg.StateAttribute.ON)
    _StateSet.setTextureAttributeAndModes(1, _InTextureDifference[1].get(), osg.StateAttribute.ON)
    _StateSet.setTextureAttributeAndModes(2, _InTextureDifference[2].get(), osg.StateAttribute.ON)
    _StateSet.setTextureAttributeAndModes(3, _InTextureDifference[3].get(), osg.StateAttribute.ON)
    _StateSet.setTextureAttributeAndModes(4, _InTextureAggregate.get(), osg.StateAttribute.ON)

    _StateSet.addUniform(new osg.Uniform("textureDiff0", 0))
    _StateSet.addUniform(new osg.Uniform("textureDiff1", 1))
    _StateSet.addUniform(new osg.Uniform("textureDiff2", 2))
    _StateSet.addUniform(new osg.Uniform("textureDiff3", 3))
    _StateSet.addUniform(new osg.Uniform("textureAggIn", 4))
    _StateSet.addUniform(new osg.Uniform("start_disparity", _StartDisparity))
    _StateSet.addUniform(new osg.Uniform("window_size", _WindowSize))

    quad_geode.addDrawable(quad_geom.get())

    top_group.addChild(quad_geode.get())

    top_group = return()

void AggregatePass.setupCamera()
    # clearing
    _Camera.setClearColor(osg.Vec4(0.1f,0.1f,0.3f,1.0f))
    _Camera.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # projection and view
    _Camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1,0,1))
    _Camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    _Camera.setViewMatrix(osg.Matrix.identity())

    # viewport
    _Camera.setViewport(0, 0, _TextureWidth, _TextureHeight)

    _Camera.setRenderOrder(osg.Camera.PRE_RENDER)
    _Camera.setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

    _Camera.attach(osg.Camera.BufferComponent(osg.Camera.COLOR_BUFFER0+0), _OutTexture.get())

void AggregatePass.setShader(str filename)
    osg.ref_ptr<osg.Shader> fshader = new osg.Shader( osg.Shader.FRAGMENT )
    fshader.loadShaderSourceFromFile(osgDB.findDataFile(filename))

    _FragmentProgram = 0
    _FragmentProgram = new osg.Program

    _FragmentProgram.addShader(fshader.get())

    _StateSet.setAttributeAndModes(_FragmentProgram.get(), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

SelectPass.SelectPass(osg.TextureRectangle *in_tex,
					   int width, int height,
					   int min_disparity, int max_disparity) :
    _TextureWidth(width),
    _TextureHeight(height),
    _MinDisparity(min_disparity),
    _MaxDisparity(max_disparity)
    _RootGroup = new osg.Group
    _InTexture = in_tex

    createOutputTextures()

    _Camera = new osg.Camera
    setupCamera()
    _Camera.addChild(createTexturedQuad().get())

    _RootGroup.addChild(_Camera.get())

    setShader("shaders/stereomatch_select.frag")

SelectPass.~SelectPass()

osg.ref_ptr<osg.Group> SelectPass.createTexturedQuad()
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
    _StateSet.setTextureAttributeAndModes(0, _InTexture.get(), osg.StateAttribute.ON)

    _StateSet.addUniform(new osg.Uniform("textureIn", 0))
    _StateSet.addUniform(new osg.Uniform("min_disparity", _MinDisparity))
    _StateSet.addUniform(new osg.Uniform("max_disparity", _MaxDisparity))

    quad_geode.addDrawable(quad_geom.get())

    top_group.addChild(quad_geode.get())

    top_group = return()

void SelectPass.setupCamera()
    # clearing
    _Camera.setClearColor(osg.Vec4(0.1f,0.1f,0.3f,1.0f))
    _Camera.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # projection and view
    _Camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1,0,1))
    _Camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    _Camera.setViewMatrix(osg.Matrix.identity())

    # viewport
    _Camera.setViewport(0, 0, _TextureWidth, _TextureHeight)

    _Camera.setRenderOrder(osg.Camera.PRE_RENDER)
    _Camera.setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

	_Camera.attach(osg.Camera.BufferComponent(osg.Camera.COLOR_BUFFER0+0), _OutTexture.get())

void SelectPass.createOutputTextures()
    _OutTexture = new osg.TextureRectangle

    _OutTexture.setTextureSize(_TextureWidth, _TextureHeight)
    _OutTexture.setInternalFormat(GL_RGBA)
    _OutTexture.setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
    _OutTexture.setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)

void SelectPass.setShader(str filename)
    osg.ref_ptr<osg.Shader> fshader = new osg.Shader( osg.Shader.FRAGMENT )
    fshader.loadShaderSourceFromFile(osgDB.findDataFile(filename))

    _FragmentProgram = 0
    _FragmentProgram = new osg.Program

    _FragmentProgram.addShader(fshader.get())

    _StateSet.setAttributeAndModes(_FragmentProgram.get(), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

StereoMultipass.StereoMultipass(osg.TextureRectangle *left_tex,
								 osg.TextureRectangle *right_tex,
								 int width, int height,
								 int min_disparity, int max_disparity, int window_size) :
    _TextureWidth(width),
    _TextureHeight(height)
    _RootGroup = new osg.Group

    createOutputTextures()

    _Camera = new osg.Camera
    setupCamera()
    _Camera.addChild(createTexturedQuad().get())

    _RootGroup.addChild(_Camera.get())

    setShader("shaders/stereomatch_clear.frag")

    flip=1
    flop=0
	# we can do 16 differences in one pass,
	# but we must ping-pong the aggregate textures between passes
	# add passes until we cover the disparity range
	for (int i=min_disparity i<=max_disparity i+=16) 
		subp =  new SubtractPass(left_tex, right_tex,
											  width, height,
											  i)
		aggp =  new AggregatePass(subp.getOutputTexture(0).get(),
												subp.getOutputTexture(1).get(),
												subp.getOutputTexture(2).get(),
												subp.getOutputTexture(3).get(),
												_OutTexture[flip].get(),
												_OutTexture[flop].get(),
												width, height,
												i, window_size)

		_RootGroup.addChild(subp.getRoot().get())
		_RootGroup.addChild(aggp.getRoot().get())
		flip = flip ? 0 : 1
		flop = flop ? 0 : 1
    # add select pass
    _SelectPass = new SelectPass(_OutTexture[flip].get(),
								 width, height,
								 min_disparity, max_disparity)
    _RootGroup.addChild(_SelectPass.getRoot().get())

StereoMultipass.~StereoMultipass()

osg.ref_ptr<osg.Group> StereoMultipass.createTexturedQuad()
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

    quad_geode.addDrawable(quad_geom.get())

    top_group.addChild(quad_geode.get())

    top_group = return()

void StereoMultipass.setupCamera()
    # clearing
    _Camera.setClearColor(osg.Vec4(10.0f,0.0f,0.0f,1.0f))
    _Camera.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # projection and view
    _Camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1,0,1))
    _Camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    _Camera.setViewMatrix(osg.Matrix.identity())

    # viewport
    _Camera.setViewport(0, 0, _TextureWidth, _TextureHeight)

    _Camera.setRenderOrder(osg.Camera.PRE_RENDER)
    _Camera.setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

	# attach two textures for aggregating results
    _Camera.attach(osg.Camera.BufferComponent(osg.Camera.COLOR_BUFFER0+0), _OutTexture[0].get())
    _Camera.attach(osg.Camera.BufferComponent(osg.Camera.COLOR_BUFFER0+1), _OutTexture[1].get())

void StereoMultipass.createOutputTextures()
    for (int i=0 i<2 i++) 
		_OutTexture[i] = new osg.TextureRectangle

		_OutTexture[i].setTextureSize(_TextureWidth, _TextureHeight)
		_OutTexture[i].setInternalFormat(GL_RGBA)
		_OutTexture[i].setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
		_OutTexture[i].setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)

		# hdr, we want to store floats
		_OutTexture[i].setInternalFormat(GL_RGBA16F_ARB)
		#_OutTexture[i].setInternalFormat(GL_FLOAT_RGBA32_NV)
		#_OutTexture[i].setInternalFormat(GL_FLOAT_RGBA16_NV)
		_OutTexture[i].setSourceFormat(GL_RGBA)
		_OutTexture[i].setSourceType(GL_FLOAT)

void StereoMultipass.setShader(str filename)
    osg.ref_ptr<osg.Shader> fshader = new osg.Shader( osg.Shader.FRAGMENT )
    fshader.loadShaderSourceFromFile(osgDB.findDataFile(filename))

    _FragmentProgram = 0
    _FragmentProgram = new osg.Program

    _FragmentProgram.addShader(fshader.get())

    _StateSet.setAttributeAndModes(_FragmentProgram.get(), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )

# -*- Mode: C++ tab-width: 4 indent-tabs-mode: t c-basic-offset: 4 -*- 

# OpenSceneGraph example, osgstereomatch.
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


#ifndef STEREOMULTIPASS_H
#define STEREOMULTIPASS_H 1

#include <osg/ref_ptr>
#include <osg/Group>
#include <osg/Camera>
#include <osg/MatrixTransform>
#include <osg/Projection>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Texture2D>
#include <osg/TextureRectangle>

class SubtractPass 
public:
    SubtractPass(osg.TextureRectangle *left_tex, 
				 osg.TextureRectangle *right_tex,
				 int width, int height,
				 int start_disparity)
    ~SubtractPass()
    osg.ref_ptr<osg.Group> getRoot()  return _RootGroup 
    osg.ref_ptr<osg.TextureRectangle> getOutputTexture(int i)  return _OutTexture[i] 
    setShader = void(str filename)

private:
    osg.ref_ptr<osg.Group> createTexturedQuad()
    createOutputTextures = void()
    setupCamera = void()

    osg.ref_ptr<osg.Group> _RootGroup
    osg.ref_ptr<osg.Camera> _Camera
    osg.ref_ptr<osg.TextureRectangle> _InTextureLeft
    osg.ref_ptr<osg.TextureRectangle> _InTextureRight
    osg.ref_ptr<osg.TextureRectangle> _OutTexture[4]
    _TextureWidth = int()
    _TextureHeight = int()
    _StartDisparity = int()
    osg.ref_ptr<osg.Program> _FragmentProgram
    osg.ref_ptr<osg.StateSet> _StateSet


class AggregatePass 
public:
    AggregatePass(osg.TextureRectangle *diff_tex0,
				  osg.TextureRectangle *diff_tex1,
				  osg.TextureRectangle *diff_tex2,
				  osg.TextureRectangle *diff_tex3,
				  osg.TextureRectangle *agg_tex_in,
				  osg.TextureRectangle *agg_tex_out,
				  int width, int height,
				  int start_disparity, int window_size)
    ~AggregatePass()
    osg.ref_ptr<osg.Group> getRoot()  return _RootGroup 
    osg.ref_ptr<osg.TextureRectangle> getOutputTexture()  return _OutTexture 
    setShader = void(str filename)

private:
    osg.ref_ptr<osg.Group> createTexturedQuad()
    setupCamera = void()
    
    osg.ref_ptr<osg.Group> _RootGroup
    osg.ref_ptr<osg.Camera> _Camera
    osg.ref_ptr<osg.TextureRectangle> _InTextureDifference[4]
    osg.ref_ptr<osg.TextureRectangle> _InTextureAggregate
    osg.ref_ptr<osg.TextureRectangle> _OutTextureAggregate
    osg.ref_ptr<osg.TextureRectangle> _OutTexture
    _TextureWidth = int()
    _TextureHeight = int()
    _StartDisparity = int()
    _WindowSize = int()
    osg.ref_ptr<osg.Program> _FragmentProgram
    osg.ref_ptr<osg.StateSet> _StateSet


class SelectPass 
public:
    SelectPass(osg.TextureRectangle *in_tex, 
			   int width, int height,
			   int min_disparity, int max_disparity)
    ~SelectPass()
    osg.ref_ptr<osg.Group> getRoot()  return _RootGroup 
    osg.ref_ptr<osg.TextureRectangle> getOutputTexture()  return _OutTexture 
    setShader = void(str filename)
	
private:
    osg.ref_ptr<osg.Group> createTexturedQuad()
    createOutputTextures = void()
    setupCamera = void()

    osg.ref_ptr<osg.Group> _RootGroup
    osg.ref_ptr<osg.Camera> _Camera
    osg.ref_ptr<osg.TextureRectangle> _InTexture
	osg.ref_ptr<osg.TextureRectangle> _OutTexture
	osg.ref_ptr<osg.Image> _OutImage
	_TextureWidth = int()
    _TextureHeight = int()
    _MinDisparity = int()
    _MaxDisparity = int()
	osg.ref_ptr<osg.Program> _FragmentProgram
    osg.ref_ptr<osg.StateSet> _StateSet


class StereoMultipass 
public:
    StereoMultipass(osg.TextureRectangle *left_tex, 
					osg.TextureRectangle *right_tex,
					int width, int height, 
					int min_disparity, int max_disparity, int window_size)
    ~StereoMultipass()
    osg.ref_ptr<osg.Group> getRoot()  return _RootGroup 
    osg.ref_ptr<osg.TextureRectangle> getOutputTexture()  return _SelectPass.getOutputTexture().get() 
    setShader = void(str filename)

private:
    osg.ref_ptr<osg.Group> createTexturedQuad()
    createOutputTextures = void()
    setupCamera = void()
    
    osg.ref_ptr<osg.Group> _RootGroup
    osg.ref_ptr<osg.Camera> _Camera
    osg.ref_ptr<osg.TextureRectangle> _InTexture
    osg.ref_ptr<osg.TextureRectangle> _OutTexture[2]
	_TextureWidth = int()
    _TextureHeight = int()
	osg.ref_ptr<osg.Program> _FragmentProgram
    osg.ref_ptr<osg.StateSet> _StateSet

    *_SelectPass = SelectPass()

    flip = int()
    flop = int()


#endif #STEREOMULTIPASS_H
# -*- Mode: C++ tab-width: 4 indent-tabs-mode: t c-basic-offset: 4 -*- 

# OpenSceneGraph example, osgstereomatch.
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


#include "StereoPass.h"
#include <osgDB/FileUtils>
#include <iostream>

StereoPass.StereoPass(osg.TextureRectangle *left_tex, 
					   osg.TextureRectangle *right_tex,
					   int width, int height,
					   int min_disparity, int max_disparity, int window_size):
    _TextureWidth(width),
    _TextureHeight(height),
    _MinDisparity(min_disparity),
    _MaxDisparity(max_disparity),
    _WindowSize(window_size)
    _RootGroup = new osg.Group
    
	_InTextureLeft = left_tex
    _InTextureRight = right_tex
   
    createOutputTextures()

    _Camera = new osg.Camera
    setupCamera()
    _Camera.addChild(createTexturedQuad().get())

    _RootGroup.addChild(_Camera.get())

    setShader("shaders/stereomatch_stereopass.frag")

StereoPass.~StereoPass()

osg.ref_ptr<osg.Group> StereoPass.createTexturedQuad()
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

    quad_geom.setVertexArray(quad_coords.get())
    quad_geom.setTexCoordArray(0, quad_tcoords.get())
    quad_geom.addPrimitiveSet(quad_da.get())
    
    _StateSet = quad_geom.getOrCreateStateSet()
    _StateSet.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
    _StateSet.setTextureAttributeAndModes(0, _InTextureLeft.get(), osg.StateAttribute.ON)
    _StateSet.setTextureAttributeAndModes(1, _InTextureRight.get(), osg.StateAttribute.ON)

    _StateSet.addUniform(new osg.Uniform("textureID0", 0))
    _StateSet.addUniform(new osg.Uniform("textureID1", 1))
    _StateSet.addUniform(new osg.Uniform("min_disparity", _MinDisparity))
    _StateSet.addUniform(new osg.Uniform("max_disparity", _MaxDisparity))
    _StateSet.addUniform(new osg.Uniform("window_size", _WindowSize))

    quad_geode.addDrawable(quad_geom.get())
    
    top_group.addChild(quad_geode.get())

    top_group = return()

void StereoPass.setupCamera()
    # clearing
    _Camera.setClearColor(osg.Vec4(1.0f,0.0f,0.0f,1.0f))
    _Camera.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # projection and view
    _Camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1,0,1))
    _Camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    _Camera.setViewMatrix(osg.Matrix.identity())

    # viewport
    _Camera.setViewport(0, 0, _TextureWidth, _TextureHeight)

    _Camera.setRenderOrder(osg.Camera.PRE_RENDER)
    _Camera.setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

	# attach the output texture and use it as the color buffer.
	_Camera.attach(osg.Camera.COLOR_BUFFER, _OutTexture.get())

void StereoPass.createOutputTextures()
    _OutTexture = new osg.TextureRectangle
    
    _OutTexture.setTextureSize(_TextureWidth, _TextureHeight)
    _OutTexture.setInternalFormat(GL_RGBA)
    _OutTexture.setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
    _OutTexture.setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)

void StereoPass.setShader(str filename)
    osg.ref_ptr<osg.Shader> fshader = new osg.Shader( osg.Shader.FRAGMENT ) 
    fshader.loadShaderSourceFromFile(osgDB.findDataFile(filename))

    _FragmentProgram = 0
    _FragmentProgram = new osg.Program

    _FragmentProgram.addShader(fshader.get())

    _StateSet.setAttributeAndModes(_FragmentProgram.get(), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE )
# -*- Mode: C++ tab-width: 4 indent-tabs-mode: t c-basic-offset: 4 -*- 

# OpenSceneGraph example, osgstereomatch.
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


#ifndef STEREOPASS_H
#define STEREOPASS_H 1

#include <osg/ref_ptr>
#include <osg/Group>
#include <osg/Camera>
#include <osg/MatrixTransform>
#include <osg/Projection>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Texture2D>
#include <osg/TextureRectangle>

class StereoPass 
public:
    StereoPass(osg.TextureRectangle *left_tex, 
			   osg.TextureRectangle *right_tex,
			   int width, int height,
			   int min_disparity, int max_disparity, int window_size)
    ~StereoPass()
    osg.ref_ptr<osg.Group> getRoot()  return _RootGroup 
    osg.ref_ptr<osg.TextureRectangle> getOutputTexture()  return _OutTexture 
    setShader = void(str filename)
	
private:
    osg.ref_ptr<osg.Group> createTexturedQuad()
    createOutputTextures = void()
    setupCamera = void()

    osg.ref_ptr<osg.Group> _RootGroup
    osg.ref_ptr<osg.Camera> _Camera
    osg.ref_ptr<osg.TextureRectangle> _InTextureLeft
    osg.ref_ptr<osg.TextureRectangle> _InTextureRight
	osg.ref_ptr<osg.TextureRectangle> _OutTexture
	
	_TextureWidth = int()
    _TextureHeight = int()
    _MinDisparity = int()
    _MaxDisparity = int()
    _WindowSize = int()
	
    osg.ref_ptr<osg.Program> _FragmentProgram
    osg.ref_ptr<osg.StateSet> _StateSet


#endif #STEREOPASS_H


if __name__ == "__main__":
    main(sys.argv)
