#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osganimationeasemotion"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgAnimation
from osgpypp import osgGA
from osgpypp import osgViewer
from osgpypp import osgWidget


# Translated from file 'osganimationeasemotion.cpp'

#  -*-c++-*-
# *  Copyright (C) 2010 Jeremy Moles <cubicool@gmail.com>
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
# 

#include <osg/Geode>
#include <osg/MatrixTransform>
#include <osg/ShapeDrawable>
#include <osgGA/TrackballManipulator>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgAnimation/EaseMotion>
#include <osgWidget/WindowManager>
#include <osgWidget/Box>
#include <osgWidget/Table>
#include <osgWidget/Label>

EaseMotionSampler = class()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MASK_2D = 0xF0000000
MASK_3D = 0x0F000000
M_START = 0.0
M_DURATION = 2.0
M_CHANGE = 1.0

EASE_MOTION_SAMPLER = 0
EASE_MOTION_GEODE = 0

def createEaseMotionGeometry(motion):

    
    geom = osg.Geometry()
    cols = osg.Vec4Array()
    v = osg.Vec3Array()

    for(float i = 0.0 i < M_DURATION i += M_DURATION / 256.0) v.push_back(
        osg.Vec3(i * 30.0, motion.getValueAt(i) * 30.0, 0.0)
        )

    cols.push_back(osg.Vec4(1.0, 1.0, 1.0, 1.0))

    geom.setUseDisplayList(False)
    geom.setVertexArray(v)
    geom.setColorArray(cols, osg.Array.BIND_OVERALL)
    geom.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_STRIP, 0, v.size()))

    return geom

class EaseMotionSampler (osg.NodeCallback) :
    _previous = float()
    _pos = osg.Vec3()

    _motion = osgAnimation.Motion()

    EaseMotionSampler( osg.Vec3 pos):
        _previous (0.0),
        _pos      (pos) 

    void operator()(osg.Node* node, osg.NodeVisitor* nv) 
        if !_motion.valid() : return

        mt = dynamic_cast<osg.MatrixTransform*>(node)

        if !mt : return

        t = nv.getFrameStamp().getSimulationTime()

        # This avoids a little glitch when the animation doesn't start right away
        # when the application is launched.
        if _previous == 0.0 : _previous = t

        _motion.update(t - _previous)

        _previous = t

        mt.setMatrix(osg.Matrix.translate(_pos * _motion.getValue()))

    template<typename T>
    def setMotion():
        
        _motion = T(M_START, M_DURATION, M_CHANGE, osgAnimation.Motion.LOOP)

        EASE_MOTION_GEODE.removeDrawables(0, EASE_MOTION_GEODE.getNumDrawables())
        EASE_MOTION_GEODE.addDrawable(createEaseMotionGeometry(_motion.get()))


class ColorLabel (osgWidget.Label) :
ColorLabel( char* label):
        osgWidget.Label(label, "") 
        setFont("fonts/VeraMono.ttf")
        setFontSize(14)
        setFontColor(1.0, 1.0, 1.0, 1.0)

        setColor(0.3, 0.3, 0.3, 1.0)
        setPadding(2.0)
        setCanFill(True)

        addSize(150.0, 25.0)

        setLabel(label)
        setEventMask(osgWidget.EVENT_MOUSE_PUSH | osgWidget.EVENT_MASK_MOUSE_MOVE)

    bool mousePush(double, double,  osgWidget.WindowManager*) 
        p = dynamic_cast<osgWidget.Table*>(_parent)

        if !p : return False

        p.hide()

        name = getName()

        if !name.compare("OutQuadMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutQuadMotion>()
                

        elif !name.compare("InQuadMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InQuadMotion>()
                

        elif !name.compare("InOutQuadMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutQuadMotion>()
                

        elif !name.compare("OutCubicMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutCubicMotion>()
                

        elif !name.compare("InCubicMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InCubicMotion>()
                

        elif !name.compare("InOutCubicMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutCubicMotion>()
                

        elif !name.compare("OutQuartMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutQuartMotion>()
                

        elif !name.compare("InQuartMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InQuartMotion>()
                

        elif !name.compare("InOutQuartMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutQuartMotion>()
                

        elif !name.compare("OutBounceMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutBounceMotion>()
                

        elif !name.compare("InBounceMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InBounceMotion>()
                

        elif !name.compare("InOutBounceMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutBounceMotion>()
                

        elif !name.compare("OutElasticMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutElasticMotion>()
                

        elif !name.compare("InElasticMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InElasticMotion>()
                

        elif !name.compare("InOutElasticMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutElasticMotion>()
                

        elif !name.compare("OutSineMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutSineMotion>()
                

        elif !name.compare("InSineMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InSineMotion>()
                

        elif !name.compare("InOutSineMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutSineMotion>()
                

        elif !name.compare("OutBackMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutBackMotion>()
                

        elif !name.compare("InBackMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InBackMotion>()
                

        elif !name.compare("InOutBackMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutBackMotion>()
                

        elif !name.compare("OutCircMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutCircMotion>()
                

        elif !name.compare("InCircMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InCircMotion>()
                

        elif !name.compare("InOutCircMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutCircMotion>()
                

        elif !name.compare("OutExpoMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.OutExpoMotion>()
                

        elif !name.compare("InExpoMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InExpoMotion>()
                

        elif !name.compare("InOutExpoMotion") :
            EASE_MOTION_SAMPLER.setMotion<osgAnimation.InOutExpoMotion>()
                

        else : EASE_MOTION_SAMPLER.setMotion<osgAnimation.LinearMotion>()

        return True

    bool mouseEnter(double, double,  osgWidget.WindowManager*) 
        setColor(0.9, 0.6, 0.1, 1.0)

        return True

    bool mouseLeave(double, double,  osgWidget.WindowManager*) 
        setColor(0.3, 0.3, 0.3, 1.0)

        return True


class ColorLabelMenu (ColorLabel) :
_window = osgWidget.Table()
    ColorLabelMenu( char* label):
        ColorLabel(label) 
        _window = osgWidget.Table(str("Menu_") + label, 6, 5)

        _window.addWidget(ColorLabel("OutQuadMotion"), 0, 0)
        _window.addWidget(ColorLabel("InQuadMotion"), 1, 0)
        _window.addWidget(ColorLabel("InOutQuadMotion"), 2, 0)
        _window.addWidget(ColorLabel("OutCubicMotion"), 3, 0)
        _window.addWidget(ColorLabel("InCubicMotion"), 4, 0)
        _window.addWidget(ColorLabel("InOutCubicMotion"), 5, 0)

        _window.addWidget(ColorLabel("OutQuartMotion"), 0, 1)
        _window.addWidget(ColorLabel("InQuartMotion"), 1, 1)
        _window.addWidget(ColorLabel("InOutQuartMotion"), 2, 1)
        _window.addWidget(ColorLabel("OutBounceMotion"), 3, 1)
        _window.addWidget(ColorLabel("InBounceMotion"), 4, 1)
        _window.addWidget(ColorLabel("InOutBounceMotion"), 5, 1)

        _window.addWidget(ColorLabel("OutElasticMotion"), 0, 2)
        _window.addWidget(ColorLabel("InElasticMotion"), 1, 2)
        _window.addWidget(ColorLabel("InOutElasticMotion"), 2, 2)
        _window.addWidget(ColorLabel("OutSineMotion"), 3, 2)
        _window.addWidget(ColorLabel("InSineMotion"), 4, 2)
        _window.addWidget(ColorLabel("InOutSineMotion"), 5, 2)

        _window.addWidget(ColorLabel("OutBackMotion"), 0, 3)
        _window.addWidget(ColorLabel("InBackMotion"), 1, 3)
        _window.addWidget(ColorLabel("InOutBackMotion"), 2, 3)
        _window.addWidget(ColorLabel("OutCircMotion"), 3, 3)
        _window.addWidget(ColorLabel("InCircMotion"), 4, 3)
        _window.addWidget(ColorLabel("InOutCircMotion"), 5, 3)

        _window.addWidget(ColorLabel("OutExpoMotion"), 0, 4)
        _window.addWidget(ColorLabel("InExpoMotion"), 1, 4)
        _window.addWidget(ColorLabel("InOutExpoMotion"), 2, 4)
        _window.addWidget(ColorLabel("Linear"), 3, 4)

        _window.resize()

    def managed(wm):

        
        osgWidget.Label.managed(wm)

        wm.addChild(_window.get())

        _window.hide()

    def positioned():

        
        osgWidget.Label.positioned()

        _window.setOrigin(_parent.getX(), _parent.getY() +  _parent.getHeight())

    bool mousePush(double, double,  osgWidget.WindowManager*) 
        if !_window.isVisible() : _window.show()

        else : _window.hide()

        return True


def main(argc, argv):

    
    viewer = osgViewer.Viewer()

    wm = osgWidget.WindowManager(
        viewer,
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        MASK_2D
        )

    menu = osgWidget.Box("menu", osgWidget.Box.HORIZONTAL)

    menu.addWidget(ColorLabelMenu("Choose EaseMotion"))
    menu.getBackground().setColor(1.0, 1.0, 1.0, 1.0)
    menu.setPosition(15.0, 15.0, 0.0)

    wm.addChild(menu)

    group = osg.Group()
    geode = osg.Geode()
    mt = osg.MatrixTransform()

    geode.addDrawable(osg.ShapeDrawable(osg.Sphere(osg.Vec3(), 4.0)))

    EASE_MOTION_SAMPLER = EaseMotionSampler(osg.Vec3(50.0, 0.0, 0.0))
    EASE_MOTION_GEODE   = osg.Geode()

    mt.addChild(geode)
    mt.setUpdateCallback(EASE_MOTION_SAMPLER)
    mt.setNodeMask(MASK_3D)

    viewer.setCameraManipulator(osgGA.TrackballManipulator())
    viewer.getCameraManipulator().setHomePosition(
        osg.Vec3d(0.0, 0.0, 200.0),
        osg.Vec3d(20.0, 0.0, 0.0),
        osg.Vec3d(0.0, 1.0, 0.0)
        )
    viewer.home()

    group.addChild(mt)
    group.addChild(EASE_MOTION_GEODE)

    return osgWidget.createExample(viewer, wm, group)


if __name__ == "__main__":
    main(sys.argv)
