#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgspotlight"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgspotlight.cpp'

# OpenSceneGraph example, osgspotlight.
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

#include <osg/Notify>
#include <osg/MatrixTransform>
#include <osg/ShapeDrawable>
#include <osg/PositionAttitudeTransform>
#include <osg/Geometry>
#include <osg/Texture2D>
#include <osg/Geode>
#include <osg/LightSource>
#include <osg/TexGenNode>

#include <osgUtil/Optimizer>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>


# for the grid data..
#include "../osghangglide/terrain_coords.h"


def createSpotLightImage(centerColour, backgroudColour, size, power):


    
    image = osg.Image()
    image.allocateImage(size,size,1,
                         GL_RGBA,GL_UNSIGNED_BYTE)
     
     
    mid = (float(size)-1)*0.5
    div = 2.0/float(size)
    for(unsigned int r=0r<size++r)
        ptr = image.data(0,r,0)
        for(unsigned int c=0c<size++c)
            dx = (float(c) - mid)*div
            dy = (float(r) - mid)*div
            r = powf(1.0-sqrtf(dx*dx+dy*dy),power)
            if r<0.0 : r=0.0
            color = centerColour*r+backgroudColour*(1.0-r)
            *ptr++ = (unsigned char)((color[0])*255.0)
            *ptr++ = (unsigned char)((color[1])*255.0)
            *ptr++ = (unsigned char)((color[2])*255.0)
            *ptr++ = (unsigned char)((color[3])*255.0)
    return image

    #return osgDB.readImageFile("spot.dds")

def createSpotLightDecoratorState(lightNum, textureUnit):

    
    stateset = osg.StateSet()
    
    stateset.setMode(GL_LIGHT0+lightNum, osg.StateAttribute.ON)

    centerColour = osg.Vec4(1.0,1.0,1.0,1.0)
    ambientColour = osg.Vec4(0.05,0.05,0.05,1.0) 

    # set up spot light texture
    texture = osg.Texture2D()
    texture.setImage(createSpotLightImage(centerColour, ambientColour, 64, 1.0))
    texture.setBorderColor(osg.Vec4(ambientColour))
    texture.setWrap(osg.Texture.WRAP_S,osg.Texture.CLAMP_TO_BORDER)
    texture.setWrap(osg.Texture.WRAP_T,osg.Texture.CLAMP_TO_BORDER)
    texture.setWrap(osg.Texture.WRAP_R,osg.Texture.CLAMP_TO_BORDER)
    
    stateset.setTextureAttributeAndModes(textureUnit, texture, osg.StateAttribute.ON)
    
    # set up tex gens
    stateset.setTextureMode(textureUnit, GL_TEXTURE_GEN_S, osg.StateAttribute.ON)
    stateset.setTextureMode(textureUnit, GL_TEXTURE_GEN_T, osg.StateAttribute.ON)
    stateset.setTextureMode(textureUnit, GL_TEXTURE_GEN_R, osg.StateAttribute.ON)
    stateset.setTextureMode(textureUnit, GL_TEXTURE_GEN_Q, osg.StateAttribute.ON)
    
    return stateset


def createSpotLightNode(position, direction, angle, lightNum, textureUnit):


    
    group = osg.Group()
    
    # create light source.
    lightsource = osg.LightSource()
    light = lightsource.getLight()
    light.setLightNum(lightNum)
    light.setPosition(osg.Vec4(position,1.0))
    light.setAmbient(osg.Vec4(0.00,0.00,0.05,1.0))
    light.setDiffuse(osg.Vec4(1.0,1.0,1.0,1.0))
    group.addChild(lightsource)
    
    # create tex gen.
    
    up = osg.Vec3(0.0,0.0,1.0)
    up = (direction ^ up) ^ direction
    up.normalize()
    
    texgenNode = osg.TexGenNode()
    texgenNode.setTextureUnit(textureUnit)
    texgen = texgenNode.getTexGen()
    texgen.setMode(osg.TexGen.EYE_LINEAR)
    texgen.setPlanesFromMatrix(osg.Matrixd.lookAt(position, position+direction, up)*
                                osg.Matrixd.perspective(angle,1.0,0.1,100)*
                                osg.Matrixd.translate(1.0,1.0,1.0)*
                                osg.Matrixd.scale(0.5,0.5,0.5))

    
    group.addChild(texgenNode)
    
    return group
    


def createAnimationPath(center, radius, looptime):


    
    # set up the animation path 
    animationPath = osg.AnimationPath()
    animationPath.setLoopMode(osg.AnimationPath.LOOP)
    
    numSamples = 40
    yaw = 0.0
    yaw_delta = 2.0*osg.PI/((float)numSamples-1.0)
    roll = osg.inDegrees(30.0)
    
    time = 0.0
    time_delta = looptime/(double)numSamples
    for(int i=0i<numSamples++i)
        position = osg.Vec3(center+osg.Vec3(sinf(yaw)*radius,cosf(yaw)*radius,0.0))
        rotation = osg.Quat(osg.Quat(roll,osg.Vec3(0.0,1.0,0.0))*osg.Quat(-(yaw+osg.inDegrees(90.0)),osg.Vec3(0.0,0.0,1.0)))
        
        animationPath.insert(time,osg.AnimationPath.ControlPoint(position,rotation))

        yaw += yaw_delta
        time += time_delta

    return animationPath    

def createBase(center, radius):

    

    geode = osg.Geode()
    
    # set up the texture of the base.
    stateset = osg.StateSet()
    image = osgDB.readImageFile("Images/lz.rgb")
    if image :
        texture = osg.Texture2D()
        texture.setImage(image)
        stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)
    
    geode.setStateSet( stateset )


    grid = osg.HeightField()
    grid.allocate(38,39)
    grid.setOrigin(center+osg.Vec3(-radius,-radius,0.0))
    grid.setXInterval(radius*2.0/(float)(38-1))
    grid.setYInterval(radius*2.0/(float)(39-1))
    
    minHeight = FLT_MAX
    maxHeight = -FLT_MAX


    r = unsigned int()
    for(r=0r<39++r)
        for(unsigned int c=0c<38++c)
            h = vertex[r+c*39][2]
            if h>maxHeight : maxHeight=h
            if h<minHeight : minHeight=h
    
    hieghtScale = radius*0.5/(maxHeight-minHeight)
    hieghtOffset = -(minHeight+maxHeight)*0.5

    for(r=0r<39++r)
        for(unsigned int c=0c<38++c)
            h = vertex[r+c*39][2]
            grid.setHeight(c,r,(h+hieghtOffset)*hieghtScale)
    
    geode.addDrawable(osg.ShapeDrawable(grid))
     
    group = osg.Group()
    group.addChild(geode)
     
    return group


def createMovingModel(center, radius):

    
    animationLength = 10.0

    animationPath = createAnimationPath(center,radius,animationLength)

    model = osg.Group()
 
    cessna = osgDB.readNodeFile("cessna.osgt")
    if cessna :
        bs = cessna.getBound()

        size = radius/bs.radius()*0.3
        positioned = osg.MatrixTransform()
        positioned.setDataVariance(osg.Object.STATIC)
        positioned.setMatrix(osg.Matrix.translate(-bs.center())*
                              osg.Matrix.scale(size,size,size)*
                              osg.Matrix.rotate(osg.inDegrees(180.0),0.0,0.0,2.0))
    
        positioned.addChild(cessna)
    
        xform = osg.MatrixTransform()
        xform.setUpdateCallback(osg.AnimationPathCallback(animationPath,0.0,2.0))
        xform.addChild(positioned)

        xform.addChild(createSpotLightNode(osg.Vec3(0.0,0.0,0.0), osg.Vec3(0.0,1.0,-1.0), 60.0, 0, 1))

        model.addChild(xform)
    
    return model




def createModel():




    
    center = osg.Vec3(0.0,0.0,0.0)
    radius = 100.0
    lightPosition = osg.Vec3(center+osg.Vec3(0.0,0.0,radius))

    # the shadower model
    shadower = createMovingModel(center,radius*0.5)

    # the shadowed model
    shadowed = createBase(center-osg.Vec3(0.0,0.0,radius*0.1),radius)

    # combine the models together to create one which has the shadower and the shadowed with the required callback.
    root = osg.Group()
    
    root.setStateSet(createSpotLightDecoratorState(0,1))

    root.addChild(shadower)
    root.addChild(shadowed)

    return root


int main(int, char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()
    
    # add the spoit light model to the viewer
    viewer.setSceneData( createModel() )
    
    # run the viewer main frame loop.
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
