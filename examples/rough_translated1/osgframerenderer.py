#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgframerenderer"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'CameraPathProperty.cpp'

#include "CameraPathProperty.h"

using namespace gsc

void CameraPathProperty.update(osgViewer.View* view)
    camera = view.getCamera()
    fs = view.getFrameStamp()

    if _animationPath.valid() :
        cp = osg.AnimationPath.ControlPoint()
        _animationPath.getInterpolatedControlPoint( fs.getSimulationTime(), cp )

        OSG_NOTICE, "CameraPathProperty ", fs.getFrameNumber(), " ", fs.getSimulationTime()

        matrix = osg.Matrixd()
        cp.getMatrix( matrix )
        camera.setViewMatrix( osg.Matrix.inverse(matrix) )

void CameraPathProperty.loadAnimationPath()
    _animationPath = osg.AnimationPath()
    #_animationPath.setLoopMode(osg.AnimationPath.LOOP)

    in = osgDB.ifstream(_filename.c_str())
    if  not in :
        OSG_WARN, "CameraPathProperty: Cannot open animation path file \"", _filename, "\".\n"
        return

    _animationPath.read(in)

bool CameraPathProperty.getTimeRange(double startTime, double endTime) 
    if  not _animationPath : return False
    
    tcpm = _animationPath.getTimeControlPointMap()
    if tcpm.empty() : return False

    startTime = tcpm.begin().first
    endTime = tcpm.rbegin().first
    
    return True

void CameraPathProperty.resetTimeRange(double startTime, double endTime)
    if  not _animationPath : return

    tcpm = _animationPath.getTimeControlPointMap()
    if tcpm.empty() : return

    copy_tcpm = tcpm

    offset = tcpm.begin().first
    originalLength = tcpm.rbegin().first - tcpm.begin().first 
    scale =  (endTime-startTime)/originalLength if (originalLength>0.0) else  1.0

    tcpm.clear()

    for(osg.AnimationPath.TimeControlPointMap.iterator itr = copy_tcpm.begin()
        not = copy_tcpm.end()
        ++itr)
        tcpm[startTime + (itr.first-offset)*scale] = itr.second

############################################/
#
# Serialization support
#
REGISTER_OBJECT_WRAPPER( gsc_CameraPathProperty,
                         gsc.CameraPathProperty,
                         gsc.CameraPathProperty,
                         "osg.Object gsc.CameraPathProperty" )
    ADD_STRING_SERIALIZER( AnimationPathFileName, "" )





# Translated from file 'CameraPathProperty.h'

#ifndef CAMERAPATHPROPERTY_H
#define CAMERAPATHPROPERTY_H

#include <osg/AnimationPath>

#include "UpdateProperty.h"

namespace gsc

class CameraPathProperty (gsc.UpdateProperty) :

    CameraPathProperty() 
    CameraPathProperty( str filename)  setAnimationPathFileName(filename) 
    CameraPathProperty( CameraPathProperty cpp,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY) 
 
    META_Object(gsc, CameraPathProperty)

    def setAnimationPathFileName(filename):

         _filename = filename loadAnimationPath() 
    def getAnimationPathFileName():
         return _filename 

    def setAnimationPath(ap):

         _animationPath = ap 
    def getAnimationPath():
         return _animationPath 
    def getAnimationPath():
         return _animationPath 

    bool getTimeRange(double startTime, double endTime) 

    resetTimeRange = void(double startTime, double endTime)

    update = virtual void(osgViewer.View* view)

    virtual ~CameraPathProperty() 

    loadAnimationPath = void()

    _filename = str()
    _animationPath = osg.AnimationPath()



#endif
# Translated from file 'CameraProperty.cpp'

#include "CameraProperty.h"

using namespace gsc

void CameraProperty.setToModel( osg.Node* node)
    bs = node.getBound()

    dist = osg.DisplaySettings.instance().getScreenDistance()

    OSG_NOTICE, "Node name ", node.getName()
    
#if 1
    if node.getName().find("Presentation")==str.npos :
        screenWidth = osg.DisplaySettings.instance().getScreenWidth()
        screenHeight = osg.DisplaySettings.instance().getScreenHeight()
        screenDistance = osg.DisplaySettings.instance().getScreenDistance()

        vfov = atan2(screenHeight/2.0,screenDistance)*2.0
        hfov = atan2(screenWidth/2.0,screenDistance)*2.0
        viewAngle =  vfov if (vfov<hfov) else  hfov

        dist = bs.radius() / sin(viewAngle*0.5)
#endif

    _center = bs.center()
    _eye = _center - osg.Vec3d(0.0, dist, 0.0)
    _up = osg.Vec3d(0.0, 0.0, 1.0)
    
    _rotationCenter = _center
    _rotationAxis = osg.Vec3d(0.0, 0.0, 1.0)
    _rotationSpeed = 0.0


void CameraProperty.update(osgViewer.View* view)
    camera = view.getCamera()
    fs = view.getFrameStamp()

    matrix = osg.Matrixd()
    matrix.makeLookAt(_eye, _center, _up)

    if _rotationSpeed not =0.0 :
        matrix.preMult(osg.Matrixd.translate(-_rotationCenter) *
                    osg.Matrix.rotate(osg.DegreesToRadians(_rotationSpeed*fs.getSimulationTime()), _rotationAxis) *
                    osg.Matrixd.translate(_rotationCenter))
    
    camera.setViewMatrix( matrix )

    # set the fusion distance up so that the left and right eye images are co-incedent on the image plane at the center of ration.
    view.setFusionDistance(osgUtil.SceneView.USE_FUSION_DISTANCE_VALUE,(_center-_eye).length())
    # view.setFusionDistance(osgUtil.SceneView.PROPORTIONAL_TO_SCREEN_DISTANCE, 1.0)


############################################/
#
# Serialization support
#
REGISTER_OBJECT_WRAPPER( gsc_CameraProperty,
                         gsc.CameraProperty,
                         gsc.CameraProperty,
                         "osg.Object gsc.CameraProperty" )
    ADD_VEC3D_SERIALIZER( Center, osg.Vec3d(0.0,0.0,0.0) )
    ADD_VEC3D_SERIALIZER( EyePoint, osg.Vec3d(0.0,-1.0,0.0) )
    ADD_VEC3D_SERIALIZER( UpVector, osg.Vec3d(0.0,0.0,1.0) )
    ADD_VEC3D_SERIALIZER( RotationCenter, osg.Vec3d(0.0,0.0,0.0) )
    ADD_VEC3D_SERIALIZER( RotationAxis, osg.Vec3d(0.0,0.0,1.0) )
    ADD_DOUBLE_SERIALIZER( RotationSpeed, 0.0 )
    





# Translated from file 'CameraProperty.h'

#ifndef CAMERAPROPERTY_H
#define CAMERAPROPERTY_H

#include <osg/AnimationPath>

#include "UpdateProperty.h"

namespace gsc

class CameraProperty (gsc.UpdateProperty) :

    CameraProperty():
        _center(0.0,0.0,0.0),
        _eye(0.0,-1.0,0.0),
        _up(0.0,0.0,1.0),
        _rotationCenter(0.0,0.0,0.0),
        _rotationAxis(0.0,0.0,1.0),
        _rotationSpeed(0.0) 
        
    CameraProperty( CameraProperty cp,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY):
        _center(cp._center),
        _eye(cp._eye),
        _up(cp._up),
        _rotationCenter(cp._rotationCenter),
        _rotationAxis(cp._rotationAxis),
        _rotationSpeed(cp._rotationSpeed)
        
 
    META_Object(gsc, CameraProperty)

    setToModel = void( osg.Node* node)

    def setCenter(center):

         _center = center 
    def getCenter():
         return _center 

    def setEyePoint(eye):

         _eye = eye 
    def getEyePoint():
         return _eye 
    
    def setUpVector(up):
    
         _up = up 
    def getUpVector():
         return _up 

    def setRotationCenter(center):

         _rotationCenter = center 
    def getRotationCenter():
         return _rotationCenter 

    def setRotationAxis(axis):

         _rotationAxis = axis 
    def getRotationAxis():
         return _rotationAxis 

    def setRotationSpeed(speed):

         _rotationSpeed = speed 
    def getRotationSpeed():
         return _rotationSpeed 

    update = virtual void(osgViewer.View* view)

    virtual ~CameraProperty() 


    _center = osg.Vec3d()
    _eye = osg.Vec3d()
    _up = osg.Vec3d()
    _rotationCenter = osg.Vec3d()
    _rotationAxis = osg.Vec3d()
    _rotationSpeed = double()




#endif
# Translated from file 'CaptureSettings.cpp'

#include "CaptureSettings.h"

using namespace gsc

CaptureSettings.CaptureSettings():
    _stereoMode(OFF),
    _offscreen(False),
    _outputImageFlip(False),
    _width(1024),
    _height(512),
    _screenWidth(0.0),
    _screenHeight(0.0),
    _screenDistance(0.0),
    _samples(0),
    _sampleBuffers(0),
    _frameRate(60.0),
    _numberOfFrames(0.0)

CaptureSettings.CaptureSettings( CaptureSettings cs,  osg.CopyOp copyop):
    osg.Object(cs, copyop),
    _inputFileName(cs._inputFileName),
    _outputFileName(cs._outputFileName),
    _outputDirectoryName(cs._outputDirectoryName),
    _outputBaseFileName(cs._outputBaseFileName),
    _outputExtension(cs._outputExtension),
    _stereoMode(cs._stereoMode),
    _offscreen(cs._offscreen),
    _outputImageFlip(cs._outputImageFlip),
    _width(cs._width),
    _height(cs._height),
    _screenWidth(cs._screenWidth),
    _screenHeight(cs._screenHeight),
    _screenDistance(cs._screenDistance),
    _samples(cs._samples),
    _sampleBuffers(cs._sampleBuffers),
    _frameRate(cs._frameRate),
    _numberOfFrames(cs._numberOfFrames),
    _eventHandlers(cs._eventHandlers),
    _properties(cs._properties)

void CaptureSettings.setOutputFileName( str filename)
    _outputFileName = filename
    
    _outputDirectoryName = osgDB.getFilePath(filename)
    if  not _outputDirectoryName.empty() : _outputDirectoryName += osgDB.getNativePathSeparator()
    
    _outputBaseFileName = osgDB.getStrippedName(filename)
    
    _outputExtension = osgDB.getFileExtensionIncludingDot(filename)

 str CaptureSettings.getOutputFileName() 
    return _outputFileName

str CaptureSettings.getOutputFileName(unsigned int frameNumber) 
    str = strstream()
    str, _outputDirectoryName, _outputBaseFileName, "_", frameNumber, _outputExtension
    return str.str()
str CaptureSettings.getOutputFileName(unsigned int cameraNum, unsigned int frameNumber) 
    str = strstream()
    str, _outputDirectoryName, _outputBaseFileName, "_", cameraNum, "_", frameNumber, _outputExtension
    return str.str()

bool CaptureSettings.valid() 
    return _numberOfFrames>0  and   not _outputBaseFileName.empty()  and   not _outputExtension.empty()  and   not _inputFileName.empty()


############################################/
#
# Serialization support
#
static bool checkEventHandlers(  gsc.CaptureSettings cs )
    return  not cs.getEventHandlers().empty()

static bool readEventHandlers( osgDB.InputStream is, gsc.CaptureSettings cs )
    size = 0 is >> size >> is.BEGIN_BRACKET
    for ( unsigned int i=0 i<size ++i )
        obj = is.readObject()
        up = dynamic_cast<gsc.UpdateProperty*>( obj )
        if  up  : cs.addUpdateProperty( up )
    is >> is.END_BRACKET
    return True

static bool writeEventHandlers( osgDB.OutputStream os,  gsc.CaptureSettings cs )
    pl = cs.getEventHandlers()
    size = pl.size()
    os, size, os.BEGIN_BRACKET
    for ( unsigned int i=0 i<size ++i )
        os, pl[i]
    os, os.END_BRACKET
    return True

static bool checkProperties(  gsc.CaptureSettings cs )
    return  not cs.getProperties().empty()

static bool readProperties( osgDB.InputStream is, gsc.CaptureSettings cs )
    size = 0 is >> size >> is.BEGIN_BRACKET
    for ( unsigned int i=0 i<size ++i )
        obj = is.readObject()
        up = dynamic_cast<gsc.UpdateProperty*>( obj )
        if  up  : cs.addUpdateProperty( up )
    is >> is.END_BRACKET
    return True

static bool writeProperties( osgDB.OutputStream os,  gsc.CaptureSettings cs )
    pl = cs.getProperties()
    size = pl.size()
    os, size, os.BEGIN_BRACKET
    for ( unsigned int i=0 i<size ++i )
        os, pl[i]
    os, os.END_BRACKET
    return True

REGISTER_OBJECT_WRAPPER( gsc_CaptureSettings,
                         gsc.CaptureSettings,
                         gsc.CaptureSettings,
                         "osg.Object gsc.CaptureSettings" )
    ADD_STRING_SERIALIZER( InputFileName, "" )
    ADD_STRING_SERIALIZER( OutputFileName, "" )
    ADD_DOUBLE_SERIALIZER( FrameRate, 60.0 )

    BEGIN_ENUM_SERIALIZER( StereoMode, OFF )
        ADD_ENUM_VALUE( OFF )
        ADD_ENUM_VALUE( HORIZONTAL_SPLIT )
        ADD_ENUM_VALUE( VERTICAL_SPLIT )
    END_ENUM_SERIALIZER()

    ADD_BOOL_SERIALIZER( Offscreen, False )
    ADD_BOOL_SERIALIZER( OutputImageFlip, False )

    ADD_UINT_SERIALIZER( Width, 1024 )
    ADD_UINT_SERIALIZER( Height, 512 )

    ADD_FLOAT_SERIALIZER( ScreenWidth, 0.0 )
    ADD_FLOAT_SERIALIZER( ScreenHeight, 0.0 )
    ADD_FLOAT_SERIALIZER( ScreenDistance, 0.0 )

    BEGIN_ENUM_SERIALIZER( PixelFormat, RGB )
        ADD_ENUM_VALUE( RGB )
        ADD_ENUM_VALUE( RGBA )
    END_ENUM_SERIALIZER()
    
    ADD_UINT_SERIALIZER( Samples, 0 )
    ADD_UINT_SERIALIZER( SampleBuffers, 0 )
    
    ADD_UINT_SERIALIZER( NumberOfFrames, 0 )
    ADD_USER_SERIALIZER( EventHandlers )
    ADD_USER_SERIALIZER( Properties )


    


# Translated from file 'CaptureSettings.h'

#ifndef CAPTURESETTINGS_H
#define CAPTURESETTINGS_H

#include <osgDB/ReadFile>
#include <osgDB/FileNameUtils>
#include <osgDB/WriteFile>
#include <osgViewer/Viewer>
#include <osg/AnimationPath>

#include "UpdateProperty.h"

namespace gsc

class CaptureSettings (osg.Object) :
    CaptureSettings()
    CaptureSettings( CaptureSettings cs,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY)

    META_Object(gsc, CaptureSettings)

    def setInputFileName(filename):

         _inputFileName = filename 
    def getInputFileName():
         return _inputFileName 
    
    setOutputFileName = void( str filename)
     str getOutputFileName() 
    
    str getOutputFileName(unsigned int frameNumber) 
    str getOutputFileName(unsigned int cameraNumber, unsigned int frameNumber) 

    enum StereoMode
        OFF,
        HORIZONTAL_SPLIT,
        VERTICAL_SPLIT
    

    def setStereoMode(mode):

         _stereoMode = mode 
    def getStereoMode():
         return _stereoMode 

    def setOffscreen(o):

         _offscreen = o 
    def getOffscreen():
         return _offscreen 

    def setOutputImageFlip(flip):

         _outputImageFlip = flip 
    def getOutputImageFlip():
         return _outputImageFlip 

    def setWidth(width):

         _width = width 
    def getWidth():
         return _width 

    def setHeight(height):

         _height = height 
    def getHeight():
         return _height 

    def setScreenWidth(width):

         _screenWidth = width 
    def getScreenWidth():
         return _screenWidth 

    def setScreenHeight(height):

         _screenHeight = height 
    def getScreenHeight():
         return _screenHeight 

    def setScreenDistance(distance):

         _screenDistance = distance 
    def getScreenDistance():
         return _screenDistance 


    enum PixelFormat
        RGB,
        RGBA
    
    
    def setPixelFormat(format):
    
         _pixelFormat = format 
    def getPixelFormat():
         return _pixelFormat 

    def setSamples(s):

         _samples = s 
    def getSamples():
         return _samples 

    def setSampleBuffers(s):

         _sampleBuffers = s 
    def getSampleBuffers():
         return _sampleBuffers 

    def setFrameRate(fr):

         _frameRate = fr 
    def getFrameRate():
         return _frameRate 

    def setNumberOfFrames(nf):

         _numberOfFrames = nf 
    def getNumberOfFrames():
         return _numberOfFrames 

    typedef std.vector< osgGA.GUIEventHandler > EventHandlers
    setEventHandlers = void( EventHandlers eh)
    def getEventHandlers():
         return _eventHandlers 
    def getEventHandlers():
         return _eventHandlers 

    typedef std.vector< UpdateProperty > Properties

    def addUpdateProperty(up):

         _properties.push_back(up) 
    
    def setProperties(pl):
    
         _properties = pl 
    def getProperties():
         return _properties 
    def getProperties():
         return _properties 

    template<typename T>
    def getPropertyOfType():
        
        for(Properties.iterator itr = _properties.begin()
            not = _properties.end()
            ++itr)
            p = dynamic_cast<T*>(itr)
            if p : return p
        return 0
    
    bool valid() 
    virtual ~CaptureSettings() 

    _inputFileName = str()

    _outputFileName = str()
    _outputDirectoryName = str()
    _outputBaseFileName = str()
    _outputExtension = str()

    _stereoMode = StereoMode()
    _offscreen = bool()
    _outputImageFlip = bool()
    
    _width = unsigned int()
    _height = unsigned int()
    
    _screenWidth = float()
    _screenHeight = float()
    _screenDistance = float()

    _pixelFormat = PixelFormat()
    _samples = unsigned int()
    _sampleBuffers = unsigned int()
    
    _frameRate = double()
    _numberOfFrames = unsigned int()

    _eventHandlers = EventHandlers()
    _properties = Properties()
    

    

#endif

# Translated from file 'EventProperty.cpp'

#include "EventProperty.h"

namespace gsc

void EventProperty.update(osgViewer.View* view)
    if view  and  view.getEventQueue()  and  _event.valid() :
        view.getEventQueue().addEvent(_event)

############################################/
#
# Serialization support
#
REGISTER_OBJECT_WRAPPER( gsc_EventProperty,
                         gsc.EventProperty,
                         gsc.EventProperty,
                         "osg.Object gsc.EventProperty" )
    ADD_OBJECT_SERIALIZER( Event, osgGA.GUIEventAdapter, NULL )



namespace osgGA

    

    
namespace B


 

# Translated from file 'EventProperty.h'

#ifndef EVENTPROPERTY_H
#define EVENTPROPERTY_H

#include <osgGA/GUIEventAdapter>
#include "UpdateProperty.h"

namespace gsc

class EventProperty (gsc.UpdateProperty) :

    EventProperty() 
    EventProperty(osgGA.GUIEventAdapter* event):_event(event) 
    EventProperty( EventProperty cpp,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY) 

    META_Object(gsc, EventProperty)

    def setEvent(ea):

         _event = ea 
    def getEvent():
         return _event 
    def getEvent():
         return _event 
    
    update = virtual void(osgViewer.View* view)

    virtual ~EventProperty() 

    _previousFrameTime = double()
    _event = osgGA.GUIEventAdapter()





#endif
# Translated from file 'osgframerenderer.cpp'

#include <osgDB/ReadFile>
#include <osgDB/FileUtils>
#include <osgDB/FileNameUtils>
#include <osgDB/WriteFile>
#include <osgViewer/Viewer>
#include <osg/AnimationPath>

#include "UpdateProperty.h"
#include "CameraProperty.h"
#include "CameraPathProperty.h"
#include "EventProperty.h"

#include "CaptureSettings.h"

#include <osgGA/StateSetManipulator>


class ScreenShot (osg.Camera.DrawCallback) :
ScreenShot(GLenum pixelFormat, bool flip):
        _pixelFormat(pixelFormat),
        _flip(flip) 

    virtual void operator () (osg.RenderInfo renderInfo) 
        if  not _frameCapture :
            OSG_NOTICE, "No FrameCamera assigned"
            return

        frameNumber = renderInfo.getState().getFrameStamp().getFrameNumber()
        
        itr = _cameraNumMap.find(renderInfo.getCurrentCamera())
        outputFileName =  _frameCapture.getOutputFileName(itr.second, frameNumber) if ((itr not =_cameraNumMap.end())) else 
                                     _frameCapture.getOutputFileName(frameNumber)
                                     
        OSG_NOTICE, "outputFileName=", outputFileName

        camera = renderInfo.getCurrentCamera()
        viewport =  camera.getViewport() if (camera) else  0
        if viewport :
            OSG_NOTICE, "Doing read of =", viewport.x(), ", ", viewport.y(), ", ", viewport.width(), ", ", viewport.height(), " with pixelFormat=0x", std.hex, _pixelFormat, std.dec

            glReadBuffer(camera.getDrawBuffer())
            image = osg.Image()
            
            image.readPixels(viewport.x(),viewport.y(),viewport.width(),viewport.height(),
                              _pixelFormat, GL_UNSIGNED_BYTE, 1)

            if _flip : image.flipVertical()

            osgDB.writeImageFile(*image, outputFileName)
        

    typedef std.map< osg.Camera*, unsigned int> CameraNumMap

    _pixelFormat = GLenum()
    _flip = bool()
    _frameCapture = gsc.CaptureSettings()
    _cameraNumMap = CameraNumMap()


def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use of 3D textures.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options]")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("-i <filename>","Input scene (or presentation) filename.")
    arguments.getApplicationUsage().addCommandLineOption("-o <filename>","Base ouput filename of the images, recommended to use something like Images/image.png")
    arguments.getApplicationUsage().addCommandLineOption("--cs <filename>","Load pre-generated configuration file for run.")
    arguments.getApplicationUsage().addCommandLineOption("--ouput-cs <filename>","Output configuration file with settings provided on commandline.")
    arguments.getApplicationUsage().addCommandLineOption("-p <filename>","Use specificied camera path file to control camera position.")
    arguments.getApplicationUsage().addCommandLineOption("--offscreen","Use an pbuffer to render the images offscreen.")
    arguments.getApplicationUsage().addCommandLineOption("--screen","Use an window to render the images.")
    arguments.getApplicationUsage().addCommandLineOption("--width <width>","Window/output image width.")
    arguments.getApplicationUsage().addCommandLineOption("--height <height>","Window/output image height.")
    arguments.getApplicationUsage().addCommandLineOption("--screen-distance <distance>","Set the distance of the viewer from the physical screen.")
    arguments.getApplicationUsage().addCommandLineOption("--screen-width <width>","Set the width of the physical screen.")
    arguments.getApplicationUsage().addCommandLineOption("--screen-height <height>","Set the height of the physical screen.")
    arguments.getApplicationUsage().addCommandLineOption("--ms <s>","Number of multi-samples to use when rendering, an enable a single sample buffer.")
    arguments.getApplicationUsage().addCommandLineOption("--samples <s>","Number of multi-samples to use when rendering.")
    arguments.getApplicationUsage().addCommandLineOption("--sampleBuffers <sb>","Number of sample buffers to use when rendering.")
    arguments.getApplicationUsage().addCommandLineOption("-f <fps>","Number of frames per second in simulation time.")
    arguments.getApplicationUsage().addCommandLineOption("-n <frames>","Number of frames to render/images to create.")
    arguments.getApplicationUsage().addCommandLineOption("-d <time>","Duration of rendering run (duration = frames/fps).")
    arguments.getApplicationUsage().addCommandLineOption("--center <x> <y> <z>","View center.")
    arguments.getApplicationUsage().addCommandLineOption("--eye <x> <y> <z>","Camera eye point.")
    arguments.getApplicationUsage().addCommandLineOption("--up <x> <y> <z>","Camera up vector.")
    arguments.getApplicationUsage().addCommandLineOption("--rotation-center <x> <y> <z>","Position to rotatate around.")
    arguments.getApplicationUsage().addCommandLineOption("--rotation-axis <x> <y> <z>","Axis to rotate around.")
    arguments.getApplicationUsage().addCommandLineOption("--rotation-speed <v>","Degrees per second.")
    arguments.getApplicationUsage().addCommandLineOption("--stereo <mode>","OFF | HORIZONTAL_SPLIT | VERTICAL_SPLIT")

    helpType = 0
    if helpType = arguments.readHelpType() : :
        arguments.getApplicationUsage().write(std.cout, helpType)
        return 1

    viewer = osgViewer.Viewer()

    typedef std.list< gsc.CaptureSettings > CaptureSettingsList
    frameCaptureList = CaptureSettingsList()

    fc = gsc.CaptureSettings()

    duration = 0.0
    fps = 0.0
    nframes = 0

    readCaptureSettings = False
    filename = str()
    if arguments.read("--cs",filename) :
        object = osgDB.readObjectFile(filename)
        input_cs = dynamic_cast<gsc.CaptureSettings*>(object)
        if input_cs :  fc = input_cs readCaptureSettings = True 
        else:
            OSG_NOTICE, "Unable to read CaptureSettings from file: ", filename
            if object.valid() : OSG_NOTICE, "Object read, ", object, ", className()=", object.className()
            return 1

    screenWidth = fc.getScreenWidth() not  fc.getScreenWidth() : osg.DisplaySettings: if (=0.0) else instance().getScreenWidth()
    if arguments.read("--screen-width",screenWidth) : 

    screenHeight = fc.getScreenHeight() not  fc.getScreenHeight() : osg.DisplaySettings: if (=0.0) else instance().getScreenHeight()
    if arguments.read("--screen-height",screenHeight) : 

    screenDistance = fc.getScreenDistance() not  fc.getScreenDistance() : osg.DisplaySettings: if (=0.0) else instance().getScreenDistance()
    if arguments.read("--screen-distance",screenDistance) : 

    fc.setScreenWidth(screenWidth)
    osg.DisplaySettings.instance().setScreenWidth(screenWidth)
    
    fc.setScreenHeight(screenHeight)
    osg.DisplaySettings.instance().setScreenHeight(screenHeight)

    fc.setScreenDistance(screenDistance)
    osg.DisplaySettings.instance().setScreenDistance(screenDistance)

    useScreenSizeForProjectionMatrix = True

    if arguments.read("-i",filename) : fc.setInputFileName(filename)
    if arguments.read("-o",filename) : fc.setOutputFileName(filename)
    if arguments.read("-p",filename) :
        cpp = gsc.CameraPathProperty()
        cpp.setAnimationPathFileName(filename)

        startTime = 0, endTime = 1.0
        if cpp.getTimeRange(startTime, endTime) :
            OSG_NOTICE, "Camera path time range ", startTime, ", ", endTime
            if startTime not =0.0 :
                cpp.resetTimeRange(0.0, endTime-startTime)
                if cpp.getTimeRange(startTime, endTime) :
                    OSG_NOTICE, "   time range ", startTime, ", ", endTime()
                else:
                    OSG_NOTICE, "   failed to set time range ", startTime, ", ", endTime()
            duration = endTime            
        else:
            OSG_NOTICE, "Camera path time range ", startTime, ", ", endTime

        fc.addUpdateProperty(cpp)
    else:
        cp = fc.getPropertyOfType<gsc.CameraProperty>()

        newCameraProperty = False
        valueSet = False
        
        if  not cp :
            newCameraProperty = True
            cp = gsc.CameraProperty()

            node =  0 : osgDB: if (fc.getInputFileName().empty()) else readNodeFile(fc.getInputFileName())
            if node.valid() :
                cp.setToModel(node)
                valueSet = True
            
        
        vec = osg.Vec3d()
        while arguments.read("--center",vec.x(), vec.y(), vec.z()) :  cp.setCenter(vec) valueSet = True 
        while arguments.read("--eye",vec.x(), vec.y(), vec.z()) :  cp.setEyePoint(vec) valueSet = True 
        while arguments.read("--up",vec.x(), vec.y(), vec.z()) :  cp.setUpVector(vec) valueSet = True 
        while arguments.read("--rotation-center",vec.x(), vec.y(), vec.z()) :  cp.setRotationCenter(vec) valueSet = True 
        while arguments.read("--rotation-axis",vec.x(), vec.y(), vec.z()) :  cp.setRotationAxis(vec) valueSet = True 

        speed = double()
        while arguments.read("--rotation-speed",speed) :  cp.setRotationSpeed(speed) valueSet = True 

        if newCameraProperty  and  valueSet :
            fc.addUpdateProperty(cp)

    stereoMode = str()
    if arguments.read("--stereo", stereoMode) :
        if stereoMode=="HORIZONTAL_SPLIT" : fc.setStereoMode(gsc.CaptureSettings.HORIZONTAL_SPLIT)
        elif stereoMode=="VERTICAL_SPLIT" : fc.setStereoMode(gsc.CaptureSettings.VERTICAL_SPLIT)
        elif stereoMode=="OFF" : fc.setStereoMode(gsc.CaptureSettings.OFF)

    if arguments.read("--offscreen") : fc.setOffscreen(True)
    if arguments.read("--screen") : fc.setOffscreen(False)

    if arguments.read("--flip") : fc.setOutputImageFlip(True)
    if arguments.read("--no-flip") : fc.setOutputImageFlip(False)

    width = 1024
    if arguments.read("--width",width) : fc.setWidth(width)

    height = 512
    if arguments.read("--height",height) : fc.setHeight(height)

    if arguments.read("--rgb") : fc.setPixelFormat(gsc.CaptureSettings.RGB)
    if arguments.read("--rgba") : fc.setPixelFormat(gsc.CaptureSettings.RGBA)
    
    clearColor = osg.Vec4(0.0,0.0,0.0,0.0)
    while arguments.read("--clear-color",clearColor[0],clearColor[1],clearColor[2],clearColor[3]) : 


    samples = 0
    if arguments.read("--samples",samples) : fc.setSamples(samples)

    sampleBuffers = 0
    if arguments.read("--sampleBuffers",sampleBuffers) : fc.setSampleBuffers(sampleBuffers)

    ms = 0
    if arguments.read("--ms",ms) :
        fc.setSamples(ms)
        fc.setSampleBuffers(1)

    if arguments.read("-f",fps) : fc.setFrameRate(fps)

    if arguments.read("-n",nframes) : fc.setNumberOfFrames(nframes)

    if arguments.read("-d",duration) : 


    key = str()
    time = double()
    while arguments.read("--key-down",time, key)  and  key.size()>=1 :
        OSG_NOTICE, "keydown ", key, ", ", time
        event = osgGA.GUIEventAdapter()
        event.setTime(time)
        event.setEventType(osgGA.GUIEventAdapter.KEYDOWN)
        event.setKey(key[0])
        fc.addUpdateProperty(gsc.EventProperty(event))

    while arguments.read("--key-up",time, key)  and  key.size()>=1 :
        OSG_NOTICE, "keyup ", key, ", ", time
        event = osgGA.GUIEventAdapter()
        event.setTime(time)
        event.setEventType(osgGA.GUIEventAdapter.KEYUP)
        event.setKey(key[0])
        fc.addUpdateProperty(gsc.EventProperty(event))

    double mouse_x, mouse_y
    while arguments.read("--mouse-move",time, mouse_x, mouse_y) :
        OSG_NOTICE, "mouse move ", time, ", ", mouse_x, ", ", mouse_y
        event = osgGA.GUIEventAdapter()
        event.setTime(time)
        event.setEventType(osgGA.GUIEventAdapter.MOVE)
        event.setX(mouse_x)
        event.setY(mouse_y)
        fc.addUpdateProperty(gsc.EventProperty(event))

    while arguments.read("--mouse-drag",time, mouse_x, mouse_y) :
        OSG_NOTICE, "mouse drag ", time, ", ", mouse_x, ", ", mouse_y
        event = osgGA.GUIEventAdapter()
        event.setTime(time)
        event.setEventType(osgGA.GUIEventAdapter.DRAG)
        event.setX(mouse_x)
        event.setY(mouse_y)
        fc.addUpdateProperty(gsc.EventProperty(event))


    if  not readCaptureSettings :
        if duration not =0.0 :
            if fps not =0.0 : nframes = static_cast<unsigned int>(ceil(duration*fps))
            elif nframes not =0 : fps = duration/static_cast<double>(nframes)
            else:
                fps = 60.0
                nframes = static_cast<unsigned int>(ceil(duration/fps))
        else # duration == 0.0
            if fps==0.0 : fps=60.0
            if nframes==0 : nframes=1

            duration = static_cast<double>(nframes)/fps

        fc.setNumberOfFrames(nframes)
        fc.setFrameRate(fps)
        OSG_NOTICE, "Duration=", duration, ", FPS=", fps, ", Number of Frames=", nframes
    



    if arguments.read("--output-cs",filename) :
        osgDB.writeObjectFile(*fc, filename)
        return 1

    

    if fc.valid() :
        frameCaptureList.push_back(fc)

    if frameCaptureList.empty() :
        OSG_NOTICE, "No settings provided"
        return 1


    # setup viewer
        ds = osg.DisplaySettings()

        stereo = fc.getStereoMode() not =gsc.CaptureSettings.OFF
        stereoMode =  osg.DisplaySettings.VERTICAL_SPLIT : osg.DisplaySettings: if (fc.getStereoMode()==gsc.CaptureSettings.VERTICAL_SPLIT) else HORIZONTAL_SPLIT
        fovx_multiple =  2.0 if (fc.getStereoMode()==gsc.CaptureSettings.HORIZONTAL_SPLIT) else  1
        fovy_multiple =  2.0 if (fc.getStereoMode()==gsc.CaptureSettings.VERTICAL_SPLIT) else  1
        ds.setStereoMode(stereoMode)
        ds.setStereo(stereo)

        if fc.getScreenWidth() not =0.0 : ds.setScreenWidth(fc.getScreenWidth())
        if fc.getScreenHeight() not =0.0 : ds.setScreenHeight(fc.getScreenHeight())
        if fc.getScreenDistance() not =0.0 : ds.setScreenDistance(fc.getScreenDistance())

        
        traits = osg.GraphicsContext.Traits(ds)

        traits.readDISPLAY()
        if traits.displayNum<0 : traits.displayNum = 0

        traits.x = 0
        traits.y = 0
        traits.width = fc.getWidth()
        traits.height = fc.getHeight()
        traits.alpha =  8 if ((fc.getPixelFormat() == gsc.CaptureSettings.RGBA)) else  0
        traits.samples = fc.getSamples()
        traits.sampleBuffers = fc.getSampleBuffers()
        traits.windowDecoration =  not (fc.getOffscreen())
        traits.doubleBuffer = True
        traits.sharedContext = 0
        traits.pbuffer = fc.getOffscreen()

        gc = osg.GraphicsContext.createGraphicsContext(traits)
        if  not gc :
            OSG_NOTICE, "Failed to created requested graphics context"
            return 1

        viewer.getCamera().setClearColor(clearColor)
        viewer.getCamera().setGraphicsContext(gc)
        viewer.getCamera().setDisplaySettings(ds)

        gw = dynamic_cast<osgViewer.GraphicsWindow*>(gc)
        if gw :
            OSG_INFO, "GraphicsWindow has been created successfully."
            gw.getEventQueue().getCurrentEventState().setWindowRectangle(0, 0, fc.getWidth(),  fc.getHeight())
        else:
            OSG_NOTICE, "PixelBuffer has been created succseffully ", traits.width, ", ", traits.height

        if useScreenSizeForProjectionMatrix :
            OSG_NOTICE, "Setting projection matrix"
            
            vfov = osg.RadiansToDegrees(atan2(screenHeight/2.0,screenDistance)*2.0)
            # double hfov = osg.RadiansToDegrees(atan2(width/2.0,distance)*2.0)

            viewer.getCamera().setProjectionMatrixAsPerspective( vfov*fovy_multiple, (screenWidth/screenHeight)*fovx_multiple, 0.1, 1000.0)

            OSG_NOTICE, "setProjectionMatrixAsPerspective( ", vfov*fovy_multiple, ", ", (screenWidth/screenHeight)*fovx_multiple, ", ", 0.1, ", ", 1000.0, ")"

            
        else:
            double fovy, aspectRatio, zNear, zFar
            viewer.getCamera().getProjectionMatrixAsPerspective(fovy, aspectRatio, zNear, zFar)

            newAspectRatio = double(traits.width) / double(traits.height)
            aspectRatioChange = newAspectRatio / aspectRatio
            if aspectRatioChange  not = 1.0 :
                viewer.getCamera().getProjectionMatrix() *= osg.Matrix.scale(fovx_multiple/aspectRatioChange,fovy_multiple,1.0)

        # set up stereo masks
        viewer.getCamera().setCullMask(0xffffffff)
        viewer.getCamera().setCullMaskLeft(0x00000001)
        viewer.getCamera().setCullMaskRight(0x00000002)

        viewer.getCamera().setViewport(osg.Viewport(0, 0, traits.width, traits.height))

        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT

        viewer.getCamera().setDrawBuffer(buffer)
        viewer.getCamera().setReadBuffer(buffer)

    outputPath = osgDB.getFilePath(fc.getOutputFileName())
    if  not outputPath.empty() :
        type = osgDB.fileType(outputPath)
        switch(type)
            case(osgDB.FILE_NOT_FOUND):
                if  not osgDB.makeDirectory(outputPath) :
                    OSG_NOTICE, "Error: could not create directory [", outputPath, "]."                    
                    return 1
                OSG_NOTICE, "Created directory [", outputPath, "]."
                break
            case(osgDB.REGULAR_FILE):
                OSG_NOTICE, "Error: filepath for output files is regular file, not a directory as required."
                return 1
            case(osgDB.DIRECTORY):
                OSG_NOTICE, "Valid path[", outputPath, "] provided for output files."
                break

    pixelFormat =  GL_RGBA if ((fc.getPixelFormat()==gsc.CaptureSettings.RGBA)) else  GL_RGB
    

    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)
    viewer.realize()

    # set up screen shot
    screenShot = ScreenShot(pixelFormat, fc.getOutputImageFlip())

        cameras = osgViewer.Viewer.Cameras()
        viewer.getCameras(cameras)
        if cameras.size()>1 :
            cameraNum = 0
            for(osgViewer.Viewer.Cameras.iterator itr = cameras.begin()
                not = cameras.end()
                ++itr, ++cameraNum)
                camera = *itr
                camera.setFinalDrawCallback(screenShot)
                screenShot._cameraNumMap[camera] = cameraNum
        elif cameras.size()==1 :
            camera = cameras.front()
            camera.setFinalDrawCallback(screenShot)
        else:
            OSG_NOTICE, "No usable Cameras created."
            return 1

    for(CaptureSettingsList.iterator itr = frameCaptureList.begin()
        not = frameCaptureList.end()
        ++itr)
        fc = itr
        screenShot._frameCapture = fc

        model = osgDB.readNodeFile(fc.getInputFileName())
        if  not model : break

        viewer.setSceneData(model)

        simulationTime = 0.0
                
        for(unsigned int i=0 i<fc.getNumberOfFrames() ++i)
            OSG_NOTICE, "fc.getOutputFileName(", i, ")=", fc.getOutputFileName(i)

            viewer.advance(simulationTime)
            
            pl = fc.getProperties()
            for(gsc.CaptureSettings.Properties.iterator plitr = pl.begin()
                not = pl.end()
                ++plitr)
                (*plitr).update(viewer)

            viewer.eventTraversal()
            viewer.updateTraversal()
            viewer.renderingTraversals()

            # advance simulationTime and number of frames rendered
            simulationTime += 1.0/fc.getFrameRate()

    object = osgGA.StateSetManipulator()
    ss = dynamic_cast<osgGA.StateSetManipulator*>(object)
   
    return 0

# Translated from file 'UpdateProperty.cpp'

#include "UpdateProperty.h"

using namespace gsc


# Translated from file 'UpdateProperty.h'

#ifndef UPDATEPROPERTY_H
#define UPDATEPROPERTY_H

#include <osgDB/ReadFile>
#include <osgDB/FileNameUtils>
#include <osgDB/WriteFile>
#include <osgViewer/Viewer>
#include <osg/AnimationPath>

namespace gsc

class UpdateProperty (osg.Object) :

    UpdateProperty() 
    UpdateProperty( UpdateProperty up,  osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY) 

    META_Object(gsc, UpdateProperty)

    def update(view):


    virtual ~UpdateProperty() 




#endif

if __name__ == "__main__":
    main(sys.argv)
