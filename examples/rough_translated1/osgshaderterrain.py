#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgshaderterrain"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgshaderterrain.cpp'

# OpenSceneGraph example, osgshaderterrain.
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

#include <osg/AlphaFunc>
#include <osg/Billboard>
#include <osg/BlendFunc>
#include <osg/Depth>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/GL2Extensions>
#include <osg/Material>
#include <osg/Math>
#include <osg/MatrixTransform>
#include <osg/PolygonOffset>
#include <osg/Program>
#include <osg/Projection>
#include <osg/Shader>
#include <osg/ShapeDrawable>
#include <osg/StateSet>
#include <osg/Switch>
#include <osg/Texture2D>
#include <osg/Uniform>

#include <osgDB/ReadFile>
#include <osgDB/FileUtils>

#include <osgUtil/SmoothingVisitor>

#include <osgText/Text>

#include <osgViewer/Viewer>

#include <iostream>

# for the grid data..
#include "../osghangglide/terrain_coords.h"

def createScene():

    
    scene = osg.Group()

    numColumns = 38
    numRows = 39
    r = unsigned int()
    c = unsigned int()

    origin = osg.Vec3(0.0,0.0,0.0)
    size = osg.Vec3(1000.0,1000.0,250.0)
    scaleDown = osg.Vec3(1.0/size.x(),1.0/size.y(),1.0/size.z())

    # ---------------------------------------
    # Set up a StateSet to texture the objects
    # ---------------------------------------
    stateset = osg.StateSet()


    originUniform = osg.Uniform("terrainOrigin",origin)
    stateset.addUniform(originUniform)

    sizeUniform = osg.Uniform("terrainSize",size)
    stateset.addUniform(sizeUniform)

    scaleDownUniform = osg.Uniform("terrainScaleDown",scaleDown)
    stateset.addUniform(scaleDownUniform)

    terrainTextureSampler = osg.Uniform("terrainTexture",0)
    stateset.addUniform(terrainTextureSampler)

    baseTextureSampler = osg.Uniform("baseTexture",1)
    stateset.addUniform(baseTextureSampler)

    treeTextureSampler = osg.Uniform("treeTexture",1)
    stateset.addUniform(treeTextureSampler)


    # compute z range of z values of grid data so we can scale it.
    min_z = FLT_MAX
    max_z = -FLT_MAX
    for(r=0r<numRows++r)
        for(c=0c<numColumns++c)
            min_z = osg.minimum(min_z,vertex[r+c*numRows][2])
            max_z = osg.maximum(max_z,vertex[r+c*numRows][2])

    scale_z = size.z()/(max_z-min_z)

    terrainImage = osg.Image()
    terrainImage.allocateImage(numColumns,numRows,1,GL_LUMINANCE, GL_FLOAT)
    terrainImage.setInternalTextureFormat(GL_LUMINANCE_FLOAT32_ATI)
    for(r=0r<numRows++r)
        for(c=0c<numColumns++c)
            *((float*)(terrainImage.data(c,r))) = (vertex[r+c*numRows][2]-min_z)*scale_z

    terrainTexture = osg.Texture2D()
    terrainTexture.setImage(terrainImage)
    terrainTexture.setFilter(osg.Texture2D.MIN_FILTER, osg.Texture2D.NEAREST)
    terrainTexture.setFilter(osg.Texture2D.MAG_FILTER, osg.Texture2D.NEAREST)
    terrainTexture.setResizeNonPowerOfTwoHint(False)
    stateset.setTextureAttributeAndModes(0,terrainTexture,osg.StateAttribute.ON)


    image = osgDB.readImageFile("Images/lz.rgb")
    if image :
        texture = osg.Texture2D()

        texture.setImage(image)
        stateset.setTextureAttributeAndModes(1,texture,osg.StateAttribute.ON)

        print "Creating terrain..."

        geode = osg.Geode()
        geode.setStateSet( stateset )


            program = osg.Program()
            stateset.setAttribute(program)

#if 1
            # use inline shaders

            #################################/
            # vertex shader using just Vec4 coefficients
            char vertexShaderSource[] =
               "uniform sampler2D terrainTexture\n"
               "uniform vec3 terrainOrigin\n"
               "uniform vec3 terrainScaleDown\n"
               "\n"
               "varying vec2 texcoord\n"
               "\n"
               "void main(void)\n"
               "\n"
               "    texcoord = gl_Vertex.xy - terrainOrigin.xy\n"
               "    texcoord.x *= terrainScaleDown.x\n"
               "    texcoord.y *= terrainScaleDown.y\n"
               "\n"
               "    vec4 position\n"
               "    position.x = gl_Vertex.x\n"
               "    position.y = gl_Vertex.y\n"
               "    position.z = texture2D(terrainTexture, texcoord).r\n"
               "    position.w = 1.0\n"
               " \n"
               "    gl_Position     = gl_ModelViewProjectionMatrix * position\n"
                "   gl_FrontColor = vec4(1.0,1.0,1.0,1.0)\n"
               "\n"

            #################################
            # fragment shader
            #
            char fragmentShaderSource[] =
                "uniform sampler2D baseTexture \n"
                "varying vec2 texcoord\n"
                "\n"
                "void main(void) \n"
                "\n"
                "    gl_FragColor = texture2D( baseTexture, texcoord) \n"
                "\n"

            program.addShader(osg.Shader(osg.Shader.VERTEX, vertexShaderSource))
            program.addShader(osg.Shader(osg.Shader.FRAGMENT, fragmentShaderSource))

#else :

            # get shaders from source
            program.addShader(osg.Shader.readShaderFile(osg.Shader.VERTEX, osgDB.findDataFile("shaders/terrain.vert")))
            program.addShader(osg.Shader.readShaderFile(osg.Shader.FRAGMENT, osgDB.findDataFile("shaders/terrain.frag")))

#endif

            # get shaders from source


            geometry = osg.Geometry()

            v = *(osg.Vec3Array(numColumns*numRows))
            color = *(osg.Vec4ubArray(1))

            color[0].set(255,255,255,255)

            rowCoordDelta = size.y()/(float)(numRows-1)
            columnCoordDelta = size.x()/(float)(numColumns-1)

            rowTexDelta = 1.0/(float)(numRows-1)
            columnTexDelta = 1.0/(float)(numColumns-1)

            pos = origin
            tex = osg.Vec2(0.0,0.0)
            vi = 0
            for(r=0r<numRows++r)
                pos.x() = origin.x()
                tex.x() = 0.0
                for(c=0c<numColumns++c)
                    v[vi].set(pos.x(),pos.y(),pos.z())
                    pos.x()+=columnCoordDelta
                    tex.x()+=columnTexDelta
                    ++vi
                pos.y() += rowCoordDelta
                tex.y() += rowTexDelta

            geometry.setVertexArray(v)
            geometry.setColorArray(color, osg.Array.BIND_OVERALL)

            for(r=0r<numRows-1++r)
                drawElements = *(osg.DrawElementsUShort(GL_QUAD_STRIP,2*numColumns))
                geometry.addPrimitiveSet(drawElements)
                ei = 0
                for(c=0c<numColumns++c)
                    drawElements[ei++] = (r+1)*numColumns+c
                    drawElements[ei++] = (r)*numColumns+c

            geometry.setInitialBound(osg.BoundingBox(origin, origin+size))

            geode.addDrawable(geometry)

            scene.addChild(geode)

    print "done."

    return scene

class TestSupportOperation (osg.GraphicsOperation) :

    TestSupportOperation():
        osg.GraphicsOperation("TestSupportOperation",False),
        _supported(True),
        _errorMessage() 

    virtual void operator () (osg.GraphicsContext* gc)
        lock = OpenThreads.ScopedLock<OpenThreads.Mutex>(_mutex)

        contextID = gc.getState().getContextID()
        gl2ext = osg.GL2Extensions.Get(contextID,True)
        if  gl2ext  :
            if  !gl2ext.isGlslSupported()  :
                _supported = False
                _errorMessage = "ERROR: GLSL not supported by OpenGL driver."

            numVertexTexUnits = 0
            glGetIntegerv( GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS, numVertexTexUnits )
            if  numVertexTexUnits <= 0  :
                _supported = False
                _errorMessage = "ERROR: vertex texturing not supported by OpenGL driver."
        else :
            _supported = False
            _errorMessage = "ERROR: GLSL not supported."

    _mutex = OpenThreads.Mutex()
    _supported = bool()
    _errorMessage = str()


int main(int, char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    node = createScene()

    # add model to viewer.
    viewer.setSceneData( node )

    viewer.setUpViewAcrossAllScreens()

    testSupportOperation = TestSupportOperation()
#if 0
    # temporily commenting out as its causing the viewer to crash... no clue yet to why
    viewer.setRealizeOperation(testSupportOperation.get())
#endif
    # create the windows and run the threads.
    viewer.realize()

    if !testSupportOperation._supported :
        osg.notify(osg.WARN), testSupportOperation._errorMessage

        return 1

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
