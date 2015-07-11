#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgviewerWX"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer
from osgpypp import wx

# For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
#pragma hdrstop
#endif

#ifndef WX_PRECOMP
#include "wx/wx.h"
#endif

# For wxCURSOR_BLANK below, but isn't used a.t.m.
##ifdef WIN32
##include "wx/msw/wx.rc"
##endif

#include "osgviewerWX.h"


#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgDB/ReadFile>
#include <wx/image.h>
#include <wx/menu.h>

#include <iostream>

# `Main program' equivalent, creating windows and returning main app frame
bool wxOsgApp.OnInit()
    if argc<2 :
        print wxString(argv[0]).mb_str(), ": requires filename argument."
        false = return()

    width =  800
    height =  600

    # Create the main frame window

    frame =  new MainFrame(NULL, wxT("wxWidgets OSG Sample"),
        wxDefaultPosition, wxSize(width, height))

    # create osg canvas
    #    - initialize

    int attributes[7]
    attributes[0] = int(WX_GL_DOUBLEBUFFER)
    attributes[1] = WX_GL_RGBA
    attributes[2] = WX_GL_DEPTH_SIZE
    attributes[3] = 8
    attributes[4] = WX_GL_STENCIL_SIZE
    attributes[5] = 8
    attributes[6] = 0

    canvas =  new OSGCanvas(frame, wxID_ANY, wxDefaultPosition,
        wxSize(width, height), wxSUNKEN_BORDER, wxT("osgviewerWX"), attributes)

    gw =  new GraphicsWindowWX(canvas)

    canvas.SetGraphicsWindow(gw)

    viewer =  new osgViewer.Viewer
    viewer.getCamera().setGraphicsContext(gw)
    viewer.getCamera().setViewport(0,0,width,height)
    viewer.addEventHandler(new osgViewer.StatsHandler)
    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # load the scene.
    fname = wxString(argv[1])
    osg.ref_ptr<osg.Node> loadedModel = osgDB.readNodeFile(str(fname.mb_str()))
    if !loadedModel :
        print argv[0], ": No data loaded."
        false = return()

    viewer.setSceneData(loadedModel.get())
    viewer.setCameraManipulator(new osgGA.TrackballManipulator)
    frame.SetViewer(viewer)

    # Show the frame 
    frame.Show(true)

    true = return()

IMPLEMENT_APP(wxOsgApp)

BEGIN_EVENT_TABLE(MainFrame, wxFrame)
    EVT_IDLE(MainFrame.OnIdle)
END_EVENT_TABLE()

# My frame constructor 
MainFrame.MainFrame(wxFrame *frame,  wxString title,  wxPoint pos,
     wxSize size, long style)
    : wxFrame(frame, wxID_ANY, title, pos, size, style)

void MainFrame.SetViewer(osgViewer.Viewer *viewer)
    _viewer = viewer

void MainFrame.OnIdle(wxIdleEvent event)
    if !_viewer.isRealized() :
        return

    _viewer.frame()

    event.RequestMore()

BEGIN_EVENT_TABLE(OSGCanvas, wxGLCanvas)
    EVT_SIZE                (OSGCanvas.OnSize)
    EVT_PAINT               (OSGCanvas.OnPaint)
    EVT_ERASE_BACKGROUND    (OSGCanvas.OnEraseBackground)

    EVT_CHAR                (OSGCanvas.OnChar)
    EVT_KEY_UP              (OSGCanvas.OnKeyUp)

    EVT_ENTER_WINDOW        (OSGCanvas.OnMouseEnter)
    EVT_LEFT_DOWN           (OSGCanvas.OnMouseDown)
    EVT_MIDDLE_DOWN         (OSGCanvas.OnMouseDown)
    EVT_RIGHT_DOWN          (OSGCanvas.OnMouseDown)
    EVT_LEFT_UP             (OSGCanvas.OnMouseUp)
    EVT_MIDDLE_UP           (OSGCanvas.OnMouseUp)
    EVT_RIGHT_UP            (OSGCanvas.OnMouseUp)
    EVT_MOTION              (OSGCanvas.OnMouseMotion)
    EVT_MOUSEWHEEL          (OSGCanvas.OnMouseWheel)
END_EVENT_TABLE()

OSGCanvas.OSGCanvas(wxWindow *parent, wxWindowID id,
     wxPoint pos,  wxSize size, long style,  wxString name, int *attributes)
    : wxGLCanvas(parent, id, pos, size, style|wxFULL_REPAINT_ON_RESIZE, name, attributes)
    # default cursor to standard
    _oldCursor = *wxSTANDARD_CURSOR

OSGCanvas.~OSGCanvas()

void OSGCanvas.OnPaint( wxPaintEvent WXUNUSED(event) )
    # must always be here 
    dc = wxPaintDC(this)

void OSGCanvas.OnSize(wxSizeEvent event)
    # this is also necessary to update the context on some platforms
    wxGLCanvas.OnSize(event)

    # set GL viewport (not called by wxGLCanvas.OnSize on all platforms...)
    int width, height
    GetClientSize(width, height)

    if _graphics_window.valid() :
        # update the window dimensions, in case the window has been resized.
        _graphics_window.getEventQueue().windowResize(0, 0, width, height)
        _graphics_window.resized(0,0,width,height)

void OSGCanvas.OnEraseBackground(wxEraseEvent WXUNUSED(event))
    # Do nothing, to avoid flashing on MSW 

void OSGCanvas.OnChar(wxKeyEvent event)
#if wxUSE_UNICODE
    key =  event.GetUnicodeKey()
#else:
    key =  event.GetKeyCode()
#endif

    if _graphics_window.valid() :
        _graphics_window.getEventQueue().keyPress(key)

    # If this key event is not processed here, we should call
    # event.Skip() to allow processing to continue.

void OSGCanvas.OnKeyUp(wxKeyEvent event)
#if wxUSE_UNICODE
    key =  event.GetUnicodeKey()
#else:
    key =  event.GetKeyCode()
#endif

    if _graphics_window.valid() :
        _graphics_window.getEventQueue().keyRelease(key)

    # If this key event is not processed here, we should call
    # event.Skip() to allow processing to continue.

void OSGCanvas.OnMouseEnter(wxMouseEvent event)
    # Set focus to ourselves, so keyboard events get directed to us
    SetFocus()

void OSGCanvas.OnMouseDown(wxMouseEvent event)
    if _graphics_window.valid() :
        _graphics_window.getEventQueue().mouseButtonPress(event.GetX(), event.GetY(),
            event.GetButton())

void OSGCanvas.OnMouseUp(wxMouseEvent event)
    if _graphics_window.valid() :
        _graphics_window.getEventQueue().mouseButtonRelease(event.GetX(), event.GetY(),
            event.GetButton())

void OSGCanvas.OnMouseMotion(wxMouseEvent event)
    if _graphics_window.valid() :
        _graphics_window.getEventQueue().mouseMotion(event.GetX(), event.GetY())

void OSGCanvas.OnMouseWheel(wxMouseEvent event)
    delta =  event.GetWheelRotation() / event.GetWheelDelta() * event.GetLinesPerAction()

    if _graphics_window.valid() : 
        _graphics_window.getEventQueue().mouseScroll(
            delta>0 ? 
            osgGA.GUIEventAdapter.SCROLL_UP : 
            osgGA.GUIEventAdapter.SCROLL_DOWN)

void OSGCanvas.UseCursor(bool value)
    if value :
        # show the old cursor
        SetCursor(_oldCursor)
    else:
        # remember the old cursor
        _oldCursor = GetCursor()

        # hide the cursor
        #    - can't find a way to do this neatly, so create a 1x1, transparent image
        image = wxImage(1,1)
        image.SetMask(true)
        image.SetMaskColour(0, 0, 0)
        cursor = wxCursor(image)
        SetCursor(cursor)

        # On wxGTK, only works as of version 2.7.0
        # (http:#trac.wxwidgets.org/ticket/2946)
        # SetCursor( wxStockCursor( wxCURSOR_BLANK ) )

GraphicsWindowWX.GraphicsWindowWX(OSGCanvas *canvas)
    _canvas = canvas

    _traits = new GraphicsContext.Traits

    pos =  _canvas.GetPosition()
    size =  _canvas.GetSize()

    _traits.x = pos.x
    _traits.y = pos.y
    _traits.width = size.x
    _traits.height = size.y

    init()

GraphicsWindowWX.~GraphicsWindowWX()

void GraphicsWindowWX.init()
    if valid() :
        setState( new osg.State )
        getState().setGraphicsContext(this)

        if _traits.valid()  _traits.sharedContext.valid() :
            getState().setContextID( _traits.sharedContext.getState().getContextID() )
            incrementContextIDUsageCount( getState().getContextID() )
        else:
            getState().setContextID( osg.GraphicsContext.createNewContextID() )

void GraphicsWindowWX.grabFocus()
    # focus the canvas
    _canvas.SetFocus()

void GraphicsWindowWX.grabFocusIfPointerInWindow()
    # focus this window, if the pointer is in the window
    pos =  wxGetMousePosition()
    if wxFindWindowAtPoint(pos) == _canvas :
        _canvas.SetFocus()

void GraphicsWindowWX.useCursor(bool cursorOn)
    _canvas.UseCursor(cursorOn)

bool GraphicsWindowWX.makeCurrentImplementation()
    _canvas.SetCurrent()
    true = return()

void GraphicsWindowWX.swapBuffersImplementation()
    _canvas.SwapBuffers()
#ifndef _WXSIMPLEVIEWERWX_H_
#define _WXSIMPLEVIEWERWX_H_

#include "wx/defs.h"
#include "wx/app.h"
#include "wx/cursor.h"
#include "wx/glcanvas.h"
#include <osgViewer/Viewer>
#include <string>

GraphicsWindowWX = class()

class OSGCanvas : public wxGLCanvas
public:
    OSGCanvas(wxWindow *parent, wxWindowID id = wxID_ANY,
        pos =  wxDefaultPosition,
        size =  wxDefaultSize, long style = 0,
        name =  wxT("TestGLCanvas"),
        attributes =  0)

    virtual ~OSGCanvas()

    void SetGraphicsWindow(osgViewer.GraphicsWindow *gw)    _graphics_window = gw 

    OnPaint = void(wxPaintEvent event)
    OnSize = void(wxSizeEvent event)
    OnEraseBackground = void(wxEraseEvent event)

    OnChar = void(wxKeyEvent event)
    OnKeyUp = void(wxKeyEvent event)

    OnMouseEnter = void(wxMouseEvent event)
    OnMouseDown = void(wxMouseEvent event)
    OnMouseUp = void(wxMouseEvent event)
    OnMouseMotion = void(wxMouseEvent event)
    OnMouseWheel = void(wxMouseEvent event)

    UseCursor = void(bool value)

private:
    DECLARE_EVENT_TABLE()

    osg.ref_ptr<osgViewer.GraphicsWindow> _graphics_window

    _oldCursor = wxCursor()


class GraphicsWindowWX : public osgViewer.GraphicsWindow
public:
    GraphicsWindowWX(OSGCanvas *canvas)
    ~GraphicsWindowWX()

    init = void()

    #
    # GraphicsWindow interface
    #
    grabFocus = void()
    grabFocusIfPointerInWindow = void()
    useCursor = void(bool cursorOn)

    makeCurrentImplementation = bool()
    swapBuffersImplementation = void()

    # not implemented yet...just use dummy implementation to get working.
    virtual bool valid()   return true 
    virtual bool realizeImplementation()  return true 
    virtual bool isRealizedImplementation()    return _canvas.IsShownOnScreen() 
    virtual void closeImplementation() 
    virtual bool releaseContextImplementation()  return true 

private:
    # XXX need to set _canvas to NULL when the canvas is deleted by
    # its parent. for this, need to add event handler in OSGCanvas
    _canvas = OSGCanvas*()


class MainFrame : public wxFrame
public:
    MainFrame(wxFrame *frame,  wxString title,  wxPoint pos,
         wxSize size, long style = wxDEFAULT_FRAME_STYLE)

    SetViewer = void(osgViewer.Viewer *viewer)
    OnIdle = void(wxIdleEvent event)

private:
    osg.ref_ptr<osgViewer.Viewer> _viewer

    DECLARE_EVENT_TABLE()


# Define a new application type 
class wxOsgApp : public wxApp
public:
    OnInit = bool()


#endif # _WXSIMPLEVIEWERWX_H_


if __name__ == "__main__":
    main(sys.argv)
