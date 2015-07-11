#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgocclusionquery"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgocclusionquery.cpp'

# OpenSceneGraph example, osganimate.
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

# This exampl demonstrates use of OcclusionQueryNode.
#
# In general, you use OcclusionQueryNode by simply attaching a subgraph
# or subgraphs as children, and it performs an OpenGL oclusion query
# to determine whether to draw the subgraphs or not.
#
# You can manually insert OcclusionQueryNodes at strategic locations
# in your scene graph, or you can write a NodeVisitor to insert them
# automatically, as this example shows.
#
# Run this example with no command line arguments, and it creates
# a "stock scene" to show how OcclusionQueryNode can be used.
#
# Or, run this example with a model on the command line, and the
# example uses a NodeVisitor to try to find worthwhile locations
# for OcclusionQueryNodes in your the scene graph.

#include <osg/NodeVisitor>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/StateSet>
#include <osg/StateAttribute>
#include <osg/PolygonMode>
#include <osg/ColorMask>
#include <osg/PolygonOffset>
#include <osg/Depth>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osgUtil/Optimizer>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/StateSetManipulator>

#include <osg/OcclusionQueryNode>

#include <iostream>
#include <sstream>


# NodeVisitors and utility functions for OcclusionQueryNode

# Use this visitor to insert OcclusionQueryNodes (OQNs) in the
#   visited subgraph. Only one OQN will test any particular node
#   (no nesting). See also OcclusionQueryNonFlatVisitor.
class OcclusionQueryVisitor (osg.NodeVisitor) :
    OcclusionQueryVisitor()
    virtual ~OcclusionQueryVisitor()

    # Specify the vertex count threshold for performing occlusion
    #   query tests. Nodes in the scene graph whose total child geometry
    #   contains fewer vertices than the specified threshold will
    #   never be tested, just drawn. (In fact, they will br treated as
    #   potential occluders and rendered first in front-to-back order.)
    setOccluderThreshold = void( int vertices )
    int getOccluderThreshold() 

    apply = virtual void( osg.OcclusionQueryNode oqn )
    apply = virtual void( osg.Group group )
    apply = virtual void( osg.Geode geode )
    addOQN = void( osg.Node node )

    # When an OQR creates all OQNs and each OQN shares the same OQC,
    #   these methods are used to uniquely name all OQNs. Handy
    #   for debugging.
    getNextOQNName = str()
    def getNameIdx():
         return _nameIdx 

    _state = osg.StateSet()
    _debugState = osg.StateSet()

    _nameIdx = unsigned int()

    _occluderThreshold = int()


# Find all OQNs in the visited scene graph and set their visibility threshold.
class VisibilityThresholdVisitor (osg.NodeVisitor) :
    VisibilityThresholdVisitor( unsigned int threshold=500 )
      : osg.NodeVisitor( osg.NodeVisitor.TRAVERSE_ALL_CHILDREN ),
        _visThreshold( threshold ) 
    virtual ~VisibilityThresholdVisitor() 

    apply = virtual void( osg.OcclusionQueryNode oqn )
    _visThreshold = unsigned int()


# Find all OQNs in the visited scene graph and set the number of frames
#   between queries.
class QueryFrameCountVisitor (osg.NodeVisitor) :
    QueryFrameCountVisitor( int count=5 )
      : osg.NodeVisitor( osg.NodeVisitor.TRAVERSE_ALL_CHILDREN ),
        _count( count ) 
    virtual ~QueryFrameCountVisitor() 

    apply = virtual void( osg.OcclusionQueryNode oqn )
    _count = unsigned int()


# Find all OQNs in the visited scene graph and enable or disable queries..
class EnableQueryVisitor (osg.NodeVisitor) :
    EnableQueryVisitor( bool enable=True )
      : osg.NodeVisitor( osg.NodeVisitor.TRAVERSE_ALL_CHILDREN ),
        _enabled( enable ) 
    virtual ~EnableQueryVisitor() 

    apply = virtual void( osg.OcclusionQueryNode oqn )
    _enabled = bool()


# Find all OQNs in the visited scene graph and enable or disable the
#   debug bounding volume display.
class DebugDisplayVisitor (osg.NodeVisitor) :
    DebugDisplayVisitor( bool debug=True )
      : osg.NodeVisitor( osg.NodeVisitor.TRAVERSE_ALL_CHILDREN ),
        _debug( debug ) 
    virtual ~DebugDisplayVisitor() 

    apply = virtual void( osg.OcclusionQueryNode oqn )
    _debug = bool()


# Remove all OQNs from the visited scene graph.
class RemoveOcclusionQueryVisitor (osg.NodeVisitor) :
    RemoveOcclusionQueryVisitor()
    virtual ~RemoveOcclusionQueryVisitor()

    apply = virtual void( osg.OcclusionQueryNode oqn )


# Gather statistics about OQN performance in the visited scene graph.
class StatisticsVisitor (osg.NodeVisitor) :
    StatisticsVisitor( osg.NodeVisitor.TraversalMode mode=osg.NodeVisitor.TRAVERSE_ACTIVE_CHILDREN )
    virtual ~StatisticsVisitor()

    apply = virtual void( osg.OcclusionQueryNode oqn )

    reset = void()
    unsigned int getNumOQNs() 
    unsigned int getNumPassed() 
    _numOQNs = unsigned int()
    _numPassed = unsigned int()



def countGeometryVertices(geom):


    
    if !geom.getVertexArray() :
        return 0

    # TBD This will eventually iterate over the PrimitiveSets and total the
    #   number of vertices actually used. But for now, it just returns the
    #   size of the vertex array.

    return geom.getVertexArray().getNumElements()

class VertexCounter (osg.NodeVisitor) :
    VertexCounter( int limit )
      : osg.NodeVisitor( osg.NodeVisitor.TRAVERSE_ALL_CHILDREN ),
        _limit( limit ),
        _total( 0 ) 
    ~VertexCounter() 

    def getTotal():

         return _total 
    def exceeded():
         return _total > _limit 
    def reset():
         _total = 0 

    def apply(node):

        
        # Check for early abort. If out total already exceeds the
        #   max number of vertices, no need to traverse further.
        if exceeded() :
            return
        traverse( node )

    def apply(geode):

        
        # Possible early abort.
        if exceeded() :
            return

        i = unsigned int()
        for( i = 0 i < geode.getNumDrawables() i++ )
            geom = dynamic_cast<osg.Geometry *>(geode.getDrawable(i))
            if  !geom  :
                continue

            _total += countGeometryVertices( geom )

            if _total > _limit :
                break
    _limit = int()
    _total = int()




OcclusionQueryVisitor.OcclusionQueryVisitor()
  : osg.NodeVisitor( osg.NodeVisitor.TRAVERSE_ALL_CHILDREN ),
    _nameIdx( 0 ),
    _occluderThreshold( 5000 )
    # Create a dummy OcclusionQueryNode just so we can get its state.
    # We'll then share that state between all OQNs we add to the visited scene graph.
    oqn = osg.OcclusionQueryNode()

    _state = oqn.getQueryStateSet()
    _debugState = oqn.getDebugStateSet()

OcclusionQueryVisitor.~OcclusionQueryVisitor()
    osg.notify( osg.INFO ), "osgOQ: OcclusionQueryVisitor: Added ", getNameIdx(), " OQNodes."

void
OcclusionQueryVisitor.setOccluderThreshold( int vertices )
    _occluderThreshold = vertices
int
OcclusionQueryVisitor.getOccluderThreshold() 
    return _occluderThreshold

void
OcclusionQueryVisitor.apply( osg.OcclusionQueryNode oqn )
    # A subgraph is already under osgOQ control.
    # Don't traverse further.
    return

void
OcclusionQueryVisitor.apply( osg.Group group )
    if group.getNumParents() == 0 :
        # Can't add an OQN above a root node.
        traverse( group )
        return

    preTraverseOQNCount = getNameIdx()
    traverse( group )

    if getNameIdx() > preTraverseOQNCount :
        # A least one OQN was added below the current node.
        #   Don't add one here to avoid hierarchical nesting.
        return

    # There are no OQNs below this group. If the vertex
    #   count exceeds the threshold, add an OQN here.
    addOQN( group )

void
OcclusionQueryVisitor.apply( osg.Geode geode )
    if geode.getNumParents() == 0 :
        # Can't add an OQN above a root node.
        traverse( geode )
        return

    addOQN( geode )

void
OcclusionQueryVisitor.addOQN( osg.Node node )
    vc = VertexCounter( _occluderThreshold )
    node.accept( vc )
    if vc.exceeded() :
        # Insert OQN(s) above this node.
        np = node.getNumParents()
        while np-- :
            parent = dynamic_cast<osg.Group*>( node.getParent( np ) )
            if parent != NULL :
                oqn = osg.OcclusionQueryNode()
                oqn.addChild( node )
                parent.replaceChild( node, oqn.get() )

                oqn.setName( getNextOQNName() )
                # Set all OQNs to use the same query StateSets (instead of multiple copies
                #   of the same StateSet) for efficiency.
                oqn.setQueryStateSet( _state.get() )
                oqn.setDebugStateSet( _debugState.get() )

str
OcclusionQueryVisitor.getNextOQNName()
    ostr = std.ostringstream()
    ostr, "OQNode_", _nameIdx++
    return ostr.str()




#
void
VisibilityThresholdVisitor.apply( osg.OcclusionQueryNode oqn )
    oqn.setVisibilityThreshold( _visThreshold )

    traverse( oqn )

void
QueryFrameCountVisitor.apply( osg.OcclusionQueryNode oqn )
    oqn.setQueryFrameCount( _count )

    traverse( oqn )

void
EnableQueryVisitor.apply( osg.OcclusionQueryNode oqn )
    oqn.setQueriesEnabled( _enabled )

    traverse( oqn )


void
DebugDisplayVisitor.apply( osg.OcclusionQueryNode oqn )
    oqn.setDebugDisplay( _debug )

    traverse( oqn )


RemoveOcclusionQueryVisitor.RemoveOcclusionQueryVisitor()
  : osg.NodeVisitor( osg.NodeVisitor.TRAVERSE_ALL_CHILDREN )

RemoveOcclusionQueryVisitor.~RemoveOcclusionQueryVisitor()

void
RemoveOcclusionQueryVisitor.apply( osg.OcclusionQueryNode oqn )
    if oqn.getNumParents() == 0 :
        # Even if this is an OQN, can't delete it because it's the root.
        traverse( oqn )
        return

    oqnPtr = oqn

    np = oqn.getNumParents()
    while np-- :
        parent = dynamic_cast<osg.Group*>( oqn.getParent( np ) )
        if parent != NULL :
            # Remove OQN from parent.
            parent.removeChild( oqnPtr.get() )

            # Add OQN's children to parent.
            nc = oqn.getNumChildren()
            while nc-- :
                parent.addChild( oqn.getChild( nc ) )



StatisticsVisitor.StatisticsVisitor( osg.NodeVisitor.TraversalMode mode )
  : osg.NodeVisitor( mode ),
    _numOQNs( 0 ),
    _numPassed( 0 )

StatisticsVisitor.~StatisticsVisitor()

void
StatisticsVisitor.apply( osg.OcclusionQueryNode oqn )
    _numOQNs++
    if oqn.getPassed() :
        _numPassed++

    traverse( oqn )

void
StatisticsVisitor.reset()
    _numOQNs = _numPassed = 0

unsigned int
StatisticsVisitor.getNumOQNs() 
    return _numOQNs
unsigned int
StatisticsVisitor.getNumPassed() 
    return _numPassed

# End NodeVisitors



# KetHandler --
# Allow user to do interesting things with an
# OcclusionQueryNode-enabled scene graph at run time.
class KeyHandler (osgGA.GUIEventHandler) :
    KeyHandler( osg.Node node )
      : _node( node ),
        _enable( True ),
        _debug( False )
    

    bool handle(  osgGA.GUIEventAdapter ea, osgGA.GUIActionAdapter )
        switch( ea.getEventType() )
            case(osgGA.GUIEventAdapter.KEYUP):
                if ea.getKey()==osgGA.GUIEventAdapter.KEY_F6 :
                    # F6 -- Toggle osgOQ testing.
                    _enable = !_enable
                    eqv = EnableQueryVisitor( _enable )
                    _node.accept( eqv )
                    return True
                elif ea.getKey()==osgGA.GUIEventAdapter.KEY_F7 :
                    # F7 -- Toggle display of OQ test bounding volumes
                    _debug = !_debug
                    ddv = DebugDisplayVisitor( _debug )
                    _node.accept( ddv )
                    return True
                elif ea.getKey()==osgGA.GUIEventAdapter.KEY_F8 :
                    # F8 -- Gether stats and display
                    sv = StatisticsVisitor()
                    _node.accept( sv )
                    print "osgOQ: Stats: numOQNs ", sv.getNumOQNs(), ", numPased ", sv.getNumPassed()
                    return True
                elif ea.getKey()==osgGA.GUIEventAdapter.KEY_F9 :
                    # F9 -- Remove all OcclusionQueryNodes
                    roqv = RemoveOcclusionQueryVisitor()
                    _node.accept( roqv )
                    return True
                elif ea.getKey()=='o' :
                    if osgDB.writeNodeFile( _node, "saved_model.osgt" ) :
                        osg.notify( osg.ALWAYS ), "osgOQ: Wrote scene graph to \"saved_model.osgt\""
                    else :
                        osg.notify( osg.ALWAYS ), "osgOQ: Wrote failed for \"saved_model.osgt\""
                    return True
                return False
            default:
                break
        return False

    _node = osg.Node()

    bool _enable, _debug


# Create a cube with one side missing. This makes a great simple occluder.
def createBox():
    
    box = osg.Geode()

    state = box.getOrCreateStateSet()
    pm = osg.PolygonMode(
        osg.PolygonMode.FRONT_AND_BACK, osg.PolygonMode.FILL )
    state.setAttributeAndModes( pm,
        osg.StateAttribute.ON | osg.StateAttribute.PROTECTED )

    geom = deprecated_osg.Geometry()
    v = osg.Vec3Array()
    geom.setVertexArray( v.get() )

        x =  float( 0. )
        y =  float( 0. )
        z =  float( 0. )
        r =  float( 1.1 )

        v.push_back( osg.Vec3( x-r, y-r, z-r ) ) #left -X
        v.push_back( osg.Vec3( x-r, y-r, z+r ) )
        v.push_back( osg.Vec3( x-r, y+r, z+r ) )
        v.push_back( osg.Vec3( x-r, y+r, z-r ) )

        v.push_back( osg.Vec3( x+r, y-r, z+r ) ) #right +X
        v.push_back( osg.Vec3( x+r, y-r, z-r ) )
        v.push_back( osg.Vec3( x+r, y+r, z-r ) )
        v.push_back( osg.Vec3( x+r, y+r, z+r ) )

        v.push_back( osg.Vec3( x-r, y-r, z-r ) ) # bottom -Z
        v.push_back( osg.Vec3( x-r, y+r, z-r ) )
        v.push_back( osg.Vec3( x+r, y+r, z-r ) )
        v.push_back( osg.Vec3( x+r, y-r, z-r ) )

        v.push_back( osg.Vec3( x-r, y-r, z+r ) ) # top +Z
        v.push_back( osg.Vec3( x+r, y-r, z+r ) )
        v.push_back( osg.Vec3( x+r, y+r, z+r ) )
        v.push_back( osg.Vec3( x-r, y+r, z+r ) )

        v.push_back( osg.Vec3( x-r, y+r, z-r ) ) # back +Y
        v.push_back( osg.Vec3( x-r, y+r, z+r ) )
        v.push_back( osg.Vec3( x+r, y+r, z+r ) )
        v.push_back( osg.Vec3( x+r, y+r, z-r ) )

    c = osg.Vec4Array()
    geom.setColorArray( c.get() )
    geom.setColorBinding( deprecated_osg.Geometry.BIND_OVERALL )
    c.push_back( osg.Vec4( 0., 1., 1., 1. ) )

    n = osg.Vec3Array()
    geom.setNormalArray( n.get() )
    geom.setNormalBinding( deprecated_osg.Geometry.BIND_PER_PRIMITIVE )
    n.push_back( osg.Vec3( -1., 0., 0. ) )
    n.push_back( osg.Vec3( 1., 0., 0. ) )
    n.push_back( osg.Vec3( 0., 0., -1. ) )
    n.push_back( osg.Vec3( 0., 0., 1. ) )
    n.push_back( osg.Vec3( 0., 1., 0. ) )

    geom.addPrimitiveSet( osg.DrawArrays( GL_QUADS, 0, 20 ) )
    box.addDrawable( geom.get() )

    return box.get()

# Make a Geometry that renders slow intentionally.
# To make sure it renders slow, we do the following:
#  * Disable display lists
#  * Force glBegin/glEnd slow path
#  * Lots of vertices and color data per vertex
#  * No vertex sharing
#  * Draw the triangles as wireframe
def createRandomTriangles(num):
    
    tris = osg.Geode()

    ss = tris.getOrCreateStateSet()

    # Force wireframe. Many gfx cards handle this poorly.
    pm = osg.PolygonMode(
        osg.PolygonMode.FRONT_AND_BACK, osg.PolygonMode.LINE )
    ss.setAttributeAndModes( pm, osg.StateAttribute.ON |
        osg.StateAttribute.PROTECTED)
    ss.setMode( GL_LIGHTING, osg.StateAttribute.OFF |
        osg.StateAttribute.PROTECTED)

    geom = deprecated_osg.Geometry()
    # Disable display lists to decrease performance.
    geom.setUseDisplayList( False )

    v = osg.Vec3Array()
    geom.setVertexArray( v.get() )
    v.resize( num*3 )

    i = unsigned int()
    srand( 0 )
#define RAND_NEG1_TO_1 ( ((rand()%20)-10)*.1 )
    for (i=0 i<num i++)
        v0 = (*v)[ i*3+0 ]
        v1 = (*v)[ i*3+1 ]
        v2 = (*v)[ i*3+2 ]
        v0 = osg.Vec3( RAND_NEG1_TO_1, RAND_NEG1_TO_1, RAND_NEG1_TO_1 )
        v1 = osg.Vec3( RAND_NEG1_TO_1, RAND_NEG1_TO_1, RAND_NEG1_TO_1 )
        v2 = osg.Vec3( RAND_NEG1_TO_1, RAND_NEG1_TO_1, RAND_NEG1_TO_1 )

    c = osg.Vec4Array()
    geom.setColorArray( c.get() )
    # Bind per primitive to force slow glBegin/glEnd path.
    geom.setColorBinding( deprecated_osg.Geometry.BIND_PER_PRIMITIVE )
    c.resize( num )

#define RAND_0_TO_1 ( (rand()%10)*.1 )
    for (i=0 i<num i++)
        c0 = (*c)[ i ]
        c0 = osg.Vec4( RAND_0_TO_1, RAND_0_TO_1, RAND_0_TO_1, 1. )

    geom.addPrimitiveSet( osg.DrawArrays( GL_TRIANGLES, 0, num*3 ) )
    tris.addDrawable( geom.get() )

    return tris.get()

# Create the stock scene:
# Top level Group
#   Geode (simple occluder
#   OcclusionQueryNode
#     Geode with complex, slow geometry.
def createStockScene():
    
    # Create a simple box occluder
    root = osg.Group()
    root.addChild( createBox().get() )

    # Create a complex mess of triangles as a child below an
    #   OcclusionQueryNode. The OQN will ensure that the
    #   subgraph isn't rendered when it's not visible.
    oqn = osg.OcclusionQueryNode()
    oqn.addChild( createRandomTriangles( 20000 ).get() )
    root.addChild( oqn.get() )

    return root.get()


def main(argc, argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" demonstrates OpenGL occlusion query in OSG using the OcclusionQueryNode.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] [filename(s)]")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display command line parameters")

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout, osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    viewer = osgViewer.Viewer( arguments )

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    # add the help handler
    viewer.addEventHandler(osgViewer.HelpHandler(arguments.getApplicationUsage()))

    optimize = arguments.read( "--opt" )

    # load the specified model
    root = 0

    if arguments.argc()>1 :
        root = osgDB.readNodeFiles( arguments )
        if root.valid() :
            # Run a NodeVisitor to insert OcclusionQueryNodes in the scene graph.
            oqv = OcclusionQueryVisitor()
            root.accept( oqv )
        else :
            print arguments.getApplicationName(), ": unable to load specified data."
            return 1
    else :
        root = createStockScene().get()
        if !root :
            print arguments.getApplicationName(), ": Failed to create stock scene."
            return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1


    # optimize the scene graph, remove redundant nodes and state etc.
    if optimize :
        optimizer = osgUtil.Optimizer()
        optimizer.optimize( root.get() )

    viewer.setSceneData( root.get() )

    kh = KeyHandler( *root )
    viewer.addEventHandler( kh )

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
