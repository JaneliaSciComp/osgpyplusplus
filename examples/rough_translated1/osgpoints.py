#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgpoints"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgpoints.cpp'

# OpenSceneGraph example, osgpoints.
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

#include <osgDB/ReadFile>
#include <osgUtil/Optimizer>
#include <osgViewer/Viewer>

#include <osg/Point>
#include <osg/BlendFunc>
#include <osg/Texture2D>
#include <osg/PointSprite>
#include <osg/PolygonMode>

#include <iostream>

class KeyboardEventHandler (osgGA.GUIEventHandler) :
    
        KeyboardEventHandler(osg.StateSet* stateset):
            _stateset(stateset)
            _point = osg.Point()
            _point.setDistanceAttenuation(osg.Vec3(0.0,0.0000,0.05))
            _stateset.setAttribute(_point)
    
        virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
            switch(ea.getEventType())
                case(osgGA.GUIEventAdapter.KEYDOWN):
                    if ea.getKey()==ord("+")  or  ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Add :
                       changePointSize(1.0)
                       return True
                    elif ea.getKey()==ord("-")  or  ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Subtract :
                       changePointSize(-1.0)
                       return True
                    elif ea.getKey()==ord("<") :
                       changePointAttenuation(1.1)
                       return True
                    elif ea.getKey()==ord(">") :
                       changePointAttenuation(1.0/1.1)
                       return True
                    break
                default:
                    break
            return False
        
        
        def getPointSize():
        
        
            
            return _point.getSize()
        
        def setPointSize(psize):
        
            
            if psize>0.0 :
                _point.setSize(psize)
            print "Point size ", psize

        def changePointSize(delta):

            
            setPointSize(getPointSize()+delta)

        def changePointAttenuation(scale):

            
            _point.setDistanceAttenuation(_point.getDistanceAttenuation()*scale)
        
        _stateset = osg.StateSet()
        _point = osg.Point()
        


def main(argv):

    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)
    
    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" example provides an interactive viewer for visualising point clouds..")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--sprites","Point sprites.")
    arguments.getApplicationUsage().addCommandLineOption("--points","Sets the polygon mode to GL_POINT for front and back faces.")


    # construct the viewer.
    viewer = osgViewer.Viewer()

    shader = False
    while arguments.read("--shader") : shader = True

    # if user request help write it out to cout.
    if arguments.read("-h")  or  arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1
    
    usePointSprites = False
    while arguments.read("--sprites") :  usePointSprites = True 

    forcePointMode = False
    while arguments.read("--points") :  forcePointMode = True 

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    # read the scene from the list of file specified commandline args.
    loadedModel = osgDB.readNodeFiles(arguments)

    # if no model has been successfully loaded report failure.
    if  not loadedModel : 
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # optimize the scene graph, remove redundant nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel)


    # set the scene to render
    viewer.setSceneData(loadedModel)
    

    stateset = loadedModel.getOrCreateStateSet()
    if usePointSprites :    
        #/ Setup cool blending
        fn = osg.BlendFunc()
        stateset.setAttributeAndModes(fn, osg.StateAttribute.ON)

        #/ Setup the point sprites
        sprite = osg.PointSprite()
        stateset.setTextureAttributeAndModes(0, sprite, osg.StateAttribute.ON)

        #/ The texture for the sprites
        tex = osg.Texture2D()
        tex.setImage(osgDB.readImageFile("Images/particle.rgb"))
        stateset.setTextureAttributeAndModes(0, tex, osg.StateAttribute.ON)

    if  forcePointMode  :
        #/ Set polygon mode to GL_POINT
        pm = osg.PolygonMode(
            osg.PolygonMode.FRONT_AND_BACK, osg.PolygonMode.POINT )
        stateset.setAttributeAndModes( pm, osg.StateAttribute.ON | osg.StateAttribute.OVERRIDE)
    

    # register the handler for modifying the point size
    viewer.addEventHandler(KeyboardEventHandler(viewer.getCamera().getOrCreateStateSet()))


    if shader :
        stateset = loadedModel.getOrCreateStateSet()
    
        #################################/
        # vertex shader using just Vec4 coefficients
        char vertexShaderSource[] = 
            "void main(void) \n"
            " \n"
            "\n"
            "    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex\n"
            "\n"



        program = osg.Program()
        stateset.setAttribute(program)

        vertex_shader = osg.Shader(osg.Shader.VERTEX, vertexShaderSource)
        program.addShader(vertex_shader)

#if 0
        #################################
        # fragment shader
        #
        char fragmentShaderSource[] = 
            "void main(void) \n"
            " \n"
            "    gl_FragColor = gl_Color \n"
            "\n"

        fragment_shader = osg.Shader(osg.Shader.FRAGMENT, fragmentShaderSource)
        program.addShader(fragment_shader)
#endif

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
