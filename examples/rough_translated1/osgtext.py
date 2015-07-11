#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgtext"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgtext.
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


#include <osgUtil/Optimizer>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgDB/Registry>

#include <osgGA/StateSetManipulator>
#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osg/Geode>
#include <osg/Camera>
#include <osg/ShapeDrawable>
#include <osg/Sequence>
#include <osg/PolygonMode>
#include <osg/io_utils>

#include <osgText/Font>
#include <osgText/Text>


def createHUDText():
    rootNode =  new osg.Group

    font =  osgText.readFontFile("fonts/arial.ttf")

    geode =  new osg.Geode
    rootNode.addChild(geode)

    windowHeight =  1024.0f
    windowWidth =  1280.0f
    margin =  50.0f


####################################################
#    
# Examples of how to set up different text layout
#

    layoutColor = osg.Vec4(1.0f,1.0f,0.0f,1.0f)
    layoutCharacterSize =  20.0f    
    
        text =  new osgText.Text
        text.setFont(font)
        text.setColor(layoutColor)
        text.setCharacterSize(layoutCharacterSize)
        text.setPosition(osg.Vec3(margin,windowHeight-margin,0.0f))

        # the default layout is left to right, typically used in languages
        # originating from europe such as English, French, German, Spanish etc..
        text.setLayout(osgText.Text.LEFT_TO_RIGHT)

        text.setText("text.setLayout(osgText.Text.LEFT_TO_RIGHT)")
        geode.addDrawable(text)

        text =  new osgText.Text
        text.setFont(font)
        text.setColor(layoutColor)
        text.setCharacterSize(layoutCharacterSize)
        text.setPosition(osg.Vec3(windowWidth-margin,windowHeight-margin,0.0f))

        # right to left layouts would be used for hebrew or arabic fonts.
        text.setLayout(osgText.Text.RIGHT_TO_LEFT)
        text.setAlignment(osgText.Text.RIGHT_BASE_LINE)

        text.setText("text.setLayout(osgText.Text.RIGHT_TO_LEFT)")
        geode.addDrawable(text)

        text =  new osgText.Text
        text.setFont(font)
        text.setColor(layoutColor)
        text.setPosition(osg.Vec3(margin,windowHeight-margin,0.0f))
        text.setCharacterSize(layoutCharacterSize)

        # vertical font layout would be used for asian fonts.
        text.setLayout(osgText.Text.VERTICAL)

        text.setText("text.setLayout(osgText.Text.VERTICAL)")
        geode.addDrawable(text)
    
    
####################################################
#    
# Examples of how to set up different font resolution
#

    fontSizeColor = osg.Vec4(0.0f,1.0f,1.0f,1.0f)
    fontSizeCharacterSize =  30
    
    cursor =  osg.Vec3(margin*2,windowHeight-margin*2,0.0f)
    
        text =  new osgText.Text
        text.setFont(font)
        text.setColor(fontSizeColor)
        text.setCharacterSize(fontSizeCharacterSize)
        text.setPosition(cursor)
        
        # use text that uses 10 by 10 texels as a target resolution for fonts.
        text.setFontResolution(10,10) # blocky but small texture memory usage
        
        text.setText("text.setFontResolution(10,10) # blocky but small texture memory usage")
        geode.addDrawable(text)
    
    cursor.y() -= fontSizeCharacterSize
        text =  new osgText.Text
        text.setFont(font)
        text.setColor(fontSizeColor)
        text.setCharacterSize(fontSizeCharacterSize)
        text.setPosition(cursor)
        
        # use text that uses 20 by 20 texels as a target resolution for fonts.
        text.setFontResolution(20,20) # smoother but higher texture memory usage (but still quite low).
        
        text.setText("text.setFontResolution(20,20) # smoother but higher texture memory usage (but still quite low).")
        geode.addDrawable(text)
    
    cursor.y() -= fontSizeCharacterSize
        text =  new osgText.Text
        text.setFont(font)
        text.setColor(fontSizeColor)
        text.setCharacterSize(fontSizeCharacterSize)
        text.setPosition(cursor)
        
        # use text that uses 40 by 40 texels as a target resolution for fonts.
        text.setFontResolution(40,40) # even smoother but again higher texture memory usage.
        
        text.setText("text.setFontResolution(40,40) # even smoother but again higher texture memory usage.")
        geode.addDrawable(text)


####################################################
#    
# Examples of how to set up different sized text
#

    characterSizeColor = osg.Vec4(1.0f,0.0f,1.0f,1.0f)
    
    cursor.y() -= fontSizeCharacterSize*2.0f
    
        text =  new osgText.Text
        text.setFont(font)
        text.setColor(characterSizeColor)
        text.setFontResolution(20,20)
        text.setPosition(cursor)
        
        # use text that is 20 units high.
        text.setCharacterSize(20) # small
        
        text.setText("text.setCharacterSize(20.0f) # small")
        geode.addDrawable(text)
    
    cursor.y() -= 30.0f
        text =  new osgText.Text
        text.setFont(font)
        text.setColor(characterSizeColor)
        text.setFontResolution(30,30)
        text.setPosition(cursor)
        
        # use text that is 30 units high.
        text.setCharacterSize(30.0f) # medium
        
        text.setText("text.setCharacterSize(30.0f) # medium")
        geode.addDrawable(text)
    
    cursor.y() -= 50.0f
        text =  new osgText.Text
        text.setFont(font)
        text.setColor(characterSizeColor)
        text.setFontResolution(40,40)
        text.setPosition(cursor)
        
        # use text that is 60 units high.
        text.setCharacterSize(60.0f) # large
        
        text.setText("text.setCharacterSize(60.0f) # large")
        geode.addDrawable(text)


####################################################
#    
# Examples of how to set up different alignments
#

    alignmentSizeColor = osg.Vec4(0.0f,1.0f,0.0f,1.0f)
    alignmentCharacterSize =  25.0f
    cursor.x() = 640
    cursor.y() = margin*4.0f
    
    typedef std.pair<osgText.Text.AlignmentType,str> AlignmentPair
    typedef std.vector<AlignmentPair> AlignmentList
    alignmentList = AlignmentList()
    alignmentList.push_back(AlignmentPair(osgText.Text.LEFT_TOP,"text.setAlignment(\nosgText.Text.LEFT_TOP)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.LEFT_CENTER,"text.setAlignment(\nosgText.Text.LEFT_CENTER)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.LEFT_BOTTOM,"text.setAlignment(\nosgText.Text.LEFT_BOTTOM)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.CENTER_TOP,"text.setAlignment(\nosgText.Text.CENTER_TOP)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.CENTER_CENTER,"text.setAlignment(\nosgText.Text.CENTER_CENTER)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.CENTER_BOTTOM,"text.setAlignment(\nosgText.Text.CENTER_BOTTOM)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.RIGHT_TOP,"text.setAlignment(\nosgText.Text.RIGHT_TOP)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.RIGHT_CENTER,"text.setAlignment(\nosgText.Text.RIGHT_CENTER)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.RIGHT_BOTTOM,"text.setAlignment(\nosgText.Text.RIGHT_BOTTOM)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.LEFT_BASE_LINE,"text.setAlignment(\nosgText.Text.LEFT_BASE_LINE)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.CENTER_BASE_LINE,"text.setAlignment(\nosgText.Text.CENTER_BASE_LINE)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.RIGHT_BASE_LINE,"text.setAlignment(\nosgText.Text.RIGHT_BASE_LINE)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.LEFT_BOTTOM_BASE_LINE,"text.setAlignment(\nosgText.Text.LEFT_BOTTOM_BASE_LINE)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.CENTER_BOTTOM_BASE_LINE,"text.setAlignment(\nosgText.Text.CENTER_BOTTOM_BASE_LINE)"))
    alignmentList.push_back(AlignmentPair(osgText.Text.RIGHT_BOTTOM_BASE_LINE,"text.setAlignment(\nosgText.Text.RIGHT_BOTTOM_BASE_LINE)"))


    sequence =  new osg.Sequence
        for(AlignmentList.iterator itr=alignmentList.begin()
            itr!=alignmentList.end()
            ++itr)
            alignmentGeode =  new osg.Geode
            sequence.addChild(alignmentGeode)
            sequence.setTime(sequence.getNumChildren(), 1.0f)

            text =  new osgText.Text
            text.setFont(font)
            text.setColor(alignmentSizeColor)
            text.setCharacterSize(alignmentCharacterSize)
            text.setPosition(cursor)
            text.setDrawMode(osgText.Text.TEXT|osgText.Text.ALIGNMENT|osgText.Text.BOUNDINGBOX)
            
            text.setAlignment(itr.first)
            text.setText(itr.second)
            
            alignmentGeode.addDrawable(text)


        

    sequence.setMode(osg.Sequence.START)
    sequence.setInterval(osg.Sequence.LOOP, 0, -1)
    sequence.setDuration(1.0f, -1)
    
    rootNode.addChild(sequence)


####################################################
#    
# Examples of how to set up different fonts...
#

    cursor.x() = margin*2.0f
    cursor.y() = margin*2.0f
    
    fontColor = osg.Vec4(1.0f,0.5f,0.0f,1.0f)
    fontCharacterSize =  20.0f
    spacing =  40.0f
    
        text =  new osgText.Text
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(0)
        text.setText("text.setFont(0) # inbuilt font.")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
    
        arial =  osgText.readFontFile("fonts/arial.ttf")

        text =  new osgText.Text
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(arial)
        text.setText(arial!=0?
                      "text.setFont(\"fonts/arial.ttf\")":
                      "unable to load \"fonts/arial.ttf\"")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
    
        times =  osgText.readFontFile("fonts/times.ttf")

        text =  new osgText.Text
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        geode.addDrawable(text)
        text.setFont(times)
        text.setText(times!=0?
                      "text.setFont(\"fonts/times.ttf\")":
                      "unable to load \"fonts/times.ttf\"")

        cursor.x() = text.getBound().xMax() + spacing 
    
    cursor.x() = margin*2.0f
    cursor.y() = margin

        dirtydoz =  osgText.readFontFile("fonts/dirtydoz.ttf")

        text =  new osgText.Text
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(dirtydoz)
        text.setText(dirtydoz!=0?
                      "text.setFont(\"fonts/dirtydoz.ttf\")":
                      "unable to load \"fonts/dirtydoz.ttf\"")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
    
        fudd =  osgText.readFontFile("fonts/fudd.ttf")
    
        text =  new osgText.Text
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(fudd)
        text.setText(fudd!=0?
                      "text.setFont(\"fonts/fudd.ttf\")":
                      "unable to load \"fonts/fudd.ttf\"")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
            
    rootNode = return()    




# create text which sits in 3D space such as would be inserted into a normal model
def create3DText(center, radius):
    geode =  new osg.Geode

    
####################################################
#    
# Examples of how to set up axis/orientation alignments
#

    characterSize = radius*0.2f


    pos = osg.Vec3(center.x()-radius*.5f,center.y()-radius*.5f,center.z()-radius*.5f)

    text1 =  new osgText.Text
    text1.setFont("fonts/times.ttf")
    text1.setCharacterSize(characterSize)
    text1.setPosition(pos)
    text1.setAxisAlignment(osgText.Text.XY_PLANE)
    text1.setText("XY_PLANE")
    geode.addDrawable(text1)

    text2 =  new osgText.Text
    text2.setFont("fonts/times.ttf")
    text2.setCharacterSize(characterSize)
    text2.setPosition(pos)
    text2.setAxisAlignment(osgText.Text.YZ_PLANE)
    text2.setText("YZ_PLANE")
    geode.addDrawable(text2)

    text3 =  new osgText.Text
    text3.setFont("fonts/times.ttf")
    text3.setCharacterSize(characterSize)
    text3.setPosition(pos)
    text3.setAxisAlignment(osgText.Text.XZ_PLANE)
    text3.setText("XZ_PLANE")
    geode.addDrawable(text3)

    characterSizeModeColor = osg.Vec4(1.0f,0.0f,0.5f,1.0f)

    text4 =  new osgText.Text
    text4.setFont("fonts/times.ttf")
    text4.setCharacterSize(characterSize)
    text4.setPosition(center)
    text4.setAxisAlignment(osgText.Text.SCREEN)

    # reproduce outline bounding box compute problem with backdrop on.
    text4.setBackdropType(osgText.Text.OUTLINE)
    text4.setDrawMode(osgText.Text.TEXT | osgText.Text.BOUNDINGBOX)

    text4.setText("SCREEN")
    geode.addDrawable(text4)

    text5 =  new osgText.Text
    text5.setColor(characterSizeModeColor)
    text5.setFont("fonts/times.ttf")
    #text5.setCharacterSize(characterSize)
    text5.setCharacterSize(32.0f) # medium
    text5.setPosition(center - osg.Vec3(0.0, 0.0, 0.2))
    text5.setAxisAlignment(osgText.Text.SCREEN)
    text5.setCharacterSizeMode(osgText.Text.SCREEN_COORDS)
    text5.setDrawMode(osgText.Text.TEXT | osgText.Text.BOUNDINGBOX)
    text5.setText("CharacterSizeMode SCREEN_COORDS(size 32.0)")
    geode.addDrawable(text5)

    text6 =  new osgText.Text
    text6.setColor(characterSizeModeColor)
    text6.setFont("fonts/times.ttf")
    text6.setCharacterSize(characterSize)
    text6.setPosition(center - osg.Vec3(0.0, 0.0, 0.4))
    text6.setAxisAlignment(osgText.Text.SCREEN)
    text6.setCharacterSizeMode(osgText.Text.OBJECT_COORDS_WITH_MAXIMUM_SCREEN_SIZE_CAPPED_BY_FONT_HEIGHT)
    text6.setText("CharacterSizeMode OBJECT_COORDS_WITH_MAXIMUM_SCREEN_SIZE_CAPPED_BY_FONT_HEIGHT")
    geode.addDrawable(text6)

    text7 =  new osgText.Text
    text7.setColor(characterSizeModeColor)
    text7.setFont("fonts/times.ttf")
    text7.setCharacterSize(characterSize)
    text7.setPosition(center - osg.Vec3(0.0, 0.0, 0.6))
    text7.setAxisAlignment(osgText.Text.SCREEN)
    text7.setCharacterSizeMode(osgText.Text.OBJECT_COORDS)
    text7.setText("CharacterSizeMode OBJECT_COORDS (default)")
    geode.addDrawable(text7)



    shape =  new osg.ShapeDrawable(new osg.Sphere(center,characterSize*0.2f))
    shape.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.ON)
    geode.addDrawable(shape)

    rootNode =  new osg.Group
    rootNode.addChild(geode)

    rootNode = return()    

class UpdateTextOperation : public osg.Operation
public:

    UpdateTextOperation( osg.Vec3 center, float diameter, osg.Group* group):        
        Operation("UpdateTextOperation", true),
        _center(center),
        _diameter(diameter),
        _maxNumChildren(200),
        _maxNumTextPerGeode(10),
        _group(group)

    virtual void operator () (osg.Object* callingObject)
        # decided which method to call according to whole has called me.
        viewer =  dynamic_cast<osgViewer.Viewer*>(callingObject)

        if viewer : update()
        load = else:()
    
    def update():
        # osg.notify(osg.NOTICE), "*** Doing update"
        
        OpenThreads.ScopedLock<OpenThreads.Mutex> lock(_mutex)
        
        if _mergeSubgraph.valid() :
            _group.addChild(_mergeSubgraph.get())

            _mergeSubgraph = 0

            if _group.getNumChildren()>_maxNumChildren :
                geode =  dynamic_cast<osg.Geode*>(_group.getChild(0))
                if geode :
                    _availableSubgraph.push_back(geode)
                    geode.removeDrawables(0,geode.getNumDrawables())
                _group.removeChild(0,1)
            
            _waitOnMergeBlock.release()
    
    def load():
        # osg.notify(osg.NOTICE), "Doing load"

        osg.ref_ptr<osg.Geode> geode
            OpenThreads.ScopedLock<OpenThreads.Mutex> lock(_mutex)
            if !_availableSubgraph.empty() :
                geode = _availableSubgraph.front()
                _availableSubgraph.pop_front()
        
        if !geode : geode = new osg.Geode

        for(unsigned int i=0 i<_maxNumTextPerGeode ++i)
            x =  float(rand()) / float(RAND_MAX) - 0.5f
            y =  float(rand()) / float(RAND_MAX) - 0.5f
            z =  float(i)      / float(_maxNumTextPerGeode) - 0.5f
            position = osg.Vec3(x, y, z)

            str = str()
            unsigned int _numCharacters = 5
            for(unsigned int ni=0 ni<_numCharacters++ni)
                str.push_back(char(32.0 + (float(rand())/float(RAND_MAX))*128.0f))
                        
            text =  new osgText.Text
            text.setDataVariance(osg.Object.DYNAMIC)
            text.setPosition(_center + position * _diameter)
            text.setFont("times.ttf")
            text.setText(str)
            text.setCharacterSize(0.025f * _diameter)
            text.setAxisAlignment(osgText.Text.SCREEN)
            
            geode.addDrawable(text)


            OpenThreads.ScopedLock<OpenThreads.Mutex> lock(_mutex)
            _mergeSubgraph = geode
        
        # osg.notify(osg.NOTICE), "Waiting on merge"

        _waitOnMergeBlock.block()

    
    virtual void release()
        _waitOnMergeBlock.release()

    typedef std.list< osg.ref_ptr<osg.Geode> > AvailableList

    _center = osg.Vec3()
    _diameter = float()
    unsigned int                _maxNumChildren
    unsigned int                _maxNumTextPerGeode
    
    _mutex = OpenThreads.Mutex()
    osg.ref_ptr<osg.Group>    _group
    osg.ref_ptr<osg.Geode>    _mergeSubgraph
    _availableSubgraph = AvailableList()
    _waitOnMergeBlock = OpenThreads.Block()
    
    unsigned int                _counter




def main(argc, argv):
    arguments = osg.ArgumentParser(argc, argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)
    
    typedef std.list< osg.ref_ptr<osg.OperationThread> > Threads

    operationThreads = Threads()
    osg.ref_ptr<UpdateTextOperation> updateOperation

    unsigned int numThreads = 0
    if arguments.read("--mt", numThreads) || arguments.read("--mt") :
        # construct a multi-threaded text updating test.
        if numThreads==0 : numThreads = 1
        
        # create a group to add everything into.
        mainGroup =  new osg.Group
        
        center = osg.Vec3(0.5f,0.5f,0.5f)
        diameter =  1.0f
        
        osg.ref_ptr<osg.Node> loadedModel = osgDB.readNodeFiles(arguments)
        if loadedModel.valid() :
            mainGroup.addChild(loadedModel.get())
            
            center = loadedModel.getBound().center()
            diameter = loadedModel.getBound().radius() * 2.0f
        
        for(unsigned int i=0 i<numThreads ++i)
            textGroup =  new osg.Group
            mainGroup.addChild(textGroup)

            # create the background thread
            operationThread =  new osg.OperationThread
            
            operationThreads.push_back(operationThread)

            # create the operation that will run in the background and
            # sync once per frame with the main viewer loop.
            updateOperation = new UpdateTextOperation(center, diameter, textGroup)

            # add the operation to the operation thread and start it.
            operationThread.add(updateOperation.get())
            operationThread.startThread()

            # add the operation to the viewer to sync once per frame.
            viewer.addUpdateOperation(updateOperation.get())


            # add a unit cube for the text to appear within.
            geode =  new osg.Geode
            geode.getOrCreateStateSet().setAttribute(new osg.PolygonMode(osg.PolygonMode.FRONT_AND_BACK,osg.PolygonMode.LINE))
            geode.addDrawable(new osg.ShapeDrawable(new osg.Box(center,diameter)))

            mainGroup.addChild(geode)
                
        viewer.setSceneData(mainGroup)        
    else:
        # prepare scene.
        center = osg.Vec3(0.0f,0.0f,0.0f)
        radius =  1.0f
        
        # make sure the root node is group so we can add extra nodes to it.
        group =  new osg.Group

        if true :
            # create the hud.
            camera =  new osg.Camera
            camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
            camera.setProjectionMatrixAsOrtho2D(0,1280,0,1024)
            camera.setViewMatrix(osg.Matrix.identity())
            camera.setClearMask(GL_DEPTH_BUFFER_BIT)
            camera.addChild(createHUDText())
            camera.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)

            group.addChild(camera)

        if true :
            group.addChild(create3DText(center,radius))

        # set the scene to render
        viewer.setSceneData(group)

    filename = str()
    if arguments.read("-o",filename) :
        osgDB.writeNodeFile(*viewer.getSceneData(),filename)
        return 0

    viewer.addEventHandler( new osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()) )
    viewer.addEventHandler(new osgViewer.StatsHandler())

    viewer.run()
    
    if !operationThreads.empty() :
        for(Threads.iterator itr = operationThreads.begin()
            itr != operationThreads.end()
            ++itr)
            (*itr).cancel()

    return 0



if __name__ == "__main__":
    main(sys.argv)
