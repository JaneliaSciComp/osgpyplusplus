#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgtexture2D"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osgtexture2D.cpp'

# OpenSceneGraph example, osgtexture2D.
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
#include <osg/MatrixTransform>
#include <osg/Texture2D>
#include <osg/DrawPixels>
#include <osg/PolygonOffset>
#include <osg/Geode>

#include <osgDB/Registry>
#include <osgDB/ReadFile>

#include <osgText/Text>

#include <osgViewer/Viewer>

#####################################################################/
#
# filter wall and animation callback.
#

class FilterCallback (osg.NodeCallback) :

    FilterCallback(osg.Texture2D* texture,osgText.Text* text,double delay=1.0):
        _texture(texture),
        _text(text),
        _delay(delay),
        _currPos(0),
        _prevTime(0.0)
        # start with a mip mapped mode to ensure that
        _minFilterList.push_back(osg.Texture2D.LINEAR_MIPMAP_LINEAR)
        _magFilterList.push_back(osg.Texture2D.LINEAR)
        _textList.push_back("Tri-linear mip mapping (default filtering)\nsetFilter(MIN_FILTER,LINEAR_MIP_LINEAR)\nsetFilter(MAG_FILTER,LINEAR)")

        _minFilterList.push_back(osg.Texture2D.NEAREST)
        _magFilterList.push_back(osg.Texture2D.NEAREST)
        _textList.push_back("Nearest filtering\nsetFilter(MIN_FILTER,NEAREST)\nsetFilter(MAG_FILTER,NEAREST)")

        _minFilterList.push_back(osg.Texture2D.LINEAR)
        _magFilterList.push_back(osg.Texture2D.LINEAR)
        _textList.push_back("Linear filtering\nsetFilter(MIN_FILTER,LINEAR)\nsetFilter(MAG_FILTER,LINEAR)")

        _minFilterList.push_back(osg.Texture2D.NEAREST_MIPMAP_NEAREST)
        _magFilterList.push_back(osg.Texture2D.LINEAR)
        _textList.push_back("nearest mip mapping (default filtering)\nsetFilter(MIN_FILTER,)\nsetFilter(MAG_FILTER,LINEAR)")

        _minFilterList.push_back(osg.Texture2D.LINEAR_MIPMAP_NEAREST)
        _magFilterList.push_back(osg.Texture2D.LINEAR)
        _textList.push_back("bi-linear mip mapping\nsetFilter(MIN_FILTER,LINEAR_MIPMAP_NEAREST)\nsetFilter(MAG_FILTER,LINEAR)")

        _minFilterList.push_back(osg.Texture2D.NEAREST_MIPMAP_LINEAR)
        _magFilterList.push_back(osg.Texture2D.LINEAR)
        _textList.push_back("bi-linear mip mapping\nsetFilter(MIN_FILTER,NEAREST_MIPMAP_LINEAR)\nsetFilter(MAG_FILTER,LINEAR)")


        setValues()

    virtual void operator()(osg.Node*, osg.NodeVisitor* nv)
        if nv.getFrameStamp() :
            currTime = nv.getFrameStamp().getSimulationTime()
            if currTime-_prevTime>_delay :
                # update filter modes and text.
                setValues()

                # advance the current positon, wrap round if required.
                _currPos++
                if _currPos>=_minFilterList.size() : _currPos=0

                # record time
                _prevTime = currTime

    def setValues():

        
        _texture.setFilter(osg.Texture2D.MIN_FILTER,_minFilterList[_currPos])
        _texture.setFilter(osg.Texture2D.MAG_FILTER,_magFilterList[_currPos])

        _text.setText(_textList[_currPos])

    typedef std.vector<osg.Texture2D.FilterMode> FilterList
    typedef std.vector<str>                TextList

    _texture = osg.Texture2D()
    _text = osgText.Text()
    _delay = double()

    _minFilterList = FilterList()
    _magFilterList = FilterList()
    _textList = TextList()

    _currPos = unsigned int()
    _prevTime = double()



def createFilterWall(bb, filename):

    
    group = osg.Group()

    # left hand side of bounding box.
    top_left = osg.Vec3(bb.xMin(),bb.yMin(),bb.zMax())
    bottom_left = osg.Vec3(bb.xMin(),bb.yMin(),bb.zMin())
    bottom_right = osg.Vec3(bb.xMin(),bb.yMax(),bb.zMin())
    top_right = osg.Vec3(bb.xMin(),bb.yMax(),bb.zMax())
    center = osg.Vec3(bb.xMin(),(bb.yMin()+bb.yMax())*0.5,(bb.zMin()+bb.zMax())*0.5)
    height = bb.zMax()-bb.zMin()

    # create the geometry for the wall.
    geom = osg.Geometry()

    vertices = osg.Vec3Array(4)
    (*vertices)[0] = top_left
    (*vertices)[1] = bottom_left
    (*vertices)[2] = bottom_right
    (*vertices)[3] = top_right
    geom.setVertexArray(vertices)

    texcoords = osg.Vec2Array(4)
    (*texcoords)[0].set(0.0,1.0)
    (*texcoords)[1].set(0.0,0.0)
    (*texcoords)[2].set(1.0,0.0)
    (*texcoords)[3].set(1.0,1.0)
    geom.setTexCoordArray(0,texcoords)

    normals = osg.Vec3Array(1)
    (*normals)[0].set(1.0,0.0,0.0)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

    colors = osg.Vec4Array(1)
    (*colors)[0].set(1.0,1.0,1.0,1.0)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(osg.DrawArrays(GL_QUADS,0,4))

    geom_geode = osg.Geode()
    geom_geode.addDrawable(geom)
    group.addChild(geom_geode)


    # set up the texture state.
    texture = osg.Texture2D()
    texture.setDataVariance(osg.Object.DYNAMIC) # protect from being optimized away as static state.
    texture.setImage(osgDB.readImageFile(filename))

    stateset = geom.getOrCreateStateSet()
    stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

    # create the text label.

    text = osgText.Text()
    text.setDataVariance(osg.Object.DYNAMIC)

    text.setFont("fonts/arial.ttf")
    text.setPosition(center)
    text.setCharacterSize(height*0.03)
    text.setAlignment(osgText.Text.CENTER_CENTER)
    text.setAxisAlignment(osgText.Text.YZ_PLANE)

    text_geode = osg.Geode()
    text_geode.addDrawable(text)

    text_stateset = text_geode.getOrCreateStateSet()
    text_stateset.setAttributeAndModes(osg.PolygonOffset(-1.0,-1.0),osg.StateAttribute.ON)

    group.addChild(text_geode)

    # set the update callback to cycle through the various min and mag filter modes.
    group.setUpdateCallback(FilterCallback(texture,text))

    return group


#####################################################################/
#
# anisotropic wall and animation callback.
#

class AnisotropicCallback (osg.NodeCallback) :

    AnisotropicCallback(osg.Texture2D* texture,osgText.Text* text,double delay=1.0):
        _texture(texture),
        _text(text),
        _delay(delay),
        _currPos(0),
        _prevTime(0.0)

        _maxAnisotropyList.push_back(1.0)
        _textList.push_back("No anisotropic filtering (default)\nsetMaxAnisotropy(1.0)")

        _maxAnisotropyList.push_back(2.0)
        _textList.push_back("Anisotropic filtering\nsetMaxAnisotropy(2.0)")

        _maxAnisotropyList.push_back(4.0)
        _textList.push_back("Anisotropic filtering\nsetMaxAnisotropy(4.0)")

        _maxAnisotropyList.push_back(8.0)
        _textList.push_back("Anisotropic filtering\nsetMaxAnisotropy(8.0)")

        _maxAnisotropyList.push_back(16.0)
        _textList.push_back("Higest quality anisotropic filtering\nsetMaxAnisotropy(16.0)")

        setValues()

    virtual void operator()(osg.Node*, osg.NodeVisitor* nv)
        if nv.getFrameStamp() :
            currTime = nv.getFrameStamp().getSimulationTime()
            if currTime-_prevTime>_delay :
                # update filter modes and text.
                setValues()

                # advance the current positon, wrap round if required.
                _currPos++
                if _currPos>=_maxAnisotropyList.size() : _currPos=0

                # record time
                _prevTime = currTime

    def setValues():

        
        _texture.setMaxAnisotropy(_maxAnisotropyList[_currPos])

        _text.setText(_textList[_currPos])

    typedef std.vector<float>          AnisotropyList
    typedef std.vector<str>    TextList

    _texture = osg.Texture2D()
    _text = osgText.Text()
    _delay = double()

    _maxAnisotropyList = AnisotropyList()
    _textList = TextList()

    _currPos = unsigned int()
    _prevTime = double()



def createAnisotripicWall(bb, filename):

    
    group = osg.Group()

    # left hand side of bounding box.
    top_left = osg.Vec3(bb.xMin(),bb.yMax(),bb.zMin())
    bottom_left = osg.Vec3(bb.xMin(),bb.yMin(),bb.zMin())
    bottom_right = osg.Vec3(bb.xMax(),bb.yMin(),bb.zMin())
    top_right = osg.Vec3(bb.xMax(),bb.yMax(),bb.zMin())
    center = osg.Vec3((bb.xMin()+bb.xMax())*0.5,(bb.yMin()+bb.yMax())*0.5,bb.zMin())
    height = bb.yMax()-bb.yMin()

    # create the geometry for the wall.
    geom = osg.Geometry()

    vertices = osg.Vec3Array(4)
    (*vertices)[0] = top_left
    (*vertices)[1] = bottom_left
    (*vertices)[2] = bottom_right
    (*vertices)[3] = top_right
    geom.setVertexArray(vertices)

    texcoords = osg.Vec2Array(4)
    (*texcoords)[0].set(0.0,1.0)
    (*texcoords)[1].set(0.0,0.0)
    (*texcoords)[2].set(1.0,0.0)
    (*texcoords)[3].set(1.0,1.0)
    geom.setTexCoordArray(0,texcoords)

    normals = osg.Vec3Array(1)
    (*normals)[0].set(0.0,0.0,1.0)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

    colors = osg.Vec4Array(1)
    (*colors)[0].set(1.0,1.0,1.0,1.0)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(osg.DrawArrays(GL_QUADS,0,4))

    geom_geode = osg.Geode()
    geom_geode.addDrawable(geom)
    group.addChild(geom_geode)


    # set up the texture state.
    texture = osg.Texture2D()
    texture.setDataVariance(osg.Object.DYNAMIC) # protect from being optimized away as static state.
    texture.setImage(osgDB.readImageFile(filename))

    stateset = geom.getOrCreateStateSet()
    stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

    # create the text label.

    text = osgText.Text()
    text.setDataVariance(osg.Object.DYNAMIC)
    text.setFont("fonts/arial.ttf")
    text.setPosition(center)
    text.setCharacterSize(height*0.03)
    text.setColor(osg.Vec4(1.0,0.0,1.0,1.0))
    text.setAlignment(osgText.Text.CENTER_CENTER)
    text.setAxisAlignment(osgText.Text.XY_PLANE)

    text_geode = osg.Geode()
    text_geode.addDrawable(text)

    text_stateset = text_geode.getOrCreateStateSet()
    text_stateset.setAttributeAndModes(osg.PolygonOffset(-1.0,-1.0),osg.StateAttribute.ON)

    group.addChild(text_geode)

    # set the update callback to cycle through the various min and mag filter modes.
    group.setUpdateCallback(AnisotropicCallback(texture,text))

    return group


#####################################################################/
#
# wrap wall and animation callback.
#
class WrapCallback (osg.NodeCallback) :

    WrapCallback(osg.Texture2D* texture,osgText.Text* text,double delay=1.0):
        _texture(texture),
        _text(text),
        _delay(delay),
        _currPos(0),
        _prevTime(0.0)

        _wrapList.push_back(osg.Texture2D.CLAMP)
        _textList.push_back("Default tex coord clamp\nsetWrap(WRAP_S,CLAMP)")

        _wrapList.push_back(osg.Texture2D.CLAMP_TO_EDGE)
        _textList.push_back("Clamp to edge extension\nsetWrap(WRAP_S,CLAMP_TO_EDGE)")

        _wrapList.push_back(osg.Texture2D.CLAMP_TO_BORDER)
        _textList.push_back("Clamp to border color extension\nsetWrap(WRAP_S,CLAMP_TO_BORDER)")

        _wrapList.push_back(osg.Texture2D.REPEAT)
        _textList.push_back("Repeat wrap\nsetWrap(WRAP_S,REPEAT)")

        _wrapList.push_back(osg.Texture2D.MIRROR)
        _textList.push_back("Mirror wrap extension\nsetWrap(WRAP_S,MIRROR)")

        setValues()

    virtual void operator()(osg.Node*, osg.NodeVisitor* nv)
        if nv.getFrameStamp() :
            currTime = nv.getFrameStamp().getSimulationTime()
            if currTime-_prevTime>_delay :
                # update filter modes and text.
                setValues()

                # advance the current positon, wrap round if required.
                _currPos++
                if _currPos>=_wrapList.size() : _currPos=0

                # record time
                _prevTime = currTime

    def setValues():

        
        _texture.setWrap(osg.Texture2D.WRAP_S,_wrapList[_currPos])
        _texture.setWrap(osg.Texture2D.WRAP_T,_wrapList[_currPos])

        _text.setText(_textList[_currPos])

    typedef std.vector<osg.Texture2D.WrapMode> WrapList
    typedef std.vector<str>              TextList

    _texture = osg.Texture2D()
    _text = osgText.Text()
    _delay = double()

    _wrapList = WrapList()
    _textList = TextList()

    _currPos = unsigned int()
    _prevTime = double()



def createWrapWall(bb, filename):

    
    group = osg.Group()

    # left hand side of bounding box.
    top_left = osg.Vec3(bb.xMax(),bb.yMax(),bb.zMax())
    bottom_left = osg.Vec3(bb.xMax(),bb.yMax(),bb.zMin())
    bottom_right = osg.Vec3(bb.xMax(),bb.yMin(),bb.zMin())
    top_right = osg.Vec3(bb.xMax(),bb.yMin(),bb.zMax())
    center = osg.Vec3(bb.xMax(),(bb.yMin()+bb.yMax())*0.5,(bb.zMin()+bb.zMax())*0.5)
    height = bb.zMax()-bb.zMin()

    # create the geometry for the wall.
    geom = osg.Geometry()

    vertices = osg.Vec3Array(4)
    (*vertices)[0] = top_left
    (*vertices)[1] = bottom_left
    (*vertices)[2] = bottom_right
    (*vertices)[3] = top_right
    geom.setVertexArray(vertices)

    texcoords = osg.Vec2Array(4)
    (*texcoords)[0].set(-1.0,2.0)
    (*texcoords)[1].set(-1.0,-1.0)
    (*texcoords)[2].set(2.0,-1.0)
    (*texcoords)[3].set(2.0,2.0)
    geom.setTexCoordArray(0,texcoords)

    normals = osg.Vec3Array(1)
    (*normals)[0].set(-1.0,0.0,0.0)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

    colors = osg.Vec4Array(1)
    (*colors)[0].set(1.0,1.0,1.0,1.0)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(osg.DrawArrays(GL_QUADS,0,4))

    geom_geode = osg.Geode()
    geom_geode.addDrawable(geom)
    group.addChild(geom_geode)


    # set up the texture state.
    texture = osg.Texture2D()
    texture.setDataVariance(osg.Object.DYNAMIC) # protect from being optimized away as static state.
    texture.setBorderColor(osg.Vec4(1.0,1.0,1.0,0.5)) # only used when wrap is set to CLAMP_TO_BORDER
    texture.setImage(osgDB.readImageFile(filename))

    stateset = geom.getOrCreateStateSet()
    stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)
    stateset.setMode(GL_BLEND,osg.StateAttribute.ON)
    stateset.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)

    # create the text label.

    text = osgText.Text()
    text.setDataVariance(osg.Object.DYNAMIC)
    text.setFont("fonts/arial.ttf")
    text.setPosition(center)
    text.setCharacterSize(height*0.03)
    text.setAlignment(osgText.Text.CENTER_CENTER)
    text.setAxisAlignment(osgText.Text.YZ_PLANE)

    text_geode = osg.Geode()
    text_geode.addDrawable(text)

    text_stateset = text_geode.getOrCreateStateSet()
    text_stateset.setAttributeAndModes(osg.PolygonOffset(-1.0,-1.0),osg.StateAttribute.ON)

    group.addChild(text_geode)

    # set the update callback to cycle through the various min and mag filter modes.
    group.setUpdateCallback(WrapCallback(texture,text))

    return group


#####################################################################/
#
# sublooad wall and animation callback.
#

class ImageUpdateCallback (osg.NodeCallback) :

    ImageUpdateCallback(osg.Texture2D* texture,osgText.Text* text,double delay=1.0):
        _texture(texture),
        _text(text),
        _delay(delay),
        _currPos(0),
        _prevTime(0.0)

#if 1
        originalImage = osgDB.readImageFile("Images/dog_left_eye.jpg")

        subImage = osg.Image()
        subImage.setUserData(originalImage) # attach the originalImage as user data to prevent it being deleted.

        # now assign the appropriate portion data from the originalImage
        subImage.setImage(originalImage.s()/2, originalImage.t()/2, originalImage.r(), # half the width and height
                           originalImage.getInternalTextureFormat(), # same internal texture format
                           originalImage.getPixelFormat(),originalImage.getDataType(), # same pixel foramt and data type
                           originalImage.data(originalImage.s()/4,originalImage.t()/4), # offset teh start point to 1/4 into the image
                           osg.Image.NO_DELETE, # don't attempt to delete the image data, leave this to the originalImage
                           originalImage.getPacking(), # use the the same packing
                           originalImage.s()) # use the width of the original image as the row width


        subImage.setPixelBufferObject(osg.PixelBufferObject(subImage))

#if 0
        OSG_NOTICE, "orignalImage iterator"
        for(osg.Image.DataIterator itr(originalImage) itr.valid() ++itr)
            OSG_NOTICE, "  ", (void*)itr.data(), ", ", itr.size()

        OSG_NOTICE, "subImage iterator, size ", subImage.s(), ", ", subImage.t()
        i = 0
        for(osg.Image.DataIterator itr(subImage) itr.valid() ++itr, ++i)
            OSG_NOTICE, "  ", i, ", ", (void*)itr.data(), ", ", itr.size()

            for(unsigned char* d=const_cast<unsigned char*>(itr.data()) d<(itr.data()+itr.size()) ++d)
                *d = 255-*d
#endif


        _imageList.push_back(subImage)

#else:
        _imageList.push_back(osgDB.readImageFile("Images/dog_left_eye.jpg"))
#endif
        _textList.push_back("Subloaded Image 1 - dog_left_eye.jpg")

        _imageList.push_back(osgDB.readImageFile("Images/dog_right_eye.jpg"))
        _textList.push_back("Subloaded Image 2 - dog_right_eye.jpg")

        setValues()

    virtual void operator()(osg.Node*, osg.NodeVisitor* nv)
        if nv.getFrameStamp() :
            currTime = nv.getFrameStamp().getSimulationTime()
            if currTime-_prevTime>_delay :
                # update filter modes and text.
                setValues()

                # advance the current positon, wrap round if required.
                _currPos++
                if _currPos>=_imageList.size() : _currPos=0

                # record time
                _prevTime = currTime

    def setValues():

        
        # Note, as long as the images are the same dimensions subloading will be used
        # to update the textures.  If dimensions change then the texture objects have
        # to be deleted and re-recreated.
        #
        # The load/subload happens during the draw traversal so doesn't happen on
        # the setImage which just updates internal pointers and modifed flags.

        _texture.setImage(_imageList[_currPos])

        #_texture.dirtyTextureObject()

        _text.setText(_textList[_currPos])


    typedef std.vector< osg.Image > ImageList
    typedef std.vector<str>                TextList

    _texture = osg.Texture2D()
    _text = osgText.Text()
    _delay = double()

    _imageList = ImageList()
    _textList = TextList()

    _currPos = unsigned int()
    _prevTime = double()



def createSubloadWall(bb):

    
    group = osg.Group()

    # left hand side of bounding box.
    top_left = osg.Vec3(bb.xMin(),bb.yMax(),bb.zMax())
    bottom_left = osg.Vec3(bb.xMin(),bb.yMax(),bb.zMin())
    bottom_right = osg.Vec3(bb.xMax(),bb.yMax(),bb.zMin())
    top_right = osg.Vec3(bb.xMax(),bb.yMax(),bb.zMax())
    center = osg.Vec3((bb.xMax()+bb.xMin())*0.5,bb.yMax(),(bb.zMin()+bb.zMax())*0.5)
    height = bb.zMax()-bb.zMin()

    # create the geometry for the wall.
    geom = osg.Geometry()

    vertices = osg.Vec3Array(4)
    (*vertices)[0] = top_left
    (*vertices)[1] = bottom_left
    (*vertices)[2] = bottom_right
    (*vertices)[3] = top_right
    geom.setVertexArray(vertices)

    texcoords = osg.Vec2Array(4)
    (*texcoords)[0].set(0.0,1.0)
    (*texcoords)[1].set(0.0,0.0)
    (*texcoords)[2].set(1.0,0.0)
    (*texcoords)[3].set(1.0,1.0)
    geom.setTexCoordArray(0,texcoords)

    normals = osg.Vec3Array(1)
    (*normals)[0].set(0.0,-1.0,0.0)
    geom.setNormalArray(normals, osg.Array.BIND_OVERALL)

    colors = osg.Vec4Array(1)
    (*colors)[0].set(1.0,1.0,1.0,1.0)
    geom.setColorArray(colors, osg.Array.BIND_OVERALL)

    geom.addPrimitiveSet(osg.DrawArrays(GL_QUADS,0,4))

    geom_geode = osg.Geode()
    geom_geode.addDrawable(geom)
    group.addChild(geom_geode)


    # set up the texture state.
    texture = osg.Texture2D()
    texture.setDataVariance(osg.Object.DYNAMIC) # protect from being optimized away as static state.
    texture.setFilter(osg.Texture2D.MIN_FILTER,osg.Texture2D.LINEAR)
    texture.setFilter(osg.Texture2D.MAG_FILTER,osg.Texture2D.LINEAR)

    stateset = geom.getOrCreateStateSet()
    stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

    # create the text label.

    text = osgText.Text()
    text.setDataVariance(osg.Object.DYNAMIC)
    text.setFont("fonts/arial.ttf")
    text.setPosition(center)
    text.setCharacterSize(height*0.03)
    text.setAlignment(osgText.Text.CENTER_CENTER)
    text.setAxisAlignment(osgText.Text.XZ_PLANE)

    text_geode = osg.Geode()
    text_geode.addDrawable(text)

    text_stateset = text_geode.getOrCreateStateSet()
    text_stateset.setAttributeAndModes(osg.PolygonOffset(-1.0,-1.0),osg.StateAttribute.ON)

    group.addChild(text_geode)

    # set the update callback to cycle through the various min and mag filter modes.
    group.setUpdateCallback(ImageUpdateCallback(texture,text))

    return group



def createModel():


    

    # create the root node which will hold the model.
    root = osg.Group()

    # turn off lighting
    root.getOrCreateStateSet().setMode(GL_LIGHTING,osg.StateAttribute.OFF)

    bb = osg.BoundingBox(0.0,0.0,0.0,1.0,1.0,1.0)

    root.addChild(createFilterWall(bb,"Images/lz.rgb"))
    root.addChild(createAnisotripicWall(bb,"Images/primitives.gif"))
    root.addChild(createWrapWall(bb,"Images/tree0.rgba"))
    root.addChild(createSubloadWall(bb))

    return root

int main(int , char **)
    # construct the viewer.
    viewer = osgViewer.Viewer()

    # add model to viewer.
    viewer.setSceneData( createModel() )

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
