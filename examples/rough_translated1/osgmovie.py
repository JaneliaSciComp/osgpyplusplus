#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgmovie"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer


# Translated from file 'osgmovie.cpp'

# OpenSceneGraph example, osgmovie.
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

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgDB/ReadFile>

#include <osg/Geode>
#include <osg/Geometry>
#include <osg/StateSet>
#include <osg/Material>
#include <osg/Texture2D>
#include <osg/TextureRectangle>
#include <osg/TextureCubeMap>
#include <osg/TexMat>
#include <osg/CullFace>
#include <osg/ImageStream>
#include <osg/io_utils>

#include <osgGA/TrackballManipulator>
#include <osgGA/StateSetManipulator>
#include <osgGA/EventVisitor>

#include <iostream>

class MovieEventHandler (osgGA.GUIEventHandler) :

    MovieEventHandler():_trackMouse(False) 

    def setMouseTracking(track):

         _trackMouse = track 
    def getMouseTracking():
         return _trackMouse 

    set = void(osg.Node* node)

    handle = virtual bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa, osg.Object*, osg.NodeVisitor* nv)

    virtual void getUsage(osg.ApplicationUsage usage) 

    typedef std.vector< osg.observer_ptr<osg.ImageStream> > ImageStreamList

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
            if  not stateset : return

            attr = stateset.getTextureAttribute(0,osg.StateAttribute.TEXTURE)
            if attr :
                texture2D = dynamic_cast<osg.Texture2D*>(attr)
                if texture2D : apply(dynamic_cast<osg.ImageStream*>(texture2D.getImage()))

                textureRec = dynamic_cast<osg.TextureRectangle*>(attr)
                if textureRec : apply(dynamic_cast<osg.ImageStream*>(textureRec.getImage()))

        inline void apply(osg.ImageStream* imagestream)
            if imagestream :
                _imageStreamList.push_back(imagestream)

        _imageStreamList = ImageStreamList()

        operator = ( FindImageStreamsVisitor)  return *this 

    


    _trackMouse = bool()
    _imageStreamList = ImageStreamList()
    _seekIncr = unsigned int()





void MovieEventHandler.set(osg.Node* node)
    _imageStreamList.clear()
    if node :
        fisv = FindImageStreamsVisitor(_imageStreamList)
        node.accept(fisv)


bool MovieEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa, osg.Object*, osg.NodeVisitor* nv)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.MOVE):
        case(osgGA.GUIEventAdapter.PUSH):
        case(osgGA.GUIEventAdapter.RELEASE):
            if _trackMouse :
                view = dynamic_cast<osgViewer.View*>(aa)
                intersections = osgUtil.LineSegmentIntersector.Intersections()
                foundIntersection =  False if (view==0) else 
                     view.computeIntersections(ea, intersections) if ((nv==0) else 
                             view.computeIntersections(ea, nv.getNodePath(), intersections))

                if foundIntersection :

                    # use the nearest intersection
                    intersection = *(intersections.begin())
                    drawable = intersection.drawable
                    geometry =  drawable.asGeometry() if (drawable) else  0
                    vertices =  dynamic_cast<osg.Vec3Array*>(geometry.getVertexArray()) if (geometry) else  0
                    if vertices :
                        # get the vertex indices.
                        indices = intersection.indexList
                        ratios = intersection.ratioList

                        if indices.size()==3  and  ratios.size()==3 :
                            i1 = indices[0]
                            i2 = indices[1]
                            i3 = indices[2]

                            r1 = ratios[0]
                            r2 = ratios[1]
                            r3 = ratios[2]

                            texcoords =  geometry.getTexCoordArray(0) if ((geometry.getNumTexCoordArrays()>0)) else  0
                            texcoords_Vec2Array = dynamic_cast<osg.Vec2Array*>(texcoords)
                            if texcoords_Vec2Array :
                                # we have tex coord array so now we can compute the final tex coord at the point of intersection.
                                tc1 = (*texcoords_Vec2Array)[i1]
                                tc2 = (*texcoords_Vec2Array)[i2]
                                tc3 = (*texcoords_Vec2Array)[i3]
                                tc = tc1*r1 + tc2*r2 + tc3*r3

                                osg.notify(osg.NOTICE), "We hit tex coords ", tc

                        else:
                            osg.notify(osg.NOTICE), "Intersection has insufficient indices to work with"

                else:
                    osg.notify(osg.NOTICE), "No intersection"
            break
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()==ord("p") :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    not = _imageStreamList.end()
                    ++itr)
                    playToggle = (*itr).getStatus()
                    if playToggle  not = osg.ImageStream.PLAYING :
                        print (*itr), " Play"
                        (*itr).play()
                    else:
                        # playing, so pause
                        print (*itr), " Pause"
                        (*itr).pause()
                return True
            elif ea.getKey()==ord("r") :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    not = _imageStreamList.end()
                    ++itr)
                    print (*itr), " Restart"
                    (*itr).rewind()
                    (*itr).play()
                return True
            elif ea.getKey()==ord(">") :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    not = _imageStreamList.end()
                    ++itr)
                    print "Seeking"
                    if _seekIncr > 3 : _seekIncr = 0
                    length = (*itr).getLength()
                    t_pos = (length/4.0)*_seekIncr
                    #(*itr).rewind()
                    (*itr).seek(t_pos)
                    (*itr).play()
                    _seekIncr++
                return True
            elif ea.getKey()==ord("L") :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    not = _imageStreamList.end()
                    ++itr)
                    if *itr :.getLoopingMode() == osg.ImageStream.LOOPING :
                        print (*itr), " Toggle Looping Off"
                        (*itr).setLoopingMode( osg.ImageStream.NO_LOOPING )
                    else:
                        print (*itr), " Toggle Looping On"
                        (*itr).setLoopingMode( osg.ImageStream.LOOPING )
                return True
            elif ea.getKey()==ord("+") :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    not = _imageStreamList.end()
                    ++itr)
                    tm = (*itr).getTimeMultiplier()
                    tm += 0.1
                    (*itr).setTimeMultiplier(tm)
                    print (*itr), " Increase speed rate ", (*itr).getTimeMultiplier()
                return True
            elif ea.getKey()==ord("-") :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    not = _imageStreamList.end()
                    ++itr)
                    tm = (*itr).getTimeMultiplier()
                    tm -= 0.1
                    (*itr).setTimeMultiplier(tm)
                    print (*itr), " Decrease speed rate ", (*itr).getTimeMultiplier()
                return True
            elif ea.getKey()==ord("o") :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    not = _imageStreamList.end()
                    ++itr)
                    print (*itr), " Frame rate  ", (*itr).getFrameRate()
                return True
            return False

        default:
            return False
    return False

void MovieEventHandler.getUsage(osg.ApplicationUsage usage) 
    usage.addKeyboardMouseBinding("p","Play/Pause movie")
    usage.addKeyboardMouseBinding("r","Restart movie")
    usage.addKeyboardMouseBinding("l","Toggle looping of movie")
    usage.addKeyboardMouseBinding("+","Increase speed of movie")
    usage.addKeyboardMouseBinding("-","Decrease speed of movie")
    usage.addKeyboardMouseBinding("o","Display frame rate of movie")
    usage.addKeyboardMouseBinding(">","Advance the movie using seek")


def myCreateTexturedQuadGeometry(pos, width, height, image, useTextureRectangle, xyPlane, option_flip):


    
    flip = image.getOrigin()==osg.Image.TOP_LEFT
    if option_flip : flip =  not flip

    if useTextureRectangle :
        pictureQuad = osg.createTexturedQuadGeometry(pos,
                                           osg.Vec3(width,0.0,0.0),
                                            osg.Vec3(0.0,height,0.0) : osg: if (xyPlane) else Vec3(0.0,0.0,height),
                                           0.0,  image.t() : 0.0, image.s(), flip ? 0.0 if (flip) else  image.t())

        texture = osg.TextureRectangle(image)
        texture.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_EDGE)
        texture.setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_EDGE)


        pictureQuad.getOrCreateStateSet().setTextureAttributeAndModes(0,
                                                                        texture,
                                                                        osg.StateAttribute.ON)

        return pictureQuad
    else:
        pictureQuad = osg.createTexturedQuadGeometry(pos,
                                           osg.Vec3(width,0.0,0.0),
                                            osg.Vec3(0.0,height,0.0) : osg: if (xyPlane) else Vec3(0.0,0.0,height),
                                           0.0,  1.0 : 0.0 , 1.0, flip ? 0.0 if (flip) else  1.0)

        texture = osg.Texture2D(image)
        texture.setResizeNonPowerOfTwoHint(False)
        texture.setFilter(osg.Texture.MIN_FILTER,osg.Texture.LINEAR)
        texture.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_EDGE)
        texture.setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_EDGE)


        pictureQuad.getOrCreateStateSet().setTextureAttributeAndModes(0,
                    texture,
                    osg.StateAttribute.ON)

        return pictureQuad

#if USE_SDL

class SDLAudioSink (osg.AudioSink) :

        SDLAudioSink(osg.AudioStream* audioStream):
            _started(False),
            _paused(False),
            _audioStream(audioStream) 

        ~SDLAudioSink()

        play = virtual void()
        pause = virtual void()
        stop = virtual void()

        def playing():

             return _started  and   not _paused 


        _started = bool()
        _paused = bool()
        _audioStream = osg.observer_ptr<osg.AudioStream>()


#endif

def main(argv):

    
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" example demonstrates the use of ImageStream for rendering movies as textures.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--texture2D","Use Texture2D rather than TextureRectangle.")
    arguments.getApplicationUsage().addCommandLineOption("--shader","Use shaders to post process the video.")
    arguments.getApplicationUsage().addCommandLineOption("--interactive","Use camera manipulator to allow movement around movie.")
    arguments.getApplicationUsage().addCommandLineOption("--flip","Flip the movie so top becomes bottom.")
#if defined(WIN32)  or  defined(__APPLE__)
    arguments.getApplicationUsage().addCommandLineOption("--devices","Print the Video input capability via QuickTime and exit.")
#endif

    useTextureRectangle = True
    useShader = False

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

#if defined(WIN32)  or  defined(__APPLE__)
    # if user requests devices video capability.
    if arguments.read("-devices")  or  arguments.read("--devices") :
        # Force load QuickTime plugin, probe video capability, exit
        osgDB.readImageFile("devices.live")
        return 1
#endif

    while arguments.read("--texture2D") : useTextureRectangle=False
    while arguments.read("--shader") : useShader=True

    mouseTracking = False
    while arguments.read("--mouse") : mouseTracking=True


    # if user request help write it out to cout.
    if arguments.read("-h")  or  arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    fullscreen = not arguments.read("--interactive")
    flip = arguments.read("--flip")

    geode = osg.Geode()

    stateset = geode.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

    if useShader :
        #useTextureRectangle = False

        static  char *shaderSourceTextureRec = 
            "uniform vec4 cutoff_color\n"
            "uniform samplerRect movie_texture\n"
            "void main(void)\n"
            "\n"
            "    vec4 texture_color = textureRect(movie_texture, gl_TexCoord[0].st) \n"
            "    if all(lessThanEqual(texture_color,cutoff_color)) : discard \n"
            "    gl_FragColor = texture_color\n"
            "\n"
        

        static  char *shaderSourceTexture2D = 
            "uniform vec4 cutoff_color\n"
            "uniform sampler2D movie_texture\n"
            "void main(void)\n"
            "\n"
            "    vec4 texture_color = texture2D(movie_texture, gl_TexCoord[0].st) \n"
            "    if all(lessThanEqual(texture_color,cutoff_color)) : discard \n"
            "    gl_FragColor = texture_color\n"
            "\n"
        

        program = osg.Program()

        program.addShader(osg.Shader(osg.Shader.FRAGMENT,
                                            shaderSourceTextureRec if (useTextureRectangle) else  shaderSourceTexture2D))

        stateset.addUniform(osg.Uniform("cutoff_color",osg.Vec4(0.1,0.1,0.1,1.0)))
        stateset.addUniform(osg.Uniform("movie_texture",0))

        stateset.setAttribute(program)


    pos = osg.Vec3(0.0,0.0,0.0)
    topleft = pos
    bottomright = pos

    xyPlane = fullscreen
    
    useAudioSink = False
    while arguments.read("--audio") :  useAudioSink = True 
    
#if USE_SDL
    numAudioStreamsEnabled = 0
#endif

    for(int i=1i<arguments.argc()++i)
        if arguments.isString(i) :
            image = osgDB.readImageFile(arguments[i])
            imagestream = dynamic_cast<osg.ImageStream*>(image)
            if imagestream : 
                audioStreams = imagestream.getAudioStreams()
                if useAudioSink  and   not audioStreams.empty() :
                    audioStream = audioStreams[0]
                    osg.notify(osg.NOTICE), "AudioStream read [", audioStream.getName(), "]"
#if USE_SDL
                    if numAudioStreamsEnabled==0 :
                        audioStream.setAudioSink(SDLAudioSink(audioStream))
                        
                        ++numAudioStreamsEnabled
#endif


                imagestream.play()

            if image :
                osg.notify(osg.NOTICE), "image.s()", image.s(), " image-t()=", image.t(), " aspectRatio=", image.getPixelAspectRatio()

                width = image.s() * image.getPixelAspectRatio()
                height = image.t()

                drawable = myCreateTexturedQuadGeometry(pos, width, height,image, useTextureRectangle, xyPlane, flip)
                
                if image.isImageTranslucent() :
                    osg.notify(osg.NOTICE), "Transparent movie, enabling blending."

                    drawable.getOrCreateStateSet().setMode(GL_BLEND, osg.StateAttribute.ON)
                    drawable.getOrCreateStateSet().setRenderingHint(osg.StateSet.TRANSPARENT_BIN)

                geode.addDrawable(drawable)

                bottomright = pos + osg.Vec3(width,height,0.0)

                if xyPlane : pos.y() += height*1.05
                else pos.z() += height*1.05
            else:
                print "Unable to read file ", arguments[i]

    # set the scene to render
    viewer.setSceneData(geode)

    if viewer.getSceneData()==0 :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # pass the model to the MovieEventHandler so it can pick out ImageStream's to manipulate.
    meh = MovieEventHandler()
    meh.setMouseTracking( mouseTracking )
    meh.set( viewer.getSceneData() )
    viewer.addEventHandler( meh )

    viewer.addEventHandler( osgViewer.StatsHandler )()
    viewer.addEventHandler( osgGA.StateSetManipulator( viewer.getCamera().getOrCreateStateSet() ) )
    viewer.addEventHandler( osgViewer.WindowSizeHandler )()

    # add the record camera path handler
    viewer.addEventHandler(osgViewer.RecordCameraPathHandler)()

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    if fullscreen :
        viewer.realize()
        
        viewer.getCamera().setClearColor(osg.Vec4(0.0,0.0,0.0,1.0))

        screenAspectRatio = 1280.0/1024.0

        wsi = osg.GraphicsContext.getWindowingSystemInterface()
        if wsi : 
            unsigned int width, height
            wsi.getScreenResolution(osg.GraphicsContext.ScreenIdentifier(0), width, height)
            
            screenAspectRatio = float(width) / float(height)
        
        modelAspectRatio = (bottomright.x()-topleft.x())/(bottomright.y()-topleft.y())
        
        viewer.getCamera().setViewMatrix(osg.Matrix.identity())


        center = (bottomright + topleft)*0.5
        dx = osg.Vec3(bottomright.x()-center.x(), 0.0, 0.0)
        dy = osg.Vec3(0.0, topleft.y()-center.y(), 0.0)

        ratio = modelAspectRatio/screenAspectRatio

        if ratio>1.0 :
            # use model width as the control on model size.
            bottomright = center + dx - dy * ratio
            topleft = center - dx + dy * ratio
        else:
            # use model height as the control on model size.
            bottomright = center + dx / ratio - dy
            topleft = center - dx / ratio + dy

        viewer.getCamera().setProjectionMatrixAsOrtho2D(topleft.x(),bottomright.x(),topleft.y(),bottomright.y())

        while  not viewer.done() :
            viewer.frame()
        return 0
    else:
        # create the windows and run the threads.
        return viewer.run()

#if USE_SDL

#include "SDL.h"

static void soundReadCallback(void * user_data, uint8_t * data, int datalen)
    sink = reinterpret_cast<SDLAudioSink*>(user_data)
    as = sink._audioStream
    if as.valid() :
        as.consumeAudioBuffer(data, datalen)

SDLAudioSink.~SDLAudioSink()
    stop()

void SDLAudioSink.play()
    if _started :
        if _paused :
            SDL_PauseAudio(0)
            _paused = False
        return

    _started = True
    _paused = False

    osg.notify(osg.NOTICE), "SDLAudioSink().startPlaying()"

    osg.notify(osg.NOTICE), "  audioFrequency()=", _audioStream.audioFrequency()
    osg.notify(osg.NOTICE), "  audioNbChannels()=", _audioStream.audioNbChannels()
    osg.notify(osg.NOTICE), "  audioSampleFormat()=", _audioStream.audioSampleFormat()

    specs =  0 
    wanted_specs =  0 

    wanted_specs.freq = _audioStream.audioFrequency()
    wanted_specs.format = AUDIO_S16SYS
    wanted_specs.channels = _audioStream.audioNbChannels()
    wanted_specs.silence = 0
    wanted_specs.samples = 1024
    wanted_specs.callback = soundReadCallback
    wanted_specs.userdata = this

    if SDL_OpenAudio(wanted_specs, specs) < 0 :
        throw "SDL_OpenAudio() failed (" + str(SDL_GetError()) + ")"

    SDL_PauseAudio(0)


void SDLAudioSink.pause()
    if _started :
        SDL_PauseAudio(1)
        _paused = True

void SDLAudioSink.stop()
    if _started :
        if  not _paused : SDL_PauseAudio(1)
        SDL_CloseAudio()

        osg.notify(osg.NOTICE), "~SDLAudioSink() destructor, but still playing"

#endif



if __name__ == "__main__":
    main(sys.argv)
