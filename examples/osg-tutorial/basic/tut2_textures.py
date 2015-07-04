#!/bin/env python

# Translated into python from C++ tutorial at
# http:#trac.openscenegraph.org/projects/osg/wiki/Support/Tutorials/Textures

from osgpypp import osg, osgDB, osgViewer
import sys

# Creating Textured Geometry using StateSets
# Goals

# Add a texture to geometry defined by OpenGL drawing primitives introduced in 
# tutorial Basic geometry.
# Background

# The previous tutorial introduced viewing scenes that include basic shapes 
# created from OpenGL primitives. This section explains how to add textures to 
# these shapes. To make the code easier to use, we'll put the pyramid code 
# into a function that creates a geode and returns a pointer to it. The 
# following code is from tutorial Basic geometry.

def createPyramid():
    pyramidGeode = osg.Geode()
    pyramidGeometry = osg.Geometry()
    pyramidGeode.addDrawable(pyramidGeometry) 

    # Specify the vertices:
    pyramidVertices = osg.Vec3Array()
    pyramidVertices.append( osg.Vec3(0, 0, 0) ) # front left 
    pyramidVertices.append( osg.Vec3(2, 0, 0) ) # front right 
    pyramidVertices.append( osg.Vec3(2, 2, 0) ) # back right 
    pyramidVertices.append( osg.Vec3( 0,2, 0) ) # back left 
    pyramidVertices.append( osg.Vec3( 1, 1,2) ) # peak

    # Associate this set of vertices with the geometry associated with the 
    # geode we added to the scene.
    pyramidGeometry.setVertexArray( pyramidVertices )

    # Create a QUAD primitive for the base by specifying the 
    # vertices from our vertex list that make up this QUAD:
    pyramidBase = osg.DrawElementsUInt(osg.PrimitiveSet.QUADS, 0)
    pyramidBase.append(3)
    pyramidBase.append(2)
    pyramidBase.append(1)
    pyramidBase.append(0)

    # Add this primitive to the geometry: 
    # pyramidGeometry.addPrimitiveSet(pyramidBase)
    # code to create other faces goes here!
    pyramidGeometry.addPrimitiveSet(pyramidBase) 
    # Repeat the same for each of the four sides. Again, vertices are specified in counter-clockwise order. 
    pyramidFaceOne = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
    pyramidFaceOne.append(0)
    pyramidFaceOne.append(1)
    pyramidFaceOne.append(4)
    pyramidGeometry.addPrimitiveSet(pyramidFaceOne)

    pyramidFaceTwo = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
    pyramidFaceTwo.append(1)
    pyramidFaceTwo.append(2)
    pyramidFaceTwo.append(4)
    pyramidGeometry.addPrimitiveSet(pyramidFaceTwo)

    pyramidFaceThree = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
    pyramidFaceThree.append(2)
    pyramidFaceThree.append(3)
    pyramidFaceThree.append(4)
    pyramidGeometry.addPrimitiveSet(pyramidFaceThree)

    pyramidFaceFour = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
    pyramidFaceFour.append(3)
    pyramidFaceFour.append(0)
    pyramidFaceFour.append(4)
    pyramidGeometry.addPrimitiveSet(pyramidFaceFour)

    colors = osg.Vec4Array()
    colors.append(osg.Vec4(1.0, 0.0, 0.0, 1.0) ) #index 0 red
    colors.append(osg.Vec4(0.0, 1.0, 0.0, 1.0) ) #index 1 green
    colors.append(osg.Vec4(0.0, 0.0, 1.0, 1.0) ) #index 2 blue
    colors.append(osg.Vec4(1.0, 1.0, 1.0, 1.0) ) #index 3 white
    colors.append(osg.Vec4(1.0, 0.0, 0.0, 1.0) ) #index 4 red

    pyramidGeometry.setColorArray(colors)
    pyramidGeometry.setColorBinding(osg.Geometry.BIND_PER_VERTEX)

    # Since the mapping from vertices to texture coordinates is 1:1, 
    # we don't need to use an index array to map vertices to texture
    # coordinates. We can do it directly with the 'setTexCoordArray' 
    # method of the Geometry class. 
    # This method takes a variable that is an array of two dimensional
    # vectors (osg.Vec2). This variable needs to have the same
    # number of elements as our Geometry has vertices. Each array element
    # defines the texture coordinate for the cooresponding vertex in the
    # vertex array.
    texcoords = osg.Vec2Array(5)
    texcoords[0].set(0.00,0.0) # tex coord for vertex 0 
    texcoords[1].set(0.25,0.0) # tex coord for vertex 1 
    texcoords[2].set(0.50,0.0) # ""
    texcoords[3].set(0.75,0.0) # "" 
    texcoords[4].set(0.50,1.0) # ""
    pyramidGeometry.setTexCoordArray(0,texcoords)

    return pyramidGeode


# Loading a Texture, Creating a State Set, assigning it to a Node

# The method for rendering primitives is controlled using StateSets. This 
# section of code demonstrates how to load a texture from file, create a 
# StateSet in which this texture is enabled, and assign this StateSet to a 
# node in the scene. The first section starts out the same as previous 
# tutorials. Initialize a viewer and build a scene with a single pyramid.

# Declare a group to act as root node of a scene:
root = osg.Group()
pyramidGeode = createPyramid()
root.addChild(pyramidGeode)

# Now for adding a texture. Here we'll declare a texture instance and set 
# its data variance as 'DYNAMIC'. (If we don't declare the texture as dynamic, 
# some of the osg's optimization routines could remove it.) The texture class 
# encapsulates OpenGL texture modes (wrap, filiter, etc.) as well as an 
# osg.Image. The code below shows how to read an osg.Image instance from a 
# file and associate this image with a texture.

KLN89FaceTexture = osg.Texture2D()

# protect from being optimized away as static state:
KLN89FaceTexture.setDataVariance(osg.Object.DYNAMIC) 

# load an image by reading a file: 
klnFace = osgDB.readImageFile("KLN89FaceB.tga")
if klnFace is None:
    print " Couldn't find texture, quitting."
    sys.exit(-1)

# Assign the texture to the image we read from file: 
KLN89FaceTexture.setImage(klnFace)

# Textures can be associated with rendering StateSets. The next step is to 
# create a StateSet, associate and enable our texture with this state set and 
# assign the StateSet to our geometry.

# Create a StateSet with default settings: 
stateOne = osg.StateSet()

# Assign texture unit 0 of our StateSet to the texture 
# we just created and enable the texture.
stateOne.setTextureAttributeAndModes(0, KLN89FaceTexture, osg.StateAttribute.ON)
# Associate this state set with the Geode that contains
# the pyramid: 
pyramidGeode.setStateSet(stateOne)

# The last step is the simulation loop:

viewer = osgViewer.Viewer()

#The final step is to set up and enter a simulation loop.
viewer.setSceneData( root )

viewer.run()
