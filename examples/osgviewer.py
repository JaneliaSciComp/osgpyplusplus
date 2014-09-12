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
from osgpypp import osg, osgDB, osgGA, osgViewer, osgUtil

osg.Vec3 = osg.Vec3f
osg.Matrix = osg.Matrixd
import sys

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
viewer.setSceneData(root)
viewer.addEventHandler(osgViewer.HelpHandler());
viewer.addEventHandler(osgViewer.StatsHandler());
viewer.addEventHandler(osgGA.StateSetManipulator(root.stateSet));
viewer.run()
