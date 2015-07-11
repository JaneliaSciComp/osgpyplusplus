#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgdepthpeeling"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgViewer

#
  Steffen Frey
  Fachpraktikum Graphik-Programmierung 2007
  Institut fuer Visualisierung und Interaktive Systeme
  Universitaet Stuttgart
 

#export OSG_NOTIFY_LEVEL=DEBUG_INFO

#include "DePee.h"

#include <stdio.h>

#include <osg/GLExtensions>
#include <osg/Node>
#include <osg/MatrixTransform>
#include <osg/Projection>
#include <osg/Geode>

#include "Utility.h"

#include <osg/ShapeDrawable>
#include <osg/Geometry>
#include <assert.h>
#include <iostream>

DePee.DePee(osg.Group* parent, osg.Group* subgraph, unsigned width, unsigned height)
  _renderToFirst = false

  _isSketchy =false
  _isColored = false
  _isEdgy = true
  _isCrayon = false

  _normalDepthMapProgram = Utility.createProgram("shaders/depthpeel_normaldepthmap.vert","shaders/depthpeel_normaldepthmap.frag")
  _colorMapProgram = Utility.createProgram("shaders/depthpeel_colormap.vert","shaders/depthpeel_colormap.frag" )
  _edgeMapProgram = Utility.createProgram("shaders/depthpeel_edgemap.vert", "shaders/depthpeel_edgemap.frag")

  _parent = new osg.Group
  parent.addChild(_parent.get())
  _subgraph = subgraph

  _width = width
  _height = height
  _texWidth = width
  _texHeight = height

  assert(parent)
  assert(subgraph)

  _fps = 0
  _colorCamera = 0

  _sketchy = new osg.Uniform("sketchy", false)
  _colored = new osg.Uniform("colored", false)
  _edgy = new osg.Uniform("edgy", true)
  _sketchiness = new osg.Uniform("sketchiness", (float) 1.0)

  _normalDepthMap0  = Utility.newColorTexture2D(_texWidth, _texHeight, 32)
  _normalDepthMap1  = Utility.newColorTexture2D(_texWidth, _texHeight, 32)
  _edgeMap = Utility.newColorTexture2D(_texWidth, _texHeight, 8)
  _colorMap = Utility.newColorTexture2D(_texWidth, _texHeight, 8)

  #create a noise map...this doesn't end up in a new rendering pass
  (void) createMap(NOISE_MAP)

  #the viewport aligned quad
  _quadGeode = Utility.getCanvasQuad(_width, _height)


  #!!!Getting problems if assigning unit to texture in depth peeling subgraph and removing depth peeling steps!!!
  #That's why it is done here
  stateset =  _parent.getOrCreateStateSet()
  stateset.setTextureAttributeAndModes(1, _normalDepthMap0.get(), osg.StateAttribute.ON)
  stateset.setTextureAttributeAndModes(2, _normalDepthMap1.get(), osg.StateAttribute.ON)
  stateset.setTextureAttributeAndModes(3, _edgeMap.get(), osg.StateAttribute.ON)
  stateset.setTextureAttributeAndModes(4, _colorMap.get(), osg.StateAttribute.ON)
  stateset.setTextureAttributeAndModes(5, _noiseMap.get(), osg.StateAttribute.ON)

  # render the final thing
  (void) createFinal()

    #take one step initially
  addDePeePass()

  #render head up display
  (void) createHUD()

DePee.~DePee()

void DePee.setSketchy(bool sketchy)
    _sketchy.set(sketchy)
    _isSketchy = sketchy

void DePee.setCrayon(bool crayon)
  if _isCrayon != crayon :
      _isCrayon = crayon
      createMap(NOISE_MAP)

void DePee.setSketchiness(double sketchiness)
    _sketchiness.set((float)sketchiness)

void DePee.setColored(bool colored)
  if colored == !_isColored :
      if colored :
	  (void) createMap(COLOR_MAP, false)
      else:
	  _dePeePasses.back().remRenderPass(COLOR_MAP)
      _colored.set(colored)
      _isColored = colored

void DePee.setEdgy(bool edgy)

  if edgy != _isEdgy :

      _isEdgy = edgy
      unsigned int n = 0
      while remDePeePass() :
	  ++n

      if edgy :
	  (void) createMap(EDGE_MAP,_dePeePasses.size() == 1)
      else:
	  _dePeePasses.back().remRenderPass(EDGE_MAP)

      for(unsigned int i=0 i < n i++)
	  addDePeePass()
  _edgy.set(edgy)



void DePee.setFPS(double* fps)
  _fps = fps

unsigned int DePee.getNumberOfRenderPasses()
  unsigned int n = 0
  for(unsigned int i=0 i < _dePeePasses.size()i++)
    n += _dePeePasses.at(i).Cameras.size()
  # add one pass for final rendering pass and one for hud
  return n+2

bool DePee.addDePeePass()

  if _isColored :
      #remove previous color pass
      _dePeePasses.back().remRenderPass(COLOR_MAP)

  _dePeePasses.push_back(new DePeePass())
  _parent.addChild(_dePeePasses.back().root.get())

  #need to create a depth map in every case
  (void) createMap(NORMAL_DEPTH_MAP, _dePeePasses.size() == 1)

  if _isEdgy :
      (void) createMap(EDGE_MAP,_dePeePasses.size() == 1)

  if _isColored :
      (void) createMap(COLOR_MAP, false)

  true = return()

bool DePee.remDePeePass()
  if _dePeePasses.size() < 2 :
    false = return()

  _parent.removeChild(_dePeePasses.back().root.get())
  delete _dePeePasses.back()
  _dePeePasses.pop_back()

  _renderToFirst = !_renderToFirst

  if _isColored :
      (void) createMap(COLOR_MAP, false)

  true = return()


#create noise map with values ranging from 0 to 255
bool DePee.createNoiseMap()
    stateset =  _parent.getOrCreateStateSet()
    _noiseMap = new osg.Texture2D
    _noiseMap.setTextureSize(_width, _height)
    _noiseMap.setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
    _noiseMap.setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)
    stateset.setTextureAttributeAndModes(5, _noiseMap.get(), osg.StateAttribute.ON)

  image =  new osg.Image
  unsigned char* data = new unsigned char[_width*_height]
  unsigned char* tmpData = new unsigned char[_width*_height]

  random = rand() % 5000
  for(unsigned y=0 y < _height y++)
    for(unsigned x=0 x < _width x++)
      data[y*_width + x] = (unsigned char) (0.5 * 255.0 + Utility.getNoise(x, y, random) * 0.5 * 255.0)

  #if style isn't crayon style, smooth the noise map
  if !_isCrayon :
      for(unsigned i=0 i < 4 i++)
          for(unsigned y=0 y < _height y++)
            for(unsigned x=0 x < _width x++)
              tmpData[y*_width + x] = (unsigned char)Utility.smoothNoise(_width, _height,x,y, data)

          for(unsigned y=0 y < _height y++)
            for(unsigned x=0 x < _width x++)
              data[y*_width + x] = (unsigned char)Utility.smoothNoise(_width, _height, x,y, tmpData)

  image.setImage(_width, _height, 1,
		  1, GL_LUMINANCE, GL_UNSIGNED_BYTE,
		  data,
		  osg.Image.USE_NEW_DELETE)
  _noiseMap.setImage(image)
  true = return()

bool DePee.createHUD()
    geode =  new osg.Geode()

    timesFont = str("fonts/arial.ttf")

    # turn lighting off for the text and disable depth test to ensure its always ontop.
    stateset =  geode.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

    stateset.setTextureAttributeAndModes(1, _normalDepthMap0.get(), osg.StateAttribute.OFF)
    stateset.setTextureAttributeAndModes(2, _normalDepthMap1.get(), osg.StateAttribute.OFF)
    stateset.setTextureAttributeAndModes(3, _edgeMap.get(), osg.StateAttribute.OFF)
    stateset.setTextureAttributeAndModes(4, _colorMap.get(), osg.StateAttribute.OFF)
    stateset.setTextureAttributeAndModes(5, _noiseMap.get(), osg.StateAttribute.OFF)

    position = osg.Vec3(5.0f,7.0f,0.0f)
    delta = osg.Vec3(0.0f,-120.0f,0.0f)

    _hudText = new  osgText.Text

      geode.addDrawable( _hudText )
      _hudText.setDataVariance(osg.Object.DYNAMIC)
      _hudText.setFont(timesFont)
      _hudText.setPosition(position)
      _hudText.setText("Head Up Display")
      _hudText.setColor(osg.Vec4(0.5, 0.5, 0.5, 1.0))
      _hudText.setCharacterSize(20.0)
      position += delta

      bb = osg.BoundingBox()
      for(unsigned int i=0i<geode.getNumDrawables()++i)
	  bb.expandBy(geode.getDrawable(i).getBound())

      geom =  new osg.Geometry

      vertices =  new osg.Vec3Array
      depth =  bb.zMin()-0.1
      vertices.push_back(osg.Vec3(bb.xMin(),bb.yMax(),depth))
      vertices.push_back(osg.Vec3(bb.xMin(),bb.yMin(),depth))
      vertices.push_back(osg.Vec3(bb.xMax(),bb.yMin(),depth))
      vertices.push_back(osg.Vec3(bb.xMax(),bb.yMax(),depth))
      geom.setVertexArray(vertices)

      normals =  new osg.Vec3Array
      normals.push_back(osg.Vec3(0.0f,0.0f,1.0f))
      geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

      colors =  new osg.Vec4Array
      colors.push_back(osg.Vec4(0.0f,0.0,0.0f,0.3f))
      geom.setColorArray(colors, osg.Array.BIND_OVERALL)

      geom.addPrimitiveSet(new osg.DrawArrays(GL_QUADS,0,4))

      stateset =  geom.getOrCreateStateSet()
      stateset.setMode(GL_BLEND,osg.StateAttribute.ON)

      stateset.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)

      #geode.addDrawable(geom)

    camera =  new osg.Camera

    # set the projection matrix
    camera.setProjectionMatrix(osg.Matrix.ortho2D(0,1280,0,1024))

    # set the view matrix
    camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    camera.setViewMatrix(osg.Matrix.identity())

    # only clear the depth buffer
    camera.setClearMask(GL_DEPTH_BUFFER_BIT)

    # draw subgraph after main camera view.
    camera.setRenderOrder(osg.Camera.POST_RENDER)

    camera.addChild(geode)

    _parent.addChild(camera)

    true = return()



# then create the first camera node to do the render to texture
# render normal and depth map color map

bool DePee.createMap(MapMode mapMode, bool first)
    switch(mapMode)
      case EDGE_MAP:
	createEdgeMap = return(first)
      case NOISE_MAP:
	createNoiseMap = return()
      case NORMAL_DEPTH_MAP:
      case COLOR_MAP:
	createNormalDepthColorMap = return(mapMode, first)
      default:
	std.cerr, "mapMode not recognized!!!\n"
	false = return()

bool DePee.createFinal()
  screenAlignedProjectionMatrix =  new osg.Projection

  screenAlignedProjectionMatrix.setMatrix(osg.Matrix.ortho2D(0,_width,0,_height))
  screenAlignedProjectionMatrix.setCullingActive(false)

  screenAlignedModelViewMatrix =  new osg.MatrixTransform
  screenAlignedModelViewMatrix.setMatrix(osg.Matrix.identity())

  # Make sure the model view matrix is not affected by any transforms
  # above it in the scene graph:
  screenAlignedModelViewMatrix.setReferenceFrame(osg.Transform.ABSOLUTE_RF)


  # new we need to add the texture to the Drawable, we do so by creating a
  # StateSet to contain the Texture StateAttribute.
  stateset =  new osg.StateSet

  stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)

  _quadGeode.setStateSet(stateset)

  _parent.addChild(screenAlignedProjectionMatrix)
  screenAlignedProjectionMatrix.addChild(screenAlignedModelViewMatrix)
  screenAlignedModelViewMatrix.addChild(_quadGeode.get())

  #setup shader
  vertSource = str()
  if !Utility.readFile("shaders/depthpeel_final.vert", vertSource) :
      printf("shader source not found\n")
      false = return()

  fragSource = str()
  if !Utility.readFile("shaders/depthpeel_final.frag", fragSource) :
      printf("shader source not found\n")
      false = return()

  osg.ref_ptr<osg.Program> program = new osg.Program
  program.addShader( new osg.Shader( osg.Shader.VERTEX, vertSource.c_str() ) )
  program.addShader( new osg.Shader( osg.Shader.FRAGMENT, fragSource.c_str() ) )

  #choose map to display
  stateset.addUniform( new osg.Uniform("normalDepthMap0", 1))
  stateset.addUniform( new osg.Uniform("normalDepthMap1", 2))
  stateset.addUniform(new osg.Uniform("edgeMap", 3))
  stateset.addUniform( new osg.Uniform("colorMap", 4))
  stateset.addUniform( new osg.Uniform("noiseMap", 5))

  stateset.addUniform(_sketchy)
  stateset.addUniform(_colored)
  stateset.addUniform(_edgy)
  stateset.addUniform(_sketchiness)

  stateset.setAttributeAndModes( program.get(), osg.StateAttribute.OVERRIDE | osg.StateAttribute.ON)

  #switch lighting off
  stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE | osg.StateAttribute.OFF)
  true = return()

bool DePee.createEdgeMap(bool first)
#create the edge map of the first normal and depth map
  _dePeePasses.back().newRenderPass(EDGE_MAP)


  # set up the background color and clear mask.
  _dePeePasses.back().Cameras[EDGE_MAP].setClearColor(osg.Vec4(0.3,0.3f,0.3f,1.0f))
  _dePeePasses.back().Cameras[EDGE_MAP].setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  bs =  _quadGeode.getBound()
  if !bs.valid() :
      false = return()

  znear =  1.0f*bs.radius()
  zfar =  3.0f*bs.radius()

  znear *= 0.9f
  zfar *= 1.1f


  # set up projection.
  #_dePeePasses.back().Cameras.top().setProjectionMatrixAsFrustum(-proj_right,proj_right,-proj_top,proj_top,znear,zfar)
  _dePeePasses.back().Cameras[EDGE_MAP].setProjectionMatrixAsOrtho(0,_width,0,_height,znear,zfar)

  #set view
  _dePeePasses.back().Cameras[EDGE_MAP].setReferenceFrame(osg.Transform.ABSOLUTE_RF)

  _dePeePasses.back().Cameras[EDGE_MAP].setViewMatrixAsLookAt(osg.Vec3(0.0f,0.0f,2.0f)*bs.radius(), osg.Vec3(0.0,0.0,0.0),osg.Vec3(0.0f,1.0f,0.0f))

  # set viewport
  _dePeePasses.back().Cameras[EDGE_MAP].setViewport(0,0,_texWidth,_texHeight)

  # set the camera to render before the main camera.
  _dePeePasses.back().Cameras[EDGE_MAP].setRenderOrder(osg.Camera.PRE_RENDER)

  # tell the camera to use OpenGL frame buffer object
  _dePeePasses.back().Cameras[EDGE_MAP].setRenderTargetImplementation(osg.Camera.FRAME_BUFFER)

  #switch lighting off
  osg.ref_ptr<osg.StateSet> stateset = new osg.StateSet


  if _renderToFirst :
      stateset.addUniform(new osg.Uniform("normalDepthMap", 1))
  else:
      stateset.addUniform(new osg.Uniform("normalDepthMap", 2))

  _dePeePasses.back().Cameras[EDGE_MAP].attach(osg.Camera.COLOR_BUFFER, _edgeMap.get())
  stateset.addUniform( new osg.Uniform("edgeMap", 3))

  stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE |
              osg.StateAttribute.OFF)
  #setup shader
  stateset.setAttributeAndModes(_edgeMapProgram.get(), osg.StateAttribute.OVERRIDE | osg.StateAttribute.ON)
  stateset.addUniform(new osg.Uniform("width", (float) _width))
  stateset.addUniform(new osg.Uniform("height", (float) _height))

  if first :
      stateset.addUniform(new osg.Uniform("first", (float)1.0))
  else:
      stateset.addUniform(new osg.Uniform("first", (float)0.0))
  _dePeePasses.back().settingNodes[EDGE_MAP].setStateSet(stateset.get())

  # add subgraph to render
  assert(_dePeePasses.size() > 0)

  _dePeePasses.back().settingNodes[EDGE_MAP].addChild(_quadGeode.get())

  true = return()


bool DePee.createNormalDepthColorMap(MapMode mapMode, bool first)
  pass = DePeePass*()

  pass = _dePeePasses.back()

  pass.newRenderPass(mapMode)

  #
  # setup camera
  #

  # set up the background color and clear mask
  pass.Cameras[mapMode].setClearColor(osg.Vec4(0.f,0.f,1.f,1.f))
  pass.Cameras[mapMode].setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  bs =  _subgraph.getBound()
  if !bs.valid() :
      false = return()

  znear =  1.0f*bs.radius()
  zfar =  3.0f*bs.radius()

  # 2:1 aspect ratio as per flag geometry below.
  projTop =  0.25f*znear
  projRight =  projTop * ((double)_width/(double)_height)

  znear *= 0.9f
  zfar *= 1.1f

  # set up projection.
  pass.Cameras[mapMode].setProjectionMatrixAsFrustum(-projRight,projRight,-projTop,projTop, znear,zfar)

  # setup view
  pass.Cameras[mapMode].setReferenceFrame(osg.Transform.ABSOLUTE_RF)

  pass.Cameras[mapMode].setViewMatrixAsLookAt(bs.center()-osg.Vec3(0.0f,2.0f,0.0f)*bs.radius(),
							       bs.center(),
							       osg.Vec3(0.0f,0.0f,1.0f))
  # set viewport
  pass.Cameras[mapMode].setViewport(0,0,_texWidth,_texHeight)

  # set the camera to render before the main camera.
  pass.Cameras[mapMode].setRenderOrder(osg.Camera.PRE_RENDER)

  pass.Cameras[mapMode].setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

  #
  # setup stateset
  #
  #switch lighting off
  osg.ref_ptr<osg.StateSet> stateset = new osg.StateSet

  stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE |
		    osg.StateAttribute.OFF)

    switch(mapMode)
      case NORMAL_DEPTH_MAP:

	_renderToFirst = !_renderToFirst

	if _renderToFirst :
	    pass.Cameras[mapMode].attach(osg.Camera.COLOR_BUFFER, _normalDepthMap0.get())
	    stateset.addUniform(new osg.Uniform("normalDepthMap", 2))
	else:
	    pass.Cameras[mapMode].attach(osg.Camera.COLOR_BUFFER, _normalDepthMap1.get())
	    stateset.addUniform(new osg.Uniform("normalDepthMap", 1))

	stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE | osg.StateAttribute.OFF)
        stateset.setAttributeAndModes(_normalDepthMapProgram.get(), osg.StateAttribute.OVERRIDE | osg.StateAttribute.ON)
	break

      case COLOR_MAP:

        assert(pass == _dePeePasses.back())
        pass.Cameras[mapMode].attach(osg.Camera.COLOR_BUFFER, _colorMap.get())


	if _renderToFirst :
	    stateset.addUniform(new osg.Uniform("normalDepthMap", 1))
	else:
	    stateset.addUniform(new osg.Uniform("normalDepthMap", 2))
	pass.Cameras[mapMode].setClearColor(osg.Vec4(1.f,1.f,1.f,1.f))
	stateset.setMode(GL_LIGHTING,osg.StateAttribute.OVERRIDE | osg.StateAttribute.OFF)
	stateset.setMode(GL_BLEND, osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE)
	stateset.setAttributeAndModes(_colorMapProgram.get(), osg.StateAttribute.OVERRIDE | osg.StateAttribute.ON)
	stateset.addUniform(new osg.Uniform("tex", 0))

	break
      default:
	false = return()
      

    # add subgraph to render

    pass.settingNodes[mapMode].addChild(_subgraph.get())

    stateset.addUniform(new osg.Uniform("first", first))

    stateset.addUniform(new osg.Uniform("width", (float) _width))
    stateset.addUniform(new osg.Uniform("height", (float) _height))
    stateset.addUniform(new osg.Uniform("znear", znear))
    stateset.addUniform(new osg.Uniform("zfar", zfar))


    pass.settingNodes[mapMode].setStateSet(stateset.get())

    true = return()


bool DePee.updateHUDText()
  if !_fps :
    false = return()
  str = str()
  tmp =  Utility.toString(*_fps)
  i =  tmp.find_first_of('.')
  tmp = tmp.substr(0, i + 3)
  _hudText.setText(Utility.toString(_dePeePasses.size())
		    + " Depth Peeling Pass" + (_dePeePasses.size() == 1 ? " " : "es ")
		    + "((a)dd (r)emove) "
		    + (_isEdgy ? "+" : "-") + "(E)dgy " +
		    + (_isSketchy ? "+" : "-") + "(S)ketchy " +
		    + (_isColored ? "+" : "-") + "(C)olored " +
		    + ". "+Utility.toString(getNumberOfRenderPasses())+ " Rendering Passes "
		    + "@ "
		    + tmp + " fps")
  true = return()
#
  Steffen Frey
  Fachpraktikum Graphik-Programmierung 2007
  Institut fuer Visualisierung und Interaktive Systeme
  Universitaet Stuttgart
 

#ifndef _DEPEE_H_
#define _DEPEE_H_

#include <osg/Node>
#include <osg/Camera>
#include <osg/Group>
#include <osg/Texture2D>
#include <osgText/Text>
#include <string>
#include <stack>

#include "DePeePass.h"

#!
  The DePee class is main class for setting up and managing depth peeling. 
  A DePee object can be seen as a virtual node, that has one parent and one child. The rendering of every child and subchil of this child is managed by the the DePee node. Besides that, it handles a head up display.
 
class DePee : public osg.Referenced
public:
  #!
    The constructor is initialized by giving it a parent and child node (subgraph), as well as the width and height in pixels of the output window. Additionally a subgraph can be added whose children aren't depth peeled but combined with de depth peeled scene
   
  DePee(osg.Group* parent, osg.Group* subgraph, unsigned width, unsigned height)
  #!
    Takes care of clean removal of DePee
   
  ~DePee()
  
  #!
    The head up display shows information like internal status and current frames per second. This function needs to be called in the rendering loop to keep the information updated.
   
  updateHUDText = bool()

  #!
    Sets whether sketchiness is activated or deactivated
   
  setSketchy = void(bool sketchy)
  
  #!
    If sketchiness is enabled, sets whether a crayon should be used
   
  setCrayon = void(bool crayon)
  
  #!
    Sets whether color display is activated or deactivated
   
  setColored = void(bool colored)
  
  #!
    Sets whether edges are displayed or not
   
  setEdgy = void(bool edgy)

  #!
    Sets how sketchy lines and colors should be displayed (standard is 1.0)
   
  setSketchiness = void(double sketchiness)
  
  #!
    Set the pointer to the double variable containing the current fps for displaying it on the head up display
   
  setFPS = void(double* fps)

  #!
    Add a depth peeling pass and adjust the render passes accordingly
   
  addDePeePass = bool()

  #!
    Remove a depth peeling pass and adjust the render passes accordingly
   
  remDePeePass = bool()
  
private:
  #!
    Create a map. This is a function for convenience and calls either 
    createNoiseMap(), createEdgeMap() or createNormalDepthColorMap().
    Apart from NOISE_MAP, for every texture generation 
    one rendering pass is needed.
    The boolean first is used to indicate whether this rendering pass
    belongs to the first depth peeling pass.
   
  createMap = bool(MapMode mapMode, bool first=false)

  #!
    Creates a two dimensional noise map and initalizes _noiseMap with it
   
  createNoiseMap = bool()

  #!
    Depending on the chosen MapMode, it either creates a new rendering
    pass for creaeting a normal, depth or color map. The created rendering
    pass is added to the current depth peeling pass.
   
  createNormalDepthColorMap = bool(MapMode mapMode, bool first)
  
  #!
    Create an edge map. A previous depth and normal rendering pass in this 
    depth peeling pass is required for that.
   
  createEdgeMap = bool(bool first)
  
  #!
    Creates the final rendering pass for depth peeling. Color and edge map are
    added up here and sketchiness is applied.
   
  createFinal = bool()
  
  #!
    Create the rendering pass for the head up display
   
  createHUD = bool()

  #
    Returns the number of rendering passes of the depth peeling object
   
  unsigned int getNumberOfRenderPasses()
  
  
  _texWidth = unsigned()
  _texHeight = unsigned()
  _width = unsigned()
  _height = unsigned()
  
  osg.ref_ptr<osg.Group> _parent
  osg.ref_ptr<osg.Group> _subgraph
  osg.ref_ptr<osg.Texture2D> _noiseMap
  osg.ref_ptr<osg.Texture2D> _normalDepthMap0
  osg.ref_ptr<osg.Texture2D> _normalDepthMap1
  
  osg.ref_ptr<osg.Texture2D> _edgeMap
  
  osg.ref_ptr<osg.Texture2D> _colorMap
  
  osg.ref_ptr<osg.Geode> _quadGeode

  _hudText = osgText.Text*()
  _fps = double*()
  
  std.vector<DePeePass*> _dePeePasses
  
  _sketchy = osg.Uniform*()
  _colored = osg.Uniform*()
  _edgy = osg.Uniform*()
  _sketchiness = osg.Uniform*()
  
  _isSketchy = bool()
  _isColored = bool()
  _isEdgy = bool()
  _isCrayon = bool()

  _colorCamera = osg.Camera*()

  #shader programs
  osg.ref_ptr<osg.Program> _normalDepthMapProgram
  osg.ref_ptr<osg.Program> _colorMapProgram
  osg.ref_ptr<osg.Program> _edgeMapProgram

  _renderToFirst = bool()


#endif
#
  Steffen Frey
  Fachpraktikum Graphik-Programmierung 2007
  Institut fuer Visualisierung und Interaktive Systeme
  Universitaet Stuttgart
 

#include "DePeePass.h"

#include <iostream>
#include <assert.h>

DePeePass.DePeePass()
  root = new osg.Group

DePeePass.~DePeePass()
  root.releaseGLObjects()
  assert(Cameras.size() == settingNodes.size())
  while !Cameras.empty() :
      remRenderPass((*Cameras.begin()).first)
  
void DePeePass.newRenderPass(MapMode mapMode)
  Cameras[mapMode] = new osg.Camera
  settingNodes[mapMode] = new osg.Group
  root.addChild(Cameras[mapMode].get())
  Cameras[mapMode].addChild(settingNodes[mapMode].get())
  
void DePeePass.remRenderPass(MapMode mapMode)
  assert(Cameras.find(mapMode) != Cameras.end())
  Cameras[mapMode].releaseGLObjects()
  settingNodes[mapMode].releaseGLObjects()
  
  Cameras[mapMode].removeChild(settingNodes[mapMode].get())
  #setting Nodes have exactly one child
  assert(settingNodes[mapMode].getNumChildren() == 1)
  settingNodes[mapMode].removeChild(0,1)
  
  Cameras.erase(Cameras.find(mapMode))
  settingNodes.erase(settingNodes.find(mapMode))
#
  Steffen Frey
  Fachpraktikum Graphik-Programmierung 2007
  Institut fuer Visualisierung und Interaktive Systeme
  Universitaet Stuttgart
 

#ifndef _DEPEEPASS_H_
#define _DEPEEPASS_H_

#include <map>
#include <osg/Node>
#include <osg/Camera>
#include <osg/Group>

#!
  MapMode specifies the kind of texture maps that can be generated for later
  usage
 
enum MapMode NORMAL_DEPTH_MAP, COLOR_MAP, EDGE_MAP, NOISE_MAP

#!
  DePeePass can be seen as a mera data structure and typically used by 
  the class DePee. It represents one depth peeling pass and is initialized
  by functions in the DePee class, but cleans itself up.
  Please note, that no texture generation mode is allowed to appear twice

class DePeePass
 public:
  #!
    Constructor
   
  DePeePass()
  
  #!
    Desctructor cleans the whole depth peeling pass
   
  ~DePeePass()
  
  #!
    Make data structure ready for incorporating a new rendering pass
   
  newRenderPass = void(MapMode mapMode)
  
  #!
    Clean up the specified rendering pass
   
  remRenderPass = void(MapMode mapMode)
  
  osg.ref_ptr<osg.Group> root
  std.map<MapMode, osg.ref_ptr<osg.Camera> > Cameras
  std.map<MapMode, osg.ref_ptr<osg.Group> > settingNodes


#endif
#
  Steffen Frey
  Fachpraktikum Graphik-Programmierung 2007
  Institut fuer Visualisierung und Interaktive Systeme
  Universitaet Stuttgart
 

#include <osg/GLExtensions>
#include <osg/Node>
#include <osg/Geometry>
#include <osg/Notify>
#include <osg/MatrixTransform>
#include <osg/AnimationPath>

#include <osgDB/ReadFile>
#include <osgViewer/Viewer>
#include <osgGA/TrackballManipulator>

#include <iostream>

#include "DePee.h"    

#!
  Handles keyboard events.
  Maintains a copy of the DePee object and part of its internal state
  Used for example to set sketchiness, color, add or remove a depth peeling pass
 
class KeyboardEventHandler : public osgGA.GUIEventHandler
public:
  
  KeyboardEventHandler(DePee* dePee)
    _apc = 0
    _dePee = dePee
    _sketchy = false
    _sketchiness = 1.0
    _colored = false
    _edgy = true
    _crayon = false
    _dePee.setSketchy(_sketchy)
    _dePee.setColored(_colored)
  
  virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
    switch(ea.getEventType())
	
      case(osgGA.GUIEventAdapter.KEYDOWN):
	  if ea.getKey()==osgGA.GUIEventAdapter.KEY_Space :
	      if _apc :
		_apc.setPause(!_apc.getPause())
	      true = return()
	  else: if ea.getKey() == 'a' :
	      _dePee.addDePeePass()
	      true = return()
	  else: if ea.getKey() == 'r' :
	      _dePee.remDePeePass()
	      true = return()
	  else: if ea.getKey() == 'c' :
	      _colored = !_colored
	      _dePee.setColored(_colored)
	      true = return()
	  else: if ea.getKey() == 's' :
	      _sketchy = !_sketchy
	      _dePee.setSketchy(_sketchy)
	      true = return()
	  
	  else: if ea.getKey() == 'e' :
	      _edgy = !_edgy
	      _dePee.setEdgy(_edgy)
	      true = return()
	  else: if ea.getKey() == 'f' :
	      true = return()
	  else: if ea.getKey() == '+' :
	      _sketchiness += 0.5
	      _dePee.setSketchiness(_sketchiness)
	  else: if ea.getKey() == '-' :
	      _sketchiness -= 0.5
	      if _sketchiness < 0.0 :
		_sketchiness = 0.0
	      _dePee.setSketchiness(_sketchiness)

	  else: if ea.getKey() == 'y' :
	      _crayon = !_crayon
	      _dePee.setCrayon(_crayon)
	  
	  break
	  
      default:
	break
	
    false = return()
  def registerAnimationPathCallback(apc):
    _apc = apc
private:
  _dePee = DePee*()
  _sketchy = bool()
  _colored = bool()
  _edgy = bool()
  _crayon = bool()
  _sketchiness = double()
  _apc = osg.AnimationPathCallback*()



#!
  Handles mouse events.
  Maintains a copy of the DePee object and part of its internal state
  Used to rotate the object
 
class MouseEventHandler : public osgGA.GUIEventHandler
public:
  
  MouseEventHandler(DePee* dePee)
    _dePee = dePee
  
  virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
    switch(ea.getEventType())
	#mouse
      case(osgGA.GUIEventAdapter.DRAG):
	  rotate(ea.getXnormalized(), ea.getYnormalized()) 
	  break
      case(osgGA.GUIEventAdapter.MOVE):
	_prevX = ea.getXnormalized() 
	_prevY = ea.getYnormalized()
	break
	
      default:
	break
	
    false = return()
  def registerModelGroupTransform(modelGroupTransform):
    _modelGroupTransform = modelGroupTransform
    _rotCenter = modelGroupTransform.getBound().center()
private:
  def rotate(x, y):
    baseMatrix =  _modelGroupTransform.getMatrix()
    
    baseMatrix.preMultTranslate(_rotCenter)
    baseMatrix.preMultRotate(osg.Quat((x - _prevX) * 3, osg.Vec3d(0.0, 0.0, 1.0)))
    baseMatrix.preMultRotate(osg.Quat(-(y - _prevY) * 3, (baseMatrix * osg.Vec3d(1.0, 0.0, 0.0))))
    baseMatrix.preMultTranslate(-_rotCenter)
    
    _modelGroupTransform.setMatrix(baseMatrix)

    _prevX = x 
    _prevY = y
  
 
  _dePee = DePee*()
  
  _prevX = float() 
  _prevY = float()
  
  _rotCenter = osg.Vec3()
  _modelGroupTransform = osg.MatrixTransform*() 




def main(argc, argv):
  # use an ArgumentParser object to manage the program arguments.
  arguments = osg.ArgumentParser(argc,argv)
  
  # set up the usage document, in case we need to print out how to use this program.
  arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates Depth Peeling")
  arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" filename")
  
  
  # construct the viewer
  viewer = osgViewer.Viewer(arguments)
    
  # any option left unread are converted into errors to write out later.
  arguments.reportRemainingOptionsAsUnrecognized()
  
  # report any errors if they have occurred when parsing the program arguments.
  if arguments.errors() :
      arguments.writeErrorMessages(std.cout)
      return 1
  
  if arguments.argc()<=1 || arguments.argc() > 3 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1


  #only displays a textured quad
  viewer.getCamera().setComputeNearFarMode(osg.CullSettings.DO_NOT_COMPUTE_NEAR_FAR)

  # read the model to do depth peeling with
  loadedModel =  osgDB.readNodeFile(arguments.argv()[1])
  
  if !loadedModel :
    return 1
    
  # create a transform to spin the model.
  modelGroupTransform =  new osg.MatrixTransform
  modelGroup =  new osg.Group
  modelGroupTransform.addChild(modelGroup)
  modelGroup.addChild(loadedModel)
  
  rootNode =  new osg.Group()
  
  # add model to the viewer.
  viewer.setSceneData(rootNode)
  
  # Depth peel example only works on a single graphics context right now
  # so open up viewer on single screen to prevent problems
  viewer.setUpViewOnSingleScreen(0)
  
  # create the windows and run the threads.
  viewer.realize()
  
  unsigned int width = 1280
  unsigned int height = 1280
  windows = osgViewer.Viewer.Windows()
  viewer.getWindows(windows)
  if !windows.empty() :
    width = windows.front().getTraits().width
    height = windows.front().getTraits().height


  osg.ref_ptr<DePee> dePee = new DePee(rootNode, 
			        modelGroupTransform, 
			        width,
			        height)
  
  #create event handlers
  keyboardEventHandler =  new KeyboardEventHandler(dePee.get())
  mouseEventHandler =  new MouseEventHandler(dePee.get())
  viewer.addEventHandler(keyboardEventHandler)
  viewer.addEventHandler(mouseEventHandler)

  #viewer.setCameraManipulator(new osgGA.TrackballManipulator)
    
  stateset =  modelGroupTransform.getOrCreateStateSet()

  stateset.setMode(GL_BLEND, osg.StateAttribute.OFF)

  #create new animation callback for autmatic object rotation
  apc =  new osg.AnimationPathCallback(modelGroupTransform.getBound().center(),osg.Vec3(0.0f,0.0f,1.0f),osg.inDegrees(45.0f))
  apc.setPause(true)
  modelGroupTransform.setUpdateCallback(apc)
  
  keyboardEventHandler.registerAnimationPathCallback(apc)
  mouseEventHandler.registerModelGroupTransform(modelGroupTransform)
    
  #setup stuff that is necessary for measuring fps
  osg.Timer_t current_tick, previous_tick = 1
  fps =  new double
  dePee.setFPS(fps)
  
  while !viewer.done() :
    current_tick = osg.Timer.instance().tick()

    *fps = 1.0/osg.Timer.instance().delta_s(previous_tick,current_tick)
    dePee.updateHUDText()

    previous_tick = current_tick

    # fire off the cull and draw traversals of the scene.
    viewer.frame()

  return 0
#
  Steffen Frey
  Fachpraktikum Graphik-Programmierung 2007
  Institut fuer Visualisierung und Interaktive Systeme
  Universitaet Stuttgart
 

#include "Utility.h"

#include <assert.h>
#include <iostream>
#include <stdio.h>
#include <osg/Geometry>
#include <osg/Geode>
#include <osgDB/FileUtils>
#include <osgDB/fstream>

bool Utility.readFile( char* fName, str s)
  foundFile =  osgDB.findDataFile(fName)
  if foundFile.empty() : return false

  is = osgDB.ifstream()#(fName)
  is.open(foundFile.c_str())
  if is.fail() :
      std.cerr, "Could not open ", fName, " for reading.\n"
      false = return()
  ch =  is.get()
  while !is.eof() :
      s += ch
      ch = is.get()
  is.close()
  true = return()

str Utility.toString(double d)
  ostr = strstream()
  ostr, d
  return ostr.str()

osg.Program* Utility.createProgram(str vs, str fs)
  #setup shader
  vertSource = str()
  if !readFile((char*)vs.c_str(), vertSource) :
      printf("shader source not found\n")
      return 0

  fragSource = str()
  if !readFile((char*)fs.c_str(), fragSource) :
      printf("shader source not found\n")
      return 0


  program =  new osg.Program
  program.addShader( new osg.Shader( osg.Shader.VERTEX, vertSource.c_str() ) )
  program.addShader( new osg.Shader( osg.Shader.FRAGMENT, fragSource.c_str() ) )
  program = return()

double Utility.getNoise(unsigned x, unsigned y, unsigned random)
  n =  x + y * 57 + random * 131
  n = (n, 13) ^ n
  noise =  (1.0f - ( (n * (n * n * 15731 + 789221) +
                1376312589)0x7fffffff)* 0.000000000931322574615478515625f)
  noise = return()

double Utility.smoothNoise(unsigned width, unsigned height, unsigned x, unsigned y, unsigned char* noise)
  assert(noise)

  if x==0 || x > width -2
     || y==0 || y > height -2 :
    return noise[x + y*width]

  corners =  (noise[x-1 + (y-1) *width]
            +noise[x+1 + (y-1)*width]
            +noise[x-1 + (y+1) * width]
            +noise[x+1 + (y+1) * width]) / 16.0
  sides =  (noise[x-1 + y*width]
            +noise[x+1 + y*width]
            +noise[x + (y-1)*width]
            +noise[x + (y+1)*width]) / 8.0
  center =   noise[x + y*width] / 4.0

  return corners + sides + center

osg.Texture2D* Utility.newColorTexture2D(unsigned width, unsigned height, unsigned accuracy)
  texture2D =  new osg.Texture2D

  texture2D.setTextureSize(width, height)
  if accuracy == 32 :
      texture2D.setInternalFormat(GL_RGBA32F_ARB)
      texture2D.setSourceFormat(GL_RGBA)
  else: if accuracy == 8 :
      texture2D.setInternalFormat(GL_RGBA)
  texture2D.setSourceType(GL_FLOAT)
  texture2D.setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
  texture2D.setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)
  texture2D = return()

osg.Geode* Utility.getCanvasQuad(unsigned width, unsigned height, double depth)
  vertices =  new osg.Vec3Array
  texCoords =  new osg.Vec2Array
  vertices.push_back(osg.Vec3(0,0,depth))
  texCoords.push_back(osg.Vec2(0,0))

  vertices.push_back(osg.Vec3(width,0,depth))
  texCoords.push_back(osg.Vec2(1,0))

  vertices.push_back(osg.Vec3(0,height,depth))
  texCoords.push_back(osg.Vec2(0,1))

  vertices.push_back(osg.Vec3(width,height,depth))
  texCoords.push_back(osg.Vec2(1,1))

  quad =  new osg.Geometry
  quad.setVertexArray(vertices)
  quad.setTexCoordArray(1,texCoords)

  quad.addPrimitiveSet(new osg.DrawArrays(osg.PrimitiveSet.QUAD_STRIP,0,vertices.size()))

  colors =  new osg.Vec4Array
  colors.push_back(osg.Vec4(1.0f,1.0f,1.0f,1.0f))
  quad.setColorArray(colors, osg.Array.BIND_OVERALL)

  geode =  new osg.Geode()
  geode.addDrawable(quad)

  geode = return()

#
  Steffen Frey
  Fachpraktikum Graphik-Programmierung 2007
  Institut fuer Visualisierung und Interaktive Systeme
  Universitaet Stuttgart
 


#ifndef _UTILITY_H_
#define _UTILITY_H_

#include <string>
#include <sstream>
#include <osg/Program>
#include <osg/Texture2D>

namespace Utility
#!
  Reads a file and returns a string
 
readFile = bool( char* fName, str s)

#!
  Converts a number to a string
 
toString = str(double d)

#!
  Create a osg shader program consisting of a vertex shader and a 
  fragment shader
 
createProgram = osg.Program*(str vs, str fs)

#!
This is a random generator to generate noise patterns.
The returned values range from -1 to 1

getNoise = double(unsigned x, unsigned y, unsigned random)

#!
  Returns a smoothed noise version of the value that is read from the noise
  texture
 
smoothNoise = double(unsigned width, unsigned height, unsigned x, unsigned y, unsigned char* noise)

#!
  Creates a two dimensional color texture and apply some standard settings
 
 newColorTexture2D = osg.Texture2D*(unsigned width, unsigned height, unsigned accuracy)

#!
  Get a quad with screen size in order to show a texture full screen
 
getCanvasQuad = osg.Geode*(unsigned width, unsigned height, double depth=-1)
#endif


if __name__ == "__main__":
    main(sys.argv)
