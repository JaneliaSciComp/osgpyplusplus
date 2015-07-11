#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganimationmakepath"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osganimationmakepath.cpp'

#  -*-c++-*- 
# *  Copyright (C) 2008 Cedric Pinson <mornifle@plopbyte.net>
# *
# * This library is open source and may be redistributed and/or modified under  
# * the terms of the OpenSceneGraph Public License (OSGPL) version 0.0 or 
# * (at your option) any later version.  The full license is in LICENSE file
# * included with this distribution, and on the openscenegraph.org website.
# * 
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# * OpenSceneGraph Public License for more details.
# *
# *  Authors:
# *   Jeremy Moles  <jeremy@emperorlinux.com>
# *   Cedric Pinson <mornifle@plopbyte.net>
#

#include <iostream>
#include <osg/io_utils>
#include <osg/Geometry>
#include <osg/Shape>
#include <osg/ShapeDrawable>
#include <osg/Material>
#include <osg/MatrixTransform>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/TrackballManipulator>
#include <osgAnimation/Sampler>

  class AnimtkUpdateCallback (osg.NodeCallback) :
      META_Object(osgAnimation, AnimtkUpdateCallback)

      AnimtkUpdateCallback() 
          _sampler = osgAnimation.Vec3CubicBezierSampler()
          _playing = False
          _lastUpdate = 0
      AnimtkUpdateCallback( AnimtkUpdateCallback val,  osg.CopyOp copyop = osg.CopyOp.SHALLOW_COPY):
          osg.Object(val, copyop),
          osg.NodeCallback(val, copyop),
          _sampler(val._sampler),
          _startTime(val._startTime),
          _currentTime(val._currentTime),
          _playing(val._playing),
          _lastUpdate(val._lastUpdate)

      #* Callback method called by the NodeVisitor when visiting a node.
      virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)
          if nv.getVisitorType() == osg.NodeVisitor.UPDATE_VISITOR  
              nv.getFrameStamp()  
              nv.getFrameStamp().getFrameNumber() != _lastUpdate : 

              _lastUpdate = nv.getFrameStamp().getFrameNumber()
              _currentTime = osg.Timer.instance().tick()

              if _playing  _sampler.get()  _sampler.getKeyframeContainer() : 
                  transform = dynamic_cast<osg.MatrixTransform*>(node)
                  if transform : 
                      result = osg.Vec3()
                      t = osg.Timer.instance().delta_s(_startTime, _currentTime)
                      duration = _sampler.getEndTime() - _sampler.getStartTime()
                      t = fmod(t, duration)
                      t += _sampler.getStartTime()
                      _sampler.getValueAt(t, result)
                      transform.setMatrix(osg.Matrix.translate(result))
          # note, callback is responsible for scenegraph traversal so
          # they must call traverse(node,nv) to ensure that the
          # scene graph subtree (and associated callbacks) are traversed.
          traverse(node,nv)

      def start():

           _startTime = osg.Timer.instance().tick() _currentTime = _startTime _playing = True
      def stop():
           _currentTime = _startTime _playing = False

      _sampler = osgAnimation.Vec3CubicBezierSampler()
      _startTime = osg.Timer_t()
      _currentTime = osg.Timer_t()
      _playing = bool()
      _lastUpdate = unsigned int()
  


class AnimtkStateSetUpdateCallback (osg.StateSet.Callback) :
    META_Object(osgAnimation, AnimtkStateSetUpdateCallback)

    AnimtkStateSetUpdateCallback() 
        _sampler = osgAnimation.Vec4LinearSampler()
        _playing = False
        _lastUpdate = 0

    AnimtkStateSetUpdateCallback( AnimtkStateSetUpdateCallback val,  osg.CopyOp copyop = osg.CopyOp.SHALLOW_COPY):
        osg.Object(val, copyop),
        osg.StateSet.Callback(val, copyop),
        _sampler(val._sampler),
        _startTime(val._startTime),
        _currentTime(val._currentTime),
        _playing(val._playing),
        _lastUpdate(val._lastUpdate)

    #* Callback method called by the NodeVisitor when visiting a node.
    virtual void operator()(osg.StateSet* state, osg.NodeVisitor* nv)
        if state  
            nv.getVisitorType() == osg.NodeVisitor.UPDATE_VISITOR  
            nv.getFrameStamp()  
            nv.getFrameStamp().getFrameNumber() != _lastUpdate : 

            _lastUpdate = nv.getFrameStamp().getFrameNumber()
            _currentTime = osg.Timer.instance().tick()

            if _playing  _sampler.get()  _sampler.getKeyframeContainer() : 
                material = dynamic_cast<osg.Material*>(state.getAttribute(osg.StateAttribute.MATERIAL))
                if material : 
                    result = osg.Vec4()
                    t = osg.Timer.instance().delta_s(_startTime, _currentTime)
                    duration = _sampler.getEndTime() - _sampler.getStartTime()
                    t = fmod(t, duration)
                    t += _sampler.getStartTime()
                    _sampler.getValueAt(t, result)
                    material.setDiffuse(osg.Material.FRONT_AND_BACK, result)

    def start():

         _startTime = osg.Timer.instance().tick() _currentTime = _startTime _playing = True
    def stop():
         _currentTime = _startTime _playing = False

    _sampler = osgAnimation.Vec4LinearSampler()
    _startTime = osg.Timer_t()
    _currentTime = osg.Timer_t()
    _playing = bool()
    _lastUpdate = unsigned int()


# This won't really give good results in any situation, but it does demonstrate
# on possible "fast" usage...
class MakePathTimeCallback (AnimtkUpdateCallback) :
_geode = osg.Geode()
    _lastAdd = float()
    _addSeconds = float()
    MakePathTimeCallback(osg.Geode* geode):
        _geode(geode),
        _lastAdd(0.0),
        _addSeconds(0.08) 

    virtual void operator()(osg.Node* node, osg.NodeVisitor* nv) 
        t = osg.Timer.instance().delta_s(_startTime, _currentTime)

        if _lastAdd + _addSeconds <= t  t <= 8.0 : 
            pos = osg.Vec3()

            _sampler.getValueAt(t, pos)

            _geode.addDrawable(osg.ShapeDrawable(osg.Sphere(pos, 0.5)))
            _geode.dirtyBound()

            _lastAdd += _addSeconds

        AnimtkUpdateCallback.operator()(node, nv)


# This will give great results if you DO NOT have VSYNC enabled and can generate
# decent FPS.
class MakePathDistanceCallback (AnimtkUpdateCallback) :
_geode = osg.Geode()
    _lastAdd = osg.Vec3()
    _threshold = float()
    _count = unsigned int()
    MakePathDistanceCallback(osg.Geode* geode):
        _geode(geode),
        _threshold(0.5),
        _count(0) 

    virtual void operator()(osg.Node* node, osg.NodeVisitor* nv) 
        static bool countReported = False

        t = osg.Timer.instance().delta_s(_startTime, _currentTime)

        pos = osg.Vec3()

        _sampler.getValueAt(t, pos)

        distance = _lastAdd - pos

        if t <= 8.0  distance.length() >= _threshold : 
            _geode.addDrawable(osg.ShapeDrawable(osg.Sphere(pos, 0.25)))
            _lastAdd = pos
            _count++
        elif t > 8.0 : 
            if !countReported : print "Created ", _count, " nodes."
            countReported = True

        AnimtkUpdateCallback.operator()(node, nv)


def setupStateSet():

    
    st = osg.StateSet()
    
    st.setAttributeAndModes(osg.Material(), True)
    st.setMode(GL_BLEND, True)
    
    callback = AnimtkStateSetUpdateCallback()
    keys = callback._sampler.getOrCreateKeyframeContainer()
    keys.push_back(osgAnimation.Vec4Keyframe(0, osg.Vec4(1,0,0,1)))
    keys.push_back(osgAnimation.Vec4Keyframe(2, osg.Vec4(0.,1,0,1)))
    keys.push_back(osgAnimation.Vec4Keyframe(4, osg.Vec4(0,0,1,1)))
    keys.push_back(osgAnimation.Vec4Keyframe(6, osg.Vec4(0,0,1,1)))
    keys.push_back(osgAnimation.Vec4Keyframe(8, osg.Vec4(0,1,0,1)))
    keys.push_back(osgAnimation.Vec4Keyframe(10, osg.Vec4(1,0,0,1)))
    callback.start()
    st.setUpdateCallback(callback)
    
    return st

def setupAnimtkNode(staticGeode):

    
    osg.Vec3 v[5]

    v[0] = osg.Vec3(  0,   0,   0)
    v[1] = osg.Vec3(20, 40, 60)
    v[2] = osg.Vec3(40, 60, 20)
    v[3] = osg.Vec3(60, 20, 40)
    v[4] = osg.Vec3( 0,  0,  0)

    node = osg.MatrixTransform()
    callback = MakePathDistanceCallback(staticGeode)
    keys = callback._sampler.getOrCreateKeyframeContainer()

    keys.push_back(osgAnimation.Vec3CubicBezierKeyframe(0, osgAnimation.Vec3CubicBezier(
                                                        v[0],
                                                        v[0] + (v[0] - v[3]),
                                                        v[1] - (v[1] - v[0])
                                                        )))

    keys.push_back(osgAnimation.Vec3CubicBezierKeyframe(2, osgAnimation.Vec3CubicBezier(
                                                        v[1],
                                                        v[1] + (v[1] - v[0]),
                                                        v[2] - (v[2] - v[1])
                                                        )))

    keys.push_back(osgAnimation.Vec3CubicBezierKeyframe(4, osgAnimation.Vec3CubicBezier(
                                                        v[2],
                                                        v[2] + (v[2] - v[1]),
                                                        v[3] - (v[3] - v[2])
                                                        )))

    keys.push_back(osgAnimation.Vec3CubicBezierKeyframe(6, osgAnimation.Vec3CubicBezier(
                                                        v[3],
                                                        v[3] + (v[3] - v[2]),
                                                        v[4] - (v[4] - v[3])
                                                        )))

    keys.push_back(osgAnimation.Vec3CubicBezierKeyframe(8, osgAnimation.Vec3CubicBezier(
                                                        v[4],
                                                        v[4] + (v[4] - v[3]),
                                                        v[0] - (v[0] - v[4])
                                                        )))

    callback.start()
    node.setUpdateCallback(callback)

    geode = osg.Geode()
    
    geode.setStateSet(setupStateSet())
    geode.addDrawable(osg.ShapeDrawable(osg.Sphere(osg.Vec3(0.0, 0.0, 0.0), 2)))
    
    node.addChild(geode)

    return node

def main(argc, argv):

    
    arguments = osg.ArgumentParser(argc, argv)
    viewer = osgViewer.Viewer(arguments)
    
    tbm = osgGA.TrackballManipulator()

    viewer.setCameraManipulator(tbm)

    viewer.addEventHandler(osgViewer.StatsHandler())
    viewer.addEventHandler(osgViewer.WindowSizeHandler())

    root = osg.Group()
    geode = osg.Geode()

    geode.setStateSet(setupStateSet())

    root.setInitialBound(osg.BoundingSphere(osg.Vec3(10,0,20), 50))
    root.addChild(setupAnimtkNode(geode))
    root.addChild(geode)

    viewer.setSceneData(root)

    # tbm.setDistance(150)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
