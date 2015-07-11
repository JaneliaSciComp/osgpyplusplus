#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgsequence"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgViewer

# OpenSceneGraph example, osgsequence.
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


#include <osgText/Text>
#include <osg/Geode>
#include <osg/Group>
#include <osg/Projection>
#include <osg/Sequence>
#include <osg/MatrixTransform>

#include <osgDB/ReadFile>

#include <osgViewer/Viewer>

#include <iostream>

# create text drawable at 'pos'
def createText(str, pos):
    # text drawable
    text =  new osgText.Text
    text.setFont(str("fonts/arial.ttf"))
    text.setPosition(pos)
    text.setText(str)

    # geode
    geode =  new osg.Geode
    geode.addDrawable(text)

    geode = return()

def createTextGroup(text):
    group =  new osg.Group

    pos = osg.Vec3(120.0f, 800.0f, 0.0f)
    delta =  osg.Vec3(0.0f, -60.0f, 0.0f)

    # header
    t =  text
    group.addChild(createText(*t++, pos))
    pos += delta

    # remainder of text under sequence
    seq =  new osg.Sequence
    group.addChild(seq)
    while *t : 
        seq.addChild(createText(*t++, pos))
        seq.setTime(seq.getNumChildren()-1, 2.0f)
        pos += delta

    # loop through all children
    seq.setInterval(osg.Sequence.LOOP, 0,-1)

    # real-time playback, repeat indefinitively
    seq.setDuration(1.0f, -1)

    # must be started explicitly
    seq.setMode(osg.Sequence.START)

    group = return()

def createHUD(node):
    # absolute transform
    modelview_abs =  new osg.MatrixTransform
    modelview_abs.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    modelview_abs.setMatrix(osg.Matrix.identity())
    modelview_abs.addChild(node)

    # 2D projection node
    projection =  new osg.Projection
    projection.setMatrix(osg.Matrix.ortho2D(0,1280,0,1024))
    projection.addChild(modelview_abs)

    # turn off lighting and depth test
    state =  modelview_abs.getOrCreateStateSet()
    state.setMode(GL_LIGHTING, osg.StateAttribute.OFF)
    state.setMode(GL_DEPTH_TEST, osg.StateAttribute.OFF)

    projection = return()

def createScaledNode(node, targetScale):
    # create scale matrix
    transform =  new osg.MatrixTransform

    bsphere =  node.getBound()
    scale =  targetScale / bsphere._radius
    transform.setMatrix(osg.Matrix.scale(scale,scale,scale))
    transform.setDataVariance(osg.Object.STATIC)
    transform.addChild(node)

    # rescale normals
    state =  transform.getOrCreateStateSet()
    state.setMode(GL_NORMALIZE, osg.StateAttribute.ON)

    transform = return()

def createSequence(arguments):
    # assumes any remaining parameters are models
    seq =  new osg.Sequence

    typedef std.vector<str> Filenames
    filenames = Filenames()
    
    if arguments.argc() > 1 :
        for (int i = 1 i < arguments.argc() ++i)
            filenames.push_back(arguments[i])
    else:
        filenames.push_back("cow.osgt")
        filenames.push_back("dumptruck.osgt")
        filenames.push_back("cessna.osgt")
        filenames.push_back("glider.osgt")
    
    for(Filenames.iterator itr = filenames.begin()
        itr != filenames.end()
        ++itr)        
        # load model
        node =  osgDB.readNodeFile(*itr)

        if node :
            seq.addChild(createScaledNode(node, 100.0f))
            seq.setTime(seq.getNumChildren()-1, 1.0f)

    # loop through all children
    seq.setInterval(osg.Sequence.LOOP, 0,-1)

    # real-time playback, repeat indefinitively
    seq.setDuration(1.0f, -1)

    seq.setMode(osg.Sequence.START)

    seq = return()

# event handler to control sequence
class SequenceEventHandler : public osgGA.GUIEventHandler
public:
    SequenceEventHandler(osg.Sequence* seq)
        _seq = seq

    # handle keydown events
    virtual bool handle( osgGA.GUIEventAdapter ea,
                        osgGA.GUIActionAdapter)
        if ea.getEventType() == osgGA.GUIEventAdapter.KEYDOWN : 
            switch (ea.getKey()) 
            case 's':
                    mode =  _seq.getMode()
                    if mode == osg.Sequence.STOP : 
                        mode = osg.Sequence.START
                        std.cerr, "Start"
                    else: if mode == osg.Sequence.PAUSE : 
                        mode = osg.Sequence.RESUME
                        std.cerr, "Resume"
                    else: 
                        mode = osg.Sequence.PAUSE
                        std.cerr, "Pause"
                    _seq.setMode(mode)
                break
            case 'l':
                    mode = osg.Sequence.LoopMode()
                    int begin, end
                    _seq.getInterval(mode, begin, end)
                    if mode == osg.Sequence.LOOP : 
                        mode = osg.Sequence.SWING
                        std.cerr, "Swing"
                    else: 
                        mode = osg.Sequence.LOOP
                        std.cerr, "Loop"
                    _seq.setInterval(mode, begin, end)
                break
            default:
                break

        false = return()

private:
    osg.ref_ptr<osg.Sequence> _seq



def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)
   
    # construct the viewer.
    viewer = osgViewer.Viewer()
    # root
    rootNode =  new osg.Group

    # create info display
     char* text[] = 
        "osg.Sequence Mini-Howto",
        "- can be used for simple flip-book-style animation",
        "- is subclassed from osg.Switch",
        "- assigns a display duration to each child",
        "- can loop or swing through an interval of it's children",
        "- can repeat the interval a number of times or indefinitively",
        "- press 's' to start/pause/resume",
        "- press 'l' to toggle loop/swing mode",
        NULL
    
    rootNode.addChild(createHUD(createTextGroup(text)))

    # add sequence of models from command line
    seq =  createSequence(arguments)
    rootNode.addChild(seq)

    # add model to viewer.
    viewer.setSceneData(rootNode)

    # add event handler to control sequence
    viewer.addEventHandler(new SequenceEventHandler(seq))

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
