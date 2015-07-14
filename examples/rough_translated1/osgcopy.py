#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgcopy"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgcopy.cpp'

# OpenSceneGraph example, osgcopy.
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

#include <osg/MatrixTransform>
#include <osg/Billboard>
#include <osg/Geode>
#include <osg/Group>
#include <osg/Notify>
#include <osg/Texture>

#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osgViewer/Viewer>

#include <osgUtil/Optimizer>

#include <iostream>

# Customize the CopyOp so that we add our own verbose 
# output of what's being copied.
class MyCopyOp (osg.CopyOp) :
    
        inline MyCopyOp(CopyFlags flags=SHALLOW_COPY):
            osg.CopyOp(flags),
            _indent(0),
            _step(4) 

        inline void moveIn()   _indent += _step 
        inline void moveOut()   _indent -= _step 
        inline void writeIndent()  
            for(int i=0i<_indent++i) print " "
    
        virtual osg.Referenced*     operator() ( osg.Referenced* ref) 
            writeIndent() print "copying Referenced ", ref
            moveIn()
            ret_ref = CopyOp.operator()(ref)
            moveOut()
            return ret_ref
        
        virtual osg.Object*         operator() ( osg.Object* obj) 
            writeIndent() print "copying Object ", obj
            if obj : print " ", obj.className()
            print std.endl
            moveIn()
            ret_obj = CopyOp.operator()(obj)
            moveOut()
            return ret_obj
        
        virtual osg.Node*           operator() ( osg.Node* node) 
            writeIndent() print "copying Node ", node
            if node : print " ", node.className(), " '", node.getName(), "'"
            print std.endl
            moveIn()
            ret_node = CopyOp.operator()(node)
            moveOut()
            return ret_node

        virtual osg.Drawable*       operator() ( osg.Drawable* drawable) 
            writeIndent() print "copying Drawable ", drawable
            if drawable : print " ", drawable.className()
            print std.endl
            moveIn()
            ret_drawable = CopyOp.operator()(drawable)
            moveOut()
            return ret_drawable

        virtual osg.StateSet*       operator() ( osg.StateSet* stateset) 
            writeIndent() print "copying StateSet ", stateset
            if stateset : print " ", stateset.className()
            print std.endl
            moveIn()
            ret_stateset = CopyOp.operator()(stateset)
            moveOut()
            return ret_stateset

        virtual osg.StateAttribute* operator() ( osg.StateAttribute* attr) 
            writeIndent() print "copying StateAttribute ", attr
            if attr : print " ", attr.className()
            print std.endl
            moveIn()
            ret_attr = CopyOp.operator()(attr)
            moveOut()
            return ret_attr

        virtual osg.Texture*        operator() ( osg.Texture* text) 
            writeIndent() print "copying Texture ", text
            if text : print " ", text.className()
            print std.endl
            moveIn()
            ret_text = CopyOp.operator()(text)
            moveOut()
            return ret_text

        virtual osg.Image*          operator() ( osg.Image* image) 
            writeIndent() print "copying Image ", image
            if image : print " ", image.className()
            print std.endl
            moveIn()
            ret_image = CopyOp.operator()(image)
            moveOut()
            return ret_image
    
        # must be mutable since CopyOp is passed around as  to
        # the various clone/copy constructors.
        mutable int _indent
        mutable int _step


# this CopyOp class will preserve the multi-parent structure of the copied 
# object, instead of expanding it into a tree. Works with the 
# DEEP_COPY_NODES flag.
class GraphCopyOp (osg.CopyOp) :
    
        inline GraphCopyOp(CopyFlags flags=SHALLOW_COPY):
            osg.CopyOp(flags)  _nodeCopyMap.clear()
            
        virtual osg.Node* operator() ( osg.Node* node) 
            if node  and  _flagsDEEP_COPY_NODES :
                if  node.getNumParents() > 1  :
                    if  _nodeCopyMap.find(node)  not = _nodeCopyMap.end()  :
                        print "Copy of node ", node, " ", node.getName(), ", ", _nodeCopyMap[node], ", will be reused"
                        return (osg.Node*)(_nodeCopyMap[node])
                    else:
                        newNode = dynamic_cast<osg.Node*>( node.clone(*this) )
                        _nodeCopyMap[node] = newNode
                        return newNode
                else:
                    return dynamic_cast<osg.Node*>( node.clone(*this) )
            else:
                return const_cast<osg.Node*>(node)
    
        # must be mutable since CopyOp is passed around as  to
        # the various clone/copy constructors.
        mutable std.map< osg.Node*,osg.Node*> _nodeCopyMap



def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # initialize the viewer.
    viewer = osgViewer.Viewer()

    # load the nodes from the commandline arguments.
    rootnode = osgDB.readNodeFiles(arguments)
    if  not rootnode :
        osg.notify(osg.NOTICE), "Please specify a model filename on the command line."
        return 1
    
    # run optimization over the scene graph
    optimzer = osgUtil.Optimizer()
    optimzer.optimize(rootnode)
    
# -------------    Start of copy specific code -------------------------------------------------------
    
    # do a deep copy, using MyCopyOp to reveal whats going on under the good,
    # in your own code you'd typically just use the basic osg.CopyOp something like
    mycopy = dynamic_cast<osg.Node*>(rootnode.clone(osg.CopyOp.DEEP_COPY_ALL))
    print "Doing a deep copy of scene graph"

    # note, we need the dyanmic_cast because MS Visual Studio can't handle covarient
    # return types, so that clone has return just Object*.  bahh hum bug
    deep_copy = dynamic_cast<osg.Node*>(rootnode.clone(MyCopyOp(osg.CopyOp.DEEP_COPY_ALL)))
    
    print "----------------------------------------------------------------"

    # do a graph preserving deep copy.
    print "Doing a graph preserving deep copy of scene graph nodes"
    graph_copy = dynamic_cast<osg.Node*>(rootnode.clone(GraphCopyOp(osg.CopyOp.DEEP_COPY_NODES)))


    # do a shallow copy.
    print "Doing a shallow copy of scene graph"
    shallow_copy = dynamic_cast<osg.Node*>(rootnode.clone(MyCopyOp(osg.CopyOp.SHALLOW_COPY)))


    # write out the various scene graphs so that they can be browsed, either
    # in an editor or using a graphics diff tool gdiff/xdiff/xxdiff.
    print std.endl, "Writing out the original scene graph as 'original.osgt'"
    osgDB.writeNodeFile(*rootnode,"original.osgt")

    print std.endl, "Writing out the graph preserving scene graph as 'graph_copy.osgt'"
    osgDB.writeNodeFile(*graph_copy,"graph_copy.osgt")

    print "Writing out the deep copied scene graph as 'deep_copy.osgt'"
    osgDB.writeNodeFile(*deep_copy,"deep_copy.osgt")

    print "Writing out the shallow copied scene graph as 'shallow_copy.osgt'"
    osgDB.writeNodeFile(*shallow_copy,"shallow_copy.osgt")


    # You can use a bit mask to control which parts of the scene graph are shallow copied
    # vs deep copied.  The options are (from include/osg/CopyOp) :
    # enum Options 
    #        SHALLOW_COPY = 0,
    #        DEEP_COPY_OBJECTS = 1,
    #        DEEP_COPY_NODES = 2,
    #        DEEP_COPY_DRAWABLES = 4,
    #        DEEP_COPY_STATESETS = 8,
    #        DEEP_COPY_STATEATTRIBUTES = 16,
    #        DEEP_COPY_TEXTURES = 32,
    #        DEEP_COPY_IMAGES = 64,
    #        DEEP_COPY_ALL = 0xffffffff
    # 
    # 
    # These options you can use together such as :
    #    osg.Node* mycopy = dynamic_cast<osg.Node*>(rootnode.clone(osg.CopyOp.DEEP_COPY_NODES | DEEP_COPY_DRAWABLES))
    # Which shares state but creates copies of all nodes and drawables (which contain the geometry).
    # 
    # You may also want to subclass from CopyOp to provide finer grained control of what gets shared (shallow copy) vs
    # cloned (deep copy).
    


# -------------    End of copy specific code -------------------------------------------------------
     
    # set the scene to render
    viewer.setSceneData(rootnode)

    # viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
