#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgfpdepth"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgfpdepth.cpp'

# OpenSceneGraph example, osgfpdepth.
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
#include <osg/ColorMask>
#include <osg/CullFace>
#include <osg/Depth>
#include <osg/FrameBufferObject>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/GLExtensions>
#include <osg/Node>
#include <osg/NodeCallback>
#include <osg/Notify>
#include <osg/observer_ptr>
#include <osg/Projection>
#include <osg/Switch>
#include <osg/Texture2D>

#include <osgDB/ReadFile>
#include <osgGA/GUIEventHandler>
#include <osgUtil/Optimizer>

#include <osgText/Text>

#include <osgViewer/Renderer>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <iostream>
#include <sstream>

# Demonstration of floating point depth buffers. The most basic way to use
# * a floating point depth buffer in OpenGL is to create a frame buffer
# * object, attach a color and floating point depth texture, render,
# * and then copy the color texture to the screen. When doing
# * multisampling we can't use textures directly, so we have to create
# * render buffers with the proper format. Then we let OSG handle the
# * details of resolving the multisampling.
# *
# * When using a floating point depth buffer, it's advantageous to
# * reverse the depth buffer range (and the depth test, of course) so
# * that 0.0 corresponds to the far plane. See
# * e.g. http:#www.humus.name/index.php?ID=25 for details.
# 
using namespace osg
using namespace std

# createFBO() and destroyFBO(), and the supporting classes and
# * functions below, are only used to test possible valid frame buffer
# * configurations at startup. They wouldn't be used in a normal OSG
# * program unless we wanted to enumerate all the valid FBO
# * combinations and let the user choose between them.
# 

# Properties of an FBO that we will try to create
class FboConfig :
FboConfig()
        : colorFormat(0), depthFormat(0), redbits(0), depthBits(0),
          depthSamples(0), coverageSamples(0)
    FboConfig( string name_, GLenum colorFormat_, GLenum depthFormat_,
              int redbits_, int depthBits_, int depthSamples_ = 0,
              coverageSamples_ = 0)
        : name(name_), colorFormat(colorFormat_), depthFormat(depthFormat_),
          redbits(redbits_), depthBits(depthBits_), depthSamples(depthSamples_),
          coverageSamples(coverageSamples_)
    name = string()
    colorFormat = GLenum()
    depthFormat = GLenum()
    redbits = int()
    depthBits = int()
    depthSamples = int()
    coverageSamples = int()


# Properties of a buffer
class BufferConfig :
BufferConfig() 
    BufferConfig( string name_, GLenum format_, int bits_)
        : name(name_), format(format_), bits(bits_)
    name = string()
    format = GLenum()
    bits = int()


typedef vector<BufferConfig> BufferConfigList

validConfigs = vector<FboConfig>()
# Ugly global variables for the viewport width and height
int width, height

# This is only used when testing possible frame buffer configurations
# to find valid ones.
class FboData :
tex = ref_ptr<Texture2D>()             # color texture
    depthTex = ref_ptr<Texture2D>()        # depth texture
    fb = ref_ptr<FrameBufferObject>()      # render framebuffer
    resolveFB = ref_ptr<FrameBufferObject>() # multisample resolve target


makeDepthTexture = Texture2D*(int width, int height, GLenum internalFormat)

# Assemble lists of the valid buffer configurations, along with the
# possibilities for multisample coverage antialiasing, if any.
def getPossibleConfigs(gc, colorConfigs, depthConfigs, coverageConfigs):
    
    maxSamples = 0
    coverageSampleConfigs = 0
    contextID = gc.getState().getContextID()
    colorConfigs.push_back(BufferConfig("RGBA8", GL_RGBA8, 8))
    depthConfigs.push_back(BufferConfig("D24", GL_DEPTH_COMPONENT24, 24))
    fboe = FBOExtensions.instance(contextID, True)
    if !fboe.isSupported() :
        return
    if fboe.isMultisampleSupported() :
        glGetIntegerv(GL_MAX_SAMPLES_EXT, maxSamples)
    # isMultisampleCoverageSupported
    if isGLExtensionSupported(contextID,
                               "GL_NV_framebuffer_multisample_coverage") :
        glGetIntegerv(GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV,
                      coverageSampleConfigs)
        coverageConfigs.resize(coverageSampleConfigs * 2 + 4)
        glGetIntegerv(GL_MULTISAMPLE_COVERAGE_MODES_NV, coverageConfigs[0])
    if isGLExtensionSupported(contextID, "GL_ARB_depth_buffer_float") :
        depthConfigs.push_back(BufferConfig("D32F", GL_DEPTH_COMPONENT32F, 32))
    elif isGLExtensionSupported(contextID, "GL_NV_depth_buffer_float") :
        depthConfigs.push_back(BufferConfig("D32F", GL_DEPTH_COMPONENT32F_NV,
                                            32))

def checkFramebufferStatus(gc, silent):

    
    state = *gc.getState()
    contextID = state.getContextID()
    fboe = FBOExtensions.instance(contextID, True)
    switch(fboe.glCheckFramebufferStatus(GL_FRAMEBUFFER_EXT)) 
        case GL_FRAMEBUFFER_COMPLETE_EXT:
            break
        case GL_FRAMEBUFFER_UNSUPPORTED_EXT:
            if !silent :
                print "Unsupported framebuffer format\n"
            return False
        case GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT:
            if !silent :
                print "Framebuffer incomplete, missing attachment\n"
            return False
        case GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT:
            if !silent :
                print "Framebuffer incomplete, duplicate attachment\n"
            return False
        case GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT:
            if !silent :
                print "Framebuffer incomplete, attached images must have same dimensions\n"
            return False
        case GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT:
            if !silent :
                print "Framebuffer incomplete, attached images must have same format\n"
            return False
        case GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT:
            if !silent :
                print "Framebuffer incomplete, missing draw buffer\n"
            return False
        case GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT:
            if !silent :
                print "Framebuffer incomplete, missing read buffer\n"
            return False
        default:
            return False
    return True

# Attempt to create an FBO with a certain configuration. If the FBO
# is created with fewer bits in any of its parameters, the creation
# is deemed to have failed. Even though the result is a valid FBO,
# we're only interested in discrete, valid configurations.
def createFBO(gc, config, data):
    
    result = True
    multisample = config.depthSamples > 0
    csaa = config.coverageSamples > config.depthSamples
    data.fb = FrameBufferObject()
    texWidth = 512, texHeight = 512
    data.tex = Texture2D()
    data.tex.setTextureSize(texWidth, texHeight)
    data.tex.setInternalFormat(config.colorFormat)
    data.tex.setSourceFormat(GL_RGBA)
    data.tex.setSourceType(GL_FLOAT)
    data.tex.setFilter(Texture.MIN_FILTER, Texture.LINEAR_MIPMAP_LINEAR)
    data.tex.setFilter(Texture.MAG_FILTER, Texture.LINEAR)
    data.tex.setWrap(Texture.WRAP_S, Texture.CLAMP_TO_EDGE)
    data.tex.setWrap(Texture.WRAP_T, Texture.CLAMP_TO_EDGE)
    colorRB = 0
    depthRB = 0
    if multisample :
        data.resolveFB = FrameBufferObject()
        data.resolveFB.setAttachment(Camera.COLOR_BUFFER,
                                      FrameBufferAttachment(data.tex.get()))
        colorRB = RenderBuffer(texWidth, texHeight, config.colorFormat,
                                   config.coverageSamples, config.depthSamples)
        data.fb.setAttachment(Camera.COLOR_BUFFER,
                               FrameBufferAttachment(colorRB))
        depthRB = RenderBuffer(texWidth, texHeight, config.depthFormat,
                                   config.coverageSamples, config.depthSamples)
        data.fb.setAttachment(Camera.DEPTH_BUFFER,
                               FrameBufferAttachment(depthRB))
    else :
        data.depthTex = makeDepthTexture(texWidth, texHeight,
                                         config.depthFormat)
        data.fb.setAttachment(Camera.COLOR_BUFFER,
                               FrameBufferAttachment(data.tex.get()))
        data.fb.setAttachment(Camera.DEPTH_BUFFER,
                               FrameBufferAttachment(data.depthTex.get()))
    state = *gc.getState()
    contextID = state.getContextID()
    fboe = FBOExtensions.instance(contextID, True)

    data.fb.apply(state)
    result = checkFramebufferStatus(gc, True)
    if !result :
        fboe.glBindFramebuffer(GL_FRAMEBUFFER_EXT, 0)
        return False
    query = int()
    if multisample :
        colorRBID = colorRB.getObjectID(contextID, fboe)
        fboe.glBindRenderbuffer(GL_RENDERBUFFER_EXT, colorRBID)
        if csaa :
            fboe.glGetRenderbufferParameteriv(GL_RENDERBUFFER_EXT,
                                               GL_RENDERBUFFER_COVERAGE_SAMPLES_NV,
                                               query)
            if query < config.coverageSamples :
                result = False
            else :
                config.coverageSamples = query
            fboe.glGetRenderbufferParameteriv(GL_RENDERBUFFER_EXT,
                                               GL_RENDERBUFFER_COLOR_SAMPLES_NV,
                                               query)

            if  query < config.depthSamples :
               result = False
            else :
                config.depthSamples = query # report back the actual number

        else :
            fboe.glGetRenderbufferParameteriv(GL_RENDERBUFFER_EXT,
                                               GL_RENDERBUFFER_SAMPLES_EXT,
                                               query)
            if query < config.depthSamples :
                result = False
            else :
                config.depthSamples = query
    glGetIntegerv( GL_RED_BITS, query)
    if query != config.redbits :
        result = False
    glGetIntegerv(GL_DEPTH_BITS, query)
    if  query != config.depthBits :
        result = False
    if result  multisample  data.resolveFB.valid() :
        data.resolveFB.apply(state)
        result = checkFramebufferStatus(gc, True)
        if result :
            glGetIntegerv( GL_RED_BITS, query)
            if query != config.redbits :
                result = False
    fboe.glBindFramebuffer(GL_FRAMEBUFFER_EXT, 0)
    return result

def destroyFBO(gc, data):

    
    data.tex = 0
    data.depthTex = 0
    data.fb = 0
    data.resolveFB = 0
    state = *gc.getState()
    availableTime = 100.0
    RenderBuffer.flushDeletedRenderBuffers(state.getContextID(), 0.0,
                                            availableTime)
    availableTime = 100.0
    FrameBufferObject.flushDeletedFrameBufferObjects(state.getContextID(),
                                                      0.0, availableTime)

setAttachmentsFromConfig = void(Camera* camera,  FboConfig config)
makeTexturesAndGeometry = Switch*(int width, int height, Switch* sw = 0)

# Application state accessed from event handlers and main function
# contains state that can be changed by the user and the OSG classes
# used to display / indicate that state.
#
# camera - Camera with fbo, using either fp depth buffer or fixed
# switch child 0 - texture containing rendering of scene
# switch child 1 - fp depth buffer as texture
# switch child 2 - integer depth buffer as texture
# textNotAvailable- "not available" text if texture isn't valid.

class AppState (Referenced) :
AppState(osgViewer.Viewer* viewer_)
    setStateFromConfig = void( FboConfig config)
    advanceConfig = void(int increment)
    updateDisplayedTexture = void()
    updateNear = void()
    virtual ~AppState() 
    sw = ref_ptr<Switch>()         # switch between displayed texture
    displayScene = bool()
    invertRange = bool()
    currentConfig = int()
    viewer = osgViewer.Viewer*()
    zNear = double()
    camera = ref_ptr<Camera>()
    # text displayed on the screen showing the user's choices
    textProjection = ref_ptr<Projection>()
    configText = ref_ptr<osgText.Text>()
    zNearText = ref_ptr<osgText.Text>()
    textNotAvailable = ref_ptr<Geode>()
    textInverted = ref_ptr<Geode>()


AppState.AppState(osgViewer.Viewer* viewer_)
    : displayScene(True), invertRange(True), currentConfig(0),
      viewer(viewer_), zNear(0.03125)
    sw = Switch()
    fontName = string("fonts/arial.ttf")
    # Text description of current config
    configText = osgText.Text()
    configText.setDataVariance(Object.DYNAMIC)
    configText.setFont(fontName)
    configText.setPosition(Vec3(50.0, 50.0, 0.0))
    configText.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
    textGeode = Geode()
    textGeode.addDrawable(configText.get())
    # Text for the near plane distance
    zNearText = osgText.Text()
    zNearText.setDataVariance(Object.DYNAMIC)
    zNearText.setFont(fontName)
    zNearText.setPosition(Vec3(1230.0, 50.0, 0.0))
    zNearText.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
    zNearText.setAlignment(osgText.Text.RIGHT_BASE_LINE)
    textGeode.addDrawable(zNearText.get())
    # Projection that lets the text be placed in pixels.
    textProjection = Projection()
    textProjection.setMatrix(Matrix.ortho2D(0,1280,0,1024))
    textProjection.addChild(textGeode)
    # "texture not available" text displayed when the user trys to
    # display the depth texture while multisampling.
    noCanDo = osgText.Text()
    noCanDo.setFont(fontName)
    noCanDo.setPosition(Vec3(512.0, 384.0, 0.0))
    noCanDo.setColor(Vec4(1.0, 0.0, 0.0, 1.0))
    noCanDo.setText("not available")
    textNotAvailable = Geode()
    textNotAvailable.addDrawable(noCanDo)
    textProjection.addChild(textNotAvailable.get())
    # Is the depth test inverted?
    inverted = osgText.Text()
    inverted.setFont(fontName)
    inverted.setPosition(Vec3(512.0, 50.0, 0.0))
    inverted.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
    inverted.setText("inverted depth test")
    textInverted = Geode()
    textInverted.addDrawable(inverted)
    textInverted.setNodeMask(~0u)
    textProjection.addChild(textInverted.get())
    textProjection.getOrCreateStateSet().setRenderBinDetails(11, "RenderBin")

void AppState.setStateFromConfig( FboConfig config)
    camera = viewer.getSlave(0)._camera.get()
    setAttachmentsFromConfig(camera, config)
    renderer = dynamic_cast<osgViewer.Renderer*>(camera.getRenderer())
    if renderer :
        renderer.setCameraRequiresSetUp(True)
    if configText.valid() :
        configText.setText(validConfigs[currentConfig].name)
        configText.update()
    updateDisplayedTexture()

void AppState.advanceConfig(int increment)
    currentConfig = (currentConfig + increment) % validConfigs.size()
    setStateFromConfig(validConfigs[currentConfig])

void AppState.updateDisplayedTexture()
    if displayScene :
        sw.setSingleChildOn(0)
    elif validConfigs[currentConfig].depthSamples > 0
             || validConfigs[currentConfig].coverageSamples > 0 :
        sw.setAllChildrenOff()
    elif validConfigs[currentConfig].depthFormat != GL_DEPTH_COMPONENT24 :
        sw.setSingleChildOn(2)
    else :
        sw.setSingleChildOn(3)
    if displayScene
        || (validConfigs[currentConfig].depthSamples == 0
             validConfigs[currentConfig].coverageSamples == 0) :
        textNotAvailable.setNodeMask(0u)
    else :
        textNotAvailable.setNodeMask(~0u)

void AppState.updateNear()
    # Assume that the viewing frustum is symmetric.
    double fovy, aspectRatio, cNear, cFar
    viewer.getCamera().getProjectionMatrixAsPerspective(fovy, aspectRatio,
                                                          cNear, cFar)
    viewer.getCamera().setProjectionMatrixAsPerspective(fovy, aspectRatio,
                                                          zNear, cFar)
    nearStream = stringstream()
    nearStream, "near: ", zNear
    zNearText.setText(nearStream.str())
    zNearText.update()

class ConfigHandler (osgGA.GUIEventHandler) :

    ConfigHandler(AppState* appState)
        : _appState(appState)

    virtual bool handle( osgGA.GUIEventAdapter ea,
                        osgGA.GUIActionAdapter aa,
                        Object*, NodeVisitor* #nv)
        if ea.getHandled() : return False
        viewer = dynamic_cast<osgViewer.Viewer*>(aa)
        if !viewer : return False
        switch(ea.getEventType())
        case osgGA.GUIEventAdapter.KEYUP:
            if ea.getKey()=='d' :
                _appState.displayScene = !_appState.displayScene
                _appState.updateDisplayedTexture()
                return True
            elif ea.getKey()==osgGA.GUIEventAdapter.KEY_Right ||
                     ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Right :
                _appState.advanceConfig(1)
                return True
            elif ea.getKey()==osgGA.GUIEventAdapter.KEY_Left ||
                     ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Left :
                _appState.advanceConfig(-1)
                return True
            break
        default:
            break
        return False

    def getUsage(usage):

        
        usage.addKeyboardMouseBinding("d", "display depth texture")
        usage.addKeyboardMouseBinding("right arrow",
                                      "next frame buffer configuration")
        usage.addKeyboardMouseBinding("left arrow",
                                      "previous frame buffer configuration")
    virtual ~ConfigHandler() 
    _appState = ref_ptr<AppState>()


class DepthHandler (osgGA.GUIEventHandler) :

    DepthHandler(AppState *appState, Depth* depth)
        : _appState(appState), _depth(depth)
        depth.setDataVariance(Object.DYNAMIC)

    virtual bool handle( osgGA.GUIEventAdapter ea,
                        osgGA.GUIActionAdapter #aa,
                        Object*, NodeVisitor* #nv)
        if ea.getHandled() : return False

        depth = ref_ptr<Depth>()
        if !_depth.lock(depth) : return False

        switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYUP):
            if ea.getKey() == 'i' :
                _appState.invertRange = !_appState.invertRange
                if !_appState.invertRange :
                    _appState.camera.setClearDepth(1.0)
                    depth.setFunction(Depth.LESS)
                    depth.setRange(0.0, 1.0)
                    _appState.textInverted.setNodeMask(0u)
                else :
                    _appState.camera.setClearDepth(0.0)
                    depth.setFunction(Depth.GEQUAL)
                    depth.setRange(1.0, 0.0)
                    _appState.textInverted.setNodeMask(~0u)
                return True
            elif ea.getKey()==osgGA.GUIEventAdapter.KEY_Up ||
                     ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Up :
                _appState.zNear *= 2.0
                _appState.updateNear()
                return True
            elif ea.getKey()==osgGA.GUIEventAdapter.KEY_Down ||
                     ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Down :
                _appState.zNear *= .5
                _appState.updateNear()
                return True
            break
        default:
            break
        return False

    def getUsage(usage):

        
        usage.addKeyboardMouseBinding("i", "invert depth buffer range")
        usage.addKeyboardMouseBinding("up arrow",
                                      "double near plane distance")
        usage.addKeyboardMouseBinding("down arrow",
                                      "half near plane distance")
    virtual ~DepthHandler() 
    _appState = ref_ptr<AppState>()
    _depth = observer_ptr<Depth>()


def createTextureQuad(texture):

    
    vertices = Vec3Array()
    vertices.push_back(Vec3(-1.0, -1.0, 0.0))
    vertices.push_back(Vec3(1.0, -1.0, 0.0))
    vertices.push_back(Vec3(1.0, 1.0, 0.0))
    vertices.push_back(Vec3(-1.0, 1.0, 0.0))

    texcoord = Vec2Array()
    texcoord.push_back(Vec2(0.0, 0.0))
    texcoord.push_back(Vec2(1.0, 0.0))
    texcoord.push_back(Vec2(1.0, 1.0))
    texcoord.push_back(Vec2(0.0, 1.0))

    geom = Geometry()
    geom.setVertexArray(vertices)
    geom.setTexCoordArray(0, texcoord)
    geom.addPrimitiveSet(DrawArrays(GL_QUADS, 0, 4))

    geode = Geode()
    geode.addDrawable(geom)
    geode.getOrCreateStateSet().setTextureAttributeAndModes(0, texture, StateAttribute.ON)

    return geode

class ResizedCallback (osg.GraphicsContext.ResizedCallback) :
ResizedCallback(AppState* appState)
        : _appState(appState)
    resizedImplementation = void(GraphicsContext* gc, int x, int y, int width,
                               int height)
    _appState = ref_ptr<AppState>()


void ResizedCallback.resizedImplementation(GraphicsContext* gc, int x, int y,
                                            int width, int height)
    gc.resizedImplementation(x, y, width, height)
    makeTexturesAndGeometry(width, height, _appState.sw.get())
    _appState.setStateFromConfig(validConfigs[_appState
                                               .currentConfig])
    viewer = _appState.viewer
    vp = viewer.getSlave(0)._camera.getViewport()
    if vp :
        oldWidth = vp.width(), oldHeight = vp.height()
        aspectRatioChange = (width / oldWidth) / (height / oldHeight)
        vp.setViewport(0, 0, width, height)
        if aspectRatioChange != 1.0 :
            master = viewer.getCamera()
            switch (master.getProjectionResizePolicy())
            case Camera.HORIZONTAL:
                master.getProjectionMatrix()
                    *= Matrix.scale(1.0/aspectRatioChange,1.0,1.0)
                break
            case Camera.VERTICAL:
                master.getProjectionMatrix()
                    *= Matrix.scale(1.0, aspectRatioChange,1.0)
                break
            default:
                break

# Prefer GL_DEPTH_COMPONENT32F, otherwise use
# GL_DEPTH_COMPONENT32F_NV if available
depthTextureEnum = 0

# Standard OSG code for initializing osgViewer.Viewer with explicit
# creation of own graphics context. This is also a good time to test
# for valid frame buffer configurations we have a valid graphics
# context, but multithreading hasn't started, etc.
def setupGC(viewer, arguments):
    
    x = -1, y = -1, width = -1, height = -1
    while arguments.read("--window",x,y,width,height) : 

    wsi = GraphicsContext.getWindowingSystemInterface()
    if !wsi :
        OSG_NOTIFY(NOTICE), "View.setUpViewOnSingleScreen() : Error, no WindowSystemInterface available, cannot create windows."
        return 0

    ds = viewer.getDisplaySettings() ? viewer.getDisplaySettings() : DisplaySettings.instance().get()
    si = GraphicsContext.ScreenIdentifier()
    si.readDISPLAY()

    # displayNum has not been set so reset it to 0.
    if si.displayNum<0 : si.displayNum = 0

    decoration = True
    if x < 0 :
        unsigned int w, h
        wsi.getScreenResolution(si, w, h)
        x = 0
        y = 0
        width = w
        height = h
        decoration = False

    traits = GraphicsContext.Traits(ds)
    traits.hostName = si.hostName
    traits.displayNum = si.displayNum
    traits.screenNum = si.screenNum
    traits.x = x
    traits.y = y
    traits.width = width
    traits.height = height
    traits.windowDecoration = decoration
    traits.doubleBuffer = True
    traits.sharedContext = 0
    gc = GraphicsContext.createGraphicsContext(traits.get())
    gw = dynamic_cast<osgViewer.GraphicsWindow*>(gc.get())
    if gw :
        OSG_NOTIFY(INFO), "View.setUpViewOnSingleScreen - GraphicsWindow has been created successfully."
        gw.getEventQueue().getCurrentEventState()
            .setWindowRectangle(0, 0, width, height)
    else :
        OSG_NOTIFY(NOTICE), "  GraphicsWindow has not been created successfully."
    double fovy, aspectRatio, zNear, zFar
    viewer.getCamera().getProjectionMatrixAsPerspective(fovy, aspectRatio,
                                                         zNear, zFar)
    newAspectRatio = double(traits.width) / double(traits.height)
    aspectRatioChange = newAspectRatio / aspectRatio
    if aspectRatioChange != 1.0 :
        viewer.getCamera().getProjectionMatrix()
            *= Matrix.scale(1.0/aspectRatioChange,1.0,1.0)
    # Context has to be current to test for extensions
    gc.realize()
    gc.makeCurrent()
    contextID = gc.getState().getContextID()
    fboe = FBOExtensions.instance(contextID, True)
    if !fboe.isSupported() :
        OSG_NOTIFY(NOTICE), "Frame buffer objects are not supported\n"
        gc.releaseContext()
        gc.close(True)
        return 0
    if isGLExtensionSupported(contextID, "GL_ARB_depth_buffer_float") :
        depthTextureEnum = GL_DEPTH_COMPONENT32F
    elif isGLExtensionSupported(contextID, "GL_NV_depth_buffer_float") :
        depthTextureEnum = GL_DEPTH_COMPONENT32F_NV
    colorConfigs = BufferConfigList()
    depthConfigs = BufferConfigList()
    coverageConfigs = vector<int>()
    getPossibleConfigs(gc.get(), colorConfigs, depthConfigs, coverageConfigs)
    coverageSampleConfigs = (coverageConfigs.size() - 4) / 2
    print "color configs\nname\tbits\n"
    for (BufferConfigList.const_iterator colorItr = colorConfigs.begin(),
             colorEnd = colorConfigs.end()
         colorItr != colorEnd
         ++colorItr)
        for (BufferConfigList.const_iterator depthItr = depthConfigs.begin(),
             depthEnd = depthConfigs.end()
             depthItr != depthEnd
             ++depthItr)
            root = colorItr.name + " " + depthItr.name
            config = FboConfig(root, colorItr.format, depthItr.format,
                             colorItr.bits, depthItr.bits)
            data = FboData()
            if createFBO(gc.get(), config, data) :
                validConfigs.push_back(config)
            destroyFBO(gc.get(), data)
            if coverageConfigs.size() > 0 :
                #CSAA provides a list of all supported AA modes for
                #quick enumeration
                for (int kk = 0 kk < coverageSampleConfigs kk++)
                    msText = stringstream()
                    msText, root
                    config.depthSamples = coverageConfigs[kk*2+1]
                    config.coverageSamples = coverageConfigs[kk*2]

                    if  config.coverageSamples == config.depthSamples  :
                        # Normal antialiasing
                        msText, " - ", config.depthSamples, " MSAA"
                    else :
                        # coverage antialiasing
                        msText, " - ", config.coverageSamples, "/", config.depthSamples, " CSAA"
                    config.name = msText.str()

                    if createFBO(gc.get(), config, data) : 
                        validConfigs.push_back( config)
                    destroyFBO(gc.get(), data)
    if validConfigs.empty() :
        print "no valid frame buffer configurations!\n"
        return 0
    print "valid frame buffer configurations:\n"
    for (vector<FboConfig>.iterator itr = validConfigs.begin(),
             end = validConfigs.end()
         itr != end
         ++itr)
        print itr.name, "\n"
    gc.releaseContext()

    return gc.release()

colorTexture = ref_ptr<Texture2D>()
depthTexture = ref_ptr<Texture2D>()
depthTexture24 = ref_ptr<Texture2D>()

def makeDepthTexture(width, height, internalFormat):

    
    depthTex = Texture2D()
    depthTex.setTextureSize(width, height)
    depthTex.setSourceFormat(GL_DEPTH_COMPONENT)
    depthTex.setSourceType(GL_FLOAT)
    depthTex.setInternalFormat(internalFormat)
    depthTex.setFilter(Texture2D.MIN_FILTER, Texture2D.NEAREST)
    depthTex.setFilter(Texture2D.MAG_FILTER, Texture2D.NEAREST)
    depthTex.setWrap(Texture.WRAP_S, Texture.CLAMP_TO_EDGE)
    depthTex.setWrap(Texture.WRAP_T, Texture.CLAMP_TO_EDGE)
    return depthTex

def makeRttCamera(gc, width, height):

    
    rttCamera = Camera()
    rttCamera.setGraphicsContext(gc)
    rttCamera.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rttCamera.setClearColor(Vec4(0.0, 0.4, 0.5, 0.0))
    # normally the depth test is inverted, although the user can
    # change that.
    rttCamera.setClearDepth(0.0)
    rttCamera.setViewport(0, 0, width, height)
    rttCamera.setDrawBuffer(GL_FRONT)
    rttCamera.setReadBuffer(GL_FRONT)
    rttCamera.setRenderTargetImplementation(Camera.FRAME_BUFFER_OBJECT)
    rttCamera.setComputeNearFarMode(CullSettings.DO_NOT_COMPUTE_NEAR_FAR)
    return rttCamera

def setAttachmentsFromConfig(camera, config):

    
    # XXX Detaching the old buffers may not be necessary.
    if !camera.getBufferAttachmentMap().empty() :
        camera.detach(Camera.COLOR_BUFFER)
        camera.detach(Camera.DEPTH_BUFFER)
    camera.attach(Camera.COLOR_BUFFER, colorTexture.get(), 0, 0, False,
                   config.coverageSamples, config.depthSamples)
    if config.coverageSamples != 0 || config.depthSamples != 0 :
        camera.attach(Camera.DEPTH_BUFFER, config.depthFormat)
    elif config.depthFormat == GL_DEPTH_COMPONENT24 :
        camera.attach(Camera.DEPTH_BUFFER, depthTexture24.get())
    else :
        camera.attach(Camera.DEPTH_BUFFER, depthTexture.get())

# Create the parts of the local scene graph used to display the final
# results.
def makeTexturesAndGeometry(width, height, sw):
    
    if !sw :
        sw = Switch()
    colorTexture = Texture2D()
    colorTexture.setTextureSize(width, height)
    colorTexture.setInternalFormat(GL_RGBA)
    colorTexture.setFilter(Texture2D.MIN_FILTER, Texture2D.LINEAR)
    colorTexture.setFilter(Texture2D.MAG_FILTER, Texture2D.LINEAR)
    colorTexture.setWrap(Texture.WRAP_S, Texture.CLAMP_TO_EDGE)
    colorTexture.setWrap(Texture.WRAP_T, Texture.CLAMP_TO_EDGE)
    colorTexture.setBorderColor(Vec4(0, 0, 0, 0))

    depthTexture24 = makeDepthTexture(width, height, GL_DEPTH_COMPONENT24)
    if depthTextureEnum :
        depthTexture = makeDepthTexture(width, height, depthTextureEnum)
    depthTexture = depthTexture24
    sw.removeChildren(0, sw.getNumChildren())
    sw.addChild(createTextureQuad(colorTexture.get()))
    sw.addChild(createTextureQuad(depthTexture.get()))
    sw.addChild(createTextureQuad(depthTexture24.get()))
    sw.setSingleChildOn(0)
    return sw

def main(argc, argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = ArgumentParser(argc,argv)
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()
                         + " demonstrates using a floating point depth buffer.\nThe user can invert the depth buffer range and choose among available multi-sample configurations.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("--far <number>", "Set far plane value")
    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1
    zFar = 500.0
    while arguments.read("--far", zFar) :
        
    # construct the viewer.
    viewer = osgViewer.Viewer()
    appState = AppState(viewer)
    viewer.addEventHandler(osgViewer.StatsHandler)()
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()
    viewer.addEventHandler(osgViewer.ScreenCaptureHandler)()
    # The aspect ratio is set to the correct ratio for the window in
    # setupGC().
    viewer.getCamera()
        .setProjectionMatrixAsPerspective(40.0, 1.0, appState.zNear, zFar)
    gc = setupGC(viewer, arguments)
    if !gc :
        return 1
    gc.setResizedCallback(ResizedCallback(appState.get()))
    traits = gc.getTraits()
    width = traits.width
    height = traits.height
    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1
    loadedModel = osgDB.readNodeFiles(arguments)
    if !loadedModel : 
        cerr, "couldn't load ", argv[1], "\n"
        return 1
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel.get())
    # creates texture to be rendered
    sw = makeTexturesAndGeometry(width, height, appState.sw.get())
    rttCamera = makeRttCamera(gc, width, height)
    rttCamera.setRenderOrder(Camera.PRE_RENDER)
    viewer.addSlave(rttCamera.get())
    appState.camera = rttCamera
    # geometry and slave camera to display the result
    displayRoot = Group()
    displayRoot.addChild(sw)
    displayRoot.addChild(appState.textProjection.get())
    displaySS = displayRoot.getOrCreateStateSet()
    displaySS.setMode(GL_LIGHTING, StateAttribute.OFF)
    displaySS.setMode(GL_DEPTH_TEST, StateAttribute.OFF)
    texCamera = Camera()
    texCamera.setGraphicsContext(gc)
    texCamera.setClearMask(GL_COLOR_BUFFER_BIT)
    texCamera.setClearColor(Vec4(0.0, 0.0, 0.0, 0.0))
    texCamera.setReferenceFrame(Camera.ABSOLUTE_RF)
    texCamera.setViewport(0, 0, width, height)
    texCamera.setDrawBuffer(GL_BACK)
    texCamera.setReadBuffer(GL_BACK)
    texCamera.addChild(displayRoot)
    texCamera.setAllowEventFocus(False)
    texCamera.setCullingMode(CullSettings.NO_CULLING)
    texCamera.setProjectionResizePolicy(Camera.FIXED)
    viewer.addSlave(texCamera, Matrixd(), Matrixd(), False)
    viewer.addEventHandler(ConfigHandler(appState.get()))

    # add model to the viewer.
    sceneRoot = Group()
    sceneSS = sceneRoot.getOrCreateStateSet()
    depth = Depth(Depth.GEQUAL, 1.0, 0.0)
    sceneSS.setAttributeAndModes(depth,(StateAttribute.ON
                                         | StateAttribute.OVERRIDE))
#if 0
    # Hack to work around Blender osg export bug
    sceneSS.setAttributeAndModes(CullFace(CullFace.BACK))
#endif
    sceneRoot.addChild(loadedModel.get())
    appState.setStateFromConfig(validConfigs[0])
    appState.updateNear()
    viewer.addEventHandler(DepthHandler(appState.get(), depth))
    # add the help handler
    viewer.addEventHandler(osgViewer
                           .HelpHandler(arguments.getApplicationUsage()))

    viewer.setSceneData(sceneRoot)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
