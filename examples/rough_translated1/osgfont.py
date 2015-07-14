#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgfont"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osgfont.cpp'

#include <cstdlib>
#include <sstream>
#include <osg/io_utils>
#include <osg/ArgumentParser>
#include <osg/Geode>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>
#include <osgGA/StateSetManipulator>

def textInfo(text):

    
    tgqm = text.getTextureGlyphQuadMap()

    tgqmi = tgqm.begin()

    gq = tgqmi.second

    s = text.getText()

    for(unsigned int i = 0 i < s.size() i++)
        ul = gq.getCoords()[0 + (i * 4)] # upperLeft
        ll = gq.getCoords()[1 + (i * 4)] # lowerLeft
        lr = gq.getCoords()[2 + (i * 4)] # lowerRight
        ur = gq.getCoords()[3 + (i * 4)] # upperRight

        #
#        ul = gq.getTransformedCoords(0)[0 + (i * 4)]
#        ll = gq.getTransformedCoords(0)[1 + (i * 4)]
#        lr = gq.getTransformedCoords(0)[2 + (i * 4)]
#        ur = gq.getTransformedCoords(0)[3 + (i * 4)]
#        

        osg.notify(osg.NOTICE), "'", static_cast<char>(s[i]), "':", " width(", lr.x() - ll.x(), ")", " height(", ul.y() - ll.y(), ")", "\t", "ul(", ul, "), ", "ll(", ll, "), ", "lr(", lr, "), ", "ur(", ur, ")"
        

def createOrthoCamera(width, height):

    
    camera = osg.Camera()

    camera.getOrCreateStateSet().setMode(
        GL_LIGHTING,
        osg.StateAttribute.PROTECTED | osg.StateAttribute.OFF
    )

    m = osg.Matrix.ortho2D(0.0, width, 0.0, height)

    camera.setProjectionMatrix(m)
    camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    camera.setViewMatrix(osg.Matrix.identity())
    camera.setClearMask(GL_DEPTH_BUFFER_BIT)
    camera.setRenderOrder(osg.Camera.POST_RENDER)

    return camera

def createLabel(l, f, size):

    
    static osg.Vec3 pos(10.0, 10.0, 0.0)

    label = osgText.Text()
    font = osgText.readFontFile(f)

    label.setFont(font)
    label.setCharacterSize(size)
    label.setFontResolution(size, size)
    label.setColor(osg.Vec4(1.0, 1.0, 1.0, 1.0))
    label.setPosition(pos)
    label.setAlignment(osgText.Text.LEFT_BOTTOM)

    # It seems to be important we do this last to get best results?
    label.setText(l)

    textInfo(label)

    pos.y() += size + 10.0

    return label

typedef std.list<unsigned int> Sizes

def main(argv):

    
    viewer = osgViewer.Viewer()
    args = osg.ArgumentParser(argv)

    # Make sure we have the minimum args...
    if argc <= 2 :
        osg.notify(osg.FATAL), "usage: ", args[0], " fontfile size1 [size2 ...]"

        return 1


    viewer.addEventHandler( osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    viewer.addEventHandler(osgViewer.StatsHandler())
    viewer.addEventHandler(osgViewer.WindowSizeHandler())

    group = osg.Group()
    camera = createOrthoCamera(1280.0, 1024.0)

    # Create the list of desired sizes.
    sizes = Sizes()

    for(int i = 2 i < argc i++)
        if  not args.isNumber(i) : continue

        sizes.push_back(std.atoi(args[i]))

    geode = osg.Geode()

    # Add all of our osgText drawables.
    for(Sizes.const_iterator i = sizes.begin() i  not = sizes.end() i++)
        ss = strstream()

        ss, *i, " 1234567890 abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        geode.addDrawable(createLabel(ss.str(), args[1], *i))

    camera.addChild(geode)

    group.addChild(camera)

    viewer.setSceneData(group)

    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
