#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgdistortion"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgdistortion.cpp'

# OpenSceneGraph example, osgdistortion.
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

#include <osg/GLExtensions>
#include <osg/Node>
#include <osg/Geometry>
#include <osg/Notify>
#include <osg/MatrixTransform>
#include <osg/Texture2D>
#include <osg/Stencil>
#include <osg/ColorMask>
#include <osg/Depth>
#include <osg/Billboard>
#include <osg/Material>
#include <osg/Projection>
#include <osg/TextureCubeMap>
#include <osg/io_utils>


#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>
#include <osgGA/KeySwitchMatrixManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/AnimationPathManipulator>
#include <osgGA/TerrainManipulator>

#include <osgUtil/SmoothingVisitor>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <iostream>

using namespace osg

def createDistortionSubgraph(subgraph, clearColour):

    
    distortionNode = osg.Group()

    tex_width = 1024
    tex_height = 1024

    texture = osg.Texture2D()
    texture.setTextureSize(tex_width, tex_height)
    texture.setInternalFormat(GL_RGBA)
    texture.setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
    texture.setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)

    # set up the render to texture camera.
        camera = osg.Camera()

        # set clear the color and depth buffer
        camera.setClearColor(clearColour)
        camera.setClearMask(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # just inherit the main cameras view
        camera.setReferenceFrame(osg.Transform.RELATIVE_RF)
        camera.setProjectionMatrix(osg.Matrixd.identity())
        camera.setViewMatrix(osg.Matrixd.identity())

        # set viewport
        camera.setViewport(0,0,tex_width,tex_height)

        # set the camera to render before the main camera.
        camera.setRenderOrder(osg.Camera.PRE_RENDER)

        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(osg.Camera.FRAME_BUFFER_OBJECT)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture)

        # add subgraph to render
        camera.addChild(subgraph)

        distortionNode.addChild(camera)

    # set up the hud camera
        # create the quad to visualize.
        polyGeom = osg.Geometry()

        polyGeom.setSupportsDisplayList(False)

        origin = osg.Vec3(0.0,0.0,0.0)
        xAxis = osg.Vec3(1.0,0.0,0.0)
        yAxis = osg.Vec3(0.0,1.0,0.0)
        height = 1024.0
        width = 1280.0
        noSteps = 50

        vertices = osg.Vec3Array()
        texcoords = osg.Vec2Array()
        colors = osg.Vec4Array()

        bottom = origin
        dx = xAxis*(width/((float)(noSteps-1)))
        dy = yAxis*(height/((float)(noSteps-1)))

        bottom_texcoord = osg.Vec2(0.0,0.0)
        dx_texcoord = osg.Vec2(1.0/(float)(noSteps-1),0.0)
        dy_texcoord = osg.Vec2(0.0,1.0/(float)(noSteps-1))

        int i,j
        for(i=0i<noSteps++i)
            cursor = bottom+dy*(float)i
            texcoord = bottom_texcoord+dy_texcoord*(float)i
            for(j=0j<noSteps++j)
                vertices.push_back(cursor)
                texcoords.push_back(osg.Vec2((sin(texcoord.x()*osg.PI-osg.PI*0.5)+1.0)*0.5,(sin(texcoord.y()*osg.PI-osg.PI*0.5)+1.0)*0.5))
                colors.push_back(osg.Vec4(1.0,1.0,1.0,1.0))

                cursor += dx
                texcoord += dx_texcoord

        # pass the created vertex array to the points geometry object.
        polyGeom.setVertexArray(vertices)

        polyGeom.setColorArray(colors, osg.Array.BIND_PER_VERTEX)

        polyGeom.setTexCoordArray(0,texcoords)


        for(i=0i<noSteps-1++i)
            elements = osg.DrawElementsUShort(osg.PrimitiveSet.QUAD_STRIP)
            for(j=0j<noSteps++j)
                elements.push_back(j+(i+1)*noSteps)
                elements.push_back(j+(i)*noSteps)
            polyGeom.addPrimitiveSet(elements)


        # we need to add the texture to the Drawable, we do so by creating a
        # StateSet to contain the Texture StateAttribute.
        stateset = polyGeom.getOrCreateStateSet()
        stateset.setTextureAttributeAndModes(0, texture,osg.StateAttribute.ON)
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

        geode = osg.Geode()
        geode.addDrawable(polyGeom)

        # set up the camera to render the textured quad
        camera = osg.Camera()

        # just inherit the main cameras view
        camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
        camera.setViewMatrix(osg.Matrix.identity())
        camera.setProjectionMatrixAsOrtho2D(0,1280,0,1024)

        # set the camera to render before the main camera.
        camera.setRenderOrder(osg.Camera.NESTED_RENDER)

        # add subgraph to render
        camera.addChild(geode)

        distortionNode.addChild(camera)
    return distortionNode

def setDomeFaces(viewer, arguments):

    

    wsi = osg.GraphicsContext.getWindowingSystemInterface()
    if  not wsi :
        osg.notify(osg.NOTICE), "Error, no WindowSystemInterface available, cannot create windows."
        return

    unsigned int width, height
    wsi.getScreenResolution(osg.GraphicsContext.ScreenIdentifier(0), width, height)

    while arguments.read("--width",width) : 
    while arguments.read("--height",height) : 

    traits = osg.GraphicsContext.Traits()
    traits.x = 0
    traits.y = 0
    traits.width = width
    traits.height = height
    traits.windowDecoration = True
    traits.doubleBuffer = True
    traits.sharedContext = 0

    gc = osg.GraphicsContext.createGraphicsContext(traits)
    if  not gc :
        osg.notify(osg.NOTICE), "GraphicsWindow has not been created successfully."
        return


    center_x = width/2
    center_y = height/2
    camera_width = 256
    camera_height = 256

    # front face
        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(center_x-camera_width/2, center_y, camera_width, camera_height))

        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd())

    # top face
        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(center_x-camera_width/2, center_y+camera_height, camera_width, camera_height))
        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(-90.0), 1.0,0.0,0.0))

    # left face
        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(center_x-camera_width*3/2, center_y, camera_width, camera_height))
        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(-90.0), 0.0,1.0,0.0))

    # right face
        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(center_x+camera_width/2, center_y, camera_width, camera_height))
        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(90.0), 0.0,1.0,0.0))

    # bottom face
        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(center_x-camera_width/2, center_y-camera_height, camera_width, camera_height))
        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(90.0), 1.0,0.0,0.0))

    # back face
        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(center_x-camera_width/2, center_y-2*camera_height, camera_width, camera_height))
        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(-180.0), 1.0,0.0,0.0))

    viewer.getCamera().setProjectionMatrixAsPerspective(90.0, 1.0, 1, 1000.0)

    viewer.assignSceneDataToCameras()

def createDomeDistortionMesh(origin, widthVector, heightVector, arguments):

    
    sphere_radius = 1.0
    if arguments.read("--radius", sphere_radius) : 

    collar_radius = 0.45
    if arguments.read("--collar", collar_radius) : 

    center = osg.Vec3d(0.0,0.0,0.0)
    eye = osg.Vec3d(0.0,0.0,0.0)

    distance = sqrt(sphere_radius*sphere_radius - collar_radius*collar_radius)
    if arguments.read("--distance", distance) : 

    centerProjection = False

    projector = eye - osg.Vec3d(0.0,0.0, distance)


    osg.notify(osg.NOTICE), "Projector position = ", projector
    osg.notify(osg.NOTICE), "distance = ", distance


    # create the quad to visualize.
    geometry = osg.Geometry()

    geometry.setSupportsDisplayList(False)

    xAxis = osg.Vec3(widthVector)
    width = widthVector.length()
    xAxis /= width

    yAxis = osg.Vec3(heightVector)
    height = heightVector.length()
    yAxis /= height

    noSteps = 50

    vertices = osg.Vec3Array()
    texcoords = osg.Vec3Array()
    colors = osg.Vec4Array()

    bottom = origin
    dx = xAxis*(width/((float)(noSteps-1)))
    dy = yAxis*(height/((float)(noSteps-1)))

    screenCenter = origin + widthVector*0.5 + heightVector*0.5
    screenRadius = heightVector.length() * 0.5

    int i,j
    if centerProjection :
        for(i=0i<noSteps++i)
            cursor = bottom+dy*(float)i
            for(j=0j<noSteps++j)
                delta = osg.Vec2(cursor.x() - screenCenter.x(), cursor.y() - screenCenter.y())
                theta = atan2(-delta.y(), delta.x())
                phi = osg.PI_2 * delta.length() / screenRadius
                if phi > osg.PI_2 : phi = osg.PI_2

                phi *= 2.0

                # osg.notify(osg.NOTICE), "theta = ", theta, "phi=", phi

                texcoord = osg.Vec3(sin(phi) * cos(theta),
                                   sin(phi) * sin(theta),
                                   cos(phi))

                vertices.push_back(cursor)
                colors.push_back(osg.Vec4(1.0,1.0,1.0,1.0))
                texcoords.push_back(texcoord)

                cursor += dx
            # osg.notify(osg.NOTICE)
    else:
        for(i=0i<noSteps++i)
            cursor = bottom+dy*(float)i
            for(j=0j<noSteps++j)
                delta = osg.Vec2(cursor.x() - screenCenter.x(), cursor.y() - screenCenter.y())
                theta = atan2(-delta.y(), delta.x())
                phi = osg.PI_2 * delta.length() / screenRadius
                if phi > osg.PI_2 : phi = osg.PI_2

                # osg.notify(osg.NOTICE), "theta = ", theta, "phi=", phi

                f = distance * sin(phi)
                e = distance * cos(phi) + sqrt( sphere_radius*sphere_radius - f*f)
                l = e * cos(phi)
                h = e * sin(phi)
                z = l - distance

                texcoord = osg.Vec3(h * cos(theta) / sphere_radius,
                                   h * sin(theta) / sphere_radius,
                                   z / sphere_radius)

                vertices.push_back(cursor)
                colors.push_back(osg.Vec4(1.0,1.0,1.0,1.0))
                texcoords.push_back(texcoord)

                cursor += dx
            # osg.notify(osg.NOTICE)

    # pass the created vertex array to the points geometry object.
    geometry.setVertexArray(vertices)

    geometry.setColorArray(colors, osg.Array.BIND_PER_VERTEX)

    geometry.setTexCoordArray(0,texcoords)

    for(i=0i<noSteps-1++i)
        elements = osg.DrawElementsUShort(osg.PrimitiveSet.QUAD_STRIP)
        for(j=0j<noSteps++j)
            elements.push_back(j+(i+1)*noSteps)
            elements.push_back(j+(i)*noSteps)
        geometry.addPrimitiveSet(elements)

    return geometry

def setDomeCorrection(viewer, arguments):

    

    wsi = osg.GraphicsContext.getWindowingSystemInterface()
    if  not wsi :
        osg.notify(osg.NOTICE), "Error, no WindowSystemInterface available, cannot create windows."
        return

    unsigned int width, height
    wsi.getScreenResolution(osg.GraphicsContext.ScreenIdentifier(0), width, height)

    while arguments.read("--width",width) : 
    while arguments.read("--height",height) : 

    traits = osg.GraphicsContext.Traits()
    traits.x = 0
    traits.y = 0
    traits.width = width
    traits.height = height
    traits.windowDecoration = False
    traits.doubleBuffer = True
    traits.sharedContext = 0



    gc = osg.GraphicsContext.createGraphicsContext(traits)
    if  not gc :
        osg.notify(osg.NOTICE), "GraphicsWindow has not been created successfully."
        return

    tex_width = 512
    tex_height = 512

    camera_width = tex_width
    camera_height = tex_height

    texture = osg.TextureCubeMap()

    texture.setTextureSize(tex_width, tex_height)
    texture.setInternalFormat(GL_RGB)
    texture.setFilter(osg.Texture.MIN_FILTER,osg.Texture.LINEAR)
    texture.setFilter(osg.Texture.MAG_FILTER,osg.Texture.LINEAR)

#if 0
    renderTargetImplementation = osg.Camera.SEPERATE_WINDOW
    buffer = GL_FRONT
#else:
    renderTargetImplementation = osg.Camera.FRAME_BUFFER_OBJECT
    buffer = GL_FRONT
#endif

    # front face
        camera = osg.Camera()
        camera.setName("Front face camera")
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(0,0,camera_width, camera_height))
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setAllowEventFocus(False)
        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(renderTargetImplementation)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture, 0, osg.TextureCubeMap.POSITIVE_Y)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd())


    # top face
        camera = osg.Camera()
        camera.setName("Top face camera")
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(0,0,camera_width, camera_height))
        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setAllowEventFocus(False)

        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(renderTargetImplementation)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture, 0, osg.TextureCubeMap.POSITIVE_Z)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(-90.0), 1.0,0.0,0.0))

    # left face
        camera = osg.Camera()
        camera.setName("Left face camera")
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(0,0,camera_width, camera_height))
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setAllowEventFocus(False)

        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(renderTargetImplementation)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture, 0, osg.TextureCubeMap.NEGATIVE_X)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(-90.0), 0.0,1.0,0.0) * osg.Matrixd.rotate(osg.inDegrees(-90.0), 0.0,0.0,1.0))

    # right face
        camera = osg.Camera()
        camera.setName("Right face camera")
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(0,0,camera_width, camera_height))
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setAllowEventFocus(False)

        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(renderTargetImplementation)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture, 0, osg.TextureCubeMap.POSITIVE_X)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(90.0), 0.0,1.0,0.0 ) * osg.Matrixd.rotate(osg.inDegrees(90.0), 0.0,0.0,1.0))

    # bottom face
        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setName("Bottom face camera")
        camera.setViewport(osg.Viewport(0,0,camera_width, camera_height))
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setAllowEventFocus(False)

        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(renderTargetImplementation)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture, 0, osg.TextureCubeMap.NEGATIVE_Z)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(90.0), 1.0,0.0,0.0) * osg.Matrixd.rotate(osg.inDegrees(180.0), 0.0,0.0,1.0))

    # back face
        camera = osg.Camera()
        camera.setName("Back face camera")
        camera.setGraphicsContext(gc)
        camera.setViewport(osg.Viewport(0,0,camera_width, camera_height))
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setAllowEventFocus(False)

        # tell the camera to use OpenGL frame buffer object where supported.
        camera.setRenderTargetImplementation(renderTargetImplementation)

        # attach the texture and use it as the color buffer.
        camera.attach(osg.Camera.COLOR_BUFFER, texture, 0, osg.TextureCubeMap.NEGATIVE_Y)

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd.rotate(osg.inDegrees(180.0), 1.0,0.0,0.0))

    viewer.getCamera().setProjectionMatrixAsPerspective(90.0, 1.0, 1, 1000.0)



    # distortion correction set up.
        geode = osg.Geode()
        geode.addDrawable(createDomeDistortionMesh(osg.Vec3(0.0,0.0,0.0), osg.Vec3(width,0.0,0.0), osg.Vec3(0.0,height,0.0), arguments))

        # we need to add the texture to the mesh, we do so by creating a
        # StateSet to contain the Texture StateAttribute.
        stateset = geode.getOrCreateStateSet()
        stateset.setTextureAttributeAndModes(0, texture,osg.StateAttribute.ON)
        stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

        camera = osg.Camera()
        camera.setGraphicsContext(gc)
        camera.setClearMask(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT )
        camera.setClearColor( osg.Vec4(0.1,0.1,1.0,1.0) )
        camera.setViewport(osg.Viewport(0, 0, width, height))
        buffer =  GL_BACK if (traits.doubleBuffer) else  GL_FRONT
        camera.setDrawBuffer(buffer)
        camera.setReadBuffer(buffer)
        camera.setReferenceFrame(osg.Camera.ABSOLUTE_RF)
        camera.setAllowEventFocus(False)
        #camera.setInheritanceMask(camera.getInheritanceMask()  ~osg.CullSettings.CLEAR_COLOR  ~osg.CullSettings.COMPUTE_NEAR_FAR_MODE)
        #camera.setComputeNearFarMode(osg.CullSettings.DO_NOT_COMPUTE_NEAR_FAR)

        camera.setProjectionMatrixAsOrtho2D(0,width,0,height)
        camera.setViewMatrix(osg.Matrix.identity())

        # add subgraph to render
        camera.addChild(geode)

        camera.setName("DistortionCorrectionCamera")

        viewer.addSlave(camera, osg.Matrixd(), osg.Matrixd(), False)

    viewer.getCamera().setNearFarRatio(0.0001)


def main(argv):


    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # load the nodes from the commandline arguments.
    loadedModel = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default mode instead.
    if  not loadedModel : loadedModel = osgDB.readNodeFile("cow.osgt")

    if  not loadedModel :
        print arguments.getApplicationName(), ": No data loaded"
        return 1


    if arguments.read("--dome")  or  arguments.read("--puffer")  :

        setDomeCorrection(viewer, arguments)

        viewer.setSceneData( loadedModel )
    elif arguments.read("--faces") :

        setDomeFaces(viewer, arguments)

        viewer.setSceneData( loadedModel )
    else:
        distortionNode = createDistortionSubgraph( loadedModel, viewer.getCamera().getClearColor())
        viewer.setSceneData( distortionNode )

    while arguments.read("--sky-light") :
        viewer.setLightingMode(osg.View.SKY_LIGHT)

    if viewer.getLightingMode()==osg.View.HEADLIGHT :
        viewer.getLight().setPosition(osg.Vec4(0.0,0.0,0.0,1.0))


    # load the nodes from the commandline arguments.
    if  not viewer.getSceneData() :
        osg.notify(osg.NOTICE), "Please specify a model filename on the command line."
        return 1


    # set up the camera manipulators.
        keyswitchManipulator = osgGA.KeySwitchMatrixManipulator()

        keyswitchManipulator.addMatrixManipulator( ord("1"), "Trackball", osgGA.TrackballManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("2"), "Flight", osgGA.FlightManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("3"), "Drive", osgGA.DriveManipulator() )
        keyswitchManipulator.addMatrixManipulator( ord("4"), "Terrain", osgGA.TerrainManipulator() )

        pathfile = str()
        keyForAnimationPath = ord("5")
        while arguments.read("-p",pathfile) :
            apm = osgGA.AnimationPathManipulator(pathfile)
            if apm  or   not apm.valid() :
                num = keyswitchManipulator.getNumMatrixManipulators()
                keyswitchManipulator.addMatrixManipulator( keyForAnimationPath, "Path", apm )
                keyswitchManipulator.selectMatrixManipulator(num)
                ++keyForAnimationPath

        viewer.setCameraManipulator( keyswitchManipulator )

    viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    # add the state manipulator
    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
