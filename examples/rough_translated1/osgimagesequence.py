#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgimagesequence"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgViewer


# Translated from file 'osgimagesequence.cpp'

# OpenSceneGraph example, osgtexture3D.
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

#include <osg/Node>
#include <osg/Geometry>
#include <osg/Notify>
#include <osg/Texture1D>
#include <osg/Texture2D>
#include <osg/Texture3D>
#include <osg/TextureRectangle>
#include <osg/ImageSequence>
#include <osg/Geode>

#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgDB/WriteFile>
#include <osgDB/FileNameUtils>
#include <osgDB/FileUtils>


#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <iostream>


static osgDB.DirectoryContents getSuitableFiles(osg.ArgumentParser arguments)
    files = osgDB.DirectoryContents()
    for(int i=1 i<arguments.argc() ++i)
        if osgDB.fileType(arguments[i]) == osgDB.DIRECTORY :
            directory = arguments[i]
            dc = osgDB.getSortedDirectoryContents(directory)
            
            for(osgDB.DirectoryContents.iterator itr = dc.begin() itr != dc.end() ++itr)
                full_file_name = directory + "/" + (*itr)
                ext = osgDB.getLowerCaseFileExtension(full_file_name)
                if ext == "jpg" : || (ext == "png") || (ext == "gif") ||  (ext == "rgb") || (ext == "dds")  :
                    files.push_back(full_file_name)
        else : 
            files.push_back(arguments[i])
    return files


#
# A simple demo demonstrating how to set on an animated texture using an osg.ImageSequence
#

def createState(arguments):

    
    imageSequence = osg.ImageSequence()

    preLoad = True
        
    while arguments.read("--page-and-discard") :
        imageSequence.setMode(osg.ImageSequence.PAGE_AND_DISCARD_USED_IMAGES)
        preLoad = False
    
    while arguments.read("--page-and-retain") :
        imageSequence.setMode(osg.ImageSequence.PAGE_AND_RETAIN_IMAGES)
        preLoad = False
    
    while arguments.read("--preload") :
        imageSequence.setMode(osg.ImageSequence.PRE_LOAD_ALL_IMAGES)
        preLoad = True
    
    length = -1.0
    while arguments.read("--length",length) : 
    
    fps = 30.0
    while arguments.read("--fps",fps) : 

    files = getSuitableFiles(arguments)
    if !files.empty() :
        for(osgDB.DirectoryContents.iterator itr = files.begin()
            itr != files.end()
            ++itr)
            filename = *itr
            if preLoad :
                image = osgDB.readImageFile(filename)
                if image.valid() :
                    imageSequence.addImage(image.get())
            else :
                imageSequence.addImageFile(filename)

        
        if length>0.0 :
            imageSequence.setLength(length)
        else :
            maxNum = imageSequence.getNumImageData()
            imageSequence.setLength(double(maxNum)*(1.0/fps))
    else :
        if length>0.0 :
            imageSequence.setLength(length)
        else :
            imageSequence.setLength(4.0)
        imageSequence.addImage(osgDB.readImageFile("Cubemap_axis/posx.png"))
        imageSequence.addImage(osgDB.readImageFile("Cubemap_axis/negx.png"))
        imageSequence.addImage(osgDB.readImageFile("Cubemap_axis/posy.png"))
        imageSequence.addImage(osgDB.readImageFile("Cubemap_axis/negy.png"))
        imageSequence.addImage(osgDB.readImageFile("Cubemap_axis/posz.png"))
        imageSequence.addImage(osgDB.readImageFile("Cubemap_axis/negz.png"))
        
    # start the image sequence playing
    imageSequence.play()

#if 1
    texture = osg.Texture2D()
    texture.setFilter(osg.Texture.MIN_FILTER,osg.Texture.LINEAR)
    texture.setFilter(osg.Texture.MAG_FILTER,osg.Texture.LINEAR)
    texture.setWrap(osg.Texture.WRAP_R,osg.Texture.REPEAT)
    texture.setResizeNonPowerOfTwoHint(False)
    texture.setImage(imageSequence.get())
    #texture.setTextureSize(512,512)
#else :    
    texture = osg.TextureRectangle()
    texture.setFilter(osg.Texture.MIN_FILTER,osg.Texture.LINEAR)
    texture.setFilter(osg.Texture.MAG_FILTER,osg.Texture.LINEAR)
    texture.setWrap(osg.Texture.WRAP_R,osg.Texture.REPEAT)
    texture.setImage(imageSequence.get())
    #texture.setTextureSize(512,512)
#endif

    # create the StateSet to store the texture data
    stateset = osg.StateSet()

    stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

    return stateset

def createModel(arguments):

    

    # create the geometry of the model, just a simple 2d quad right now.    
    geode = osg.Geode()
    geode.addDrawable(osg.createTexturedQuadGeometry(osg.Vec3(0.0,0.0,0.0), osg.Vec3(1.0,0.0,0.0), osg.Vec3(0.0,0.0,1.0)))

    geode.setStateSet(createState(arguments))
    
    return geode



s_imageStream = 0
class MovieEventHandler (osgGA.GUIEventHandler) :

    MovieEventHandler():_playToggle(True),_trackMouse(False) 
    
    def setMouseTracking(track):
    
         _trackMouse = track 
    def getMouseTracking():
         return _trackMouse 
    
    set = void(osg.Node* node)

    def setTrackMouse(tm):

        
        if tm==_trackMouse : return

        _trackMouse = tm

        print "tracking mouse: ", (_trackMouse ? "ON" : "OFF")

        for(ImageStreamList.iterator itr=_imageStreamList.begin()
            itr!=_imageStreamList.end()
            ++itr)
            if *itr :.getStatus()==osg.ImageStream.PLAYING :
                (*itr).pause()
            else :
                (*itr).play()


    def getTrackMouse():

         return _trackMouse 

    handle = virtual bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa, osg.Object*, osg.NodeVisitor* nv)
    
    virtual void getUsage(osg.ApplicationUsage usage) 

    typedef std.vector< osg.observer_ptr<osg.ImageStream> > ImageStreamList
    
    class ImageStreamPlaybackSpeedData :
fps = double()
        lastData = unsigned char*()
        double timeStamp, lastOutput
        
        ImageStreamPlaybackSpeedData() : fps(0), lastData(NULL), timeStamp(0), lastOutput(0) 
        
    
    
    typedef std.vector< ImageStreamPlaybackSpeedData > ImageStreamPlayBackSpeedList

    virtual ~MovieEventHandler() 

    class FindImageStreamsVisitor (osg.NodeVisitor) :
        FindImageStreamsVisitor(ImageStreamList imageStreamList):
            _imageStreamList(imageStreamList) 
            
        def apply(geode):
            
            
            apply(geode.getStateSet())

            for(unsigned int i=0i<geode.getNumDrawables()++i)
                apply(geode.getDrawable(i).getStateSet())
        
            traverse(geode)

        def apply(node):

            
            apply(node.getStateSet())
            traverse(node)
        
        inline void apply(osg.StateSet* stateset)
            if !stateset : return
            
            attr = stateset.getTextureAttribute(0,osg.StateAttribute.TEXTURE)
            if attr :
                texture2D = dynamic_cast<osg.Texture2D*>(attr)
                if texture2D : apply(dynamic_cast<osg.ImageStream*>(texture2D.getImage()))

                textureRec = dynamic_cast<osg.TextureRectangle*>(attr)
                if textureRec : apply(dynamic_cast<osg.ImageStream*>(textureRec.getImage()))
        
        inline void apply(osg.ImageStream* imagestream)
            if imagestream :
                _imageStreamList.push_back(imagestream) 
                s_imageStream = imagestream
        
        _imageStreamList = ImageStreamList()
    
        operator = ( FindImageStreamsVisitor)  return *this 
    


    _playToggle = bool()
    _trackMouse = bool()
    _imageStreamList = ImageStreamList()
    _imageStreamPlayBackSpeedList = ImageStreamPlayBackSpeedList()
    




void MovieEventHandler.set(osg.Node* node)
    _imageStreamList.clear()
    if node :
        fisv = FindImageStreamsVisitor(_imageStreamList)
        node.accept(fisv)
    _imageStreamPlayBackSpeedList.resize(_imageStreamList.size())


bool MovieEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa, osg.Object*, osg.NodeVisitor* nv)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.FRAME):
                t = ea.getTime()
                printed = bool(False)
                
                fps_itr = _imageStreamPlayBackSpeedList.begin()
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr, ++fps_itr)
                    if *itr :.getStatus()==osg.ImageStream.PLAYING :  ((*itr).data() != (*fps_itr).lastData) :
                        data = ImageStreamPlaybackSpeedData(*fps_itr)
                        dt = (data.timeStamp > 0) ? t - data.timeStamp : 1/60.0
                        data.lastData = (*itr).data()
                        data.fps = (*fps_itr).fps * 0.8 + 0.2 * (1/dt)
                        data.timeStamp = t
                        
                        if t-data.lastOutput > 1 :
                            print data.fps, " "
                            data.lastOutput = t
                            printed = True
                        
                if printed : 
                    print std.endl
            break
        case(osgGA.GUIEventAdapter.MOVE):
                if _trackMouse :
                    for(ImageStreamList.iterator itr=_imageStreamList.begin()
                        itr!=_imageStreamList.end()
                        ++itr)
                        dt = (*itr).getLength() * ((1.0+ea.getXnormalized()) / 2.0)
                        (*itr).seek(dt)
                        print "seeking to ", dt, " length: ", (*itr).getLength()
                return False
            
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()=='p' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    if *itr :.getStatus()==osg.ImageStream.PLAYING :
                        # playing, so pause
                        print "Pause"
                        (*itr).pause()
                    else :
                        # playing, so pause
                        print "Play"
                        (*itr).play()
                return True
            elif ea.getKey()=='r' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    print "Restart"
                    (*itr).rewind()
                return True
            elif ea.getKey()=='L' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    if *itr :.getLoopingMode() == osg.ImageStream.LOOPING :
                        print "Toggle Looping Off"
                        (*itr).setLoopingMode( osg.ImageStream.NO_LOOPING )
                    else :
                        print "Toggle Looping On"
                        (*itr).setLoopingMode( osg.ImageStream.LOOPING )
                return True
            elif ea.getKey() == 'i' : 
                setTrackMouse(!_trackMouse)
                
                
            return False

        default:
            return False

    return False

void MovieEventHandler.getUsage(osg.ApplicationUsage usage) 
    usage.addKeyboardMouseBinding("i","toggle interactive mode, scrub via mouse-move")
    usage.addKeyboardMouseBinding("p","Play/Pause movie")
    usage.addKeyboardMouseBinding("r","Restart movie")
    usage.addKeyboardMouseBinding("l","Toggle looping of movie")




def main(argc, argv):




    
    arguments = osg.ArgumentParser(argc,argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    filename = str()
    arguments.read("-o",filename)

    # create a model from the images and pass it to the viewer.
    viewer.setSceneData(createModel(arguments))

    # pass the model to the MovieEventHandler so it can pick out ImageStream's to manipulate.
    meh = MovieEventHandler()
    meh.set( viewer.getSceneData() )

    if arguments.read("--track-mouse") : meh.setTrackMouse(True)
    
    viewer.addEventHandler( meh )

    viewer.addEventHandler( osgViewer.StatsHandler())

    if !filename.empty() :
        osgDB.writeNodeFile(*viewer.getSceneData(),filename)

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
