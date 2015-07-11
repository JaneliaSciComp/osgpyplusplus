#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgqfont"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgQt
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osgqfont.cpp'

# OpenSceneGraph example, osgtext.
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

#include <QApplication>
#include <QGridLayout>
#include <QWidget>

#include <osgQt/GraphicsWindowQt>
#include <osgQt/QFontImplementation>

#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgDB/Registry>

#include <osgGA/StateSetManipulator>
#include <osgGA/TrackballManipulator>
#include <osgViewer/CompositeViewer>
#include <osgViewer/ViewerEventHandlers>

#include <osg/Geode>
#include <osg/Camera>
#include <osg/ShapeDrawable>
#include <osg/Sequence>
#include <osg/PolygonMode>

#include <osgText/Font>
#include <osgText/Text>

def createHUDText():

    

    rootNode = osg.Group()

    font = osgText.Font(osgQt.QFontImplementation(QFont("Arial")))

    geode = osg.Geode()
    rootNode.addChild(geode)

    windowHeight = 1024.0
    windowWidth = 1280.0
    margin = 50.0


####################################################
#    
# Examples of how to set up different text layout
#

    layoutColor = osg.Vec4(1.0,1.0,0.0,1.0)
    layoutCharacterSize = 20.0    
    
        text = osgText.Text()
        text.setFont(font)
        text.setColor(layoutColor)
        text.setCharacterSize(layoutCharacterSize)
        text.setPosition(osg.Vec3(margin,windowHeight-margin,0.0))

        # the default layout is left to right, typically used in languages
        # originating from europe such as English, French, German, Spanish etc..
        text.setLayout(osgText.Text.LEFT_TO_RIGHT)

        text.setText("text.setLayout(osgText.Text.LEFT_TO_RIGHT)")
        geode.addDrawable(text)

        text = osgText.Text()
        text.setFont(font)
        text.setColor(layoutColor)
        text.setCharacterSize(layoutCharacterSize)
        text.setPosition(osg.Vec3(windowWidth-margin,windowHeight-margin,0.0))

        # right to left layouts would be used for hebrew or arabic fonts.
        text.setLayout(osgText.Text.RIGHT_TO_LEFT)
        text.setAlignment(osgText.Text.RIGHT_BASE_LINE)

        text.setText("text.setLayout(osgText.Text.RIGHT_TO_LEFT)")
        geode.addDrawable(text)

        text = osgText.Text()
        text.setFont(font)
        text.setColor(layoutColor)
        text.setPosition(osg.Vec3(margin,windowHeight-margin,0.0))
        text.setCharacterSize(layoutCharacterSize)

        # vertical font layout would be used for asian fonts.
        text.setLayout(osgText.Text.VERTICAL)

        text.setText("text.setLayout(osgText.Text.VERTICAL)")
        geode.addDrawable(text)
    
    
####################################################
#    
# Examples of how to set up different font resolution
#

    fontSizeColor = osg.Vec4(0.0,1.0,1.0,1.0)
    fontSizeCharacterSize = 30
    
    cursor = osg.Vec3(margin*2,windowHeight-margin*2,0.0)
    
        text = osgText.Text()
        text.setFont(font)
        text.setColor(fontSizeColor)
        text.setCharacterSize(fontSizeCharacterSize)
        text.setPosition(cursor)
        
        # use text that uses 10 by 10 texels as a target resolution for fonts.
        text.setFontResolution(10,10) # blocky but small texture memory usage
        
        text.setText("text.setFontResolution(10,10) # blocky but small texture memory usage")
        geode.addDrawable(text)
    
    cursor.y() -= fontSizeCharacterSize
        text = osgText.Text()
        text.setFont(font)
        text.setColor(fontSizeColor)
        text.setCharacterSize(fontSizeCharacterSize)
        text.setPosition(cursor)
        
        # use text that uses 20 by 20 texels as a target resolution for fonts.
        text.setFontResolution(20,20) # smoother but higher texture memory usage (but still quite low).
        
        text.setText("text.setFontResolution(20,20) # smoother but higher texture memory usage (but still quite low).")
        geode.addDrawable(text)
    
    cursor.y() -= fontSizeCharacterSize
        text = osgText.Text()
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

    characterSizeColor = osg.Vec4(1.0,0.0,1.0,1.0)
    
    cursor.y() -= fontSizeCharacterSize*2.0
    
        text = osgText.Text()
        text.setFont(font)
        text.setColor(characterSizeColor)
        text.setFontResolution(20,20)
        text.setPosition(cursor)
        
        # use text that is 20 units high.
        text.setCharacterSize(20) # small
        
        text.setText("text.setCharacterSize(20.0) # small")
        geode.addDrawable(text)
    
    cursor.y() -= 30.0
        text = osgText.Text()
        text.setFont(font)
        text.setColor(characterSizeColor)
        text.setFontResolution(30,30)
        text.setPosition(cursor)
        
        # use text that is 30 units high.
        text.setCharacterSize(30.0) # medium
        
        text.setText("text.setCharacterSize(30.0) # medium")
        geode.addDrawable(text)
    
    cursor.y() -= 50.0
        text = osgText.Text()
        text.setFont(font)
        text.setColor(characterSizeColor)
        text.setFontResolution(40,40)
        text.setPosition(cursor)
        
        # use text that is 60 units high.
        text.setCharacterSize(60.0) # large
        
        text.setText("text.setCharacterSize(60.0) # large")
        geode.addDrawable(text)


####################################################
#    
# Examples of how to set up different alignments
#

    alignmentSizeColor = osg.Vec4(0.0,1.0,0.0,1.0)
    alignmentCharacterSize = 25.0
    cursor.x() = 640
    cursor.y() = margin*4.0
    
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


    sequence = osg.Sequence()
        for(AlignmentList.iterator itr=alignmentList.begin()
            itr!=alignmentList.end()
            ++itr)
            alignmentGeode = osg.Geode()
            sequence.addChild(alignmentGeode)
            sequence.setTime(sequence.getNumChildren(), 1.0)

            text = osgText.Text()
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
    sequence.setDuration(1.0, -1)
    
    rootNode.addChild(sequence)


####################################################
#    
# Examples of how to set up different fonts...
#

    cursor.x() = margin*2.0
    cursor.y() = margin*2.0
    
    fontColor = osg.Vec4(1.0,0.5,0.0,1.0)
    fontCharacterSize = 20.0
    spacing = 40.0
    
        text = osgText.Text()
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(0)
        text.setText("text.setFont(0) # inbuilt font.")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
    
        arial = osgText.Font(osgQt.QFontImplementation(QFont("Arial")))

        text = osgText.Text()
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(arial)
        text.setText(arial!=0?
                      "text.setFont(\"fonts/arial.ttf\")":
                      "unable to load \"fonts/arial.ttf\"")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
    
        times = osgText.Font(osgQt.QFontImplementation(QFont("Times")))

        text = osgText.Text()
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        geode.addDrawable(text)
        text.setFont(times)
        text.setText(times!=0?
                      "text.setFont(\"fonts/times.ttf\")":
                      "unable to load \"fonts/times.ttf\"")

        cursor.x() = text.getBound().xMax() + spacing 
    
    cursor.x() = margin*2.0
    cursor.y() = margin

        dirtydoz = osgText.Font(osgQt.QFontImplementation(QFont("Times")))

        text = osgText.Text()
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(dirtydoz)
        text.setText(dirtydoz!=0?
                      "text.setFont(\"fonts/dirtydoz.ttf\")":
                      "unable to load \"fonts/dirtydoz.ttf\"")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
    
        fudd = osgText.Font(osgQt.QFontImplementation(QFont("Times")))
    
        text = osgText.Text()
        text.setColor(fontColor)
        text.setPosition(cursor)
        text.setCharacterSize(fontCharacterSize)
        
        text.setFont(fudd)
        text.setText(fudd!=0?
                      "text.setFont(\"fonts/fudd.ttf\")":
                      "unable to load \"fonts/fudd.ttf\"")
        geode.addDrawable(text)

        cursor.x() = text.getBound().xMax() + spacing 
            
    return rootNode    




# create text which sits in 3D space such as would be inserted into a normal model
def create3DText(center, radius):
    

    geode = osg.Geode()

####################################################
#    
# Examples of how to set up axis/orientation alignments
#

    characterSize = radius*0.2
    
    pos = osg.Vec3(center.x()-radius*.5,center.y()-radius*.5,center.z()-radius*.5)

    text1 = osgText.Text()
    text1.setFont(osgText.Font(osgQt.QFontImplementation(QFont("Times"))))
    text1.setCharacterSize(characterSize)
    text1.setPosition(pos)
    text1.setAxisAlignment(osgText.Text.XY_PLANE)
    text1.setText("XY_PLANE")
    geode.addDrawable(text1)

    text2 = osgText.Text()
    text2.setFont(osgText.Font(osgQt.QFontImplementation(QFont("Times"))))
    text2.setCharacterSize(characterSize)
    text2.setPosition(pos)
    text2.setAxisAlignment(osgText.Text.YZ_PLANE)
    text2.setText("YZ_PLANE")
    geode.addDrawable(text2)

    text3 = osgText.Text()
    text3.setFont(osgText.Font(osgQt.QFontImplementation(QFont("Times"))))
    text3.setCharacterSize(characterSize)
    text3.setPosition(pos)
    text3.setAxisAlignment(osgText.Text.XZ_PLANE)
    text3.setText("XZ_PLANE")
    geode.addDrawable(text3)


    text4 = osgText.Text()
    text4.setFont(osgText.Font(osgQt.QFontImplementation(QFont("Times"))))
    text4.setCharacterSize(characterSize)
    text4.setPosition(center)
    text4.setAxisAlignment(osgText.Text.SCREEN)

    characterSizeModeColor = osg.Vec4(1.0,0.0,0.5,1.0)

    text5 = osgText.Text()
    text5.setColor(characterSizeModeColor)
    text5.setFont(osgText.Font(osgQt.QFontImplementation(QFont("Times"))))
    #text5.setCharacterSize(characterSize)
    text5.setCharacterSize(32.0) # medium
    text5.setPosition(center - osg.Vec3(0.0, 0.0, 0.2))
    text5.setAxisAlignment(osgText.Text.SCREEN)
    text5.setCharacterSizeMode(osgText.Text.SCREEN_COORDS)
    text5.setText("CharacterSizeMode SCREEN_COORDS(size 32.0)")
    geode.addDrawable(text5)

    text6 = osgText.Text()
    text6.setColor(characterSizeModeColor)
    text6.setFont(osgText.Font(osgQt.QFontImplementation(QFont("Times"))))
    text6.setCharacterSize(characterSize)
    text6.setPosition(center - osg.Vec3(0.0, 0.0, 0.4))
    text6.setAxisAlignment(osgText.Text.SCREEN)
    text6.setCharacterSizeMode(osgText.Text.OBJECT_COORDS_WITH_MAXIMUM_SCREEN_SIZE_CAPPED_BY_FONT_HEIGHT)
    text6.setText("CharacterSizeMode OBJECT_COORDS_WITH_MAXIMUM_SCREEN_SIZE_CAPPED_BY_FONT_HEIGHT")
    geode.addDrawable(text6)

    text7 = osgText.Text()
    text7.setColor(characterSizeModeColor)
    text7.setFont(osgText.Font(osgQt.QFontImplementation(QFont("Times"))))
    text7.setCharacterSize(characterSize)
    text7.setPosition(center - osg.Vec3(0.0, 0.0, 0.6))
    text7.setAxisAlignment(osgText.Text.SCREEN)
    text7.setCharacterSizeMode(osgText.Text.OBJECT_COORDS)
    text7.setText("CharacterSizeMode OBJECT_COORDS (default)")
    geode.addDrawable(text7)

#if 1
    # reproduce outline bounding box compute problem with backdrop on.
    text4.setBackdropType(osgText.Text.OUTLINE)
    text4.setDrawMode(osgText.Text.TEXT | osgText.Text.BOUNDINGBOX)
#endif

    text4.setText("SCREEN")
    geode.addDrawable(text4)

    shape = osg.ShapeDrawable(osg.Sphere(center,characterSize*0.2))
    shape.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.ON)
    geode.addDrawable(shape)

    rootNode = osg.Group()
    rootNode.addChild(geode)

    return rootNode    

class MainWindow (QWidget) :
    MainWindow()
        traits = osg.GraphicsContext.Traits(osg.DisplaySettings.instance().get())
        traits.width = width()
        traits.height = height()
        traits.doubleBuffer = True
        graphicsWindow = osgQt.GraphicsWindowQt(traits.get())

        grid = QGridLayout()
        grid.setMargin(0)
        grid.addWidget(graphicsWindow.getGLWidget(), 0, 0)
        setLayout(grid)

        _viewer.setThreadingModel(osgViewer.Viewer.SingleThreaded)

        camera = _viewer.getCamera()
        camera.setGraphicsContext(graphicsWindow)
        camera.setViewport(osg.Viewport(0, 0, width(), height()))

        startTimer(10)

    def paintEvent(event):

        
        _viewer.frame()
    def timerEvent(event):
        
        _viewer.frame()

    def setSceneData(node):

        
        _viewer.setSceneData(node)
    def setCameraManipulator(manipulator, resetPosition):
        
        _viewer.setCameraManipulator(manipulator, resetPosition)
    _viewer = osgViewer.Viewer()


def main(argc, argv):

    
    app = QApplication(argc, argv)

    # prepare scene.
    center = osg.Vec3(0.0,0.0,0.0)
    radius = 1.0
    
    # create the hud.
    camera = osg.Camera()
    camera.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    camera.setProjectionMatrixAsOrtho2D(0,1280,0,1024)
    camera.setViewMatrix(osg.Matrix.identity())
    camera.setClearMask(GL_DEPTH_BUFFER_BIT)
    camera.addChild(createHUDText())
    camera.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)
    
    # make sure the root node is group so we can add extra nodes to it.
    group = osg.Group()
    group.addChild(camera.get())
    group.addChild(create3DText(center, radius))

    # The qt window
    widget = MainWindow()
    
    # set the scene to render
    widget.setSceneData(group.get())
    widget.setCameraManipulator(osgGA.TrackballManipulator)()

    widget.setGeometry(100, 100, 800, 600)
    widget.show()

    return app.exec()


if __name__ == "__main__":
    main(sys.argv)
