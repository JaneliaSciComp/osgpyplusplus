#!/bin/env python

# Translated into python from C++ tutorial at
# http:#trac.openscenegraph.org/projects/osg/wiki/Support/Tutorials/BasicGeometry

from osgpypp import osg, osgViewer

# The following section of code sets up a viewer to see the scene we create, a 'group' instance to serve as the root of the scene graph, a geometry node (geode) to collect drawables, and a geometry instance to associate vertices and vertex data. (In this case the shape to render is a four-sided pyramid.) 
root = osg.Group()
pyramidGeode = osg.Geode()
pyramidGeometry = osg.Geometry()
# Next we need to associate the pyramid geometry with the pyramid geode and add the pyramid geode to the root node of the scene graph. 
pyramidGeode.addDrawable(pyramidGeometry) 
root.addChild(pyramidGeode)
# Declare an array of vertices. Each vertex will be represented by a triple -- an instances of the vec3 class. An instance of osg.Vec3Array can be used to store these triples. Since osg.Vec3Array is derived from the STL vector class, we can use the append method to add array elements. Push back adds elements to the end of the vector, thus the index of first element entered is zero, the second entries index is 1, etc.
# Using a right-handed coordinate system with 'z' up, array elements zero..four below represent the 5 points required to create a simple pyramid. 
pyramidVertices = osg.Vec3Array()
pyramidVertices.append( osg.Vec3( 0, 0, 0) ) # front left
pyramidVertices.append( osg.Vec3(10, 0, 0) ) # front right
pyramidVertices.append( osg.Vec3(10,10, 0) ) # back right 
pyramidVertices.append( osg.Vec3( 0,10, 0) ) # back left 
pyramidVertices.append( osg.Vec3( 5, 5,10) ) # peak
# Associate this set of vertices with the geometry associated with the geode we added to the scene. 
pyramidGeometry.setVertexArray(pyramidVertices)
# Next, create a primitive set and add it to the pyramid geometry. Use the first four points of the pyramid to define the base using an instance of the DrawElementsUint class. Again this class is derived from the STL vector, so the append method will add elements in sequential order. To ensure proper backface cullling, vertices should be specified in counterclockwise order. The arguments for the constructor are the enumerated type for the primitive (same as the OpenGL primitive enumerated types), and the index in the vertex array to start from. 
pyramidBase = osg.DrawElementsUInt(osg.PrimitiveSet.QUADS, 0)
pyramidBase.addElement(3)
pyramidBase.addElement(2)
pyramidBase.addElement(1)
pyramidBase.addElement(0)
pyramidGeometry.addPrimitiveSet(pyramidBase) 
# Repeat the same for each of the four sides. Again, vertices are specified in counter-clockwise order. 
pyramidFaceOne = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
pyramidFaceOne.addElement(0)
pyramidFaceOne.addElement(1)
pyramidFaceOne.addElement(4)
pyramidGeometry.addPrimitiveSet(pyramidFaceOne)

pyramidFaceTwo = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
pyramidFaceTwo.addElement(1)
pyramidFaceTwo.addElement(2)
pyramidFaceTwo.addElement(4)
pyramidGeometry.addPrimitiveSet(pyramidFaceTwo)

pyramidFaceThree = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
pyramidFaceThree.addElement(2)
pyramidFaceThree.addElement(3)
pyramidFaceThree.addElement(4)
pyramidGeometry.addPrimitiveSet(pyramidFaceThree)

pyramidFaceFour = osg.DrawElementsUInt(osg.PrimitiveSet.TRIANGLES, 0)
pyramidFaceFour.addElement(3)
pyramidFaceFour.addElement(0)
pyramidFaceFour.addElement(4)
pyramidGeometry.addPrimitiveSet(pyramidFaceFour)
# Declare and load an array of Vec4 elements to store colors. 
colors = osg.Vec4Array()
colors.append(osg.Vec4(1.0, 0.0, 0.0, 1.0) ) # index 0 red
colors.append(osg.Vec4(0.0, 1.0, 0.0, 1.0) ) # index 1 green
colors.append(osg.Vec4(0.0, 0.0, 1.0, 1.0) ) # index 2 blue
colors.append(osg.Vec4(1.0, 1.0, 1.0, 1.0) ) # index 3 white 
colors.append(osg.Vec4(1.0, 0.0, 0.0, 1.0) ) # index 4 red
# Declare the variable that will match vertex array elements to color array 
# elements. This vector should have the same number of elements as the number 
# of vertices. This vector serves as a link between vertex arrays and color 
# arrays. The next step is to associate the array of colors with the geometr 
# and set the binding mode to BIND_PER_VERTEX. 
pyramidGeometry.setColorArray(colors)
pyramidGeometry.setColorBinding(osg.Geometry.BIND_PER_VERTEX)
# Now that we have created a geometry node and added it to the scene we can 
# reuse this geometry. For example, if we wanted to put a second pyramid 15 
# units to the right of the first one, we could add this geode as the child 
# of a transform node in our scene graph. 
#  Declare and initialize a transform node.
pyramidTwoXForm = osg.PositionAttitudeTransform()
#  Use the 'addChild' method of the osg.Group class to
#  add the transform as a child of the root node and the
#  pyramid node as a child of the transform.
root.addChild(pyramidTwoXForm)
pyramidTwoXForm.addChild(pyramidGeode)
#  Declare and initialize a Vec3 instance to change the
#  position of the tank model in the scene
pyramidTwoPosition = osg.Vec3(15,0,0)
pyramidTwoXForm.setPosition( pyramidTwoPosition ) 
# The final step is to set up and enter a simulation loop. 
viewer = osgViewer.Viewer()
viewer.setSceneData( root )
viewer.run()
