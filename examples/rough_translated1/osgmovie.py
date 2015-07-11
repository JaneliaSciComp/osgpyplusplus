#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgmovie"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgViewer

# OpenSceneGraph example, osgmovie.
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

class MovieEventHandler : public osgGA.GUIEventHandler
public:

    MovieEventHandler():_trackMouse(false) 

    void setMouseTracking(bool track)  _trackMouse = track 
    bool getMouseTracking()   return _trackMouse 

    set = void(osg.Node* node)

    virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter aa, osg.Object*, osg.NodeVisitor* nv)

    virtual void getUsage(osg.ApplicationUsage usage) 

    typedef std.vector< osg.observer_ptr<osg.ImageStream> > ImageStreamList

protected:

    virtual ~MovieEventHandler() 

    class FindImageStreamsVisitor : public osg.NodeVisitor
    public:
        FindImageStreamsVisitor(ImageStreamList imageStreamList):
            _imageStreamList(imageStreamList) 

        virtual void apply(osg.Geode geode)
            apply(geode.getStateSet())

            for(unsigned int i=0i<geode.getNumDrawables()++i)
                apply(geode.getDrawable(i).getStateSet())

            traverse(geode)

        virtual void apply(osg.Node node)
            apply(node.getStateSet())
            traverse(node)

        inline void apply(osg.StateSet* stateset)
            if !stateset : return

            attr =  stateset.getTextureAttribute(0,osg.StateAttribute.TEXTURE)
            if attr :
                texture2D =  dynamic_cast<osg.Texture2D*>(attr)
                if texture2D : apply(dynamic_cast<osg.ImageStream*>(texture2D.getImage()))

                textureRec =  dynamic_cast<osg.TextureRectangle*>(attr)
                if textureRec : apply(dynamic_cast<osg.ImageStream*>(textureRec.getImage()))

        inline void apply(osg.ImageStream* imagestream)
            if imagestream :
                _imageStreamList.push_back(imagestream)

        _imageStreamList = ImageStreamList()

    protected:

        operator =  ( FindImageStreamsVisitor)  return *this 

    


    _trackMouse = bool()
    _imageStreamList = ImageStreamList()
    unsigned int    _seekIncr





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
                view =  dynamic_cast<osgViewer.View*>(aa)
                intersections = osgUtil.LineSegmentIntersector.Intersections()
                foundIntersection =  view==0 ? false :
                    (nv==0 ? view.computeIntersections(ea, intersections) :
                             view.computeIntersections(ea, nv.getNodePath(), intersections))

                if foundIntersection :

                    # use the nearest intersection
                    intersection =  *(intersections.begin())
                    drawable =  intersection.drawable.get()
                    geometry =  drawable ? drawable.asGeometry() : 0
                    vertices =  geometry ? dynamic_cast<osg.Vec3Array*>(geometry.getVertexArray()) : 0
                    if vertices :
                        # get the vertex indices.
                        indices =  intersection.indexList
                        ratios =  intersection.ratioList

                        if indices.size()==3  ratios.size()==3 :
                            unsigned int i1 = indices[0]
                            unsigned int i2 = indices[1]
                            unsigned int i3 = indices[2]

                            r1 =  ratios[0]
                            r2 =  ratios[1]
                            r3 =  ratios[2]

                            texcoords =  (geometry.getNumTexCoordArrays()>0) ? geometry.getTexCoordArray(0) : 0
                            texcoords_Vec2Array =  dynamic_cast<osg.Vec2Array*>(texcoords)
                            if texcoords_Vec2Array :
                                # we have tex coord array so now we can compute the final tex coord at the point of intersection.
                                tc1 =  (*texcoords_Vec2Array)[i1]
                                tc2 =  (*texcoords_Vec2Array)[i2]
                                tc3 =  (*texcoords_Vec2Array)[i3]
                                tc =  tc1*r1 + tc2*r2 + tc3*r3

                                osg.notify(osg.NOTICE), "We hit tex coords ", tc

                        else:
                            osg.notify(osg.NOTICE), "Intersection has insufficient indices to work with"

                else:
                    osg.notify(osg.NOTICE), "No intersection"
            break
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()=='p' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    playToggle =  (*itr).getStatus()
                    if playToggle != osg.ImageStream.PLAYING :
                        print (*itr).get(), " Play"
                        (*itr).play()
                    else:
                        # playing, so pause
                        print (*itr).get(), " Pause"
                        (*itr).pause()
                true = return()
            else: if ea.getKey()=='r' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    print (*itr).get(), " Restart"
                    (*itr).rewind()
                    (*itr).play()
                true = return()
            else: if ea.getKey()=='>' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    print "Seeking"
                    if _seekIncr > 3 : _seekIncr = 0
                    length =  (*itr).getLength()
                    t_pos =  (length/4.0f)*_seekIncr
                    #(*itr).rewind()
                    (*itr).seek(t_pos)
                    (*itr).play()
                    _seekIncr++
                true = return()
            else: if ea.getKey()=='L' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    if *itr :.getLoopingMode() == osg.ImageStream.LOOPING :
                        print (*itr).get(), " Toggle Looping Off"
                        (*itr).setLoopingMode( osg.ImageStream.NO_LOOPING )
                    else:
                        print (*itr).get(), " Toggle Looping On"
                        (*itr).setLoopingMode( osg.ImageStream.LOOPING )
                true = return()
            else: if ea.getKey()=='+' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    tm =  (*itr).getTimeMultiplier()
                    tm += 0.1
                    (*itr).setTimeMultiplier(tm)
                    print (*itr).get(), " Increase speed rate ", (*itr).getTimeMultiplier()
                true = return()
            else: if ea.getKey()=='-' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    tm =  (*itr).getTimeMultiplier()
                    tm -= 0.1
                    (*itr).setTimeMultiplier(tm)
                    print (*itr).get(), " Decrease speed rate ", (*itr).getTimeMultiplier()
                true = return()
            else: if ea.getKey()=='o' :
                for(ImageStreamList.iterator itr=_imageStreamList.begin()
                    itr!=_imageStreamList.end()
                    ++itr)
                    print (*itr).get(), " Frame rate  ", (*itr).getFrameRate()
                true = return()
            false = return()

        default:
            false = return()
    false = return()

void MovieEventHandler.getUsage(osg.ApplicationUsage usage) 
    usage.addKeyboardMouseBinding("p","Play/Pause movie")
    usage.addKeyboardMouseBinding("r","Restart movie")
    usage.addKeyboardMouseBinding("l","Toggle looping of movie")
    usage.addKeyboardMouseBinding("+","Increase speed of movie")
    usage.addKeyboardMouseBinding("-","Decrease speed of movie")
    usage.addKeyboardMouseBinding("o","Display frame rate of movie")
    usage.addKeyboardMouseBinding(">","Advance the movie using seek")


def myCreateTexturedQuadGeometry(pos, width, height, image, useTextureRectangle, xyPlane, option_flip):
    flip =  image.getOrigin()==osg.Image.TOP_LEFT
    if option_flip : flip = !flip

    if useTextureRectangle :
        pictureQuad =  osg.createTexturedQuadGeometry(pos,
                                           osg.Vec3(width,0.0f,0.0f),
                                           xyPlane ? osg.Vec3(0.0f,height,0.0f) : osg.Vec3(0.0f,0.0f,height),
                                           0.0f, flip ? image.t() : 0.0, image.s(), flip ? 0.0 : image.t())

        texture =  new osg.TextureRectangle(image)
        texture.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_EDGE)
        texture.setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_EDGE)


        pictureQuad.getOrCreateStateSet().setTextureAttributeAndModes(0,
                                                                        texture,
                                                                        osg.StateAttribute.ON)

        pictureQuad = return()
    else:
        pictureQuad =  osg.createTexturedQuadGeometry(pos,
                                           osg.Vec3(width,0.0f,0.0f),
                                           xyPlane ? osg.Vec3(0.0f,height,0.0f) : osg.Vec3(0.0f,0.0f,height),
                                           0.0f, flip ? 1.0f : 0.0f , 1.0f, flip ? 0.0f : 1.0f)

        texture =  new osg.Texture2D(image)
        texture.setResizeNonPowerOfTwoHint(false)
        texture.setFilter(osg.Texture.MIN_FILTER,osg.Texture.LINEAR)
        texture.setWrap(osg.Texture.WRAP_S, osg.Texture.CLAMP_TO_EDGE)
        texture.setWrap(osg.Texture.WRAP_T, osg.Texture.CLAMP_TO_EDGE)


        pictureQuad.getOrCreateStateSet().setTextureAttributeAndModes(0,
                    texture,
                    osg.StateAttribute.ON)

        pictureQuad = return()

#if USE_SDL

class SDLAudioSink : public osg.AudioSink
    public:

        SDLAudioSink(osg.AudioStream* audioStream):
            _started(false),
            _paused(false),
            _audioStream(audioStream) 

        ~SDLAudioSink()

        virtual void play()
        virtual void pause()
        virtual void stop()

        virtual bool playing()   return _started  !_paused 


        _started = bool()
        _paused = bool()
        osg.observer_ptr<osg.AudioStream> _audioStream


#endif

def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)

    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" example demonstrates the use of ImageStream for rendering movies as textures.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display this information")
    arguments.getApplicationUsage().addCommandLineOption("--texture2D","Use Texture2D rather than TextureRectangle.")
    arguments.getApplicationUsage().addCommandLineOption("--shader","Use shaders to post process the video.")
    arguments.getApplicationUsage().addCommandLineOption("--interactive","Use camera manipulator to allow movement around movie.")
    arguments.getApplicationUsage().addCommandLineOption("--flip","Flip the movie so top becomes bottom.")
#if defined(WIN32) || defined(__APPLE__)
    arguments.getApplicationUsage().addCommandLineOption("--devices","Print the Video input capability via QuickTime and exit.")
#endif

    useTextureRectangle =  true
    useShader =  false

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    if arguments.argc()<=1 :
        arguments.getApplicationUsage().write(std.cout,osg.ApplicationUsage.COMMAND_LINE_OPTION)
        return 1

#if defined(WIN32) || defined(__APPLE__)
    # if user requests devices video capability.
    if arguments.read("-devices") || arguments.read("--devices") :
        # Force load QuickTime plugin, probe video capability, exit
        osgDB.readImageFile("devices.live")
        return 1
#endif

    while arguments.read("--texture2D") : useTextureRectangle=false
    while arguments.read("--shader") : useShader=true

    mouseTracking =  false
    while arguments.read("--mouse") : mouseTracking=true


    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    fullscreen =  !arguments.read("--interactive")
    flip =  arguments.read("--flip")

    osg.ref_ptr<osg.Geode> geode = new osg.Geode

    stateset =  geode.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

    if useShader :
        #useTextureRectangle = false

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
        

        program =  new osg.Program

        program.addShader(new osg.Shader(osg.Shader.FRAGMENT,
                                           useTextureRectangle ? shaderSourceTextureRec : shaderSourceTexture2D))

        stateset.addUniform(new osg.Uniform("cutoff_color",osg.Vec4(0.1f,0.1f,0.1f,1.0f)))
        stateset.addUniform(new osg.Uniform("movie_texture",0))

        stateset.setAttribute(program)


    pos = osg.Vec3(0.0f,0.0f,0.0f)
    topleft =  pos
    bottomright =  pos

    xyPlane =  fullscreen
    
    useAudioSink =  false
    while arguments.read("--audio") :  useAudioSink = true 
    
#if USE_SDL
    unsigned int numAudioStreamsEnabled = 0
#endif

    for(int i=1i<arguments.argc()++i)
        if arguments.isString(i) :
            image =  osgDB.readImageFile(arguments[i])
            imagestream =  dynamic_cast<osg.ImageStream*>(image)
            if imagestream : 
                audioStreams =  imagestream.getAudioStreams()
                if useAudioSink  !audioStreams.empty() :
                    audioStream =  audioStreams[0].get()
                    osg.notify(osg.NOTICE), "AudioStream read [", audioStream.getName(), "]"
#if USE_SDL
                    if numAudioStreamsEnabled==0 :
                        audioStream.setAudioSink(new SDLAudioSink(audioStream))
                        
                        ++numAudioStreamsEnabled
#endif


                imagestream.play()

            if image :
                osg.notify(osg.NOTICE), "image.s()", image.s(), " image-t()=", image.t(), " aspectRatio=", image.getPixelAspectRatio()

                width =  image.s() * image.getPixelAspectRatio()
                height =  image.t()

                osg.ref_ptr<osg.Drawable> drawable = myCreateTexturedQuadGeometry(pos, width, height,image, useTextureRectangle, xyPlane, flip)
                
                if image.isImageTranslucent() :
                    osg.notify(osg.NOTICE), "Transparent movie, enabling blending."

                    drawable.getOrCreateStateSet().setMode(GL_BLEND, osg.StateAttribute.ON)
                    drawable.getOrCreateStateSet().setRenderingHint(osg.StateSet.TRANSPARENT_BIN)

                geode.addDrawable(drawable.get())

                bottomright = pos + osg.Vec3(width,height,0.0f)

                if xyPlane : pos.y() += height*1.05f
                else: pos.z() += height*1.05f
            else:
                print "Unable to read file ", arguments[i]

    # set the scene to render
    viewer.setSceneData(geode.get())

    if viewer.getSceneData()==0 :
        arguments.getApplicationUsage().write(std.cout)
        return 1

    # pass the model to the MovieEventHandler so it can pick out ImageStream's to manipulate.
    meh =  new MovieEventHandler()
    meh.setMouseTracking( mouseTracking )
    meh.set( viewer.getSceneData() )
    viewer.addEventHandler( meh )

    viewer.addEventHandler( new osgViewer.StatsHandler )
    viewer.addEventHandler( new osgGA.StateSetManipulator( viewer.getCamera().getOrCreateStateSet() ) )
    viewer.addEventHandler( new osgViewer.WindowSizeHandler )

    # add the record camera path handler
    viewer.addEventHandler(new osgViewer.RecordCameraPathHandler)

    # report any errors if they have occurred when parsing the program arguments.
    if arguments.errors() :
        arguments.writeErrorMessages(std.cout)
        return 1

    if fullscreen :
        viewer.realize()
        
        viewer.getCamera().setClearColor(osg.Vec4(0.0f,0.0f,0.0f,1.0f))

        screenAspectRatio =  1280.0f/1024.0f

        wsi =  osg.GraphicsContext.getWindowingSystemInterface()
        if wsi : 
            unsigned int width, height
            wsi.getScreenResolution(osg.GraphicsContext.ScreenIdentifier(0), width, height)
            
            screenAspectRatio = float(width) / float(height)
        
        modelAspectRatio =  (bottomright.x()-topleft.x())/(bottomright.y()-topleft.y())
        
        viewer.getCamera().setViewMatrix(osg.Matrix.identity())


        center =  (bottomright + topleft)*0.5f
        dx = osg.Vec3(bottomright.x()-center.x(), 0.0f, 0.0f)
        dy = osg.Vec3(0.0f, topleft.y()-center.y(), 0.0f)

        ratio =  modelAspectRatio/screenAspectRatio

        if ratio>1.0f :
            # use model width as the control on model size.
            bottomright = center + dx - dy * ratio
            topleft = center - dx + dy * ratio
        else:
            # use model height as the control on model size.
            bottomright = center + dx / ratio - dy
            topleft = center - dx / ratio + dy

        viewer.getCamera().setProjectionMatrixAsOrtho2D(topleft.x(),bottomright.x(),topleft.y(),bottomright.y())

        while !viewer.done() :
            viewer.frame()
        return 0
    else:
        # create the windows and run the threads.
        return viewer.run()

#if USE_SDL

#include "SDL.h"

static void soundReadCallback(void * user_data, uint8_t * data, int datalen)
    sink =  reinterpret_cast<SDLAudioSink*>(user_data)
    osg.ref_ptr<osg.AudioStream> as = sink._audioStream.get()
    if as.valid() :
        as.consumeAudioBuffer(data, datalen)

SDLAudioSink.~SDLAudioSink()
    stop()

void SDLAudioSink.play()
    if _started :
        if _paused :
            SDL_PauseAudio(0)
            _paused = false
        return

    _started = true
    _paused = false

    osg.notify(osg.NOTICE), "SDLAudioSink().startPlaying()"

    osg.notify(osg.NOTICE), "  audioFrequency()=", _audioStream.audioFrequency()
    osg.notify(osg.NOTICE), "  audioNbChannels()=", _audioStream.audioNbChannels()
    osg.notify(osg.NOTICE), "  audioSampleFormat()=", _audioStream.audioSampleFormat()

    specs =   0 
    wanted_specs =   0 

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
        _paused = true

void SDLAudioSink.stop()
    if _started :
        if !_paused : SDL_PauseAudio(1)
        SDL_CloseAudio()

        osg.notify(osg.NOTICE), "~SDLAudioSink() destructor, but still playing"

#endif



if __name__ == "__main__":
    main(sys.argv)
