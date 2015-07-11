#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgtexture1D"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgViewer

# OpenSceneGraph example, osgtexture1D.
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
#include <osg/Texture1D>
#include <osg/TexGenNode>
#include <osg/Material>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>

#include <iostream>

# Creates a stateset which contains a 1D texture which is populated by contour banded color,
# and allows tex gen to override the S texture coordinate
def create1DTextureStateToDecorate(loadedModel):
    image =  new osg.Image

    noPixels =  1024
    
    # allocate the image data, noPixels x 1 x 1 with 4 rgba floats - equivalent to a Vec4!
    image.allocateImage(noPixels,1,1,GL_RGBA,GL_FLOAT)
    image.setInternalTextureFormat(GL_RGBA)
    
    typedef std.vector<osg.Vec4> ColorBands
    colorbands = ColorBands()
    colorbands.push_back(osg.Vec4(0.0f,0.0,0.0,1.0f))
    colorbands.push_back(osg.Vec4(1.0f,0.0,0.0,1.0f))
    colorbands.push_back(osg.Vec4(1.0f,1.0,0.0,1.0f))
    colorbands.push_back(osg.Vec4(0.0f,1.0,0.0,1.0f))
    colorbands.push_back(osg.Vec4(0.0f,1.0,1.0,1.0f))
    colorbands.push_back(osg.Vec4(0.0f,0.0,1.0,1.0f))
    colorbands.push_back(osg.Vec4(1.0f,0.0,1.0,1.0f))
    colorbands.push_back(osg.Vec4(1.0f,1.0,1.0,1.0f))

    nobands =  colorbands.size()
    delta =  nobands/(float)noPixels
    pos =  0.0f

    # fill in the image data.    
    dataPtr =  (osg.Vec4*)image.data()
    for(int i=0i<noPixels++i,pos+=delta)
        #float p = floorf(pos)
        #float r = pos-p
        #osg.Vec4 color = colorbands[(int)p]*(1.0f-r)
        #if p+1<colorbands.size() : color += colorbands[(int)p+1]*r
        color =  colorbands[(int)pos]
        *dataPtr++ = color
    
    texture =  new osg.Texture1D
    texture.setWrap(osg.Texture1D.WRAP_S,osg.Texture1D.MIRROR)
    texture.setFilter(osg.Texture1D.MIN_FILTER,osg.Texture1D.LINEAR)
    texture.setImage(image)
    
    material =  new osg.Material
    
    stateset =  new osg.StateSet
    
    stateset.setTextureAttribute(0,texture,osg.StateAttribute.OVERRIDE)
    stateset.setTextureMode(0,GL_TEXTURE_1D,osg.StateAttribute.ON|osg.StateAttribute.OVERRIDE)
    stateset.setTextureMode(0,GL_TEXTURE_2D,osg.StateAttribute.OFF|osg.StateAttribute.OVERRIDE)
    stateset.setTextureMode(0,GL_TEXTURE_3D,osg.StateAttribute.OFF|osg.StateAttribute.OVERRIDE)

    stateset.setTextureMode(0,GL_TEXTURE_GEN_S,osg.StateAttribute.ON|osg.StateAttribute.OVERRIDE)
    
    stateset.setAttribute(material,osg.StateAttribute.OVERRIDE)
    
    stateset = return()


# An app callback which alternates the tex gen mode between object linear and eye linear to illustrate what differences it makes.
class AnimateTexGenCallback : public osg.NodeCallback
    public:
        AnimateTexGenCallback() 
        
        def animateTexGen(texgenNode, time):
            # here we simply get any existing texgen, and then increment its
            # plane, pushing the R coordinate through the texture.
            timeInterval =  2.0f
            
            static double previousTime = time
            static bool state = false
            while time>previousTime+timeInterval :
                previousTime+=timeInterval
                state = !state
        
            if state :
                texgenNode.getTexGen().setMode(osg.TexGen.OBJECT_LINEAR)
            else:
                texgenNode.getTexGen().setMode(osg.TexGen.EYE_LINEAR)
            

        virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
            texgenNode =  dynamic_cast<osg.TexGenNode*>(node)

            if texgenNode  nv.getFrameStamp() :
                # we have an exisitng stateset, so lets animate it.
                animateTexGen(texgenNode,nv.getFrameStamp().getSimulationTime())

            # note, callback is repsonsible for scenegraph traversal so
            # should always include call the traverse(node,nv) to ensure 
            # that the rest of cullbacks and the scene graph are traversed.
            traverse(node,nv)



def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)
   
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # load the images specified on command line
    loadedModel =  osgDB.readNodeFiles(arguments)
  
    # if not loaded assume no arguments passed in, try use default mode instead.
    if !loadedModel : loadedModel = osgDB.readNodeFile("dumptruck.osgt")
    
    if !loadedModel :
        osg.notify(osg.NOTICE), arguments.getApplicationUsage().getCommandLineUsage()
        return 0

    stateset =  create1DTextureStateToDecorate(loadedModel)
    if !stateset :
        print "Error: failed to create 1D texture state."
        return 1


    loadedModel.setStateSet(stateset)

    osg. Group *root = new osg. Group
    root . addChild( loadedModel )

    # The contour banded color texture is used in conjunction with TexGenNode
    # to create contoured models, either in object linear coords - like
    # contours on a map, or eye linear which contour the distance from
    # the eye. An app callback toggles between the two tex gen modes.
    texgenNode =  new osg.TexGenNode
    texgenNode.setReferenceFrame( osg.TexGenNode.ABSOLUTE_RF )
    texgenNode.getTexGen().setMode( osg.TexGen.OBJECT_LINEAR )

    bs =  loadedModel.getBound()
    zBase =  bs.center().z()-bs.radius()
    zScale =  2.0f/bs.radius()
    texgenNode.getTexGen().setPlane(osg.TexGen.S,osg.Plane(0.0f,0.0f,zScale,-zBase))

    texgenNode.setUpdateCallback(new AnimateTexGenCallback())

    root . addChild( texgenNode )


    viewer.setSceneData( root )

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
