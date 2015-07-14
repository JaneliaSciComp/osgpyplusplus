#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgfadetext"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgSim
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osgfadetext.cpp'

# OpenSceneGraph example, osgfadetext.
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

#include <osg/Group>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Texture2D>
#include <osg/PositionAttitudeTransform>
#include <osg/MatrixTransform>
#include <osg/CoordinateSystemNode>
#include <osg/ClusterCullingCallback>

#include <osgDB/FileUtils>
#include <osgDB/ReadFile>

#include <osgText/FadeText>

#include <osgSim/OverlayNode>
#include <osgSim/SphereSegment>

#include <osgGA/TerrainManipulator>

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
    

def createText(ellipsoid, latitude, longitude, height, str):

    
    double X,Y,Z
    ellipsoid.convertLatLongHeightToXYZ( osg.DegreesToRadians(latitude), osg.DegreesToRadians(longitude), height, X, Y, Z)


    text = osgText.FadeText()

    normal = ellipsoid.computeLocalUpVector( X, Y, Z)
    text.setCullCallback(osg.ClusterCullingCallback(osg.Vec3(X,Y,Z), normal, 0.0))

    text.setText(str)
    text.setFont("fonts/arial.ttf")
    text.setPosition(osg.Vec3(X,Y,Z))
    text.setCharacterSize(300000.0)
    text.setCharacterSizeMode(osgText.Text.OBJECT_COORDS_WITH_MAXIMUM_SCREEN_SIZE_CAPPED_BY_FONT_HEIGHT)
    text.setAutoRotateToScreen(True)
    
    return text

def createFadeText(ellipsoid):

    
    group = osg.Group()

    group.getOrCreateStateSet().setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
    
    geode = osg.Geode()
    group.addChild(geode)
    
    textList = std.vector<str>()
    textList.push_back("Town")
    textList.push_back("City")
    textList.push_back("Village")
    textList.push_back("River")
    textList.push_back("Mountain")
    textList.push_back("Road")
    textList.push_back("Lake")
    
    numLat = 15
    numLong = 20
    latitude = 0.0
    longitude = -100.0
    deltaLatitude = 1.0
    deltaLongitude = 1.0

    t = 0
    for(unsigned int i = 0 i < numLat ++i, latitude += deltaLatitude)
        lgnt = longitude
        for(unsigned int j = 0 j < numLong ++j, ++t, lgnt += deltaLongitude)
            geode.addDrawable( createText( ellipsoid, latitude, lgnt, 0, textList[t % textList.size()]) )

    return group


int main(int, char**)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    viewer.getCamera().setComputeNearFarMode(osg.CullSettings.COMPUTE_NEAR_FAR_USING_PRIMITIVES)
    viewer.getCamera().setNearFarRatio(0.00001)
    
    # read the scene from the list of file specified commandline args.
    root = createEarth()
    
    if  not root : return 0

    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData(root)

    csn = dynamic_cast<osg.CoordinateSystemNode*>(root)
    if csn :
        # add fade text around the globe
        csn.addChild(createFadeText(csn.getEllipsoidModel()))

    viewer.setCameraManipulator(osgGA.TerrainManipulator)()

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
