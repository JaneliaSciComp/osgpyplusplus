#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgviewerMFC"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'ChildFrm.cpp'

# ChildFrm.cpp : implementation of the CChildFrame class
#
#include "stdafx.h"
#include "MFC_OSG_MDI.h"
#include "ChildFrm.h"

#ifdef _DEBUG
#define DEBUG_NEW
#endif


# CChildFrame

IMPLEMENT_DYNCREATE(CChildFrame, CMDIChildWnd)

BEGIN_MESSAGE_MAP(CChildFrame, CMDIChildWnd)
END_MESSAGE_MAP()


# CChildFrame construction/destruction

CChildFrame.CChildFrame()
    # TODO: add member initialization code here

CChildFrame.~CChildFrame()

BOOL CChildFrame.PreCreateWindow(CREATESTRUCT cs)
    # TODO: Modify the Window class or styles here by modifying the CREATESTRUCT cs
    if  !CMDIChildWnd.PreCreateWindow(cs)  :
        return FALSE

    cs.style = WS_CHILD | WS_VISIBLE | WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU
        | FWS_ADDTOTITLE | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX | WS_MAXIMIZE

    return TRUE


# CChildFrame diagnostics

#ifdef _DEBUG
void CChildFrame.AssertValid() 
    CMDIChildWnd.AssertValid()

void CChildFrame.Dump(CDumpContext dc) 
    CMDIChildWnd.Dump(dc)

#endif #_DEBUG


# CChildFrame message handlers

# Translated from file 'ChildFrm.h'

# ChildFrm.h : interface of the CChildFrame class
#


#pragma once


class CChildFrame (CMDIChildWnd) :
DECLARE_DYNCREATE(CChildFrame)
    CChildFrame()

# Operations

# Overrides
    PreCreateWindow = virtual BOOL(CREATESTRUCT cs)

# Implementation
    virtual ~CChildFrame()
#ifdef _DEBUG
    virtual void AssertValid() 
    virtual void Dump(CDumpContext dc) 
#endif

# Generated message map functions
    DECLARE_MESSAGE_MAP()


# Translated from file 'MainFrm.cpp'

# MainFrm.cpp : implementation of the CMainFrame class
#

#include "stdafx.h"
#include "MFC_OSG_MDI.h"

#include "MainFrm.h"

#ifdef _DEBUG
#define DEBUG_NEW
#endif


# CMainFrame

IMPLEMENT_DYNAMIC(CMainFrame, CMDIFrameWnd)

BEGIN_MESSAGE_MAP(CMainFrame, CMDIFrameWnd)
    ON_WM_CREATE()
END_MESSAGE_MAP()

static UINT indicators[] =
    ID_SEPARATOR,           # status line indicator
    ID_INDICATOR_CAPS,
    ID_INDICATOR_NUM,
    ID_INDICATOR_SCRL,



# CMainFrame construction/destruction

CMainFrame.CMainFrame()
    m_bAutoMenuEnable = False

CMainFrame.~CMainFrame()


int CMainFrame.OnCreate(LPCREATESTRUCT lpCreateStruct)
    if CMDIFrameWnd.OnCreate(lpCreateStruct) == -1 :
        return -1
    
    if !m_wndToolBar.CreateEx(this, TBSTYLE_FLAT | TBSTYLE_TRANSPARENT) ||
        !m_wndToolBar.LoadToolBar(IDR_MAINFRAME) :
        TRACE0("Failed to create toolbar\n")
        return -1      # fail to create
    if !m_wndDlgBar.Create(this, IDR_MAINFRAME, 
        CBRS_ALIGN_TOP, AFX_IDW_DIALOGBAR) :
        TRACE0("Failed to create dialogbar\n")
        return -1        # fail to create

    if !m_wndReBar.Create(this) ||
        !m_wndReBar.AddBar(m_wndToolBar) ||
        !m_wndReBar.AddBar(m_wndDlgBar) :
        TRACE0("Failed to create rebar\n")
        return -1      # fail to create

    if !m_wndStatusBar.Create(this) ||
        !m_wndStatusBar.SetIndicators(indicators,
          sizeof(indicators)/sizeof(UINT)) :
        TRACE0("Failed to create status bar\n")
        return -1      # fail to create

    # TODO: Remove this if you don't want tool tips
    m_wndToolBar.SetBarStyle(m_wndToolBar.GetBarStyle() |
        CBRS_TOOLTIPS | CBRS_FLYBY)

    return 0

BOOL CMainFrame.PreCreateWindow(CREATESTRUCT cs)
    if  !CMDIFrameWnd.PreCreateWindow(cs)  :
        return FALSE
    # TODO: Modify the Window class or styles here by modifying
    #  the CREATESTRUCT cs

    return TRUE


# CMainFrame diagnostics

#ifdef _DEBUG
void CMainFrame.AssertValid() 
    CMDIFrameWnd.AssertValid()

void CMainFrame.Dump(CDumpContext dc) 
    CMDIFrameWnd.Dump(dc)

#endif #_DEBUG


# CMainFrame message handlers




# Translated from file 'MainFrm.h'

# MainFrm.h : interface of the CMainFrame class
#


#pragma once

class CMainFrame (CMDIFrameWnd) :
DECLARE_DYNAMIC(CMainFrame)
    CMainFrame()

# Attributes

# Operations

# Overrides
    PreCreateWindow = virtual BOOL(CREATESTRUCT cs)

# Implementation
    virtual ~CMainFrame()
#ifdef _DEBUG
    virtual void AssertValid() 
    virtual void Dump(CDumpContext dc) 
#endif  # control bar embedded members
    m_wndStatusBar = CStatusBar()
    m_wndToolBar = CToolBar()
    m_wndReBar = CReBar()
    m_wndDlgBar = CDialogBar()

# Generated message map functions
    afx_msg int OnCreate(LPCREATESTRUCT lpCreateStruct)
    afx_msg void OnTimer(UINT nIDEvent)
    DECLARE_MESSAGE_MAP()




# Translated from file 'MFC_OSG.cpp'

# MFC_OSG.cpp : implementation of the cOSG class
#
#include "stdafx.h"
#include "MFC_OSG.h"


cOSG.cOSG(HWND hWnd) :
   m_hWnd(hWnd) 

cOSG.~cOSG()
    mViewer.setDone(True)
    Sleep(1000)
    mViewer.stopThreading()

    mViewer = delete()

void cOSG.InitOSG(str modelname)
    # Store the name of the model to load
    m_ModelName = modelname

    # Init different parts of OSG
    InitManipulators()
    InitSceneGraph()
    InitCameraConfig()

void cOSG.InitManipulators(void)
    # Create a trackball manipulator
    trackball = osgGA.TrackballManipulator()

    # Create a Manipulator Switcher
    keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

    # Add our trackball manipulator to the switcher
    keyswitchManipulator.addMatrixManipulator( '1', "Trackball", trackball.get())

    # Init the switcher to the first manipulator (in this case the only manipulator)
    keyswitchManipulator.selectMatrixManipulator(0)  # Zero based index Value


void cOSG.InitSceneGraph(void)
    # Init the main Root Node/Group
    mRoot  = osg.Group()

    # Load the Model from the model name
    mModel = osgDB.readNodeFile(m_ModelName)
    if !mModel : return

    # Optimize the model
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(mModel.get())
    optimizer.reset()

    # Add the model to the scene
    mRoot.addChild(mModel.get())

void cOSG.InitCameraConfig(void)
    # Local Variable to hold window size data
    rect = RECT()

    # Create the viewer for this window
    mViewer = osgViewer.Viewer()

    # Add a Stats Handler to the viewer
    mViewer.addEventHandler(osgViewer.StatsHandler)()
    
    # Get the current window size
    .GetWindowRect(m_hWnd, rect)

    # Init the GraphicsContext Traits
    traits = osg.GraphicsContext.Traits()

    # Init the Windata Variable that holds the handle for the Window to display OSG in.
    windata = osgViewer.GraphicsWindowWin32.WindowData(m_hWnd)

    # Setup the traits parameters
    traits.x = 0
    traits.y = 0
    traits.width = rect.right - rect.left
    traits.height = rect.bottom - rect.top
    traits.windowDecoration = False
    traits.doubleBuffer = True
    traits.sharedContext = 0
    traits.setInheritedWindowPixelFormat = True
    traits.inheritedWindowData = windata

    # Create the Graphics Context
    gc = osg.GraphicsContext.createGraphicsContext(traits.get())

    # Init Master Camera for this View
    camera = mViewer.getCamera()

    # Assign Graphics Context to the Camera
    camera.setGraphicsContext(gc)

    # Set the viewport for the Camera
    camera.setViewport(osg.Viewport(traits.x, traits.y, traits.width, traits.height))

    # Set projection matrix and camera attribtues
    camera.setClearMask(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
    camera.setClearColor(osg.Vec4f(0.2, 0.2, 0.4, 1.0))
    camera.setProjectionMatrixAsPerspective(
        30.0, static_cast<double>(traits.width)/static_cast<double>(traits.height), 1.0, 1000.0)

    # Add the Camera to the Viewer
    #mViewer.addSlave(camera.get())
    mViewer.setCamera(camera.get())

    # Add the Camera Manipulator to the Viewer
    mViewer.setCameraManipulator(keyswitchManipulator.get())

    # Set the Scene Data
    mViewer.setSceneData(mRoot.get())

    # Realize the Viewer
    mViewer.realize()

    # Correct aspect ratio
    #double fovy,aspectRatio,z1,z2
#    mViewer.getCamera().getProjectionMatrixAsPerspective(fovy,aspectRatio,z1,z2)
#    aspectRatio=double(traits.width)/double(traits.height)
#    mViewer.getCamera().setProjectionMatrixAsPerspective(fovy,aspectRatio,z1,z2)

void cOSG.PreFrameUpdate()
    # Due any preframe updates in this routine

void cOSG.PostFrameUpdate()
    # Due any postframe updates in this routine

#void cOSG.Render(void* ptr)
#
#    osg = (cOSG*)ptr
#
#    viewer = osg.getViewer()
#
#    # You have two options for the main viewer loop
#    #      viewer.run()   or
#    #      while !viewer.done() :  viewer.frame() 
#
#    #viewer.run()
#    while !viewer.done() :
#    
#        osg.PreFrameUpdate()
#        viewer.frame()
#        osg.PostFrameUpdate()
#        #Sleep(10)         # Use this command if you need to allow other processes to have cpu time
#    
#
#    # For some reason this has to be here to avoid issue: 
#    # if you have multiple OSG windows up 
#    # and you exit one then all stop rendering
#    AfxMessageBox("Exit Rendering Thread")
#
#    _endthread()
#

CRenderingThread.CRenderingThread( cOSG* ptr )
:   OpenThreads.Thread(), _ptr(ptr), _done(False)

CRenderingThread.~CRenderingThread()
    _done = True
    while  isRunning()  :
        OpenThreads.Thread.YieldCurrentThread()

void CRenderingThread.run()
    if  !_ptr  :
        _done = True
        return

    viewer = _ptr.getViewer()
    do
        _ptr.PreFrameUpdate()
        viewer.frame()
        _ptr.PostFrameUpdate()
     while  !testCancel()  !viewer.done()  !_done  :

# Translated from file 'MFC_OSG.h'

#pragma once

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgViewer/api/win32/GraphicsWindowWin32>
#include <osgGA/TrackballManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgDB/DatabasePager>
#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgUtil/Optimizer>
#include <string>

class cOSG :
    cOSG(HWND hWnd)
    ~cOSG()

    InitOSG = void(str filename)
    InitManipulators = void(void)
    InitSceneGraph = void(void)
    InitCameraConfig = void(void)
    SetupWindow = void(void)
    SetupCamera = void(void)
    PreFrameUpdate = void(void)
    PostFrameUpdate = void(void)
    def Done(value):
         mDone = value 
    bool Done(void)  return mDone 
    #static void Render(void* ptr)

    def getViewer():

         return mViewer 
    mDone = bool()
    m_ModelName = str()
    m_hWnd = HWND()
    mViewer = osgViewer.Viewer*()
    mRoot = osg.Group()
    mModel = osg.Node()
    trackball = osgGA.TrackballManipulator()
    keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()


class CRenderingThread (OpenThreads.Thread) :
    CRenderingThread( cOSG* ptr )
    virtual ~CRenderingThread()

    run = virtual void()
    _ptr = cOSG*()
    _done = bool()


# Translated from file 'MFC_OSG_MDI.cpp'

# MFC_OSG_MDI.cpp : Defines the class behaviors for the application.
#

#include "stdafx.h"
#include "MFC_OSG_MDI.h"
#include "MainFrm.h"

#include "ChildFrm.h"
#include "MFC_OSG_MDIDoc.h"
#include "MFC_OSG_MDIView.h"

#ifdef _DEBUG
#define DEBUG_NEW
#endif


# CMFC_OSG_MDIApp

BEGIN_MESSAGE_MAP(CMFC_OSG_MDIApp, CWinApp)
    ON_COMMAND(ID_APP_ABOUT, CMFC_OSG_MDIApp.OnAppAbout)
    ON_COMMAND(ID_FILE_OPEN, CWinApp.OnFileOpen)
END_MESSAGE_MAP()


# CMFC_OSG_MDIApp construction

CMFC_OSG_MDIApp.CMFC_OSG_MDIApp()


# The one and only CMFC_OSG_MDIApp object

theApp = CMFC_OSG_MDIApp()


# CMFC_OSG_MDIApp initialization

BOOL CMFC_OSG_MDIApp.InitInstance()
    # InitCommonControlsEx() is required on Windows XP if an application
    # manifest specifies use of ComCtl32.dll version 6 or later to enable
    # visual styles.  Otherwise, any window creation will fail.
    InitCtrls = INITCOMMONCONTROLSEX()
    InitCtrls.dwSize = sizeof(InitCtrls)
    # Set this to include all the common control classes you want to use
    # in your application.
    InitCtrls.dwICC = ICC_WIN95_CLASSES
    InitCommonControlsEx(InitCtrls)

    CWinApp.InitInstance()

    # Standard initialization
    # If you are not using these features and wish to reduce the size
    # of your final executable, you should remove from the following
    # the specific initialization routines you do not need
    # Change the registry key under which our settings are stored
    # TODO: You should modify this string to be something appropriate
    # such as the name of your company or organization
    SetRegistryKey(_T("Local AppWizard-Generated Applications"))
    LoadStdProfileSettings(4)  # Load standard INI file options (including MRU)
    # Register the application's document templates.  Document templates
    #  serve as the connection between documents, frame windows and views
    pDocTemplate = CMultiDocTemplate*()
    pDocTemplate = CMultiDocTemplate(IDR_MFC_OSG_MDITYPE,
        RUNTIME_CLASS(CMFC_OSG_MDIDoc),
        RUNTIME_CLASS(CChildFrame), # custom MDI child frame
        RUNTIME_CLASS(CMFC_OSG_MDIView))
    if !pDocTemplate :
        return FALSE
    AddDocTemplate(pDocTemplate)

    # create main MDI Frame window
    pMainFrame = CMainFrame()
    if !pMainFrame || !pMainFrame.LoadFrame(IDR_MAINFRAME) :
        pMainFrame = delete()
        return FALSE
    m_pMainWnd = pMainFrame
    # call DragAcceptFiles only if there's a suffix
    #  In an MDI app, this should occur immediately after setting m_pMainWnd

    # Parse command line for standard shell commands, DDE, file open
    cmdInfo = CCommandLineInfo()
    ParseCommandLine(cmdInfo)

    # Don't display a MDI child window during startup
    if cmdInfo.m_nShellCommand == CCommandLineInfo.FileNew :
        cmdInfo.m_nShellCommand = CCommandLineInfo.FileNothing


    # Dispatch commands specified on the command line.  Will return FALSE if
    # app was launched with /RegServer, /Register, /Unregserver or /Unregister.
    if !ProcessShellCommand(cmdInfo) :
        return FALSE
    # The main window has been initialized, so show and update it
    pMainFrame.ShowWindow(m_nCmdShow)
    pMainFrame.UpdateWindow()

    return TRUE



# CAboutDlg dialog used for App About

class CAboutDlg (CDialog) :
    CAboutDlg()

# Dialog Data
    enum  IDD = IDD_ABOUTBOX 
    DoDataExchange = virtual void(CDataExchange* pDX)    # DDX/DDV support

# Implementation
    DECLARE_MESSAGE_MAP()


CAboutDlg.CAboutDlg() : CDialog(CAboutDlg.IDD)

void CAboutDlg.DoDataExchange(CDataExchange* pDX)
    CDialog.DoDataExchange(pDX)

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
END_MESSAGE_MAP()

# App command to run the dialog
void CMFC_OSG_MDIApp.OnAppAbout()
    aboutDlg = CAboutDlg()
    aboutDlg.DoModal()


# CMFC_OSG_MDIApp message handlers


# Translated from file 'MFC_OSG_MDI.h'

# MFC_OSG_MDI.h : main header file for the MFC_OSG_MDI application
#
#pragma once

#ifndef __AFXWIN_H__
    #error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"       # main symbols


# CMFC_OSG_MDIApp:
# See MFC_OSG_MDI.cpp for the implementation of this class
#

class CMFC_OSG_MDIApp (CWinApp) :
    CMFC_OSG_MDIApp()


# Overrides
    InitInstance = virtual BOOL()

# Implementation
    afx_msg void OnAppAbout()
    DECLARE_MESSAGE_MAP()


extern CMFC_OSG_MDIApp theApp
# Translated from file 'MFC_OSG_MDIDoc.cpp'

# MFC_OSG_MDIDoc.cpp : implementation of the CMFC_OSG_MDIDoc class
#

#include "stdafx.h"
#include "MFC_OSG_MDI.h"

#include "MFC_OSG_MDIDoc.h"

#ifdef _DEBUG
#define DEBUG_NEW
#endif


# CMFC_OSG_MDIDoc

IMPLEMENT_DYNCREATE(CMFC_OSG_MDIDoc, CDocument)

BEGIN_MESSAGE_MAP(CMFC_OSG_MDIDoc, CDocument)
END_MESSAGE_MAP()


# CMFC_OSG_MDIDoc construction/destruction

CMFC_OSG_MDIDoc.CMFC_OSG_MDIDoc()

CMFC_OSG_MDIDoc.~CMFC_OSG_MDIDoc()

BOOL CMFC_OSG_MDIDoc.OnOpenDocument(LPCTSTR lpszPathName)
    m_csFileName = lpszPathName

    if !CDocument.OnOpenDocument(lpszPathName) :
      return FALSE

    return TRUE


# CMFC_OSG_MDIDoc serialization

void CMFC_OSG_MDIDoc.Serialize(CArchive ar)
    if ar.IsStoring() :
        # TODO: add storing code here
    else :
        # TODO: add loading code here


# CMFC_OSG_MDIDoc diagnostics

#ifdef _DEBUG
void CMFC_OSG_MDIDoc.AssertValid() 
    CDocument.AssertValid()

void CMFC_OSG_MDIDoc.Dump(CDumpContext dc) 
    CDocument.Dump(dc)
#endif #_DEBUG


# CMFC_OSG_MDIDoc commands

# Translated from file 'MFC_OSG_MDIDoc.h'

# MFC_OSG_MDIDoc.h : interface of the CMFC_OSG_MDIDoc class
#


#pragma once


class CMFC_OSG_MDIDoc (CDocument) : # create from serialization only
    CMFC_OSG_MDIDoc()
    DECLARE_DYNCREATE(CMFC_OSG_MDIDoc)

# Attributes

# Operations

# Overrides
    Serialize = virtual void(CArchive ar)
    OnOpenDocument = virtual BOOL(LPCTSTR lpszPathName)
    def GetFileName():
         return m_csFileName 

# Implementation
    virtual ~CMFC_OSG_MDIDoc()
#ifdef _DEBUG
    virtual void AssertValid() 
    virtual void Dump(CDumpContext dc) 
#endif
    m_csFileName = CString()

# Generated message map functions
    DECLARE_MESSAGE_MAP()




# Translated from file 'MFC_OSG_MDIView.cpp'

# MFC_OSG_MDIView.cpp : implementation of the CMFC_OSG_MDIView class
#

#include "stdafx.h"
#include "MFC_OSG_MDI.h"
#include "MFC_OSG_MDIDoc.h"
#include "MFC_OSG_MDIView.h"

#ifdef _DEBUG
#define DEBUG_NEW
#endif


IMPLEMENT_DYNCREATE(CMFC_OSG_MDIView, CView)

BEGIN_MESSAGE_MAP(CMFC_OSG_MDIView, CView)
    ON_WM_CREATE()
    ON_WM_DESTROY()
    ON_WM_KEYDOWN()
    ON_WM_ERASEBKGND()
END_MESSAGE_MAP()

CMFC_OSG_MDIView.CMFC_OSG_MDIView() :
   mOSG(0L)

CMFC_OSG_MDIView.~CMFC_OSG_MDIView()

BOOL CMFC_OSG_MDIView.PreCreateWindow(CREATESTRUCT cs)
    return CView.PreCreateWindow(cs)

void CMFC_OSG_MDIView.OnDraw(CDC* #pDC)
    pDoc = GetDocument()
    ASSERT_VALID(pDoc)
    if !pDoc :
        return

#ifdef _DEBUG
void CMFC_OSG_MDIView.AssertValid() 
    CView.AssertValid()

void CMFC_OSG_MDIView.Dump(CDumpContext dc) 
    CView.Dump(dc)

CMFC_OSG_MDIDoc* CMFC_OSG_MDIView.GetDocument()  # non-debug version is inline
    ASSERT(m_pDocument.IsKindOf(RUNTIME_CLASS(CMFC_OSG_MDIDoc)))
    return (CMFC_OSG_MDIDoc*)m_pDocument
#endif #_DEBUG


int CMFC_OSG_MDIView.OnCreate(LPCREATESTRUCT lpCreateStruct) 
    # Let MFC create the window before OSG
    if CView.OnCreate(lpCreateStruct) == -1 :
        return -1

    # Now that the window is created setup OSG
    mOSG = cOSG(m_hWnd)

    return 1

void CMFC_OSG_MDIView.OnDestroy()
    mThreadHandle = delete()
    if mOSG != 0 : delete mOSG

    #WaitForSingleObject(mThreadHandle, 1000)

    CView.OnDestroy()

void CMFC_OSG_MDIView.OnInitialUpdate()
    CView.OnInitialUpdate()

    # Get Filename from DocumentOpen Dialog
    csFileName = GetDocument().GetFileName()

    # Init the osg class
    mOSG.InitOSG(csFileName.GetString())

    # Start the thread to do OSG Rendering
    #mThreadHandle = (HANDLE)_beginthread(cOSG.Render, 0, mOSG) 
    mThreadHandle = CRenderingThread(mOSG)
    mThreadHandle.start()

void CMFC_OSG_MDIView.OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags)
    # Pass Key Presses into OSG
    #mOSG.getViewer().getEventQueue().keyPress(nChar)

    # Close Window on Escape Key
    if nChar == VK_ESCAPE :
        GetParent().SendMessage(WM_CLOSE)


BOOL CMFC_OSG_MDIView.OnEraseBkgnd(CDC* pDC)
    # Do nothing, to avoid flashing on MSW 
    return True

# Translated from file 'MFC_OSG_MDIView.h'

# MFC_OSG_MDIView.h : interface of the CMFC_OSG_MDIView class
#
#pragma once

#include "MFC_OSG.h"

class CMFC_OSG_MDIView (CView) : # create from serialization only
    CMFC_OSG_MDIView()
    DECLARE_DYNCREATE(CMFC_OSG_MDIView)

# Attributes
    CMFC_OSG_MDIDoc* GetDocument() 

# Operations

# Overrides
    OnDraw = virtual void(CDC* pDC)  # overridden to draw this view
    OnInitialUpdate = virtual void()
    PreCreateWindow = virtual BOOL(CREATESTRUCT cs)

# Implementation
    virtual ~CMFC_OSG_MDIView()
#ifdef _DEBUG
    virtual void AssertValid() 
    virtual void Dump(CDumpContext dc) 
#endif
    mOSG = cOSG*()
    #HANDLE mThreadHandle
    mThreadHandle = CRenderingThread*()

# Generated message map functions
    DECLARE_MESSAGE_MAP()

    afx_msg int  OnCreate(LPCREATESTRUCT lpCreateStruct)
    afx_msg void OnDestroy()
    afx_msg void OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags)
    afx_msg BOOL OnEraseBkgnd(CDC* pDC)


#ifndef _DEBUG  # debug version in MFC_OSG_MDIView.cpp
inline CMFC_OSG_MDIDoc* CMFC_OSG_MDIView.GetDocument() 
    return reinterpret_cast<CMFC_OSG_MDIDoc*>(m_pDocument) 
#endif


# Translated from file 'Resource.h'

#NO_DEPENDENCIES
# Microsoft Visual C++ generated include file.
# Used by MFC_OSG_MDI.rc
#
#define IDD_ABOUTBOX                100
#define IDR_MAINFRAME                128
#define IDR_MFC_OSG_MDITYPE                129

# Next default values for objects
# 
#ifdef APSTUDIO_INVOKED
#ifndef APSTUDIO_READONLY_SYMBOLS
#define _APS_NEXT_RESOURCE_VALUE    130
#define _APS_NEXT_CONTROL_VALUE        1000
#define _APS_NEXT_SYMED_VALUE        101
#define _APS_NEXT_COMMAND_VALUE        32771
#endif
#endif

# Translated from file 'stdafx.cpp'

# stdafx.cpp : source file that includes just the standard includes
# MFC_OSG_MDI.pch will be the pre-compiled header
# stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"



# Translated from file 'stdafx.h'

# stdafx.h : include file for standard system include files,
# or project specific include files that are used frequently,
# but are changed infrequently

#pragma once

#ifndef _SECURE_ATL
#define _SECURE_ATL 1
#endif

#ifndef VC_EXTRALEAN
#define VC_EXTRALEAN        # Exclude rarely-used stuff from Windows headers
#endif

# Modify the following defines if you have to target a platform prior to the ones specified below.
# Refer to MSDN for the latest info on corresponding values for different platforms.
#ifndef WINVER                # Allow use of features specific to Windows XP or later.
#define WINVER 0x0501        # Change this to the appropriate value to target other versions of Windows.
#endif

#ifndef _WIN32_WINNT        # Allow use of features specific to Windows XP or later.                   
#define _WIN32_WINNT 0x0501    # Change this to the appropriate value to target other versions of Windows.
#endif                        

#ifndef _WIN32_WINDOWS        # Allow use of features specific to Windows 98 or later.
#define _WIN32_WINDOWS 0x0410 # Change this to the appropriate value to target Windows Me or later.
#endif

#ifndef _WIN32_IE            # Allow use of features specific to IE 6.0 or later.
#define _WIN32_IE 0x0600    # Change this to the appropriate value to target other versions of IE.
#endif

#define _ATL_CSTRING_EXPLICIT_CONSTRUCTORS    # some CString constructors will be explicit

# turns off MFC's hiding of some common and often safely ignored warning messages
#define _AFX_ALL_WARNINGS

#include <afxwin.h>         # MFC core and standard components
#include <afxext.h>         # MFC extensions


#ifndef _AFX_NO_OLE_SUPPORT
#include <afxdtctl.h>        # MFC support for Internet Explorer 4 Common Controls
#endif
#ifndef _AFX_NO_AFXCMN_SUPPORT
#include <afxcmn.h>            # MFC support for Windows Common Controls
#endif # _AFX_NO_AFXCMN_SUPPORT

#include <process.h>


#ifdef _UNICODE
#if defined _M_IX86
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='x86' publicKeyToken='6595b64144ccf1df' language='*'\"")
#elif defined _M_IA64
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='ia64' publicKeyToken='6595b64144ccf1df' language='*'\"")
#elif defined _M_X64
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='amd64' publicKeyToken='6595b64144ccf1df' language='*'\"")
#else :
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='*' publicKeyToken='6595b64144ccf1df' language='*'\"")
#endif
#endif




if __name__ == "__main__":
    main(sys.argv)
