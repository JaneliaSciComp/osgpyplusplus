#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgshadercomposition"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgViewer


# Translated from file 'osgshadercomposition.cpp'

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

#include <osgViewer/Viewer>
#include <osgDB/ReadFile>
#include <osg/ShaderAttribute>
#include <osg/PositionAttitudeTransform>

def createSceneGraph(arguments):

    
    node = osgDB.readNodeFiles(arguments)
    if  not node : return 0

    group = osg.Group()
    spacing = node.getBound().radius() * 2.0

    position = osg.Vec3d(0.0,0.0,0.0)

    sa1 = NULL

        stateset = group.getOrCreateStateSet()
        sa = osg.ShaderAttribute()
        sa.setType(osg.StateAttribute.Type(10000))
        sa1 = sa
        stateset.setAttribute(sa)

            vertex_shader = osg.Shader(osg.Shader.VERTEX)
            vertex_shader.addCodeInjection(-1,"varying vec4 color\n")
            vertex_shader.addCodeInjection(-1,"varying vec4 texcoord\n")
            vertex_shader.addCodeInjection(0,"color = gl_Color\n")
            vertex_shader.addCodeInjection(0,"texcoord = gl_MultiTexCoord0\n")
            vertex_shader.addCodeInjection(0,"gl_Position = ftransform()\n")
            sa.addShader(vertex_shader)

            fragment_shader = osg.Shader(osg.Shader.FRAGMENT)
            fragment_shader.addCodeInjection(-1,"varying vec4 color\n")
            fragment_shader.addCodeInjection(-1,"varying vec4 texcoord\n")
            fragment_shader.addCodeInjection(-1,"uniform sampler2D baseTexture \n")
            fragment_shader.addCodeInjection(0,"gl_FragColor = color * texture2DProj( baseTexture, texcoord )\n")

            sa.addShader(fragment_shader)

        sa.addUniform(osg.Uniform("baseTexture",0))


    # inherit the ShaderComponents entirely from above
        pat = osg.PositionAttitudeTransform()
        pat.setPosition(position)
        pat.addChild(node)

        position.x() += spacing

        group.addChild(pat)


        pat = osg.PositionAttitudeTransform()
        pat.setPosition(position)
        pat.addChild(node)

        position.x() += spacing

        stateset = pat.getOrCreateStateSet()
        stateset.setMode(GL_BLEND, osg.StateAttribute.ON)

        sa = osg.ShaderAttribute()
        sa.setType(osg.StateAttribute.Type(10001))
        stateset.setAttribute(sa)

            fragment_shader = osg.Shader(osg.Shader.FRAGMENT)
            fragment_shader.addCodeInjection(0.9,"gl_FragColor.a = gl_FragColor.a*0.5\n")

            sa.addShader(fragment_shader)

        group.addChild(pat)

    # resuse the first ShaderAttribute's type and ShaderComponent, just use uniform
        pat = osg.PositionAttitudeTransform()
        pat.setPosition(position)
        pat.addChild(node)

        position.x() += spacing

        stateset = pat.getOrCreateStateSet()
        sa = osg.ShaderAttribute(*sa1)
        stateset.setAttribute(sa)

        # reuse the same ShaderComponent as the first branch
        sa.addUniform(osg.Uniform("myColour",osg.Vec4(1.0,1.0,0.0,1.0)))

        group.addChild(pat)



    # resuse the first ShaderAttribute's type and ShaderComponent, just use uniform
        pat = osg.PositionAttitudeTransform()
        pat.setPosition(position)
        pat.addChild(node)

        position.x() += spacing

        stateset = pat.getOrCreateStateSet()
        sa = osg.ShaderAttribute()
        sa.setType(osg.StateAttribute.Type(10000))
        stateset.setAttribute(sa)
        stateset.setMode(GL_BLEND, osg.StateAttribute.ON)
        stateset.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)

            vertex_shader = osg.Shader(osg.Shader.VERTEX)
            vertex_shader.addCodeInjection(0,"gl_Position = ftransform()\n")

            sa.addShader(vertex_shader)

            fragment_shader = osg.Shader(osg.Shader.FRAGMENT)
            fragment_shader.addCodeInjection(-1,"uniform vec4 newColour\n")
            fragment_shader.addCodeInjection(-1,"uniform float osg_FrameTime\n")
            fragment_shader.addCodeInjection(0,"gl_FragColor = vec4(newColour.r,newColour.g,newColour.b, 0.5+sin(osg_FrameTime*2.0)*0.5)\n")

            sa.addShader(fragment_shader)
            sa.addUniform(osg.Uniform("newColour",osg.Vec4(1.0,1.0,1.0,0.5)))

        group.addChild(pat)


    return group

def main(argv):

    
    arguments = osg.ArgumentParser(argv)

    viewer = osgViewer.Viewer(arguments)

    scenegraph = createSceneGraph(arguments)
    if  not scenegraph : return 1

    viewer.setSceneData(scenegraph)

    viewer.realize()

    # enable shader composition
    windows = osgViewer.Viewer.Windows()
    viewer.getWindows(windows)
    for(osgViewer.Viewer.Windows.iterator itr = windows.begin()
        not = windows.end()
        ++itr)
        (*itr).getState().setShaderCompositionEnabled(True)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
