#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgposter"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgposter.cpp'

# -*-c++-*- OpenSceneGraph example, osgposter.
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

#include <osg/ArgumentParser>
#include <osg/Texture2D>
#include <osg/Switch>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgViewer/Renderer>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <iostream>
#include "PosterPrinter.h"

# Computing view matrix helpers 
template<class T>
class FindTopMostNodeOfTypeVisitor (osg.NodeVisitor) :
    FindTopMostNodeOfTypeVisitor()
    :   osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _foundNode(0)
    
    
    def apply(node):
    
        
        result = dynamic_cast<T*>( node )
        if  result  : _foundNode = result
        traverse = else( node )
    
    _foundNode = T*()


template<class T>
def findTopMostNodeOfType(node):
    
    if   not node  : return 0
    
    fnotv = FindTopMostNodeOfTypeVisitor<T>()
    node.accept( fnotv )
    return fnotv._foundNode

# Computing view matrix functions 
def computeViewMatrix(camera, eye, hpr):
    
    matrix = osg.Matrixd()
    matrix.makeTranslate( eye )
    matrix.preMult( osg.Matrixd.rotate( hpr[0], 0.0, 1.0, 0.0) )
    matrix.preMult( osg.Matrixd.rotate( hpr[1], 1.0, 0.0, 0.0) )
    matrix.preMult( osg.Matrixd.rotate( hpr[2], 0.0, 0.0, 1.0) )
    camera.setViewMatrix( osg.Matrixd.inverse(matrix) )

def computeViewMatrixOnEarth(camera, scene, latLongHeight, hpr):

    
    csn = findTopMostNodeOfType<osg.CoordinateSystemNode>(scene)
    if   not csn  : return
    
    # Compute eye point in world coordiantes
    eye = osg.Vec3d()
    csn.getEllipsoidModel().convertLatLongHeightToXYZ(
        latLongHeight.x(), latLongHeight.y(), latLongHeight.z(), eye.x(), eye.y(), eye.z() )
    
    # Build matrix for computing target vector
    target_matrix = osg.Matrixd.rotate( -hpr.x(), osg.Vec3d(1,0,0),
                              -latLongHeight.x(), osg.Vec3d(0,1,0),
                               latLongHeight.y(), osg.Vec3d(0,0,1) )
    
    # Compute tangent vector
    tangent = target_matrix.preMult( osg.Vec3d(0,0,1) )
    
    # Compute non-inclined, non-rolled up vector
    up = osg.Vec3d( eye )
    up.normalize()
    
    # Incline by rotating the target- and up vector around the tangent/up-vector
    # cross-product
    up_cross_tangent = up ^ tangent
    incline_matrix = osg.Matrixd.rotate( hpr.y(), up_cross_tangent )
    target = incline_matrix.preMult( tangent )
    
    # Roll by rotating the up vector around the target vector
    roll_matrix = incline_matrix * osg.Matrixd.rotate( hpr.z(), target )
    up = roll_matrix.preMult( up )
    camera.setViewMatrixAsLookAt( eye, eye+target, up )

# CustomRenderer: Do culling only while loading PagedLODs 
class CustomRenderer (osgViewer.Renderer) :
    CustomRenderer( osg.Camera* camera )
    : osgViewer.Renderer(camera), _cullOnly(True)
    
    def setCullOnly(on):
    
         _cullOnly = on 

    virtual void operator ()( osg.GraphicsContext* )
        if  _graphicsThreadDoesCull  :
            if _cullOnly : cull()
            cull_draw = else()
    
    def cull():
    
        
        sceneView = _sceneView[0]
        if   not sceneView  or  _done  or  _graphicsThreadDoesCull  :
            return
        
        updateSceneView( sceneView )
        
        view = dynamic_cast<osgViewer.View*>( _camera.getView() )
        if  view  :
            sceneView.setFusionDistance( view.getFusionDistanceMode(), view.getFusionDistanceValue() )
        sceneView.inheritCullSettings( *(sceneView.getCamera()) )
        sceneView.cull()
    
    _cullOnly = bool()


# PrintPosterHandler: A gui handler for interactive high-res capturing 
class PrintPosterHandler (osgGA.GUIEventHandler) :
    PrintPosterHandler( PosterPrinter* printer )
    : _printer(printer), _started(False) 
    
    def handle(ea, aa):
    
        
        view = dynamic_cast<osgViewer.View*>( aa )
        if   not view  : return False
        
        switch( ea.getEventType() )
        case osgGA.GUIEventAdapter.FRAME:
            if  view.getDatabasePager()  :
                # Wait until all paged nodes are processed
                if  view.getDatabasePager().getRequestsInProgress()  :
                    break
            
            if  _printer.valid()  :
                _printer.frame( view.getFrameStamp(), view.getSceneData() )
                if  _started  and  _printer.done()  :
                    root = dynamic_cast<osg.Switch*>( view.getSceneData() )
                    if  root  :
                        # Assume child 0 is the loaded model and 1 is the poster camera
                        # Switch them in time to prevent dual traversals of subgraph
                        root.setValue( 0, True )
                        root.setValue( 1, False )
                    _started = False
            break
        
        case osgGA.GUIEventAdapter.KEYDOWN:
            if  ea.getKey()==ord("p")  or  ea.getKey()==ord("P")  :
                if  _printer.valid()  :
                    root = dynamic_cast<osg.Switch*>( view.getSceneData() )
                    if  root  :
                        # Assume child 0 is the loaded model and 1 is the poster camera
                        root.setValue( 0, False )
                        root.setValue( 1, True )
                    
                    _printer.init( view.getCamera() )
                    _started = True
                return True
            break
        
        default:
            break
        return False
    _printer = PosterPrinter()
    _started = bool()


# The main entry 
def main(argv):
    
    arguments = osg.ArgumentParser( argc, argv )
    usage = arguments.getApplicationUsage()
    usage.setDescription( arguments.getApplicationName() +
                           " is the example which demonstrates how to render high-resolution images (posters).")
    usage.setCommandLineUsage( arguments.getApplicationName() + " [options] scene_file" )
    usage.addCommandLineOption( "-h or --help", "Display this information." )
    usage.addCommandLineOption( "--color <r> <g> <b>", "The background color." )
    usage.addCommandLineOption( "--ext <ext>", "The output tiles' extension (Default: bmp)." )
    usage.addCommandLineOption( "--poster <filename>", "The output poster's name (Default: poster.bmp)." )
    usage.addCommandLineOption( "--tilesize <w> <h>", "Size of each image tile (Default: 640 480)." )
    usage.addCommandLineOption( "--finalsize <w> <h>", "Size of the poster (Default: 6400 4800)." )
    usage.addCommandLineOption( "--enable-output-poster", "Output the final poster file (Default)." )
    usage.addCommandLineOption( "--disable-output-poster", "Don't output the final poster file." )
    #usage.addCommandLineOption( "--enable-output-tiles", "Output all tile files." )
    #usage.addCommandLineOption( "--disable-output-tiles", "Don't output all tile files (Default)." )
    usage.addCommandLineOption( "--use-fb", "Use Frame Buffer for rendering tiles (Default, recommended).")
    usage.addCommandLineOption( "--use-fbo", "Use Frame Buffer Object for rendering tiles.")
    usage.addCommandLineOption( "--use-pbuffer","Use Pixel Buffer for rendering tiles.")
    usage.addCommandLineOption( "--use-pbuffer-rtt","Use Pixel Buffer RTT for rendering tiles.")
    usage.addCommandLineOption( "--inactive", "Inactive capturing mode." )
    usage.addCommandLineOption( "--camera-eye <x> <y> <z>", "Set eye position in inactive mode." )
    usage.addCommandLineOption( "--camera-latlongheight <lat> <lon> <h>", "Set eye position on earth in inactive mode." )
    usage.addCommandLineOption( "--camera-hpr <h> <p> <r>", "Set eye rotation in inactive mode." )
    
    if  arguments.read("-h")  or  arguments.read("--help")  :
        usage.write( std.cout )
        return 1
    
    # Poster arguments
    activeMode = True
    outputPoster = True
    #bool outputTiles = False
    tileWidth = 640, tileHeight = 480
    posterWidth = 640*2, posterHeight = 480*2
    posterName = "poster.bmp", extName = "bmp"
    bgColor = osg.Vec4(0.2, 0.2, 0.6, 1.0)
    renderImplementation = osg.Camera.FRAME_BUFFER_OBJECT
    
    while  arguments.read("--inactive")  :  activeMode = False 
    while  arguments.read("--color", bgColor.r(), bgColor.g(), bgColor.b())  : 
    while  arguments.read("--tilesize", tileWidth, tileHeight)  : 
    while  arguments.read("--finalsize", posterWidth, posterHeight)  : 
    while  arguments.read("--poster", posterName)  : 
    while  arguments.read("--ext", extName)  : 
    while  arguments.read("--enable-output-poster")  :  outputPoster = True 
    while  arguments.read("--disable-output-poster")  :  outputPoster = False 
    #while  arguments.read("--enable-output-tiles")  :  outputTiles = True 
    #while  arguments.read("--disable-output-tiles")  :  outputTiles = False 
    while  arguments.read("--use-fbo") :  renderImplementation = osg.Camera.FRAME_BUFFER_OBJECT 
    while  arguments.read("--use-pbuffer") :  renderImplementation = osg.Camera.PIXEL_BUFFER 
    while  arguments.read("--use-pbuffer-rtt") :  renderImplementation = osg.Camera.PIXEL_BUFFER_RTT 
    while  arguments.read("--use-fb") :  renderImplementation = osg.Camera.FRAME_BUFFER 
    
    # Camera settings for inactive screenshot
    useLatLongHeight = True
    eye = osg.Vec3d()
    latLongHeight = osg.Vec3d( 50.0, 10.0, 2000.0 )
    hpr = osg.Vec3d( 0.0, 0.0, 0.0 )
    if  arguments.read("--camera-eye", eye.x(), eye.y(), eye.z())  :
        useLatLongHeight = False
        activeMode = False
    elif  arguments.read("--camera-latlongheight", latLongHeight.x(), latLongHeight.y(), latLongHeight.z())  :
        activeMode = False
        latLongHeight.x() = osg.DegreesToRadians( latLongHeight.x() )
        latLongHeight.y() = osg.DegreesToRadians( latLongHeight.y() )
    if  arguments.read("--camera-hpr", hpr.x(), hpr.y(), hpr.z())  :
        activeMode = False
        hpr.x() = osg.DegreesToRadians( hpr.x() )
        hpr.y() = osg.DegreesToRadians( hpr.y() )
        hpr.z() = osg.DegreesToRadians( hpr.z() )
    
    # Construct scene graph
    scene = osgDB.readNodeFiles( arguments )
    if   not scene  : scene = osgDB.readNodeFile( "cow.osgt" )
    if   not scene  :
        print arguments.getApplicationName(), ": No data loaded"
        return 1
    
    # Create camera for rendering tiles offscreen. FrameBuffer is recommended because it requires less memory.
    camera = osg.Camera()
    camera.setClearColor( bgColor )
    camera.setClearMask( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    camera.setReferenceFrame( osg.Transform.ABSOLUTE_RF )
    camera.setRenderOrder( osg.Camera.PRE_RENDER )
    camera.setRenderTargetImplementation( renderImplementation )
    camera.setViewport( 0, 0, tileWidth, tileHeight )
    camera.addChild( scene )
    
    # Set the printer
    printer = PosterPrinter()
    printer.setTileSize( tileWidth, tileHeight )
    printer.setPosterSize( posterWidth, posterHeight )
    printer.setCamera( camera )
    
    posterImage = 0
    if  outputPoster  :
        posterImage = osg.Image()
        posterImage.allocateImage( posterWidth, posterHeight, 1, GL_RGBA, GL_UNSIGNED_BYTE )
        printer.setFinalPoster( posterImage )
        printer.setOutputPosterName( posterName )
    
#if 0
    # While recording sub-images of the poster, the scene will always be traversed twice, from its two
    # parent node: root and camera. Sometimes this may not be so comfortable.
    # To prevent this behaviour, we can use a switch node to enable one parent and disable the other.
    # However, the solution also needs to be used with care, as the window will go blank while taking
    # snapshots and recover later.
    root = osg.Switch()
    root.addChild( scene, True )
    root.addChild( camera, False )
#else:
    root = osg.Group()
    root.addChild( scene )
    root.addChild( camera )
#endif
    
    viewer = osgViewer.Viewer()
    viewer.setSceneData( root )
    viewer.getDatabasePager().setDoPreCompile( False )
    
    if  renderImplementation==osg.Camera.FRAME_BUFFER  :
        # FRAME_BUFFER requires the window resolution equal or greater than the to-be-copied size
        viewer.setUpViewInWindow( 100, 100, tileWidth, tileHeight )
    else:
        # We want to see the console output, so just render in a window
        viewer.setUpViewInWindow( 100, 100, 800, 600 )
    
    if  activeMode  :
        viewer.addEventHandler( PrintPosterHandler(printer) )
        viewer.addEventHandler( osgViewer.StatsHandler )()
        viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
        viewer.setCameraManipulator( osgGA.TrackballManipulator )()
        viewer.run()
    else:
        camera = viewer.getCamera()
        if   not useLatLongHeight  : computeViewMatrix( camera, eye, hpr )
        computeViewMatrixOnEarth = else( camera, scene, latLongHeight, hpr )
        
        renderer = CustomRenderer( camera )
        camera.setRenderer( renderer )
        viewer.setThreadingModel( osgViewer.Viewer.SingleThreaded )
        
        # Realize and initiate the first PagedLOD request
        viewer.realize()
        viewer.frame()
        
        printer.init( camera )
        while   not printer.done()  :
            viewer.advance()
            
            # Keep updating and culling until full level of detail is reached
            renderer.setCullOnly( True )
            while  viewer.getDatabasePager().getRequestsInProgress()  :
                viewer.updateTraversal()
                viewer.renderingTraversals()
            
            renderer.setCullOnly( False )
            printer.frame( viewer.getFrameStamp(), viewer.getSceneData() )
            viewer.renderingTraversals()
    return 0

# Translated from file 'PosterPrinter.cpp'

#include <osg/ClusterCullingCallback>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <string.h>
#include <iostream>
#include <sstream>
#include "PosterPrinter.h"

# PagedLoadingCallback: Callback for loading paged nodes while doing intersecting test 
class PagedLoadingCallback (osgUtil.IntersectionVisitor.ReadCallback) :
def readNodeFile(filename):
    
        return osgDB.readNodeFile( filename )

static PagedLoadingCallback g_pagedLoadingCallback = PagedLoadingCallback()

# LodCullingCallback: Callback for culling LODs and selecting the highest level 
class LodCullingCallback (osg.NodeCallback) :
    virtual void operator()( osg.Node* node, osg.NodeVisitor* nv )
        lod = static_cast<osg.LOD*>(node)
        if  lod  and  lod.getNumChildren()>0  :
            lod.getChild(lod.getNumChildren()-1).accept(*nv)

static LodCullingCallback g_lodCullingCallback = LodCullingCallback()

# PagedCullingCallback: Callback for culling paged nodes and selecting the highest level 
class PagedCullingCallback (osg.NodeCallback) :
    virtual void operator()( osg.Node* node, osg.NodeVisitor* nv )
        pagedLOD = static_cast<osg.PagedLOD*>(node)
        if  pagedLOD  and  pagedLOD.getNumChildren()>0  :
            numChildren = pagedLOD.getNumChildren()
            updateTimeStamp = nv.getVisitorType()==osg.NodeVisitor.CULL_VISITOR
            if  nv.getFrameStamp()  and  updateTimeStamp  :
                timeStamp =  nv.getFrameStamp().getReferenceTime() if (nv.getFrameStamp()) else 0.0
                frameNumber =  nv.getFrameStamp().getFrameNumber() if (nv.getFrameStamp()) else 0
                
                pagedLOD.setFrameNumberOfLastTraversal( frameNumber )
                pagedLOD.setTimeStamp( numChildren-1, timeStamp )
                pagedLOD.setFrameNumber( numChildren-1, frameNumber )
                pagedLOD.getChild(numChildren-1).accept(*nv)
            
            # Request for child
            if   not pagedLOD.getDisableExternalChildrenPaging()  and 
                 nv.getDatabaseRequestHandler()  and 
                 numChildren<pagedLOD.getNumRanges()  :
                if  pagedLOD.getDatabasePath().empty()  :
                    nv.getDatabaseRequestHandler().requestNodeFile(
                        pagedLOD.getFileName(numChildren), nv.getNodePath(),
                        1.0, nv.getFrameStamp(),
                        pagedLOD.getDatabaseRequest(numChildren), pagedLOD.getDatabaseOptions() )
                else:
                    nv.getDatabaseRequestHandler().requestNodeFile(
                        pagedLOD.getDatabasePath()+pagedLOD.getFileName(numChildren), nv.getNodePath(),
                        1.0, nv.getFrameStamp(),
                        pagedLOD.getDatabaseRequest(numChildren), pagedLOD.getDatabaseOptions() )
        #node.traverse(*nv)

static PagedCullingCallback g_pagedCullingCallback = PagedCullingCallback()

# PosterVisitor: A visitor for adding culling callbacks to newly allocated paged nodes 
PosterVisitor.PosterVisitor()
:   osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
    _appliedCount(0), _needToApplyCount(0),
    _addingCallbacks(True)

void PosterVisitor.apply( osg.LOD node )
    #if   not hasCullCallback(node.getCullCallback(), g_lodCullingCallback)  :
#    
#        if   not node.getName().empty()  :
#        
#            itr = _pagedNodeNames.find( node.getName() )
#            if  itr not =_pagedNodeNames.end()  :
#            
#                insertCullCallback( node, g_lodCullingCallback )
#                _appliedCount++
#            
#        
#    
#    def if _addingCallbacks .
#        
#        node.removeCullCallback( g_lodCullingCallback )
#        _appliedCount--
#    
    traverse( node )

void PosterVisitor.apply( osg.PagedLOD node )
    if   not hasCullCallback(node.getCullCallback(), g_pagedCullingCallback)  :
        for ( unsigned int i=0 i<node.getNumFileNames() ++i )
            if  node.getFileName(i).empty()  : continue
            
            itr = _pagedNodeNames.find( node.getFileName(i) )
            if  itr not =_pagedNodeNames.end()  :
                node.addCullCallback( g_pagedCullingCallback )
                _appliedCount++
            break
    def if _addingCallbacks .
        
        node.removeCullCallback( g_pagedCullingCallback )
        if  _appliedCount>0  : _appliedCount--
    traverse( node )

# PosterIntersector: A simple polytope intersector for updating pagedLODs in each image-tile 
PosterIntersector.PosterIntersector(  osg.Polytope polytope )
:   _intersectionVisitor(0), _parent(0), _polytope(polytope)


PosterIntersector.PosterIntersector( double xMin, double yMin, double xMax, double yMax )
:   Intersector(osgUtil.Intersector.PROJECTION),
    _intersectionVisitor(0), _parent(0)
    _polytope.add( osg.Plane( 1.0, 0.0, 0.0,-xMin) )
    _polytope.add( osg.Plane(-1.0, 0.0, 0.0, xMax) )
    _polytope.add( osg.Plane( 0.0, 1.0, 0.0,-yMin) )
    _polytope.add( osg.Plane( 0.0,-1.0, 0.0, yMax) )

osgUtil.Intersector* PosterIntersector.clone( osgUtil.IntersectionVisitor iv )
    matrix = osg.Matrix()
    if  iv.getProjectionMatrix()  : matrix.preMult( *iv.getProjectionMatrix() )
    if  iv.getViewMatrix()  : matrix.preMult( *iv.getViewMatrix() )
    if  iv.getModelMatrix()  : matrix.preMult( *iv.getModelMatrix() )
    
    transformedPolytope = osg.Polytope()
    transformedPolytope.setAndTransformProvidingInverse( _polytope, matrix )
    
    pi = PosterIntersector( transformedPolytope )
    pi._intersectionVisitor = iv
    pi._parent = this
    return pi.release()

bool PosterIntersector.enter(  osg.Node node )
    if   not node.isCullingActive()  : return True
    if  _polytope.contains(node.getBound())  :
        if  node.getCullCallback()  :
            cccb = dynamic_cast< osg.ClusterCullingCallback*>( node.getCullCallback() )
            if  cccb  and  cccb.cull(_intersectionVisitor, 0, NULL)  : return False
        return True
    return False

void PosterIntersector.reset()
    _intersectionVisitor = NULL
    Intersector.reset()

void PosterIntersector.intersect( osgUtil.IntersectionVisitor iv, osg.Drawable* drawable )
    if   not _polytope.contains(drawable.getBound())  : return
    if  iv.getDoDummyTraversal()  : return
    
    # Find and collect all paged LODs in the node path
    nodePath = iv.getNodePath()
    for ( osg.NodePath.iterator itr=nodePath.begin() itr not =nodePath.end() ++itr )
        pagedLOD = dynamic_cast<osg.PagedLOD*>(*itr)
        if  pagedLOD  :
            # FIXME: The first non-empty getFileName() is used as the identity of this paged node.
            # This should work with VPB-generated terrains but maybe unusable with others.
            for ( unsigned int i=0 i<pagedLOD.getNumFileNames() ++i )
                if  pagedLOD.getFileName(i).empty()  : continue
                if  _parent._visitor.valid()  :
                    _parent._visitor.insertName( pagedLOD.getFileName(i) )
                break
            continue
        
        #osg.LOD* lod = dynamic_cast<osg.LOD*>(*itr)
#        if  lod  :
#        
#            if   not lod.getName().empty()  and  _parent._visitor.valid()  :
#                _parent._visitor.insertName( lod.getName() )
#        

# PosterPrinter: The implementation class of high-res rendering 
PosterPrinter.PosterPrinter():
    _outputTiles(False), _outputTileExt("bmp"),
    _isRunning(False), _isFinishing(False), _lastBindingFrame(0),
    _currentRow(0), _currentColumn(0),
    _camera(0), _finalPoster(0)
    _intersector = PosterIntersector(-1.0, -1.0, 1.0, 1.0)
    _visitor = PosterVisitor()
    _intersector.setPosterVisitor( _visitor )

void PosterPrinter.init(  osg.Camera* camera )
    if  _camera.valid()  :
        init( camera.getViewMatrix(), camera.getProjectionMatrix() )

void PosterPrinter.init(  osg.Matrixd view,  osg.Matrixd proj )
    if  _isRunning  : return
    _images.clear()
    _visitor.clearNames()
    _tileRows = (int)(_posterSize.y() / _tileSize.y())
    _tileColumns = (int)(_posterSize.x() / _tileSize.x())
    _currentRow = 0
    _currentColumn = 0
    _currentViewMatrix = view
    _currentProjectionMatrix = proj
    _lastBindingFrame = 0
    _isRunning = True
    _isFinishing = False

void PosterPrinter.frame(  osg.FrameStamp* fs, osg.Node* node )
    # Add cull callbacks to all existing paged nodes,
    # and advance frame when all callbacks are dispatched.
    if  addCullCallbacks(fs, node)  :
        return
    
    if  _isFinishing  :
        if fs.getFrameNumber()-_lastBindingFrame :>2  :
            # Record images and the final poster
            recordImages()
            if  _finalPoster.valid()  :
                print "Writing final result to file..."
                osgDB.writeImageFile( *_finalPoster, _outputPosterName )
            
            # Release all cull callbacks to free unused paged nodes
            removeCullCallbacks( node )
            _visitor.clearNames()
            
            _isFinishing = False
            print "Recording images finished."
    
    if  _isRunning  :
        # Every "copy-to-image" process seems to be finished in 2 frames.
        # So record them and dispatch camera to next tiles.
        if fs.getFrameNumber()-_lastBindingFrame :>2  :
            # Record images and unref them to free memory
            recordImages()
            
            # Release all cull callbacks to free unused paged nodes
            removeCullCallbacks( node )
            _visitor.clearNames()
            
            if  _camera.valid()  :
                print "Binding sub-camera ", _currentRow, "_", _currentColumn, " to image..."
                bindCameraToImage( _camera, _currentRow, _currentColumn )
                if  _currentColumn<_tileColumns-1  :
                    _currentColumn++
                else:
                    if  _currentRow<_tileRows-1  :
                        _currentRow++
                        _currentColumn = 0
                    else:
                        _isRunning = False
                        _isFinishing = True
            _lastBindingFrame = fs.getFrameNumber()

bool PosterPrinter.addCullCallbacks(  osg.FrameStamp* fs, osg.Node* node )
    if   not _visitor.inQueue()  or  done()  :
        return False
    
    _visitor.setAddingCallbacks( True )
    _camera.accept( *_visitor )
    _lastBindingFrame = fs.getFrameNumber()
    
    print "Dispatching callbacks to paged nodes... ", _visitor.inQueue()
    return True

void PosterPrinter.removeCullCallbacks( osg.Node* node )
    _visitor.setAddingCallbacks( False )
    _camera.accept( *_visitor )

void PosterPrinter.bindCameraToImage( osg.Camera* camera, int row, int col )
    stream = strstream()
    stream, "image_", row, "_", col
    
    image = osg.Image()
    image.setName( stream.str() )
    image.allocateImage( (int)_tileSize.x(), (int)_tileSize.y(), 1, GL_RGBA, GL_UNSIGNED_BYTE )
    _images[TilePosition(row,col)] = image
    
    # Calculate projection matrix offset of each tile
    offsetMatrix = osg.Matrix.scale(_tileColumns, _tileRows, 1.0) *
        osg.Matrix.translate(_tileColumns-1-2*col, _tileRows-1-2*row, 0.0)
    camera.setViewMatrix( _currentViewMatrix )
    camera.setProjectionMatrix( _currentProjectionMatrix * offsetMatrix )
    
    # Check intersections between the image-tile box and the model
    iv = osgUtil.IntersectionVisitor( _intersector )
    iv.setReadCallback( g_pagedLoadingCallback )
    _intersector.reset()
    camera.accept( iv )
    if  _intersector.containsIntersections()  :
        # Apply a cull calback to every paged node obtained, to force the highest level displaying.
        # This will be done by the PosterVisitor, who already records all the paged nodes.
    
    # Reattach cameras and allocated images
    camera.setRenderingCache( NULL )  # FIXME: Uses for reattaching camera with image, maybe  camera.detach( osg.Camera: if (inefficient) else COLOR_BUFFER )
    camera.attach( osg.Camera.COLOR_BUFFER, image, 0, 0 )

void PosterPrinter.recordImages()
    for ( TileImages.iterator itr=_images.begin() itr not =_images.end() ++itr )
        image = (itr.second)
        if  _finalPoster.valid()  :
            # FIXME: A stupid way to combine tile images to final result. Any better ideas?
            row = itr.first.first, col = itr.first.second
            for ( int t=0 t<image.t() ++t )
                source = image.data( 0, t )
                target = _finalPoster.data( col*(int)_tileSize.x(), t + row*(int)_tileSize.y() )
                memcpy( target, source, image.s() * 4 * sizeof(unsigned char) )
        
        if  _outputTiles  :
            osgDB.writeImageFile( *image, image.getName()+"."+_outputTileExt )
    _images.clear()

# Translated from file 'PosterPrinter.h'

#ifndef OSGPOSTER_POSTERPRINTER
#define OSGPOSTER_POSTERPRINTER

#include <osg/Camera>
#include <osg/PagedLOD>
#include <osgUtil/IntersectionVisitor>

#* PosterVisitor: A visitor for adding culling callbacks to newly allocated paged nodes 
class PosterVisitor (osg.NodeVisitor) :
    typedef std.set<str> PagedNodeNameSet
    
    PosterVisitor()
    META_NodeVisitor( osgPoster, PosterVisitor )
    
    def insertName(name):
    
         if  _pagedNodeNames.insert(name).second  : _needToApplyCount++ 
    
    def eraseName(name):
    
         if  _pagedNodeNames.erase(name)>0  : _needToApplyCount-- 
    
    def clearNames():
    
         _pagedNodeNames.clear() _needToApplyCount = 0 _appliedCount = 0 
    def getNumNames():
         return _pagedNodeNames.size() 
    
    def getPagedNodeNames():
    
         return _pagedNodeNames 
    def getPagedNodeNames():
         return _pagedNodeNames 
    
    def getNeedToApplyCount():
    
         return _needToApplyCount 
    def getAppliedCount():
         return _appliedCount 
    def inQueue():
         return  _needToApplyCount-_appliedCount if (_needToApplyCount>_appliedCount) else  0 
    
    def setAddingCallbacks(b):
    
         _addingCallbacks = b 
    def getAddingCallbacks():
         return _addingCallbacks 
    
    apply = virtual void( osg.LOD node )
    apply = virtual void( osg.PagedLOD node )
    def hasCullCallback(nc, target):
        
        if  nc==target  : return True
        elif   not nc  : return False
        hasCullCallback = return( nc.getNestedCallback(), target )
    
    _pagedNodeNames = PagedNodeNameSet()
    _appliedCount = unsigned int()
    _needToApplyCount = unsigned int()
    _addingCallbacks = bool()


#* PosterIntersector: A simple polytope intersector for updating pagedLODs in each image-tile 
class PosterIntersector (osgUtil.Intersector) :
    typedef std.set<str> PagedNodeNameSet
    
    PosterIntersector(  osg.Polytope polytope )
    PosterIntersector( double xMin, double yMin, double xMax, double yMax )
    
    def setPosterVisitor(pcv):
    
         _visitor = pcv 
    def getPosterVisitor():
         return _visitor 
    def getPosterVisitor():
         return _visitor 
    
    clone = virtual Intersector*( osgUtil.IntersectionVisitor iv )
    
    def containsIntersections():
    
         return _visitor.valid() and _visitor.getNumNames()>0 
    
    enter = virtual bool(  osg.Node node )
    def leave():
    reset = virtual void()
    intersect = virtual void( osgUtil.IntersectionVisitor iv, osg.Drawable* drawable )
    _intersectionVisitor = osgUtil.IntersectionVisitor*()
    _visitor = PosterVisitor()
    _parent = PosterIntersector*()
    _polytope = osg.Polytope()


#* PosterPrinter: The implementation class of high-res rendering 
class PosterPrinter (osg.Referenced) :
    typedef std.pair<unsigned int, unsigned int> TilePosition
    typedef std.map< TilePosition, osg.Image > TileImages
    
    PosterPrinter()
    
    #* Set to output each sub-image-tile to disk 
    def setOutputTiles(b):
         _outputTiles = b 
    def getOutputTiles():
         return _outputTiles 
    
    #* Set the output sub-image-tile extension, e.g. bmp 
    def setOutputTileExtension(ext):
         _outputTileExt = ext 
    def getOutputTileExtension():
         return _outputTileExt 
    
    #* Set the output poster name, e.g. output.bmp 
    def setOutputPosterName(name):
         _outputPosterName = name 
    def getOutputPosterName():
         return _outputPosterName 
    
    #* Set the size of each sub-image-tile, e.g. 640x480 
    def setTileSize(w, h):
         _tileSize.set(w, h) 
    def getTileSize():
         return _tileSize 
    
    #* Set the final size of the high-res poster, e.g. 6400x4800 
    def setPosterSize(w, h):
         _posterSize.set(w, h) 
    def getPosterSize():
         return _posterSize 
    
    #* Set the capturing camera 
    def setCamera(camera):
         _camera = camera 
    def getCamera():
         return _camera 
    
    #* Set the final poster image, should be already allocated 
    def setFinalPoster(image):
         _finalPoster = image 
    def getFinalPoster():
         return _finalPoster 
    
    def getPosterVisitor():
    
         return _visitor 
    def getPosterVisitor():
         return _visitor 
    
    def done():
    
         return  not _isRunning  and   not _isFinishing 
    
    init = void(  osg.Camera* camera )
    init = void(  osg.Matrixd view,  osg.Matrixd proj )
    frame = void(  osg.FrameStamp* fs, osg.Node* node )
    virtual ~PosterPrinter() 
    
    addCullCallbacks = bool(  osg.FrameStamp* fs, osg.Node* node )
    removeCullCallbacks = void( osg.Node* node )
    bindCameraToImage = void( osg.Camera* camera, int row, int col )
    recordImages = void()
    
    _outputTiles = bool()
    _outputTileExt = str()
    _outputPosterName = str()
    _tileSize = osg.Vec2()
    _posterSize = osg.Vec2()
    
    _isRunning = bool()
    _isFinishing = bool()
    _lastBindingFrame = unsigned int()
    _tileRows = int()
    _tileColumns = int()
    _currentRow = int()
    _currentColumn = int()
    _intersector = PosterIntersector()
    _visitor = PosterVisitor()
    
    _currentViewMatrix = osg.Matrixd()
    _currentProjectionMatrix = osg.Matrixd()
    _camera = osg.Camera()
    _finalPoster = osg.Image()
    _images = TileImages()


#endif


if __name__ == "__main__":
    main(sys.argv)
