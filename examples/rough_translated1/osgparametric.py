#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgparametric"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgparametric.cpp'

# OpenSceneGraph example, osgparametric.
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

#include <osg/Vec3>
#include <osg/Vec4>
#include <osg/Quat>
#include <osg/Matrix>
#include <osg/ShapeDrawable>
#include <osg/Geometry>
#include <osg/Geode>
#include <osg/Texture2D>

#include <osgDB/FileUtils>
#include <osgDB/ReadFile>

#include <osgUtil/Optimizer>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <iostream>

# for the grid data..
#include "../osghangglide/terrain_coords.h"

#################################/
# vertex shader using just Vec4 coefficients
char vertexShaderSource_simple[] = 
    "uniform vec4 coeff \n"
    "\n"
    "void main(void) \n"
    " \n"
    "\n"
    "    gl_TexCoord[0] = gl_Vertex \n"
    "    vec4 vert = gl_Vertex \n"
    "    vert.z = gl_Vertex.x*coeff[0] + gl_Vertex.x*gl_Vertex.x* coeff[1] + \n"
    "             gl_Vertex.y*coeff[2] + gl_Vertex.y*gl_Vertex.y* coeff[3] \n"
    "    gl_Position = gl_ModelViewProjectionMatrix * vert\n"
    "\n"
  
  
#################################
# vertex shader using full Matrix4 coefficients
char vertexShaderSource_matrix[] = 
    "uniform vec4  origin \n"
    "uniform mat4  coeffMatrix \n"
    "\n"
    "void main(void) \n"
    " \n"
    "\n"
    "    gl_TexCoord[0] = gl_Vertex \n"
    "    vec4 v = vec4(gl_Vertex.x, gl_Vertex.x*gl_Vertex.x, gl_Vertex.y, gl_Vertex.y*gl_Vertex.y ) \n"
    "    gl_Position = gl_ModelViewProjectionMatrix * (origin + coeffMatrix * v)\n"
    "\n"

#################################
# vertex shader using texture read
char vertexShaderSource_texture[] = 
    "uniform sampler2D vertexTexture \n"
    "\n"
    "void main(void) \n"
    " \n"
    "\n"
    "    gl_TexCoord[0] = gl_Vertex \n"
    "    vec4 vert = gl_Vertex \n"
    "    vert.z = texture2D( vertexTexture, gl_TexCoord[0].xy).x*0.0001 \n"
    "    gl_Position = gl_ModelViewProjectionMatrix * vert\n"
    "\n"


#################################
# fragment shader
#
char fragmentShaderSource[] = 
    "uniform sampler2D baseTexture \n"
    "\n"
    "void main(void) \n"
    " \n"
    "    gl_FragColor = texture2D( baseTexture, gl_TexCoord[0].xy) \n"
    "\n"



class UniformVarying (osg.Uniform.Callback) :
virtual void operator () (osg.Uniform* uniform, osg.NodeVisitor* nv)
        fs = nv.getFrameStamp()
        value = sinf(fs.getSimulationTime())
        uniform.set(osg.Vec4(value,-value,-value,value))


def createModel(shader, textureFileName, terrainFileName, dynamic, useVBO):

    
    geode = osg.Geode()
    
    geom = osg.Geometry()
    geode.addDrawable(geom)
    
    # dimensions for ~one million triangles :-)
    num_x = 708
    num_y = 708

    # set up state
    
        stateset = geom.getOrCreateStateSet()

        program = osg.Program()
        stateset.setAttribute(program)

        if shader=="simple" :
            vertex_shader = osg.Shader(osg.Shader.VERTEX, vertexShaderSource_simple)
            program.addShader(vertex_shader)

            coeff = osg.Uniform("coeff",osg.Vec4(1.0,-1.0,-1.0,1.0))
            
            stateset.addUniform(coeff)

            if dynamic :
                coeff.setUpdateCallback(UniformVarying)()
                coeff.setDataVariance(osg.Object.DYNAMIC)
                stateset.setDataVariance(osg.Object.DYNAMIC)
            
        elif shader=="matrix" :
            vertex_shader = osg.Shader(osg.Shader.VERTEX, vertexShaderSource_matrix)
            program.addShader(vertex_shader)

            origin = osg.Uniform("origin",osg.Vec4(0.0,0.0,0.0,1.0))
            stateset.addUniform(origin)

            coeffMatrix = osg.Uniform("coeffMatrix",
                osg.Matrix(1.0,0.0,1.0,0.0,
                            0.0,0.0,-1.0,0.0,
                            0.0,1.0,-1.0,0.0,
                            0.0,0.0,1.0,0.0))

            stateset.addUniform(coeffMatrix)
        elif shader=="texture" :
            vertex_shader = osg.Shader(osg.Shader.VERTEX, vertexShaderSource_texture)
            program.addShader(vertex_shader)

            image = 0

            if terrainFileName.empty() :
                image = osg.Image()
                tx = 38
                ty = 39
                image.allocateImage(tx,ty,1,GL_LUMINANCE,GL_FLOAT,1)
                for(unsigned int r=0r<ty++r)
                    for(unsigned int c=0c<tx++c)
                        *((float*)image.data(c,r)) = vertex[r+c*39][2]*0.1

                num_x = tx
                num_y = tx
            else :
                image = osgDB.readImageFile(terrainFileName)

                num_x = image.s()
                num_y = image.t()

            vertexTexture = osg.Texture2D(image)


            vertexTexture.setFilter(osg.Texture.MIN_FILTER,osg.Texture.NEAREST)
            vertexTexture.setFilter(osg.Texture.MAG_FILTER,osg.Texture.NEAREST)
            vertexTexture.setInternalFormat(GL_LUMINANCE_FLOAT32_ATI)
            stateset.setTextureAttributeAndModes(1,vertexTexture)

            vertexTextureSampler = osg.Uniform("vertexTexture",1)
            stateset.addUniform(vertexTextureSampler)


        fragment_shader = osg.Shader(osg.Shader.FRAGMENT, fragmentShaderSource)
        program.addShader(fragment_shader)

        texture = osg.Texture2D(osgDB.readImageFile(textureFileName))
        stateset.setTextureAttributeAndModes(0,texture)

        baseTextureSampler = osg.Uniform("baseTexture",0)
        stateset.addUniform(baseTextureSampler)



    # set up geometry data.

    vertices = osg.Vec3Array( num_x * num_y )
    
    dx = 1.0/(float)(num_x-1)
    dy = 1.0/(float)(num_y-1)
    row = osg.Vec3(0.0,0.0,0.0)
    
    vert_no = 0
    iy = unsigned int()
    for(iy=0 iy<num_y ++iy)
        column = row
        for(unsigned int ix=0ix<num_x++ix)
            (*vertices)[vert_no++] = column
            column.x() += dx
        row.y() += dy

    geom.setVertexArray(vertices)

    vbo = useVBO ? osg.VertexBufferObject : 0()
    if vbo : vertices.setVertexBufferObject(vbo)
    
    ebo = useVBO ? osg.ElementBufferObject : 0()

    for(iy=0 iy<num_y-1 ++iy)
        element_no = 0
        elements = osg.DrawElementsUInt(GL_TRIANGLE_STRIP, num_x*2)
        index = iy * num_x
        for(unsigned int ix = 0 ix<num_x ++ix)
            (*elements)[element_no++] = index + num_x
            (*elements)[element_no++] = index++
        geom.addPrimitiveSet(elements) 
        
        if ebo : elements.setElementBufferObject(ebo)
    
    geom.setUseVertexBufferObjects(useVBO)

    return geode

int main(int argc, char *argv[])
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrate support for ARB_vertex_program.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
   
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    shader = str("simple")
    while arguments.read("-s",shader) : 
    
    textureFileName = str("Images/lz.rgb")
    while arguments.read("-t",textureFileName) : 

    terrainFileName = str("")
    while arguments.read("-d",terrainFileName) : 

    dynamic = True
    while arguments.read("--static") :  dynamic = False 

    vbo = False
    while arguments.read("--vbo") :  vbo = True 

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1
    
    # load the nodes from the commandline arguments.
    model = createModel(shader,textureFileName,terrainFileName, dynamic, vbo)
    if !model :
        return 1
    
    viewer.setSceneData(model)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
