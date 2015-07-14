#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgdirectinput"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'DirectInputRegistry.cpp'

# OpenSceneGraph example, osgdirectinput.
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

#include <osgGA/EventQueue>
#include <iostream>
#include "DirectInputRegistry"

typedef std.pair<int, int> KeyValue
typedef std.map<int, KeyValue> KeyMap
g_keyMap = KeyMap()

def buildKeyMap():

    
    # TODO: finish the key map as you wish
    g_keyMap[DIK_ESCAPE] = KeyValue(osgGA.GUIEventAdapter.KEY_Escape, 0)
    g_keyMap[DIK_1] = KeyValue(ord("1"), 0)
    g_keyMap[DIK_2] = KeyValue(ord("2"), 0)
    g_keyMap[DIK_3] = KeyValue(ord("3"), 0)
    g_keyMap[DIK_4] = KeyValue(ord("4"), 0)
    g_keyMap[DIK_5] = KeyValue(ord("5"), 0)
    g_keyMap[DIK_6] = KeyValue(ord("6"), 0)
    g_keyMap[DIK_7] = KeyValue(ord("7"), 0)
    g_keyMap[DIK_8] = KeyValue(ord("8"), 0)
    g_keyMap[DIK_9] = KeyValue(ord("9"), 0)
    g_keyMap[DIK_0] = KeyValue(ord("0"), 0)
    g_keyMap[DIK_MINUS] = KeyValue(ord("-"), 0)
    g_keyMap[DIK_EQUALS] = KeyValue(ord("="), 0)
    g_keyMap[DIK_BACK] = KeyValue(osgGA.GUIEventAdapter.KEY_BackSpace, 0)
    g_keyMap[DIK_TAB] = KeyValue(osgGA.GUIEventAdapter.KEY_Tab, 0)
    g_keyMap[DIK_SPACE] = KeyValue(osgGA.GUIEventAdapter.KEY_Space, 0)

bool DirectInputRegistry.initKeyboard( HWND handle )
    if   not _inputDevice  : return False
    
    hr = _inputDevice.CreateDevice( GUID_SysKeyboard, _keyboard, NULL )
    if  FAILED(hr)  or  _keyboard==NULL  :
        osg.notify(osg.WARN), "Unable to create keyboard."
        return False
    buildKeyMap()
    initImplementation = return( handle, _keyboard, c_dfDIKeyboard )

bool DirectInputRegistry.initMouse( HWND handle )
    if   not _inputDevice  : return False
    
    hr = _inputDevice.CreateDevice( GUID_SysMouse, _mouse, NULL )
    if  FAILED(hr)  or  _mouse==NULL  :
        osg.notify(osg.WARN), "Unable to create mouse."
        return False
    initImplementation = return( handle, _mouse, c_dfDIMouse2 )

bool DirectInputRegistry.initJoystick( HWND handle )
    if   not _inputDevice  : return False
    
    hr = _inputDevice.EnumDevices( DI8DEVCLASS_GAMECTRL, EnumJoysticksCallback,
                                            NULL, DIEDFL_ATTACHEDONLY )
    if  FAILED(hr)  or  _joystick==NULL  :
        osg.notify(osg.WARN), "Unable to enumerate joysticks."
        return False
    initImplementation = return( handle, _joystick, c_dfDIJoystick2 )

void DirectInputRegistry.updateState( osgGA.EventQueue* eventQueue )
    hr = HRESULT()
    if   not _supportDirectInput  or   not eventQueue  : return
    
    if  _keyboard  :
        pollDevice( _keyboard )
        
        char buffer[256] = 0
        hr = _keyboard.GetDeviceState( sizeof(buffer), buffer )
        if  SUCCEEDED(hr)  :
            for ( KeyMap.iterator itr=g_keyMap.begin() itr not =g_keyMap.end() ++itr )
                key = itr.second
                value = buffer[itr.first]
                if  key.second==value  : continue
                
                key.second = value
                if  value0x80  :
                    eventQueue.keyPress( key.first )
                else:
                    eventQueue.keyRelease( key.first )
    
    if  _mouse  :
        pollDevice( _mouse )
        
        mouseState = DIMOUSESTATE2()
        hr = _mouse.GetDeviceState( sizeof(DIMOUSESTATE2), mouseState )
        
        # TODO: add mouse handlers
    
    if  _joystick  :
        pollDevice( _joystick )
        
        event = JoystickEvent()
        hr = _joystick.GetDeviceState( sizeof(DIJOYSTATE2), (event._js) )
        if  SUCCEEDED(hr)  : eventQueue.userEvent( event )

DirectInputRegistry.DirectInputRegistry()
:   _keyboard(0), _mouse(0), _joystick(0),
    _supportDirectInput(True)
    hr = DirectInput8Create( GetModuleHandle(NULL), DIRECTINPUT_VERSION,
                                     IID_IDirectInput8, (VOID**)_inputDevice, NULL )
    if  FAILED(hr)  :
        osg.notify(osg.WARN), "Unable to create DirectInput object."
        _supportDirectInput = False

DirectInputRegistry.~DirectInputRegistry()
    releaseDevice( _keyboard )
    releaseDevice( _mouse )
    releaseDevice( _joystick )
    if  _inputDevice  : _inputDevice.Release()

bool DirectInputRegistry.initImplementation( HWND handle, LPDIRECTINPUTDEVICE8 device, LPCDIDATAFORMAT format )
    _supportDirectInput = True
    hr = device.SetDataFormat( format )
    if  FAILED(hr)  :
        osg.notify(osg.WARN), "Unable to set device data format."
        _supportDirectInput = False
    
    hr = device.SetCooperativeLevel( handle, DISCL_EXCLUSIVE|DISCL_FOREGROUND )
    if  FAILED(hr)  :
        osg.notify(osg.WARN), "Unable to attach device to window."
        _supportDirectInput = False
    
    device.Acquire()
    return _supportDirectInput

void DirectInputRegistry.pollDevice( LPDIRECTINPUTDEVICE8 device )
    hr = device.Poll()
    if  FAILED(hr)  :
        device.Acquire()
        if  hr==DIERR_INPUTLOST  :
            osg.notify(osg.WARN), "Device lost."

void DirectInputRegistry.releaseDevice( LPDIRECTINPUTDEVICE8 device )
    if  device  :
        device.Unacquire()
        device.Release()

BOOL CALLBACK DirectInputRegistry.EnumJoysticksCallback(  DIDEVICEINSTANCE* didInstance, VOID* )
    hr = HRESULT()
    device = DirectInputRegistry.instance().getDevice()
    if  device  :
        hr = device.CreateDevice( didInstance.guidInstance,
                                   (DirectInputRegistry.instance().getJoyStick()), NULL )
    if  FAILED(hr)  : return DIENUM_CONTINUE
    return DIENUM_STOP

# Translated from file 'osgdirectinput.cpp'

# OpenSceneGraph example, osgdirectinput.
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

#include <osgDB/ReadFile>
#include <osgGA/StateSetManipulator>
#include <osgViewer/api/Win32/GraphicsWindowWin32>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <iostream>
#include "DirectInputRegistry"

class CustomViewer (osgViewer.Viewer) :
    CustomViewer() : osgViewer.Viewer() 
    virtual ~CustomViewer() 
    
    def eventTraversal():
    
        
        DirectInputRegistry.instance().updateState( _eventQueue )
        osgViewer.Viewer.eventTraversal()
    def viewerInit():
        
        windowWin32 = dynamic_cast<osgViewer.GraphicsWindowWin32*>( _camera.getGraphicsContext() )
        if  windowWin32  :
            hwnd = windowWin32.getHWND()
            DirectInputRegistry.instance().initKeyboard( hwnd )
            #DirectInputRegistry.instance().initMouse( hwnd )
            DirectInputRegistry.instance().initJoystick( hwnd )
        osgViewer.Viewer.viewerInit()


class JoystickHandler (osgGA.GUIEventHandler) :
    JoystickHandler() 
    
    def handle(ea, aa):
    
        
        switch ( ea.getEventType() )
        case osgGA.GUIEventAdapter.KEYDOWN:
            print "*** Key 0x", std.hex, ea.getKey(), std.dec, " down ***"
            break
        case osgGA.GUIEventAdapter.KEYUP:
            print "*** Key 0x", std.hex, ea.getKey(), std.dec, " up ***"
            break
        case osgGA.GUIEventAdapter.USER:
                event = dynamic_cast< JoystickEvent*>( ea.getUserData() )
                if   not event  : break
                
                js = event._js
                for ( unsigned int i=0 i<128 ++i )
                    if  js.rgbButtons[i]  :
                        print "*** Joystick Btn", i, " = ", (int)js.rgbButtons[i]
                
                if  js.lX==0x0000  : print "*** Joystick X-"
                elif  js.lX==0xffff  : print "*** Joystick X+"
                
                if  js.lY==0  : print "*** Joystick Y-"
                elif  js.lY==0xffff  : print "*** Joystick Y+"
            return True
        default:
            break
        return False


def main(argv):

    
    arguments = osg.ArgumentParser( argc, argv )
    model = osgDB.readNodeFiles( arguments )
    if   not model  : model = osgDB.readNodeFile( "cow.osgt" )
    if   not model  : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1
    
    viewer = CustomViewer()
    viewer.addEventHandler( JoystickHandler )()
    viewer.addEventHandler( osgViewer.StatsHandler )()
    viewer.addEventHandler( osgViewer.WindowSizeHandler )()
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    viewer.setSceneData( model )
    viewer.setUpViewInWindow( 250, 50, 800, 600 )
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
