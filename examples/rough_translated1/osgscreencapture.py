#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgscreencapture"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgscreencapture.cpp'

# -*-c++-*- OpenSceneGraph - Copyright (C) 1998-2006 Robert Osfield 
# *
# * This application is open source and may be redistributed and/or modified   
# * freely and without restriction, both in commercial and non commercial applications,
# * as long as this copyright notice is maintained.
# * 
# * This application is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osgUtil/Optimizer>
#include <osg/CoordinateSystemNode>

#include <osg/Switch>
#include <osgText/Text>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <iostream>
#include <sstream>
#include <string.h>

class WindowCaptureCallback (osg.Camera.DrawCallback) :
    
        enum Mode
            READ_PIXELS,
            SINGLE_PBO,
            DOUBLE_PBO,
            TRIPLE_PBO
        
    
        enum FramePosition
            START_FRAME,
            END_FRAME
        
    
        class ContextData (osg.Referenced) :
ContextData(osg.GraphicsContext* gc, Mode mode, GLenum readBuffer,  str name):
                _gc(gc),
                _mode(mode),
                _readBuffer(readBuffer),
                _fileName(name),
                _pixelFormat(GL_BGRA),
                _type(GL_UNSIGNED_BYTE),
                _width(0),
                _height(0),
                _currentImageIndex(0),
                _currentPboIndex(0),
                _reportTimingFrequency(100),
                _numTimeValuesRecorded(0),
                _timeForReadPixels(0.0),
                _timeForFullCopy(0.0),
                _timeForMemCpy(0.0)

                _previousFrameTick = osg.Timer.instance().tick()

                if gc.getTraits() :
                    if gc.getTraits().alpha :
                        osg.notify(osg.NOTICE), "Select GL_BGRA read back format"
                        _pixelFormat = GL_BGRA
                    else:
                        osg.notify(osg.NOTICE), "Select GL_BGR read back format"
                        _pixelFormat = GL_BGR 
            
                getSize(gc, _width, _height)
                
                print "Window size ", _width, ", ", _height
            
                # single buffered image
                _imageBuffer.push_back(osg.Image)()
                
                # double buffer PBO.
                switch(_mode)
                    case(READ_PIXELS):
                        osg.notify(osg.NOTICE), "Reading window usig glReadPixels, with out PixelBufferObject."
                        break
                    case(SINGLE_PBO): 
                        osg.notify(osg.NOTICE), "Reading window usig glReadPixels, with a single PixelBufferObject."
                        _pboBuffer.push_back(0) 
                        break
                    case(DOUBLE_PBO): 
                        osg.notify(osg.NOTICE), "Reading window usig glReadPixels, with a double buffer PixelBufferObject."
                        _pboBuffer.push_back(0) 
                        _pboBuffer.push_back(0) 
                        break
                    case(TRIPLE_PBO): 
                        osg.notify(osg.NOTICE), "Reading window usig glReadPixels, with a triple buffer PixelBufferObject."
                        _pboBuffer.push_back(0) 
                        _pboBuffer.push_back(0) 
                        _pboBuffer.push_back(0) 
                        break
                    default:
                        break                                
            
            def getSize(gc, width, height):
            
                
                if gc.getTraits() :
                    width = gc.getTraits().width
                    height = gc.getTraits().height
            
            updateTimings = void(osg.Timer_t tick_start,
                               osg.Timer_t tick_afterReadPixels,
                               osg.Timer_t tick_afterMemCpy,
                               unsigned int dataSize)

            def read():

                
                ext = osg.GLBufferObject.getExtensions(_gc.getState().getContextID(),True)

                if ext.isPBOSupported()  and   not _pboBuffer.empty() :
                    if _pboBuffer.size()==1 :
                        singlePBO(ext)
                    else:
                        multiPBO(ext)
                else:
                    readPixels()
            
            readPixels = void()

            singlePBO = void(osg.GLBufferObject.Extensions* ext)

            multiPBO = void(osg.GLBufferObject.Extensions* ext)
        
            typedef std.vector< osg.Image >             ImageBuffer
            typedef std.vector< GLuint > PBOBuffer
        
            _gc = osg.GraphicsContext*()
            _mode = Mode()
            _readBuffer = GLenum()
            _fileName = str()
            
            _pixelFormat = GLenum()
            _type = GLenum()
            _width = int()
            _height = int()
            
            _currentImageIndex = unsigned int()
            _imageBuffer = ImageBuffer()
            
            _currentPboIndex = unsigned int()
            _pboBuffer = PBOBuffer()

            _reportTimingFrequency = unsigned int()
            _numTimeValuesRecorded = unsigned int()
            _timeForReadPixels = double()
            _timeForFullCopy = double()
            _timeForMemCpy = double()
            _previousFrameTick = osg.Timer_t()
        
    
        WindowCaptureCallback(Mode mode, FramePosition position, GLenum readBuffer):
            _mode(mode),
            _position(position),
            _readBuffer(readBuffer)

        def getFramePosition():

             return _position 

        def createContextData(gc):

            
            filename = strstream()
            filename, "test_", _contextDataMap.size(), ".jpg"
            return ContextData(gc, _mode, _readBuffer, filename.str())
        
        def getContextData(gc):
        
            
            lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
            data = _contextDataMap[gc]
            if  not data : data = createContextData(gc)
            
            return data

        virtual void operator () (osg.RenderInfo renderInfo) 
            glReadBuffer(_readBuffer)

            gc = renderInfo.getState().getGraphicsContext()
            cd = getContextData(gc)
            cd.read()
        
        typedef std.map<osg.GraphicsContext*, ContextData > ContextDataMap

        _mode = Mode()        
        _position = FramePosition()
        _readBuffer = GLenum()
        mutable OpenThreads.Mutex  _mutex
        mutable ContextDataMap      _contextDataMap
        
        


void WindowCaptureCallback.ContextData.updateTimings(osg.Timer_t tick_start,
                                                       osg.Timer_t tick_afterReadPixels,
                                                       osg.Timer_t tick_afterMemCpy,
                                                       unsigned int dataSize)
    if  not _reportTimingFrequency : return

    timeForReadPixels = osg.Timer.instance().delta_s(tick_start, tick_afterReadPixels)
    timeForFullCopy = osg.Timer.instance().delta_s(tick_start, tick_afterMemCpy)
    timeForMemCpy = osg.Timer.instance().delta_s(tick_afterReadPixels, tick_afterMemCpy)

    _timeForReadPixels += timeForReadPixels
    _timeForFullCopy += timeForFullCopy
    _timeForMemCpy += timeForMemCpy
    
    ++_numTimeValuesRecorded
    
    if _numTimeValuesRecorded==_reportTimingFrequency :
        timeForReadPixels = _timeForReadPixels/double(_numTimeValuesRecorded)
        timeForFullCopy = _timeForFullCopy/double(_numTimeValuesRecorded)
        timeForMemCpy = _timeForMemCpy/double(_numTimeValuesRecorded)
        
        averageFrameTime = osg.Timer.instance().delta_s(_previousFrameTick, tick_afterMemCpy)/double(_numTimeValuesRecorded)
        fps = 1.0/averageFrameTime    
        _previousFrameTick = tick_afterMemCpy

        _timeForReadPixels = 0.0
        _timeForFullCopy = 0.0
        _timeForMemCpy = 0.0

        _numTimeValuesRecorded = 0

        numMPixels = double(_width * _height) / 1000000.0
        numMb = double(dataSize) / (1024*1024)

        prec = osg.notify(osg.NOTICE).precision(5)

        if timeForMemCpy==0.0 :
            osg.notify(osg.NOTICE), "fps = ", fps, ", full frame copy = ", timeForFullCopy*1000.0, "ms rate = ", numMPixels / timeForFullCopy, " Mpixel/sec, copy speed = ", numMb / timeForFullCopy, " Mb/sec"
        else:
            osg.notify(osg.NOTICE), "fps = ", fps, ", full frame copy = ", timeForFullCopy*1000.0, "ms rate = ", numMPixels / timeForFullCopy, " Mpixel/sec, ", numMb / timeForFullCopy, " Mb/sec ", "time for memcpy = ", timeForMemCpy*1000.0, "ms  memcpy speed = ", numMb / timeForMemCpy, " Mb/sec"
        osg.notify(osg.NOTICE).precision(prec)



void WindowCaptureCallback.ContextData.readPixels()
    # print "readPixels(", _fileName, " image ", _currentImageIndex, " ", _currentPboIndex

    nextImageIndex = (_currentImageIndex+1)%_imageBuffer.size()
    nextPboIndex =  0 if (_pboBuffer.empty()) else  (_currentPboIndex+1)%_pboBuffer.size()

    width = 0, height=0
    getSize(_gc, width, height)
    if width not =_width  or  _height not =height :
        print "   Window resized ", width, ", ", height
        _width = width
        _height = height

    image = _imageBuffer[_currentImageIndex]

    tick_start = osg.Timer.instance().tick()

#if 1
    image.readPixels(0,0,_width,_height,
                      _pixelFormat,_type)
#endif

    tick_afterReadPixels = osg.Timer.instance().tick()

    updateTimings(tick_start, tick_afterReadPixels, tick_afterReadPixels, image.getTotalSizeInBytes())

    if  not _fileName.empty() :
        # osgDB.writeImageFile(*image, _fileName)

    _currentImageIndex = nextImageIndex
    _currentPboIndex = nextPboIndex

void WindowCaptureCallback.ContextData.singlePBO(osg.GLBufferObject.Extensions* ext)
    # print "singelPBO(  ", _fileName, " image ", _currentImageIndex, " ", _currentPboIndex

    nextImageIndex = (_currentImageIndex+1)%_imageBuffer.size()

    width = 0, height=0
    getSize(_gc, width, height)
    if width not =_width  or  _height not =height :
        print "   Window resized ", width, ", ", height
        _width = width
        _height = height

    pbo = _pboBuffer[0]
    
    image = _imageBuffer[_currentImageIndex]
    if image.s()  not = _width  or  
        image.t()  not = _height :
        osg.notify(osg.NOTICE), "Allocating image "
        image.allocateImage(_width, _height, 1, _pixelFormat, _type)
        
        if pbo not =0 :
            osg.notify(osg.NOTICE), "deleting pbo ", pbo
            ext.glDeleteBuffers (1, pbo)
            pbo = 0
    
    
    if pbo==0 :
        ext.glGenBuffers(1, pbo)
        ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, pbo)
        ext.glBufferData(GL_PIXEL_PACK_BUFFER_ARB, image.getTotalSizeInBytes(), 0, GL_STREAM_READ)

        osg.notify(osg.NOTICE), "Generating pbo ", pbo
    else:
        ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, pbo)

    tick_start = osg.Timer.instance().tick()

#if 1
    glReadPixels(0, 0, _width, _height, _pixelFormat, _type, 0)
#endif

    tick_afterReadPixels = osg.Timer.instance().tick()

    src = (GLubyte*)ext.glMapBuffer(GL_PIXEL_PACK_BUFFER_ARB,
                                              GL_READ_ONLY_ARB)
    if src :
        memcpy(image.data(), src, image.getTotalSizeInBytes())
        
        ext.glUnmapBuffer(GL_PIXEL_PACK_BUFFER_ARB)

    ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, 0)

    tick_afterMemCpy = osg.Timer.instance().tick()

    updateTimings(tick_start, tick_afterReadPixels, tick_afterMemCpy, image.getTotalSizeInBytes())

    if  not _fileName.empty() :
        # osgDB.writeImageFile(*image, _fileName)


    _currentImageIndex = nextImageIndex

void WindowCaptureCallback.ContextData.multiPBO(osg.GLBufferObject.Extensions* ext)
    # print "multiPBO(  ", _fileName, " image ", _currentImageIndex, " ", _currentPboIndex
    nextImageIndex = (_currentImageIndex+1)%_imageBuffer.size()
    nextPboIndex = (_currentPboIndex+1)%_pboBuffer.size()

    width = 0, height=0
    getSize(_gc, width, height)
    if width not =_width  or  _height not =height :
        print "   Window resized ", width, ", ", height
        _width = width
        _height = height

    copy_pbo = _pboBuffer[_currentPboIndex]
    read_pbo = _pboBuffer[nextPboIndex]
    
    image = _imageBuffer[_currentImageIndex]
    if image.s()  not = _width  or  
        image.t()  not = _height :
        osg.notify(osg.NOTICE), "Allocating image "
        image.allocateImage(_width, _height, 1, _pixelFormat, _type)
        
        if read_pbo not =0 :
            osg.notify(osg.NOTICE), "deleting pbo ", read_pbo
            ext.glDeleteBuffers (1, read_pbo)
            read_pbo = 0

        if copy_pbo not =0 :
            osg.notify(osg.NOTICE), "deleting pbo ", copy_pbo
            ext.glDeleteBuffers (1, copy_pbo)
            copy_pbo = 0
    
    
    doCopy = copy_pbo not =0
    if copy_pbo==0 :
        ext.glGenBuffers(1, copy_pbo)
        ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, copy_pbo)
        ext.glBufferData(GL_PIXEL_PACK_BUFFER_ARB, image.getTotalSizeInBytes(), 0, GL_STREAM_READ)

        osg.notify(osg.NOTICE), "Generating pbo ", read_pbo

    if read_pbo==0 :
        ext.glGenBuffers(1, read_pbo)
        ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, read_pbo)
        ext.glBufferData(GL_PIXEL_PACK_BUFFER_ARB, image.getTotalSizeInBytes(), 0, GL_STREAM_READ)

        osg.notify(osg.NOTICE), "Generating pbo ", read_pbo
    else:
        ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, read_pbo)

    tick_start = osg.Timer.instance().tick()

#if 1
    glReadPixels(0, 0, _width, _height, _pixelFormat, _type, 0)
#endif

    tick_afterReadPixels = osg.Timer.instance().tick()

    if doCopy :

        ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, copy_pbo)

        src = (GLubyte*)ext.glMapBuffer(GL_PIXEL_PACK_BUFFER_ARB,
                                                  GL_READ_ONLY_ARB)
        if src :
            memcpy(image.data(), src, image.getTotalSizeInBytes())
            ext.glUnmapBuffer(GL_PIXEL_PACK_BUFFER_ARB)

        if  not _fileName.empty() :
            # osgDB.writeImageFile(*image, _fileName)
    
    ext.glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, 0)

    tick_afterMemCpy = osg.Timer.instance().tick()
    
    updateTimings(tick_start, tick_afterReadPixels, tick_afterMemCpy, image.getTotalSizeInBytes())

    _currentImageIndex = nextImageIndex
    _currentPboIndex = nextPboIndex

def addCallbackToViewer(viewer, callback):

    
    
    if callback.getFramePosition()==WindowCaptureCallback.START_FRAME :
        windows = osgViewer.ViewerBase.Windows()
        viewer.getWindows(windows)
        for(osgViewer.ViewerBase.Windows.iterator itr = windows.begin()
            not = windows.end()
            ++itr)
            window = *itr
            cameras = window.getCameras()
            firstCamera = 0
            for(osg.GraphicsContext.Cameras.iterator cam_itr = cameras.begin()
                not = cameras.end()
                ++cam_itr)
                if firstCamera :
                    if *cam_itr :.getRenderOrder() < firstCamera.getRenderOrder() :
                        firstCamera = (*cam_itr)
                    if *cam_itr :.getRenderOrder() == firstCamera.getRenderOrder()  and 
                        (*cam_itr).getRenderOrderNum() < firstCamera.getRenderOrderNum() :
                        firstCamera = (*cam_itr)
                else:
                    firstCamera = *cam_itr

            if firstCamera :
                osg.notify(osg.NOTICE), "First camera ", firstCamera

                firstCamera.setInitialDrawCallback(callback)
            else:
                osg.notify(osg.NOTICE), "No camera found"
    else:
        windows = osgViewer.ViewerBase.Windows()
        viewer.getWindows(windows)
        for(osgViewer.ViewerBase.Windows.iterator itr = windows.begin()
            not = windows.end()
            ++itr)
            window = *itr
            cameras = window.getCameras()
            lastCamera = 0
            for(osg.GraphicsContext.Cameras.iterator cam_itr = cameras.begin()
                not = cameras.end()
                ++cam_itr)
                if lastCamera :
                    if *cam_itr :.getRenderOrder() > lastCamera.getRenderOrder() :
                        lastCamera = (*cam_itr)
                    if *cam_itr :.getRenderOrder() == lastCamera.getRenderOrder()  and 
                        (*cam_itr).getRenderOrderNum() >= lastCamera.getRenderOrderNum() :
                        lastCamera = (*cam_itr)
                else:
                    lastCamera = *cam_itr

            if lastCamera :
                osg.notify(osg.NOTICE), "Last camera ", lastCamera

                lastCamera.setFinalDrawCallback(callback)
            else:
                osg.notify(osg.NOTICE), "No camera found"

def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")

    viewer = osgViewer.Viewer(arguments)

    helpType = 0
    if helpType = arguments.readHelpType() : :
        arguments.getApplicationUsage().write(std.cout, helpType)
        return 1
    
    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1
    
    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    # set up the camera manipulators.
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( ord("1"), "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("2"), "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("3"), "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("4"), "Terrain", osgGA.TerrainManipulator() )

        pathfile = str()
        keyForAnimationPath = ord("5")
        while arguments.read("-p",pathfile) :
            apm = osgGA.AnimationPathManipulator(pathfile)
            if apm  or   not apm.valid() : 
                num = keyswitchManipulator.getNumMatrixManipulators()
                keyswitchManipulator.addMatrixManipulator( keyForAnimationPath, "Path", apm )
                keyswitchManipulator.selectMatrixManipulator(num)
                ++keyForAnimationPath

        viewer.setCameraManipulator( keyswitchManipulator )

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    
    # add the thread model handler
    viewer.addEventHandler(osgViewer.ThreadingHandler)()

    # add the window size toggle handler
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()
        
    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add the help handler
    viewer.addEventHandler(osgViewer.HelpHandler(arguments.getApplicationUsage()))

    # add the record camera path handler
    viewer.addEventHandler(osgViewer.RecordCameraPathHandler)()

    # add the LOD Scale handler
    viewer.addEventHandler(osgViewer.LODScaleHandler)()

    readBuffer = GL_BACK
    position = WindowCaptureCallback.END_FRAME
    mode = WindowCaptureCallback.DOUBLE_PBO

    while arguments.read("--start-frame") :  position = WindowCaptureCallback.START_FRAME readBuffer = GL_FRONT 
    while arguments.read("--end-frame") : position = WindowCaptureCallback.END_FRAME

    while arguments.read("--front") : readBuffer = GL_FRONT
    while arguments.read("--back") : readBuffer = GL_BACK

    while arguments.read("--no-pbo") : mode = WindowCaptureCallback.READ_PIXELS
    while arguments.read("--single-pbo") : mode = WindowCaptureCallback.SINGLE_PBO
    while arguments.read("--double-pbo") : mode = WindowCaptureCallback.DOUBLE_PBO
    while arguments.read("--triple-pbo") : mode = WindowCaptureCallback.TRIPLE_PBO

    
    width = 1280
    height = 1024
    pbufferOnly = False
    pbuffer = osg.GraphicsContext()
    if arguments.read("--pbuffer",width,height)  or  
        (pbufferOnly = arguments.read("--pbuffer-only",width,height)) :
        traits = osg.GraphicsContext.Traits()
        traits.x = 0
        traits.y = 0
        traits.width = width
        traits.height = height
        traits.red = 8
        traits.green = 8
        traits.blue = 8
        traits.alpha = 8
        traits.windowDecoration = False
        traits.pbuffer = True
        traits.doubleBuffer = True
        traits.sharedContext = 0

        pbuffer = osg.GraphicsContext.createGraphicsContext(traits)
        if pbuffer.valid() :
            osg.notify(osg.NOTICE), "Pixel buffer has been created successfully."
        else:
            osg.notify(osg.NOTICE), "Pixel buffer has not been created successfully."

        
    # load the data
    loadedModel = osgDB.readNodeFiles(arguments)
    if  not loadedModel : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1


    # optimize the scene graph, remove redundant nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel)

    viewer.setSceneData( loadedModel )

    
    if pbuffer.valid() :
        camera = osg.Camera()
        camera.setGraphicsContext(pbuffer)
        camera.setViewport(osg.Viewport(0,0,width,height))
        buffer =  GL_BACK if (pbuffer.getTraits().doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setFinalDrawCallback(WindowCaptureCallback(mode, position, readBuffer))

        if pbufferOnly :
            viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd())

            viewer.realize()
        else:
            viewer.realize()

            viewer.stopThreading()

            pbuffer.realize()

            viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd())

            viewer.startThreading()
    else:
        viewer.realize()

        addCallbackToViewer(viewer, WindowCaptureCallback(mode, position, readBuffer))

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
