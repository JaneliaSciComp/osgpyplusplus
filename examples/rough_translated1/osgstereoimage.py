#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgstereoimage"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgUtil
from osgpypp import osgViewer

# OpenSceneGraph example, osgstereoimage.
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


#include <osgViewer/Viewer>
#include <osgDB/fstream>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgUtil/Optimizer>

#include <osg/ImageStream>
#include <osg/Geode>
#include <osg/Notify>
#include <osg/MatrixTransform>
#include <osg/Switch>
#include <osg/TexMat>
#include <osg/Texture2D>

#include <iostream>

typedef std.vector<str> FileList

#include <osg/Program>
#include <osg/Shader>

def createColorToGreyscaleStateSet():
    stateset =  new osg.StateSet

    program =  new osg.Program
    stateset.setAttribute(program)

    fragSource = 
        "uniform sampler2D baseTexture\n"
        "uniform mat4 colorMatrix\n"
        "void main(void)\n"
        "\n"
        "    vec4 color = texture2D( baseTexture, gl_TexCoord[0].st )\n"
        "    gl_FragColor = colorMatrix * color\n"
        "\n"
    
    program.addShader(new osg.Shader(osg.Shader.FRAGMENT, fragSource))

    stateset.addUniform(new osg.Uniform("baseTexture",0))

    colorMatrix = osg.Matrixf(
        0.3f, 0.3f, 0.3f, 0.0f,
        0.59f, 0.59f, 0.59f, 0.0f,
        0.11f, 0.11f, 0.11f, 0.0f,
        0.0f, 0.0f, 0.0f, 1.0f
    )

    stateset.addUniform(new osg.Uniform("colorMatrix",colorMatrix))

    stateset = return()


def createSectorForImage(image, texmat, s, t, radius, height, length):
    flip =  image.getOrigin()==osg.Image.TOP_LEFT

    numSegments =  20
    Theta =  length/radius
    dTheta =  Theta/(float)(numSegments-1)

    ThetaZero =  height*s/(t*radius)

    # set up the texture.
    texture =  new osg.Texture2D
    texture.setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
    texture.setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)
    texture.setWrap(osg.Texture2D.WRAP_S,osg.Texture2D.CLAMP_TO_BORDER)
    texture.setWrap(osg.Texture2D.WRAP_T,osg.Texture2D.CLAMP_TO_BORDER)
    texture.setResizeNonPowerOfTwoHint(false)
    texture.setImage(image)

    # set up the drawstate.
    dstate =  new osg.StateSet
    dstate.setMode(GL_CULL_FACE,osg.StateAttribute.OFF)
    dstate.setMode(GL_LIGHTING,osg.StateAttribute.OFF)
    dstate.setTextureAttributeAndModes(0, texture,osg.StateAttribute.ON)
    dstate.setTextureAttribute(0, texmat)

    # set up the geoset.
    geom =  new osg.Geometry
    geom.setStateSet(dstate)

    coords =  new osg.Vec3Array()
    tcoords =  new osg.Vec2Array()

    i = int()
    angle =  -Theta/2.0f
    for(i=0
        i<numSegments
        ++i, angle+=dTheta)
        coords.push_back(osg.Vec3(sinf(angle)*radius,cosf(angle)*radius,height*0.5f)) # top
        coords.push_back(osg.Vec3(sinf(angle)*radius,cosf(angle)*radius,-height*0.5f)) # bottom.

        tcoords.push_back(osg.Vec2(angle/ThetaZero+0.5f, flip ? 0.0f : 1.0f)) # top
        tcoords.push_back(osg.Vec2(angle/ThetaZero+0.5f, flip ? 1.0f : 0.0f)) # bottom.


    colors =  new osg.Vec4Array()
    colors.push_back(osg.Vec4(1.0f,1.0f,1.0f,1.0f))

    elements =  new osg.DrawArrays(osg.PrimitiveSet.QUAD_STRIP,0,coords.size())



    geom.setVertexArray(coords)
    geom.setTexCoordArray(0,tcoords)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(elements)

    # set up the geode.
    geode =  new osg.Geode
    geode.addDrawable(geom)

    geode = return()


def loadImages(image1, image2, texmatLeft, texmatRight, radius, height, length):
    osg.ref_ptr<osg.Image> imageLeft = osgDB.readImageFile(image1)
    osg.ref_ptr<osg.Image> imageRight = osgDB.readImageFile(image2)
    if imageLeft.valid()  imageRight.valid() :
	streamLeft =  dynamic_cast<osg.ImageStream*>(imageLeft.get())
	if streamLeft : streamLeft.play()

	streamRight =  dynamic_cast<osg.ImageStream*>(imageRight.get())
	if streamRight : streamRight.play()


	average_s =  (imageLeft.s()+imageRight.s())*0.5f
	average_t =  (imageLeft.t()+imageRight.t())*0.5f
	geodeLeft =  createSectorForImage(imageLeft.get(),texmatLeft,average_s,average_t, radius, height, length)
	geodeLeft.setNodeMask(0x01)

	geodeRight =  createSectorForImage(imageRight.get(),texmatRight,average_s,average_t, radius, height, length)
	geodeRight.setNodeMask(0x02)

	imageGroup =  new osg.Group

	imageGroup.addChild(geodeLeft)
	imageGroup.addChild(geodeRight)
	imageGroup = return()
    else:
	print "Warning: Unable to load both image files, '", image1, "'  '", image2, "', required for stereo imaging."
	return 0

# create a switch containing a set of child each containing a
# stereo image pair.
def createScene(fileList, texmatLeft, texmatRight, radius, height, length):
    sw =  new osg.Switch

    # load the images.
    for(unsigned int i=0i+1<fileList.size()i+=2)
        imageGroup =  loadImages(fileList[i],fileList[i+1],texmatLeft,texmatRight, radius,  height, length)
        if imageGroup : sw.addChild(imageGroup)


    if sw.getNumChildren()>0 :
        # select first child.
        sw.setSingleChildOn(0)

    sw = return()

class SlideEventHandler : public osgGA.GUIEventHandler
public:

    SlideEventHandler()

    META_Object(osgStereImageApp,SlideEventHandler)


    set = void(osg.Switch* sw, float offsetX, float offsetY, osg.TexMat* texmatLeft, osg.TexMat* texmatRight, float timePerSlide, bool autoSteppingActive)

    set = void(FileList fileList, osg.Switch* sw, float offsetX, float offsetY, osg.TexMat* texmatLeft, osg.TexMat* texmatRight, float radius, float height, float length, float timePerSlide, bool autoSteppingActive)


    virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)

    virtual void getUsage(osg.ApplicationUsage usage) 

    virtual void operator()(osg.Node* node, osg.NodeVisitor* nv)

    nextSlide = void()

    previousSlide = void()

    scaleImage = void(float s)

    offsetImage = void(float ds,float dt)

    rotateImage = void(float rx,float ry)

    initTexMatrices = void()

protected:

    ~SlideEventHandler() 
    SlideEventHandler( SlideEventHandler, osg.CopyOp) 

    osg.ref_ptr<osg.Switch>   _switch
    osg.ref_ptr<osg.TexMat>   _texmatLeft
    osg.ref_ptr<osg.TexMat>   _texmatRight
    _radius = float()
    _height = float()
    _length = float()
    _firstTraversal = bool()
    unsigned int                _activeSlide
    _previousTime = double()
    _timePerSlide = double()
    _autoSteppingActive = bool()
    _initSeperationX = float()
    _currentSeperationX = float()
    _initSeperationY = float()
    _currentSeperationY = float()
    _fileList = FileList()



SlideEventHandler.SlideEventHandler():
    _switch(0),
    _texmatLeft(0),
    _texmatRight(0),
    _firstTraversal(true),
    _activeSlide(0),
    _previousTime(-1.0f),
    _timePerSlide(5.0),
    _autoSteppingActive(false)

void SlideEventHandler.set(osg.Switch* sw, float offsetX, float offsetY, osg.TexMat* texmatLeft, osg.TexMat* texmatRight, float timePerSlide, bool autoSteppingActive)
    _switch = sw
    _switch.setUpdateCallback(this)

    _texmatLeft = texmatLeft
    _texmatRight = texmatRight

    _timePerSlide = timePerSlide
    _autoSteppingActive = autoSteppingActive

    _initSeperationX = offsetX
    _currentSeperationX = _initSeperationX

    _initSeperationY = offsetY
    _currentSeperationY = _initSeperationY

    initTexMatrices()


void SlideEventHandler.set(FileList fileList, osg.Switch* sw, float offsetX, float offsetY, osg.TexMat* texmatLeft, osg.TexMat* texmatRight, float radius, float height, float length, float timePerSlide, bool autoSteppingActive)
    _switch = sw
    _switch.setUpdateCallback(this)
    _fileList=FileList(fileList)

    osg.ref_ptr<osg.Group> imageGroup = loadImages(fileList[0],fileList[1],texmatLeft,texmatRight, radius,  height, length)
    if imageGroup.get() :_switch.addChild(imageGroup.get())

    _texmatLeft = texmatLeft
    _texmatRight = texmatRight

    _radius=radius
    _height=height
    _length=length

    _timePerSlide = timePerSlide
    _autoSteppingActive = autoSteppingActive

    _initSeperationX = offsetX
    _currentSeperationX = _initSeperationX

    _initSeperationY = offsetY
    _currentSeperationY = _initSeperationY

    initTexMatrices()


bool SlideEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()=='a' :
                _autoSteppingActive = !_autoSteppingActive
                _previousTime = ea.getTime()
                true = return()
            else: if ea.getKey()=='n' : || (ea.getKey()==osgGA.GUIEventAdapter.KEY_Right) :
                nextSlide()
                true = return()
            else: if ea.getKey()=='p' : || (ea.getKey()==osgGA.GUIEventAdapter.KEY_Left) :
                previousSlide()
                true = return()
            else: if ea.getKey()=='w' : || (ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Add) :
                scaleImage(0.99f)
                true = return()
            else: if ea.getKey()=='s' : || (ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Subtract) :
                scaleImage(1.01f)
                true = return()
            else: if ea.getKey()=='j' :
                offsetImage(-0.001f,0.0f)
                true = return()
            else: if ea.getKey()=='k' :
                offsetImage(0.001f,0.0f)
                true = return()
            else: if ea.getKey()=='i' :
                offsetImage(0.0f,-0.001f)
                true = return()
            else: if ea.getKey()=='m' :
                offsetImage(0.0f,0.001f)
                true = return()
            else: if ea.getKey()==' ' :
                initTexMatrices()
                true = return()
            false = return()
        case(osgGA.GUIEventAdapter.DRAG):
        case(osgGA.GUIEventAdapter.MOVE):
            static float px = ea.getXnormalized()
            static float py = ea.getYnormalized()

            dx =  ea.getXnormalized()-px
            dy =  ea.getYnormalized()-py

            px = ea.getXnormalized()
            py = ea.getYnormalized()

            rotateImage(dx,dy)

            true = return()

        default:
            false = return()

void SlideEventHandler.getUsage(osg.ApplicationUsage usage) 
    usage.addKeyboardMouseBinding("Space","Reset the image position to center")
    usage.addKeyboardMouseBinding("a","Toggle on/off the automatic advancement for image to image")
    usage.addKeyboardMouseBinding("n","Advance to next image")
    usage.addKeyboardMouseBinding("p","Move to previous image")
    usage.addKeyboardMouseBinding("q","Zoom into the image")
    usage.addKeyboardMouseBinding("a","Zoom out of the image")
    usage.addKeyboardMouseBinding("j","Reduce horizontal offset")
    usage.addKeyboardMouseBinding("k","Increase horizontal offset")
    usage.addKeyboardMouseBinding("m","Reduce vertical offset")
    usage.addKeyboardMouseBinding("i","Increase vertical offset")

void SlideEventHandler.operator()(osg.Node* node, osg.NodeVisitor* nv)
    if _autoSteppingActive  nv.getFrameStamp() :
        time =  nv.getFrameStamp().getSimulationTime()

        if _firstTraversal :
            _firstTraversal = false
            _previousTime = time
        else: if time-_previousTime>_timePerSlide :
            _previousTime = time

            nextSlide()


    traverse(node,nv)

void SlideEventHandler.nextSlide()

    if _switch.getNumChildren()==0 : return

    ++_activeSlide

    if _fileList.size()>0 : 
        if _activeSlide>= _fileList.size()/2  : _activeSlide = 0
        osg.ref_ptr<osg.Group> images = loadImages(_fileList[2*_activeSlide],_fileList[2*_activeSlide+1],_texmatLeft.get(),_texmatRight.get(),_radius,_height,_length)
        if images.valid() : _switch.replaceChild(_switch.getChild(0),images.get())

     else: 
        if _activeSlide>=_switch.getNumChildren() : _activeSlide = 0

        _switch.setSingleChildOn(_activeSlide)

void SlideEventHandler.previousSlide()
    if _switch.getNumChildren()==0 : return

    if _fileList.size()>0 : 
        if _activeSlide==0 : _activeSlide = _fileList.size()/2-1
        else: --_activeSlide
        osg.ref_ptr<osg.Group> images = loadImages(_fileList[2*_activeSlide],_fileList[2*_activeSlide+1],_texmatLeft.get(),_texmatRight.get(),_radius,_height,_length)
        if images.valid() : _switch.replaceChild(_switch.getChild(0),images.get())
     else: 
        if _activeSlide==0 : _activeSlide = _switch.getNumChildren()-1
        else: --_activeSlide

        _switch.setSingleChildOn(_activeSlide)

void SlideEventHandler.scaleImage(float s)
    _texmatLeft.setMatrix(_texmatLeft.getMatrix()*osg.Matrix.translate(-0.5f,-0.5f,0.0f)*osg.Matrix.scale(s,s,1.0f)*osg.Matrix.translate(0.5f,0.5f,0.0f))
    _texmatRight.setMatrix(_texmatRight.getMatrix()*osg.Matrix.translate(-0.5f,-0.5f,0.0f)*osg.Matrix.scale(s,s,1.0f)*osg.Matrix.translate(0.5f,0.5f,0.0f))

void SlideEventHandler.offsetImage(float ds,float dt)
    _currentSeperationX+=ds
    _currentSeperationY+=dt
    osg.notify(osg.NOTICE), "image offset x = ", _currentSeperationX, "  y =", _currentSeperationY
    _texmatLeft.setMatrix(_texmatLeft.getMatrix()*osg.Matrix.translate(ds,dt,0.0f))
    _texmatRight.setMatrix(_texmatRight.getMatrix()*osg.Matrix.translate(-ds,-dt,0.0f))

void SlideEventHandler.rotateImage(float rx,float ry)
    scale =  0.5f
    _texmatLeft.setMatrix(_texmatLeft.getMatrix()*osg.Matrix.translate(-rx*scale,-ry*scale,0.0f))
    _texmatRight.setMatrix(_texmatRight.getMatrix()*osg.Matrix.translate(-rx*scale,-ry*scale,0.0f))

void SlideEventHandler.initTexMatrices()
    _texmatLeft.setMatrix(osg.Matrix.translate(_initSeperationX,_initSeperationY,0.0f))
    _texmatRight.setMatrix(osg.Matrix.translate(-_initSeperationX,-_initSeperationY,0.0f))



def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is the example which demonstrates use node masks to create stereo images.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] image_file_left_eye image_file_right_eye")
    arguments.getApplicationUsage().addCommandLineOption("-d <float>","Time delay in seconds between the display of successive image pairs when in auto advance mode.")
    arguments.getApplicationUsage().addCommandLineOption("-a","Enter auto advance of image pairs on start up.")
    arguments.getApplicationUsage().addCommandLineOption("-x <float>","Horizontal offset of left and right images.")
    arguments.getApplicationUsage().addCommandLineOption("-y <float>","Vertical offset of left and right images.")
    arguments.getApplicationUsage().addCommandLineOption("--disk","Keep images on disk")
    arguments.getApplicationUsage().addCommandLineOption("-files <filename>","Load filenames from a file")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--SingleThreaded","Select SingleThreaded threading model for viewer.")
    arguments.getApplicationUsage().addCommandLineOption("--CullDrawThreadPerContext","Select CullDrawThreadPerContext threading model for viewer.")
    arguments.getApplicationUsage().addCommandLineOption("--DrawThreadPerContext","Select DrawThreadPerContext threading model for viewer.")
    arguments.getApplicationUsage().addCommandLineOption("--CullThreadPerCameraDrawThreadPerContext","Select CullThreadPerCameraDrawThreadPerContext threading model for viewer.")


    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    # register the handler to add keyboard and mouse handling.
    seh =  new SlideEventHandler()
    viewer.addEventHandler(seh)

    # read any time delay argument.
    timeDelayBetweenSlides =  5.0f
    while arguments.read("-d",timeDelayBetweenSlides) : 

    autoSteppingActive =  false
    while arguments.read("-a") : autoSteppingActive = true

    offsetX = 0.0f
    while arguments.read("-x",offsetX) : 

    offsetY = 0.0f
    while arguments.read("-y",offsetY) : 

    onDisk = false
    while arguments.read("--disk") :  onDisk=true

    filename = ""
    fileList = FileList()
    # extract the filenames from the a file, one filename per line.
    while arguments.read("-files",filename) : 
        is = osgDB.ifstream(filename.c_str())
        if is : 
                line = str()
                while std.getline(is,line,'\n') : fileList.push_back(line)
                is.close()


    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    threading =  osgViewer.Viewer.SingleThreaded
    while arguments.read("--SingleThreaded") : threading = osgViewer.Viewer.SingleThreaded
    while arguments.read("--CullDrawThreadPerContext") : threading = osgViewer.Viewer.CullDrawThreadPerContext
    while arguments.read("--DrawThreadPerContext") : threading = osgViewer.Viewer.DrawThreadPerContext
    while arguments.read("--CullThreadPerCameraDrawThreadPerContext") : threading = osgViewer.Viewer.CullThreadPerCameraDrawThreadPerContext

    viewer.setThreadingModel(threading)

    # any option left unread are converted into errors to write out later.
    arguments.reportRemainingOptionsAsUnrecognized()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    # extract the filenames from the arguments list.
    for(int pos=1pos<arguments.argc()++pos)
        if arguments.isString(pos) : fileList.push_back(arguments[pos])

    if fileList.empty() :
        fileList.push_back("Images/dog_left_eye.jpg")
         fileList.push_back("Images/dog_right_eye.jpg")
    else: if fileList.size()<2 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

    # now the windows have been realized we switch off the cursor to prevent it
    # distracting the people seeing the stereo images.
    double fovy, aspectRatio, zNear, zFar
    viewer.getCamera().getProjectionMatrixAsPerspective(fovy, aspectRatio, zNear, zFar)

    radius =  1.0f
    height =  2*radius*tan(osg.DegreesToRadians(fovy)*0.5f)
    length =  osg.PI*radius  # half a cylinder.

    # use a texture matrix to control the placement of the image.
    texmatLeft =  new osg.TexMat
    texmatRight =  new osg.TexMat

    # creat the scene from the file list.
    osg.ref_ptr<osg.Switch> rootNode
    if !onDisk :  rootNode = createScene(fileList,texmatLeft,texmatRight,radius,height,length)
    rootNode = new osg.Switch()

    #osgDB.writeNodeFile(*rootNode,"test.osgt")



    viewer.getCamera().setCullMask(0xffffffff)
    viewer.getCamera().setCullMaskLeft(0x00000001)
    viewer.getCamera().setCullMaskRight(0x00000002)

    # set up the use of stereo by default.
    osg.DisplaySettings.instance().setStereo(true)

    if osg.DisplaySettings.instance().getStereoMode()==osg.DisplaySettings.ANAGLYPHIC :
        rootNode.setStateSet(createColorToGreyscaleStateSet())


    # set the scene to render
    viewer.setSceneData(rootNode.get())


    # create the windows and run the threads.
    viewer.realize()


    # switch off the cursor
    windows = osgViewer.Viewer.Windows()
    viewer.getWindows(windows)
    for(osgViewer.Viewer.Windows.iterator itr = windows.begin()
        itr != windows.end()
        ++itr)
        (*itr).useCursor(false)

    viewer.setFusionDistance(osgUtil.SceneView.USE_FUSION_DISTANCE_VALUE,radius)

    # set up the SlideEventHandler.
    if onDisk : seh.set(fileList,rootNode.get(),offsetX,offsetY,texmatLeft,texmatRight,radius,height,length,timeDelayBetweenSlides,autoSteppingActive)
    else: seh.set(rootNode.get(),offsetX,offsetY,texmatLeft,texmatRight,timeDelayBetweenSlides,autoSteppingActive)

    homePosition = osg.Matrix()
    homePosition.makeLookAt(osg.Vec3(0.0f,0.0f,0.0f),osg.Vec3(0.0f,1.0f,0.0f),osg.Vec3(0.0f,0.0f,1.0f))

    while  !viewer.done()  :
        viewer.getCamera().setViewMatrix(homePosition)

        # fire off the cull and draw traversals of the scene.
        viewer.frame()


    return 0



if __name__ == "__main__":
    main(sys.argv)
