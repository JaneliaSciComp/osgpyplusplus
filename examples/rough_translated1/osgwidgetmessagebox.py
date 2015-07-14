#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgwidgetmessagebox"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgDB
from osgpypp import osgWidget


# Translated from file 'osgwidgetmessagebox.cpp'

# -*-c++-*- osgWidget - Copyright Cedric Pinson 2008


#include <osgWidget/Util>
#include <osgWidget/WindowManager>
#include <osgWidget/Frame>
#include <osgWidget/Box>
#include <osgWidget/Widget>
#include <osgWidget/Types>
#include <osgDB/ReadFile>
#include <osgAnimation/EaseMotion>
#include <osg/io_utils>
#include <iostream>

MASK_2D = 0xF0000000

class MessageBox :
        
    createButtonOk = osgWidget.Frame*( str theme,  str text,  str font, int fontSize)
    createLabel = osgWidget.Label*( str string,  str font, int size,  osgWidget.Color color)
        
    _window = osgWidget.Frame()
    _button = osgWidget.Frame()
        
    getButton = osgWidget.Frame*()
    getWindow = osgWidget.Frame*()

    create = bool( str themeMessage, 
                 str themeButton,
                 str titleText,
                 str messageText,
                 str buttonText,
                 str font,
                int fontSize)


osgWidget.Frame* MessageBox.getButton()  return _button 
osgWidget.Frame* MessageBox.getWindow()  return _window 

class AlphaSetterVisitor (osg.NodeVisitor) :
_alpha = float()
    AlphaSetterVisitor( float alpha = 1.0):osg.NodeVisitor(TRAVERSE_ALL_CHILDREN)  _alpha = alpha

    def apply(node):

        
        win = dynamic_cast<osgWidget.Window*>(node)

        if win : 
#             osgWidget.warn(), "I am in Window: ", win.getName()

            for (osgWidget.Window.Iterator it = win.begin() it  not = win.end() it++)
#                 osgWidget.warn(), "   I am operating on Widget: ", it.getName()
                
                color = it.getColor()
                color[3] = color[3] *_alpha
                it.setColor(color)
                color = win.getBackground().getColor()
                color[3] = color[3] *_alpha
                win.getBackground().setColor(color)
        traverse(node)



class ColorSetterVisitor (osg.NodeVisitor) :
_color = osgWidget.Color()
    ColorSetterVisitor(  osgWidget.Color color):osg.NodeVisitor(TRAVERSE_ALL_CHILDREN)  _color = color

    def apply(node):

        
        win = dynamic_cast<osgWidget.Window*>(node)

        if win : 
#            osgWidget.warn(), "I am in Window: ", win.getName()

            for (osgWidget.Window.Iterator it = win.begin() it  not = win.end() it++)
#                osgWidget.warn(), "   I am operating on Widget: ", it.getName()
                
#                 color = it.getColor()
#                 color[3] = color[3] *_alpha
                it.setColor(_color)
#                 color = win.getBackground().getColor()
#                 color[3] = color[3] *_alpha
                win.getBackground().setColor(osgWidget.Color(0,0,0,0))
        traverse(node)




struct EventOK : public osgWidget.Callback, osg.NodeCallback
    typedef osgAnimation.OutCubicMotion WidgetMotion
#    typedef osgAnimation.OutQuartMotion WidgetMotion
    _motionOver = WidgetMotion()
    _motionLeave = WidgetMotion()
    
    _lastUpdate = double()
    _defaultColor = osgWidget.Color()
    _overColor = osgWidget.Color()
    _over = bool()
    _frame = osgWidget.Frame()
    _width = float()
    _height = float()
    _matrix = osg.Matrix()
    EventOK(osgWidget.Frame* frame) : osgWidget.Callback(osgWidget.EVENT_ALL), _frame(frame) 
        _motionOver = WidgetMotion(0.0, 0.4)
        _motionLeave = WidgetMotion(0.0, 0.5)
        _defaultColor = _frame.getEmbeddedWindow().getColor()
        _overColor = osgWidget.Color(229.0/255.0,
                                      103.0/255.0,
                                      17.0/255,
                                      _defaultColor[3])
        _over  = False

    bool operator()(osgWidget.Event ev)
        if ev.type == osgWidget.EVENT_MOUSE_ENTER :
            _over = True
            _width = _frame.getWidth()
            _height = _frame.getHeight()
            _motionOver.reset()
            _matrix = _frame.getMatrix()
            #_frame.setMatrix(osg.Matrix.scale(2, 2, 1) * _frame.getMatrix())
            _frame.setScale(1.1) #osg.Matrix.scale(2, 2, 1) * _frame.getMatrix())
            _frame.update() #osg.Matrix.scale(2, 2, 1) * _frame.getMatrix())
            print "enter"
            return True
        elif ev.type == osgWidget.EVENT_MOUSE_LEAVE :
            _over = False
            _motionLeave.reset()
            #_frame.setMatrix(_matrix)
            _frame.setScale(1.0)
            _frame.update()
            print "leave"
            return True
        return False

    void operator()(osg.Node* node, osg.NodeVisitor* nv)
        if nv.getVisitorType() == osg.NodeVisitor.UPDATE_VISITOR :
            fs = nv.getFrameStamp()
            dt = fs.getSimulationTime() - _lastUpdate
            _lastUpdate = fs.getSimulationTime()

            if _frame.valid() :
                value = float()
                if _over :
                    _motionOver.update(dt)
                    value = _motionOver.getValue()
                else:
                    _motionLeave.update(dt)
                    value = 1.0 - _motionLeave.getValue()

                c = _defaultColor + ((_overColor - _defaultColor) * value)
                colorSetter = ColorSetterVisitor(c)
                _frame.accept(colorSetter)
        node.traverse(*nv)




osgWidget.Label* MessageBox.createLabel( str string,  str font, int size,  osgWidget.Color color)
    label = osgWidget.Label("", "")
    label.setFont(font)
    label.setFontSize(size)
    label.setFontColor(color)
    label.setColor(osgWidget.Color(0,0,0,0))
    label.setLabel(string)
    label.setCanFill(True)
    return label

osgWidget.Frame* MessageBox.createButtonOk( str theme, 
                                                  str text, 
                                                  str font, 
                                                 int fontSize)
    frame = osgWidget.Frame.createSimpleFrameFromTheme(
        "ButtonOK",
        osgDB.readImageFile(theme),
        300.0, 
        50.0,
        osgWidget.Frame.FRAME_TEXTURE
        )
    frame.getBackground().setColor(0.0, 0.0, 0.0, 0.0)

    label = createLabel(text, font, fontSize, osgWidget.Color(0,0,0,1))

    box = osgWidget.Box("HBOX", osgWidget.Box.HORIZONTAL)
    box.addWidget(label)
    box.resize()
    colorBack = frame.getEmbeddedWindow().getColor()
    box.getBackground().setColor(colorBack)
    frame.getEmbeddedWindow().setWindow(box)
    box.setVisibilityMode(osgWidget.Window.VM_ENTIRE)
    box.setEventMask(osgWidget.EVENT_NONE)
    frame.setVisibilityMode(osgWidget.Window.VM_ENTIRE)

    frame.resizeFrame(box.getWidth(), box.getHeight())
    frame.resizeAdd(0, 0)

    event = EventOK(frame)
    frame.setUpdateCallback(event)
    frame.addCallback(event)

    return frame.release()

bool MessageBox.create( str themeMessage, 
                         str themeButton,
                         str titleText,
                         str messageText,
                         str buttonText,
                         str font,
                        int fontSize)

    frame = osgWidget.Frame.createSimpleFrameFromTheme(
        "error",
        osgDB.readImageFile(themeMessage),
        300.0,
        50.0,
        osgWidget.Frame.FRAME_ALL
        )
    frame.getBackground().setColor(0.0, 0.0, 0.0, 0.0)

    labelText = createLabel(messageText, font, fontSize, osgWidget.Color(0,0,0,1))
    labelTitle = createLabel(titleText, font, fontSize+5, osgWidget.Color(0.4,0,0,1))

    box = osgWidget.Box("VBOX", osgWidget.Box.VERTICAL)

    _button = createButtonOk(themeButton, buttonText, font, fontSize)
    buttonOK = _button.embed()
    _button.setVisibilityMode(osgWidget.Window.VM_ENTIRE)
    buttonOK.setColor(osgWidget.Color(0,0,0,0))
    buttonOK.setCanFill(False)

    labelTitle.setPadBottom(30.0)
    labelText.setPadBottom(30.0)

    box.addWidget(buttonOK)
    box.addWidget(labelText)
    box.addWidget(labelTitle)

    colorBack = frame.getEmbeddedWindow().getColor()
    box.getBackground().setColor(colorBack)

    frame.setWindow(box)

    box.resize()
    frame.resizeFrame(box.getWidth(), box.getHeight())
    _window = frame
    return True







LABEL1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed\n"
    "do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n"
    "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in..."


def main(argv):

    

    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )

    fontSize = 20
    font = "fonts/arial.ttf"
    buttonTheme = "osgWidget/theme-8-shadow.png"
    borderTheme = "osgWidget/theme-8.png"

    message = MessageBox()
    message.create(borderTheme, 
                   buttonTheme,
                   "Error - Critical",
                   LABEL1,
                   "Quit",
                   font,
                   fontSize)

    alpha = AlphaSetterVisitor(.8)
    message.getWindow().accept(alpha)

    wm.addChild(message.getWindow())

    # center
    w = wm.getWidth()
    h = wm.getHeight()
    ww = message.getWindow().getWidth()
    hw = message.getWindow().getHeight()
    ox = (w - ww) / 2
    oy = (h - hw) / 2
    message.getWindow().setPosition(osgWidget.Point(
        osg.round(ox), osg.round(oy), message.getWindow().getPosition()[2])
    )
#    frame.resizeAdd(30, 30)

#    alpha = AlphaSetterVisitor(.8)
#    frame.accept(alpha)
    return osgWidget.createExample(viewer, wm) #osgDB.readNodeFile("cow.osgt"))


























































#if 0
class AlphaSetterVisitor (osg.NodeVisitor) :
_alpha = float()
    AlphaSetterVisitor( float alpha = 1.0):osg.NodeVisitor(TRAVERSE_ALL_CHILDREN)  _alpha = alpha

    def apply(node):

        
        win = dynamic_cast<osgWidget.Window*>(node)

        if win : 
#             osgWidget.warn(), "I am in Window: ", win.getName()

            for (osgWidget.Window.Iterator it = win.begin() it  not = win.end() it++)
#                 osgWidget.warn(), "   I am operating on Widget: ", it.getName()
                
                color = it.getColor()
                color[3] = color[3] *_alpha
                it.setColor(color)
                color = win.getBackground().getColor()
                color[3] = color[3] *_alpha
                win.getBackground().setColor(color)
        traverse(node)



class ColorSetterVisitor (osg.NodeVisitor) :
_color = osgWidget.Color()
    ColorSetterVisitor(  osgWidget.Color color):osg.NodeVisitor(TRAVERSE_ALL_CHILDREN)  _color = color

    def apply(node):

        
        win = dynamic_cast<osgWidget.Window*>(node)

        if win : 
#            osgWidget.warn(), "I am in Window: ", win.getName()

            for (osgWidget.Window.Iterator it = win.begin() it  not = win.end() it++)
#                osgWidget.warn(), "   I am operating on Widget: ", it.getName()
                
#                 osgWidget.Color color = it.getColor()
#                 color[3] = color[3] *_alpha
                it.setColor(_color)
#                 osgWidget.Color color = win.getBackground().getColor()
#                 color[3] = color[3] *_alpha
                win.getBackground().setColor(osgWidget.Color(0,0,0,0))
        traverse(node)



struct EventOK : public osgWidget.Callback, osg.NodeCallback
    typedef osgAnimation.OutQuartMotion WidgetMotion
    _motionOver = WidgetMotion()
    _motionLeave = WidgetMotion()
    
    _lastUpdate = double()
    _defaultColor = osgWidget.Color()
    _overColor = osgWidget.Color()
    _over = bool()
    _frame = osgWidget.Frame()
    _width = float()
    _height = float()
    EventOK(osgWidget.Frame* frame) : osgWidget.Callback(osgWidget.EVENT_ALL), _frame(frame) 
        _motionOver = WidgetMotion(0.0, 0.4)
        _motionLeave = WidgetMotion(0.0, 0.5)
        _defaultColor = _frame.getEmbeddedWindow().getColor()
        _overColor = osgWidget.Color(229.0/255.0,
                                      103.0/255.0,
                                      17.0/255,
                                      _defaultColor[3])
        _over  = False

    bool operator()(osgWidget.Event ev)
        if ev.type == osgWidget.EVENT_MOUSE_ENTER :
            _over = True
#            print "Enter"
            _width = _frame.getWidth()
            _height = _frame.getHeight()
            _motionOver.reset()

#             _frame.resize(_width * 1.2, _height * 1.2)
            return True
        elif ev.type == osgWidget.EVENT_MOUSE_LEAVE : 
            _over = False
#            print "Leave"
#             _frame.resize(_width, _height)
            _motionLeave.reset()
            return True
        return False

    void operator()(osg.Node* node, osg.NodeVisitor* nv)
        if nv.getVisitorType() == osg.NodeVisitor.UPDATE_VISITOR :
            fs = nv.getFrameStamp()
            dt = fs.getSimulationTime() - _lastUpdate
            _lastUpdate = fs.getSimulationTime()

            if _frame.valid() :
                value = float()
                if _over :
                    _motionOver.update(dt)
                    value = _motionOver.getValue()
                else:
                    _motionLeave.update(dt)
                    value = 1.0 - _motionLeave.getValue()

                c = _defaultColor + ((_overColor - _defaultColor) * value)
                colorSetter = ColorSetterVisitor(c)
                _frame.accept(colorSetter)
        node.traverse(*nv)




def createLabel(string, font, size, color):



    
    label = osgWidget.Label("", "")
    label.setFont(font)
    label.setFontSize(size)
    label.setFontColor(color)
    label.setColor(osgWidget.Color(0,0,0,0))
    label.setLabel(string)
    label.setCanFill(True)
    return label

def createButtonOk(theme, text, fontSize):

    
    frame = osgWidget.Frame.createSimpleFrameFromTheme(
        "ButtonOK",
        osgDB.readImageFile(theme),
        300.0, 
        50.0,
        osgWidget.Frame.FRAME_TEXTURE
        )
    frame.getBackground().setColor(0.0, 0.0, 0.0, 0.0)

    label = createLabel(text, "fonts/Vera.ttf", fontSize, osgWidget.Color(0,0,0,1))

    box = osgWidget.Box("HBOX", osgWidget.Box.HORIZONTAL)
    box.addWidget(label)
    box.resize()
    colorBack = frame.getEmbeddedWindow().getColor()
    box.getBackground().setColor(colorBack)
    frame.getEmbeddedWindow().setWindow(box)
    box.setVisibilityMode(osgWidget.Window.VM_ENTIRE)
    box.setEventMask(osgWidget.EVENT_NONE)

    frame.resizeFrame(box.getWidth(), box.getHeight())
    frame.resizeAdd(0, 0)

    event = EventOK(frame)
    frame.setUpdateCallback(event)
    frame.addCallback(event)


    return frame.release()

def createErrorMessage(themeMessage, themeButton, titleText, messageText, buttonText, font, fontSize):

    

    frame = osgWidget.Frame.createSimpleFrameFromTheme(
        "error",
        osgDB.readImageFile(themeMessage),
        300.0,
        50.0,
        osgWidget.Frame.FRAME_ALL
        )
    frame.getBackground().setColor(0.0, 0.0, 0.0, 0.0)

    labelText = createLabel(messageText, font, fontSize, osgWidget.Color(0,0,0,1))
    labelTitle = createLabel(titleText, font, fontSize+5, osgWidget.Color(0.4,0,0,1))

    box = osgWidget.Box("VBOX", osgWidget.Box.VERTICAL)

    buttonOK = createButtonOk(themeButton, buttonText, fontSize).embed()
    buttonOK.setColor(osgWidget.Color(0,0,0,0))
    buttonOK.setCanFill(False)

    box.addWidget(buttonOK)
    box.addWidget(labelText)
    box.addWidget(labelTitle)

    colorBack = frame.getEmbeddedWindow().getColor()
    box.getBackground().setColor(colorBack)

    frame.setWindow(box)

    box.resize()
    frame.resizeFrame(box.getWidth(), box.getHeight())
    return frame.release()


LABEL1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed\n"
    "do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n"
    "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in..."


def main(argv):

    
    theme = "osgWidget/theme-1.png"
    if argc > 1 :
        theme = str(argv[1])

    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        1280.0,
        1024.0,
        MASK_2D,
        osgWidget.WindowManager.WM_PICK_DEBUG
    )

    frame = createErrorMessage(theme,
                                          "osgWidget/theme-8-shadow.png",
                                          "Error - Critical",
                                          LABEL1,
                                          "Ok",
                                          "fonts/Vera.ttf",
                                          20)
    # Add everything to the WindowManager.
    wm.addChild(frame)
    frame.resizeAdd(30, 30)

    alpha = AlphaSetterVisitor(.8)
    frame.accept(alpha)
    return osgWidget.createExample(viewer, wm, osgDB.readNodeFile("cow.osgt"))
#endif


if __name__ == "__main__":
    main(sys.argv)
