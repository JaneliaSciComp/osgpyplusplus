#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgviewerFLTK"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import FL
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osgviewerFLTK.cpp'

# OpenSceneGraph example, osganimate.
#*
#*  C++ source file - (C) 2003 Robert Osfield.
#*  (C) 2005 Mike Weiblen http:#mew.cx/
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


#include <osgViewer/Viewer>
#include <osgViewer/CompositeViewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgDB/ReadFile>

#include <FL/Fl.H>
#include <FL/Fl_Gl_Window.H>

#include <iostream>

class AdapterWidget (Fl_Gl_Window) :

    AdapterWidget(int x, int y, int w, int h,  char *label=0)
    virtual ~AdapterWidget() 

    def getGraphicsWindow():

         return _gw.get() 
    def getGraphicsWindow():
         return _gw.get() 

    resize = virtual void(int x, int y, int w, int h)

    handle = virtual int(int event)
    
    _gw = osgViewer.GraphicsWindowEmbedded()


AdapterWidget.AdapterWidget(int x, int y, int w, int h,  char *label):
    Fl_Gl_Window(x, y, w, h, label)
    _gw = osgViewer.GraphicsWindowEmbedded(x,y,w,h)

void AdapterWidget.resize(int x, int y, int w, int h)
    _gw.getEventQueue().windowResize(x, y, w, h )
    _gw.resized(x,y,w,h)

    Fl_Gl_Window.resize(x,y,w,h)


int AdapterWidget.handle(int event)
    switch(event)
        case FL_PUSH:
            _gw.getEventQueue().mouseButtonPress(Fl.event_x(), Fl.event_y(), Fl.event_button())
            return 1
        case FL_MOVE:
        case FL_DRAG:
            _gw.getEventQueue().mouseMotion(Fl.event_x(), Fl.event_y())
            return 1
        case FL_RELEASE:
            _gw.getEventQueue().mouseButtonRelease(Fl.event_x(), Fl.event_y(), Fl.event_button())
            return 1
        case FL_KEYDOWN:
            _gw.getEventQueue().keyPress((osgGA.GUIEventAdapter.KeySymbol)Fl.event_key())
            return 1
        case FL_KEYUP:
            _gw.getEventQueue().keyRelease((osgGA.GUIEventAdapter.KeySymbol)Fl.event_key())
            return 1
        default:
            # pass other events to the base class
            return Fl_Gl_Window.handle(event)

def idle_cb():

    
    Fl.redraw()

class ViewerFLTK : public osgViewer.Viewer, public AdapterWidget
        ViewerFLTK(int x, int y, int w, int h,  char *label=0):
            AdapterWidget(x,y,w,h,label)
                getCamera().setViewport(osg.Viewport(0,0,w,h))
                getCamera().setProjectionMatrixAsPerspective(30.0, static_cast<double>(w)/static_cast<double>(h), 1.0, 10000.0)
                getCamera().setGraphicsContext(getGraphicsWindow())
                setThreadingModel(osgViewer.Viewer.SingleThreaded)
        def draw():
             frame() 



class CompositeViewerFLTK : public osgViewer.CompositeViewer, public AdapterWidget

        CompositeViewerFLTK(int x, int y, int w, int h,  char *label=0):
            AdapterWidget(x,y,w,h,label)
            setThreadingModel(osgViewer.CompositeViewer.SingleThreaded)
        def draw():
             frame() 




def main(argc, argv):


    
    
    if argc<2 :
        print argv[0], ": requires filename argument."
        return 1

    arguments = osg.ArgumentParser(argc, argv)

    # load the scene.
    loadedModel = osgDB.readNodeFiles(arguments)
    if !loadedModel :
        print argv[0], ": No data loaded."
        return 1


    if arguments.read("--CompositeViewer") :
        width = 1024
        height = 800

        viewerWindow = CompositeViewerFLTK(100,100,width,height)
        viewerWindow.resizable(viewerWindow)
        
            view1 = osgViewer.View()
            view1.getCamera().setGraphicsContext(viewerWindow.getGraphicsWindow())
            view1.getCamera().setProjectionMatrixAsPerspective(30.0, static_cast<double>(width)/static_cast<double>(height/2), 1.0, 1000.0)
            view1.getCamera().setViewport(osg.Viewport(0,0,width,height/2))
            view1.setCameraManipulator(osgGA.TrackballManipulator)()
            view1.setSceneData(loadedModel.get())
            
            viewerWindow.addView(view1)
        
            view2 = osgViewer.View()
            view2.getCamera().setGraphicsContext(viewerWindow.getGraphicsWindow())
            view2.getCamera().setProjectionMatrixAsPerspective(30.0, static_cast<double>(width)/static_cast<double>(height/2), 1.0, 1000.0)
            view2.getCamera().setViewport(osg.Viewport(0,height/2,width,height/2))
            view2.setCameraManipulator(osgGA.TrackballManipulator)()
            view2.setSceneData(loadedModel.get())
            
            viewerWindow.addView(view2)

        viewerWindow.show()

        Fl.set_idle(idle_cb)

        return Fl.run()
    else :

        viewerWindow = ViewerFLTK(100,100,800,600)
        viewerWindow.resizable(viewerWindow)

        viewerWindow.setSceneData(loadedModel.get())
        viewerWindow.setCameraManipulator(osgGA.TrackballManipulator)()
        viewerWindow.addEventHandler(osgViewer.StatsHandler)()

        viewerWindow.show()

        Fl.set_idle(idle_cb)

        return Fl.run()


if __name__ == "__main__":
    main(sys.argv)
