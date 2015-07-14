#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgdelaunay"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgdelaunay.cpp'

# OpenSceneGraph example, osgdelaunay.
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


#* Example of use of delaunay triangulator with constraints.
#* this could be a method of generating terrains, a constraint forces certain edges to
#* exist in the triangulation.
#

#include <osgDB/ReadFile>
#include <osgUtil/Optimizer>
#include <osgViewer/Viewer>
#include <osg/CoordinateSystemNode>
#include <osgUtil/DelaunayTriangulator>
#include <osg/Material>
#include <osg/Texture2D>
#include <osg/Projection>
#include <osg/MatrixTransform>
#include <osgUtil/Tessellator> # tessellator triangulates the constrained triangles

#include <osgText/Text>

#include <sstream>
#include <iostream>

#* here are 2 common types of constraint
#*  Area - forces an area to be filled replacement geometry is a canopy and optional wall
#*  Linear - constructs a closed loop of constant width around a line.
#
class WallConstraint (osgUtil.DelaunayConstraint) :
# forces lines to eb edge
    # wall constraint - can generate a wall at the coordinates of the constraint
#* if you derive a class from DelaunayConstraint then you can create
#*  a specific geometry creation routine.
#    
    WallConstraint() : height(0), txxrepWall(10), txyrepWall(10)   

    #* or create a wall around the constraint area: 
    virtual osg.Geometry * makeWallGeometry(void) 

    #* for basic purposes, you can call these routines to make simple fill in geometries 
    virtual osg.DrawArrays* makeWall(void )   # build a wall height high around the constraint
        _line = dynamic_cast< osg.Vec3Array*>(getVertexArray())
        return (osg.DrawArrays(osg.PrimitiveSet.QUAD_STRIP,0,2*_line.size()))


    virtual osg.Vec3Array *getWall( float height) 
    virtual osg.Vec2Array *getWallTexcoords( float height) 
    virtual osg.Vec3Array *getWallNormals(void)  
        nrms = osg.Vec3Array()
        vertices = dynamic_cast< osg.Vec3Array*>(getVertexArray())
        for (unsigned int ipr=0 ipr<getNumPrimitiveSets() ipr++) 
            prset = getPrimitiveSet(ipr)
            if prset.getMode()==osg.PrimitiveSet.LINE_LOOP  or 
                prset.getMode()==osg.PrimitiveSet.LINE_STRIP :  # loops and walls
                # start with the last point on the loop
                prevp = (*vertices)[prset.index (prset.getNumIndices()-1)]
                for (unsigned int i=0 i<prset.getNumIndices() i++) 
                    curp = (*vertices)[prset.index (i)]
                    nrm = (curp-prevp)^osg.Vec3(0,0,1)
                    nrm.normalize()
                    nrms.push_back(nrm)
                    nrms.push_back(nrm)
                    prevp=curp
                curp = (*vertices)[prset.index (0)]
                nrm = (curp-prevp)^osg.Vec3(0,0,1)
                nrm.normalize()
                nrms.push_back(nrm)
                nrms.push_back(nrm)
        return nrms.release()



    # geometry creation parameters
    def setWallTexrep(w, h):
         txxrepWall=wtxyrepWall=h

    #* Wall Geometry will return with this texture applied: 
    def setTexture(tx):
         texture=tx
    #* fence/wall height 
    def setHeight(h):
         height=h
    height = float()
    texture = str()
    float txxrepWall, txyrepWall

class ArealConstraint (osgUtil.DelaunayConstraint) :
# forces edges of an area to fit triangles
    # areal constraint - general nonuniform field, forest, lake etc.
#* if you derive a class from DelaunayConstraint then you can create
#*  a specific geometry creation routine.
#    
    ArealConstraint() : txxrepArea(10), txyrepArea(10),txxrepWall(10), txyrepWall(10)  

    #* return a geometry that fills the constraint.
#    
    makeAreal = virtual deprecated_osg.Geometry *( osg.Vec3Array *points)

    #* or create a wall around the constraint area: 
    makeWallGeometry = virtual deprecated_osg.Geometry *( osg.Vec3Array *points)

    #* for basic purposes, you can call these routines to make simple fill in geometries 
    virtual osg.DrawArrays* makeWall(void ) 
    virtual osg.Vec3Array *getWall( float height) 
    virtual osg.Vec2Array *getWallTexcoords( float height) 
    virtual osg.Vec3Array *getWallNormals(void) 
    #* Canopies are the same triangles as the terrain but offset by height above
#    * (height might be 0). 
    virtual osg.DrawArrays* makeCanopy(void ) 
    virtual osg.Vec3Array *getCanopy( osg.Vec3Array *points, float height) 
    virtual osg.Vec2Array *getCanopyTexcoords( osg.Vec3Array *points) 
    virtual osg.Vec3Array *getCanopyNormals( osg.Vec3Array *points) 

    # geometry creation parameters
    def setTexrep(w, h):
         txxrepArea=wtxyrepArea=h
    def setWallTexrep(w, h):
         txxrepWall=wtxyrepWall=h
    #* Geometry will return with this texture applied: 
    def setWallTexture(tx):
         walltexture=tx
    #* Geometry will return with this texture applied: 
    def setTexture(tx):
         texture=tx
    #* fence/wall height 
    def setHeight(h):
         height=h
    walltexture = str()
    height = float()
    texture = str()
    float txxrepArea, txyrepArea
    float txxrepWall, txyrepWall


class LinearConstraint (osgUtil.DelaunayConstraint) :
#* forces edges of a "road" to fit triangles
#*  if 2 roads cross, then the overlap will be replaced by a 'cross road'
#    *  and the roads built up to the cross roads with a texture along its length. 
    LinearConstraint() : osgUtil.DelaunayConstraint(), txxrepAlong(10), txyrepAcross(10), width(2)  

    #* geometry creation parameters 
    # Width of linear feature (eg road, railway) 
    def setWidth(w):
         width=w

    #* Texture repeat distance across linear (often equal to width) and along its length 
    def setTexrep(w, h):
         txyrepAcross=htxxrepAlong=w 

    #* generate constant width around line - creates the area to be cut into the terrain. 
    setVertices = virtual void( osg.Vec3Array *lp,  float width)

    #* return a geometry that fills the constraint.
#    
    *makeGeometry = virtual deprecated_osg.Geometry( osg.Vec3Array *points)

    #* return normals array - flat shaded 
    getNormals = osg.Vec3Array*( osg.Vec3Array *points)

    #* Roads apply a texture proportional to length along the road line. 
    virtual osg.DrawArrays* makeRoad( ) 
    virtual osg.Vec3Array *getRoadVertices() 
    *getRoadTexcoords = virtual osg.Vec2Array( osg.Vec3Array *points)

    virtual osg.Vec3Array *getRoadNormals( osg.Vec3Array *points) 
    #* Geometry will return with this texture applied: 
    def setTexture(tx):
         texture=tx
    _tcoords = osg.Vec2Array()
    _edgecoords = osg.Vec3Array()
    float txxrepAlong, txyrepAcross
    texture = str()
    width = float() # width of a linear feature
    _midline = osg.Vec3Array() # defines the midline of a road, rail etc.


#* a specific type of constaint - that replaces an area with a pyramid 

class pyramid (osgUtil.DelaunayConstraint) :
#* sample user constriant - creates hole in terrain to fit base of pyramid, and
#    *  geometry of an Egyptian pyramid to fit the hole. 
    pyramid() : _side(100.) 

    def setpos(p, size):

         _pos=p_side=size

    virtual osg.Geometry * makeGeometry(void) 
        # create pyramid geometry. Centre plus points around base
        _line = dynamic_cast< osg.Vec3Array*>(getVertexArray())
        gm = deprecated_osg.Geometry()
        pts = osg.Vec3Array()
        norms = osg.Vec3Array()
        tcoords = osg.Vec2Array()
        ip = int()

        pts.push_back(_pos+osg.Vec3(0,0,_side)*0.5)
        for (ip=0 ip<4 ip++) 
            pts.push_back((*_line)[ip])
        for (ip=1 ip<5 ip++) 
            nrm =  0 if (((*pts)[ip]-(*pts)[0])^((*pts)[ip==4) else ip+1]-(*pts)[ip])
            nrm.normalize(  )
            norms.push_back(nrm)

        gm.setNormalBinding(deprecated_osg.Geometry.BIND_PER_PRIMITIVE)
        gm.setVertexArray(pts)
        dstate = gm.getOrCreateStateSet(  )
        dstate.setMode( GL_LIGHTING, osg.StateAttribute.ON )

        image = osgDB.readImageFile("Images/Brick-Std-Orange.TGA")
        if image :
            txt = osg.Texture2D()
            txt.setImage(image)
            txt.setWrap( osg.Texture2D.WRAP_S, osg.Texture2D.REPEAT )
            txt.setWrap( osg.Texture2D.WRAP_T, osg.Texture2D.REPEAT )
            dstate.setTextureAttributeAndModes(0,txt,osg.StateAttribute.ON)
        gm.setNormalArray(norms)
        ##        gm.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.TRIANGLE_FAN,0,6))
        dui = osg.DrawElementsUInt(GL_TRIANGLES)
        for (ip=0 ip<4 ip++) 
            dui.push_back(0)
            dui.push_back(ip+1)
             1 if (dui.push_back(ip==3) else ip+2)
        tcoords.push_back(osg.Vec2(2,4))
        tcoords.push_back(osg.Vec2(0,0))
        tcoords.push_back(osg.Vec2(4,0))
        tcoords.push_back(osg.Vec2(0,0))
        tcoords.push_back(osg.Vec2(4,0))
        gm.setTexCoordArray(0,tcoords)
        gm.addPrimitiveSet(dui)
        return gm
    virtual void calcVertices( void)  # must have a position first
        edges = osg.Vec3Array()
        valong = osg.Vec3()
        edges.push_back(_pos+osg.Vec3(0.5,0.5,0)*_side)
        edges.push_back(_pos+osg.Vec3(-0.5,0.5,0)*_side)
        edges.push_back(_pos+osg.Vec3(-0.5,-0.5,0)*_side)
        edges.push_back(_pos+osg.Vec3(0.5,-0.5,0)*_side)
        setVertexArray(edges)
    _pos = osg.Vec3() # where the pyramid is
    _side = float() # length of side


def getheight(x, y):

     # returns the x,y,height of terrain
    return 150*sin(x*.0020)*cos(y*.0020)
def getpt(np):
     # returns the x,y,height of terrain up to maxp^2 points
    static int maxp =40
    i = np/maxp
    j = np%maxp
    # make the random scale 0.00 if you want an equispaced XY grid.
    x = 3000.0/(maxp-1)*i+16.*(float)rand()/RAND_MAX
    y = 3000.0/(maxp-1)*j+16.*(float)rand()/RAND_MAX
    z = getheight(x,y)
    if np>=maxp*maxp : z=-1.e32
    return osg.Vec3d(x,y,z)
def createHUD(ndcs, what):
     # add a string reporting the type of winding rule tessellation applied
    geode = osg.Geode()

    timesFont = str("fonts/arial.ttf")

    # turn lighting off for the text and disable depth test to ensure its always ontop.
    stateset = geode.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

    # Disable depth test, and make sure that the hud is drawn after everything
    # else so that it always appears ontop.
    stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
    stateset.setRenderBinDetails(11,"RenderBin")

    position = osg.Vec3(50.0,900.0,0.0)
    delta = osg.Vec3(0.0,-35.0,0.0)

        text = osgText.Text()
        geode.addDrawable( text )
        cue = std.ostringstream()
        cue, "Delaunay triangulation with constraints level ", ndcs, "\n", what

        text.setFont(timesFont)
        text.setPosition(position)
        text.setText(cue.str())
        text.setColor(osg.Vec4(1.0,1.0,0.8,1.0))
        position += delta*(ndcs+2)

#if 0
        text = osgText.Text()
        geode.addDrawable( text )

        text.setFont(timesFont)
        text.setPosition(position)
        text.setText("(use ord("W") wireframe  ord("T") texture to visualise mesh)")
        text.setColor(osg.Vec4(1.0,1.0,0.8,1.0))
        position += delta
#endif
        text = osgText.Text()
        geode.addDrawable( text )

        text.setFont(timesFont)
        text.setPosition(position)
        text.setText("Press ord("n") to add another constraint.")


    # create the hud.
    modelview_abs = osg.MatrixTransform()
    modelview_abs.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    modelview_abs.setMatrix(osg.Matrix.identity())
    modelview_abs.addChild(geode)

    projection = osg.Projection()
    projection.setMatrix(osg.Matrix.ortho2D(0,1280,0,1024))
    projection.addChild(modelview_abs)

    return projection

osg.Group *makedelaunay( int ndcs)
 # create a terrain tile. This is just an example not 
    # ndcs is the number of delaunay constraints to be applied
    grp = osg.Group()
    geode = osg.Geode()
    trig = osgUtil.DelaunayTriangulator()
    stateset = geode.getOrCreateStateSet()

    points = osg.Vec3Array()

    image = osgDB.readImageFile("Images/blueFlowers.png")
    if image :
        texture = osg.Texture2D()
        texture.setImage(image)
        texture.setWrap( osg.Texture2D.WRAP_S, osg.Texture2D.REPEAT )
        texture.setWrap( osg.Texture2D.WRAP_T, osg.Texture2D.REPEAT )
        stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

    geode.setStateSet( stateset )
    i = unsigned int()

    eod = 0
    while eod>=0 : 
        pos = getpt(eod)
        if pos.z()>-10000 : 
            points.push_back(pos)
            eod++
         else:
            eod=-9999
    std.vector < pyramid* > pyrlist
    wc = WallConstraint() # This example does not remove the interior
    dc2 = ArealConstraint()
    forest = ArealConstraint()
    dc3 = LinearConstraint()
    dc6 = LinearConstraint()
    dc6a = LinearConstraint()
    dc8 = LinearConstraint()
    forestroad = LinearConstraint()
    forestroad2 = LinearConstraint()
    forestroad3 = LinearConstraint()
    dc = osgUtil.DelaunayConstraint()
    what = std.ostringstream()
    if 1==0 :  # add a simple constraint of few points
        dc = osgUtil.DelaunayConstraint()
        bounds = osg.Vec3Array()
        nmax = 4
        for (i=0  i<nmax i++) 
            x = 910.0+800.0*(i)/(float)nmax,y=810.0+6000*(i-1)*(i-1)/(float)(nmax*nmax)
            bounds.push_back(osg.Vec3(x,y,getheight(x,y)))
        dc.setVertexArray(bounds)
        dc.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_STRIP,0,nmax) )

        trig.addInputConstraint(dc)
        what, nmax, " point simple constraint\n"
    if ndcs>0 :  # add 5 pyramids
        for (unsigned int ipy=0 ipy<5#5 ipy++) 
            pyr = pyramid()
            x = 2210+ipy*120, y=1120+ipy*220
            pyr.setpos(osg.Vec3(x,y,getheight(x,y)),125.0+10*ipy)
            pyr.calcVertices() # make vertices
            pyr.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_LOOP,0,4) )
            trig.addInputConstraint(pyr)
            pyrlist.push_back(pyr)
        what, 5, " pyramids\n"
        if ndcs>1 : 
            # add a simple constraint feature - this can cut holes in the terrain or just leave the triangles
            # with edges forced to the constraint.
            dc=osgUtil.DelaunayConstraint()
            bounds = osg.Vec3Array()
            for (i=0  i<12 i++) 
                x = 610.0+420*sin(i/3.0),y=610.0+420*cos(i/3.0)
                bounds.push_back(osg.Vec3(x,y,getheight(x,y)))
            dc.setVertexArray(bounds)
            dc.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_LOOP,0,12) )

            trig.addInputConstraint(dc)
            what, 12, " point closed loop"

            if ndcs>2 : 
                wc=WallConstraint() # This example does not remove the interior
                # eg to force terrain edges that are on ridges in the terrain etc.
                # use wireframe to see the constrained edges.
                # NB this is not necessarily a closed loop of edges.
                # we do however build a wall at the coordinates.
                bounds=osg.Vec3Array()
                for (i=0  i<5 i++) 
                    x = 1610.0+420*sin(i/1.0),y=1610.0+420*cos(i/1.0)
                    bounds.push_back(osg.Vec3(x,y,getheight(x,y)))
                wc.setVertexArray(bounds)
                wc.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_STRIP,0,5) )
                wc.setHeight(12.0)
                trig.addInputConstraint(wc)
                what, " with interior removed\n"
                what, 5, " point wall derived constraint\n"

                if ndcs>3 : 
                    # add a removed area and replace it with a different texture
                    dc2=ArealConstraint()
                    bounds=osg.Vec3Array()
                    for (i=0  i<18 i++) 
                        x = 1610.0+420*sin(i/3.0),y=610.0+220*cos(i/3.0)
                        bounds.push_back(osg.Vec3(x,y,getheight(x,y)))
                    dc2.setVertexArray(bounds)
                    dc2.setTexrep(100,100) # texture is repeated at this frequency
                    dc2.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_LOOP,0,18) )
                    trig.addInputConstraint(dc2)
                    what, 18, " point area replaced\n"

                    if ndcs>4 : 
                        dc3=LinearConstraint()
                        # a linear feature or 'road'
                        verts = osg.Vec3Array()
                        for (i=0  i<32 i++) 
                            x = 610.0+50*i+90*sin(i/5.0),y=1110.0+90*cos(i/5.0)
                            verts.push_back(osg.Vec3(x,y,getheight(x,y)))
                        dc3.setVertices(verts,9.5) # width of road
                        for (osg.Vec3Array.iterator vit=points.begin() vit not =points.end() ) 
                            if dc3.contains(*vit) : 
                                vit=points.erase(vit)
                             else:
                                vit++
                        trig.addInputConstraint(dc3)
                        what, 32, " point road constraint\n"
                        if ndcs>5 : 
                            # add a removed area and replace it with a 'forest' with textured roof and walls
                            forest=ArealConstraint()
                            bounds=osg.Vec3Array()
                            for (i=0  i<12 i++) 
                                x = 610.0+420*sin(i/2.0),y=1810.0+420*cos(i/2.0)
                                bounds.push_back(osg.Vec3(x,y,getheight(x,y)))
                            forest.setVertexArray(bounds)
                            forest.setHeight(50)
                            forest.setWallTexrep(100,50)
                            forest.setTexrep(100,100) # texture is repeated at this frequency
                            forest.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_LOOP,0,12) )
                            if ndcs==6 : trig.addInputConstraint(forest)
                            what, 12, " point forest constraint\n"

                            if ndcs>6 :  # add roads that intersect forest
                                forestplus = osgUtil.DelaunayConstraint()
                                forestroad=LinearConstraint()
                                verts=osg.Vec3Array()
                                for (i=0  i<12 i++) 
                                    ip = (i-6)*(i-6)
                                    xp = 410.0+20.0*ip
                                    y = 1210.0+150*i
                                    verts.push_back(osg.Vec3(xp,y,getheight(xp,y)))
                                forestroad.setVertices(verts,22) # add road
                                forestplus.merge(forestroad)
                                forestroad2=LinearConstraint()
                                verts=osg.Vec3Array()
                                for (i=0  i<12 i++) 
                                    ip = (i-6)*(i-6)
                                    xp = 810.0-10.0*ip
                                    y = 1010.0+150*i
                                    verts.push_back(osg.Vec3(xp,y,getheight(xp,y)))
                                forestroad2.setVertices(verts,22) # add road
                                forestplus.merge(forestroad2)
                                forestroad3=LinearConstraint()
                                verts=osg.Vec3Array()
                                for (i=0  i<6 i++) 
                                    ip = (i-6)*(i-6)
                                    xp = 210.0+140.0*i+ip*10.0
                                    y = 1510.0+150*i
                                    verts.push_back(osg.Vec3(xp,y,getheight(xp,y)))
                                forestroad3.setVertices(verts,22) # add road
                                forestplus.merge(forestroad3)
                                forestplus.merge(forest)
                                forestplus.handleOverlaps()
                                for (osg.Vec3Array.iterator vit=points.begin() vit not =points.end() ) 
                                    if forestroad.contains(*vit) : 
                                        vit=points.erase(vit)
                                     elif forestroad2.contains(*vit) : 
                                        vit=points.erase(vit)
                                     elif forestroad3.contains(*vit) : 
                                        vit=points.erase(vit)
                                     else:
                                        vit++
                                trig.addInputConstraint(forestplus)
                                what, " roads intersect forest constraint\n"
                                if ndcs>7 : 
                                    # this option adds a more complex DC
                                    # made of several (ok 2 - extend your own way) overlapping DC's
                                    dcoverlap = osgUtil.DelaunayConstraint()
                                    x = 1200 float y=1900
                                        verts=osg.Vec3Array()
                                        dc6=LinearConstraint()
                                        verts.push_back(osg.Vec3(x-180,y,getheight(x-180,y)))
                                        verts.push_back(osg.Vec3(x+180,y,getheight(x+180,y)))
                                        dc6.setVertices(verts,22) # width of road
                                        dcoverlap.merge(dc6)
                                        dc6a= LinearConstraint()
                                        verts=osg.Vec3Array()
                                        verts.push_back(osg.Vec3(x,y-180,getheight(x,y-180)))
                                        verts.push_back(osg.Vec3(x-20,y,getheight(x,y)))
                                        verts.push_back(osg.Vec3(x,y+180,getheight(x,y+180)))
                                        dc6a.setVertices(verts,22) # width of road
                                        dcoverlap.merge(dc6a)
                                    what, "2 intersecting roads, with added points\n"
                                    if ndcs>9 : 
                                        # add yet more roads
                                        dc8= LinearConstraint()
                                        verts=osg.Vec3Array()
                                        rad = 60.0
                                        for (float theta=0 theta<4*osg.PI theta+=0.1*osg.PI) 
                                            xp = x+rad*cos(theta), yp=y+rad*sin(theta)
                                            verts.push_back(osg.Vec3(xp,yp,getheight(xp,yp)))
                                            rad+=2.5
                                        dc8.setVertices(verts,16) # width of road
                                        dcoverlap.merge(dc8)
                                        what, "Spiral road crosses several other constraints."
                                    dcoverlap.handleOverlaps()
                                    if ndcs>8 : 
                                        # remove vertices cleans up the texturing at the intersection.
                                        dcoverlap.removeVerticesInside(dc6)
                                        dcoverlap.removeVerticesInside(dc6a)
                                        if dc8.valid() : dcoverlap.removeVerticesInside(dc8)
                                        what, "    remove internal vertices to improve texturing."
                                    for (osg.Vec3Array.iterator vit=points.begin() vit not =points.end() ) 
                                        if dcoverlap.contains(*vit) : 
                                            vit=points.erase(vit)
                                         else:
                                            vit++
                                    trig.addInputConstraint(dcoverlap)
     # ndcs>0
    trig.setInputPointArray(points)

    #* NB you need to supply a vec3 array for the triangulator to calculate normals into 
    norms = osg.Vec3Array()
    trig.setOutputNormalArray(norms)

    trig.triangulate()
    osg.notify(osg.WARN), " End of trig\n "

    # Calculate the texture coordinates after triangulation as
    #the points may get disordered by the triangulate function
    gm = deprecated_osg.Geometry()
    gm.setVertexArray(points) # points may have been modified in order by triangulation.
    #* calculate texture coords for terrain points 
    if image : 
        repeat = 150.0, ry=150.0 # how often to repeat texture
        tcoords = osg.Vec2Array()
        for (osg.Vec3Array.iterator itr=points.begin() itr not =points.end() itr++) 
            tcatxy = osg.Vec2((*itr).x()/repeat,(*itr).y()/ry)
            tcoords.push_back(tcatxy)
        gm.setTexCoordArray(0,tcoords)
    gm.addPrimitiveSet(trig.getTriangles())
    gm.setNormalArray(trig.getOutputNormalArray())
    gm.setNormalBinding(deprecated_osg.Geometry.BIND_PER_PRIMITIVE)
    geode.addDrawable(gm)
    if ndcs>0 : 
        for ( std.vector < pyramid* >.iterator itr=pyrlist.begin() itr not =pyrlist.end() itr++) 
            trig.removeInternalTriangles(*itr)
            geode.addDrawable((*itr).makeGeometry()) # this fills the holes of each pyramid with geometry

        if ndcs>2 : 
            trig.removeInternalTriangles(dc)

            wc.setTexture("Images/Brick-Norman-Brown.TGA") # wall looks like brick
            geode.addDrawable(wc.makeWallGeometry()) # this creates wall at wc drawarrays
            if ndcs>3 : 
                trig.removeInternalTriangles(dc2)
                arpts = dc2.getPoints(points)
                dc2.setTexture("Images/purpleFlowers.png")
                geode.addDrawable(dc2.makeAreal(arpts)) # this creates fill in geometry

                if ndcs>4 :  # a simple "road"
                    trig.removeInternalTriangles(dc3)
                    dc3.setTexture ("Images/road.png")
                    dc3.setTexrep(40,9.5) # texture is repeated at this frequency
                    geode.addDrawable(dc3.makeGeometry(points)) # this creates road geometry

                    if ndcs>5 : 
                        if ndcs>6 :  #  road  forest overlap - order of removal is important
                            trig.removeInternalTriangles(forestroad)
                            trig.removeInternalTriangles(forestroad2)
                            trig.removeInternalTriangles(forestroad3)
                        trig.removeInternalTriangles(forest)
                        forest.setTexture("Images/forestRoof.png")
                        locpts = forest.getPoints(points)
                        geode.addDrawable(forest.makeAreal(locpts))

                        forest.setWallTexture("Images/forestWall.png")
                        geode.addDrawable(forest.makeWallGeometry(locpts) )
                        for (osg.Vec3Array.iterator vit=(*locpts).begin() vit not =(*locpts).end() vit++) 
                            (*vit)+=osg.Vec3(0,0,30)

                        if ndcs>6 : #  road  forest overlap
                            forestroad.setTexture ("Images/road.png")
                            forestroad.setTexrep(40,22) # texture is repeated at this frequency
                            geode.addDrawable(forestroad.makeGeometry(points)) # this creates road geometry
                            forestroad2.setTexture ("Images/road.png")
                            forestroad2.setTexrep(40,22) # texture is repeated at this frequency
                            geode.addDrawable(forestroad2.makeGeometry(points)) # this creates road geometry
                            forestroad3.setTexture ("Images/road.png")
                            forestroad3.setTexrep(40,22) # texture is repeated at this frequency
                            geode.addDrawable(forestroad3.makeGeometry(points)) # this creates road geometry
                            if ndcs>7 : #  several overlapping DC's - add geom
                                trig.removeInternalTriangles(dc6)
                                #                            dc6.makeDrawable()
                                #                            dc6a.makeDrawable()
                                dc6.setTexture ("Images/road.png")
                                dc6.setTexrep(40,22) # texture is repeated at this frequency
                                geode.addDrawable(dc6.makeGeometry(points)) # this creates road geometry
                                trig.removeInternalTriangles(dc6a)
                                dc6a.setTexture ("Images/road.png")
                                dc6a.setTexrep(40,22) # texture is repeated at this frequency
                                geode.addDrawable(dc6a.makeGeometry(points)) # this creates road geometry
                                if dc8.valid() : 
                                    trig.removeInternalTriangles(dc8)
                                    dc8.setTexture ("Images/road.png")
                                    dc8.setTexrep(40,16) # texture is repeated at this frequency
                                    geode.addDrawable(dc8.makeGeometry(points)) # this creates road geometry
    grp.addChild(geode)
    grp.addChild(createHUD(ndcs,what.str()))
    return grp.release()

class KeyboardEventHandler (osgGA.GUIEventHandler) :
# extra event handler traps ord("n") key to re-triangulate the basic terrain.

    KeyboardEventHandler(osgViewer.Viewer vr):
      viewer(vr), iview(0) 

      virtual bool handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter)
          switch(ea.getEventType())
          case(osgGA.GUIEventAdapter.KEYDOWN):
                  if ea.getKey()==ord("n") :
                      iview++
                      if iview>10 : iview=0
                      loadedModel = makedelaunay(iview)
                      viewer.setSceneData(loadedModel)
                      return True
                  break
          default:
              break
          return False

      viewer = osgViewer.Viewer()
      iview = int()


osg.Vec3Array * WallConstraint.getWall( float height) 
 # return array of points for a wall height high around the constraint
    wall = osg.Vec3Array()
    if height>0.0 : 
        off = osg.Vec3(0,0,height)
        vertices = dynamic_cast< osg.Vec3Array*>(getVertexArray())
        for (unsigned int ipr=0 ipr<getNumPrimitiveSets() ipr++) 
            prset = getPrimitiveSet(ipr)
            if prset.getMode()==osg.PrimitiveSet.LINE_LOOP  or 
                prset.getMode()==osg.PrimitiveSet.LINE_STRIP :  # nothing else loops
                # start with the last point on the loop
                for (unsigned int i=0 i<prset.getNumIndices() i++) 
                    curp = (*vertices)[prset.index (i)]
                    wall.push_back(curp)
                    wall.push_back(curp+off)
                curp = (*vertices)[prset.index (0)]
                wall.push_back(curp)
                wall.push_back(curp+off)
    return wall
osg.Vec2Array * WallConstraint.getWallTexcoords( float height) 
 # return array of points for a wall height high around the constraint
    tcoords = NULL
    if height>0.0 : 
        texrepRound = txxrepWall
        tcoords= osg.Vec2Array()
        circumference = 0 # distance around wall to get exact number of repeats of texture
        vertices = dynamic_cast< osg.Vec3Array*>(getVertexArray())
        for (unsigned int ipr=0 ipr<getNumPrimitiveSets() ipr++) 
            prset = getPrimitiveSet(ipr)
            prevp = (*vertices)[prset.index (prset.getNumIndices()-1)]
                        i = unsigned int()
            for (i=0 i<prset.getNumIndices() i++) 
                curp = (*vertices)[prset.index (i)]
                circumference+=(curp-prevp).length()
                prevp=curp
            curp = (*vertices)[prset.index (0)]
            circumference+=(curp-prevp).length()

            nround = (int)(circumference/txxrepWall)
            if nround<1 : nround=1 # at least one repeat.
            texrepRound=circumference/nround

            ds = 0
            prevp=(*vertices)[prset.index (prset.getNumIndices()-1)]
            if tcoords : 
                for (i=0 i<prset.getNumIndices() i++) 
                    curp = (*vertices)[prset.index (i)]
                    tci = osg.Vec2f(ds/texrepRound,0/txyrepWall)
                    tcoords.push_back(tci)
                    tci=osg.Vec2f(ds/texrepRound,height/txyrepWall)
                    tcoords.push_back(tci)
                    ds+=(curp-prevp).length()
                    prevp=curp
                tci = osg.Vec2f(ds/texrepRound,0/txyrepWall)
                tcoords.push_back(tci)
                tci=osg.Vec2f(ds/texrepRound,height/txyrepWall)
                tcoords.push_back(tci)
         # per primitiveset

    return tcoords
osg.Geometry *WallConstraint.makeWallGeometry() 
    gm = osg.Geometry() # the wall
    if texture not ="" : 
        image = osgDB.readImageFile(texture.c_str())
        if image :
            txt = osg.Texture2D()
            stateset = gm.getOrCreateStateSet()
            txt.setImage(image)
            txt.setWrap( osg.Texture2D.WRAP_S, osg.Texture2D.REPEAT )
            txt.setWrap( osg.Texture2D.WRAP_T, osg.Texture2D.CLAMP )
            stateset.setTextureAttributeAndModes(0,txt,osg.StateAttribute.ON)
            material = osg.Material()
            material.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(1.0,1.0,0.0,1.0))
            material.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(1.0,1.0,1.0,1.0))
            stateset.setAttribute(material,osg.StateAttribute.ON)
            stateset.setMode( GL_LIGHTING, osg.StateAttribute.ON )
    gm.setVertexArray(getWall(height))
    gm.addPrimitiveSet(makeWall())
    gm.setTexCoordArray(0,getWallTexcoords(height))
    gm.setNormalArray(getWallNormals(), osg.Array.BIND_PER_VERTEX) # this creates normals to walls

    return gm.release()

osg.Vec3Array *ArealConstraint.getWallNormals() 
    nrms = osg.Vec3Array()
    vertices = dynamic_cast< osg.Vec3Array*>(getVertexArray())
    for (unsigned int ipr=0 ipr<getNumPrimitiveSets() ipr++) 
        prset = getPrimitiveSet(ipr)
        if prset.getMode()==osg.PrimitiveSet.LINE_LOOP :  # nothing else loops
            # start with the last point on the loop
            prevp = (*vertices)[prset.index (prset.getNumIndices()-1)]
            for (unsigned int i=0 i<prset.getNumIndices() i++) 
                curp = (*vertices)[prset.index (i)]
                nrm = (curp-prevp)^osg.Vec3(0,0,1)
                nrm.normalize()
                nrms.push_back(nrm)
                nrms.push_back(nrm)
                prevp=curp
            curp = (*vertices)[prset.index (0)]
            nrm = (curp-prevp)^osg.Vec3(0,0,1)
            nrm.normalize()
            nrms.push_back(nrm)
            nrms.push_back(nrm)
    return nrms


osg.Vec3Array * ArealConstraint.getWall( float height) 
 # return array of points for a wall height high around the constraint
    wall = osg.Vec3Array()
    if height>0.0 : 
        off = osg.Vec3(0,0,height)
        vertices = dynamic_cast< osg.Vec3Array*>(getVertexArray())
        for (unsigned int ipr=0 ipr<getNumPrimitiveSets() ipr++) 
            prset = getPrimitiveSet(ipr)
            if prset.getMode()==osg.PrimitiveSet.LINE_LOOP :  # nothing else loops
                # start with the last point on the loop
                for (unsigned int i=0 i<prset.getNumIndices() i++) 
                    curp = (*vertices)[prset.index (i)]
                    wall.push_back(curp)
                    wall.push_back(curp+off)
                curp = (*vertices)[prset.index (0)]
                wall.push_back(curp)
                wall.push_back(curp+off)
    return wall

osg.Vec2Array * ArealConstraint.getWallTexcoords( float height) 
 # return array of points for a wall height high around the constraint
    tcoords = NULL
    if height>0.0 : 
        texrepRound = txxrepWall
        tcoords= osg.Vec2Array()
        circumference = 0 # distance around wall to get exact number of repeats of texture
        vertices = dynamic_cast< osg.Vec3Array*>(getVertexArray())
        for (unsigned int ipr=0 ipr<getNumPrimitiveSets() ipr++) 
            prset = getPrimitiveSet(ipr)
            prevp = (*vertices)[prset.index (prset.getNumIndices()-1)]
                        i = unsigned int()
            for (i=0 i<prset.getNumIndices() i++) 
                curp = (*vertices)[prset.index (i)]
                circumference+=(curp-prevp).length()
                prevp=curp
            curp = (*vertices)[prset.index (0)]
            circumference+=(curp-prevp).length()

            nround = (int)(circumference/txxrepWall)
            if nround<1 : nround=1 # at least one repeat.
            texrepRound=circumference/nround

            ds = 0
            prevp=(*vertices)[prset.index (prset.getNumIndices()-1)]
            if tcoords : 
                for (i=0 i<prset.getNumIndices() i++) 
                    curp = (*vertices)[prset.index (i)]
                    tci = osg.Vec2f(ds/texrepRound,0/txyrepWall)
                    tcoords.push_back(tci)
                    tci=osg.Vec2f(ds/texrepRound,height/txyrepWall)
                    tcoords.push_back(tci)
                    ds+=(curp-prevp).length()
                    prevp=curp
                tci = osg.Vec2f(ds/texrepRound,0/txyrepWall)
                tcoords.push_back(tci)
                tci=osg.Vec2f(ds/texrepRound,height/txyrepWall)
                tcoords.push_back(tci)
         # per primitiveset
    return tcoords
osg.DrawArrays* ArealConstraint.makeCanopy( void ) 
    return (osg.DrawArrays(osg.PrimitiveSet.TRIANGLES,0,3*_interiorTris.size()))
osg.Vec3Array *ArealConstraint.getCanopy( osg.Vec3Array *points, float height) 
 # returns the array of vertices in the canopy
    off = osg.Vec3(0,0,height)
    internals = osg.Vec3Array()
    tritr = trilist.const_iterator()
    for (tritr=_interiorTris.begin() tritr not =_interiorTris.end()tritr++) 
        for (int i=0 i<3 i++) 
            index = (*tritr)[i]
            internals.push_back((*points)[index]+off)
    return internals
osg.Vec3Array *ArealConstraint.getCanopyNormals( osg.Vec3Array *points) 
    nrms = osg.Vec3Array()
    tritr = trilist.const_iterator()
    for (tritr=_interiorTris.begin() tritr not =_interiorTris.end()tritr++) 
        e1 = (*points)[(*tritr)[1]]-(*points)[(*tritr)[0]]
        e2 = (*points)[(*tritr)[2]]-(*points)[(*tritr)[0]]
        nrm = e1^e2
        nrm.normalize()
        nrms.push_back(nrm)
    return nrms

osg.Vec2Array *ArealConstraint.getCanopyTexcoords( osg.Vec3Array *points) 
    tritr = osg.Vec3Array.const_iterator()
    tcoords = osg.Vec2Array()
    for (tritr=points.begin() tritr not =points.end()tritr++) 
                # calculate tcoords for terrain from xy drape.
        tci = osg.Vec2f(tritr.x()/txxrepArea, tritr.y()/txyrepArea)
        tcoords.push_back(tci)
    return tcoords.release()

osg.DrawArrays * ArealConstraint.makeWall(void) 
 # build a wall height high around the constraint
    _line = dynamic_cast< osg.Vec3Array*>(getVertexArray())
    return (osg.DrawArrays(osg.PrimitiveSet.QUAD_STRIP,0,2+2*_line.size()))

deprecated_osg.Geometry *ArealConstraint.makeWallGeometry( osg.Vec3Array *pt)
    gm = deprecated_osg.Geometry() # the wall
    edges = deprecated_osg.Geometry() # edges of bounds
    edges.setVertexArray(pt)
    trgeom = getTriangles()
    edges.addPrimitiveSet(trgeom)

    tscx = osgUtil.Tessellator() # this assembles all the constraints
    tscx.setTessellationType(osgUtil.Tessellator.TESS_TYPE_GEOMETRY)
    tscx.setBoundaryOnly(True)
    tscx.setWindingType( osgUtil.Tessellator.TESS_WINDING_NONZERO)
    #  find all edges.
    points = dynamic_cast<osg.Vec3Array*>(getVertexArray())

    tscx.retessellatePolygons(*(edges)) # find all edges

    if walltexture not ="" : 
        image = osgDB.readImageFile(walltexture.c_str())
        if image :
            txt = osg.Texture2D()
            stateset = gm.getOrCreateStateSet()
            txt.setImage(image)
            txt.setWrap( osg.Texture2D.WRAP_S, osg.Texture2D.REPEAT )
            txt.setWrap( osg.Texture2D.WRAP_T, osg.Texture2D.CLAMP )
            stateset.setTextureAttributeAndModes(0,txt,osg.StateAttribute.ON)
    points=dynamic_cast<osg.Vec3Array*>(edges.getVertexArray())
    nstart = 0
    coords = osg.Vec3Array()
    tcoords = osg.Vec2Array()
    for (unsigned int i=0 i<edges.getNumPrimitiveSets() i++) 
        pr = edges.getPrimitiveSet(i)
        if pr.getMode() == osg.PrimitiveSet.LINE_LOOP : 
            ds = 0
            for (unsigned int icon=0 icon<pr.getNumIndices() icon++) 
                ithis = pr.index(icon)
                pt = (*points)[ithis]
                coords.push_back(pt)
                coords.push_back(pt+osg.Vec3(0,0,height))
                tcoords.push_back(osg.Vec2(ds/txxrepWall,0))
                tcoords.push_back(osg.Vec2(ds/txxrepWall,1.0))
                if icon<pr.getNumIndices()-1 : ds+=((*points)[pr.index(icon+1)]-(*points)[ithis]).length()
                else ds+=((*points)[pr.index(0)]-(*points)[ithis]).length()
            # repeat first point
            ithis = pr.index(0)
            coords.push_back((*points)[ithis])
            coords.push_back((*points)[ithis]+osg.Vec3(0,0,height))
            tcoords.push_back(osg.Vec2(ds/txxrepWall,0))
            tcoords.push_back(osg.Vec2(ds/txxrepWall,1.0))
            gm.setVertexArray(coords)
            gm.setTexCoordArray(0,tcoords)
            gm.addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.QUAD_STRIP,nstart,2+2*pr.getNumIndices()))
            nstart+=2+2*pr.getNumIndices()

    return gm.release()


deprecated_osg.Geometry * ArealConstraint.makeAreal( osg.Vec3Array *points)
    gm = deprecated_osg.Geometry() # the fill in area
    if _interiorTris.size()>0 : 
        gm =deprecated_osg.Geometry() # the forest roof
        gm.setVertexArray(points)
        trgeom = getTriangles()
        gm.addPrimitiveSet(trgeom)
        gm.setNormalArray(getCanopyNormals(points))
        gm.setNormalBinding(deprecated_osg.Geometry.BIND_PER_PRIMITIVE)
        gm.setTexCoordArray(0,getCanopyTexcoords(points))
        image = osgDB.readImageFile(texture)
        if image :
            txt = osg.Texture2D()
            stateset = gm.getOrCreateStateSet()
            txt.setImage(image)
            txt.setWrap( osg.Texture2D.WRAP_S, osg.Texture2D.REPEAT )
            txt.setWrap( osg.Texture2D.WRAP_T, osg.Texture2D.REPEAT )
            stateset.setTextureAttributeAndModes(0,txt,osg.StateAttribute.ON)
            material = osg.Material()
            material.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(1.0,1.0,1.0,1.0))
            material.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(1.0,1.0,1.0,1.0))
            stateset.setAttribute(material,osg.StateAttribute.ON)
            stateset.setMode( GL_LIGHTING, osg.StateAttribute.ON )
    return gm.release()


void LinearConstraint.setVertices( osg.Vec3Array *lp,  float w)
 # generate constant width around line (calls setvertices(edges))
    edges = osg.Vec3Array()
    _tcoords=osg.Vec2Array() # texture coordinates for replacement geometry
    _edgecoords=osg.Vec3Array() # posiiton coordinates for replacement geometry
    width=w
    _midline=lp
    ds = 0
    for(unsigned int i=0i<lp.size()i++) 
        valong = osg.Vec3()
        osg.Vec3 pos[2]

        if i==0 : 
            valong=(*lp)[i+1]-(*lp)[i]
         elif i==lp.size()-1 : 
            valong=(*lp)[i]-(*lp)[i-1]
         else:
            valong=(*lp)[i+1]-(*lp)[i-1]
        valong.normalize()
        vperp = valong^osg.Vec3(0,0,1)
        pos[0]=(*lp)[i]-vperp*.5*width
        pos[1]=(*lp)[i]+vperp*.5*width
        edges.push_back(pos[0])
        _edgecoords.push_back(pos[0])
        _tcoords.push_back(osg.Vec2(0/txyrepAcross,ds/txxrepAlong))
        edges.insert(edges.begin() ,pos[1])
        _edgecoords.insert(_edgecoords.begin() ,pos[1])
        _tcoords.insert(_tcoords.begin() ,osg.Vec2(width/txyrepAcross,ds/txxrepAlong))
        if i<lp.size()-1 : ds+=((*lp)[i+1]-(*lp)[i]).length()
    setVertexArray(edges)
    addPrimitiveSet(osg.DrawArrays(osg.PrimitiveSet.LINE_LOOP,0,edges.size()) )

osg.DrawArrays* LinearConstraint.makeRoad(void ) 
    return     osg.DrawArrays(osg.PrimitiveSet.QUAD_STRIP,0,2*_midline.size())


osg.Vec3Array *LinearConstraint.getRoadNormals( osg.Vec3Array* #points) 
    nrms = osg.Vec3Array()
    for(unsigned int i=0i<_midline.size()i++) 
        valong = osg.Vec3() # vector along midline of road
        if i==0 : 
            valong=(*_midline)[i+1]-(*_midline)[i]
         elif i==_midline.size()-1 : 
            valong=(*_midline)[i]-(*_midline)[i-1]
         else:
            valong=(*_midline)[i+1]-(*_midline)[i-1]
        vperp = valong^osg.Vec3(0,0,1)
        nrm = vperp^valong # normal to linear
        nrm.normalize()
        nrms.push_back(nrm) # repeated for each vertex of linear.
        nrms.push_back(nrm)
    return nrms
osg.Vec3Array *LinearConstraint.getRoadVertices() 
    linearEdges = osg.Vec3Array()
    for(unsigned int i=0i<_midline.size()i++) 
        valong = osg.Vec3() # vector along midline of road
        if i==0 : 
            valong=(*_midline)[i+1]-(*_midline)[i]
         elif i==_midline.size()-1 : 
            valong=(*_midline)[i]-(*_midline)[i-1]
         else:
            valong=(*_midline)[i+1]-(*_midline)[i-1]
        valong.normalize()
        vperp = valong^osg.Vec3(0,0,1) # vector across road
        # sides of linear
        linearEdges.push_back((*_midline)[i]-vperp*.5*width)
        linearEdges.push_back((*_midline)[i]+vperp*.5*width)
    return linearEdges

osg.Vec2Array *LinearConstraint.getRoadTexcoords( osg.Vec3Array *points)  
    # need to create a vec2 array from the coordinates that fits the road
    tritr = osg.Vec3Array.const_iterator()
    tcoords = osg.Vec2Array()
    for (tritr=points.begin() tritr not =points.end()tritr++) 
        tci = osg.Vec2(-1.,-1.)
        ib = 0
        # osg.Vec3Array *varr=dynamic_cast<osg.Vec3Array*>(getVertexArray())
        ptfound = False
        for (osg.Vec3Array.iterator vit=_edgecoords.begin() vit not = _edgecoords.end()  and   not ptfound vit++) 
            if *vit :==(*tritr) : 
                tci=_tcoords.at(ib)
                ptfound=True
            ib++
        if  not ptfound :  # search for surrounding points and interpolate
            ib=0
            pminus = (_edgecoords.back()) # need pminus for interpolation
            ibm1 = _edgecoords.size()-1
            for (osg.Vec3Array.iterator vit=_edgecoords.begin() vit not = _edgecoords.end() # and   not ptfound vit++) 
                pplus = (*vit)-(*tritr)
                dpm = pminus-(*tritr)
                pplus.set (pplus.x(),pplus.y(),0)
                dpm.set (dpm.x(),dpm.y(),0)
                dprod = pplus*dpm/(pplus.length() * dpm.length())
                if dprod<-0.9999 :  # *tritr lies between....
                    tminus = _tcoords.at(ibm1)
                    tplus = _tcoords.at(ib)
                    frac = (dpm.length()/(dpm.length()+pplus.length()))
                    tci=tminus+((tplus-tminus)*frac)
                    ptfound=True
                ibm1=ib
                ib++
                pminus=(*vit)
        tcoords.push_back(tci)
    # some extra points are not interpolated as they lie between 2 interpolated vertices
    for (tritr=points.begin() tritr not =points.end()tritr++) 
        ib = tritr-points.begin()
        tci = tcoords.at(ib)
        if tci.x()<-.99  and  tci.y()<-.99 : 
            # search through each of the primitivesets
            ptitr = osg.Vec3Array.const_iterator()
            #    osg.notify(osg.WARN), "Not calculated ", (*tritr).x(), ",", (*tritr).y()
            for (ptitr=points.begin() ptitr not =points.end()ptitr++) 
    return tcoords.release()
osg.Vec3Array * LinearConstraint.getNormals( osg.Vec3Array *points)
    norms = osg.Vec3Array()
    for (osg.DrawElementsUInt.iterator uiitr=prim_tris_.begin() uiitr not =prim_tris_.end()uiitr+=3) 
        e1 = (*points)[*(uiitr+1)]-(*points)[(*uiitr)]
        e2 = (*points)[*(uiitr+2)]-(*points)[*(uiitr+1)]
        n = e1^e2
        n.normalize()
        #    if n.z()<0 : n=-n
        norms.push_back(n)
    return norms.release()

deprecated_osg.Geometry * LinearConstraint.makeGeometry( osg.Vec3Array *points)
    gm = deprecated_osg.Geometry() # the fill in road/railway
    if _midline.size()>0 : 
        locpts = getPoints(points)
        if texture not ="" : 
            image = osgDB.readImageFile(texture.c_str())
            if image :
                txt = osg.Texture2D()
                stateset = gm.getOrCreateStateSet()
                txt.setImage(image)
                txt.setWrap( osg.Texture2D.WRAP_S, osg.Texture2D.REPEAT )
                txt.setWrap( osg.Texture2D.WRAP_T, osg.Texture2D.REPEAT )
                stateset.setTextureAttributeAndModes(0,txt,osg.StateAttribute.ON)
                material = osg.Material()
                material.setAmbient(osg.Material.FRONT_AND_BACK,osg.Vec4(1.0,1.0,1.0,1.0))
                material.setDiffuse(osg.Material.FRONT_AND_BACK,osg.Vec4(1.0,1.0,1.0,1.0))
                stateset.setAttribute(material,osg.StateAttribute.ON)
                stateset.setMode( GL_LIGHTING, osg.StateAttribute.ON )
            gm.setTexCoordArray(0,getRoadTexcoords(locpts))
        gm.setVertexArray(locpts)
        gm.setNormalArray(getNormals(locpts))
        gm.setNormalBinding(deprecated_osg.Geometry.BIND_PER_PRIMITIVE)
        gm.addPrimitiveSet(getTriangles())

    return gm.release()




def main(argv):



    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer()

    # create the scene from internal specified terrain/constraints.
    loadedModel = makedelaunay(0)

    # if no model has been successfully loaded report failure.
    if  not loadedModel :
        print arguments.getApplicationName(), ": No data loaded"
        return 1

    # optimize the scene graph, remove redundant nodes and state etc.
    optimizer = osgUtil.Optimizer()
    optimizer.optimize(loadedModel)

    # pass the loaded scene graph to the viewer.
    viewer.setSceneData(loadedModel)

    # copied from osgtessealte.cpp
    # add event handler for keyboard ord("n") to retriangulate
    viewer.addEventHandler(KeyboardEventHandler(viewer))

    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
