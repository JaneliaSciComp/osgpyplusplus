#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganimationviewer"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer
from osgpypp import osgWidget

#  -*-c++-*-
 *  Copyright (C) 2008 Cedric Pinson <mornifle@plopbyte.net>
 *
 * This library is open source and may be redistributed and/or modified under
 * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or
 * (at your option) any later version.  The full license is in LICENSE file
 * included with this distribution, and on the openscenegraph.org website.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * OpenSceneGraph Public License for more details.
 *
 * Authors:
 * Cedric Pinson <mornifle@plopbyte.net>
 * jeremy Moles <jeremy@emperorlinux.com>


#include "AnimtkViewerKeyHandler"
#include "AnimtkViewerGUI"

#include <iostream>
#include <osg/io_utils>
#include <osg/Geometry>
#include <osg/MatrixTransform>
#include <osg/Geode>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgWidget/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgDB/ReadFile>
#include <osgAnimation/AnimationManagerBase>
#include <osgAnimation/Bone>

WIDTH =  1440
HEIGHT =  900


def createAxis():
    geode =  new osg.Geode()
    geometry =  new osg.Geometry()
    vertices =  new osg.Vec3Array()
    colors =  new osg.Vec4Array()

    vertices.push_back(osg.Vec3(0.0f, 0.0f, 0.0f))
    vertices.push_back(osg.Vec3(1.0f, 0.0f, 0.0f))
    vertices.push_back(osg.Vec3(0.0f, 0.0f, 0.0f))
    vertices.push_back(osg.Vec3(0.0f, 1.0f, 0.0f))
    vertices.push_back(osg.Vec3(0.0f, 0.0f, 0.0f))
    vertices.push_back(osg.Vec3(0.0f, 0.0f, 1.0f))

    colors.push_back(osg.Vec4(1.0f, 0.0f, 0.0f, 1.0f))
    colors.push_back(osg.Vec4(1.0f, 0.0f, 0.0f, 1.0f))
    colors.push_back(osg.Vec4(0.0f, 1.0f, 0.0f, 1.0f))
    colors.push_back(osg.Vec4(0.0f, 1.0f, 0.0f, 1.0f))
    colors.push_back(osg.Vec4(0.0f, 0.0f, 1.0f, 1.0f))
    colors.push_back(osg.Vec4(0.0f, 0.0f, 1.0f, 1.0f))

    geometry.setVertexArray(vertices)
    geometry.setColorArray(colors, osg.Array.BIND_PER_VERTEX)
    geometry.addPrimitiveSet(new osg.DrawArrays(osg.PrimitiveSet.LINES, 0, 6))
    geometry.getOrCreateStateSet().setMode(GL_LIGHTING, false)

    geode.addDrawable(geometry)

    geode = return()


struct AnimationManagerFinder : public osg.NodeVisitor
    osg.ref_ptr<osgAnimation.BasicAnimationManager> _am
    AnimationManagerFinder() : osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN) 
    def apply(node):
        if _am.valid() :
            return
        if node.getUpdateCallback() : 
            b =  dynamic_cast<osgAnimation.AnimationManagerBase*>(node.getUpdateCallback())
            if b : 
                _am = new osgAnimation.BasicAnimationManager(*b)
                return
        traverse(node)



struct AddHelperBone : public osg.NodeVisitor
    AddHelperBone() : osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN) 
    def apply(node):
        bone =  dynamic_cast<osgAnimation.Bone*>(node)
        if bone :
            bone.addChild(createAxis())
        traverse(node)


def main(argc, argv):
    arguments = osg.ArgumentParser(argc, argv)
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is an example for viewing osgAnimation animations.")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","List command line options.")
    arguments.getApplicationUsage().addCommandLineOption("--drawbone","draw helps to display bones.")

    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout, osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 0

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout, osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    drawBone =  false
    if arguments.read("--drawbone") :
        drawBone = true

    viewer = osgViewer.Viewer(arguments)
    osg.ref_ptr<osg.Group> group = new osg.Group()

    node =  dynamic_cast<osg.Group*>(osgDB.readNodeFiles(arguments)) #dynamic_cast<osgAnimation.AnimationManager*>(osgDB.readNodeFile(psr[1]))
    if !node :
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # Set our Singleton's model.
    finder = AnimationManagerFinder()
    node.accept(finder)
    if finder._am.valid() : 
        node.setUpdateCallback(finder._am.get())
        AnimtkViewerModelController.setModel(finder._am.get())
     else: 
        osg.notify(osg.WARN), "no osgAnimation.AnimationManagerBase found in the subgraph, no animations available"

    if drawBone : 
        osg.notify(osg.INFO), "Add Bones Helper"
        addHelper = AddHelperBone()
        node.accept(addHelper)
    node.addChild(createAxis())

    gui =  new AnimtkViewerGUI(viewer, WIDTH, HEIGHT, 0x1234)
    camera =  gui.createParentOrthoCamera()

    node.setNodeMask(0x0001)

    group.addChild(node)
    group.addChild(camera)

    viewer.addEventHandler(new AnimtkKeyEventHandler())
    viewer.addEventHandler(new osgViewer.StatsHandler())
    viewer.addEventHandler(new osgViewer.WindowSizeHandler())
    viewer.addEventHandler(new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()))
    viewer.addEventHandler(new osgWidget.MouseHandler(gui))
    viewer.addEventHandler(new osgWidget.KeyboardHandler(gui))
    viewer.addEventHandler(new osgWidget.ResizeHandler(gui, camera))
    viewer.setSceneData(group.get())

    viewer.setUpViewInWindow(40, 40, WIDTH, HEIGHT)

    return viewer.run()
#  -*-c++-*- 
 *  Copyright (C) 2008 Cedric Pinson <mornifle@plopbyte.net>
 *
 * This library is open source and may be redistributed and/or modified under  
 * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or 
 * (at your option) any later version.  The full license is in LICENSE file
 * included with this distribution, and on the openscenegraph.org website.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
 * OpenSceneGraph Public License for more details.
 *
 * Authors:
 * Cedric Pinson <mornifle@plopbyte.net>
 * jeremy Moles <jeremy@emperorlinux.com>


#include "AnimtkViewer"
#include "AnimtkViewerGUI"

#include <osg/Version>
#include <osgWidget/WindowManager>
#include <osgAnimation/EaseMotion>

IMAGE_PATH =  "osgWidget/"

template <class T>
struct Sampler: public osg.Drawable.UpdateCallback 
    _motion = T()
    Sampler() 


typedef Sampler<osgAnimation.OutQuadMotion> WidgetSampler

struct ButtonFunctor: public WidgetSampler 
    _direction = float()
    _previous = float()

    _speed =  float()
    
    ButtonFunctor(): _speed(5)  _direction = -_speed _previous = 0

    bool enter(osgWidget.Event)
        _direction = _speed 
        true = return()

    bool leave(osgWidget.Event)
        _direction = -_speed 
        true = return()

    def update(nv, geom):
        f =  nv.getFrameStamp()
        dt =  f.getSimulationTime() - _previous
        _previous = f.getSimulationTime()
        update(dt,dynamic_cast<osgWidget.Widget*>(geom))

    def update(t, w):
        if !w : return
        _motion.update(t*_direction) 
        val =  _motion.getValue()*0.5
        val += 0.5
        if val >= 1.0 :
            val = 1.0
        w.setColor(osg.Vec4(val, val, val, 1))


struct LabelFunctor: public WidgetSampler 
    _previous = float()
    _active = bool()

    _fadeOutTime =  float()

    _scaleSampler = osgAnimation.OutCubicMotion()

    LabelFunctor():
        _fadeOutTime(1.5f) 
        _previous = 0.0f
        _active   = false

        _scaleSampler = osgAnimation.OutCubicMotion(0.5, 1.0, 1.0)

    def setActive(active):
        _active = active

        if active : _motion.reset()

        _scaleSampler.reset()

    def update(nv, geom):
        f =  nv.getFrameStamp()

        st =  f.getSimulationTime()
        dt =  st - _previous

        _previous = st

        if !_active : return

        update(dt, dynamic_cast<osgWidget.Label*>(geom))
        updateScale(dt, dynamic_cast<osgWidget.Label*>(geom))

    def update(t, w):
        if !w : return

        _motion.update(t / _fadeOutTime)

        val =  _motion.getValue()

        if val >= 1.0f : 
            _motion.reset()
            _active = false

        w.setFontColor(osg.Vec4(0.0f, 0.0f, 0.0f, (1.0f - val) * 0.7f))

    def updateScale(t, w):
        _scaleSampler.update(t)
        val =  _scaleSampler.getValue()
        win =  w.getParent()
        win.setScale(val)
        win.update()




struct ListFunctor: public osg.NodeCallback 
    _previous = float()
    _direction = int()

    _transformSampler = osgAnimation.InQuadMotion()

    ListFunctor() 
        _direction = 1
        _previous  = 0

        _transformSampler.update(1.0f)

    def toggleShown():
        if _direction == 1 : _direction = -1

        _direction =  1

    virtual void operator()(osg.Node* node, osg.NodeVisitor* nv) 
        f =  nv.getFrameStamp()

        st =  f.getSimulationTime()
        dt =  st - _previous

        _previous = st

        _transformSampler.update((dt * _direction) / 0.5f)

        val =  _transformSampler.getValue()

        if val > 1.0f || val < 0.0f : return

        win =  dynamic_cast<osgWidget.Window*>(node)

        w =  win.getWidth()
        wmw =  win.getWindowManager().getWidth()

        win.setX((wmw - w) + (val * w))
        win.update()



# This is a temporary hack to "prevent" dragging on Widgets and Windows.
bool eatDrag(osgWidget.Event) 
    true = return()

AnimtkViewerGUI.AnimtkViewerGUI(osgViewer.View* view, float w, float h, unsigned int mask):
    osgWidget.WindowManager(view, w, h, mask, 0) 
    _createButtonBox()
    _createLabelBox()
    _createListBox()

    _labelBox.setAnchorHorizontal(osgWidget.Window.HA_LEFT)
    _labelBox.setY(74.0f)
    _labelBox.setVisibilityMode(osgWidget.Window.VM_ENTIRE)

    _listBox.setOrigin(getWidth(), 74.0f)

    addChild(_buttonBox.get())
    addChild(_labelBox.get())
    addChild(_listBox.get())

    resizeAllWindows()

    # Remember, you can't call resizePercent until AFTER the box is parented
    # by a WindowManager how could it possibly resize itself if it doesn't know
    # how large it's viewable area is?
    _buttonBox.resizePercent(100.0f)
    _buttonBox.resizeAdd(0.0f, 10.0f)

osgWidget.Widget* AnimtkViewerGUI._createButton( str name) 
    b =  new osgWidget.Widget(name, 64.0f, 64.0f)
    
    if !b : return 0

    b.setImage(IMAGE_PATH + name + ".png", true)
    b.setEventMask(osgWidget.EVENT_MASK_MOUSE_DRAG)

    bt =  new ButtonFunctor()
    b.setUpdateCallback(bt)
    
    b.addCallback(new osgWidget.Callback(ButtonFunctor.enter, bt, osgWidget.EVENT_MOUSE_ENTER))
    b.addCallback(new osgWidget.Callback(ButtonFunctor.leave, bt, osgWidget.EVENT_MOUSE_LEAVE))
    b.addCallback(new osgWidget.Callback(AnimtkViewerGUI._buttonPush, this, osgWidget.EVENT_MOUSE_PUSH))
    b.addCallback(new osgWidget.Callback(eatDrag, osgWidget.EVENT_MOUSE_DRAG))

    b = return()

bool AnimtkViewerGUI._listMouseHover(osgWidget.Event ev) 
    l =  dynamic_cast<osgWidget.Label*>(ev.getWidget())

    if !l : return false

    if ev.type == osgWidget.EVENT_MOUSE_ENTER : l.setFontColor(1.0f, 1.0f, 1.0f, 1.0f)

    else: if ev.type == osgWidget.EVENT_MOUSE_LEAVE : l.setFontColor(1.0f, 1.0f, 1.0f, 0.3f)

    else: if ev.type == osgWidget.EVENT_MOUSE_PUSH : 
        AnimtkViewerModelController.instance().playByName(ev.getWidget().getName())
    
    else: return false

    true = return()

bool AnimtkViewerGUI._buttonPush(osgWidget.Event ev) 
    if !ev.getWidget() : return false

    l =  static_cast<osgWidget.Label*>(_labelBox.getByName("label"))

    if !l : return false

    lf =  dynamic_cast<LabelFunctor*>(l.getUpdateCallback())

    if !lf : return false

    # We're safe at this point, so begin processing.
    mc =  AnimtkViewerModelController.instance()
    name =  ev.getWidget().getName()

    if name == "play" : mc.play()

    else: if name == "stop" : mc.stop()

    else: if name == "next" : 
        mc.next()

        l.setFontColor(osg.Vec4(0.0f, 0.0f, 0.0f, 0.7f))
        l.setLabel(mc.getCurrentAnimationName())
        lf.setActive(true)
    
    else: if name == "back" : 
        mc.previous()
        
        l.setFontColor(osg.Vec4(0.0f, 0.0f, 0.0f, 0.7f))
        l.setLabel(mc.getCurrentAnimationName())
        lf.setActive(true)

    else: if name == "pause" : 

    else: if name == "open" : 
        lsf =  dynamic_cast<ListFunctor*>(_listBox.getUpdateCallback())

        if !lsf : return false

        lsf.toggleShown()

    else: return false

    true = return()

void AnimtkViewerGUI._createButtonBox() 
    _buttonBox = new osgWidget.Box("buttonBox", osgWidget.Box.HORIZONTAL)

    space =  new osgWidget.Widget("nullSpace", 0.0f, 0.0f)
    back =  _createButton("back")
    next =  _createButton("next")
    play =  _createButton("play")
    pause =  _createButton("pause")
    stop =  _createButton("stop")
    open =  _createButton("open")

    space.setCanFill(true)
    space.setColor(0.0f, 0.0f, 0.0f, 0.0f)

    _buttonBox.addWidget(space)
    _buttonBox.addWidget(back)
    _buttonBox.addWidget(next)
    _buttonBox.addWidget(play)
    _buttonBox.addWidget(pause)
    _buttonBox.addWidget(stop)
    _buttonBox.addWidget(open)
    _buttonBox.addWidget(osg.clone(space, "space1", osg.CopyOp.DEEP_COPY_ALL))
    _buttonBox.getBackground().setColor(0.0f, 0.0f, 0.0f, 0.7f)
    
    _buttonBox.setEventMask(osgWidget.EVENT_MASK_MOUSE_DRAG)
    _buttonBox.addCallback(new osgWidget.Callback(eatDrag, osgWidget.EVENT_MOUSE_DRAG))

void AnimtkViewerGUI._createListBox() 
    _listBox = new osgWidget.Box("listBox", osgWidget.Box.VERTICAL)

    amv = 
        AnimtkViewerModelController.instance().getAnimationMap()
        

    for(
        i =  amv.begin()
        i != amv.end()
        i++
        ) 
        label =  new osgWidget.Label(*i)

        label.setCanFill(true)
        label.setFont("fonts/Vera.ttf")
        label.setFontSize(15)
        label.setFontColor(1.0f, 1.0f, 1.0f, 0.3f)
        label.setPadding(5.0f)
        label.setAlignHorizontal(osgWidget.Widget.HA_RIGHT)
        label.setLabel(*i)
        label.setEventMask(osgWidget.EVENT_MASK_MOUSE_DRAG)
        label.addCallback(new osgWidget.Callback(AnimtkViewerGUI._listMouseHover, this, osgWidget.EVENT_MOUSE_ENTER))
        label.addCallback(new osgWidget.Callback(AnimtkViewerGUI._listMouseHover, this, osgWidget.EVENT_MOUSE_LEAVE))
        label.addCallback(new osgWidget.Callback(AnimtkViewerGUI._listMouseHover, this, osgWidget.EVENT_MOUSE_PUSH))

        _listBox.addWidget(label)

    lf =  new ListFunctor()

    _listBox.setUpdateCallback(lf)
    _listBox.getBackground().setColor(0.0f, 0.0f, 0.0f, 0.7f)

void AnimtkViewerGUI._createLabelBox() 
    _labelBox = new osgWidget.Box("labelBox", osgWidget.Box.VERTICAL)

    label =  new osgWidget.Label("label")
    
    label.setFont("fonts/Vera.ttf")
    label.setFontSize(50)
    label.setFontColor(0.0f, 0.0f, 0.0f, 0.7f)
    label.setAlignHorizontal(osgWidget.Widget.HA_LEFT)
    label.setPadding(10.0f)

    lf =  new LabelFunctor()
    label.setUpdateCallback(lf)

    _labelBox.addWidget(label)
    _labelBox.getBackground().setColor(0.0f, 0.0f, 0.0f, 0.0f)
#  -*-c++-*- 
 *  Copyright (C) 2008 Cedric Pinson <mornifle@plopbyte.net>
 *
 * This program is free software you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Authors:
 * 
 * Cedric Pinson <mornifle@plopbyte.net>
 *
 

#include "AnimtkViewerKeyHandler"

AnimtkKeyEventHandler.AnimtkKeyEventHandler()
    _actionKeys[List] = 'l'
    _actionKeys[Help] = 'h'
    _actionKeys[Play] = 'p'
    _actionKeys[Next] = ']'
    _actionKeys[Prev] = '['

void AnimtkKeyEventHandler.printUsage()  
    print (char) _actionKeys.find(Help).second, " for Help"
    print (char) _actionKeys.find(List).second, " for List"
    print (char) _actionKeys.find(Play).second, " for Play"
    print (char) _actionKeys.find(Next).second, " for select Next item"
    print (char) _actionKeys.find(Prev).second, " for select Previous item"


bool AnimtkKeyEventHandler.handle( osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter,
                                   osg.Object*, osg.NodeVisitor*)
    mc =  AnimtkViewerModelController.instance()
    if ea.getEventType() == osgGA.GUIEventAdapter.KEYDOWN : 
        if ea.getKey() == _actionKeys[List] : return mc.list()
        else: if ea.getKey() == _actionKeys[Play] : return mc.play()
        else: if ea.getKey() == _actionKeys[Next] : return mc.next()
        else: if ea.getKey() == _actionKeys[Prev] : return mc.previous()
        else: if ea.getKey() == _actionKeys[Help] : 
            printUsage()
            true = return()

    false = return()


if __name__ == "__main__":
    main(sys.argv)