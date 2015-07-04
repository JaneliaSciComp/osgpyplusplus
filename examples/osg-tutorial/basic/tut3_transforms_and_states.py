#!/bin/env python

# Translated into python from C++ tutorial at
# http:#trac.openscenegraph.org/projects/osg/wiki/Support/Tutorials/Textures

from osgpypp import osg, osgDB, osgViewer


def createPyramid():
   pyramidGeode = osg.Geode()
   pyramidGeometry = osg.Geometry()
   pyramidGeode.addDrawable(pyramidGeometry) 
   pyramidVertices = osg.Vec3Array()
   pyramidVertices.append( osg.Vec3(0, 0, 0) ) # front left 
   pyramidVertices.append( osg.Vec3(2, 0, 0) ) # front right 
   pyramidVertices.append( osg.Vec3(2, 2, 0) ) # back right 
   pyramidVertices.append( osg.Vec3( 0,2, 0) ) # back left 
   pyramidVertices.append( osg.Vec3( 1, 1,2) ) # peak
   # Associate this set of vertices with the geometry associated with the 
   # geode we added to the scene.
   pyramidGeometry.setVertexArray( pyramidVertices )
   pyramidBase = osg.DrawElementsUInt(osg.PrimitiveSet.QUADS, 3)
   pyramidBase.append(3)
   pyramidBase.append(2)
   pyramidBase.append(1)
   pyramidBase.append(0)
   pyramidGeometry.addPrimitiveSet(pyramidBase)

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

   osg.TemplateIndexArray
      <unsigned int, osg.Array.UIntArrayType,4,4> *colorIndexArray
   colorIndexArray = 
      osg.TemplateIndexArray<unsigned int, osg.Array.UIntArrayType,4,4>
   colorIndexArray.append(0) # vertex 0 assigned color array element 0
   colorIndexArray.append(1) # vertex 1 assigned color array element 1
   colorIndexArray.append(2) # vertex 2 assigned color array element 2
   colorIndexArray.append(3) # vertex 3 assigned color array element 3
   colorIndexArray.append(0) # vertex 4 assigned color array element 0

   pyramidGeometry.setColorArray(colors)
   pyramidGeometry.setColorIndices(colorIndexArray)
   pyramidGeometry.setColorBinding(osg.Geometry.BIND_PER_VERTEX)

   osg.Vec2Array* texcoords = osg.Vec2Array(5)
   (*texcoords)[0].set(0.00,0.0)
   (*texcoords)[1].set(0.25,0.0)
   (*texcoords)[2].set(0.50,0.0)
   (*texcoords)[3].set(0.75,0.0)
   (*texcoords)[4].set(0.50,1.0)

   pyramidGeometry.setTexCoordArray(0,texcoords)
   return pyramidGeode



def main():
   osgViewer.Viewer viewer

   # Declare a group to act as root node of a scene:
   osg.Group* root = osg.Group()

   # Declare a box class (derived from shape class) instance
   # This constructor takes an osg.Vec3 to define the center
   #  and a float to define the height, width and depth.
   #  (an overloaded constructor allows you to specify unique
   #   height, width and height values.)
   osg.Box* unitCube = osg.Box( osg.Vec3(0,0,0), 1.0)
   unitCube.setDataVariance(osg.Object.DYNAMIC)

   # Declare an instance of the shape drawable class and initialize 
   #  it with the unitCube shape we created above.
   #  This class is derived from 'drawable' so instances of this
   #  class can be added to Geode instances.
   osg.ShapeDrawable* unitCubeDrawable = osg.ShapeDrawable(unitCube)

   # Declare a instance of the geode class: 
   osg.Geode* basicShapesGeode = osg.Geode()

   # Add the unit cube drawable to the geode:
   basicShapesGeode.addDrawable(unitCubeDrawable)

   # Add the goede to the scene:
   root.addChild(basicShapesGeode)

   osg.Sphere* unitSphere = osg.Sphere( osg.Vec3(0,0,0), 1.0)
   osg.ShapeDrawable* unitSphereDrawable = osg.ShapeDrawable(unitSphere)
   unitSphereDrawable.setColor( osg.Vec4(0.1, 0.1, 0.1, 0.1) )

   osg.PositionAttitudeTransform* unitSphereXForm = 
      osg.PositionAttitudeTransform()
   unitSphereXForm.setPosition(osg.Vec3(3.0,0,0))

   osg.Geode* unitSphereGeode = osg.Geode()
   root.addChild(unitSphereXForm)
   unitSphereXForm.addChild(unitSphereGeode)
   unitSphereGeode.addDrawable(unitSphereDrawable)

   osg.Geode* pyramidGeode = createPyramid()
   
   osg.PositionAttitudeTransform* pyramidXForm = 
      osg.PositionAttitudeTransform()
   pyramidXForm.setPosition(osg.Vec3(0,-3.0,0))
   root.addChild(pyramidXForm)
   pyramidXForm.addChild(pyramidGeode)

   osg.Texture2D* KLN89FaceTexture = osg.Texture2D
   # protect from being optimized away as static state:
   KLN89FaceTexture.setDataVariance(osg.Object.DYNAMIC) 
   osg.Image* klnFace = osgDB.readImageFile("../NPS_Data/Textures/KLN89FaceB.tga")
   if (!klnFace)
   
      std.cout << " couldn't find texture, quitting." << std.endl
      return -1
   
   KLN89FaceTexture.setImage(klnFace)

   # Declare a state set for 'BLEND' texture mode
   osg.StateSet* blendStateSet = osg.StateSet()

   # Declare a TexEnv instance, set the mode to 'BLEND'
   osg.TexEnv* blendTexEnv = osg.TexEnv
   blendTexEnv.setMode(osg.TexEnv.BLEND)

   # Turn the attribute of texture 0 'ON'
   blendStateSet.setTextureAttributeAndModes(0,KLN89FaceTexture,osg.StateAttribute.ON)
   # Set the texture texture environment for texture 0 to the 
   #  texture envirnoment we declared above:
   blendStateSet.setTextureAttribute(0,blendTexEnv)

   osg.StateSet* decalStateSet = osg.StateSet()
   osg.TexEnv* decalTexEnv = osg.TexEnv()
   decalTexEnv.setMode(osg.TexEnv.DECAL)

   decalStateSet.setTextureAttributeAndModes(0,KLN89FaceTexture,osg.StateAttribute.ON)
   decalStateSet.setTextureAttribute(0,decalTexEnv)

   root.setStateSet(blendStateSet)
   unitSphereGeode.setStateSet(decalStateSet)

   # OSG1 viewer.setUpViewer(osgProducer.Viewer.STANDARD_SETTINGS)
   viewer.setSceneData( root )
   viewer.setCameraManipulator(new osgGA.TrackballManipulator())
   viewer.realize()

   while( !viewer.done() )
   
      viewer.frame()
    
   return 0


if __name__ == "__main__":
   main()
