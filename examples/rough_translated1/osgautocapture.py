#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgautocapture"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgTerrain
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgautocapture.cpp'

#*
# * TODO:
# * 1) Change example to use offscreen rendering (pbuffer) so that it becomes a True commandline tool with now windows
# * 2) Make example work with other threading models than SingleThreaded
# * 3) Add support for autocapture to movies
# *
# 
#include <osg/ArgumentParser>
#include <osg/CoordinateSystemNode>
#include <osg/Matrix>
#include <osg/NodeVisitor>

#include <osgUtil/IntersectionVisitor>
#include <osgUtil/GLObjectsVisitor>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osgGA/DriveManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/TerrainManipulator>
#include <osgGA/TrackballManipulator>

#include <osgTerrain/Terrain>
#include <osgTerrain/GeometryTechnique>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgViewer/Renderer>
    
#include <iostream>
#include <sstream>

#* Helper class
template<class T>
class FindTopMostNodeOfTypeVisitor (osg.NodeVisitor) :
    FindTopMostNodeOfTypeVisitor():
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _foundNode(0)
    
    
    def apply(node):
    
        
        result = dynamic_cast<T*>(node)
        if result :
             _foundNode = result
         traverse = else :(node)
    
    _foundNode = T*()


#* Convenience function
template<class T>
def findTopMostNodeOfType(node):
    
    if !node : return 0

    fnotv = FindTopMostNodeOfTypeVisitor<T>()
    node.accept(fnotv)
    
    return fnotv._foundNode

#* Capture the frame buffer and write image to disk
class WindowCaptureCallback (osg.Camera.DrawCallback) :    
    WindowCaptureCallback(GLenum readBuffer,  str name):
        _readBuffer(readBuffer),
        _fileName(name)
            _image = osg.Image()
    
    virtual void operator () (osg.RenderInfo renderInfo) 
            #if !defined(OSG_GLES1_AVAILABLE)  !defined(OSG_GLES2_AVAILABLE)
            glReadBuffer(_readBuffer)
            #else :
            osg.notify(osg.NOTICE), "Error: GLES unable to do glReadBuffer"
            #endif

            lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)
            gc = renderInfo.getState().getGraphicsContext()
            if gc.getTraits() :
                pixelFormat = GLenum()

                if gc.getTraits().alpha :
                    pixelFormat = GL_RGBA
                pixelFormat = GL_RGB
                
#if defined(OSG_GLES1_AVAILABLE) || defined(OSG_GLES2_AVAILABLE)
                 if pixelFormat == GL_RGB :
                    value = 0
                    #ifndef GL_IMPLEMENTATION_COLOR_READ_FORMAT
                        #define GL_IMPLEMENTATION_COLOR_READ_FORMAT 0x8B9B
                    #endif
                    glGetIntegerv(GL_IMPLEMENTATION_COLOR_READ_FORMAT, value)
                    if  value != GL_RGB ||
                         value != GL_UNSIGNED_BYTE  :
                        pixelFormat = GL_RGBA#always supported
#endif
                width = gc.getTraits().width
                height = gc.getTraits().height

                print "Capture: size=", width, "x", height, ", format=", (pixelFormat == GL_RGBA ? "GL_RGBA":"GL_RGB")

                _image.readPixels(0, 0, width, height, pixelFormat, GL_UNSIGNED_BYTE)
                
            if !_fileName.empty() :
                print "Writing to: ", _fileName
                osgDB.writeImageFile(*_image, _fileName)
    _readBuffer = GLenum()
    _fileName = str()
    _image = osg.Image()
    mutable OpenThreads.Mutex  _mutex



#* Do Culling only while loading PagedLODs
class CustomRenderer (osgViewer.Renderer) :
    CustomRenderer(osg.Camera* camera) 
        : osgViewer.Renderer(camera),
          _cullOnly(True)

    #* Set flag to omit drawing in renderingTraversals 
    def setCullOnly(on):
         _cullOnly = on 

    virtual void operator () (osg.GraphicsContext* #context)
            if _graphicsThreadDoesCull :
                if _cullOnly :
                    cull()
                cull_draw = else :()

    def cull():

        
            sceneView = _sceneView[0].get()
            if !sceneView || _done  : return
            
            updateSceneView(sceneView)
            
            view = dynamic_cast<osgViewer.View*>(_camera.getView())
            if view : sceneView.setFusionDistance(view.getFusionDistanceMode(), view.getFusionDistanceValue())

            sceneView.inheritCullSettings(*(sceneView.getCamera()))
            sceneView.cull()
    
    _cullOnly = bool()

    

#===============================================================
# MAIN
#
def main(argc, argv):
    
    arguments = osg.ArgumentParser(argc, argv)
    usage = arguments.getApplicationUsage()

    usage.setApplicationName(arguments.getApplicationName())
    usage.setDescription(arguments.getApplicationName()+" loads a model, sets a camera position and automatically captures screenshot to disk")
    usage.setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    usage.addCommandLineOption("--camera <lat> <lon> <alt> <heading> <incline> <roll>", "Specify camera position for image capture. Angles are specified in degrees and altitude in meters above sealevel (e.g. --camera 55 10 300000 0 30 0)")
    usage.addCommandLineOption("--filename", "Filename for the captured image", "autocapture.jpg")
    usage.addCommandLineOption("--db-threads", "Number of DatabasePager threads to use", "2")
    usage.addCommandLineOption("--active", "Use active rendering instead of passive / lazy rendering")
    usage.addCommandLineOption("--pbuffer", "Render into a pbuffer, not into a window")

    # Construct the viewer and register options arguments.
    viewer = osgViewer.Viewer(arguments)

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

   # Get user specified number of DatabaseThreads
    dbThreads = 2
    arguments.read("--db-threads", dbThreads)
    if dbThreads < 1 : dbThreads = 1

    osg.DisplaySettings.instance().setNumOfDatabaseThreadsHint(dbThreads)

    # Get user specified file name
    fileName = str("autocapture.jpg")
    arguments.read("--filename", fileName)

    # Rendering mode is passive by default
    activeMode = False
    if arguments.read("--active") :
        activeMode = True

    use_pbuffer = False
    if arguments.read("--pbuffer") : 
        if !activeMode : 
            use_pbuffer = True
         else : 
            osg.notify(osg.NOTICE), "ignoring --pbuffer because --active specified on commandline"
    if use_pbuffer : 
        ds = osg.DisplaySettings.instance().get()
        traits = osg.GraphicsContext.Traits(ds)

        if viewer.getCamera().getGraphicsContext()  viewer.getCamera().getGraphicsContext().getTraits() : 
            #use viewer settings for window size
            src_traits = viewer.getCamera().getGraphicsContext().getTraits()
            traits.screenNum = src_traits.screenNum
            traits.displayNum = src_traits.displayNum
            traits.hostName = src_traits.hostName
            traits.width = src_traits.width
            traits.height = src_traits.height
            traits.red = src_traits.red
            traits.green = src_traits.green
            traits.blue = src_traits.blue
            traits.alpha = src_traits.alpha
            traits.depth = src_traits.depth
            traits.pbuffer = True
         else : 
            #viewer would use fullscreen size (unknown here) pbuffer will use 4096 x4096 (or best avaiable)
            traits.width = 1, 12
            traits.height = 1, 12
            traits.pbuffer = True
        pbuffer = osg.GraphicsContext.createGraphicsContext(traits.get())
        if pbuffer.valid() :
            osg.notify(osg.NOTICE), "Pixel buffer has been created successfully."
            camera = osg.Camera(*viewer.getCamera())
            camera.setGraphicsContext(pbuffer.get())
            camera.setViewport(osg.Viewport(0,0,traits.width,traits.height))
            buffer = pbuffer.getTraits().doubleBuffer ? GL_BACK : GL_FRONT
            camera.setDrawBuffer(buffer)
            camera.setReadBuffer(buffer)
            viewer.setCamera(camera.get())
        else :
            osg.notify(osg.NOTICE), "Pixel buffer has not been created successfully."

    # Read camera settings for screenshot
    lat = 50
    lon = 10
    alt = 2000
    heading = 0
    incline = 45
    roll = 0
    camera_specified = False
    if arguments.read("--camera", lat, lon, alt, heading, incline, roll) :
        camera_specified=True
        lat = osg.DegreesToRadians(lat)
        lon = osg.DegreesToRadians(lon)
        heading = osg.DegreesToRadians(heading)
        incline = osg.DegreesToRadians(incline)
        roll = osg.DegreesToRadians(roll)

    # load the data
    loadedModel = osgDB.readNodeFiles(arguments)
    if !loadedModel : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1

     # any option left unread are converted into errors to write out later.
     arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    # Setup specified camera
    if camera_specified :
        csn = findTopMostNodeOfType<osg.CoordinateSystemNode>(loadedModel.get())
        if !csn : return 1
        
        # Compute eye point in world coordiantes
        eye = osg.Vec3d()
        csn.getEllipsoidModel().convertLatLongHeightToXYZ(lat, lon, alt, eye.x(), eye.y(), eye.z())

        # Build matrix for computing target vector
        target_matrix = osg.Matrixd.rotate(-heading, osg.Vec3d(1,0,0),
                                                          -lat,     osg.Vec3d(0,1,0),
                                                          lon,      osg.Vec3d(0,0,1))

        # Compute tangent vector ...
        tangent = target_matrix.preMult(osg.Vec3d(0, 0, 1))

        # Compute non-inclined, non-rolled up vector ...
        up = osg.Vec3d(eye)
        up.normalize()

        # Incline by rotating the target- and up vector around the tangent/up-vector
        # cross-product ...
        up_cross_tangent = up ^ tangent
        incline_matrix = osg.Matrixd.rotate(incline, up_cross_tangent)
        target = incline_matrix.preMult(tangent)
        
        # Roll by rotating the up vector around the target vector ...
        roll_matrix = incline_matrix * osg.Matrixd.rotate(roll, target)
        up = roll_matrix.preMult(up)
        
        viewer.getCamera().setViewMatrixAsLookAt(eye, eye+target, up)
    else :
        # Only add camera manipulators if camera is not specified
        camera_specified=False
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( '1', "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( '2', "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( '3', "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( '4', "Terrain", osgGA.TerrainManipulator() )

        viewer.setCameraManipulator( keyswitchManipulator.get() ) 

            
    # Optimize DatabasePager for auto-capture
    pager = viewer.getDatabasePager()
    pager.setDoPreCompile(False)

    # Install custom renderer
    customRenderer = CustomRenderer(viewer.getCamera())
    viewer.getCamera().setRenderer(customRenderer.get())

    # Override threading model
    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # Set the final SceneData to show
    viewer.setSceneData(loadedModel.get())

    # Realize GUI
    viewer.realize()

    #--- Load PageLOD tiles ---

    # Initiate the first PagedLOD request
    viewer.frame()
        
    beforeLoadTick = osg.Timer.instance().tick()
    
    # Keep updating and culling until full level of detail is reached
    while !viewer.done()  pager.getRequestsInProgress() :
#        print pager.getRequestsInProgress(), " "
        viewer.updateTraversal()
        viewer.renderingTraversals()
#    print std.endl
        
    afterLoadTick = osg.Timer.instance().tick()
    print "Load and Compile time = ", osg.Timer.instance().delta_s(beforeLoadTick, afterLoadTick), " seconds"

    # Do cull and draw to render the scene correctly
    customRenderer.setCullOnly(False)
    
  
    #--- Capture the image!!! ---
    if !activeMode :
        # Add the WindowCaptureCallback now that we have full resolution
        buffer = viewer.getCamera().getGraphicsContext().getTraits().doubleBuffer ? GL_BACK : GL_FRONT
        viewer.getCamera().setFinalDrawCallback(WindowCaptureCallback(buffer, fileName))

        beforeRenderTick = osg.Timer.instance().tick()

        # Do rendering with capture callback
         viewer.renderingTraversals()

        afterRenderTick = osg.Timer.instance().tick()
        print "Rendring time = ", osg.Timer.instance().delta_s(beforeRenderTick, afterRenderTick), " seconds"

        return 0
    else :
        return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
