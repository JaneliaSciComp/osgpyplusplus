#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgvertexattributes"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgvertexattributes.cpp'

# OpenSceneGraph example, osgvertexattributes.
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

#include <osgUtil/ShaderGen>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>

class ConvertToVertexAttibArrays (osg.NodeVisitor) :

        typedef std.pair<unsigned int, str> AttributeAlias

        ConvertToVertexAttibArrays():
            osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN)
            _manualVertexAliasing = False

            # mappings taken from http:#www.opengl.org/registry/specs/NV/vertex_program.txt
            _vertexAlias = AttributeAlias(0, "osg_Vertex")
            _normalAlias = AttributeAlias(2, "osg_Normal")
            _colorAlias = AttributeAlias(3, "osg_Color")
            _secondaryColorAlias = AttributeAlias(4, "osg_SecondaryColor")
            _fogCoordAlias = AttributeAlias(5, "osg_FogCoord")
            _texCoordAlias[0] = AttributeAlias(8, "osg_MultiTexCoord0")
            _texCoordAlias[1] = AttributeAlias(9, "osg_MultiTexCoord1")
            _texCoordAlias[2] = AttributeAlias(10, "osg_MultiTexCoord2")
            _texCoordAlias[3] = AttributeAlias(11, "osg_MultiTexCoord3")
            _texCoordAlias[4] = AttributeAlias(12, "osg_MultiTexCoord4")
            _texCoordAlias[5] = AttributeAlias(13, "osg_MultiTexCoord5")
            _texCoordAlias[6] = AttributeAlias(14, "osg_MultiTexCoord6")
            _texCoordAlias[7] = AttributeAlias(15, "osg_MultiTexCoord7")

        def bindAttribute(program, alias):

            
                program.addBindAttribLocation(alias.second, alias.first)

        def replaceAndBindAttrib(program, source, originalStr, alias, declarationPrefix):

            
            if replace(source, originalStr, alias.second) :
                source.insert(0, declarationPrefix + alias.second + str("\n"))
                if _manualVertexAliasing : bindAttribute(program, alias)

        def replaceBuiltInUniform(source, originalStr, newStr, declarationPrefix):

            
            if replace(source, originalStr, newStr) :
                source.insert(0, declarationPrefix + newStr + str("\n"))

        def convertVertexShader(program, shader):

            
            source = shader.getShaderSource()

            # replace ftransform as it only works with built-ins
            replace(source, "ftransform()", "gl_ModelViewProjectionMatrix * gl_Vertex")

#if 1
            replaceAndBindAttrib(program, source, "gl_Normal", _normalAlias, "attribute vec3 ")
            replaceAndBindAttrib(program, source, "gl_Vertex", _vertexAlias, "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_Color", _colorAlias, "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_SecondaryColor", _secondaryColorAlias, "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_FogCoord", _fogCoordAlias, "attribute float ")

            replaceAndBindAttrib(program, source, "gl_MultiTexCoord0", _texCoordAlias[0], "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_MultiTexCoord1", _texCoordAlias[1], "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_MultiTexCoord2", _texCoordAlias[2], "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_MultiTexCoord3", _texCoordAlias[3], "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_MultiTexCoord4", _texCoordAlias[4], "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_MultiTexCoord5", _texCoordAlias[5], "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_MultiTexCoord6", _texCoordAlias[6], "attribute vec4 ")
            replaceAndBindAttrib(program, source, "gl_MultiTexCoord7", _texCoordAlias[7], "attribute vec4 ")
#endif

#if 1
            # replace built in uniform
            replaceBuiltInUniform(source, "gl_ModelViewMatrix", "osg_ModeViewMatrix", "uniform mat4 ")
            replaceBuiltInUniform(source, "gl_ModelViewProjectionMatrix", "osg_ModelViewProjectionMatrix", "uniform mat4 ")
            replaceBuiltInUniform(source, "gl_ProjectionMatrix", "osg_ProjectionMatrix", "uniform mat4 ")
#endif
            shader.setShaderSource(source)

        def convertFragmentShader(program, shader):

            

        def reset():

            
            _visited.clear()

        def apply(node):

            
            if _visited.count(node) not =0 : return
            _visited.insert(node)

            if node.getStateSet() : apply(*(node.getStateSet()))
            traverse(node)

        def apply(geode):

            
            if _visited.count(geode) not =0 : return
            _visited.insert(geode)

            if geode.getStateSet() : apply(*(geode.getStateSet()))

            for(unsigned int i=0 i<geode.getNumDrawables() ++i)
                if geode.getDrawable(i).getStateSet() : apply(*(geode.getDrawable(i).getStateSet()))

                geom = geode.getDrawable(i).asGeometry()
                if geom : apply(*geom)

        def replace(str, original_phrase, new_phrase):

            
            replacedStr = False
            pos = 0
            while pos=str.find(original_phrase, pos) : not =str.npos :
                endOfPhrasePos = pos+original_phrase.size()
                if endOfPhrasePos<str.size() :
                    c = str[endOfPhrasePos]
                    if c>=ord("0")  and  c<=ord("9") :  or 
                        (c>=ord("a")  and  c<=ord("z"))  or 
                        (c>=ord("A")  and  c<=ord("Z")) :
                        pos = endOfPhrasePos
                        continue

                replacedStr = True
                str.replace(pos, original_phrase.size(), new_phrase)
            return replacedStr

        def apply(program, shader):

            
             if _visited.count(shader) not =0 : return
            _visited.insert(shader)

            osg.notify(osg.NOTICE), "Shader ", shader.getTypename(), " ----before-----------"
            osg.notify(osg.NOTICE), shader.getShaderSource()

            if shader.getType()==osg.Shader.VERTEX : convertVertexShader(program, shader)
            elif shader.getType()==osg.Shader.FRAGMENT : convertFragmentShader(program, shader)

            osg.notify(osg.NOTICE), "--after-----------"
            osg.notify(osg.NOTICE), shader.getShaderSource()
            osg.notify(osg.NOTICE), "---------------------"

        def apply(stateset):

            
             if _visited.count(stateset) not =0 : return
            _visited.insert(stateset)

            return

            osg.notify(osg.NOTICE), "Found stateset ", stateset
            program = dynamic_cast<osg.Program*>(stateset.getAttribute(osg.StateAttribute.PROGRAM))
            if program :
                osg.notify(osg.NOTICE), "   Found Program ", program
                for(unsigned int i=0 i<program.getNumShaders() ++i)
                    apply(*program, *(program.getShader(i)))


        def apply(geom):

            
            geom.setUseDisplayList(False)

            if  not _manualVertexAliasing : return

            osg.notify(osg.NOTICE), "Found geometry ", geom
            if geom.getVertexArray() :
                setVertexAttrib(geom, _vertexAlias, geom.getVertexArray(), False, osg.Array.BIND_PER_VERTEX)
                geom.setVertexArray(0)

            if geom.getNormalArray() :
                setVertexAttrib(geom, _normalAlias, geom.getNormalArray(), True)
                geom.setNormalArray(0)

            if geom.getColorArray() :
                setVertexAttrib(geom, _colorAlias, geom.getColorArray(), False)
                geom.setColorArray(0)

            if geom.getSecondaryColorArray() :
                setVertexAttrib(geom, _secondaryColorAlias, geom.getSecondaryColorArray(), False)
                geom.setSecondaryColorArray(0)

            if geom.getFogCoordArray() :
                # should we normalize the FogCoord array? Don't think so...
                setVertexAttrib(geom, _fogCoordAlias, geom.getFogCoordArray(), False)
                geom.setFogCoordArray(0)

            maxNumTexCoords = geom.getNumTexCoordArrays()
            if maxNumTexCoords>8 :
                osg.notify(osg.NOTICE), "Warning: Ignoring ", maxNumTexCoords-8, " texture coordinate arrays, only 8 are currently supported in vertex attribute conversion code."
                maxNumTexCoords = 8
            for(unsigned int i=0 i<maxNumTexCoords ++i)
                if geom.getTexCoordArray(i) :
                    setVertexAttrib(geom, _texCoordAlias[i], geom.getTexCoordArray(i), False, osg.Array.BIND_PER_VERTEX)
                    geom.setTexCoordArray(i,0)
                else:
                    osg.notify(osg.NOTICE), "Found empty TexCoordArray(", i, ")"

        def setVertexAttrib(geom, alias, array, normalize, binding):

            
            index = alias.first
            name = alias.second
            array.setName(name)
            if binding not =osg.Array.BIND_UNDEFINED : array.setBinding(binding)
            array.setNormalize(normalize)
            geom.setVertexAttribArray(index, array)

            osg.notify(osg.NOTICE), "   vertex attrib(", name, ", index=", index, ", normalize=", normalize, " binding=", binding, ")"


        typedef std.set<osg.Object*> Visited
        _visited = Visited()

        _manualVertexAliasing = bool()
        _vertexAlias = AttributeAlias()
        _normalAlias = AttributeAlias()
        _colorAlias = AttributeAlias()
        _secondaryColorAlias = AttributeAlias()
        _fogCoordAlias = AttributeAlias()
        AttributeAlias _texCoordAlias[8]


def createSimpleTestModel():

    
    group = osg.Group()

    geode = osg.Geode()
    group.addChild(geode)

    geometry = osg.Geometry()
    geode.addDrawable(geometry)

    vertices = osg.Vec3Array()
    vertices.push_back(osg.Vec3(0.0,0.0,0.0))
    vertices.push_back(osg.Vec3(0.0,0.0,1.0))
    vertices.push_back(osg.Vec3(1.0,0.0,0.0))
    vertices.push_back(osg.Vec3(1.0,0.0,1.0))
    geometry.setVertexArray(vertices)

    geometry.addPrimitiveSet(osg.DrawArrays(GL_TRIANGLE_STRIP, 0, 4))

    char vertexShaderSource[] =
       "void main(void)\n"
       "\n"
       "    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex\n"
       "\n"

    char fragmentShaderSource[] =
        "void main(void)\n"
        "\n"
        "    gl_FragColor = vec4(1.0,1.0,0.0,1.0) \n"
        "\n"

    program = osg.Program()
    program.addShader(osg.Shader(osg.Shader.VERTEX, vertexShaderSource))
    program.addShader(osg.Shader(osg.Shader.FRAGMENT, fragmentShaderSource))

    geometry.getOrCreateStateSet().setAttribute(program)

    return group

def createSimpleTextureTestModel():

    
    group = osg.Group()

    geode = osg.Geode()
    group.addChild(geode)

    geometry = osg.Geometry()
    geode.addDrawable(geometry)

    vertices = osg.Vec3Array()
    vertices.push_back(osg.Vec3(0.0,0.0,0.0))
    vertices.push_back(osg.Vec3(0.0,0.0,1.0))
    vertices.push_back(osg.Vec3(1.0,0.0,0.0))
    vertices.push_back(osg.Vec3(1.0,0.0,1.0))
    geometry.setVertexArray(vertices)

    texcoords = osg.Vec2Array()
    texcoords.push_back(osg.Vec2(0.0,0.0))
    texcoords.push_back(osg.Vec2(0.0,1.0))
    texcoords.push_back(osg.Vec2(1.0,0.0))
    texcoords.push_back(osg.Vec2(1.0,1.0))
    geometry.setTexCoordArray(0, texcoords)

    geometry.addPrimitiveSet(osg.DrawArrays(GL_TRIANGLE_STRIP, 0, 4))

    char vertexShaderSource[] =
       "varying vec2 texCoord\n"
       "void main(void)\n"
       "\n"
       "    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex\n"
       "    texCoord = gl_MultiTexCoord0.xy\n"
       "\n"

    char fragmentShaderSource[] =
        "varying vec2 texCoord\n"
        "uniform sampler2D baseTexture\n"
        "void main(void)\n"
        "\n"
        "    gl_FragColor = texture2D(baseTexture, texCoord) \n"
        "\n"

    program = osg.Program()
    program.addShader(osg.Shader(osg.Shader.VERTEX, vertexShaderSource))
    program.addShader(osg.Shader(osg.Shader.FRAGMENT, fragmentShaderSource))

    stateset = geometry.getOrCreateStateSet()
    stateset.setAttribute(program)

    image = osgDB.readImageFile("Images/lz.rgb")
    texture = osg.Texture2D(image)
    texture.setFilter(osg.Texture.MIN_FILTER, osg.Texture.LINEAR)
    texture.setFilter(osg.Texture.MAG_FILTER, osg.Texture.LINEAR)
    stateset.setTextureAttribute(0, texture)

    baseTextureSampler = osg.Uniform("baseTexture",0)
    stateset.addUniform(baseTextureSampler)

    return group

int main(int argc, char *argv[])
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    outputFileName = str()
    while arguments.read("-o",outputFileName) : 

    loadedModel = osg.Node()

    runConvertToVertexAttributes = False
    if arguments.read("--simple")  or  arguments.read("--s") :
        loadedModel = createSimpleTestModel()
    elif arguments.read("--texture")  or  arguments.read("-t") :
        loadedModel = createSimpleTextureTestModel()
    else:
        runShaderGen = True
        while arguments.read("--shader-gen") :  runShaderGen = True 
        while arguments.read("--no-shader-gen") :  runShaderGen = False 

        while arguments.read("--vertex-attrib") :  runConvertToVertexAttributes = True 
        while arguments.read("--no-vertex-attrib") :  runConvertToVertexAttributes = False 

        loadedModel = osgDB.readNodeFiles(arguments)
        if  not loadedModel :
            osg.notify(osg.NOTICE), "No model loaded, please specify a model filename."
            return 1

        if runShaderGen :
            # convert fixed function pipeline to shaders
            sgv = osgUtil.ShaderGenVisitor()
            loadedModel.accept(sgv)

        if runConvertToVertexAttributes :
            # find any conventional vertex, colour, normal and tex coords arrays and convert to vertex attributes
            ctvaa = ConvertToVertexAttibArrays()
            loadedModel.accept(ctvaa)

    if  not loadedModel : return 1

    if  not outputFileName.empty() :
        osgDB.writeNodeFile(*loadedModel, outputFileName)
        return 0

    # add a viewport to the viewer and attach the scene graph.
    viewer.setSceneData(loadedModel)

    viewer.setCameraManipulator(osgGA.TrackballManipulator())

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    viewer.realize()


    if runConvertToVertexAttributes :
        # switch on the uniforms that track the modelview and projection matrices
        windows = osgViewer.Viewer.Windows()
        viewer.getWindows(windows)
        for(osgViewer.Viewer.Windows.iterator itr = windows.begin()
            not = windows.end()
            ++itr)
            (*itr).getState().setUseModelViewAndProjectionUniforms(True)
            (*itr).getState().setUseVertexAttributeAliasing(True)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
