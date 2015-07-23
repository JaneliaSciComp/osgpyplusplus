#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgcallback"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
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


class UpdateCallback (osg.NodeCallback):
    def __init__(self):
        super(UpdateCallback, self).__init__()

    def __call__(self, node, nv):
        print "update callback - pre traverse", node
        self.traverse(node,nv)
        print "update callback - post traverse", node


class CullCallback (osg.NodeCallback):
    def __init__(self):
        super(CullCallback, self).__init__()
        
    def __call__(self, node, nv):
        print "cull callback - pre traverse", node
        self.traverse(node,nv)
        print "cull callback - post traverse", node


class DrawableDrawCallback (osg.Drawable.DrawCallback):
    def __init__(self):
        super(DrawableDrawCallback, self).__init__()

    def drawImplementation(self, renderInfo, drawable):    
        print "draw call back - pre drawImplementation", drawable
        drawable.drawImplementation(renderInfo)
        print "draw call back - post drawImplementation", drawable


class DrawableUpdateCallback (osg.Drawable.UpdateCallback) :
    def __init__(self):
        super(DrawableUpdateCallback, self).__init__()

    def update(self, visitor, drawable):
        print "Drawable update callback ", drawable


class DrawableCullCallback (osg.Drawable.CullCallback) :
    def __init__(self):
        super(DrawableCullCallback, self).__init__()

    #* do customized cull code.
    def cull(self, visitor, drawable, state):
        print "Drawable cull callback ", drawable
        return False


class InsertCallbacksVisitor (osg.NodeVisitor) :  
    def __init__(self):
        super(InsertCallbacksVisitor, self).__init__(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN)
    
    def apply_node(self, node):
        node.setUpdateCallback(UpdateCallback())
        node.setCullCallback(CullCallback())
        self.traverse(node)

    def apply_geode(self, geode):
        geode.setUpdateCallback(UpdateCallback())
        #note, it makes no sense to attach a cull callback to the node
        #at there are no nodes to traverse below the geode, only
        #drawables, and as such the Cull node callbacks is ignored.
        #If you wish to control the culling of drawables
        #then use a drawable cullback...
        for i in range(geode.getNumDrawables()):
            geode.getDrawable(i).setUpdateCallback(DrawableUpdateCallback())
            geode.getDrawable(i).setCullCallback(DrawableCullCallback())
            geode.getDrawable(i).setDrawCallback(DrawableDrawCallback())
    
    def apply_transform(self, transform):
        self.apply_node(transform)
        
    def apply(self, node):
        if isinstance(node, osg.Geode):
            self.apply_geode(node)
        else:
            self.apply_node(node)


class MyReadFileCallback (osgDB.Registry.ReadFileCallback) :
    def __init__(self):
        super(MyReadFileCallback, self).__init__()

    def readNode(self, fileName, options):
        print "before readNode"
        # note when calling the Registry to do the read you have to call readNodeImplementation NOT readNode, as this will
        # cause on infinite recusive loop.
        result = osgDB.Registry.instance().readNodeImplementation(fileName, options)
        print "after readNode"
        return result


class CameraUpdateCallback (osg.NodeCallback) :
    def __init__(self):
        super(CameraUpdateCallback, self).__init__()

    def __call__(self, node, nv):
        print "Camera update callback - pre traverse", node
        self.traverse(node,nv)
        print "Camera update callback - post traverse", node


class CameraEventCallback (osg.NodeCallback) :
    def __init__(self):
        super(CameraEventCallback, self).__init__()

    def __call__(self, node, nv):
        print "Camera event callback - pre traverse", node
        self.traverse(node,nv)
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
    if rootnode is None:
        rootnode = osgDB.readNodeFile("cow.osgt")
    if rootnode is None:
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
