#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgmemorytest"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgViewer


# Translated from file 'osgmemorytest.cpp'

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

#include <osg/Notify>
#include <osg/Timer>
#include <osg/ArgumentParser>
#include <osg/Texture1D>
#include <osg/Texture2D>
#include <osg/Texture3D>
#include <osg/Geometry>
#include <osg/FrameBufferObject>

#include <osgViewer/Version>

#include <stdio.h>
#include <iostream>

class MemoryTest (osg.Referenced) :


class GLObject (osg.Referenced) :
        virtual void apply(osg.RenderInfo renderInfo) = 0


class GLMemoryTest (MemoryTest) :
        virtual GLObject* allocate() = 0


####################################/
#
# Context test
class ContextTest (MemoryTest) :
        ContextTest(int width, int height, bool pbuffer):
            _width(width),
            _height(height),
            _pbuffer(pbuffer) 
        
        def allocate():
        
            
            traits = osg.GraphicsContext.Traits()
            traits.width = _width
            traits.height = _height
            traits.windowDecoration = True
            traits.pbuffer = _pbuffer
            
            window = osg.GraphicsContext.createGraphicsContext(traits.get())
            if window.valid() : 
                if window.realize() :
                    return window.release()
                else :
                    if _pbuffer : throw "Failed to realize PixelBuffer"
                    else :  throw "Failed to realize GraphicsWindow"
            else :
                std.cerr, "Error: Unable to create graphics context, problem with running osgViewer-", osgViewerGetVersion(), ", cannot create windows/pbuffers."
                
                if _pbuffer : throw "Failed to create PixelBuffer"
                else :  throw "Failed to create GraphicsWindow"
    
        _width = int()
        _height = int()
        _pbuffer = bool()


####################################
#
# Wrap StateAttribute
class StateAttributeObject (GLObject) :
    
        StateAttributeObject(osg.StateAttribute* sa): _attribute(sa) 
        
        def apply(renderInfo):
        
            
            _attribute.apply(*renderInfo.getState())
            
            if renderInfo.getState().checkGLErrors(_attribute.get()) :
                throw "OpenGL error"
        
        _attribute = osg.StateAttribute()


####################################/
#
# Texture test
class TextureTest (GLMemoryTest) :

        TextureTest(int width=256, int height=256, int depth=1):
            _width(width),
            _height(height),
            _depth(depth) 
        
        def allocate():
        
            
            if _depth>1 :
                image = osg.Image()
                image.allocateImage(_width, _height, _depth, GL_RGBA, GL_UNSIGNED_BYTE)
                
                texture = osg.Texture3D()
                texture.setImage(image.get())
                texture.setResizeNonPowerOfTwoHint(False)
                
                return StateAttributeObject(texture.get())
            if _height>1 :
                image = osg.Image()
                image.allocateImage(_width, _height, 1, GL_RGBA, GL_UNSIGNED_BYTE)
                
                texture = osg.Texture2D()
                texture.setImage(image.get())
                texture.setResizeNonPowerOfTwoHint(False)
                
                return StateAttributeObject(texture.get())
            if _width>1 :
                image = osg.Image()
                image.allocateImage(_width, 1, 1, GL_RGBA, GL_UNSIGNED_BYTE)
                
                texture = osg.Texture1D()
                texture.setImage(image.get())
                texture.setResizeNonPowerOfTwoHint(False)
                
                return StateAttributeObject(texture.get())
            else :
                throw "Invalid texture size of 0,0,0"
    
        _width = int()
        _height = int()
        _depth = int()



####################################/
#
# FrameBufferObject test
class FboTest (GLMemoryTest) :

        FboTest(int width=1024, int height=1024, int depth=2):
            _width(width),
            _height(height),
            _depth(depth) 
        
        def allocate():
        
            
            fbo = osg.FrameBufferObject()

            if _depth>=1 : fbo.setAttachment(osg.Camera.COLOR_BUFFER, osg.FrameBufferAttachment(osg.RenderBuffer(_width, _height, GL_RGBA)))
            if _depth>=2 : fbo.setAttachment(osg.Camera.DEPTH_BUFFER, osg.FrameBufferAttachment(osg.RenderBuffer(_width, _height, GL_DEPTH_COMPONENT24)))

            return StateAttributeObject(fbo.get())
    
        _width = int()
        _height = int()
        _depth = int()




####################################
#
# Wrap Drawable
class DrawableObject (GLObject) :
    
        DrawableObject(osg.Drawable* drawable): _drawable(drawable) 
        
        def apply(renderInfo):
        
            
            _drawable.draw(renderInfo)
            
            if renderInfo.getState().checkGLErrors("Drawable") :
                throw "OpenGL error"
        
        _drawable = osg.Drawable()


####################################/
#
# Geometry test
class GeometryTest (GLMemoryTest) :
    
        enum GLObjectType
            VERTEX_ARRAY,
            DISPLAY_LIST,
            VERTEX_BUFFER_OBJECT
        
    

        GeometryTest(GLObjectType type, int width=64, int height=64):
            _glObjectType(type),
            _width(width),
            _height(height) 
        
        def allocate():
        
            
            numVertices = _width * _height
            vertices = osg.Vec3Array(numVertices)
            for(int j=0 j<_height ++j)
                for(int i=0 i<_width ++i)
                    (*vertices)[i+j*_width].set(float(i),float(j),0.0)

            numIndices = (_width-1) * (_height-1) * 4
            quads = osg.DrawElementsUShort(GL_QUADS)
            quads.reserve(numIndices)
            for(int j=0 j<_height-1 ++j)
                for(int i=0 i<_width-1 ++i)
                    quads.push_back(i   + j*_width)
                    quads.push_back(i+1 + j*_width)
                    quads.push_back(i+1 + (j+1)*_width)
                    quads.push_back(i   + (j+1)*_width)
            
            geometry = osg.Geometry()
            geometry.setVertexArray(vertices)
            geometry.addPrimitiveSet(quads)
            
            switch(_glObjectType)
                case(VERTEX_ARRAY):
                    geometry.setUseDisplayList(False)
                    geometry.setUseVertexBufferObjects(False)
                    break
                case(DISPLAY_LIST):
                    geometry.setUseDisplayList(True)
                    geometry.setUseVertexBufferObjects(False)
                    break
                case(VERTEX_BUFFER_OBJECT):
                    geometry.setUseDisplayList(False)
                    geometry.setUseVertexBufferObjects(True)
                    break

            return DrawableObject(geometry)
    
        _glObjectType = GLObjectType()
        _width = int()
        _height = int()


def main(argc, argv):

    
    arguments = osg.ArgumentParser(argc,argv)
    
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" tests OpenGL and Windowing memory scalability..")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","List command line options.")
    arguments.getApplicationUsage().addCommandLineOption("--pbuffer","Create a 512x512 pixel buffer.")
    arguments.getApplicationUsage().addCommandLineOption("--pbuffer <width> <height>","Create a pixel buffer of specified dimensions.")
    arguments.getApplicationUsage().addCommandLineOption("--window","Create a 512x512 graphics window.")
    arguments.getApplicationUsage().addCommandLineOption("--window <width> <height>","Create a graphics window of specified dimensions.")
    arguments.getApplicationUsage().addCommandLineOption("--delay <micoseconds>","Set a delay in microseconds before all OpenGL object operations.")
    arguments.getApplicationUsage().addCommandLineOption("--texture <width> <height> <depth>","Allocate a 3D texture of specified dimensions.")
    arguments.getApplicationUsage().addCommandLineOption("--texture <width> <height>","Allocate a 2D texture of specified dimensions.")
    arguments.getApplicationUsage().addCommandLineOption("--texture <width>","Allocate a 1D texture of specified dimensions.")
    arguments.getApplicationUsage().addCommandLineOption("--geometry <width> <height>","Allocate a osg.Geometry representing a grid of specified size, using OpenGL Dislay Lists.")
    arguments.getApplicationUsage().addCommandLineOption("--geometry-va <width> <height>","Allocate a osg.Geometry representing a grid of specified size, using Vertex Arrays.")
    arguments.getApplicationUsage().addCommandLineOption("--geometry-vbo <width> <height>","Allocate a osg.Geometry representing a grid of specified size, using Vertex Buffer Objects.")
    arguments.getApplicationUsage().addCommandLineOption("--fbo <width> <height>","Allocate a FrameBufferObject of specified dimensions.")
    arguments.getApplicationUsage().addCommandLineOption("-c <num>","Set the number of contexts to create of each type specified.")
    arguments.getApplicationUsage().addCommandLineOption("-g <num>","Set the number of GL objects to create of each type specified.")

    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout, osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1


    typedef std.list< GLMemoryTest > GLMemoryTests
    typedef std.list< ContextTest > ContextTests

    contextTests = ContextTests()
    glMemoryTests = GLMemoryTests()
    
    int width, height, depth
    while arguments.read("--pbuffer",width,height) :  contextTests.push_back(ContextTest(width, height, True)) 
    while arguments.read("--pbuffer") :  contextTests.push_back(ContextTest(512, 512, True)) 

    while arguments.read("--window",width,height) :  contextTests.push_back(ContextTest(width, height, False)) 
    while arguments.read("--window") :  contextTests.push_back(ContextTest(512,512, False)) 

    while arguments.read("--texture",width,height,depth) :  glMemoryTests.push_back(TextureTest(width,height,depth)) 
    while arguments.read("--texture",width,height) :  glMemoryTests.push_back(TextureTest(width,height,1)) 
    while arguments.read("--texture",width) :  glMemoryTests.push_back(TextureTest(width,1,1)) 

    while arguments.read("--fbo",width,height,depth) :  glMemoryTests.push_back(FboTest(width,height,depth)) 
    while arguments.read("--fbo",width,height) :  glMemoryTests.push_back(FboTest(width,height,2)) 
    while arguments.read("--fbo") :  glMemoryTests.push_back(FboTest(1024,1024,2)) 

    while arguments.read("--geometry",width,height) :  glMemoryTests.push_back(GeometryTest(GeometryTest.DISPLAY_LIST,width,height)) 
    while arguments.read("--geometry") :  glMemoryTests.push_back(GeometryTest(GeometryTest.DISPLAY_LIST,64,64)) 

    while arguments.read("--geometry-vbo",width,height) :  glMemoryTests.push_back(GeometryTest(GeometryTest.VERTEX_BUFFER_OBJECT,width,height)) 
    while arguments.read("--geometry-vbo") :  glMemoryTests.push_back(GeometryTest(GeometryTest.VERTEX_BUFFER_OBJECT,64,64)) 

    while arguments.read("--geometry-va",width,height) :  glMemoryTests.push_back(GeometryTest(GeometryTest.VERTEX_ARRAY,width,height)) 
    while arguments.read("--geometry-va") :  glMemoryTests.push_back(GeometryTest(GeometryTest.VERTEX_ARRAY,64,64)) 

    sleepTime = 0
    while arguments.read("--delay",sleepTime) : 

    maxNumContextIterations = 1
    while arguments.read("-c",maxNumContextIterations) : 

    maxNumGLIterations = 1000
    while arguments.read("-g",maxNumGLIterations) : 

#if 0
    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1
#endif
    
    typedef std.list< osg.GraphicsContext > Contexts
    typedef std.list< GLObject > GLObjects
    allocatedContexts = Contexts()
    glObjects = GLObjects()
    
    if contextTests.empty() :
        if glMemoryTests.empty() :
            print "No tests specified, please specify test using the command line options below."
        
            arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
            return 1            
        else :
            contextTests.push_back(ContextTest(512,512, False))

    startTick = osg.Timer.instance().tick()

    # use printf's below as C++'s ostream classes use more memory and are more likely to fail when everything
    # goes wrong with memory allocations.
    
    numContextIterations = 0
    numGLObjectIterations = 0
    numGLObjectsApplied = 0
    try
        for( numGLObjectIterations<maxNumGLIterations ++numGLObjectIterations)
            for(GLMemoryTests.iterator itr = glMemoryTests.begin()
                itr != glMemoryTests.end()
                ++itr)
                glObject = (*itr).allocate()
                if glObject.valid() : glObjects.push_back(glObject.get())
        
        for(numContextIterations<maxNumContextIterations ++numContextIterations)
            printf("GraphicsContext %i\n",numContextIterations)
            for(ContextTests.iterator itr = contextTests.begin()
                itr != contextTests.end()
                ++itr)
                context = (*itr).allocate()
                if context.valid() :
                    allocatedContexts.push_back(context)

                    context.makeCurrent()
                    
                    renderInfo = osg.RenderInfo()
                    renderInfo.setState(context.getState())
                    
                    for(GLObjects.iterator gitr = glObjects.begin()
                        gitr != glObjects.end()
                        ++gitr)
                        if sleepTime>0 : OpenThreads.Thread.microSleep( sleepTime )

                        printf("%i ",numGLObjectsApplied)fflush(stdout)

                        (*gitr).apply(renderInfo)
                        ++numGLObjectsApplied
                    
                    context.releaseContext()
                    
                    printf("\n\n") fflush(stdout)
    catch( char* errorString)
        printf("\nException caught, contexts completed = %i, gl objects successfully applied = %i, error = %s\n\n",numContextIterations, numGLObjectsApplied, errorString)
        return 1
    catch(...)
        printf("\nException caught, contexts completed = %i, gl objects successfully applied = %i\n\n",numContextIterations, numGLObjectsApplied)
        return 1

    endTick = osg.Timer.instance().tick()

    printf("\nSuccessful completion, contexts created = %i, gl objects applied = %i\n",numContextIterations, numGLObjectsApplied)
    printf("Duration = %f seconds.\n\n",osg.Timer.instance().delta_s(startTick, endTick))
    

    return 0


if __name__ == "__main__":
    main(sys.argv)
