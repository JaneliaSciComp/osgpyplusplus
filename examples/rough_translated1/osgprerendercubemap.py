#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgprerendercubemap"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgViewer


# Translated from file 'osgprerendercubemap.cpp'

# OpenSceneGraph example, osgprerendercubemap.
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

#include <osg/Projection>
#include <osg/Geometry>
#include <osg/Texture>
#include <osg/TexGen>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osg/PolygonOffset>
#include <osg/CullFace>
#include <osg/TextureCubeMap>
#include <osg/TexMat>
#include <osg/MatrixTransform>
#include <osg/Light>
#include <osg/LightSource>
#include <osg/PolygonOffset>
#include <osg/CullFace>
#include <osg/Material>
#include <osg/PositionAttitudeTransform>
#include <osg/ArgumentParser>

#include <osg/Camera>
#include <osg/TexGenNode>

#include <iostream>

using namespace osg


def _create_scene():


    
  scene = Group()
  geode_1 = Geode()
  scene.addChild(geode_1.get())

  geode_2 = Geode()
  transform_2 = MatrixTransform()
  transform_2.addChild(geode_2.get())
  transform_2.setUpdateCallback(osg.AnimationPathCallback(Vec3(0, 0, 0), Y_AXIS, inDegrees(45.0)))
  scene.addChild(transform_2.get())

  geode_3 = Geode()
  transform_3 = MatrixTransform()
  transform_3.addChild(geode_3.get())
  transform_3.setUpdateCallback(osg.AnimationPathCallback(Vec3(0, 0, 0), Y_AXIS, inDegrees(-22.5)))
  scene.addChild(transform_3.get())

  radius = 0.8
  height = 1.0
  hints = TessellationHints()
  hints.setDetailRatio(2.0)
  shape = ref_ptr<ShapeDrawable>()

  shape = ShapeDrawable(Box(Vec3(0.0, -2.0, 0.0), 10, 0.1, 10), hints.get())
  shape.setColor(Vec4(0.5, 0.5, 0.7, 1.0))
  geode_1.addDrawable(shape.get())


  shape = ShapeDrawable(Sphere(Vec3(-3.0, 0.0, 0.0), radius), hints.get())
  shape.setColor(Vec4(0.6, 0.8, 0.8, 1.0))
  geode_2.addDrawable(shape.get())

  shape = ShapeDrawable(Box(Vec3(3.0, 0.0, 0.0), 2 * radius), hints.get())
  shape.setColor(Vec4(0.4, 0.9, 0.3, 1.0))
  geode_2.addDrawable(shape.get())

  shape = ShapeDrawable(Cone(Vec3(0.0, 0.0, -3.0), radius, height), hints.get())
  shape.setColor(Vec4(0.2, 0.5, 0.7, 1.0))
  geode_2.addDrawable(shape.get())

  shape = ShapeDrawable(Cylinder(Vec3(0.0, 0.0, 3.0), radius, height), hints.get())
  shape.setColor(Vec4(1.0, 0.3, 0.3, 1.0))
  geode_2.addDrawable(shape.get())

  shape = ShapeDrawable(Box(Vec3(0.0, 3.0, 0.0), 2, 0.1, 2), hints.get())
  shape.setColor(Vec4(0.8, 0.8, 0.4, 1.0))
  geode_3.addDrawable(shape.get())

  # material
  matirial = Material()
  matirial.setColorMode(Material.DIFFUSE)
  matirial.setAmbient(Material.FRONT_AND_BACK, Vec4(0, 0, 0, 1))
  matirial.setSpecular(Material.FRONT_AND_BACK, Vec4(1, 1, 1, 1))
  matirial.setShininess(Material.FRONT_AND_BACK, 64.0)
  scene.getOrCreateStateSet().setAttributeAndModes(matirial.get(), StateAttribute.ON)

  return scene

def createReflector():

    
  pat = osg.PositionAttitudeTransform()
  pat.setPosition(osg.Vec3(0.0,0.0,0.0))
  pat.setAttitude(osg.Quat(osg.inDegrees(0.0),osg.Vec3(0.0,0.0,1.0)))
  
  geode_1 = Geode()
  pat.addChild(geode_1)

  radius = 0.8
  hints = TessellationHints()
  hints.setDetailRatio(2.0)
  shape = ShapeDrawable(Sphere(Vec3(0.0, 0.0, 0.0), radius * 1.5), hints.get())
  shape.setColor(Vec4(0.8, 0.8, 0.8, 1.0))
  geode_1.addDrawable(shape)
  
  nodeList = osg.NodePath()
  nodeList.push_back(pat)
  nodeList.push_back(geode_1)
  
  return nodeList

class UpdateCameraAndTexGenCallback (osg.NodeCallback) :
    
        typedef std.vector< osg.Camera >  CameraList

        UpdateCameraAndTexGenCallback(osg.NodePath reflectorNodePath, CameraList Cameras):
            _reflectorNodePath(reflectorNodePath),
            _Cameras(Cameras)
       
        virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
            # first update subgraph to make sure objects are all moved into position
            traverse(node,nv)

            # compute the position of the center of the reflector subgraph
            worldToLocal = osg.computeWorldToLocal(_reflectorNodePath)
            bs = _reflectorNodePath.back().getBound()
            position = bs.center()

            typedef std.pair<osg.Vec3, osg.Vec3> ImageData
             ImageData id[] =
                ImageData( osg.Vec3( 1,  0,  0), osg.Vec3( 0, -1,  0) ), # +X
                ImageData( osg.Vec3(-1,  0,  0), osg.Vec3( 0, -1,  0) ), # -X
                ImageData( osg.Vec3( 0,  1,  0), osg.Vec3( 0,  0,  1) ), # +Y
                ImageData( osg.Vec3( 0, -1,  0), osg.Vec3( 0,  0, -1) ), # -Y
                ImageData( osg.Vec3( 0,  0,  1), osg.Vec3( 0, -1,  0) ), # +Z
                ImageData( osg.Vec3( 0,  0, -1), osg.Vec3( 0, -1,  0) )  # -Z
            

            for(unsigned int i=0 
                i<6  i<_Cameras.size()
                ++i)
                localOffset = osg.Matrix()
                localOffset.makeLookAt(position,position+id[i].first,id[i].second)
                
                viewMatrix = worldToLocal*localOffset
            
                _Cameras[i].setReferenceFrame(osg.Camera.ABSOLUTE_RF)
                _Cameras[i].setProjectionMatrixAsFrustum(-1.0,1.0,-1.0,1.0,1.0,10000.0)
                _Cameras[i].setViewMatrix(viewMatrix)
    
        virtual ~UpdateCameraAndTexGenCallback() 
        
        _reflectorNodePath = osg.NodePath()        
        _Cameras = CameraList()


class TexMatCullCallback (osg.NodeCallback) :
    
        TexMatCullCallback(osg.TexMat* texmat):
            _texmat(texmat)
       
        virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
            # first update subgraph to make sure objects are all moved into position
            traverse(node,nv)
            
            cv = dynamic_cast<osgUtil.CullVisitor*>(nv)
            if cv :
                quat = cv.getModelViewMatrix().getRotate()
                _texmat.setMatrix(osg.Matrix.rotate(quat.inverse()))
    
        _texmat = TexMat()



def createShadowedScene(reflectedSubgraph, reflectorNodePath, unit, clearColor, tex_width, tex_height, renderImplementation):


    

    group = osg.Group()
    
    texture = osg.TextureCubeMap()
    texture.setTextureSize(tex_width, tex_height)

    texture.setInternalFormat(GL_RGB)
    texture.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_EDGE)
    texture.setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_EDGE)
    texture.setWrap(osg.Texture.WRAP_R, osg.Texture.CLAMP_TO_EDGE)
    texture.setFilter(osg.TextureCubeMap.MIN_FILTER,osg.TextureCubeMap.LINEAR)
    texture.setFilter(osg.TextureCubeMap.MAG_FILTER,osg.TextureCubeMap.LINEAR)
    
    # set up the render to texture cameras.
    Cameras = UpdateCameraAndTexGenCallback.CameraList()
    for(unsigned int i=0 i<6 ++i)
        # create the camera
        camera = osg.Camera()

        camera.setClearMask(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        camera.setClearColor(clearColor)

        # set viewport
        camera.setViewport(0,0,tex_width,tex_height)

        # set the camera to render before the main camera.
        camera.setRenderOrder(osg.Camera.PRE_RENDER)

        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(renderImplementation)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture, 0, i)

        # add subgraph to render
        camera.addChild(reflectedSubgraph)
        
        group.addChild(camera)
        
        Cameras.push_back(camera)
   
    # create the texgen node to project the tex coords onto the subgraph
    texgenNode = osg.TexGenNode()
    texgenNode.getTexGen().setMode(osg.TexGen.REFLECTION_MAP)
    texgenNode.setTextureUnit(unit)
    group.addChild(texgenNode)

    # set the reflected subgraph so that it uses the texture and tex gen settings.    
        reflectorNode = reflectorNodePath.front()
        group.addChild(reflectorNode)
                
        stateset = reflectorNode.getOrCreateStateSet()
        stateset.setTextureAttributeAndModes(unit,texture,osg.StateAttribute.ON)
        stateset.setTextureMode(unit,GL_TEXTURE_GEN_S,osg.StateAttribute.ON)
        stateset.setTextureMode(unit,GL_TEXTURE_GEN_T,osg.StateAttribute.ON)
        stateset.setTextureMode(unit,GL_TEXTURE_GEN_R,osg.StateAttribute.ON)
        stateset.setTextureMode(unit,GL_TEXTURE_GEN_Q,osg.StateAttribute.ON)

        texmat = osg.TexMat()
        stateset.setTextureAttributeAndModes(unit,texmat,osg.StateAttribute.ON)
        
        reflectorNode.setCullCallback(TexMatCullCallback(texmat))
    
    # add the reflector scene to draw just as normal
    group.addChild(reflectedSubgraph)
    
    # set an update callback to keep moving the camera and tex gen in the right direction.
    group.setUpdateCallback(UpdateCameraAndTexGenCallback(reflectorNodePath, Cameras))

    return group


def main(argc, argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = ArgumentParser(argc, argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName() + " is the example which demonstrates using of GL_ARB_shadow extension implemented in osg.Texture class")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName())
    arguments.getApplicationUsage().addCommandLineOption("-h or --help", "Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--fbo","Use Frame Buffer Object for render to texture, where supported.")
    arguments.getApplicationUsage().addCommandLineOption("--fb","Use FrameBuffer for render to texture.")
    arguments.getApplicationUsage().addCommandLineOption("--pbuffer","Use Pixel Buffer for render to texture, where supported.")
    arguments.getApplicationUsage().addCommandLineOption("--window","Use a separate Window for render to texture.")
    arguments.getApplicationUsage().addCommandLineOption("--width","Set the width of the render to texture")
    arguments.getApplicationUsage().addCommandLineOption("--height","Set the height of the render to texture")

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1
    
    tex_width = 256
    tex_height = 256
    while arguments.read("--width", tex_width) : 
    while arguments.read("--height", tex_height) : 

    renderImplementation = osg.Camera.FRAME_BUFFER_OBJECT
    
    while arguments.read("--fbo") :  renderImplementation = osg.Camera.FRAME_BUFFER_OBJECT 
    while arguments.read("--pbuffer") :  renderImplementation = osg.Camera.PIXEL_BUFFER 
    while arguments.read("--fb") :  renderImplementation = osg.Camera.FRAME_BUFFER 
    while arguments.read("--window") :  renderImplementation = osg.Camera.SEPERATE_WINDOW 
    

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
      arguments.writeErrorMessages(std.cout)
      return 1

    scene = MatrixTransform()
    scene.setMatrix(osg.Matrix.rotate(osg.DegreesToRadians(125.0),1.0,0.0,0.0))

    reflectedSubgraph = _create_scene()    
    if !reflectedSubgraph.valid() : return 1

    reflectedScene = createShadowedScene(reflectedSubgraph.get(), createReflector(), 0, viewer.getCamera().getClearColor(),
                                                        tex_width, tex_height, renderImplementation)

    scene.addChild(reflectedScene.get())

    viewer.setSceneData(scene.get())

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
