#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgQtBrowser"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgQt
from osgpypp import osgViewer
from osgpypp import osgWidget


# Translated from file 'osgQtBrowser.cpp'

# OpenSceneGraph example, osgcompositeviewer.
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

#include <iostream>

#include <osg/Notify>
#include <osg/io_utils>

#include <osg/ArgumentParser>
#include <osgDB/WriteFile>
#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgWidget/Browser>

#include <QtGlobal>
#if QT_VERSION >= 0x050000
# include <QtWebKitWidgets>
#else:
# include <QtWebKit>
#endif

#include <QWebSettings>

#include <QGraphicsScene>
#include <QGraphicsView>
#include <QApplication>
#include <QPainter>
#include <QtEvents>

#include <osgQt/QGraphicsViewAdapter>
#include <osgQt/QWebViewImage>


# Thread that runs the viewer's frame loop as we can't run Qt in the background...
class ViewerFrameThread (OpenThreads.Thread) :

        ViewerFrameThread(osgViewer.ViewerBase* viewerBase, bool doQApplicationExit):
            _viewerBase(viewerBase),
            _doQApplicationExit(doQApplicationExit) 

        ~ViewerFrameThread()
            cancel()
            while isRunning() :
                OpenThreads.Thread.YieldCurrentThread()

        def cancel():

            
            _viewerBase.setDone(True)
            return 0

        def run():

            
            result = _viewerBase.run()

            if _doQApplicationExit : QApplication.exit(result)

        _viewerBase = osgViewer.ViewerBase()
        _doQApplicationExit = bool()



def main(argv):


    
    # Qt requires that we construct the global QApplication before creating any widgets.
    app = QApplication(argc, argv)

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    useFrameLoopThread = False
    if arguments.read("--no-frame-thread") : useFrameLoopThread = False
    if arguments.read("--frame-thread") : useFrameLoopThread = True

    image = osgQt.QWebViewImage()

    if arguments.argc()>1 : image.navigateTo((arguments[1]))
    else image.navigateTo("http:#www.youtube.com/")

    hints = osgWidget.GeometryHints(osg.Vec3(0.0,0.0,0.0),
                                   osg.Vec3(1.0,0.0,0.0),
                                   osg.Vec3(0.0,0.0,1.0),
                                   osg.Vec4(1.0,1.0,1.0,1.0),
                                   osgWidget.GeometryHints.RESIZE_HEIGHT_TO_MAINTAINCE_ASPECT_RATIO)


    browser = osgWidget.Browser()
    browser.assign(image, hints)

    # image.focusBrowser(True)

    viewer = osgViewer.Viewer(arguments)
    viewer.setSceneData(browser)
    viewer.setCameraManipulator(osgGA.TrackballManipulator())
    viewer.addEventHandler(osgViewer.StatsHandler)()
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()

    if useFrameLoopThread :
        # create a thread to run the viewer's frame loop
        viewerThread = ViewerFrameThread(viewer, True)
        viewerThread.startThread()

        # now start the standard Qt event loop, then exists when the viewerThead sends the QApplication.exit() signal.
        return QApplication.exec()

    else:
        # run the frame loop, interleaving Qt and the main OSG frame loop
        while  not viewer.done() :
            # process Qt events - this handles both events and paints the browser image
            QCoreApplication.processEvents(QEventLoop.AllEvents, 100)

            viewer.frame()

        return 0


if __name__ == "__main__":
    main(sys.argv)
