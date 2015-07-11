#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osglauncher"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osglauncher.cpp'

# OpenSceneGraph example, osglauncher.
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

##include <cstdio>
##include <cstdlib>
#include <iostream>
#include <list>
#include <string>
#include <sstream>

#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Material>
#include <osg/Texture2D>
#include <osg/Geometry>
#include <osg/MatrixTransform>
#include <osg/PositionAttitudeTransform>
#include <osg/BlendFunc>
#include <osg/ClearNode>
#include <osg/Depth>
#include <osg/Projection>
#include <osg/io_utils>

#include <osgUtil/CullVisitor>
#include <osgUtil/Optimizer>

#include <osgText/Text>

#include <osgGA/TrackballManipulator>

#include <osgViewer/Viewer>

#include <osgDB/ReadFile>
#include <osgDB/FileUtils>
#include <osgDB/fstream>

runApp = int(str xapp)

# class to handle events with a pick
class PickHandler (osgGA.GUIEventHandler) : 

    PickHandler(osgViewer.Viewer* viewer,osgText.Text* updateText):
        _viewer(viewer),
        _updateText(updateText) 
        
    ~PickHandler() 
    
    handle = bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter us)

    pick = str( osgGA.GUIEventAdapter event)
    
    def highlight(name):
    
        
        if _updateText.get() : _updateText.setText(name)

    _viewer = osgViewer.Viewer*()
    _updateText = osgText.Text()


bool PickHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
    switch(ea.getEventType())
    case(osgGA.GUIEventAdapter.FRAME):
    case(osgGA.GUIEventAdapter.MOVE):
        # osg.notify(osg.NOTICE), "MOVE ", ea.getX(), ", ", ea.getY()
        picked_name = pick(ea)
        highlight(picked_name)
        return False
    case(osgGA.GUIEventAdapter.PUSH):
        # osg.notify(osg.NOTICE), "PUSH ", ea.getX(), ", ", ea.getY()
        picked_name = pick(ea)
        if !picked_name.empty() :
            runApp(picked_name)
            return True
        else :
            return False
    default:
        return False


str PickHandler.pick( osgGA.GUIEventAdapter event)
    intersections = osgUtil.LineSegmentIntersector.Intersections()
    if _viewer.computeIntersections(event, intersections) :
        for(osgUtil.LineSegmentIntersector.Intersections.iterator hitr = intersections.begin()
            hitr != intersections.end()
            ++hitr)
            node = hitr.nodePath.empty() ? 0 : hitr.nodePath.back()
            if node  !node.getName().empty() : return node.getName()

    return ""

def createHUD(updateText):

        # create the hud. derived from osgHud.cpp
    # adds a set of quads, each in a separate Geode - which can be picked individually
    # eg to be used as a menuing/help system!
    # Can pick texts too!
    modelview_abs = osg.MatrixTransform()
    modelview_abs.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    modelview_abs.setMatrix(osg.Matrix.identity())
    
    projection = osg.Projection()
    projection.setMatrix(osg.Matrix.ortho2D(0,1280,0,1024))
    projection.addChild(modelview_abs)
    
    
    timesFont = str("fonts/times.ttf")
    
    # turn lighting off for the text and disable depth test to ensure its always ontop.
    position = osg.Vec3(50.0,510.0,0.0)
    delta = osg.Vec3(0.0,-60.0,0.0)

     # this displays what has been selected
        geode = osg.Geode()
        stateset = geode.getOrCreateStateSet()
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
        stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
        geode.setName("The text label")
        geode.addDrawable( updateText )
        modelview_abs.addChild(geode)
        
        updateText.setCharacterSize(20.0)
        updateText.setFont(timesFont)
        updateText.setColor(osg.Vec4(1.0,1.0,0.0,1.0))
        updateText.setText("")
        updateText.setPosition(position)
        
        position += delta
    
    return projection

 # end create HUDf




static osg.Vec3 defaultPos( 0.0, 0.0, 0.0 )
static osg.Vec3 centerScope(0.0, 0.0, 0.0)

class Xample :
texture = str()
    app = str()
      Xample(str image, str prog)
        texture    = image
        app     = prog
        osg.notify(osg.INFO), "New Xample!"
    
    ~Xample()  
    
    def getTexture():
    
        
        return texture
    def getApp():
        
        return app
      Xample() 
 # end class Xample


typedef std.list<Xample>.iterator OP
static std.list<Xample> Xamplelist


def printList():


    
    osg.notify(osg.INFO), "start printList()"
    for (OP i = Xamplelist.begin()  i != Xamplelist.end()  ++i)
        x = *i
        osg.notify(osg.INFO), "current x.texture = ", x.getTexture()
        osg.notify(osg.INFO), "current x.app = ", x.getApp()
    osg.notify(osg.INFO), "end printList()"
 # end printList()


def runApp(xapp):


    
    osg.notify(osg.INFO), "start runApp()"
    for (OP i = Xamplelist.begin()  i != Xamplelist.end()  ++i)
        x = *i
        if !xapp.compare(x.getApp()) :
            osg.notify(osg.INFO), "app found!"
            
            cxapp = xapp.c_str()
            
            osg.notify(osg.INFO), "char* = ", cxapp
            
            system = return(cxapp)
    osg.notify(osg.INFO), "app not found!"
    return 1
 # end printList()


void readConfFile( char* confFile)                                                                # read confFile            1
    osg.notify(osg.INFO), "Start reading confFile"
    
    fileName = osgDB.findDataFile(confFile)
    if fileName.empty() :
        osg.notify(osg.INFO), "Config file not found", confFile
        return
    

    in = osgDB.ifstream(fileName.c_str())
    if !in :
        osg.notify(osg.INFO), "File ", fileName, " can not be opened!"
        exit(1)
    imageBuffer = str()
    appBuffer = str()
    
    while !in.eof() :
        std.getline(in, imageBuffer)
        std.getline(in, appBuffer)
        if imageBuffer == "" || appBuffer == "" :
        else :
            osg.notify(osg.INFO), "imageBuffer: ", imageBuffer
            osg.notify(osg.INFO), "appBuffer: ", appBuffer
#            jeweils checken ob image vorhanden ist.
            
            tmp = Xample(imageBuffer, appBuffer)                                                    # create Xample objects    2
            
            Xamplelist.push_back(tmp)                                                            # store objects in list    2
            
    
    in.close()
    
    osg.notify(osg.INFO), "End reading confFile"
    
    printList()
 # end readConfFile


def SetObjectTextureState(geodeCurrent, texture):


    
    # retrieve or create a StateSet
    stateTexture = geodeCurrent.getOrCreateStateSet()

    # load texture.jpg as an image
    imgTexture = osgDB.readImageFile( texture )
    
    # if the image is successfully loaded
    if imgTexture :
        # create a two-dimensional texture object
        texCube = osg.Texture2D()

        # set the texture to the loaded image
        texCube.setImage(imgTexture)

        # set the texture to the state
        stateTexture.setTextureAttributeAndModes(0,texCube,osg.StateAttribute.ON)

        # set the state of the current geode
        geodeCurrent.setStateSet(stateTexture)
 # end SetObjectTextureState


def createTexturedCube(fRadius, vPosition, texture, geodeName):


    
    # create a cube shape
    bCube = osg.Box(vPosition,fRadius)
    # osg.Box *bCube = osg.Box(vPosition,fRadius)

    # create a container that makes the cube drawable
    sdCube = osg.ShapeDrawable(bCube)

    # create a geode object to as a container for our drawable cube object
    geodeCube = osg.Geode()
    geodeCube.setName( geodeName )

    # set the object texture state
    SetObjectTextureState(geodeCube, texture)

    # add our drawable cube to the geode container
    geodeCube.addDrawable(sdCube)

    return(geodeCube)
 # end CreateCube


def getPATransformation(object, position, scale, pivot):


    
    tmpTrans = osg.PositionAttitudeTransform()
    tmpTrans.addChild( object )
    
    tmpTrans.setPosition( position )
    tmpTrans.setScale( scale )
    tmpTrans.setPivotPoint( pivot )
    
    return tmpTrans

def printBoundings(current, name):

    
    currentBound = current.getBound()
    osg.notify(osg.INFO), name
    osg.notify(osg.INFO), "center = ", currentBound.center()
    osg.notify(osg.INFO), "radius = ", currentBound.radius()
    
#    return currentBound.radius()


osg.Group* setupGraph()                                                                        # create Geodes/Nodes from Xamplelist    3
    xGroup = osg.Group()

    
#    positioning and sizes
    defaultRadius = 0.8

    itemsInLine = 4                                    # name says everything
    offset = 0.05
    bs = (defaultRadius / 4) + offset
    xstart = (3*bs) * (-1)
    zstart = xstart * (-1)
    xnext = xstart
    znext = zstart
    xjump = (2*bs)
    zjump = xjump
    vScale = osg.Vec3( 0.5, 0.5, 0.5 )
    vPivot = osg.Vec3( 0.0, 0.0, 0.0 )    

#  run through Xampleliste
    z = 1
    for (OP i = Xamplelist.begin()  i != Xamplelist.end()  ++i, ++z)
        x = *i
        
        tmpCube = createTexturedCube(defaultRadius, defaultPos, x.getTexture(), x.getApp())
        printBoundings(tmpCube, x.getApp())
        vPosition = osg.Vec3( xnext, 0.0, znext )
        transX = getPATransformation(tmpCube, vPosition, vScale, vPivot)
        xGroup.addChild( transX )
        
        # line feed
        if z < itemsInLine :
            xnext += xjump
        else :
            xnext = xstart
            znext -= zjump
            z = 0
     # end run through list    
    
    return xGroup
 # end setupGraph


def main(argc, argv):


    
    if argc<=1 :
        readConfFile("osg.conf")                                                                          # read ConfigFile        1
    else :
        readConfFile(argv[1])                                                                          # read ConfigFile        1
    
    # construct the viewer.
    viewer = osgViewer.Viewer()

    updateText = osgText.Text()
    updateText.setDataVariance(osg.Object.DYNAMIC)

    # add the handler for doing the picking
    viewer.addEventHandler(PickHandler(viewer,updateText.get()))

    root = osg.Group()

    root.addChild( setupGraph() )

    # add the HUD subgraph.    
    root.addChild(createHUD(updateText.get()))
   
    # add model to viewer.
    viewer.setSceneData( root )

    lookAt = osg.Matrix()
    lookAt.makeLookAt(osg.Vec3(0.0, -4.0, 0.0), centerScope, osg.Vec3(0.0, 0.0, 1.0))

    viewer.getCamera().setViewMatrix(lookAt)
        
    viewer.realize()

    while  !viewer.done()  :
        # fire off the cull and draw traversals of the scene.
        viewer.frame()        

    return 0
 # end main


if __name__ == "__main__":
    main(sys.argv)
