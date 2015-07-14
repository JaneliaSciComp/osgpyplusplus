#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgsimulation"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgParticle
from osgpypp import osgSim
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osgsimulation.cpp'

# OpenSceneGraph example, osgsimulation.
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

#ifdef WIN32
######################################/
# Disable unavoidable warning messages:

#  4103: used #pragma pack to change alignment
#  4114: same type qualifier used more than once
#  4201: nonstandard extension used : nameless struct/union
#  4237: "keyword" reserved for future use
#  4251: class needs to have dll-interface to export class
#  4275: non DLL-interface class used as base for DLL-interface class
#  4290: C++ Exception Specification ignored
#  4503: decorated name length exceeded, name was truncated
#  4786: string too long - truncated to 255 characters

#pragma warning(disable : 4103 4114 4201 4237 4251 4275 4290 4503 4335 4786)

#endif # WIN32

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osg/Group>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Texture2D>
#include <osg/PositionAttitudeTransform>
#include <osg/MatrixTransform>
#include <osg/CoordinateSystemNode>

#include <osgDB/FileUtils>
#include <osgDB/fstream>
#include <osgDB/ReadFile>

#include <osgText/Text>

#include <osg/CoordinateSystemNode>

#include <osgSim/OverlayNode>
#include <osgSim/SphereSegment>

#include <osgGA/NodeTrackerManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <osgParticle/FireEffect>

#include <iostream>

def createEarth():

    
    hints = osg.TessellationHints()
    hints.setDetailRatio(5.0)

    
    sd = osg.ShapeDrawable(osg.Sphere(osg.Vec3(0.0,0.0,0.0), osg.WGS_84_RADIUS_POLAR), hints)
    
    geode = osg.Geode()
    geode.addDrawable(sd)
    
    filename = osgDB.findDataFile("Images/land_shallow_topo_2048.jpg")
    geode.getOrCreateStateSet().setTextureAttributeAndModes(0, osg.Texture2D(osgDB.readImageFile(filename)))
    
    csn = osg.CoordinateSystemNode()
    csn.setEllipsoidModel(osg.EllipsoidModel())
    csn.addChild(geode)
    
    return csn
    


class ModelPositionCallback (osg.NodeCallback) :

    ModelPositionCallback(double speed):
        _latitude(0.0),
        _longitude(0.0),
        _height(100000.0),
        _speed(speed)
        _rotation.makeRotate(osg.DegreesToRadians(90.0),0.0,0.0,1.0)
    
    def updateParameters():
    
        
        _longitude += _speed * ((2.0*osg.PI)/360.0)/20.0


    virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
        updateParameters()
        
        nodePath = nv.getNodePath()

        mt =  0 : dynamic_cast<osg: if (nodePath.empty()) else MatrixTransform*>(nodePath.back())
        if mt :
            csn = 0

            # find coordinate system node from our parental chain
            i = unsigned int()
            for(i=0 i<nodePath.size()  and  csn==0 ++i)
                csn = dynamic_cast<osg.CoordinateSystemNode*>(nodePath[i])
            
            if csn :


                ellipsoid = csn.getEllipsoidModel()
                if ellipsoid :
                    inheritedMatrix = osg.Matrix()
                    for(i+=1 i<nodePath.size()-1 ++i)
                        transform = nodePath[i].asTransform()
                        if transform : transform.computeLocalToWorldMatrix(inheritedMatrix, nv)
                    
                    matrix = osg.Matrixd(inheritedMatrix)

                    #osg.Matrixd matrix
                    ellipsoid.computeLocalToWorldTransformFromLatLongHeight(_latitude,_longitude,_height,matrix)
                    matrix.preMultRotate(_rotation)
                    
                    mt.setMatrix(matrix)

            
        traverse(node,nv)
    
    _latitude = double()
    _longitude = double()
    _height = double()
    _rotation = osg.Quat()
    _speed = double()



class FindNamedNodeVisitor (osg.NodeVisitor) :
    FindNamedNodeVisitor( str name):
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _name(name) 
    
    def apply(node):
    
        
        if node.getName()==_name :
            _foundNodes.push_back(node)
        traverse(node)
    
    typedef std.vector< osg.Node > NodeList

    _name = str()
    _foundNodes = NodeList()



def main(argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)
    
    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use of node tracker.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName())
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    
    # add the thread model handler
    viewer.addEventHandler(osgViewer.ThreadingHandler)()

    # add the window size toggle handler
    viewer.addEventHandler(osgViewer.WindowSizeHandler)()
        
    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()
        
    # add the record camera path  handler
    viewer.addEventHandler(osgViewer.RecordCameraPathHandler)()

    # add the help handler
    viewer.addEventHandler(osgViewer.HelpHandler(arguments.getApplicationUsage()))

    # set the near far ration computation up.
    viewer.getCamera().setComputeNearFarMode(osg.CullSettings.COMPUTE_NEAR_FAR_USING_PRIMITIVES)
    viewer.getCamera().setNearFarRatio(0.000003)


    speed = 1.0
    while arguments.read("-f")  or  arguments.read("--fixed") : speed = 0.0


    rotation = osg.Quat()
    vec4 = osg.Vec4()
    while arguments.read("--rotate-model",vec4[0],vec4[1],vec4[2],vec4[3]) :
        local_rotate = osg.Quat()
        local_rotate.makeRotate(osg.DegreesToRadians(vec4[0]),vec4[1],vec4[2],vec4[3])
        
        rotation = rotation * local_rotate

    nc = 0
    flightpath_filename = str()
    while arguments.read("--flight-path",flightpath_filename) :
        fin = osgDB.ifstream(flightpath_filename.c_str())
        if fin :
            path = osg.AnimationPath()
            path.read(fin)
            nc = osg.AnimationPathCallback(path)
    
    trackerMode = osgGA.NodeTrackerManipulator.NODE_CENTER_AND_ROTATION
    mode = str()
    while arguments.read("--tracker-mode",mode) :
        if mode=="NODE_CENTER_AND_ROTATION" : trackerMode = osgGA.NodeTrackerManipulator.NODE_CENTER_AND_ROTATION
        elif mode=="NODE_CENTER_AND_AZIM" : trackerMode = osgGA.NodeTrackerManipulator.NODE_CENTER_AND_AZIM
        elif mode=="NODE_CENTER" : trackerMode = osgGA.NodeTrackerManipulator.NODE_CENTER
        else:
            print "Unrecognized --tracker-mode option ", mode, ", valid options are:"
            print "    NODE_CENTER_AND_ROTATION"
            print "    NODE_CENTER_AND_AZIM"
            print "    NODE_CENTER"
            return 1
    
    
    rotationMode = osgGA.NodeTrackerManipulator.TRACKBALL
    while arguments.read("--rotation-mode",mode) :
        if mode=="TRACKBALL" : rotationMode = osgGA.NodeTrackerManipulator.TRACKBALL
        elif mode=="ELEVATION_AZIM" : rotationMode = osgGA.NodeTrackerManipulator.ELEVATION_AZIM
        else:
            print "Unrecognized --rotation-mode option ", mode, ", valid options are:"
            print "    TRACKBALL"
            print "    ELEVATION_AZIM"
            return 1

    useOverlay = True
    while arguments.read("--no-overlay")  or  arguments.read("-n") : useOverlay = False
    
    technique = osgSim.OverlayNode.OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY
    while arguments.read("--object") : technique = osgSim.OverlayNode.OBJECT_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY
    while arguments.read("--ortho")  or  arguments.read("--orthographic") : technique = osgSim.OverlayNode.VIEW_DEPENDENT_WITH_ORTHOGRAPHIC_OVERLAY
    while arguments.read("--persp")  or  arguments.read("--perspective") : technique = osgSim.OverlayNode.VIEW_DEPENDENT_WITH_PERSPECTIVE_OVERLAY

    overlayTextureUnit = 1
    while arguments.read("--unit", overlayTextureUnit) : 
    
    pathfile = str()
    while arguments.read("-p",pathfile) : 

    addFireEffect = arguments.read("--fire")

    # if user request help write it out to cout.
    if arguments.read("-h")  or  arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1
    
    
    tm = osgGA.NodeTrackerManipulator()
    
    overlayFilename = str()
    while arguments.read("--overlay", overlayFilename) : 

    # read the scene from the list of file specified commandline args.
    root = osgDB.readNodeFiles(arguments)

    if  not root : root = createEarth()

    if  not root : return 0


    if  not overlayFilename.empty() :
        #osg.Object *pObj = osgDB.readObjectFile("alaska_clean.shp")
        #osg.Geode shapefile = dynamic_cast<osg.Geode*> (pObj)
        #
        #ConvertLatLon2EllipsoidCoordinates latlon2em
        #shapefile.accept(latlon2em)

        shapefile = osgDB.readNodeFile(overlayFilename)
        
        if  not shapefile :
            osg.notify(osg.NOTICE), "File `", overlayFilename, "` not found"
            return 1

        csn = dynamic_cast<osg.CoordinateSystemNode*>(root)
        if csn :

            overlayNode = osgSim.OverlayNode(technique)
            overlayNode.getOrCreateStateSet().setTextureAttribute(1, osg.TexEnv(osg.TexEnv.DECAL))
            overlayNode.setOverlaySubgraph(shapefile)
            overlayNode.setOverlayTextureSizeHint(1024)
            overlayNode.setOverlayTextureUnit(overlayTextureUnit)

            # insert the OverlayNode between the coordinate system node and its children.
            for(unsigned int i=0 i<csn.getNumChildren() ++i)
                overlayNode.addChild( csn.getChild(i) )

            csn.removeChildren(0, csn.getNumChildren())
            csn.addChild(overlayNode)

            viewer.setSceneData(csn)
        else:
            overlayNode = osgSim.OverlayNode(technique)
            overlayNode.getOrCreateStateSet().setTextureAttribute(1, osg.TexEnv(osg.TexEnv.DECAL))
            overlayNode.setOverlaySubgraph(shapefile)
            overlayNode.setOverlayTextureSizeHint(1024)
            overlayNode.addChild(root)

            viewer.setSceneData(overlayNode)
    else:
    

        # add a viewport to the viewer and attach the scene graph.
        viewer.setSceneData(root)

        csn = dynamic_cast<osg.CoordinateSystemNode*>(root)
        if csn :

            overlayNode = osgSim.OverlayNode()
            if useOverlay :
                overlayNode = osgSim.OverlayNode(technique)

                # insert the OverlayNode between the coordinate system node and its children.
                for(unsigned int i=0 i<csn.getNumChildren() ++i)
                    overlayNode.addChild( csn.getChild(i) )

                csn.removeChildren(0, csn.getNumChildren())
                csn.addChild(overlayNode)

                # tell the overlay node to continously update its overlay texture
                # as we know we'll be tracking a moving target.
                overlayNode.setContinuousUpdate(True)


            cessna = osgDB.readNodeFile("cessna.osgt")
            if cessna :
                s = 200000.0 / cessna.getBound().radius()

                scaler = osg.MatrixTransform()
                scaler.addChild(cessna)
                scaler.setMatrix(osg.Matrixd.scale(s,s,s)*osg.Matrixd.rotate(rotation))
                scaler.getOrCreateStateSet().setMode(GL_RESCALE_NORMAL,osg.StateAttribute.ON)
                
                if addFireEffect :
                    center = cessna.getBound().center()
                    
                    fire = osgParticle.FireEffect(center, 10.0)
                    scaler.addChild(fire)
                

                if False :
                    ss = osgSim.SphereSegment(
                                        osg.Vec3(0.0,0.0,0.0), # center
                                        19.9, # radius
                                        osg.DegreesToRadians(135.0),
                                        osg.DegreesToRadians(240.0),
                                        osg.DegreesToRadians(-10.0),
                                        osg.DegreesToRadians(30.0),
                                        60)

                    scaler.addChild(ss)

                mt = osg.MatrixTransform()
                mt.addChild(scaler)


                if  not nc : nc = ModelPositionCallback(speed)

                mt.setUpdateCallback(nc)

                csn.addChild(mt)

                # if we are using an overaly node, use the cessna subgraph as the overlay subgraph
                if overlayNode.valid() :
                    overlayNode.setOverlaySubgraph(mt)

                tm = osgGA.NodeTrackerManipulator()
                tm.setTrackerMode(trackerMode)
                tm.setRotationMode(rotationMode)
                tm.setTrackNode(scaler)
            else:
                 print "Failed to read cessna.osgt"


    # set up camera manipulators.
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        if tm.valid() : keyswitchManipulator.addMatrixManipulator( ord("0"), "NodeTracker", tm )

        keyswitchManipulator.addMatrixManipulator( ord("1"), "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("2"), "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("3"), "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("4"), "Terrain", osgGA.TerrainManipulator() )

        if  not pathfile.empty() :
            apm = osgGA.AnimationPathManipulator(pathfile)
            if apm  or   not apm.valid() : 
                num = keyswitchManipulator.getNumMatrixManipulators()
                keyswitchManipulator.addMatrixManipulator( ord("5"), "Path", apm )
                keyswitchManipulator.selectMatrixManipulator(num)

        viewer.setCameraManipulator( keyswitchManipulator )

    # viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
