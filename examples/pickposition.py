#!/usr/bin/env python
#
# This source file is part of the osgBoostPython library
# 
# Copyright (C) 2009-2010 Jean-Sebastien Guay
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# http://www.gnu.org/copyleft/lesser.txt.
#

#import the needed modules
from osgpyplusplus import osg, osgDB, osgGA, osgViewer, osgUtil
# import osg
# import osgDB
# import osgGA
# import osgViewer
# import osgUtil
osg.Vec3 = osg.Vec3f
osg.Matrix = osg.Matrixd
import sys

class PickHandler(osgGA.GUIEventHandler):
    """
    Print pick position
    """
    def __init__(self):
        osgGA.GUIEventHandler.__init__(self)
        #Store mouse xy location for button press and move events.
        self._mX = 0
        self._mY = 0
        self._selectedNode = 0
        self.wb = 0

    def handle(self, ea, aa, obj, nv):
        print "handle called"
        try:
            return self._handle(ea,aa,obj,nv)
        except:
            pass
        return False
    def _handle(self, ea, aa, obj, nv):
        vwr = aa
#        vwr = osgViewer.GUIActionAdapterToViewer(aa)
        if not vwr:
            return False
        eventtype = ea.getEventType()
        if int(eventtype) == int(osgGA.GUIEventAdapter.PUSH):
            self._mX = ea.getX()
            self._mY = ea.getY()
            return False
        if int(eventtype) == int(osgGA.GUIEventAdapter.RELEASE):
            print self._mX, self._mY
            #check if mouse didn't move (else let trackball manipulator handle it)
            if self._mX == ea.getX() and self._mY == ea.getY():
                if self.pick( ea.getXnormalized(), ea.getYnormalized(), vwr ):
                    return True
        return False
    def pick(self, x, y, viewer):
        g1 = osgUtil.IntersectorGroup()
        l1 = osgUtil.LineSegmentIntersector(osgUtil.Intersector.PROJECTION, x, y)
        g1.addIntersector(l1)
        iv = osgUtil.IntersectionVisitor(g1)
        viewer.getCameraWithFocus().accept( iv )
        #check for intersections
        if l1.containsIntersections():
            try:
                intersection = l1.getFirstIntersection()
                print 'World coordinates of intersection:'
                print intersection.getWorldIntersectPoint()
                print 'Local coordinates of intersection:'
                print intersection.getLocalIntersectPoint()
            except Exception, inst:
                print inst
            #find the first Transform node and make it the selected node
            return False
        return False

modelFile = 'cow.osg'
try:
    modelFile = sys.argv[1]
except:
    print 'You did not specify a model file. Using cow.osg as default.'

#load the model
loadedModel = osgDB.readNodeFile( modelFile )
if loadedModel == None:
    raise Exception('Loading model file failed')

root = osg.Group()
dynamicTransform1 = osg.MatrixTransform()
dynamicTransform1.addChild(loadedModel)
root.addChild(dynamicTransform1)

#create the viewer, set the scene and run
viewer = osgViewer.Viewer()

#set the scene data
viewer.setSceneData(root)

#add the stats event handler
viewer.addEventHandler(osgViewer.HelpHandler());
viewer.addEventHandler(osgViewer.StatsHandler());
viewer.addEventHandler(osgGA.StateSetManipulator(root.stateSet));
pickhandler = PickHandler()
print "adding pickhandler"
viewer.addEventHandler(pickhandler);
#run the viewer
viewer.run()
