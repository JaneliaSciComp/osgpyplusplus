#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgcomputeshaders"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osgcomputeshaders.cpp'

# -*-c++-*- OpenSceneGraph example, osgcomputeshaders.
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

# Written by Wang Rui
# This example can work only if GL version is 4.3 or greater

#include <osg/Texture2D>
#include <osg/Geometry>
#include <osg/Geode>
#include <osgDB/ReadFile>
#include <osgGA/StateSetManipulator>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

static  char* computeSrc = 
    "#version 430\n"
    "uniform float osg_FrameTime\n"
    "layout (r32f, binding =0) uniform image2D targetTex\n"
    "layout (local_size_x = 16, local_size_y = 16) in\n"
    "void main() \n"
    "   ivec2 storePos = ivec2(gl_GlobalInvocationID.xy)\n"
    "   float coeffcient = 0.5*sin(float(gl_WorkGroupID.x + gl_WorkGroupID.y)*0.1 + osg_FrameTime)\n"
    "   coeffcient *= length(vec2(ivec2(gl_LocalInvocationID.xy) - ivec2(8)) / vec2(8.0))\n"
    "   imageStore(targetTex, storePos, vec4(1.0-coeffcient, 0.0, 0.0, 0.0))\n"
    "\n"


def main(argc, argv):

    
    arguments = osg.ArgumentParser( argc, argv )
    
    # Create the texture as both the output of compute shader and the input of a normal quad
    tex2D = osg.Texture2D()
    tex2D.setTextureSize( 512, 512 )
    tex2D.setFilter( osg.Texture2D.MIN_FILTER, osg.Texture2D.LINEAR )
    tex2D.setFilter( osg.Texture2D.MAG_FILTER, osg.Texture2D.LINEAR )
    tex2D.setInternalFormat( GL_R32F )
    tex2D.setSourceFormat( GL_RED )
    tex2D.setSourceType( GL_FLOAT )
    tex2D.bindToImageUnit( 0, osg.Texture.WRITE_ONLY )  # So we can use 'image2D' in the compute shader
    
    # The compute shader can't work with other kinds of shaders
    # It also requires the work group numbers. Setting them to 0 will disable the compute shader
    computeProg = osg.Program()
    computeProg.setComputeGroups( 512/16, 512/16, 1 )
    computeProg.addShader( osg.Shader(osg.Shader.COMPUTE, computeSrc) )
    
    # Create a node for outputting to the texture.
    # It is OK to have just an empty node here, but seems inbuilt uniforms like osg_FrameTime won't work then.
    # TODO: maybe we can have a custom drawable which also will implement glMemoryBarrier?
    sourceNode = osgDB.readNodeFile("axes.osgt")
    if  !sourceNode  : sourceNode = osg.Node()
    sourceNode.setDataVariance( osg.Object.DYNAMIC )
    sourceNode.getOrCreateStateSet().setAttributeAndModes( computeProg.get() )
    sourceNode.getOrCreateStateSet().addUniform( osg.Uniform("targetTex", (int)0) )
    sourceNode.getOrCreateStateSet().setTextureAttributeAndModes( 0, tex2D.get() )
    
    # Display the texture on a quad. We will also be able to operate on the data if reading back to CPU side
    geom = osg.createTexturedQuadGeometry(
        osg.Vec3(), osg.Vec3(1.0,0.0,0.0), osg.Vec3(0.0,0.0,1.0) )
    quad = osg.Geode()
    quad.addDrawable( geom )
    quad.getOrCreateStateSet().setMode( GL_LIGHTING, osg.StateAttribute.OFF )
    quad.getOrCreateStateSet().setTextureAttributeAndModes( 0, tex2D.get() )
    
    # Create the scene graph and start the viewer
    scene = osg.Group()
    scene.addChild( sourceNode )
    scene.addChild( quad.get() )
    
    viewer = osgViewer.Viewer()
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    viewer.addEventHandler( osgViewer.StatsHandler )()
    viewer.addEventHandler( osgViewer.WindowSizeHandler )()
    viewer.setSceneData( scene.get() )
    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
