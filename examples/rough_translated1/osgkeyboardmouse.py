#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgkeyboardmouse"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgFX
from osgpypp import osgGA
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgkeyboardmouse.
*
*  Permission is hereby granted, free of charge, to any person obtaining a copy
*  of this software and associated documentation files (the "Software"), to deal
*  in the Software without restriction, including without limitation the rights
*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
*  copies of the Software, and to permit persons to whom the Software is
*  furnished to do so, subject to the following conditions:
*
*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
*  THE SOFTWARE.


# Simple example of use of osgViewer.GraphicsWindow + Viewer
# example that provides the user with control over view position with basic picking.

#include <osg/Timer>
#include <osg/io_utils>
#include <osg/observer_ptr>

#include <osgUtil/IntersectionVisitor>
#include <osgUtil/PolytopeIntersector>
#include <osgUtil/LineSegmentIntersector>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>

#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>

#include <osgViewer/Viewer>

#include <osgFX/Scribe>

#include <iostream>

class CreateModelToSaveVisitor : public osg.NodeVisitor
public:

    CreateModelToSaveVisitor():
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN)        
        _group = new osg.Group
        _addToModel = false
    
    virtual void apply(osg.Node node)
        scribe =  dynamic_cast<osgFX.Scribe*>(node)
        if scribe :
            for(unsigned int i=0 i<scribe.getNumChildren() ++i)
                _group.addChild(scribe.getChild(i))
        else:
            traverse(node)
    
    osg.ref_ptr<osg.Group> _group
    _addToModel = bool()


class DeleteSelectedNodesVisitor : public osg.NodeVisitor
public:

    DeleteSelectedNodesVisitor():
        osg.NodeVisitor(osg.NodeVisitor.TRAVERSE_ALL_CHILDREN)        
    
    virtual void apply(osg.Node node)
        scribe =  dynamic_cast<osgFX.Scribe*>(node)
        if scribe :
            _selectedNodes.push_back(scribe)
        else:
            traverse(node)
    
    def pruneSelectedNodes():
        for(SelectedNodes.iterator itr = _selectedNodes.begin()
            itr != _selectedNodes.end()
            ++itr)
            node =  itr.get()
            parents =  node.getParents()
            for(osg.Node.ParentList.iterator pitr = parents.begin()
                pitr != parents.end()
                ++pitr)
                parent =  *pitr
                parent.removeChild(node)
    
    typedef std.vector< osg.ref_ptr<osgFX.Scribe> > SelectedNodes
    _selectedNodes = SelectedNodes()
    


# class to handle events with a pick
class PickHandler : public osgGA.GUIEventHandler 
public: 

    PickHandler():
        _mx(0.0),_my(0.0),
        _usePolytopeIntersector(false),
        _useWindowCoordinates(false) 

    ~PickHandler() 

    def handle(ea, aa):
        viewer =  dynamic_cast<osgViewer.Viewer*>(aa)
        if !viewer : return false

        switch(ea.getEventType())
            case(osgGA.GUIEventAdapter.KEYUP):
                if ea.getKey()=='s' :
                    saveSelectedModel(viewer.getSceneData())
                else: if ea.getKey()=='o' :
                    osg.notify(osg.NOTICE), "Saved model to file 'saved_model.osgt'"
                    osgDB.writeNodeFile(*(viewer.getSceneData()), "saved_model.osgt")
                else: if ea.getKey()=='p' :
                    _usePolytopeIntersector = !_usePolytopeIntersector
                    if _usePolytopeIntersector :
                        osg.notify(osg.NOTICE), "Using PolytopeIntersector"
                     else: 
                        osg.notify(osg.NOTICE), "Using LineSegmentIntersector"
                else: if ea.getKey()=='c' :
                    _useWindowCoordinates = !_useWindowCoordinates
                    if _useWindowCoordinates :
                        osg.notify(osg.NOTICE), "Using window coordinates for picking"
                     else: 
                        osg.notify(osg.NOTICE), "Using projection coordiates for picking"
                else: if ea.getKey()==osgGA.GUIEventAdapter.KEY_Delete || ea.getKey()==osgGA.GUIEventAdapter.KEY_BackSpace :
                    osg.notify(osg.NOTICE), "Delete"
                    dsnv = DeleteSelectedNodesVisitor()
                    viewer.getSceneData().accept(dsnv)
                    dsnv.pruneSelectedNodes()
                false = return()
            case(osgGA.GUIEventAdapter.PUSH):
            case(osgGA.GUIEventAdapter.MOVE):
                _mx = ea.getX()
                _my = ea.getY()
                false = return()
            case(osgGA.GUIEventAdapter.RELEASE):
                if _mx == ea.getX()  _my == ea.getY() :
                    # only do a pick if the mouse hasn't moved
                    pick(ea,viewer)
                true = return()

            default:
                false = return()

    def pick(ea, viewer):
        scene =  viewer.getSceneData()
        if !scene : return

        osg.notify(osg.NOTICE)

        node =  0
        parent =  0

        if _usePolytopeIntersector :
            picker = osgUtil.PolytopeIntersector*()
            if _useWindowCoordinates :
                # use window coordinates
                # remap the mouse x,y into viewport coordinates.
                viewport =  viewer.getCamera().getViewport()
                mx =  viewport.x() + (int)((double )viewport.width()*(ea.getXnormalized()*0.5+0.5))
                my =  viewport.y() + (int)((double )viewport.height()*(ea.getYnormalized()*0.5+0.5))

                # half width, height.
                w =  5.0f
                h =  5.0f
                picker = new osgUtil.PolytopeIntersector( osgUtil.Intersector.WINDOW, mx-w, my-h, mx+w, my+h )
             else: 
                mx =  ea.getXnormalized()
                my =  ea.getYnormalized()
                w =  0.05
                h =  0.05
                picker = new osgUtil.PolytopeIntersector( osgUtil.Intersector.PROJECTION, mx-w, my-h, mx+w, my+h )
            iv = osgUtil.IntersectionVisitor(picker)

            viewer.getCamera().accept(iv)

            if picker.containsIntersections() :
                intersection =  picker.getFirstIntersection()

                osg.notify(osg.NOTICE), "Picked ", intersection.localIntersectionPoint, "  Distance to ref. plane ", intersection.distance, ", max. dist ", intersection.maxDistance, ", primitive index ", intersection.primitiveIndex, ", numIntersectionPoints ", intersection.numIntersectionPoints

                nodePath =  intersection.nodePath
                node = (nodePath.size()>=1)?nodePath[nodePath.size()-1]:0
                parent = (nodePath.size()>=2)?dynamic_cast<osg.Group*>(nodePath[nodePath.size()-2]):0

                if node : print "  Hits ", node.className(), " nodePath size ", nodePath.size()    
                toggleScribe(parent, node)

        else:
            picker = osgUtil.LineSegmentIntersector*()
            if !_useWindowCoordinates :
                # use non dimensional coordinates - in projection/clip space
                picker = new osgUtil.LineSegmentIntersector( osgUtil.Intersector.PROJECTION, ea.getXnormalized(),ea.getYnormalized() )
             else: 
                # use window coordinates
                # remap the mouse x,y into viewport coordinates.
                viewport =  viewer.getCamera().getViewport()
                mx =  viewport.x() + (int)((float)viewport.width()*(ea.getXnormalized()*0.5f+0.5f))
                my =  viewport.y() + (int)((float)viewport.height()*(ea.getYnormalized()*0.5f+0.5f))
                picker = new osgUtil.LineSegmentIntersector( osgUtil.Intersector.WINDOW, mx, my )
            iv = osgUtil.IntersectionVisitor(picker)

            viewer.getCamera().accept(iv)

            if picker.containsIntersections() :
                intersection =  picker.getFirstIntersection()
                osg.notify(osg.NOTICE), "Picked ", intersection.localIntersectionPoint

                nodePath =  intersection.nodePath
                node = (nodePath.size()>=1)?nodePath[nodePath.size()-1]:0
                parent = (nodePath.size()>=2)?dynamic_cast<osg.Group*>(nodePath[nodePath.size()-2]):0

                if node : print "  Hits ", node.className(), " nodePath size", nodePath.size()
                toggleScribe(parent, node)

        # now we try to decorate the hit node by the osgFX.Scribe to show that its been "picked"

    def toggleScribe(parent, node):
        if !parent || !node : return

        print "  parent ", parent.className()

        parentAsScribe =  dynamic_cast<osgFX.Scribe*>(parent)
        if !parentAsScribe :
            # node not already picked, so highlight it with an osgFX.Scribe
            scribe =  new osgFX.Scribe()
            scribe.addChild(node)
            parent.replaceChild(node,scribe)
        else:
            # node already picked so we want to remove scribe to unpick it.
            parentList =  parentAsScribe.getParents()
            for(osg.Node.ParentList.iterator itr=parentList.begin()
                itr!=parentList.end()
                ++itr)
                (*itr).replaceChild(parentAsScribe,node)


    def saveSelectedModel(scene):
        if !scene : return
    
        cmtsv = CreateModelToSaveVisitor()
        scene.accept(cmtsv)
        
        if cmtsv._group.getNumChildren()>0 :
            print "Writing selected compoents to 'selected_model.osgt'"
            osgDB.writeNodeFile(*cmtsv._group, "selected_model.osgt")

protected:

    float _mx,_my
    _usePolytopeIntersector = bool()
    _useWindowCoordinates = bool()


def main(argc, argv):
    osg.ref_ptr<osg.Node> loadedModel
    
    # load the scene.
    if argc>1 : loadedModel = osgDB.readNodeFile(argv[1])
    
    # if not loaded assume no arguments passed in, try use default mode instead.
    if !loadedModel : loadedModel = osgDB.readNodeFile("dumptruck.osgt")
    
    if !loadedModel : 
        print argv[0], ": No data loaded."
        return 1
    
    # create the window to draw to.
    osg.ref_ptr<osg.GraphicsContext.Traits> traits = new osg.GraphicsContext.Traits
    traits.x = 200
    traits.y = 200
    traits.width = 800
    traits.height = 600
    traits.windowDecoration = true
    traits.doubleBuffer = true
    traits.sharedContext = 0

    osg.ref_ptr<osg.GraphicsContext> gc = osg.GraphicsContext.createGraphicsContext(traits.get())
    gw =  dynamic_cast<osgViewer.GraphicsWindow*>(gc.get())
    if !gw :
        osg.notify(osg.NOTICE), "Error: unable to create graphics window."
        return 1

    # create the view of the scene.
    viewer = osgViewer.Viewer()
    viewer.getCamera().setGraphicsContext(gc.get())
    viewer.getCamera().setViewport(0,0,800,600)
    viewer.setSceneData(loadedModel.get())
    
    # create a tracball manipulator to move the camera around in response to keyboard/mouse events
    viewer.setCameraManipulator( new osgGA.TrackballManipulator )

    osg.ref_ptr<osgGA.StateSetManipulator> statesetManipulator = new osgGA.StateSetManipulator(viewer.getCamera().getStateSet())
    viewer.addEventHandler(statesetManipulator.get())

    # add the pick handler
    viewer.addEventHandler(new PickHandler())

    viewer.realize()

    # main loop (note, window toolkits which take control over the main loop will require a window redraw callback containing the code below.)
    while !viewer.done() :
        viewer.frame()

    return 0



if __name__ == "__main__":
    main(sys.argv)
