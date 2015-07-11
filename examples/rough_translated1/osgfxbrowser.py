#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgfxbrowser"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgFX
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgfxbrowser.
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


#include "Frame.h"

#include <osgText/Text>

namespace osgfxbrowser 

Frame.Frame()
:    osg.Geode(),
    bgcolor_(0.5f, 0.5f, 0.5f, 1.0f),
    rect_(0, 0, 100, 100),
    caption_("Frame")

Frame.Frame( Frame copy,  osg.CopyOp copyop)
:    osg.Geode(copy, copyop),
    bgcolor_(copy.bgcolor_),
    rect_(copy.rect_),
    caption_(copy.caption_)

void Frame.rebuild()
    zPos =  -0.1f

    removeDrawables(0, getNumDrawables())
    addDrawable(build_quad(rect_, bgcolor_))
    addDrawable(build_quad(Rect(rect_.x0 + 4, rect_.y1 - 24, rect_.x1 - 4, rect_.y1 - 4), osg.Vec4(0, 0, 0, bgcolor_.w()), false, zPos))

    osg.ref_ptr<osgText.Text> caption_text = new osgText.Text
    caption_text.setText(caption_)
    caption_text.setColor(osg.Vec4(1, 1, 1, 1))
    caption_text.setAlignment(osgText.Text.CENTER_CENTER)
    caption_text.setFont("fonts/arial.ttf")
    caption_text.setCharacterSize(16)
    caption_text.setFontResolution(16, 16)
    caption_text.setPosition(osg.Vec3((rect_.x0 + rect_.x1) / 2, rect_.y1 - 15, zPos*2.0f))
    addDrawable(caption_text.get())

    rebuild_client_area(Rect(rect_.x0 + 4, rect_.y0 + 4, rect_.x1 - 4, rect_.y1 - 28))

osg.Geometry *Frame.build_quad( Rect rect,  osg.Vec4 color, bool shadow, float z)
    shadow_space =  8
    shadow_size =  10

    osg.ref_ptr<osg.Geometry> geo = new osg.Geometry
    osg.ref_ptr<osg.Vec3Array> vx = new osg.Vec3Array

    vx.push_back(osg.Vec3(rect.x0, rect.y0, z))
    vx.push_back(osg.Vec3(rect.x1, rect.y0, z))
    vx.push_back(osg.Vec3(rect.x1, rect.y1, z))
    vx.push_back(osg.Vec3(rect.x0, rect.y1, z))

    if shadow : 
        vx.push_back(osg.Vec3(rect.x0+shadow_space, rect.y0-shadow_size, z))
        vx.push_back(osg.Vec3(rect.x1+shadow_size, rect.y0-shadow_size, z))
        vx.push_back(osg.Vec3(rect.x1, rect.y0, z))
        vx.push_back(osg.Vec3(rect.x0+shadow_space, rect.y0, z))

        vx.push_back(osg.Vec3(rect.x1, rect.y1-shadow_space, z))
        vx.push_back(osg.Vec3(rect.x1, rect.y0, z))
        vx.push_back(osg.Vec3(rect.x1+shadow_size, rect.y0-shadow_size, z))
        vx.push_back(osg.Vec3(rect.x1+shadow_size, rect.y1-shadow_space, z))

    geo.setVertexArray(vx.get())

    osg.ref_ptr<osg.Vec4Array> clr = new osg.Vec4Array
    clr.push_back(color)
    clr.push_back(color)
    clr.push_back(color)
    clr.push_back(color)

    if shadow : 

        alpha =  color.w() * 0.5f
        black =  osg.Vec3(0, 0, 0)

        clr.push_back(osg.Vec4(black, 0))
        clr.push_back(osg.Vec4(black, 0))
        clr.push_back(osg.Vec4(black, alpha))
        clr.push_back(osg.Vec4(black, alpha))

        clr.push_back(osg.Vec4(black, alpha))
        clr.push_back(osg.Vec4(black, alpha))
        clr.push_back(osg.Vec4(black, 0))
        clr.push_back(osg.Vec4(black, 0))

    geo.setColorArray(clr.get(), osg.Array.BIND_PER_VERTEX)

    geo.addPrimitiveSet(new osg.DrawArrays(GL_QUADS, 0, shadow? 12: 4))

    return geo.release()

# -*-c++-*-
*
*  OpenSceneGraph example, osgfxbrowser.
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


#ifndef FRAME_H_
#define FRAME_H_

#include <osg/Geode>
#include <osg/Geometry>

namespace osgfxbrowser 

struct Rect 
	float x0, y0, x1, y1
	Rect() 
	Rect(float x0_, float y0_, float x1_, float y1_): x0(x0_), y0(y0_), x1(x1_), y1(y1_) 
	inline float width()   return x1 - x0 
	inline float height()   return y0 - y1 


class Frame: public osg.Geode 
public:
	Frame()
	Frame( Frame copy,  osg.CopyOp copyop = osg.CopyOp.SHALLOW_COPY)

	META_Node(osgfxbrowser, Frame)

	inline  str getCaption()                return caption_ 
	inline void setCaption( str caption)         caption_ = caption 

	inline  osg.Vec4 getBackgroundColor()          return bgcolor_ 
	inline void setBackgroundColor( osg.Vec4 bgcolor)   bgcolor_ = bgcolor 

	inline  Rect getRect()                  return rect_ 
	inline void setRect( Rect rect)              rect_ = rect 

	static osg.Geometry *build_quad( Rect rect,  osg.Vec4 color, bool shadow = true, float z = 0)

	virtual void rebuild()

protected:
	virtual ~Frame() 
	Frame operator()( Frame )  return *this 	

	virtual void rebuild_client_area( Rect  #client_rect) 

private:
	bgcolor_ = osg.Vec4()
	rect_ = Rect()
	caption_ = str()



#endif
# OpenSceneGraph example, osgfxbrowser.
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


#include <osg/Group>
#include <osg/Geometry>
#include <osg/Geode>
#include <osg/Projection>
#include <osg/MatrixTransform>
#include <osg/BlendFunc>
#include <osg/LightSource>

#include <osgViewer/Viewer>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osgText/Text>

#include <osgUtil/Optimizer>

#include <osgGA/GUIEventAdapter>
#include <osgGA/GUIActionAdapter>

#include <osgFX/Registry>
#include <osgFX/Effect>

#include "Frame.h"

#include <vector>
#include <string>
#include <iostream>

class RotateCallback: public osg.NodeCallback 
public:
    RotateCallback(): osg.NodeCallback(), enabled_(true) 
    void operator()(osg.Node* node, osg.NodeVisitor *nv)
        xform =  dynamic_cast<osg.MatrixTransform *>(node)
        if xform  enabled_ : 
            t =  nv.getFrameStamp().getSimulationTime()
            xform.setMatrix(osg.Matrix.rotate(t, osg.Vec3(0, 0, 1)))
        traverse(node, nv)

    enabled_ = bool()



# yes, I know global variables are not good things in C++
# but in this case it is useful... :-P
*rotate_cb = RotateCallback()


class EffectPanel: public osgfxbrowser.Frame 
public:

    class KeyboardHandler: public osgGA.GUIEventHandler 
    public:
        KeyboardHandler(EffectPanel* ep): ep_(ep) 

        bool handle( osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter )
            if ea.getEventType() == osgGA.GUIEventAdapter.KEYDOWN : 
                if ea.getKey() == osgGA.GUIEventAdapter.KEY_Right : 
                    ep_.setEffectIndex(ep_.getEffectIndex()+1)
                    true = return()
                if ea.getKey() == osgGA.GUIEventAdapter.KEY_Left : 
                    ep_.setEffectIndex(ep_.getEffectIndex()-1)
                    true = return()
                if ea.getKey() == osgGA.GUIEventAdapter.KEY_Return : 
                    ep_.setNodeMask(0xffffffff - ep_.getNodeMask())
                    true = return()
                if ea.getKey() == osgGA.GUIEventAdapter.KEY_Delete : 
                    ep_.setEffectsEnabled(!ep_.getEffectsEnabled())
                    true = return()
                if ea.getKey() == 'x' : 
                    osgDB.writeNodeFile(*ep_.getRoot(), "osgfx_model.osgt")
                    print "written nodes to \"osgfx_model.osgt\"\n"
                    true = return()
                if ea.getKey() == 'r' : 
                    rotate_cb.enabled_ = !rotate_cb.enabled_
                    true = return()

            false = return()

    private:
        osg.ref_ptr<EffectPanel> ep_
    

    EffectPanel()
    :    osgfxbrowser.Frame(),
        _selected_fx(-1),
        _fxen(true),
        _root(new osg.Group),
        _hints_color(0.75f, 0.75f, 0.75f, 1.0f),
        _name_color(1, 1, 1, 1),
        _desc_color(1, 1, 0.7f, 1)
        setBackgroundColor(osg.Vec4(0.3f, 0.1f, 0.15f, 0.75f))

        print "INFO: available osgFX effects:\n"
        emap =  osgFX.Registry.instance().getEffectMap()
        for (osgFX.Registry.EffectMap.const_iterator i=emap.begin() i!=emap.end() ++i) 
            print "INFO: \t", i.first, "\n"
            osg.ref_ptr<osgFX.Effect> effect = static_cast<osgFX.Effect *>(i.second.cloneType())
            _effects.push_back(effect.get())            

        print "INFO: ", emap.size(), " effect(s) ready.\n"

        if !_effects.empty() : 
            _selected_fx = 0

    inline osg.Group* getRoot()  return _root.get() 
    inline void setRoot(osg.Group* node)  _root = node 

    inline osg.Node* getScene()  return _scene.get() 
    inline void setScene(osg.Node* node)  _scene = node 

    inline bool getEffectsEnabled()   return _fxen 
    inline void setEffectsEnabled(bool v) 
        _fxen = v 
        if getSelectedEffect() : 
            getSelectedEffect().setEnabled(_fxen)

    inline int getEffectIndex()   return _selected_fx 
    inline void setEffectIndex(int i)
        if i >= static_cast<int>(_effects.size()) : i = 0
        if i < 0 : i = static_cast<int>(_effects.size()-1)        
        _selected_fx = i
        rebuild()

    inline osgFX.Effect *getSelectedEffect()
        if _selected_fx >= 0  _selected_fx < static_cast<int>(_effects.size()) : 
            return _effects[_selected_fx].get()
        return 0

protected:
    def rebuild_client_area(client_rect):
                zPos =  -0.1 # note from Robert, was 0.1f, but now must be -0.1f to keep text visible??#!? due
                                   # to some other change in the OSG not tracked down yet...
        
        osg.ref_ptr<osgText.Font> arial = osgText.readFontFile("fonts/arial.ttf")

        osg.ref_ptr<osgText.Text> hints = new osgText.Text
        hints.setFont(arial.get())
        hints.setColor(_hints_color)
        hints.setAlignment(osgText.Text.CENTER_BOTTOM)
        hints.setCharacterSize(13)
        hints.setPosition(osg.Vec3((client_rect.x0+client_rect.x1)/2, client_rect.y0 + 4, zPos))
        hints.setText("<RETURN> show/hide this panel      <LEFT> previous effect      <RIGHT> next effect      <DEL> enable/disable effects      'x' save to file      'r' rotate/stop")
        addDrawable(hints.get())

        effect_name =  "No Effect Selected"
        effect_description =  ""

        if _selected_fx >= 0  _selected_fx < static_cast<int>(_effects.size()) : 
            effect_name = _effects[_selected_fx].effectName()
            author_name =  _effects[_selected_fx].effectAuthor()
            if !author_name.empty() : 
                effect_description = author_name = "AUTHOR: " + str(_effects[_selected_fx].effectAuthor()) + str("\n\n")
            effect_description += "DESCRIPTION:\n" + str(_effects[_selected_fx].effectDescription())            

            if _scene.valid()  _root.valid() : 
                _root.removeChildren(0, _root.getNumChildren())
                osg.ref_ptr<osgFX.Effect> effect = _effects[_selected_fx].get()
                effect.setEnabled(_fxen)
                effect.removeChildren(0, effect.getNumChildren())
                effect.addChild(_scene.get())
                effect.setUpDemo()
                _root.addChild(effect.get())

        osg.ref_ptr<osgText.Text> ename = new osgText.Text
        ename.setFont(arial.get())
        ename.setColor(_name_color)
        ename.setAlignment(osgText.Text.CENTER_TOP)
        ename.setCharacterSize(32)
        ename.setPosition(osg.Vec3((client_rect.x0 + client_rect.x1) / 2, client_rect.y1 - 22, zPos))
        ename.setText(effect_name)
        addDrawable(ename.get())

        osg.ref_ptr<osgText.Text> edesc = new osgText.Text
        edesc.setMaximumWidth(client_rect.width() - 16)
        edesc.setFont(arial.get())
        edesc.setColor(_desc_color)
        edesc.setAlignment(osgText.Text.LEFT_TOP)
        edesc.setCharacterSize(16)
        edesc.setPosition(osg.Vec3(client_rect.x0 + 8, client_rect.y1 - 60, zPos))
        edesc.setText(effect_description)
        addDrawable(edesc.get())

private:
    _selected_fx = int()
    typedef std.vector<osg.ref_ptr<osgFX.Effect> > Effect_list
    _effects = Effect_list()
    _fxen = bool()
    osg.ref_ptr<osg.Group> _root
    osg.ref_ptr<osg.Node> _scene
    _hints_color = osg.Vec4()
    _name_color = osg.Vec4()
    _desc_color = osg.Vec4()



def build_hud_base(root):
    osg.ref_ptr<osg.Projection> proj = new osg.Projection(osg.Matrix.ortho2D(0, 1024, 0, 768))
    proj.setCullingActive(false)
    root.addChild(proj.get())

    osg.ref_ptr<osg.MatrixTransform> xform = new osg.MatrixTransform(osg.Matrix.identity())
    xform.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    proj.addChild(xform.get())

    ss =  xform.getOrCreateStateSet()
    ss.setRenderBinDetails(100, "RenderBin")
    ss.setMode(GL_LIGHTING, osg.StateAttribute.OFF)
    ss.setMode(GL_DEPTH_TEST, osg.StateAttribute.OFF)

    osg.ref_ptr<osg.BlendFunc> bf = new osg.BlendFunc
    ss.setAttributeAndModes(bf.get())

    return xform.release()

def build_gui(root):
    osg.ref_ptr<osg.Group> hud = build_hud_base(root)

    osg.ref_ptr<EffectPanel> effect_panel = new EffectPanel
    effect_panel.setCaption("osgFX Effect Browser")
    effect_panel.setRect(osgfxbrowser.Rect(20, 20, 1000, 280))    

    hud.addChild(effect_panel.get())

    return effect_panel.release()

def build_world(root, scene, viewer):
    osg.ref_ptr<EffectPanel> effect_panel = build_gui(root)
    effect_panel.setScene(scene)
    effect_panel.rebuild()

    viewer.addEventHandler(new EffectPanel.KeyboardHandler(effect_panel.get()))

    root.addChild(effect_panel.getRoot())

int main(int argc, char *argv[])
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc, argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName() + " is a simple browser that allows you to apply osgFX effects to models interactively.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName() + " [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help", "Display this information")
    arguments.getApplicationUsage().addKeyboardMouseBinding("Left", "Apply previous effect")
    arguments.getApplicationUsage().addKeyboardMouseBinding("Right", "Apply next effect")
    arguments.getApplicationUsage().addKeyboardMouseBinding("Del", "Enable or disable osgFX")
    arguments.getApplicationUsage().addKeyboardMouseBinding("Return", "Show or hide the effect information panel")
    arguments.getApplicationUsage().addKeyboardMouseBinding("x", "Save the scene graph with current effect applied")


    # construct the viewer.
    viewer = osgViewer.Viewer()

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") : 
        arguments.getApplicationUsage().write(std.cout)
        return 1

    threading =  osgViewer.Viewer.SingleThreaded
    while arguments.read("--SingleThreaded") : threading = osgViewer.Viewer.SingleThreaded
    while arguments.read("--CullDrawThreadPerContext") : threading = osgViewer.Viewer.CullDrawThreadPerContext
    while arguments.read("--DrawThreadPerContext") : threading = osgViewer.Viewer.DrawThreadPerContext
    while arguments.read("--CullThreadPerCameraDrawThreadPerContext") : threading = osgViewer.Viewer.CullThreadPerCameraDrawThreadPerContext

    viewer.setThreadingModel(threading)

    # setup stencil buffer for Outline f/x.
    osg.DisplaySettings.instance().setMinimumNumStencilBits(1)
    unsigned int clearMask = viewer.getCamera().getClearMask()
    viewer.getCamera().setClearMask(clearMask | GL_STENCIL_BUFFER_BIT)
    viewer.getCamera().setClearStencil(0)
 
    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() : 
        arguments.writeErrorMessages(std.cout)
        return 1

    # read the scene from the list of file specified commandline args.
    osg.ref_ptr<osg.Node> loadedModel = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default mode instead.
    if !loadedModel : loadedModel = osgDB.readNodeFile("dumptruck.osgt")
  
    if !loadedModel :
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # optimize the scene graph, remove redundant nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel.get())

    # set up a transform to rotate the model
    osg.ref_ptr<osg.MatrixTransform> xform = new osg.MatrixTransform
    rotate_cb = new RotateCallback
    xform.setUpdateCallback(rotate_cb)
    xform.addChild(loadedModel.get())

    osg.ref_ptr<osg.Light> light = new osg.Light
    light.setLightNum(0)
    light.setDiffuse(osg.Vec4(1, 1, 1, 1))
    light.setSpecular(osg.Vec4(1, 1, 0.8f, 1))
    light.setAmbient(osg.Vec4(0.2f, 0.2f, 0.2f, 0.2f))
    light.setPosition(osg.Vec4(1, -1, 1, 0))

    osg.ref_ptr<osg.LightSource> root = new osg.LightSource
    root.setLight(light.get())
    root.setLocalStateSetModes()

    build_world(root.get(), xform.get(), viewer)

    # set the scene to render
    viewer.setSceneData(root.get())

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
