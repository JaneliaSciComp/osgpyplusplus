#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgplanets"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgplanets.
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


# details about distances and rotation on http:#www.solarviews.com/eng/solarsys.htm 

#include <iostream>

#include <osg/Notify>
#include <osg/MatrixTransform>
#include <osg/PositionAttitudeTransform>
#include <osg/Geometry>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/Texture2D>
#include <osg/Material>
#include <osg/Light>
#include <osg/LightSource>
#include <osg/LightModel>
#include <osg/Billboard>
#include <osg/LineWidth>
#include <osg/TexEnv>
#include <osg/TexEnvCombine>
#include <osg/ClearNode>


#include <osgUtil/Optimizer>

#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>


#include <osgGA/NodeTrackerManipulator>
#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>

#include <osgViewer/Viewer>


static osg.Vec3 defaultPos( 0.0f, 0.0f, 0.0f )
static osg.Vec3 centerScope(0.0f, 0.0f, 0.0f)


#* create quad at specified position. 
def createSquare(corner, width, height, image):
    # set up the Geometry.
    geom =  new osg.Geometry

    coords =  new osg.Vec3Array(4)
    (*coords)[0] = corner
    (*coords)[1] = corner+width
    (*coords)[2] = corner+width+height
    (*coords)[3] = corner+height


    geom.setVertexArray(coords)

    norms =  new osg.Vec3Array(1)
    (*norms)[0] = width^height
    (*norms)[0].normalize()

    geom.setNormalArray(norms, osg.Array.BIND_OVERALL)

    tcoords =  new osg.Vec2Array(4)
    (*tcoords)[0].set(0.0f,0.0f)
    (*tcoords)[1].set(1.0f,0.0f)
    (*tcoords)[2].set(1.0f,1.0f)
    (*tcoords)[3].set(0.0f,1.0f)
    geom.setTexCoordArray(0,tcoords)

    colours =  new osg.Vec4Array(1)
    (*colours)[0].set(1.0f,1.0f,1.0f,1.0f)
    geom.setColorArray(colours, osg.Array.BIND_OVERALL)


    geom.addPrimitiveSet(new osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4))

    if image :
        stateset =  new osg.StateSet
        texture =  new osg.Texture2D
        texture.setImage(image)
        stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)
        stateset.setMode(GL_LIGHTING, osg.StateAttribute.OFF)
        stateset.setMode(GL_BLEND, osg.StateAttribute.ON)
        stateset.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)
        geom.setStateSet(stateset)

    geom = return()

osg.Image* createBillboardImage( osg.Vec4 centerColour, unsigned int size, float power)
    backgroundColour =  centerColour
    backgroundColour[3] = 0.0f

    image =  new osg.Image
    image.allocateImage(size,size,1,
                         GL_RGBA,GL_UNSIGNED_BYTE)


    mid =  (float(size)-1)*0.5f
    div =  2.0f/float(size)
    for(unsigned int r=0r<size++r)
        unsigned char* ptr = image.data(0,r,0)
        for(unsigned int c=0c<size++c)
            dx =  (float(c) - mid)*div
            dy =  (float(r) - mid)*div
            r =  powf(1.0f-sqrtf(dx*dx+dy*dy),power)
            if r<0.0f : r=0.0f
            color =  centerColour*r+backgroundColour*(1.0f-r)
            # color.set(1.0f,1.0f,1.0f,0.5f)
            *ptr++ = (unsigned char)((color[0])*255.0f)
            *ptr++ = (unsigned char)((color[1])*255.0f)
            *ptr++ = (unsigned char)((color[2])*255.0f)
            *ptr++ = (unsigned char)((color[3])*255.0f)
    image = return()

    #return osgDB.readImageFile("spot.dds")

def createAnimationPath(center, radius, looptime):
    # set up the animation path
    animationPath =  new osg.AnimationPath
    animationPath.setLoopMode(osg.AnimationPath.LOOP)

    numSamples =  1000
    yaw =  0.0f
    yaw_delta =  -2.0f*osg.PI/((float)numSamples-1.0f)
    roll =  osg.inDegrees(30.0f)

    time = 0.0f
    time_delta =  looptime/(double)numSamples
    for(int i=0i<numSamples++i)
        position = osg.Vec3(center+osg.Vec3(sinf(yaw)*radius,cosf(yaw)*radius,0.0f))
        rotation = osg.Quat(osg.Quat(roll,osg.Vec3(0.0,1.0,0.0))*osg.Quat(-(yaw+osg.inDegrees(90.0f)),osg.Vec3(0.0,0.0,1.0)))

        animationPath.insert(time,osg.AnimationPath.ControlPoint(position,rotation))

        yaw += yaw_delta
        time += time_delta

    animationPath = return()
# end createAnimationPath


class SolarSystem

public:
    _radiusSpace = double()
    _radiusSun = double()
    _radiusMercury = double()
    _radiusVenus = double()
    _radiusEarth = double()
    _radiusMoon = double()
    _radiusMars = double()
    _radiusJupiter = double()

    _RorbitMercury = double()
    _RorbitVenus = double()
    _RorbitEarth = double()
    _RorbitMoon = double()
    _RorbitMars = double()
    _RorbitJupiter = double()

    _rotateSpeedSun = double()
    _rotateSpeedMercury = double()
    _rotateSpeedVenus = double()
    _rotateSpeedEarthAndMoon = double()
    _rotateSpeedEarth = double()
    _rotateSpeedMoon = double()
    _rotateSpeedMars = double()
    _rotateSpeedJupiter = double()

    _tiltEarth = double()

    _mapSpace = str()
    _mapSun = str()
    _mapVenus = str()
    _mapMercury = str()
    _mapEarth = str()
    _mapEarthNight = str()
    _mapMoon = str()
    _mapMars = str()
    _mapJupiter = str()

    _rotateSpeedFactor = double()
    _RorbitFactor = double()
    _radiusFactor = double()

    SolarSystem()
        _radiusSpace    = 500.0
        _radiusSun      = 109.0
        _radiusMercury  = 0.38
        _radiusVenus    = 0.95
        _radiusEarth    = 1.0
        _radiusMoon     = 0.1
        _radiusMars     = 0.53
        _radiusJupiter  = 5.0

        _RorbitMercury  = 11.7
        _RorbitVenus    = 21.6
        _RorbitEarth    = 30.0
        _RorbitMoon     = 1.0
        _RorbitMars     = 45.0
        _RorbitJupiter  = 156.0

                                                # orbital period in days
        _rotateSpeedSun             = 0.0      # should be 11.97  # 30.5 average
        _rotateSpeedMercury         = 4.15     # 87.96
        _rotateSpeedVenus           = 1.62     # 224.70
        _rotateSpeedEarthAndMoon    = 1.0      # 365.25
        _rotateSpeedEarth           = 1.0      #
        _rotateSpeedMoon            = 0.95     #
        _rotateSpeedMars            = 0.53     # 686.98
        _rotateSpeedJupiter         = 0.08     # 4332.71

        _tiltEarth                  = 23.45 # degrees

        _mapSpace       = "Images/spacemap2.jpg"
        _mapSun         = "SolarSystem/sun256128.jpg"
        _mapMercury     = "SolarSystem/mercury256128.jpg"
        _mapVenus       = "SolarSystem/venus256128.jpg"
        _mapEarth       = "Images/land_shallow_topo_2048.jpg"
        _mapEarthNight  = "Images/land_ocean_ice_lights_2048.jpg"
        _mapMoon        = "SolarSystem/moon256128.jpg"
        _mapMars        = "SolarSystem/mars256128.jpg"
        _mapJupiter     = "SolarSystem/jupiter256128.jpg"

        _rotateSpeedFactor = 0.5
        _RorbitFactor   = 15.0
        _radiusFactor   = 10.0

    createTranslationAndTilt = osg.MatrixTransform*( double translation, double tilt )
    createRotation = osg.MatrixTransform*( double orbit, double speed )

    createSpace = osg.Geode*(  str name,  str textureName )
    createPlanet = osg.Geode*( double radius,  str name,  osg.Vec4 color ,  str textureName )
    createPlanet = osg.Geode*( double radius,  str name,  osg.Vec4 color ,  str textureName1,  str textureName2)
    createSunLight = osg.Group*()

    def rotateSpeedCorrection():
        _rotateSpeedSun             *= _rotateSpeedFactor
        _rotateSpeedMercury         *= _rotateSpeedFactor
        _rotateSpeedVenus           *= _rotateSpeedFactor
        _rotateSpeedEarthAndMoon    *= _rotateSpeedFactor
        _rotateSpeedEarth           *= _rotateSpeedFactor
        _rotateSpeedMoon            *= _rotateSpeedFactor
        _rotateSpeedMars            *= _rotateSpeedFactor
        _rotateSpeedJupiter         *= _rotateSpeedFactor

        print "rotateSpeed corrected by factor ", _rotateSpeedFactor

    def RorbitCorrection():
        _RorbitMercury  *= _RorbitFactor
        _RorbitVenus    *= _RorbitFactor
        _RorbitEarth    *= _RorbitFactor
        _RorbitMoon     *= _RorbitFactor
        _RorbitMars     *= _RorbitFactor
        _RorbitJupiter  *= _RorbitFactor

        print "Rorbits corrected by factor ", _RorbitFactor

    def radiusCorrection():
        _radiusSpace    *= _radiusFactor
        #_radiusSun      *= _radiusFactor
        _radiusMercury  *= _radiusFactor
        _radiusVenus    *= _radiusFactor
        _radiusEarth    *= _radiusFactor
        _radiusMoon     *= _radiusFactor
        _radiusMars     *= _radiusFactor
        _radiusJupiter  *= _radiusFactor

        print "Radius corrected by factor ", _radiusFactor
    printParameters = void()

  # end SolarSystem

class FindNamedNodeVisitor : public osg.NodeVisitor
public:
    FindNamedNodeVisitor( str name):
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN),
        _name(name) 

    virtual void apply(osg.Node node)
        if node.getName()==_name :
            _foundNodes.push_back(node)
        traverse(node)

    typedef std.vector< osg.ref_ptr<osg.Node> > NodeList

    _name = str()
    _foundNodes = NodeList()



osg.MatrixTransform* SolarSystem.createRotation( double orbit, double speed )
    center = osg.Vec3( 0.0, 0.0, 0.0 )
    animationLength =  10.0f
    animationPath =  createAnimationPath( center, orbit, animationLength )

    rotation =  new osg.MatrixTransform
    rotation.setUpdateCallback( new osg.AnimationPathCallback( animationPath, 0.0f, speed ) )

    rotation = return()
# end SolarSystem.createEarthRotation


osg.MatrixTransform* SolarSystem.createTranslationAndTilt( double #translation, double tilt )
    moonPositioned =  new osg.MatrixTransform
    moonPositioned.setMatrix(osg.Matrix.translate(osg.Vec3( 0.0, _RorbitMoon, 0.0 ) )*
                                 osg.Matrix.scale(1.0, 1.0, 1.0)*
                                 osg.Matrix.rotate(osg.inDegrees( tilt ),0.0f,0.0f,1.0f))

    moonPositioned = return()
# end SolarSystem.createTranslationAndTilt


osg.Geode* SolarSystem.createSpace(  str name,  str textureName )
    spaceSphere =  new osg.Sphere( osg.Vec3( 0.0, 0.0, 0.0 ), _radiusSpace )

    sSpaceSphere =  new osg.ShapeDrawable( spaceSphere )

    if  !textureName.empty()  :
        image =  osgDB.readImageFile( textureName )
        if  image  :
            sSpaceSphere.getOrCreateStateSet().setTextureAttributeAndModes( 0, new osg.Texture2D( image ), osg.StateAttribute.ON )

            # reset the object color to white to allow the texture to set the colour.
            sSpaceSphere.setColor( osg.Vec4(1.0f,1.0f,1.0f,1.0f) )

    geodeSpace =  new osg.Geode()
    geodeSpace.setName( name )

    geodeSpace.addDrawable( sSpaceSphere )

    return( geodeSpace )

# end SolarSystem.createSpace


osg.Geode* SolarSystem.createPlanet( double radius,  str name,  osg.Vec4 color ,  str textureName)
    # create a container that makes the sphere drawable
    sPlanetSphere =  new osg.Geometry()

        # set the single colour so bind overall
        colours =  new osg.Vec4Array(1)
        (*colours)[0] = color
        sPlanetSphere.setColorArray(colours, osg.Array.BIND_OVERALL)


        # now set up the coords, normals and texcoords for geometry
        unsigned int numX = 100
        unsigned int numY = 50
        unsigned int numVertices = numX*numY

        coords =  new osg.Vec3Array(numVertices)
        sPlanetSphere.setVertexArray(coords)

        normals =  new osg.Vec3Array(numVertices)
        sPlanetSphere.setNormalArray(normals, osg.Array.BIND_PER_VERTEX)

        texcoords =  new osg.Vec2Array(numVertices)
        sPlanetSphere.setTexCoordArray(0,texcoords)
        sPlanetSphere.setTexCoordArray(1,texcoords)

        delta_elevation =  osg.PI / (double)(numY-1)
        delta_azim =  2.0*osg.PI / (double)(numX-1)
        delta_tx =  1.0 / (float)(numX-1)
        delta_ty =  1.0 / (float)(numY-1)

        elevation =  -osg.PI*0.5
        ty =  0.0
        unsigned int vert = 0
        j = unsigned()
        for(j=0
            j<numY
            ++j, elevation+=delta_elevation, ty+=delta_ty )
            azim =  0.0
            tx =  0.0
            for(unsigned int i=0
                i<numX
                ++i, ++vert, azim+=delta_azim, tx+=delta_tx)
                direction = osg.Vec3(cos(azim)*cos(elevation), sin(azim)*cos(elevation), sin(elevation))
                (*coords)[vert].set(direction*radius)
                (*normals)[vert].set(direction)
                (*texcoords)[vert].set(tx,ty)

        for(j=0
            j<numY-1
            ++j)
            unsigned int curr_row = j*numX
            unsigned int next_row = curr_row+numX
            elements =  new osg.DrawElementsUShort(GL_QUAD_STRIP)
            for(unsigned int i=0
                i<numX
                ++i)
                elements.push_back(next_row + i)
                elements.push_back(curr_row + i)
            sPlanetSphere.addPrimitiveSet(elements)


    # set the object color
    #sPlanetSphere.setColor( color )

    # create a geode object to as a container for our drawable sphere object
    geodePlanet =  new osg.Geode()
    geodePlanet.setName( name )

    if  !textureName.empty()  :
        image =  osgDB.readImageFile( textureName )
        if  image  :
            tex2d =  new osg.Texture2D( image )
            tex2d.setWrap( osg.Texture.WRAP_S, osg.Texture.REPEAT )
            tex2d.setWrap( osg.Texture.WRAP_T, osg.Texture.REPEAT )
            geodePlanet.getOrCreateStateSet().setTextureAttributeAndModes( 0, tex2d, osg.StateAttribute.ON )

            # reset the object color to white to allow the texture to set the colour.
            #sPlanetSphere.setColor( osg.Vec4(1.0f,1.0f,1.0f,1.0f) )

    # add our drawable sphere to the geode container
    geodePlanet.addDrawable( sPlanetSphere )

    return( geodePlanet )

# end SolarSystem.createPlanet

osg.Geode* SolarSystem.createPlanet( double radius,  str name,  osg.Vec4 color ,  str textureName1,  str textureName2)
    geodePlanet =  createPlanet( radius, name, color , textureName1)

    if  !textureName2.empty()  :
        image =  osgDB.readImageFile( textureName2 )
        if  image  :
            stateset =  geodePlanet.getOrCreateStateSet()

            texenv =  new osg.TexEnvCombine

            texenv.setCombine_RGB(osg.TexEnvCombine.INTERPOLATE)
            texenv.setSource0_RGB(osg.TexEnvCombine.PREVIOUS)
            texenv.setOperand0_RGB(osg.TexEnvCombine.SRC_COLOR)
            texenv.setSource1_RGB(osg.TexEnvCombine.TEXTURE)
            texenv.setOperand1_RGB(osg.TexEnvCombine.SRC_COLOR)
            texenv.setSource2_RGB(osg.TexEnvCombine.PRIMARY_COLOR)
            texenv.setOperand2_RGB(osg.TexEnvCombine.SRC_COLOR)

            stateset.setTextureAttribute( 1, texenv )
            tex2d =  new osg.Texture2D( image )
            tex2d.setWrap( osg.Texture.WRAP_S, osg.Texture.REPEAT )
            tex2d.setWrap( osg.Texture.WRAP_T, osg.Texture.REPEAT )
            stateset.setTextureAttributeAndModes( 1, tex2d, osg.StateAttribute.ON )

    return( geodePlanet )

# end SolarSystem.createPlanet

osg.Group* SolarSystem.createSunLight()

    sunLightSource =  new osg.LightSource

    sunLight =  sunLightSource.getLight()
    sunLight.setPosition( osg.Vec4( 0.0f, 0.0f, 0.0f, 1.0f ) )
    sunLight.setAmbient( osg.Vec4( 0.0f, 0.0f, 0.0f, 1.0f ) )

    sunLightSource.setLight( sunLight )
    sunLightSource.setLocalStateSetModes( osg.StateAttribute.ON )
    sunLightSource.getOrCreateStateSet().setMode(GL_LIGHTING, osg.StateAttribute.ON)

    lightModel =  new osg.LightModel
    lightModel.setAmbientIntensity(osg.Vec4(0.0f,0.0f,0.0f,1.0f))
    sunLightSource.getOrCreateStateSet().setAttribute(lightModel)


    sunLightSource = return()
# end SolarSystem.createSunLight

void SolarSystem.printParameters()
    print "radiusSpace(", _radiusSpace, ")"
    print "radiusSun(", _radiusSun, ")"
    print "radiusMercury(", _radiusMercury, ")"
    print "radiusVenus(", _radiusVenus, ")"
    print "radiusEarth(", _radiusEarth, ")"
    print "radiusMoon(", _radiusMoon, ")"
    print "radiusMars(", _radiusMars, ")"
    print "radiusJupiter(", _radiusJupiter, ")"

    print "RorbitMercury(", _RorbitMercury, ")"
    print "RorbitVenus(", _RorbitVenus, ")"
    print "RorbitEarth(", _RorbitEarth, ")"
    print "RorbitMoon(", _RorbitMoon, ")"
    print "RorbitMars(", _RorbitMars, ")"
    print "RorbitJupiter(", _RorbitJupiter, ")"

    print "rotateSpeedMercury(", _rotateSpeedMercury, ")"
    print "rotateSpeedVenus(", _rotateSpeedVenus, ")"
    print "rotateSpeedEarthAndMoon(", _rotateSpeedEarthAndMoon, ")"
    print "rotateSpeedEarth(", _rotateSpeedEarth, ")"
    print "rotateSpeedMoon(", _rotateSpeedMoon, ")"
    print "rotateSpeedMars(", _rotateSpeedMars, ")"
    print "rotateSpeedJupiter(", _rotateSpeedJupiter, ")"

    print "tiltEarth(", _tiltEarth, ")"

    print "mapSpace(", _mapSpace, ")"
    print "mapSun(", _mapSun, ")"
    print "mapMercury(", _mapMercury, ")"
    print "mapVenus(", _mapVenus, ")"
    print "mapEarth(", _mapEarth, ")"
    print "mapEarthNight(", _mapEarthNight, ")"
    print "mapMoon(", _mapMoon, ")"
    print "mapMars(", _mapMars, ")"
    print "mapJupiter(", _mapJupiter, ")"

    print "rotateSpeedFactor(", _rotateSpeedFactor, ")"
    print "RorbitFactor(", _RorbitFactor, ")"
    print "radiusFactor(", _radiusFactor, ")"


def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use of osg.AnimationPath and UpdateCallbacks for adding animation to your scenes.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("-o <filename>","Write created model to file")

    # initialize the viewer.
    viewer = osgViewer.Viewer()

    osg.ref_ptr<osgGA.KeySwitchMatrixManipulator> keyswitchManipulator = new osgGA.KeySwitchMatrixManipulator
    viewer.setCameraManipulator( keyswitchManipulator.get() )

    solarSystem = SolarSystem()

    while arguments.read("--radiusSpace",solarSystem._radiusSpace) :  
    while arguments.read("--radiusSun",solarSystem._radiusSun) :  
    while arguments.read("--radiusMercury",solarSystem._radiusMercury) :  
    while arguments.read("--radiusVenus",solarSystem._radiusVenus) :  
    while arguments.read("--radiusEarth",solarSystem._radiusEarth) :  
    while arguments.read("--radiusMoon",solarSystem._radiusMoon) :  
    while arguments.read("--radiusMars",solarSystem._radiusMars) :  
    while arguments.read("--radiusJupiter",solarSystem._radiusJupiter) :  

    while arguments.read("--RorbitEarth",solarSystem._RorbitEarth) :  
    while arguments.read("--RorbitMoon",solarSystem._RorbitMoon) :  

    while arguments.read("--rotateSpeedEarthAndMoon",solarSystem._rotateSpeedEarthAndMoon) :  
    while arguments.read("--rotateSpeedEarth",solarSystem._rotateSpeedEarth) :  
    while arguments.read("--rotateSpeedMoon",solarSystem._rotateSpeedMoon) :  
    while arguments.read("--tiltEarth",solarSystem._tiltEarth) :  

    while arguments.read("--mapSpace",solarSystem._mapSpace) :  
    while arguments.read("--mapEarth",solarSystem._mapEarth) :  
    while arguments.read("--mapEarthNight",solarSystem._mapEarthNight) :  
    while arguments.read("--mapMoon",solarSystem._mapMoon) :  

    while arguments.read("--rotateSpeedFactor",solarSystem._rotateSpeedFactor) :  
    while arguments.read("--RorbitFactor",solarSystem._RorbitFactor) :  
    while arguments.read("--radiusFactor",solarSystem._radiusFactor) :  

    solarSystem.rotateSpeedCorrection()
    solarSystem.RorbitCorrection()
    solarSystem.radiusCorrection()

    writeFileName = str()
    while arguments.read("-o",writeFileName) :  


    trackerMode =  osgGA.NodeTrackerManipulator.NODE_CENTER_AND_ROTATION
    mode = str()
    while arguments.read("--tracker-mode",mode) :
        if mode=="NODE_CENTER_AND_ROTATION" : trackerMode = osgGA.NodeTrackerManipulator.NODE_CENTER_AND_ROTATION
        else: if mode=="NODE_CENTER_AND_AZIM" : trackerMode = osgGA.NodeTrackerManipulator.NODE_CENTER_AND_AZIM
        else: if mode=="NODE_CENTER" : trackerMode = osgGA.NodeTrackerManipulator.NODE_CENTER
        else:
            print "Unrecognized --tracker-mode option ", mode, ", valid options are:"
            print "    NODE_CENTER_AND_ROTATION"
            print "    NODE_CENTER_AND_AZIM"
            print "    NODE_CENTER"
            return 1


    rotationMode =  osgGA.NodeTrackerManipulator.TRACKBALL
    while arguments.read("--rotation-mode",mode) :
        if mode=="TRACKBALL" : rotationMode = osgGA.NodeTrackerManipulator.TRACKBALL
        else: if mode=="ELEVATION_AZIM" : rotationMode = osgGA.NodeTrackerManipulator.ELEVATION_AZIM
        else:
            print "Unrecognized --rotation-mode option ", mode, ", valid options are:"
            print "    TRACKBALL"
            print "    ELEVATION_AZIM"
            return 1


    # solarSystem.printParameters()

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        print "setup the following arguments: "
        print "\t--radiusSpace: double"
        print "\t--radiusSun: double"
        print "\t--radiusMercury: double"
        print "\t--radiusVenus: double"
        print "\t--radiusEarth: double"
        print "\t--radiusMoon: double"
        print "\t--radiusMars: double"
        print "\t--radiusJupiter: double"

        print "\t--RorbitMercury: double"
        print "\t--RorbitVenus: double"
        print "\t--RorbitEarth: double"
        print "\t--RorbitMoon: double"
        print "\t--RorbitMars: double"
        print "\t--RorbitJupiter: double"

        print "\t--rotateSpeedMercury: double"
        print "\t--rotateSpeedVenus: double"
        print "\t--rotateSpeedEarthAndMoon: double"
        print "\t--rotateSpeedEarth: double"
        print "\t--rotateSpeedMoon: double"
        print "\t--rotateSpeedMars: double"
        print "\t--rotateSpeedJupiter: double"

        print "\t--tiltEarth: double"

        print "\t--mapSpace: string"
        print "\t--mapSun: string"
        print "\t--mapMercury: string"
        print "\t--mapVenus: string"
        print "\t--mapEarth: string"
        print "\t--mapEarthNight: string"
        print "\t--mapMoon: string"
        print "\t--mapMars: string"
        print "\t--mapJupiter: string"

        print "\t--rotateSpeedFactor: string"
        print "\t--RorbitFactor: string"
        print "\t--radiusFactor: string"

        return 1

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1


    root =  new osg.Group

    clearNode =  new osg.ClearNode
    clearNode.setClearColor(osg.Vec4(0.0f,0.0f,0.0f,1.0f))
    root.addChild(clearNode)

    sunLight =  solarSystem.createSunLight()
    root.addChild(sunLight)

    # create the sun
    solarSun =  solarSystem.createPlanet( solarSystem._radiusSun, "Sun", osg.Vec4( 1.0f, 1.0f, 1.0f, 1.0f), solarSystem._mapSun )
    sunStateSet =  solarSun.getOrCreateStateSet()
    material =  new osg.Material
    material.setEmission( osg.Material.FRONT_AND_BACK, osg.Vec4( 1.0f, 1.0f, 0.0f, 0.0f ) )
    sunStateSet.setAttributeAndModes( material, osg.StateAttribute.ON )

    sunBillboard =  new osg.Billboard()
    sunBillboard.setMode(osg.Billboard.POINT_ROT_EYE)
    sunBillboard.addDrawable(
        createSquare(osg.Vec3(-150.0f,0.0f,-150.0f),osg.Vec3(300.0f,0.0f,0.0f),osg.Vec3(0.0f,0.0f,300.0f),createBillboardImage( osg.Vec4( 1.0, 1.0, 0, 1.0f), 64, 1.0) ),
        osg.Vec3(0.0f,0.0f,0.0f))

    sunLight.addChild( sunBillboard )


    # stick sun right under root, no transformations for the sun
    sunLight.addChild( solarSun )

    # create light source in the sun

#
*********************************************
**  earthMoonGroup and Transformations
*********************************************

    # create earth and moon
    earth =  solarSystem.createPlanet( solarSystem._radiusEarth, "Earth", osg.Vec4( 1.0f, 1.0f, 1.0f, 1.0f), solarSystem._mapEarth, solarSystem._mapEarthNight )
    moon =  solarSystem.createPlanet( solarSystem._radiusMoon, "Moon", osg.Vec4( 1.0f, 1.0f, 1.0f, 1.0f), solarSystem._mapMoon )

    # create transformations for the earthMoonGroup
    aroundSunRotationEarthMoonGroup =  solarSystem.createRotation( solarSystem._RorbitEarth, solarSystem._rotateSpeedEarthAndMoon )
#    osg.MatrixTransform* earthMoonGroupPosition = solarSystem.createTranslationAndTilt( solarSystem._RorbitEarth, solarSystem._tiltEarth )
    earthMoonGroupPosition =  solarSystem.createTranslationAndTilt( solarSystem._RorbitEarth, 0.0 )


    #Group with earth and moon under it
    earthMoonGroup =  new osg.Group

    #transformation to rotate the earth around itself
    earthAroundItselfRotation =  solarSystem.createRotation ( 0.0, solarSystem._rotateSpeedEarth )

    #transformations for the moon
    moonAroundEarthRotation =  solarSystem.createRotation( solarSystem._RorbitMoon, solarSystem._rotateSpeedMoon )
    moonTranslation =  solarSystem.createTranslationAndTilt( solarSystem._RorbitMoon, 0.0 )


    moonTranslation.addChild( moon )
    moonAroundEarthRotation.addChild( moonTranslation )
    earthMoonGroup.addChild( moonAroundEarthRotation )

    earthAroundItselfRotation.addChild( earth )
    earthMoonGroup.addChild( earthAroundItselfRotation )

    earthMoonGroupPosition.addChild( earthMoonGroup )

    aroundSunRotationEarthMoonGroup.addChild( earthMoonGroupPosition )

    sunLight.addChild( aroundSunRotationEarthMoonGroup )
#
*********************************************
**  end earthMoonGroup and Transformations
*********************************************


#
*********************************************
**  Mercury and Transformations
*********************************************

    mercury =  solarSystem.createPlanet( solarSystem._radiusMercury, "Mercury", osg.Vec4( 1.0f, 1.0f, 1.0f, 1.0f ), solarSystem._mapMercury, "" )

    aroundSunRotationMercury =  solarSystem.createRotation( solarSystem._RorbitMercury, solarSystem._rotateSpeedMercury )
    mercuryPosition =  solarSystem.createTranslationAndTilt( solarSystem._RorbitMercury, 0.0f )

    mercuryPosition.addChild( mercury )
    aroundSunRotationMercury.addChild( mercuryPosition )

    sunLight.addChild( aroundSunRotationMercury )
#
*********************************************
**  end Mercury and Transformations
*********************************************


#
*********************************************
**  Venus and Transformations
*********************************************

    venus =  solarSystem.createPlanet( solarSystem._radiusVenus, "Venus", osg.Vec4( 1.0f, 1.0f, 1.0f, 1.0f ), solarSystem._mapVenus, "" )

    aroundSunRotationVenus =  solarSystem.createRotation( solarSystem._RorbitVenus, solarSystem._rotateSpeedVenus )
    venusPosition =  solarSystem.createTranslationAndTilt( solarSystem._RorbitVenus, 0.0f )

    venusPosition.addChild( venus )
    aroundSunRotationVenus.addChild( venusPosition )

    sunLight.addChild( aroundSunRotationVenus )
#
*********************************************
**  end Venus and Transformations
*********************************************


#
*********************************************
**  Mars and Transformations
*********************************************

    mars =  solarSystem.createPlanet( solarSystem._radiusMars, "Mars", osg.Vec4( 1.0f, 1.0f, 1.0f, 1.0f ), solarSystem._mapMars, "" )

    aroundSunRotationMars =  solarSystem.createRotation( solarSystem._RorbitMars, solarSystem._rotateSpeedMars )
    marsPosition =  solarSystem.createTranslationAndTilt( solarSystem._RorbitMars, 0.0f )

    marsPosition.addChild( mars )
    aroundSunRotationMars.addChild( marsPosition )

    sunLight.addChild( aroundSunRotationMars )
#
*********************************************
**  end Mars and Transformations
*********************************************


#
*********************************************
**  Jupiter and Transformations
*********************************************

    jupiter =  solarSystem.createPlanet( solarSystem._radiusJupiter, "Jupiter", osg.Vec4( 1.0f, 1.0f, 1.0f, 1.0f ), solarSystem._mapJupiter, "" )

    aroundSunRotationJupiter =  solarSystem.createRotation( solarSystem._RorbitJupiter, solarSystem._rotateSpeedJupiter )
    jupiterPosition =  solarSystem.createTranslationAndTilt( solarSystem._RorbitJupiter, 0.0f )

    jupiterPosition.addChild( jupiter )
    aroundSunRotationJupiter.addChild( jupiterPosition )

    sunLight.addChild( aroundSunRotationJupiter )
#
*********************************************
**  end Jupiter and Transformations
*********************************************


#
    # add space, but don't light it, as its not illuminated by our sun
    space =  solarSystem.createSpace( "Space", solarSystem._mapSpace )
    space.getOrCreateStateSet().setMode(GL_LIGHTING, osg.StateAttribute.OFF)
    root.addChild( space )


    if !writeFileName.empty() :
        osgDB.writeNodeFile(*root, writeFileName)
        print "Written solar system to \"", writeFileName, "\""
        return 0


    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize( root )

    # set the scene to render
    viewer.setSceneData( root )


    # set up tracker manipulators, once for each astral body
        fnnv = FindNamedNodeVisitor("Moon")
        root.accept(fnnv)

        if !fnnv._foundNodes.empty() :
            # set up the node tracker.
            tm =  new osgGA.NodeTrackerManipulator
            tm.setTrackerMode( trackerMode )
            tm.setRotationMode( rotationMode )
            tm.setTrackNode( fnnv._foundNodes.front().get() )

            unsigned int num = keyswitchManipulator.getNumMatrixManipulators()
            keyswitchManipulator.addMatrixManipulator( 'm', "moon", tm )
            keyswitchManipulator.selectMatrixManipulator( num )

        fnnv = FindNamedNodeVisitor("Earth")
        root.accept(fnnv)

        if !fnnv._foundNodes.empty() :
            # set up the node tracker.
            tm =  new osgGA.NodeTrackerManipulator
            tm.setTrackerMode( trackerMode )
            tm.setRotationMode( rotationMode )
            tm.setTrackNode( fnnv._foundNodes.front().get() )

            unsigned int num = keyswitchManipulator.getNumMatrixManipulators()
            keyswitchManipulator.addMatrixManipulator( 'e', "earth", tm)
            keyswitchManipulator.selectMatrixManipulator( num )

        fnnv = FindNamedNodeVisitor("Sun")
        root.accept(fnnv)

        if !fnnv._foundNodes.empty() :
            # set up the node tracker.
            tm =  new osgGA.NodeTrackerManipulator
            tm.setTrackerMode( trackerMode )
            tm.setRotationMode( rotationMode )
            tm.setTrackNode( fnnv._foundNodes.front().get() )

            unsigned int num = keyswitchManipulator.getNumMatrixManipulators()
            keyswitchManipulator.addMatrixManipulator( 's', "sun", tm)
            keyswitchManipulator.selectMatrixManipulator( num )

    return viewer.run()

# end main



if __name__ == "__main__":
    main(sys.argv)
