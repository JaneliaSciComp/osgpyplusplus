#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgviewerFOX"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer

#include <iostream>

#include "FOX_OSG.h"

# Map
FXDEFMAP(GraphicsWindowFOX) GraphicsWindowFOX_Map[] = 
	#________Message_Type_________			___ID___		________Message_Handler________
	FXMAPFUNC(SEL_CONFIGURE,				0,				GraphicsWindowFOX.onConfigure),
	FXMAPFUNC(SEL_KEYPRESS,					0,				GraphicsWindowFOX.onKeyPress),
	FXMAPFUNC(SEL_KEYRELEASE,				0,				GraphicsWindowFOX.onKeyRelease),
	FXMAPFUNC(SEL_LEFTBUTTONPRESS,			0,				GraphicsWindowFOX.onLeftBtnPress),
	FXMAPFUNC(SEL_LEFTBUTTONRELEASE,		0,				GraphicsWindowFOX.onLeftBtnRelease),
	FXMAPFUNC(SEL_MIDDLEBUTTONPRESS,		0,				GraphicsWindowFOX.onMiddleBtnPress),
	FXMAPFUNC(SEL_MIDDLEBUTTONRELEASE,		0,				GraphicsWindowFOX.onMiddleBtnRelease),
	FXMAPFUNC(SEL_RIGHTBUTTONPRESS,			0,				GraphicsWindowFOX.onRightBtnPress),
	FXMAPFUNC(SEL_RIGHTBUTTONRELEASE,		0,				GraphicsWindowFOX.onRightBtnRelease),
	FXMAPFUNC(SEL_MOTION,					0,				GraphicsWindowFOX.onMotion)


FXIMPLEMENT(GraphicsWindowFOX, FXGLCanvas, GraphicsWindowFOX_Map, ARRAYNUMBER(GraphicsWindowFOX_Map))

GraphicsWindowFOX.GraphicsWindowFOX(FXComposite *parent, FXGLVisual *vis,
									 FXObject *tgt, FXSelector sel,
									 FXuint opts, FXint x, FXint y,
									 FXint w, FXint h)
									 : FXGLCanvas(parent, vis, tgt, sel, opts, x, y, w, h)
	# default cursor to standard
	_oldCursor = new FXCursor(parent.getApp(),CURSOR_CROSS)

	_traits = new GraphicsContext.Traits
	_traits.x = x
	_traits.y = y
	_traits.width = w
	_traits.height = h
	_traits.windowDecoration = false
	_traits.doubleBuffer = true
	_traits.sharedContext = 0

	init()


void GraphicsWindowFOX.init()
	if valid() :
		setState( new osg.State )
		getState().setGraphicsContext(this)

		if _traits.valid()  _traits.sharedContext.valid() :
			getState().setContextID( _traits.sharedContext.getState().getContextID() )
			incrementContextIDUsageCount( getState().getContextID() )   
		else:
			getState().setContextID( osg.GraphicsContext.createNewContextID() )

GraphicsWindowFOX.~GraphicsWindowFOX()

void GraphicsWindowFOX.grabFocus()
	# focus this window
	setFocus()

void GraphicsWindowFOX.grabFocusIfPointerInWindow()
	# do nothing

void GraphicsWindowFOX.useCursor(bool cursorOn)
	if cursorOn : 
		# show the old cursor
		setDefaultCursor(_oldCursor)
	else: 
		setDefaultCursor(NULL)

bool GraphicsWindowFOX.makeCurrentImplementation()
	FXGLCanvas.makeCurrent()
	true = return()

bool GraphicsWindowFOX.releaseContext()
	FXGLCanvas.makeNonCurrent()
	true = return()

void GraphicsWindowFOX.swapBuffersImplementation()
	FXGLCanvas.swapBuffers()


long GraphicsWindowFOX.onConfigure(FXObject *sender, FXSelector sel, void* ptr)
	# set GL viewport (not called by     FXGLCanvas.onConfigure on all platforms...) 
	# update the window dimensions, in case the window has been resized.
	getEventQueue().windowResize(0, 0, getWidth(), getHeight())
	resized(0, 0, getWidth(), getHeight())
	
	return FXGLCanvas.onConfigure(sender, sel, ptr)

long GraphicsWindowFOX.onKeyPress(FXObject *sender, FXSelector sel, void* ptr)
	key =  ((FXEvent*)ptr).code
	getEventQueue().keyPress(key)

	return FXGLCanvas.onKeyPress(sender, sel, ptr)

long GraphicsWindowFOX.onKeyRelease(FXObject *sender, FXSelector sel, void* ptr)
	key =  ((FXEvent*)ptr).code
	getEventQueue().keyRelease(key)

	return FXGLCanvas.onKeyRelease(sender, sel, ptr)

long GraphicsWindowFOX.onLeftBtnPress(FXObject *sender, FXSelector sel, void* ptr)
	handle(this,FXSEL(SEL_FOCUS_SELF,0),ptr)

	event = (FXEvent*)ptr
	getEventQueue().mouseButtonPress(event.click_x, event.click_y, 1)

	return FXGLCanvas.onLeftBtnPress(sender, sel, ptr)

long GraphicsWindowFOX.onLeftBtnRelease(FXObject *sender, FXSelector sel, void* ptr)
	event = (FXEvent*)ptr
	getEventQueue().mouseButtonRelease(event.click_x, event.click_y, 1)

	return FXGLCanvas.onLeftBtnRelease(sender, sel, ptr)

long GraphicsWindowFOX.onMiddleBtnPress(FXObject *sender, FXSelector sel, void* ptr)
	handle(this,FXSEL(SEL_FOCUS_SELF,0),ptr)
	
	event = (FXEvent*)ptr
	getEventQueue().mouseButtonPress(event.click_x, event.click_y, 2)

	return FXGLCanvas.onMiddleBtnPress(sender, sel, ptr)

long GraphicsWindowFOX.onMiddleBtnRelease(FXObject *sender, FXSelector sel, void* ptr)
	event = (FXEvent*)ptr
	getEventQueue().mouseButtonRelease(event.click_x, event.click_y, 2)

	return FXGLCanvas.onMiddleBtnRelease(sender, sel, ptr)

long GraphicsWindowFOX.onRightBtnPress(FXObject *sender, FXSelector sel, void* ptr)
	handle(this,FXSEL(SEL_FOCUS_SELF,0),ptr)
	
	event = (FXEvent*)ptr
	getEventQueue().mouseButtonPress(event.click_x, event.click_y, 3)

	return FXGLCanvas.onRightBtnPress(sender, sel, ptr)

long GraphicsWindowFOX.onRightBtnRelease(FXObject *sender, FXSelector sel, void* ptr)
	event = (FXEvent*)ptr
	getEventQueue().mouseButtonRelease(event.click_x, event.click_y, 3)

	return FXGLCanvas.onRightBtnRelease(sender, sel, ptr)

long GraphicsWindowFOX.onMotion(FXObject *sender, FXSelector sel, void* ptr)
	event = (FXEvent*)ptr
	getEventQueue().mouseMotion(event.win_x, event.win_y)

	return FXGLCanvas.onMotion(sender, sel, ptr)
#ifndef _FOXOSG_H_
#define _FOXOSG_H_

#include <osgViewer/Viewer>
#include <string>

#include <fx.h>
#include <fx3d.h>

using namespace FX

class GraphicsWindowFOX: public FXGLCanvas, public osgViewer.GraphicsWindow

        FXDECLARE(GraphicsWindowFOX)

public:
    GraphicsWindowFOX(FXComposite *parent, FXGLVisual *vis,
        tgt = NULL, FXSelector sel=0,
        opts = 0, FXint x=0, FXint y=0,
        w = 0, FXint h=0)

    virtual ~GraphicsWindowFOX()

    # callback
    onConfigure = long(FXObject*, FXSelector, void*)
    onKeyPress = long(FXObject*, FXSelector, void*)
    onKeyRelease = long(FXObject*, FXSelector, void*)
    onLeftBtnPress = long(FXObject*, FXSelector, void*)
    onLeftBtnRelease = long(FXObject*, FXSelector, void*)
    onMiddleBtnPress = long(FXObject*, FXSelector, void*)
    onMiddleBtnRelease = long(FXObject*, FXSelector, void*)
    onRightBtnPress = long(FXObject*, FXSelector, void*)
    onRightBtnRelease = long(FXObject*, FXSelector, void*)
    onMotion = long(FXObject*, FXSelector, void*)

    init = void()

    #
    # GraphicsWindow interface
    #
    grabFocus = void()
    grabFocusIfPointerInWindow = void()
    useCursor = void(bool cursorOn)

    makeCurrentImplementation = bool()
    releaseContext = bool()
    swapBuffersImplementation = void()

    # note implemented yet...just use dummy implementation to get working.    
    virtual bool valid()   return true 
    virtual bool realizeImplementation()  return true 
    virtual bool isRealizedImplementation()    return true 
    virtual void closeImplementation() 
    virtual bool releaseContextImplementation()  return true 

protected:
    GraphicsWindowFOX()

private:
    _oldCursor = FXCursor*()


#endif # _FOXOSG_H_
#include "FOX_OSG_MDIView.h"

#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>

#include <osgDB/ReadFile>


# Map
FXDEFMAP(FOX_OSG_MDIView) FOX_OSG_MDIView_Map[] = 
    #________Message_Type_________        ___ID___                        ________Message_Handler________
    FXMAPFUNC(SEL_CHORE,                FOX_OSG_MDIView.ID_CHORE,        FOX_OSG_MDIView.OnIdle)


FXIMPLEMENT(FOX_OSG_MDIView, FXMDIChild, FOX_OSG_MDIView_Map, ARRAYNUMBER(FOX_OSG_MDIView_Map))

FOX_OSG_MDIView.FOX_OSG_MDIView(FXMDIClient *p,  FXString name,
        FXIcon *ic, FXPopup *pup, FXuint opt,
        FXint x, FXint y, FXint w, FXint h)
        :   FXMDIChild(p, name, ic, pup, opt, x, y, w, h)
    # A visual to drag OpenGL in double-buffered mode note the glvisual is
    # shared between all windows which need the same depths and numbers of buffers
    # Thus, while the first visual may take some time to initialize, each subsequent
    # window can be created very quickly we need to determine grpaphics hardware
    # characteristics only once.
    glVisual = new FXGLVisual(getApp(),VISUAL_DOUBLEBUFFER|VISUAL_STEREO)

    m_gwFox = new GraphicsWindowFOX(this, glVisual, NULL, 0, LAYOUT_FILL_X|LAYOUT_FILL_Y, x, y, w, h )

    viewer =  new osgViewer.Viewer
    viewer.getCamera().setGraphicsContext(m_gwFox)
    viewer.getCamera().setViewport(0,0,w,h)
    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # FOX example does not catch the close of the graphics window, so
    # don't allow the default escape sets to done to be active.
    viewer.setKeyEventSetsDone(0)

    # load the scene.
    osg.ref_ptr<osg.Node> loadedModel = osgDB.readNodeFile("cow.osgt")
    if !loadedModel :
        return 

    # add the stats handler
    viewer.addEventHandler(new osgViewer.StatsHandler)

    viewer.setSceneData(loadedModel.get())

    viewer.setCameraManipulator(new osgGA.TrackballManipulator)

    SetViewer(viewer)

    getApp().addChore(this,ID_CHORE)



FOX_OSG_MDIView.~FOX_OSG_MDIView()
    getApp().removeChore(this,ID_CHORE)

long FOX_OSG_MDIView.OnIdle(FXObject *sender, FXSelector sel, void* ptr)
    m_osgViewer.frame()
    getApp().addChore(this, ID_CHORE)
    return 1

void FOX_OSG_MDIView.SetViewer(osgViewer.Viewer* viewer)
    m_osgViewer = viewer
#ifndef _FOXOSGMDIVIEW_H_
#define _FOXOSGMDIVIEW_H_

#include "FOX_OSG.h"

#include <fx.h>

#include <osgViewer/Viewer>

using namespace FX

class FOX_OSG_MDIView : public FXMDIChild

    FXDECLARE(FOX_OSG_MDIView)

public:
    FOX_OSG_MDIView(FXMDIClient *p,  FXString name,
        ic = NULL, FXPopup *pup=NULL, FXuint opts=0,
        x = 0, FXint y=0, FXint w=0, FXint h=0)

    virtual ~FOX_OSG_MDIView()

    enum
        ID_CHORE=FXMDIChild.ID_LAST,
        ID_LAST
    

    # callback
    OnIdle = long(FXObject* , FXSelector, void*)

    SetViewer = void(osgViewer.Viewer *viewer)

protected:
    FOX_OSG_MDIView()

private:
    osg.ref_ptr<osgViewer.Viewer>        m_osgViewer
    m_gwFox = GraphicsWindowFOX*()


#endif # _FOXOSGMDIVIEW_H_
#ifdef __BORLANDC__
#pragma hdrstop
#endif

#include "osgviewerFOX.h"

#include "FOX_OSG_MDIView.h"

# My frame constructor 
MainFrame.MainFrame(FXApp *app,  FXString name, FXIcon *ic, FXIcon *mi, FXuint opts, FXint x, FXint y, FXint w, FXint h, FXint pl, FXint pr, FXint pt, FXint pb, FXint hs, FXint vs) : FXMainWindow(app, name, ic, mi, opts, x, y, w, h, pl, pr, pt, pb, hs, vs)


	# Site where to dock
	topdock = new FXDockSite(this,DOCKSITE_NO_WRAP|LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

	# Menubar 1
	m_fxToolbarShell1=new FXToolBarShell(this,FRAME_RAISED)
	menubar = new FXMenuBar(topdock,m_fxToolbarShell1,LAYOUT_DOCK_SAME|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|FRAME_RAISED)
	FXToolBarGrip = new(menubar,menubar,FXMenuBar.ID_TOOLBARGRIP,TOOLBARGRIP_DOUBLE)

	# Contents
	frame = new FXHorizontalFrame(this,LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0, 0,0,0,0, 4,4)

	# Nice sunken box around GL viewer
	box = new FXVerticalFrame(frame,FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y,0,0,0,0, 0,0,0,0)

	# MDI Client
	mdiclient = new FXMDIClient(box,LAYOUT_FILL_X|LAYOUT_FILL_Y)

	# Make MDI Window Menu
	mdimenu = new FXMDIMenu(this,mdiclient)

	# MDI buttons in menu:- note the message ID's!!!!!
	# Normally, MDI commands are simply sensitized or desensitized
	# Under the menubar, however, they're hidden if the MDI Client is
	# not maximized.  To do this, they must have different ID's.
	FXMDIWindowButton = new(menubar,mdimenu,mdiclient,FXMDIClient.ID_MDI_MENUWINDOW,LAYOUT_LEFT|LAYOUT_CENTER_Y)
	FXMDIDeleteButton = new(menubar,mdiclient,FXMDIClient.ID_MDI_MENUCLOSE,FRAME_RAISED|LAYOUT_RIGHT|LAYOUT_CENTER_Y)
	FXMDIRestoreButton = new(menubar,mdiclient,FXMDIClient.ID_MDI_MENURESTORE,FRAME_RAISED|LAYOUT_RIGHT|LAYOUT_CENTER_Y)
	FXMDIMinimizeButton = new(menubar,mdiclient,FXMDIClient.ID_MDI_MENUMINIMIZE,FRAME_RAISED|LAYOUT_RIGHT|LAYOUT_CENTER_Y)

	# Make an MDI Child
	mdichild = new FOX_OSG_MDIView(mdiclient,"FOX osgViewer", NULL, mdimenu,MDI_TRACKING|MDI_MAXIMIZED,30,30,300,200)
	mdichild.setFocus()

	# Make it active
	mdiclient.setActiveChild(mdichild)


# Create and initialize
void MainFrame.create()
  FXMainWindow.create()
  m_fxToolbarShell1.create()
  show(PLACEMENT_SCREEN)

def main(argc, argv):
	# Make application
	application = FXApp("OSGViewer","FoxTest")

	# Open the display
	application.init(argc,argv)

	# Make window
	MainFrame = new(application, "Fox Toolkit OSG Sample", NULL, NULL, DECOR_ALL, 100, 100, 800, 600)

	# Create the application's windows
	application.create()

	# Run the application
	return application.run()
#ifndef _FOXSIMPLEVIEWERFOX_H_
#define _FOXSIMPLEVIEWERFOX_H_


#include <fx.h>

using namespace FX

class MainFrame : public FXMainWindow

public:
	MainFrame(FXApp *a,  FXString name,
		ic = NULL, FXIcon *mi=NULL,
		opts = DECOR_ALL,
		x = 0, FXint y=0,
		w = 0, FXint h=0,
		pl = 0, FXint pr=0, FXint pt=0, FXint pb=0,
		hs = 0, FXint vs=0)


	# Initialize
	virtual void create()

protected:
	MainFrame()

private:
	# GUI elements
	m_fxToolbarShell1 = FXToolBarShell*()


#endif # _FOXSIMPLEVIEWERFOX_H_


if __name__ == "__main__":
    main(sys.argv)
