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

# -*-c++-*- OpenSceneGraph example, osgposter.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


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
class FindTopMostNodeOfTypeVisitor : public osg.NodeVisitor
public:
    FindTopMostNodeOfTypeVisitor()
    :   osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _foundNode(0)
    
    
    def apply(node):
        result =  dynamic_cast<T*>( node )
        if  result  : _foundNode = result
        traverse = else:( node )
    
    _foundNode = T*()


template<class T>
def findTopMostNodeOfType(node):
    if  !node  : return 0
    
    FindTopMostNodeOfTypeVisitor<T> fnotv
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
    csn =  findTopMostNodeOfType<osg.CoordinateSystemNode>(scene)
    if  !csn  : return
    
    # Compute eye point in world coordiantes
    eye = osg.Vec3d()
    csn.getEllipsoidModel().convertLatLongHeightToXYZ(
        latLongHeight.x(), latLongHeight.y(), latLongHeight.z(), eye.x(), eye.y(), eye.z() )
    
    # Build matrix for computing target vector
    target_matrix = 
        osg.Matrixd.rotate( -hpr.x(), osg.Vec3d(1,0,0),
                              -latLongHeight.x(), osg.Vec3d(0,1,0),
                               latLongHeight.y(), osg.Vec3d(0,0,1) )
    
    # Compute tangent vector
    tangent =  target_matrix.preMult( osg.Vec3d(0,0,1) )
    
    # Compute non-inclined, non-rolled up vector
    up = osg.Vec3d( eye )
    up.normalize()
    
    # Incline by rotating the target- and up vector around the tangent/up-vector
    # cross-product
    up_cross_tangent =  up ^ tangent
    incline_matrix =  osg.Matrixd.rotate( hpr.y(), up_cross_tangent )
    target =  incline_matrix.preMult( tangent )
    
    # Roll by rotating the up vector around the target vector
    roll_matrix =  incline_matrix * osg.Matrixd.rotate( hpr.z(), target )
    up = roll_matrix.preMult( up )
    camera.setViewMatrixAsLookAt( eye, eye+target, up )

# CustomRenderer: Do culling only while loading PagedLODs 
class CustomRenderer : public osgViewer.Renderer
public:
    CustomRenderer( osg.Camera* camera )
    : osgViewer.Renderer(camera), _cullOnly(true)
    
    void setCullOnly(bool on)  _cullOnly = on 

    virtual void operator ()( osg.GraphicsContext* )
        if  _graphicsThreadDoesCull  :
            if _cullOnly : cull()
            cull_draw = else:()
    
    virtual void cull()
        sceneView =  _sceneView[0].get()
        if  !sceneView || _done || _graphicsThreadDoesCull  :
            return
        
        updateSceneView( sceneView )
        
        view =  dynamic_cast<osgViewer.View*>( _camera.getView() )
        if  view  :
            sceneView.setFusionDistance( view.getFusionDistanceMode(), view.getFusionDistanceValue() )
        sceneView.inheritCullSettings( *(sceneView.getCamera()) )
        sceneView.cull()
    
    _cullOnly = bool()


# PrintPosterHandler: A gui handler for interactive high-res capturing 
class PrintPosterHandler : public osgGA.GUIEventHandler
public:
    PrintPosterHandler( PosterPrinter* printer )
    : _printer(printer), _started(false) 
    
    def handle(ea, aa):
        view =  dynamic_cast<osgViewer.View*>( aa )
        if  !view  : return false
        
        switch( ea.getEventType() )
        case osgGA.GUIEventAdapter.FRAME:
            if  view.getDatabasePager()  :
                # Wait until all paged nodes are processed
                if  view.getDatabasePager().getRequestsInProgress()  :
                    break
            
            if  _printer.valid()  :
                _printer.frame( view.getFrameStamp(), view.getSceneData() )
                if  _started  _printer.done()  :
                    root =  dynamic_cast<osg.Switch*>( view.getSceneData() )
                    if  root  :
                        # Assume child 0 is the loaded model and 1 is the poster camera
                        # Switch them in time to prevent dual traversals of subgraph
                        root.setValue( 0, true )
                        root.setValue( 1, false )
                    _started = false
            break
        
        case osgGA.GUIEventAdapter.KEYDOWN:
            if  ea.getKey()=='p' || ea.getKey()=='P'  :
                if  _printer.valid()  :
                    root =  dynamic_cast<osg.Switch*>( view.getSceneData() )
                    if  root  :
                        # Assume child 0 is the loaded model and 1 is the poster camera
                        root.setValue( 0, false )
                        root.setValue( 1, true )
                    
                    _printer.init( view.getCamera() )
                    _started = true
                true = return()
            break
        
        default:
            break
        false = return()

protected:
    osg.ref_ptr<PosterPrinter> _printer
    _started = bool()


# The main entry 
def main(argc, argv):
    arguments = osg.ArgumentParser( argc, argv )
    usage =  arguments.getApplicationUsage()
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
    
    if  arguments.read("-h") || arguments.read("--help")  :
        usage.write( std.cout )
        return 1
    
    # Poster arguments
    activeMode =  true
    outputPoster =  true
    #bool outputTiles = false
    tileWidth =  640, tileHeight = 480
    posterWidth =  640*2, posterHeight = 480*2
    posterName =  "poster.bmp", extName = "bmp"
    bgColor = osg.Vec4(0.2f, 0.2f, 0.6f, 1.0f)
    renderImplementation =  osg.Camera.FRAME_BUFFER_OBJECT
    
    while  arguments.read("--inactive")  :  activeMode = false 
    while  arguments.read("--color", bgColor.r(), bgColor.g(), bgColor.b())  : 
    while  arguments.read("--tilesize", tileWidth, tileHeight)  : 
    while  arguments.read("--finalsize", posterWidth, posterHeight)  : 
    while  arguments.read("--poster", posterName)  : 
    while  arguments.read("--ext", extName)  : 
    while  arguments.read("--enable-output-poster")  :  outputPoster = true 
    while  arguments.read("--disable-output-poster")  :  outputPoster = false 
    #while  arguments.read("--enable-output-tiles")  :  outputTiles = true 
    #while  arguments.read("--disable-output-tiles")  :  outputTiles = false 
    while  arguments.read("--use-fbo") :  renderImplementation = osg.Camera.FRAME_BUFFER_OBJECT 
    while  arguments.read("--use-pbuffer") :  renderImplementation = osg.Camera.PIXEL_BUFFER 
    while  arguments.read("--use-pbuffer-rtt") :  renderImplementation = osg.Camera.PIXEL_BUFFER_RTT 
    while  arguments.read("--use-fb") :  renderImplementation = osg.Camera.FRAME_BUFFER 
    
    # Camera settings for inactive screenshot
    useLatLongHeight =  true
    eye = osg.Vec3d()
    latLongHeight = osg.Vec3d( 50.0, 10.0, 2000.0 )
    hpr = osg.Vec3d( 0.0, 0.0, 0.0 )
    if  arguments.read("--camera-eye", eye.x(), eye.y(), eye.z())  :
        useLatLongHeight = false
        activeMode = false
    else: if  arguments.read("--camera-latlongheight", latLongHeight.x(), latLongHeight.y(), latLongHeight.z())  :
        activeMode = false
        latLongHeight.x() = osg.DegreesToRadians( latLongHeight.x() )
        latLongHeight.y() = osg.DegreesToRadians( latLongHeight.y() )
    if  arguments.read("--camera-hpr", hpr.x(), hpr.y(), hpr.z())  :
        activeMode = false
        hpr.x() = osg.DegreesToRadians( hpr.x() )
        hpr.y() = osg.DegreesToRadians( hpr.y() )
        hpr.z() = osg.DegreesToRadians( hpr.z() )
    
    # Construct scene graph
    scene =  osgDB.readNodeFiles( arguments )
    if  !scene  : scene = osgDB.readNodeFile( "cow.osgt" )
    if  !scene  :
        print arguments.getApplicationName(), ": No data loaded"
        return 1
    
    # Create camera for rendering tiles offscreen. FrameBuffer is recommended because it requires less memory.
    osg.ref_ptr<osg.Camera> camera = new osg.Camera
    camera.setClearColor( bgColor )
    camera.setClearMask( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    camera.setReferenceFrame( osg.Transform.ABSOLUTE_RF )
    camera.setRenderOrder( osg.Camera.PRE_RENDER )
    camera.setRenderTargetImplementation( renderImplementation )
    camera.setViewport( 0, 0, tileWidth, tileHeight )
    camera.addChild( scene )
    
    # Set the printer
    osg.ref_ptr<PosterPrinter> printer = new PosterPrinter
    printer.setTileSize( tileWidth, tileHeight )
    printer.setPosterSize( posterWidth, posterHeight )
    printer.setCamera( camera.get() )
    
    osg.ref_ptr<osg.Image> posterImage = 0
    if  outputPoster  :
        posterImage = new osg.Image
        posterImage.allocateImage( posterWidth, posterHeight, 1, GL_RGBA, GL_UNSIGNED_BYTE )
        printer.setFinalPoster( posterImage.get() )
        printer.setOutputPosterName( posterName )
    
#if 0
    # While recording sub-images of the poster, the scene will always be traversed twice, from its two
    # parent node: root and camera. Sometimes this may not be so comfortable.
    # To prevent this behaviour, we can use a switch node to enable one parent and disable the other.
    # However, the solution also needs to be used with care, as the window will go blank while taking
    # snapshots and recover later.
    osg.ref_ptr<osg.Switch> root = new osg.Switch
    root.addChild( scene, true )
    root.addChild( camera.get(), false )
#else:
    osg.ref_ptr<osg.Group> root = new osg.Group
    root.addChild( scene )
    root.addChild( camera.get() )
#endif
    
    viewer = osgViewer.Viewer()
    viewer.setSceneData( root.get() )
    viewer.getDatabasePager().setDoPreCompile( false )
    
    if  renderImplementation==osg.Camera.FRAME_BUFFER  :
        # FRAME_BUFFER requires the window resolution equal or greater than the to-be-copied size
        viewer.setUpViewInWindow( 100, 100, tileWidth, tileHeight )
    else:
        # We want to see the console output, so just render in a window
        viewer.setUpViewInWindow( 100, 100, 800, 600 )
    
    if  activeMode  :
        viewer.addEventHandler( new PrintPosterHandler(printer.get()) )
        viewer.addEventHandler( new osgViewer.StatsHandler )
        viewer.addEventHandler( new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
        viewer.setCameraManipulator( new osgGA.TrackballManipulator )
        viewer.run()
    else:
        camera =  viewer.getCamera()
        if  !useLatLongHeight  : computeViewMatrix( camera, eye, hpr )
        computeViewMatrixOnEarth = else:( camera, scene, latLongHeight, hpr )
        
        osg.ref_ptr<CustomRenderer> renderer = new CustomRenderer( camera )
        camera.setRenderer( renderer.get() )
        viewer.setThreadingModel( osgViewer.Viewer.SingleThreaded )
        
        # Realize and initiate the first PagedLOD request
        viewer.realize()
        viewer.frame()
        
        printer.init( camera )
        while  !printer.done()  :
            viewer.advance()
            
            # Keep updating and culling until full level of detail is reached
            renderer.setCullOnly( true )
            while  viewer.getDatabasePager().getRequestsInProgress()  :
                viewer.updateTraversal()
                viewer.renderingTraversals()
            
            renderer.setCullOnly( false )
            printer.frame( viewer.getFrameStamp(), viewer.getSceneData() )
            viewer.renderingTraversals()
    return 0
#include <osg/ClusterCullingCallback>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <string.h>
#include <iostream>
#include <sstream>
#include "PosterPrinter.h"

# PagedLoadingCallback: Callback for loading paged nodes while doing intersecting test 
struct PagedLoadingCallback : public osgUtil.IntersectionVisitor.ReadCallback
    virtual osg.Node* readNodeFile(  str filename )
        return osgDB.readNodeFile( filename )

static osg.ref_ptr<PagedLoadingCallback> g_pagedLoadingCallback = new PagedLoadingCallback

# LodCullingCallback: Callback for culling LODs and selecting the highest level 
class LodCullingCallback : public osg.NodeCallback
public:
    virtual void operator()( osg.Node* node, osg.NodeVisitor* nv )
        lod =  static_cast<osg.LOD*>(node)
        if  lod  lod.getNumChildren()>0  :
            lod.getChild(lod.getNumChildren()-1).accept(*nv)

static osg.ref_ptr<LodCullingCallback> g_lodCullingCallback = new LodCullingCallback

# PagedCullingCallback: Callback for culling paged nodes and selecting the highest level 
class PagedCullingCallback : public osg.NodeCallback
public:
    virtual void operator()( osg.Node* node, osg.NodeVisitor* nv )
        pagedLOD =  static_cast<osg.PagedLOD*>(node)
        if  pagedLOD  pagedLOD.getNumChildren()>0  :
            unsigned int numChildren = pagedLOD.getNumChildren()
            updateTimeStamp =  nv.getVisitorType()==osg.NodeVisitor.CULL_VISITOR
            if  nv.getFrameStamp()  updateTimeStamp  :
                timeStamp =  nv.getFrameStamp()?nv.getFrameStamp().getReferenceTime():0.0
                unsigned int frameNumber = nv.getFrameStamp()?nv.getFrameStamp().getFrameNumber():0
                
                pagedLOD.setFrameNumberOfLastTraversal( frameNumber )
                pagedLOD.setTimeStamp( numChildren-1, timeStamp )
                pagedLOD.setFrameNumber( numChildren-1, frameNumber )
                pagedLOD.getChild(numChildren-1).accept(*nv)
            
            # Request for new child
            if  !pagedLOD.getDisableExternalChildrenPaging() 
                 nv.getDatabaseRequestHandler() 
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

static osg.ref_ptr<PagedCullingCallback> g_pagedCullingCallback = new PagedCullingCallback

# PosterVisitor: A visitor for adding culling callbacks to newly allocated paged nodes 
PosterVisitor.PosterVisitor()
:   osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
    _appliedCount(0), _needToApplyCount(0),
    _addingCallbacks(true)

void PosterVisitor.apply( osg.LOD node )
    #if  !hasCullCallback(node.getCullCallback(), g_lodCullingCallback.get())  :
        if  !node.getName().empty()  :
            itr =  _pagedNodeNames.find( node.getName() )
            if  itr!=_pagedNodeNames.end()  :
                insertCullCallback( node, g_lodCullingCallback.get() )
                _appliedCount++
    else: if  !_addingCallbacks  :
        node.removeCullCallback( g_lodCullingCallback.get() )
        _appliedCount--
    traverse( node )

void PosterVisitor.apply( osg.PagedLOD node )
    if  !hasCullCallback(node.getCullCallback(), g_pagedCullingCallback.get())  :
        for ( unsigned int i=0 i<node.getNumFileNames() ++i )
            if  node.getFileName(i).empty()  : continue
            
            itr =  _pagedNodeNames.find( node.getFileName(i) )
            if  itr!=_pagedNodeNames.end()  :
                node.addCullCallback( g_pagedCullingCallback.get() )
                _appliedCount++
            break
    else: if  !_addingCallbacks  :
        node.removeCullCallback( g_pagedCullingCallback.get() )
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
    
    osg.ref_ptr<PosterIntersector> pi = new PosterIntersector( transformedPolytope )
    pi._intersectionVisitor = iv
    pi._parent = this
    return pi.release()

bool PosterIntersector.enter(  osg.Node node )
    if  !node.isCullingActive()  : return true
    if  _polytope.contains(node.getBound())  :
        if  node.getCullCallback()  :
            cccb = 
                dynamic_cast< osg.ClusterCullingCallback*>( node.getCullCallback() )
            if  cccb  cccb.cull(_intersectionVisitor, 0, NULL)  : return false
        true = return()
    false = return()

void PosterIntersector.reset()
    _intersectionVisitor = NULL
    Intersector.reset()

void PosterIntersector.intersect( osgUtil.IntersectionVisitor iv, osg.Drawable* drawable )
    if  !_polytope.contains(drawable.getBound())  : return
    if  iv.getDoDummyTraversal()  : return
    
    # Find and collect all paged LODs in the node path
    nodePath =  iv.getNodePath()
    for ( osg.NodePath.iterator itr=nodePath.begin() itr!=nodePath.end() ++itr )
        pagedLOD =  dynamic_cast<osg.PagedLOD*>(*itr)
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
        if  lod  :
            if  !lod.getName().empty()  _parent._visitor.valid()  :
                _parent._visitor.insertName( lod.getName() )

# PosterPrinter: The implementation class of high-res rendering 
PosterPrinter.PosterPrinter():
    _outputTiles(false), _outputTileExt("bmp"),
    _isRunning(false), _isFinishing(false), _lastBindingFrame(0),
    _currentRow(0), _currentColumn(0),
    _camera(0), _finalPoster(0)
    _intersector = new PosterIntersector(-1.0, -1.0, 1.0, 1.0)
    _visitor = new PosterVisitor
    _intersector.setPosterVisitor( _visitor.get() )

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
    _isRunning = true
    _isFinishing = false

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
            
            _isFinishing = false
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
                bindCameraToImage( _camera.get(), _currentRow, _currentColumn )
                if  _currentColumn<_tileColumns-1  :
                    _currentColumn++
                else:
                    if  _currentRow<_tileRows-1  :
                        _currentRow++
                        _currentColumn = 0
                    else:
                        _isRunning = false
                        _isFinishing = true
            _lastBindingFrame = fs.getFrameNumber()

bool PosterPrinter.addCullCallbacks(  osg.FrameStamp* fs, osg.Node* node )
    if  !_visitor.inQueue() || done()  :
        false = return()
    
    _visitor.setAddingCallbacks( true )
    _camera.accept( *_visitor )
    _lastBindingFrame = fs.getFrameNumber()
    
    print "Dispatching callbacks to paged nodes... ", _visitor.inQueue()
    true = return()

void PosterPrinter.removeCullCallbacks( osg.Node* node )
    _visitor.setAddingCallbacks( false )
    _camera.accept( *_visitor )

void PosterPrinter.bindCameraToImage( osg.Camera* camera, int row, int col )
    stream = strstream()
    stream, "image_", row, "_", col
    
    osg.ref_ptr<osg.Image> image = new osg.Image
    image.setName( stream.str() )
    image.allocateImage( (int)_tileSize.x(), (int)_tileSize.y(), 1, GL_RGBA, GL_UNSIGNED_BYTE )
    _images[TilePosition(row,col)] = image.get()
    
    # Calculate projection matrix offset of each tile
    offsetMatrix = 
        osg.Matrix.scale(_tileColumns, _tileRows, 1.0) *
        osg.Matrix.translate(_tileColumns-1-2*col, _tileRows-1-2*row, 0.0)
    camera.setViewMatrix( _currentViewMatrix )
    camera.setProjectionMatrix( _currentProjectionMatrix * offsetMatrix )
    
    # Check intersections between the image-tile box and the model
    iv = osgUtil.IntersectionVisitor( _intersector.get() )
    iv.setReadCallback( g_pagedLoadingCallback.get() )
    _intersector.reset()
    camera.accept( iv )
    if  _intersector.containsIntersections()  :
        # Apply a cull calback to every paged node obtained, to force the highest level displaying.
        # This will be done by the PosterVisitor, who already records all the paged nodes.
    
    # Reattach cameras and new allocated images
    camera.setRenderingCache( NULL )  # FIXME: Uses for reattaching camera with image, maybe inefficient?
    camera.detach( osg.Camera.COLOR_BUFFER )
    camera.attach( osg.Camera.COLOR_BUFFER, image.get(), 0, 0 )

void PosterPrinter.recordImages()
    for ( TileImages.iterator itr=_images.begin() itr!=_images.end() ++itr )
        image =  (itr.second).get()
        if  _finalPoster.valid()  :
            # FIXME: A stupid way to combine tile images to final result. Any better ideas?
            unsigned int row = itr.first.first, col = itr.first.second
            for ( int t=0 t<image.t() ++t )
                unsigned char* source = image.data( 0, t )
                unsigned char* target = _finalPoster.data( col*(int)_tileSize.x(), t + row*(int)_tileSize.y() )
                memcpy( target, source, image.s() * 4 * sizeof(unsigned char) )
        
        if  _outputTiles  :
            osgDB.writeImageFile( *image, image.getName()+"."+_outputTileExt )
    _images.clear()
#ifndef OSGPOSTER_POSTERPRINTER
#define OSGPOSTER_POSTERPRINTER

#include <osg/Camera>
#include <osg/PagedLOD>
#include <osgUtil/IntersectionVisitor>

#* PosterVisitor: A visitor for adding culling callbacks to newly allocated paged nodes 
class PosterVisitor : public osg.NodeVisitor
public:
    typedef std.set<str> PagedNodeNameSet
    
    PosterVisitor()
    META_NodeVisitor( osgPoster, PosterVisitor )
    
    void insertName(  str name )
     if  _pagedNodeNames.insert(name).second  : _needToApplyCount++ 
    
    void eraseName(  str name )
     if  _pagedNodeNames.erase(name)>0  : _needToApplyCount-- 
    
    void clearNames()  _pagedNodeNames.clear() _needToApplyCount = 0 _appliedCount = 0 
    unsigned int getNumNames()   return _pagedNodeNames.size() 
    
    PagedNodeNameSet getPagedNodeNames()  return _pagedNodeNames 
     PagedNodeNameSet getPagedNodeNames()   return _pagedNodeNames 
    
    unsigned int getNeedToApplyCount()   return _needToApplyCount 
    unsigned int getAppliedCount()   return _appliedCount 
    unsigned int inQueue()   return _needToApplyCount>_appliedCount ? _needToApplyCount-_appliedCount : 0 
    
    void setAddingCallbacks( bool b )  _addingCallbacks = b 
    bool getAddingCallbacks()   return _addingCallbacks 
    
    virtual void apply( osg.LOD node )
    virtual void apply( osg.PagedLOD node )
    
protected:
    def hasCullCallback(nc, target):
        if  nc==target  : return true
        else: if  !nc  : return false
        hasCullCallback = return( nc.getNestedCallback(), target )
    
    _pagedNodeNames = PagedNodeNameSet()
    unsigned int _appliedCount
    unsigned int _needToApplyCount
    _addingCallbacks = bool()


#* PosterIntersector: A simple polytope intersector for updating pagedLODs in each image-tile 
class PosterIntersector : public osgUtil.Intersector
public:
    typedef std.set<str> PagedNodeNameSet
    
    PosterIntersector(  osg.Polytope polytope )
    PosterIntersector( double xMin, double yMin, double xMax, double yMax )
    
    void setPosterVisitor( PosterVisitor* pcv )  _visitor = pcv 
    PosterVisitor* getPosterVisitor()  return _visitor.get() 
     PosterVisitor* getPosterVisitor()   return _visitor.get() 
    
    virtual Intersector* clone( osgUtil.IntersectionVisitor iv )
    
    virtual bool containsIntersections()
     return _visitor.valid()_visitor.getNumNames()>0 
    
    virtual bool enter(  osg.Node node )
    virtual void leave() 
    virtual void reset()
    virtual void intersect( osgUtil.IntersectionVisitor iv, osg.Drawable* drawable )
    
protected:
    _intersectionVisitor = osgUtil.IntersectionVisitor*()
    osg.ref_ptr<PosterVisitor> _visitor
    _parent = PosterIntersector*()
    _polytope = osg.Polytope()


#* PosterPrinter: The implementation class of high-res rendering 
class PosterPrinter : public osg.Referenced
public:
    typedef std.pair<unsigned int, unsigned int> TilePosition
    typedef std.map< TilePosition, osg.ref_ptr<osg.Image> > TileImages
    
    PosterPrinter()
    
    #* Set to output each sub-image-tile to disk 
    void setOutputTiles( bool b )  _outputTiles = b 
    bool getOutputTiles()   return _outputTiles 
    
    #* Set the output sub-image-tile extension, e.g. bmp 
    void setOutputTileExtension(  str ext )  _outputTileExt = ext 
     str getOutputTileExtension()   return _outputTileExt 
    
    #* Set the output poster name, e.g. output.bmp 
    void setOutputPosterName(  str name )  _outputPosterName = name 
     str getOutputPosterName()   return _outputPosterName 
    
    #* Set the size of each sub-image-tile, e.g. 640x480 
    void setTileSize( int w, int h )  _tileSize.set(w, h) 
     osg.Vec2 getTileSize()   return _tileSize 
    
    #* Set the final size of the high-res poster, e.g. 6400x4800 
    void setPosterSize( int w, int h )  _posterSize.set(w, h) 
     osg.Vec2 getPosterSize()   return _posterSize 
    
    #* Set the capturing camera 
    void setCamera( osg.Camera* camera )  _camera = camera 
     osg.Camera* getCamera()   return _camera.get() 
    
    #* Set the final poster image, should be already allocated 
    void setFinalPoster( osg.Image* image )  _finalPoster = image 
     osg.Image* getFinalPoster()   return _finalPoster.get() 
    
    PosterVisitor* getPosterVisitor()  return _visitor.get() 
     PosterVisitor* getPosterVisitor()   return _visitor.get() 
    
    bool done()   return !_isRunning  !_isFinishing 
    
    init = void(  osg.Camera* camera )
    init = void(  osg.Matrixd view,  osg.Matrixd proj )
    frame = void(  osg.FrameStamp* fs, osg.Node* node )
    
protected:
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
    unsigned int _lastBindingFrame
    _tileRows = int()
    _tileColumns = int()
    _currentRow = int()
    _currentColumn = int()
    osg.ref_ptr<PosterIntersector> _intersector
    osg.ref_ptr<PosterVisitor> _visitor
    
    _currentViewMatrix = osg.Matrixd()
    _currentProjectionMatrix = osg.Matrixd()
    osg.ref_ptr<osg.Camera> _camera
    osg.ref_ptr<osg.Image> _finalPoster
    _images = TileImages()


#endif


if __name__ == "__main__":
    main(sys.argv)
