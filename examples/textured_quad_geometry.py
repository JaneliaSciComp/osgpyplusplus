from osgpyplusplus import osg
from osgpyplusplus import osgDB
from osgpyplusplus import osgGA
from osgpyplusplus import osgViewer

# Adapted from https://code.google.com/p/osgboostpython/

# As a test of the capacity to create osg::Geometry through python, this
# useful utility function is not wrapped through C++ but is instead re-written
# in python and used that way.
def createTexturedQuadGeometry(corner, widthVec, heightVec, l, b, r, t):
    g = osg.Geometry()

    # Create vertex array
    vertices = osg.Vec3Array()
    vertices.append(corner+widthVec)
    vertices.append(corner)
    vertices.append(corner+heightVec)
    vertices.append(corner+widthVec+heightVec)
    g.setVertexArray(vertices)

    # Create texcoord array
    texcoords = osg.Vec2Array()
    texcoords.append(osg.Vec2f(l,t))
    texcoords.append(osg.Vec2f(l,b))
    texcoords.append(osg.Vec2f(r,b))
    texcoords.append(osg.Vec2f(r,t))
    g.setTexCoordArray(0, texcoords)

    # Create color array (single value, white)
    colors = osg.Vec4Array()
    colors.append(osg.Vec4f(1,1,1,1))
    g.setColorArray(colors)
    g.colorBinding = osg.Geometry.BIND_OVERALL

    # Create normal array (single value for all vertices)
    normals = osg.Vec3Array()
    normals.append(osg.Vec3f(0,-1,0))
    g.setNormalArray(normals)
    g.normalBinding = osg.Geometry.BIND_OVERALL

    # Add primitive set
    g.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUADS, 0, 4))

    return g

# Create a 1x1 quad in XZ plane
g = osg.createTexturedQuadGeometry(osg.Vec3f(0,0,0), osg.Vec3f(1,0,0), osg.Vec3f(0,0,1), 0, 0, 1, 1)
g.getColorArray()[0] = osg.Vec4f(1,1,1,0.5)  # change color to semitransparent

# Add it to a geode
geode = osg.Geode()
geode.addDrawable(g)

# Add texture
i = osgDB.readImageFile("Images/osg256.png")
t = osg.Texture2D(i)
s = geode.stateSet
s.setTextureAttributeAndModes(0, t, osg.StateAttribute.Values.ON)

# Make sure blending is active and the geode is in the transparent (depth sorted) bin
s.setRenderingHint(osg.StateSet.TRANSPARENT_BIN)
s.setMode(osg.GL_BLEND, osg.StateAttribute.ON)

# Create viewer, add some standard handlers to it and run it
viewer = osgViewer.Viewer()
viewer.setUpViewInWindow(50, 50, 1024, 768);
viewer.addEventHandler(osgGA.StateSetManipulator(geode.stateSet))
viewer.addEventHandler(osgViewer.HelpHandler())
viewer.addEventHandler(osgViewer.StatsHandler())
viewer.setSceneData(geode)
viewer.run()
del viewer      # To cause the dtor to be called, hence the window to be destroyed.
