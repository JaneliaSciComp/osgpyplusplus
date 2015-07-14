#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgoit"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'DepthPeeling.cpp'


#include "DepthPeeling.h"

#include <osg/Array>
#include <osg/AlphaFunc>
#include <osg/BlendFunc>
#include <osg/Depth>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Vec3>
#include <osg/MatrixTransform>
#include <osg/Texture2D>
#include <osg/TextureRectangle>
#include <osg/TexGen>
#include <osg/TexEnv>
#include <osg/TexMat>
#include <osg/TexGenNode>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osg/Math>

#include <limits>
#include <iostream>

 char *DepthPeeling.PeelingShader =
    "#version 120\n"
#ifdef USE_TEXTURE_RECTANGLE
    "#extension GL_ARB_texture_rectangle : enable\n"
    "uniform sampler2DRectShadow depthtex\n"
#else:
    "uniform sampler2DShadow depthtex\n"
#endif
    "uniform bool depthtest\n"  # depth test enable flag
    "uniform float invWidth\n"  # 1.0/width (shadow texture size)
    "uniform float invHeight\n" # 1.0/height (shadow texture size)
    "uniform float offsetX\n"   # viewport lower left corner (int)
    "uniform float offsetY\n"   # viewport lower left corner (int)
    "\n"
    "bool depthpeeling()\n"
    "\n"
    "  if  depthtest  : \n"
    "    vec3 r0 = vec3((gl_FragCoord.x-offsetX)*invWidth,\n"
    "                   (gl_FragCoord.y-offsetY)*invHeight,\n"
    "                    gl_FragCoord.z)\n"
#ifdef USE_TEXTURE_RECTANGLE
    "    return shadow2DRect(depthtex, r0).r < 0.5\n"
#else:
    "    return shadow2D(depthtex, r0).r < 0.5\n"
#endif
    "  \n"
    "  return False\n"
    "\n"


class PreDrawFBOCallback (osg.Camera.DrawCallback) :
  PreDrawFBOCallback( osg.FrameBufferObject* fbo, osg.FrameBufferObject* source_fbo, unsigned int width, unsigned int height, osg.Texture *dt, osg.Texture *ct ) :
 _fbo(fbo), _source_fbo(source_fbo), _depthTexture(dt), _colorTexture(ct), _width(width), _height(height) 

  virtual void operator () (osg.RenderInfo renderInfo) 
      # switching only the frame buffer attachments is actually faster than switching the framebuffer
#ifdef USE_PACKED_DEPTH_STENCIL
#ifdef USE_TEXTURE_RECTANGLE
     _fbo.setAttachment(osg.Camera.PACKED_DEPTH_STENCIL_BUFFER, osg.FrameBufferAttachment((osg.TextureRectangle*)(_depthTexture)))
#else:
     _fbo.setAttachment(osg.Camera.PACKED_DEPTH_STENCIL_BUFFER, osg.FrameBufferAttachment((osg.Texture2D*)(_depthTexture)))
#endif
#else:
#ifdef USE_TEXTURE_RECTANGLE
     _fbo.setAttachment(osg.Camera.DEPTH_BUFFER, osg.FrameBufferAttachment((osg.TextureRectangle*)(_depthTexture)))
#else:
     _fbo.setAttachment(osg.Camera.DEPTH_BUFFER, osg.FrameBufferAttachment((osg.Texture2D*)(_depthTexture)))
#endif
#endif
#ifdef USE_TEXTURE_RECTANGLE
     _fbo.setAttachment(osg.Camera.COLOR_BUFFER0, osg.FrameBufferAttachment((osg.TextureRectangle*)(_colorTexture)))
#else:
     _fbo.setAttachment(osg.Camera.COLOR_BUFFER0, osg.FrameBufferAttachment((osg.Texture2D*)(_colorTexture)))
#endif

     # check if we need to do some depth buffer copying from a source FBO into the current FBO
     if _source_fbo  not = NULL :
         fbo_ext = osg.FBOExtensions.instance(renderInfo.getContextID(),True)
         fbo_supported = fbo_ext  and  fbo_ext.isSupported()
         if fbo_supported  and  fbo_ext.glBlitFramebuffer :
             # blit the depth buffer from the solid geometry fbo into the current transparency fbo
             (_fbo).apply(*renderInfo.getState(), osg.FrameBufferObject.DRAW_FRAMEBUFFER)
             (_source_fbo).apply(*renderInfo.getState(), osg.FrameBufferObject.READ_FRAMEBUFFER)

#             glReadBuffer(GL_COLOR_ATTACHMENT0_EXT) # only needed to blit the color buffer
#             glDrawBuffer(GL_COLOR_ATTACHMENT0_EXT) # only needed to blit the color buffer
             fbo_ext.glBlitFramebuffer(
                 0, 0, static_cast<GLint>(_width), static_cast<GLint>(_height),
                 0, 0, static_cast<GLint>(_width), static_cast<GLint>(_height),
#ifdef USE_PACKED_DEPTH_STENCIL
                 GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT, GL_NEAREST)
#else:
                 GL_DEPTH_BUFFER_BIT, GL_NEAREST)
#endif _fbo :.apply(*renderInfo.getState(), osg.FrameBufferObject.READ_FRAMEBUFFER)
             (_fbo).apply(*renderInfo.getState(), osg.FrameBufferObject.DRAW_FRAMEBUFFER)
     # switch to this fbo, if it isn't already bound
     (_fbo).apply( *renderInfo.getState() )
  _fbo = osg.FrameBufferObject()
  _source_fbo = osg.FrameBufferObject()
  _depthTexture = osg.Texture()
  _colorTexture = osg.Texture()
  _width = unsigned int()
  _height = unsigned int()



class PostDrawFBOCallback (osg.Camera.DrawCallback) :
  PostDrawFBOCallback(bool restore) : _restore(restore) 

  virtual void operator () (osg.RenderInfo renderInfo) 
    # only unbind the fbo if this is the last transparency pass
    if _restore :
      osg.FBOExtensions.instance( renderInfo.getState().getContextID(), False ).glBindFramebuffer( GL_FRAMEBUFFER_EXT, 0 )
  _restore = bool()



DepthPeeling.CullCallback.CullCallback(unsigned int texUnit, unsigned int texWidth, unsigned int texHeight, unsigned int offsetValue) :
    _texUnit(texUnit),
    _texWidth(texWidth),
    _texHeight(texHeight),
    _offsetValue(offsetValue)

void DepthPeeling.CullCallback.operator()(osg.Node* node, osg.NodeVisitor* nv)
    cullVisitor = static_cast<osgUtil.CullVisitor*>(nv)
    renderStage = cullVisitor.getCurrentRenderStage()
    viewport = renderStage.getViewport()

    m = osg.Matrixd(*cullVisitor.getProjectionMatrix())
    m.postMultTranslate(osg.Vec3d(1, 1, 1))
    m.postMultScale(osg.Vec3d(0.5, 0.5, 0.5))

    # scale the texture coordinates to the viewport
#ifdef USE_TEXTURE_RECTANGLE
    m.postMultScale(osg.Vec3d(viewport.width(), viewport.height(), 1))
#else:
#ifndef USE_NON_POWER_OF_TWO_TEXTURE
    m.postMultScale(osg.Vec3d(viewport.width()/double(_texWidth), viewport.height()/double(_texHeight), 1))
#endif
#endif

    if _texUnit  not = 0  and  _offsetValue :
        # Kind of polygon offset: note this way, we can also offset lines and points.
        # Whereas with the polygon offset we could only handle surface primitives.
        m.postMultTranslate(osg.Vec3d(0, 0, -ldexp(double(_offsetValue), -24)))

    texMat = osg.TexMat(m)
    stateSet = osg.StateSet()
    stateSet.setTextureAttribute(_texUnit, texMat)

    if _texUnit  not = 0 :
        #
        # GLSL pipeline support
        #

#ifdef USE_TEXTURE_RECTANGLE
        # osg.Uniform.SAMPLER_2D_RECT_SHADOW not yet available in OSG 3.0.1
        # osg.Uniform* depthUniform = osg.Uniform(osg.Uniform.SAMPLER_2D_RECT_SHADOW, "depthtex")
        # depthUniform.set((int)_texUnit)
        depthUniform = osg.Uniform("depthtex", (int)_texUnit)
        invWidthUniform = osg.Uniform("invWidth", (float)1.0)
        invHeightUniform = osg.Uniform("invHeight", (float)1.0)
#else:
        depthUniform = osg.Uniform(osg.Uniform.SAMPLER_2D_SHADOW, "depthtex")
        depthUniform.set((int)_texUnit)
        invWidthUniform = osg.Uniform("invWidth", (float)1.0 / _texWidth)
        invHeightUniform = osg.Uniform("invHeight", (float)1.0 / _texHeight)
#endif
        offsetXUniform = osg.Uniform("offsetX", (float)viewport.x())
        offsetYUniform = osg.Uniform("offsetY", (float)viewport.y())

        # uniforms required for any any GLSL implementation in the rendered geometry
        stateSet.addUniform(depthUniform)
        stateSet.addUniform(invWidthUniform)
        stateSet.addUniform(invHeightUniform)
        stateSet.addUniform(offsetXUniform)
        stateSet.addUniform(offsetYUniform)

    cullVisitor.pushStateSet(stateSet)
    traverse(node, nv)
    cullVisitor.popStateSet()


osg.Node* DepthPeeling.createQuad(unsigned int layerNumber, unsigned int numTiles)
    tileSpan = 1
    tileOffsetX = 0
    tileOffsetY = 0
    if _showAllLayers : 
        tileSpan /= numTiles
        tileOffsetX = tileSpan * (layerNumber%numTiles)
        tileOffsetY = 1 - tileSpan * (1 + layerNumber/numTiles)

    vertices = osg.Vec3Array()

    vertices.push_back(osg.Vec3f(tileOffsetX           , tileOffsetY            , 0))
    vertices.push_back(osg.Vec3f(tileOffsetX           , tileOffsetY  + tileSpan, 0))
    vertices.push_back(osg.Vec3f(tileOffsetX + tileSpan, tileOffsetY  + tileSpan, 0))
    vertices.push_back(osg.Vec3f(tileOffsetX + tileSpan, tileOffsetY            , 0))

    colors = osg.Vec3Array()
    colors.push_back(osg.Vec3(1, 1, 1))

    texcoords = osg.Vec2Array()
    texcoords.push_back(osg.Vec2f(0, 0))
    texcoords.push_back(osg.Vec2f(0, 1))
    texcoords.push_back(osg.Vec2f(1, 1))
    texcoords.push_back(osg.Vec2f(1, 0))

    geometry = osg.Geometry()
    geometry.setVertexArray(vertices)
    geometry.setTexCoordArray(0, texcoords)

    geometry.setColorArray(colors, osg.Array.BIND_OVERALL)

    geometry.addPrimitiveSet(osg.DrawArrays(GL_QUADS, 0, 4))

    geode = osg.Geode()
    geode.addDrawable(geometry)

    return geode

#include <osg/State>

void DepthPeeling.createPeeling()
    numTiles = ceil(sqrt(double(_numPasses)))

    # cleanup any previous scene data
    _root.removeChildren(0, _root.getNumChildren())

    # create depth textures
    _depthTextures.clear()
    _depthTextures.resize(3)
    for (unsigned int i = 0 i < 3 ++i) 
#ifdef USE_TEXTURE_RECTANGLE
        _depthTextures[i] = osg.TextureRectangle()
#else:
        _depthTextures[i] = osg.Texture2D()
#endif
        _depthTextures[i].setTextureSize(_texWidth, _texHeight)

        _depthTextures[i].setFilter(osg.Texture.MIN_FILTER, osg.Texture.NEAREST)
        _depthTextures[i].setFilter(osg.Texture.MAG_FILTER, osg.Texture.NEAREST)
        _depthTextures[i].setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_BORDER)
        _depthTextures[i].setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_BORDER)

#ifdef USE_PACKED_DEPTH_STENCIL
        _depthTextures[i].setInternalFormat(GL_DEPTH24_STENCIL8_EXT)
        _depthTextures[i].setSourceFormat(GL_DEPTH_STENCIL_EXT)
        _depthTextures[i].setSourceType(GL_UNSIGNED_INT_24_8_EXT)
#else:
        _depthTextures[i].setInternalFormat(GL_DEPTH_COMPONENT)
#endif

        _depthTextures[i].setShadowComparison(True)
        _depthTextures[i].setShadowAmbient(0.0) # The r value if the test fails
        _depthTextures[i].setShadowCompareFunc(osg.Texture.GREATER)
        _depthTextures[i].setShadowTextureMode(osg.Texture.INTENSITY)

    # create the cameras for the individual depth peel layers
    _colorTextures.clear()
    _colorTextures.resize(_numPasses)
    for (unsigned int i = 0 i < _numPasses ++i) 

        # create textures for the color buffers
#ifdef USE_TEXTURE_RECTANGLE
        colorTexture = osg.TextureRectangle()
#else:
        colorTexture = osg.Texture2D()
#endif
        colorTexture.setTextureSize(_texWidth, _texHeight)
        colorTexture.setFilter(osg.Texture.MIN_FILTER, osg.Texture.NEAREST)
        colorTexture.setFilter(osg.Texture.MAG_FILTER, osg.Texture.NEAREST)
        colorTexture.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_BORDER)
        colorTexture.setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_BORDER)
        colorTexture.setInternalFormat(GL_RGBA)

        _colorTextures[i] = colorTexture

    # create some uniform and cull callback objects
    depthOff = osg.Uniform("depthtest", (bool)False)
    depthOn = osg.Uniform("depthtest", (bool)True)
    ccb = CullCallback(_texUnit, _texWidth, _texHeight, _offsetValue)

    # create a node for solid model rendering
    pre_solidNode = osg.Group()
    pre_solidNode.addChild(_solidscene)

    # create a node for non depth peeled transparent rendering (topmost layer)
    transparentNodeNoPeel = osg.Group()
    transparentNodeNoPeel.addChild(_transparentscene)
    transparentNodeNoPeel.getOrCreateStateSet().addUniform(depthOff)
    transparentNodeNoPeel.getOrCreateStateSet().setRenderBinDetails(99, "RenderBin", osg.StateSet.OVERRIDE_RENDERBIN_DETAILS)

    # create a node for depth peeled transparent rendering (any layers below).
    transparentNodePeel = osg.TexGenNode()
    transparentNodePeel.setReferenceFrame(osg.TexGenNode.ABSOLUTE_RF)
    transparentNodePeel.setTextureUnit(_texUnit)
    transparentNodePeel.getTexGen().setMode(osg.TexGen.EYE_LINEAR)
    transparentNodePeel.addChild(_transparentscene)
    transparentNodePeel.getOrCreateStateSet().addUniform(depthOn)
    transparentNodePeel.getOrCreateStateSet().setRenderBinDetails(99, "RenderBin", osg.StateSet.OVERRIDE_RENDERBIN_DETAILS)

    # only render fragments that are not completely transparent
    transparentNodePeel.getOrCreateStateSet().setAttributeAndModes(osg.AlphaFunc(osg.AlphaFunc.GREATER, 0.01),
                                    osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE)

    # generate texcoords for the depth texture, supporting the fixed function pipeline
    transparentNodePeel.getOrCreateStateSet().setTextureMode(_texUnit, GL_TEXTURE_GEN_S, osg.StateAttribute.ON)
    transparentNodePeel.getOrCreateStateSet().setTextureMode(_texUnit, GL_TEXTURE_GEN_T, osg.StateAttribute.ON)
    transparentNodePeel.getOrCreateStateSet().setTextureMode(_texUnit, GL_TEXTURE_GEN_R, osg.StateAttribute.ON)
    transparentNodePeel.getOrCreateStateSet().setTextureMode(_texUnit, GL_TEXTURE_GEN_Q, osg.StateAttribute.ON)

    # use two FBOs, one for solid geometry - the other one for the transparency passes
    # depth and color attachments will be switched as needed.
    osg.FrameBufferObject fbos[2] = osg.FrameBufferObject(), osg.FrameBufferObject()

    # create the cameras for the individual depth peel layers
    for (unsigned int i = 0 i < _numPasses ++i) 

        # get the pointers to the required fbo, color and depth textures for each camera instance
        # we perform ping ponging between two depth textures
        fbo0 =  fbos[0] if ((i >= 1)) else  NULL
        fbo =  fbos[1] if ((i >= 1)) else  fbos[0]
        colorTexture = _colorTextures[i]
        depthTexture =  _depthTextures[1+(i-1)%2] if ((i >= 1)) else  _depthTextures[i]
        prevDepthTexture =  _depthTextures[1+(i-2)%2] if ((i >= 2)) else  NULL

        # all our peeling layer cameras are post render
        camera = osg.Camera()
        camera.setDataVariance(osg.Object.DYNAMIC)
        camera.setInheritanceMask(osg.Camera.ALL_VARIABLES)
        camera.setRenderOrder(osg.Camera.POST_RENDER, i)
        camera.setClearMask(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
        camera.setClearColor(osg.Vec4f(0, 0, 0, 0))
        camera.setComputeNearFarMode(osg.Camera.DO_NOT_COMPUTE_NEAR_FAR)
        camera.setPreDrawCallback(PreDrawFBOCallback(fbo, fbo0, _texWidth, _texHeight, depthTexture, colorTexture))
        camera.setPostDrawCallback(PostDrawFBOCallback(i == _numPasses - 1))
        camera.setDrawBuffer(GL_COLOR_ATTACHMENT0_EXT)
        camera.setReadBuffer(GL_COLOR_ATTACHMENT0_EXT)
        camera.setAllowEventFocus(False)

        # the peeled layers are rendered with blending forced off
        # and the depth buffer is directly taken from camera 0 via framebuffer blit
        if i > 0 : 
            camera.getOrCreateStateSet().setMode(GL_BLEND, osg.StateAttribute.OFF | osg.StateAttribute.OVERRIDE)
            camera.setClearMask(GL_COLOR_BUFFER_BIT)
         else:
            # camera 0 has to clear both the depth and color buffers
            camera.setClearMask(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)

        # add the correct geometry for each pass.
        # the peeling passes also need read access to prevDepthTexture and a cull callback
        if 0 == i :         # solid geometry
            camera.addChild(pre_solidNode)
         elif 1 == i :  # topmost layer peeling pass
            camera.addChild(transparentNodeNoPeel)
         else              # behind layers peeling passes
            camera.addChild(transparentNodePeel)
            # set depth (shadow) texture for depth peeling and add a cull callback
            camera.getOrCreateStateSet().setTextureAttributeAndModes(_texUnit, prevDepthTexture)
            camera.addCullCallback(ccb)
        _root.addChild(camera)

    # create the composite camera that blends the peeled layers into the final scene
    _compositeCamera = osg.Camera()
    _compositeCamera.setDataVariance(osg.Object.DYNAMIC)
    _compositeCamera.setInheritanceMask(osg.Camera.READ_BUFFER | osg.Camera.DRAW_BUFFER)
    _compositeCamera.setRenderOrder(osg.Camera.POST_RENDER, _numPasses)
    _compositeCamera.setComputeNearFarMode(osg.Camera.COMPUTE_NEAR_FAR_USING_PRIMITIVES)
    _compositeCamera.setClearMask(0)
    _compositeCamera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    _compositeCamera.setViewMatrix(osg.Matrix())
    _compositeCamera.setProjectionMatrix(osg.Matrix.ortho2D(0, 1, 0, 1))
    _compositeCamera.setCullCallback(CullCallback(0, _texWidth, _texHeight, 0))
    stateSet = _compositeCamera.getOrCreateStateSet()
    stateSet.setRenderBinDetails(100, "TraversalOrderBin", osg.StateSet.OVERRIDE_RENDERBIN_DETAILS)
    _root.addChild(_compositeCamera)

    # solid geometry is blended first, transparency layers are blended in back to front order.
    # this order is achieved by rendering using a TraversalOrderBin (see camera stateset).
    for (unsigned int i = _numPasses i > 0 --i) 
        geode = createQuad(i%_numPasses, numTiles)
        stateSet = geode.getOrCreateStateSet()
        stateSet.setTextureAttributeAndModes(0, _colorTextures[i%_numPasses], osg.StateAttribute.ON)
        stateSet.setAttribute(osg.BlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA), osg.StateAttribute.ON)
        stateSet.setMode(GL_BLEND, osg.StateAttribute.ON)
        stateSet.setMode(GL_LIGHTING, osg.StateAttribute.OFF)
        depth = osg.Depth()
        depth.setWriteMask( False )
        stateSet.setAttributeAndModes( depth, osg.StateAttribute.ON )
        stateSet.setMode(GL_DEPTH_TEST, osg.StateAttribute.OFF)
        _compositeCamera.addChild(geode)

DepthPeeling.DepthPeeling(unsigned int width, unsigned int height) :
    _numPasses(9),
    _texUnit(2),
    _texWidth(width),
    _texHeight(height),
    _showAllLayers(False),
    _offsetValue(8),
    _root(osg.Group),
    _solidscene(osg.Group),
    _transparentscene(osg.Group)
    createPeeling()

void DepthPeeling.setSolidScene(osg.Node* scene)
    _solidscene.removeChildren(0, _solidscene.getNumChildren())
    _solidscene.addChild(scene)

void DepthPeeling.setTransparentScene(osg.Node* scene)
    _transparentscene.removeChildren(0, _transparentscene.getNumChildren())
    _transparentscene.addChild(scene)

osg.Node* DepthPeeling.getRoot()
    return _root

void DepthPeeling.resize(int width, int height)
#ifdef USE_TEXTURE_RECTANGLE
    for (unsigned int i = 0 i < 3 ++i)
        _depthTextures[i].setTextureSize(width, height)
    for (unsigned int i = 0 i < _colorTextures.size() ++i)
        _colorTextures[i].setTextureSize(width, height)
    _texWidth = width
    _texHeight = height
#else:
#ifndef USE_NON_POWER_OF_TWO_TEXTURE
    width = nextPowerOfTwo(width)
    height = nextPowerOfTwo(height)
#endif
    _depthTextures[0].setTextureSize(width, height)
    _depthTextures[1].setTextureSize(width, height)
    for (unsigned int i = 0 i < _colorTextures.size() ++i)
        _colorTextures[i].setTextureSize(width, height)
    _texWidth = width
    _texHeight = height
#endif
    createPeeling()

void DepthPeeling.setNumPasses(unsigned int numPasses)
    if numPasses == _numPasses :
        return
    if numPasses == unsigned(-1) :
        return
    _numPasses = numPasses
    createPeeling()
unsigned int DepthPeeling.getNumPasses() 
    return _numPasses

void DepthPeeling.setTexUnit(unsigned int texUnit)
    if texUnit == _texUnit :
        return
    _texUnit = texUnit
    createPeeling()

void DepthPeeling.setShowAllLayers(bool showAllLayers)
    if showAllLayers == _showAllLayers :
        return
    _showAllLayers = showAllLayers
    createPeeling()
bool DepthPeeling.getShowAllLayers() 
    return _showAllLayers

void DepthPeeling.setOffsetValue(unsigned int offsetValue)
    if offsetValue == _offsetValue :
        return
    _offsetValue = offsetValue
    createPeeling()
unsigned int DepthPeeling.getOffsetValue() 
    return _offsetValue


DepthPeeling.EventHandler.EventHandler(DepthPeeling* depthPeeling) :
    _depthPeeling(depthPeeling)
 


#* Handle events, return True if handled, False otherwise. 
bool DepthPeeling.EventHandler.handle( osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter, osg.Object*, osg.NodeVisitor*)
    if ea.getEventType() == osgGA.GUIEventAdapter.RESIZE : 
        _depthPeeling.resize(ea.getWindowWidth(), ea.getWindowHeight())
        return True

    if ea.getEventType() == osgGA.GUIEventAdapter.KEYDOWN : 
        switch (ea.getKey()) 
        case ord("m"):
            _depthPeeling.setNumPasses(_depthPeeling.getNumPasses() + 1)
            return True
        case ord("n"):
            _depthPeeling.setNumPasses(_depthPeeling.getNumPasses() - 1)
            return True
        case ord("p"):
            _depthPeeling.setOffsetValue(_depthPeeling.getOffsetValue() + 1)
            return True
        case ord("o"):
            _depthPeeling.setOffsetValue(_depthPeeling.getOffsetValue() - 1)
            return True
        case ord("l"):
            _depthPeeling.setShowAllLayers( not _depthPeeling.getShowAllLayers())
            return True
        default:
            return False
        

    return False

# Translated from file 'DepthPeeling.h'


#include <osg/Referenced>
#include <osg/Node>
#include <osg/Camera>
#include <osg/TextureRectangle>
#include <osg/Texture2D>
#include <osgGA/GUIEventHandler>

#include <limits>

#ifndef DEPTHPEELING_H
#define DEPTHPEELING_H

# Some choices for the kind of textures we can use ...
#define USE_TEXTURE_RECTANGLE
##define USE_NON_POWER_OF_TWO_TEXTURE
#define USE_PACKED_DEPTH_STENCIL

template<typename T>
inline T
nextPowerOfTwo(T k)
    if k == T(0) :
        return 1
    k--
    for (int i = 1 i < std.numeric_limits<T>.digits i, = 1)
        k = k | k >> i
    return k + 1

class DepthPeeling (osg.Referenced) :

    DepthPeeling(unsigned int width, unsigned int height)
    setSolidScene = void(osg.Node* scene)
    setTransparentScene = void(osg.Node* scene)
    getRoot = osg.Node*()
    resize = void(int width, int height)
    setNumPasses = void(unsigned int numPasses)
    unsigned int getNumPasses() 
    setTexUnit = void(unsigned int texUnit)
    setShowAllLayers = void(bool showAllLayers)
    bool getShowAllLayers() 
    setOffsetValue = void(unsigned int offsetValue)
    unsigned int getOffsetValue() 

    static  char *PeelingShader # use this to support depth peeling in GLSL shaders in transparent objects 

    class EventHandler (osgGA.GUIEventHandler) :
        EventHandler(DepthPeeling* depthPeeling)

        #* Handle events, return True if handled, False otherwise. 
        handle = virtual bool( osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter, osg.Object*, osg.NodeVisitor*)
        _depthPeeling = DepthPeeling()
    
    *createQuad = osg.Node(unsigned int layerNumber, unsigned int numTiles)
    createPeeling = void()

    class CullCallback (osg.NodeCallback) :
        CullCallback(unsigned int texUnit, unsigned int texWidth, unsigned int texHeight, unsigned int offsetValue)
        virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
        _texUnit = unsigned int()
        _texWidth = unsigned int()
        _texHeight = unsigned int()
        _offsetValue = unsigned int()
    

    _numPasses = unsigned int()
    _texUnit = unsigned int()
    _texWidth = unsigned int()
    _texHeight = unsigned int()
    _showAllLayers = bool()
    _offsetValue = unsigned int()

    # The root node that is handed over to the viewer
    _root = osg.Group()

    # The scene that is displayed
    _solidscene = osg.Group()
    _transparentscene = osg.Group()

    # The final camera that composites the pre rendered textures to the final picture
    _compositeCamera = osg.Camera()

#ifdef USE_TEXTURE_RECTANGLE
    _depthTextures = std.vector<osg.TextureRectangle >()
    _colorTextures = std.vector<osg.TextureRectangle >()
#else:
    _depthTextures = std.vector<osg.Texture2D >()
    _colorTextures = std.vector<osg.Texture2D >()
#endif


#endif # #ifndef DEPTHPEELING_H

# Translated from file 'HeatMap.cpp'

#
# * 3D Heat map using vertex displacement mapping
# * Rendered using depth peeling in fragment shader.
# 

#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Vec3>
#include <osg/MatrixTransform>
#include <osg/PositionAttitudeTransform>
#include <osg/LightModel>
#include <osg/io_utils>
#include <osg/Material>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgGA/TrackballManipulator>
#include <osgViewer/Viewer>
#include <osg/Math>
#include <iostream>

#define _USE_MATH_DEFINES
#include <math.h>

#include <osg/TexEnv>
#include <osg/TexMat>
#include <osg/Depth>
#include <osg/ShapeDrawable>
#include <osg/Texture1D>
#include <osg/Texture2D>
#include <osg/PolygonMode>
#include <osg/PolygonOffset>

#include "HeatMap.h"
#include "DepthPeeling.h"

#####################################/
# in-line GLSL source code

static  char *VertexShader = 
    "#version 120\n"
    "uniform float maximum\n"
    "uniform float maxheight\n"
    "uniform float transparency\n"
    "uniform sampler1D colortex\n"
    "uniform sampler2D datatex\n"
    "in vec2  xypos\n"
    "void main(void)\n"
    "\n"
    "    float foo\n"
    "    float tmp     = min(texture2D(datatex, xypos).x / maximum, 1.0)\n"
    "    gl_Position   = gl_ModelViewProjectionMatrix * (gl_Vertex + vec4(0.0, 0.0, maxheight * tmp, 0.0))\n"
    "    vec4 color    = texture1D(colortex, tmp)\n"
    "    color.w       = color.w * transparency\n"
    "    gl_FrontColor = color\n"
    "    gl_BackColor  = color\n"
    "\n"


static  char *FragmentShader =
    "#version 120\n"
    "bool depthpeeling()\n"
    "void main(void)\n"
    "\n"
    "  if  depthpeeling()  : discard\n"
    "  gl_FragColor = gl_Color\n"
    "\n"


#*
# * Overloaded Geometry class to return predefined bounds
# 
class MyGeometry (osg.Geometry) :
    MyGeometry(osg.BoundingBox bounds)
        m_bounds = bounds
        m_bsphere = osg.BoundingSphere(bounds)

    # an attempt to return a reasonable bounding box. Still does not prevent clipping of the heat map.
    def getBoundingBox():
        return m_bounds
    def computeBound():
        return m_bounds
    def getBound():
        return m_bsphere
    m_bounds = osg.BoundingBox()
    m_bsphere = osg.BoundingSphere()


Heatmap.Heatmap(float width, float depth, float maxheight, unsigned int K, unsigned int N, float maximum, float transparency)
    m_K = K
    m_N = N
    O = 4

    # create Geometry object to store all the vertices primitives.
    meshGeom = MyGeometry(osg.BoundingBox(osg.Vec3(-width/2, -depth/2, 0), osg.Vec3(width/2, depth/2, maxheight)))

    # we use a float attribute array storing texcoords
    xypositions = osg.Vec2Array()
    xypositions.setName("xypos")

    # create vertex coordinates
    vertices = osg.Vec3Array()
    off = osg.Vec3(-width/2, -depth/2, 0)
    for (unsigned int y=0 y < O*N y++) 
        if y % 2 == 0 :
            for (unsigned int x=0 x < O*K x++) 
                vertices.push_back(osg.Vec3(width*x/(O*K-1), depth*y/(O*N-1), 0.0)+off)
                xypositions.push_back(osg.Vec2(((float)x+0.5)/(O*K),((float)y+0.5)/(O*N)))
        else:
            vertices.push_back(osg.Vec3(0, depth*y/(O*N-1), 0.0)+off)
            xypositions.push_back(osg.Vec2(0.5/(O*K),((float)y+0.5)/(O*N)))
            for (unsigned int x=0 x < O*K-1 x++) 
                vertices.push_back(osg.Vec3(width*(0.5+x)/(O*K-1), depth*y/(O*N-1), 0.0)+off)
                xypositions.push_back(osg.Vec2(((float)(x+0.5)+0.5)/(O*K),((float)y+0.5)/(O*N)))
            vertices.push_back(osg.Vec3(width, depth*y/(O*N-1), 0.0)+off)
            xypositions.push_back(osg.Vec2(1.0-0.5/(O*K),((float)y+0.5)/(O*N)))
    xypositions.setBinding(osg.Array.BIND_PER_VERTEX)
    xypositions.setNormalize(False)

    meshGeom.setVertexAttribArray(6, xypositions)
    meshGeom.setVertexArray(vertices)

    # generate several tri strips to form a mesh
    indices = GLuint[4*O*K]()
    for (unsigned int y=0 y < O*N-1 y++) 
        if y % 2 == 0 :
            base = (y/2) * (O*K+O*K+1)
            base2 = (y/2) * (O*K+O*K+1) + O*K
            i = 0 for (unsigned int x=0 x < O*K x++)  indices[i++] = base2+x indices[i++] = base+x
            indices[i++] = base2+O*K
            meshGeom.addPrimitiveSet(osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLE_STRIP, i, indices))
        else:
            base = (y/2) * (O*K+O*K+1) + O*K
            base2 = (y/2) * (O*K+O*K+1) + O*K + O*K+1
            i = 0 for (unsigned int x=0 x < O*K x++)  indices[i++] = base+x indices[i++] = base2+x
            indices[i++] = base+O*K
            meshGeom.addPrimitiveSet(osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLE_STRIP, i, indices))
    delete[] indices

    # create vertex and fragment shader
    program = osg.Program()
    program.setName( "mesh" )
    program.addBindAttribLocation("xypos", 6)
    program.addShader( osg.Shader( osg.Shader.VERTEX, VertexShader ) )
    program.addShader( osg.Shader( osg.Shader.FRAGMENT, DepthPeeling.PeelingShader ) )
    program.addShader( osg.Shader( osg.Shader.FRAGMENT, FragmentShader ) )

    # create a 1D texture for color lookups
    colorimg = osg.Image()
    colorimg.allocateImage(5, 1, 1, GL_RGBA, GL_UNSIGNED_BYTE)
    data = colorimg.data()
    *data++ =   0 *data++ =   0 *data++ = 255 *data++ =   0  # fully transparent blue
    *data++ =   0 *data++ = 255 *data++ = 255 *data++ = 255  # turquoise
    *data++ =   0 *data++ = 255 *data++ =   0 *data++ = 255  # green
    *data++ = 255 *data++ = 255 *data++ =   0 *data++ = 255  # yellow
    *data++ = 255 *data++ =   0 *data++ =   0 *data++ = 255  # red
    colortex = osg.Texture1D(colorimg)
    colortex.setFilter(osg.Texture.MIN_FILTER, osg.Texture.LINEAR)
    colortex.setFilter(osg.Texture.MAG_FILTER, osg.Texture.LINEAR)
    colortex.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_EDGE)
    colortex.setResizeNonPowerOfTwoHint(False)

    # create a 2D texture for data lookups
    m_img2 = osg.Image()
    m_img2.allocateImage(K, N, 1, GL_LUMINANCE, GL_FLOAT)
    m_img2.setInternalTextureFormat(GL_RGB32F_ARB)
    m_data = (float*)m_img2.data()
    m_tex2 = osg.Texture2D(m_img2)
    m_tex2.setResizeNonPowerOfTwoHint(False)
    m_tex2.setFilter(osg.Texture.MIN_FILTER, osg.Texture.LINEAR)
    m_tex2.setFilter(osg.Texture.MAG_FILTER, osg.Texture.LINEAR)
    m_tex2.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_EDGE)
    m_tex2.setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_EDGE)

    # set render states
    meshstate = meshGeom.getOrCreateStateSet()
    meshstate.setMode(GL_BLEND,  osg.StateAttribute.ON)
    meshstate.setMode(GL_LIGHTING, osg.StateAttribute.OFF)
    meshstate.setAttributeAndModes(program, osg.StateAttribute.ON)
    meshstate.setTextureAttributeAndModes(0,colortex,osg.StateAttribute.ON)
    meshstate.setTextureAttributeAndModes(1,m_tex2,osg.StateAttribute.ON)

    # uniforms for height and color scaling
    maximumUniform = osg.Uniform( "maximum", (float)maximum )
    maxheightUniform = osg.Uniform( "maxheight", (float)maxheight )
    transparencyUniform = osg.Uniform( "transparency", (float)transparency)

    texUniform = osg.Uniform(osg.Uniform.SAMPLER_1D, "colortex")
    texUniform.set(0)
    texUniform2 = osg.Uniform(osg.Uniform.SAMPLER_2D, "datatex")
    texUniform2.set(1)
    meshstate.addUniform(texUniform)
    meshstate.addUniform(texUniform2)
    meshstate.addUniform(maximumUniform)
    meshstate.addUniform(maxheightUniform)
    meshstate.addUniform(transparencyUniform)

    # add the geometries to the geode.
    meshGeom.setUseDisplayList(False)
    addDrawable(meshGeom)

void Heatmap.setData(float *buffer, float maxheight, float maximum, float transparency)
    memcpy(m_data, buffer, m_N*m_K*sizeof(float))

    maximumUniform.set( maximum )
    maxheightUniform.set( maxheight )
    transparencyUniform.set ( transparency )

    m_img2.dirty()

Heatmap.~Heatmap()

# Translated from file 'HeatMap.h'


#ifndef HEATMAP_H
#define HEATMAP_H

#include <osg/Geode>
#include <osg/Uniform>
#include <osg/Texture2D>
#include <osg/Texture1D>

class Heatmap (osg.Geode) :
    Heatmap(float width, float depth, float maxheight, unsigned int K, unsigned int N, float maximum, float transparency)
    ~Heatmap()

    setData = void(float *buffer, float maxheight, float maximum, float transparency)
    m_K = unsigned int()
    m_N = unsigned int()
    *m_data = float()
    m_img2 = osg.Image()
    m_tex2 = osg.Texture2D()

    colorimg = osg.Image()
    colortex = osg.Texture1D()

    *maximumUniform = osg.Uniform()
    *maxheightUniform = osg.Uniform()
    *transparencyUniform = osg.Uniform()


#endif # #ifndef HEATMAP_H

# Translated from file 'osgoit.cpp'

# OpenSceneGraph example, myosgoit.
#*
#*  Author: Christian Buchner, based on original osgoit by Mathias Frhlich
#*
#*  This demo provides a DepthPeeling object that can correctly compose
#*  solid and transparent geometry within the same scene. The transparent
#*  geometry can also use GLSL shaders, as demonstrated in the 3D HeatMap.
#*  The solid geometry is only rendered once, and its depth buffer blitted
#*  into the cameras rendering the transparency layers.
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

#include "DepthPeeling.h"
#include "HeatMap.h"

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osg/Math>
#include <osg/PositionAttitudeTransform>
#include <osg/BlendFunc>
#include <osg/Material>
#include <osg/LightModel>
#include <osgDB/ReadFile>

#include <limits>
#include <iostream>

def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)
    arguments.getApplicationUsage().addKeyboardMouseBinding("m", "Increase the number of depth peeling layers")
    arguments.getApplicationUsage().addKeyboardMouseBinding("n", "Decrease the number of depth peeling layers")
    arguments.getApplicationUsage().addKeyboardMouseBinding("l", "Toggle display of the individual or composed layer textures")
    arguments.getApplicationUsage().addKeyboardMouseBinding("p", "Increase the layer offset")
    arguments.getApplicationUsage().addKeyboardMouseBinding("o", "Decrease the layer offset")

    # Have the usual viewer
    viewer = osgViewer.Viewer(arguments)

    displaySettings = osg.DisplaySettings()
    viewer.setDisplaySettings(displaySettings)
   
    # Add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()
   
    # add the help handler
    viewer.addEventHandler(osgViewer.HelpHandler(arguments.getApplicationUsage()))

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()
   
    # read the dump truck, we will need it twice
    dt = osgDB.readNodeFile("dumptruck.osg")

    # display a solid version of the dump truck
    solidModel = osg.PositionAttitudeTransform()
    solidModel.setPosition(osg.Vec3f(7.0, -2.0, 7.0))
    solidModel.addChild(dt)

    # generate the 3D heatmap surface to display
    hm = Heatmap(30, 30, 10, 30, 30, 1.0, 0.25)
    float data[30][30]
    for (int x=0 x < 30 ++x)
        for (int y=0 y < 30 ++y)
            data[y][x] = (double)rand() / RAND_MAX
    hm.setData((float*)data, 10.0, 1.0, 0.25)

    # add a transparent version of the truck to the scene also
    transparentTruck = osg.PositionAttitudeTransform()
    transparentTruck.setPosition(osg.Vec3f(7.0, -25.0, 7.0))

    # set the states of the truck so that it actually appears transparently and nicely lit.
    state = transparentTruck.getOrCreateStateSet()
    state.setMode(GL_BLEND, osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE)
    state.setAttribute(osg.BlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA), osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE)
    material = osg.Material()
    material.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(0.2,0.2,0.2,0.3))
    material.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(0.8,0.8,0.8,0.3))
    state.setAttribute(material,osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE)
    lm = osg.LightModel()
    lm.setTwoSided(True)
    state.setAttribute(lm, osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE)
    (transparentTruck).addChild(dt)

    # place the heatmap and a transparent dump truck in the transparent geometry group
    transparentModel = osg.Group()
    (transparentModel).addChild(hm)
    (transparentModel).addChild(transparentTruck)

    # The initial size set to 0, 0. We get a resize event for the right size...
    depthPeeling = DepthPeeling(0, 0)
    # the heat map already uses two textures bound to unit 0 and 1, so we can use TexUnit 2 for the peeling
    depthPeeling.setTexUnit(2)
    depthPeeling.setSolidScene(solidModel)
    depthPeeling.setTransparentScene(transparentModel)
    viewer.setSceneData(depthPeeling.getRoot())

    # Add the event handler for the depth peeling stuff
    viewer.addEventHandler(DepthPeeling.EventHandler(depthPeeling))

    # force a resize event, so the DepthPeeling object updates _texWidth and _texHeight
    viewer.realize()
    int x, y, width, height
    windows = osgViewer.ViewerBase.Windows()
    viewer.getWindows(windows)
    windows.front().getWindowRectangle(x,y,width,height)
    viewer.getEventQueue().windowResize(x,y,width,height)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
