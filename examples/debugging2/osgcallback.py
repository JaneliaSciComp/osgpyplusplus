#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgcallback"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgcallback.cpp'

# OpenSceneGraph example, osgcallback.
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

#include <osg/Transform>
#include <osg/Billboard>
#include <osg/Geode>
#include <osg/Group>
#include <osg/Notify>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgGA/TrackballManipulator>
#include <osgGA/FlightManipulator>
#include <osgGA/DriveManipulator>

#include <osgUtil/Optimizer>

#include <iostream>

class UpdateCallback (osg.NodeCallback) :
virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
            print "update callback - pre traverse", node
            traverse(node,nv)
            print "update callback - post traverse", node


class CullCallback (osg.NodeCallback) :
virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
            print "cull callback - pre traverse", node
            traverse(node,nv)
            print "cull callback - post traverse", node


class DrawableDrawCallback (osg.Drawable.DrawCallback) :
def drawImplementation(renderInfo, drawable):
    
            print "draw call back - pre drawImplementation", drawable
            drawable.drawImplementation(renderInfo)
            print "draw call back - post drawImplementation", drawable


class DrawableUpdateCallback (osg.Drawable.UpdateCallback) :
virtual void update(osg.NodeVisitor*, osg.Drawable* drawable)
        print "Drawable update callback ", drawable


class DrawableCullCallback (osg.Drawable.CullCallback) :
#* do customized cull code.
    virtual bool cull(osg.NodeVisitor*, osg.Drawable* drawable, osg.State* #state) 
        print "Drawable cull callback ", drawable
        return False


class InsertCallbacksVisitor (osg.NodeVisitor) :
   
        InsertCallbacksVisitor():osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN)
        
        def apply(node):
        
            
             node.setUpdateCallback(UpdateCallback())
             node.setCullCallback(CullCallback())
             traverse(node)

        def apply(geode):

            
            geode.setUpdateCallback(UpdateCallback())
            
            #note, it makes no sense to attach a cull callback to the node
            #at there are no nodes to traverse below the geode, only
            #drawables, and as such the Cull node callbacks is ignored.
            #If you wish to control the culling of drawables
            #then use a drawable cullback...

            for(unsigned int i=0i<geode.getNumDrawables()++i)
                geode.getDrawable(i).setUpdateCallback(DrawableUpdateCallback())
                geode.getDrawable(i).setCullCallback(DrawableCullCallback())
                geode.getDrawable(i).setDrawCallback(DrawableDrawCallback())
        
        def apply(node):
        
            
            apply((osg.Node)node)


class MyReadFileCallback (osgDB.Registry.ReadFileCallback) :
    def readNode(fileName, options):
        
        print "before readNode"
        # note when calling the Registry to do the read you have to call readNodeImplementation NOT readNode, as this will
        # cause on infinite recusive loop.
        result = osgDB.Registry.instance().readNodeImplementation(fileName,options)
        print "after readNode"
        return result


class CameraUpdateCallback (osg.NodeCallback) :
virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
        print "Camera update callback - pre traverse", node
        traverse(node,nv)
        print "Camera update callback - post traverse", node


class CameraEventCallback (osg.NodeCallback) :
virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
        print "Camera event callback - pre traverse", node
        traverse(node,nv)
        print "Camera event callback - post traverse", node


def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)
   
    # set the osgDB.Registy read file callback to catch all requests for reading files.
    osgDB.Registry.instance().setReadFileCallback(MyReadFileCallback())
   
    # initialize the viewer.
    viewer = osgViewer.Viewer()

    # load the nodes from the commandline arguments.
    rootnode = osgDB.readNodeFiles(arguments)

    # if not loaded assume no arguments passed in, try use default mode instead.
    if  not rootnode : rootnode = osgDB.readNodeFile("cow.osgt")

    if  not rootnode :
        osg.notify(osg.NOTICE), "Please specify a file on the command line"

        return 1
    
    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(rootnode)
     
    # insert all the callbacks
    icv = InsertCallbacksVisitor()
    rootnode.accept(icv)

    viewer.getCamera().setUpdateCallback(CameraUpdateCallback())
    viewer.getCamera().setEventCallback(CameraEventCallback())

    # set the scene to render
    viewer.setSceneData(rootnode)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
