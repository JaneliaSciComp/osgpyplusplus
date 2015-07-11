#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgspotlight"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgspotlight.
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


osg.Image* createSpotLightImage( osg.Vec4 centerColour,  osg.Vec4 backgroudColour, unsigned int size, float power)
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
            color =  centerColour*r+backgroudColour*(1.0f-r)
            *ptr++ = (unsigned char)((color[0])*255.0f)
            *ptr++ = (unsigned char)((color[1])*255.0f)
            *ptr++ = (unsigned char)((color[2])*255.0f)
            *ptr++ = (unsigned char)((color[3])*255.0f)
    image = return()

    #return osgDB.readImageFile("spot.dds")

osg.StateSet* createSpotLightDecoratorState(unsigned int lightNum, unsigned int textureUnit)
    stateset =  new osg.StateSet
    
    stateset.setMode(GL_LIGHT0+lightNum, osg.StateAttribute.ON)

    centerColour = osg.Vec4(1.0f,1.0f,1.0f,1.0f)
    ambientColour = osg.Vec4(0.05f,0.05f,0.05f,1.0f) 

    # set up spot light texture
    texture =  new osg.Texture2D()
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
    
    stateset = return()


osg.Node* createSpotLightNode( osg.Vec3 position,  osg.Vec3 direction, float angle, unsigned int lightNum, unsigned int textureUnit)
    group =  new osg.Group
    
    # create light source.
    lightsource =  new osg.LightSource
    light =  lightsource.getLight()
    light.setLightNum(lightNum)
    light.setPosition(osg.Vec4(position,1.0f))
    light.setAmbient(osg.Vec4(0.00f,0.00f,0.05f,1.0f))
    light.setDiffuse(osg.Vec4(1.0f,1.0f,1.0f,1.0f))
    group.addChild(lightsource)
    
    # create tex gen.
    
    up = osg.Vec3(0.0f,0.0f,1.0f)
    up = (direction ^ up) ^ direction
    up.normalize()
    
    texgenNode =  new osg.TexGenNode
    texgenNode.setTextureUnit(textureUnit)
    texgen =  texgenNode.getTexGen()
    texgen.setMode(osg.TexGen.EYE_LINEAR)
    texgen.setPlanesFromMatrix(osg.Matrixd.lookAt(position, position+direction, up)*
                                osg.Matrixd.perspective(angle,1.0,0.1,100)*
                                osg.Matrixd.translate(1.0,1.0,1.0)*
                                osg.Matrixd.scale(0.5,0.5,0.5))

    
    group.addChild(texgenNode)
    
    group = return()
    


def createAnimationPath(center, radius, looptime):
    # set up the animation path 
    animationPath =  new osg.AnimationPath
    animationPath.setLoopMode(osg.AnimationPath.LOOP)
    
    numSamples =  40
    yaw =  0.0f
    yaw_delta =  2.0f*osg.PI/((float)numSamples-1.0f)
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

def createBase(center, radius):
    geode =  new osg.Geode
    
    # set up the texture of the base.
    stateset =  new osg.StateSet()
    image =  osgDB.readImageFile("Images/lz.rgb")
    if image :
        texture =  new osg.Texture2D
        texture.setImage(image)
        stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)
    
    geode.setStateSet( stateset )


    grid =  new osg.HeightField
    grid.allocate(38,39)
    grid.setOrigin(center+osg.Vec3(-radius,-radius,0.0f))
    grid.setXInterval(radius*2.0f/(float)(38-1))
    grid.setYInterval(radius*2.0f/(float)(39-1))
    
    minHeight =  FLT_MAX
    maxHeight =  -FLT_MAX


    unsigned int r
    for(r=0r<39++r)
        for(unsigned int c=0c<38++c)
            h =  vertex[r+c*39][2]
            if h>maxHeight : maxHeight=h
            if h<minHeight : minHeight=h
    
    hieghtScale =  radius*0.5f/(maxHeight-minHeight)
    hieghtOffset =  -(minHeight+maxHeight)*0.5f

    for(r=0r<39++r)
        for(unsigned int c=0c<38++c)
            h =  vertex[r+c*39][2]
            grid.setHeight(c,r,(h+hieghtOffset)*hieghtScale)
    
    geode.addDrawable(new osg.ShapeDrawable(grid))
     
    group =  new osg.Group
    group.addChild(geode)
     
    group = return()


def createMovingModel(center, radius):
    animationLength =  10.0f

    animationPath =  createAnimationPath(center,radius,animationLength)

    model =  new osg.Group
 
    cessna =  osgDB.readNodeFile("cessna.osgt")
    if cessna :
        bs =  cessna.getBound()

        size =  radius/bs.radius()*0.3f
        positioned =  new osg.MatrixTransform
        positioned.setDataVariance(osg.Object.STATIC)
        positioned.setMatrix(osg.Matrix.translate(-bs.center())*
                              osg.Matrix.scale(size,size,size)*
                              osg.Matrix.rotate(osg.inDegrees(180.0f),0.0f,0.0f,2.0f))
    
        positioned.addChild(cessna)
    
        xform =  new osg.MatrixTransform
        xform.setUpdateCallback(new osg.AnimationPathCallback(animationPath,0.0f,2.0))
        xform.addChild(positioned)

        xform.addChild(createSpotLightNode(osg.Vec3(0.0f,0.0f,0.0f), osg.Vec3(0.0f,1.0f,-1.0f), 60.0f, 0, 1))

        model.addChild(xform)
    
    model = return()




def createModel():
    center = osg.Vec3(0.0f,0.0f,0.0f)
    radius =  100.0f
    lightPosition = osg.Vec3(center+osg.Vec3(0.0f,0.0f,radius))

    # the shadower model
    shadower =  createMovingModel(center,radius*0.5f)

    # the shadowed model
    shadowed =  createBase(center-osg.Vec3(0.0f,0.0f,radius*0.1),radius)

    # combine the models together to create one which has the shadower and the shadowed with the required callback.
    root =  new osg.Group
    
    root.setStateSet(createSpotLightDecoratorState(0,1))

    root.addChild(shadower)
    root.addChild(shadowed)

    root = return()


int main(int, char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()
    
    # add the spoit light model to the viewer
    viewer.setSceneData( createModel() )
    
    # run the viewer main frame loop.
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
