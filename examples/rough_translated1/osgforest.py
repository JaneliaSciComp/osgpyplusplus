#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osgforest"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgUtil
from osgpypp import osgViewer


# Translated from file 'osgforest.cpp'

# OpenSceneGraph example, osgforest.
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

#include <osg/AlphaFunc>
#include <osg/Billboard>
#include <osg/BlendFunc>
#include <osg/Depth>
#include <osg/Geode>
#include <osg/Geometry>
#include <osg/Material>
#include <osg/Math>
#include <osg/MatrixTransform>
#include <osg/PolygonOffset>
#include <osg/Projection>
#include <osg/ShapeDrawable>
#include <osg/StateSet>
#include <osg/Switch>
#include <osg/Texture2D>
#include <osg/TextureBuffer>
#include <osg/Image>
#include <osg/TexEnv>
#include <osg/VertexProgram>
#include <osg/FragmentProgram>

#include <osgDB/ReadFile>
#include <osgDB/FileUtils>

#include <osgUtil/LineSegmentIntersector>
#include <osgUtil/IntersectionVisitor>
#include <osgUtil/SmoothingVisitor>

#include <osgText/Text>

#include <osgViewer/Viewer>
#include <osgViewer/ViewerEventHandlers>

#include <osgGA/StateSetManipulator>

#include <iostream>
#include <sstream>

# for the grid data..
#include "../osghangglide/terrain_coords.h"

# class to create the forest and manage the movement between various techniques.
class ForestTechniqueManager (osg.Referenced) :

    ForestTechniqueManager() 

    class Tree (osg.Referenced) :

        Tree():
            _color(255,255,255,255),
            _width(1.0),
            _height(1.0),
            _type(0) 

        Tree( osg.Vec3 position,  osg.Vec4ub color, float width, float height, unsigned int type):
            _position(position),
            _color(color),
            _width(width),
            _height(height),
            _type(type) 

        _position = osg.Vec3()
        _color = osg.Vec4ub()
        _width = float()
        _height = float()
        _type = unsigned int()
    

    typedef std.vector< Tree > TreeList

    class Cell (osg.Referenced) :
        typedef std.vector< Cell > CellList

        Cell():_parent(0) 
        Cell(osg.BoundingBox bb):_parent(0), _bb(bb) 

        def addCell(cell):

             cell._parent=this _cells.push_back(cell) 

        def addTree(tree):

             _trees.push_back(tree) 

        def addTrees(trees):

             _trees.insert(_trees.end(),trees.begin(),trees.end()) 

        computeBound = void()

        def contains(position):

             return _bb.contains(position) 

        divide = bool(unsigned int maxNumTreesPerCell=10)

        divide = bool(bool xAxis, bool yAxis, bool zAxis)

        bin = void()


        _parent = Cell*()
        _bb = osg.BoundingBox()
        _cells = CellList()
        _trees = TreeList()

    

    def random(min, max):

         return min + (max-min)*(float)rand()/(float)RAND_MAX 
    def random(min, max):
         return min + (int)((float)(max-min)*(float)rand()/(float)RAND_MAX) 

    createTerrain = osg.Geode*( osg.Vec3 origin,  osg.Vec3 size)

    createTreeList = void(osg.Node* terrain, osg.Vec3 origin,  osg.Vec3 size,unsigned int numTreesToCreate,TreeList trees)

    createSprite = osg.Geometry*( float w, float h, osg.Vec4ub color )

    createOrthogonalQuads = osg.Geometry*(  osg.Vec3 pos, float w, float h, osg.Vec4ub color )
    createOrthogonalQuadsNoColor = osg.Geometry*(  osg.Vec3 pos, float w, float h )

    createBillboardGraph = osg.Node*(Cell* cell,osg.StateSet* stateset)

    createXGraph = osg.Node*(Cell* cell,osg.StateSet* stateset)

    createTransformGraph = osg.Node*(Cell* cell,osg.StateSet* stateset)

    createShaderGraph = osg.Node*(Cell* cell,osg.StateSet* stateset)

    createGeometryShaderGraph = osg.Node*(Cell* cell, osg.StateSet* stateset)

    createTextureBufferGraph = osg.Node*(Cell* cell, osg.Geometry* templateGeometry)

    CollectTreePositions = void(Cell* cell, std.vector< osg.Vec3 > positions)

    createHUDWithText = osg.Node*( str text)

    createScene = osg.Node*(unsigned int numTreesToCreates, unsigned int maxNumTreesPerCell)

    def advanceToNextTechnique(delta):

        
        if _techniqueSwitch.valid() :
            _currentTechnique += delta
            if _currentTechnique<0 :
                _currentTechnique = _techniqueSwitch.getNumChildren()-1
            if _currentTechnique>=(int)_techniqueSwitch.getNumChildren() :
                _currentTechnique = 0
            _techniqueSwitch.setSingleChildOn(_currentTechnique)

    _techniqueSwitch = osg.Switch()
    _currentTechnique = int()




# event handler to capture keyboard events and use them to advance the technique used for rendering
class TechniqueEventHandler (osgGA.GUIEventHandler) :

    TechniqueEventHandler(ForestTechniqueManager* ttm=0)  _ForestTechniqueManager = ttm 

    META_Object(osgforestApp,TechniqueEventHandler)

    handle = virtual bool( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter, osg.Object*, osg.NodeVisitor*)

    virtual void getUsage(osg.ApplicationUsage usage) 

    ~TechniqueEventHandler() 

    TechniqueEventHandler( TechniqueEventHandler, osg.CopyOp) 

    _ForestTechniqueManager = ForestTechniqueManager()




bool TechniqueEventHandler.handle( osgGA.GUIEventAdapter ea,osgGA.GUIActionAdapter, osg.Object*, osg.NodeVisitor*)
    switch(ea.getEventType())
        case(osgGA.GUIEventAdapter.KEYDOWN):
            if ea.getKey()==ord("n")  or 
                ea.getKey()==osgGA.GUIEventAdapter.KEY_Right  or 
                ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Right :
                _ForestTechniqueManager.advanceToNextTechnique(1)
                return True
            elif ea.getKey()==ord("p")  or 
                     ea.getKey()==osgGA.GUIEventAdapter.KEY_Left  or 
                     ea.getKey()==osgGA.GUIEventAdapter.KEY_KP_Left :
                _ForestTechniqueManager.advanceToNextTechnique(-1)
                return True
            return False

        default:
            return False

void TechniqueEventHandler.getUsage(osg.ApplicationUsage usage) 
    usage.addKeyboardMouseBinding("n or Left Arrow","Advance to next technique")
    usage.addKeyboardMouseBinding("p or Right Array","Move to previous technique")


void ForestTechniqueManager.Cell.computeBound()
    _bb.init()
    for(CellList.iterator citr=_cells.begin()
        not = _cells.end()
        ++citr)
        (*citr).computeBound()
        _bb.expandBy((*citr)._bb)

    for(TreeList.iterator titr=_trees.begin()
        not = _trees.end()
        ++titr)
        _bb.expandBy((*titr)._position)

bool ForestTechniqueManager.Cell.divide(unsigned int maxNumTreesPerCell)

    if _trees.size()<=maxNumTreesPerCell : return False

    computeBound()

    radius = _bb.radius()
    divide_distance = radius*0.7
    if divide((_bb.xMax()-_bb.xMin())>divide_distance,(_bb.yMax()-_bb.yMin())>divide_distance,(_bb.zMax()-_bb.zMin())>divide_distance) :
        # recusively divide the cells till maxNumTreesPerCell is met.
        for(CellList.iterator citr=_cells.begin()
            not = _cells.end()
            ++citr)
            (*citr).divide(maxNumTreesPerCell)
        return True
   else:
        return False

bool ForestTechniqueManager.Cell.divide(bool xAxis, bool yAxis, bool zAxis)
    if  not (xAxis  or  yAxis  or  zAxis) : return False

    if _cells.empty() :
        _cells.push_back(Cell(_bb))

    if xAxis :
        numCellsToDivide = _cells.size()
        for(unsigned int i=0i<numCellsToDivide++i)
            orig_cell = _cells[i]
            new_cell = Cell(orig_cell._bb)

            xCenter = (orig_cell._bb.xMin()+orig_cell._bb.xMax())*0.5
            orig_cell._bb.xMax() = xCenter
            new_cell._bb.xMin() = xCenter

            _cells.push_back(new_cell)

    if yAxis :
        numCellsToDivide = _cells.size()
        for(unsigned int i=0i<numCellsToDivide++i)
            orig_cell = _cells[i]
            new_cell = Cell(orig_cell._bb)

            yCenter = (orig_cell._bb.yMin()+orig_cell._bb.yMax())*0.5
            orig_cell._bb.yMax() = yCenter
            new_cell._bb.yMin() = yCenter

            _cells.push_back(new_cell)

    if zAxis :
        numCellsToDivide = _cells.size()
        for(unsigned int i=0i<numCellsToDivide++i)
            orig_cell = _cells[i]
            new_cell = Cell(orig_cell._bb)

            zCenter = (orig_cell._bb.zMin()+orig_cell._bb.zMax())*0.5
            orig_cell._bb.zMax() = zCenter
            new_cell._bb.zMin() = zCenter

            _cells.push_back(new_cell)

    bin()

    return True


void ForestTechniqueManager.Cell.bin()
    # put trees in appropriate cells.
    treesNotAssigned = TreeList()
    for(TreeList.iterator titr=_trees.begin()
        not = _trees.end()
        ++titr)
        tree = titr
        assigned = False
        for(CellList.iterator citr=_cells.begin()
            not = _cells.end()  and   not assigned
            ++citr)
            if *citr :.contains(tree._position) :
                (*citr).addTree(tree)
                assigned = True
        if  not assigned : treesNotAssigned.push_back(tree)

    # put the unassigned trees back into the original local tree list.
    _trees.swap(treesNotAssigned)


    # prune empty cells.
    cellsNotEmpty = CellList()
    for(CellList.iterator citr=_cells.begin()
        not = _cells.end()
        ++citr)
        if  not ((*citr)._trees.empty()) :
            cellsNotEmpty.push_back(*citr)
    _cells.swap(cellsNotEmpty)



osg.Geode* ForestTechniqueManager.createTerrain( osg.Vec3 origin,  osg.Vec3 size)
    geode = osg.Geode()

    # ---------------------------------------
    # Set up a StateSet to texture the objects
    # ---------------------------------------
    stateset = osg.StateSet()

    image = osgDB.readImageFile("Images/lz.rgb")
    if image :
        texture = osg.Texture2D()
        texture.setImage(image)
        stateset.setTextureAttributeAndModes(0,texture,osg.StateAttribute.ON)

    geode.setStateSet( stateset )

    numColumns = 38
    numRows = 39
    r = unsigned int()
    c = unsigned int()

    # compute z range of z values of grid data so we can scale it.
    min_z = FLT_MAX
    max_z = -FLT_MAX
    for(r=0r<numRows++r)
        for(c=0c<numColumns++c)
            min_z = osg.minimum(min_z,vertex[r+c*numRows][2])
            max_z = osg.maximum(max_z,vertex[r+c*numRows][2])

    scale_z = size.z()/(max_z-min_z)


    createGrid = False
    if createGrid :

        grid = osg.HeightField()
        grid.allocate(numColumns,numRows)
        grid.setOrigin(origin)
        grid.setXInterval(size.x()/(float)(numColumns-1))
        grid.setYInterval(size.y()/(float)(numRows-1))

        for(r=0r<numRows++r)
            for(c=0c<numColumns++c)
                grid.setHeight(c,r,(vertex[r+c*numRows][2]-min_z)*scale_z)

        geode.addDrawable(osg.ShapeDrawable(grid))
    else:
        geometry = osg.Geometry()

        v = *(osg.Vec3Array(numColumns*numRows))
        t = *(osg.Vec2Array(numColumns*numRows))
        color = *(osg.Vec4ubArray(1))

        color[0].set(255,255,255,255)

        rowCoordDelta = size.y()/(float)(numRows-1)
        columnCoordDelta = size.x()/(float)(numColumns-1)

        rowTexDelta = 1.0/(float)(numRows-1)
        columnTexDelta = 1.0/(float)(numColumns-1)

        pos = origin
        tex = osg.Vec2(0.0,0.0)
        vi = 0
        for(r=0r<numRows++r)
            pos.x() = origin.x()
            tex.x() = 0.0
            for(c=0c<numColumns++c)
                v[vi].set(pos.x(),pos.y(),pos.z()+(vertex[r+c*numRows][2]-min_z)*scale_z)
                t[vi].set(tex.x(),tex.y())
                pos.x()+=columnCoordDelta
                tex.x()+=columnTexDelta
                ++vi
            pos.y() += rowCoordDelta
            tex.y() += rowTexDelta

        geometry.setVertexArray(v)
        geometry.setColorArray(color, osg.Array.BIND_OVERALL)
        geometry.setTexCoordArray(0,t)

        for(r=0r<numRows-1++r)
            drawElements = *(osg.DrawElementsUShort(GL_QUAD_STRIP,2*numColumns))
            geometry.addPrimitiveSet(drawElements)
            ei = 0
            for(c=0c<numColumns++c)
                drawElements[ei++] = (r+1)*numColumns+c
                drawElements[ei++] = (r)*numColumns+c

        geode.addDrawable(geometry)

        sv = osgUtil.SmoothingVisitor()
        sv.smooth(*geometry)

    return geode

void ForestTechniqueManager.createTreeList(osg.Node* terrain, osg.Vec3 origin,  osg.Vec3 size,unsigned int numTreesToCreate,TreeList trees)

    max_TreeHeight = sqrtf(size.length2()/(float)numTreesToCreate)
    max_TreeWidth = max_TreeHeight*0.5

    min_TreeHeight = max_TreeHeight*0.3
    min_TreeWidth = min_TreeHeight*0.5

    trees.reserve(trees.size()+numTreesToCreate)


    for(unsigned int i=0i<numTreesToCreate++i)
        tree = Tree()
        tree._position.set(random(origin.x(),origin.x()+size.x()),random(origin.y(),origin.y()+size.y()),origin.z())
        tree._color.set(random(128,255),random(128,255),random(128,255),255)
        tree._width = random(min_TreeWidth,max_TreeWidth)
        tree._height = random(min_TreeHeight,max_TreeHeight)
        tree._type = 0

        if terrain :
            intersector = osgUtil.LineSegmentIntersector(tree._position,tree._position+osg.Vec3(0.0,0.0,size.z()))

            iv = osgUtil.IntersectionVisitor(intersector)

            terrain.accept(iv)

            if intersector.containsIntersections() :
                intersections = intersector.getIntersections()
                for(osgUtil.LineSegmentIntersector.Intersections.iterator itr = intersections.begin()
                    not = intersections.end()
                    ++itr)
                    intersection = *itr
                    tree._position = intersection.getWorldIntersectPoint()

        trees.push_back(tree)

osg.Geometry* ForestTechniqueManager.createSprite( float w, float h, osg.Vec4ub color )
    # set up the coords
    v = *(osg.Vec3Array(4))
    t = *(osg.Vec2Array(4))
    c = *(osg.Vec4ubArray(1))

    v[0].set(-w*0.5,0.0,0.0)
    v[1].set( w*0.5,0.0,0.0)
    v[2].set( w*0.5,0.0,h)
    v[3].set(-w*0.5,0.0,h)

    c[0] = color

    t[0].set(0.0,0.0)
    t[1].set(1.0,0.0)
    t[2].set(1.0,1.0)
    t[3].set(0.0,1.0)

    geom = osg.Geometry()

    geom.setVertexArray( v )

    geom.setTexCoordArray( 0, t )

    geom.setColorArray( c, osg.Array.BIND_OVERALL )

    geom.addPrimitiveSet( osg.DrawArrays(osg.PrimitiveSet.QUADS,0,4) )

    return geom

osg.Geometry* ForestTechniqueManager.createOrthogonalQuads(  osg.Vec3 pos, float w, float h, osg.Vec4ub color )
    # set up the coords
    v = *(osg.Vec3Array(8))
    t = *(osg.Vec2Array(8))
    c = *(osg.Vec4ubArray(1))

    rotation = random(0.0,osg.PI/2.0)
    sw = sinf(rotation)*w*0.5
    cw = cosf(rotation)*w*0.5

    v[0].set(pos.x()-sw,pos.y()-cw,pos.z()+0.0)
    v[1].set(pos.x()+sw,pos.y()+cw,pos.z()+0.0)
    v[2].set(pos.x()+sw,pos.y()+cw,pos.z()+h)
    v[3].set(pos.x()-sw,pos.y()-cw,pos.z()+h)

    v[4].set(pos.x()-cw,pos.y()+sw,pos.z()+0.0)
    v[5].set(pos.x()+cw,pos.y()-sw,pos.z()+0.0)
    v[6].set(pos.x()+cw,pos.y()-sw,pos.z()+h)
    v[7].set(pos.x()-cw,pos.y()+sw,pos.z()+h)

    c[0] = color

    t[0].set(0.0,0.0)
    t[1].set(1.0,0.0)
    t[2].set(1.0,1.0)
    t[3].set(0.0,1.0)

    t[4].set(0.0,0.0)
    t[5].set(1.0,0.0)
    t[6].set(1.0,1.0)
    t[7].set(0.0,1.0)

    geom = osg.Geometry()

    geom.setVertexArray( v )

    geom.setTexCoordArray( 0, t )

    geom.setColorArray( c, osg.Array.BIND_OVERALL )

    geom.addPrimitiveSet( osg.DrawArrays(osg.PrimitiveSet.QUADS,0,8) )

    return geom

osg.Node* ForestTechniqueManager.createBillboardGraph(Cell* cell,osg.StateSet* stateset)
    needGroup = not (cell._cells.empty())
    needBillboard = not (cell._trees.empty())

    billboard = 0
    group = 0

    if needBillboard :
        billboard = osg.Billboard()
        billboard.setStateSet(stateset)
        for(TreeList.iterator itr=cell._trees.begin()
            not = cell._trees.end()
            ++itr)
            tree = **itr
            billboard.addDrawable(createSprite(tree._width,tree._height,tree._color),tree._position)

    if needGroup :
        group = osg.Group()
        for(Cell.CellList.iterator itr=cell._cells.begin()
            not = cell._cells.end()
            ++itr)
            group.addChild(createBillboardGraph(itr,stateset))

        if billboard : group.addChild(billboard)

    if group : return group
    else return billboard

osg.Node* ForestTechniqueManager.createXGraph(Cell* cell,osg.StateSet* stateset)
    needGroup = not (cell._cells.empty())
    needTrees = not (cell._trees.empty())

    geode = 0
    group = 0

    if needTrees :
        geode = osg.Geode()
        geode.setStateSet(stateset)

        for(TreeList.iterator itr=cell._trees.begin()
            not = cell._trees.end()
            ++itr)
            tree = **itr
            geode.addDrawable(createOrthogonalQuads(tree._position,tree._width,tree._height,tree._color))

    if needGroup :
        group = osg.Group()
        for(Cell.CellList.iterator itr=cell._cells.begin()
            not = cell._cells.end()
            ++itr)
            group.addChild(createXGraph(itr,stateset))

        if geode : group.addChild(geode)

    if group : return group
    else return geode

osg.Node* ForestTechniqueManager.createTransformGraph(Cell* cell,osg.StateSet* stateset)
    needGroup = not (cell._cells.empty())
    needTrees = not (cell._trees.empty())

    transform_group = 0
    group = 0

    if needTrees :
        transform_group = osg.Group()

        geometry = createOrthogonalQuads(osg.Vec3(0.0,0.0,0.0),1.0,1.0,osg.Vec4ub(255,255,255,255))

        for(TreeList.iterator itr=cell._trees.begin()
            not = cell._trees.end()
            ++itr)
            tree = **itr
            transform = osg.MatrixTransform()
            transform.setMatrix(osg.Matrix.scale(tree._width,tree._width,tree._height)*osg.Matrix.translate(tree._position))

            geode = osg.Geode()
            geode.setStateSet(stateset)
            geode.addDrawable(geometry)
            transform.addChild(geode)
            transform_group.addChild(transform)

    if needGroup :
        group = osg.Group()
        for(Cell.CellList.iterator itr=cell._cells.begin()
            not = cell._cells.end()
            ++itr)
            group.addChild(createTransformGraph(itr,stateset))

        if transform_group : group.addChild(transform_group)

    if group : return group
    else return transform_group

osg.Geometry* ForestTechniqueManager.createOrthogonalQuadsNoColor(  osg.Vec3 pos, float w, float h)
    # set up the coords
    v = *(osg.Vec3Array(8))
    t = *(osg.Vec2Array(8))

    rotation = random(0.0,osg.PI/2.0)
    sw = sinf(rotation)*w*0.5
    cw = cosf(rotation)*w*0.5

    v[0].set(pos.x()-sw,pos.y()-cw,pos.z()+0.0)
    v[1].set(pos.x()+sw,pos.y()+cw,pos.z()+0.0)
    v[2].set(pos.x()+sw,pos.y()+cw,pos.z()+h)
    v[3].set(pos.x()-sw,pos.y()-cw,pos.z()+h)

    v[4].set(pos.x()-cw,pos.y()+sw,pos.z()+0.0)
    v[5].set(pos.x()+cw,pos.y()-sw,pos.z()+0.0)
    v[6].set(pos.x()+cw,pos.y()-sw,pos.z()+h)
    v[7].set(pos.x()-cw,pos.y()+sw,pos.z()+h)

    t[0].set(0.0,0.0)
    t[1].set(1.0,0.0)
    t[2].set(1.0,1.0)
    t[3].set(0.0,1.0)

    t[4].set(0.0,0.0)
    t[5].set(1.0,0.0)
    t[6].set(1.0,1.0)
    t[7].set(0.0,1.0)

    geom = osg.Geometry()

    geom.setVertexArray( v )

    geom.setTexCoordArray( 0, t )

    geom.addPrimitiveSet( osg.DrawArrays(osg.PrimitiveSet.QUADS,0,8) )

    return geom

class ShaderGeometry (osg.Drawable) :
        ShaderGeometry()  setUseDisplayList(False) 

        #* Copy constructor using CopyOp to manage deep vs shallow copy.
        ShaderGeometry( ShaderGeometry ShaderGeometry, osg.CopyOp copyop=osg.CopyOp.SHALLOW_COPY):
            osg.Drawable(ShaderGeometry,copyop) 

        META_Object(osg,ShaderGeometry)

        typedef std.vector<osg.Vec4> PositionSizeList

        def drawImplementation(renderInfo):

            
            for(PositionSizeList.const_iterator itr = _trees.begin()
                not = _trees.end()
                ++itr)
                renderInfo.getState().Color((*itr)[0],(*itr)[1],(*itr)[2],(*itr)[3])
                _geometry.draw(renderInfo)

        def computeBound():

            
            geom_box = _geometry.getBound()
            bb = osg.BoundingBox()
            for(PositionSizeList.const_iterator itr = _trees.begin()
                not = _trees.end()
                ++itr)
                bb.expandBy(geom_box.corner(0)*(*itr)[3] +
                            osg.Vec3( (*itr)[0], (*itr)[1], (*itr)[2] ))
                bb.expandBy(geom_box.corner(7)*(*itr)[3] +
                            osg.Vec3( (*itr)[0], (*itr)[1], (*itr)[2] ))
            return bb

        def setGeometry(geometry):

            
            _geometry = geometry

        def addTree(tree):

            
            _trees.push_back(osg.Vec4(tree._position.x(), tree._position.y(), tree._position.z(), tree._height))

        _geometry = osg.Geometry()

        _trees = PositionSizeList()

        virtual ~ShaderGeometry() 



shared_geometry = 0

def createGeometryShader():

    
    static  char* vertSource = 
    "#version 120\n"
    "#extension GL_EXT_geometry_shader4 : enable\n"
    "varying vec2 texcoord\n"
    "void main(void)\n"
    "\n"
    "    gl_Position = gl_Vertex\n"
    "    texcoord = gl_MultiTexCoord0.st\n"
    "\n"
    

    static  char* geomSource = 
    "#version 120\n"
    "#extension GL_EXT_geometry_shader4 : enable\n"
    "varying vec2 texcoord\n"
    "varying float intensity \n"
    "varying float red_intensity \n"
    "void main(void)\n"
    "\n"
    "    vec4 v = gl_PositionIn[0]\n"
    "    vec4 info = gl_PositionIn[1]\n"
    "    intensity = info.y\n"
    "    red_intensity = info.z\n"
    "\n"
    "    float h = info.x\n"
    "    float w = h*0.35\n"
    "    vec4 e\n"
    "    e = v + vec4(-w,0.0,0.0,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e texcoord = vec2(0.0,0.0) EmitVertex()\n"
    "    e = v + vec4(w,0.0,0.0,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e  texcoord = vec2(1.0,0.0) EmitVertex()\n"
    "    e = v + vec4(-w,0.0,h,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e  texcoord = vec2(0.0,1.0) EmitVertex()\n"
    "    e = v + vec4(w,0.0,h,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e  texcoord = vec2(1.0,1.0) EmitVertex()\n"
    "    EndPrimitive()\n"
    "    e = v + vec4(0.0,-w,0.0,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e texcoord = vec2(0.0,0.0) EmitVertex()\n"
    "    e = v + vec4(0.0,w,0.0,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e  texcoord = vec2(1.0,0.0) EmitVertex()\n"
    "    e = v + vec4(0.0,-w,h,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e  texcoord = vec2(0.0,1.0) EmitVertex()\n"
    "    e = v + vec4(0.0,w,h,0.0)  gl_Position = gl_ModelViewProjectionMatrix * e  texcoord = vec2(1.0,1.0) EmitVertex()\n"
    "    EndPrimitive()\n"
    "\n"
    


    static  char* fragSource = 
        "uniform sampler2D baseTexture \n"
        "varying vec2 texcoord \n"
        "varying float intensity \n"
        "varying float red_intensity \n"
        "\n"
        "void main(void) \n"
        " \n"
        "   vec4 finalColor = texture2D( baseTexture, texcoord) \n"
        "   vec4 color = finalColor * intensity\n"
        "   color.w = finalColor.w\n"
        "   color.x *= red_intensity\n"
        "   gl_FragColor = color\n"
        "\n"
    


    pgm = osg.Program()
    pgm.setName( "osgshader2 demo" )

    pgm.addShader( osg.Shader( osg.Shader.VERTEX,   vertSource ) )
    pgm.addShader( osg.Shader( osg.Shader.FRAGMENT, fragSource ) )

    pgm.addShader( osg.Shader( osg.Shader.GEOMETRY, geomSource ) )
    pgm.setParameter( GL_GEOMETRY_VERTICES_OUT_EXT, 8 )
    pgm.setParameter( GL_GEOMETRY_INPUT_TYPE_EXT, GL_LINES )
    pgm.setParameter( GL_GEOMETRY_OUTPUT_TYPE_EXT, GL_TRIANGLE_STRIP)

    return pgm

void ForestTechniqueManager.CollectTreePositions(Cell* cell, std.vector< osg.Vec3 > positions)
    needGroup = not (cell._cells.empty())
    needTrees = not (cell._trees.empty())

    if needTrees :
        for(TreeList.iterator itr=cell._trees.begin()
            not = cell._trees.end()
            ++itr)
            tree = **itr
            positions.push_back(tree._position)

    if needGroup :
        for(Cell.CellList.iterator itr=cell._cells.begin()
            not = cell._cells.end()
            ++itr)
            CollectTreePositions(itr,positions)


osg.Node* ForestTechniqueManager.createGeometryShaderGraph(Cell* cell, osg.StateSet* dstate)
    needGroup = not (cell._cells.empty())
    needTrees = not (cell._trees.empty())

    geode = 0
    group = 0

    if needTrees :
        geode = osg.Geode()
        geode.setStateSet(dstate)

        geometry = osg.Geometry()
        geode.addDrawable(geometry)

        v = osg.Vec3Array()

        for(TreeList.iterator itr=cell._trees.begin()
            not = cell._trees.end()
            ++itr)
            tree = **itr
            v.push_back(tree._position)
            v.push_back(osg.Vec3(#tree._height30.0,(double)random(0.75,1.15),(double)random(1.0,1.250)))
        geometry.setVertexArray( v )
        geometry.addPrimitiveSet( osg.DrawArrays( GL_LINES, 0, v.size() ) )

        sset = geode.getOrCreateStateSet()
        sset.setMode( GL_LIGHTING, osg.StateAttribute.OFF )
        sset.setAttribute( createGeometryShader() )

        baseTextureSampler = osg.Uniform("baseTexture",0)
        sset.addUniform(baseTextureSampler)


    if needGroup :
        group = osg.Group()
        for(Cell.CellList.iterator itr=cell._cells.begin()
            not = cell._cells.end()
            ++itr)
            group.addChild(createGeometryShaderGraph(itr,dstate))

        if geode : group.addChild(geode)

    if group : return group
    else return geode

osg.Node* ForestTechniqueManager.createTextureBufferGraph(Cell* cell, osg.Geometry* templateGeometry)
    needGroup = not (cell._cells.empty())
    needTrees = not (cell._trees.empty())

    geode = 0
    group = 0

    if needTrees :
        geometry = (osg.Geometry*)templateGeometry.clone( osg.CopyOp.DEEP_COPY_PRIMITIVES )
        primSet = dynamic_cast<osg.DrawArrays*>( geometry.getPrimitiveSet(0) )
        primSet.setNumInstances( cell._trees.size() )
        geode = osg.Geode()
        geode.addDrawable(geometry)

        treeParamsImage = osg.Image()
        treeParamsImage.allocateImage( 3*cell._trees.size(), 1, 1, GL_RGBA, GL_FLOAT )

        i = 0
        for(TreeList.iterator itr=cell._trees.begin()
            not = cell._trees.end()
            ++itr,++i)
            ptr = (osg.Vec4f*)treeParamsImage.data(3*i)
            tree = **itr
            ptr[0] = osg.Vec4f(tree._position.x(),tree._position.y(),tree._position.z(),1.0)
            ptr[1] = osg.Vec4f((float)tree._color.r()/255.0,(float)tree._color.g()/255.0, (float)tree._color.b()/255.0, 1.0)
            ptr[2] = osg.Vec4f(tree._width, tree._height, 1.0, 1.0)
        tbo = osg.TextureBuffer()
        tbo.setImage( treeParamsImage )
        tbo.setInternalFormat(GL_RGBA32F_ARB)
        geometry.getOrCreateStateSet().setTextureAttribute(1, tbo)
        geometry.setInitialBound( cell._bb )

    if needGroup :
        group = osg.Group()
        for(Cell.CellList.iterator itr=cell._cells.begin()
            not = cell._cells.end()
            ++itr)
            group.addChild(createTextureBufferGraph(itr,templateGeometry))

        if geode : group.addChild(geode)

    if group : return group
    else return geode


osg.Node* ForestTechniqueManager.createShaderGraph(Cell* cell,osg.StateSet* stateset)
    if shared_geometry==0 :
        shared_geometry = createOrthogonalQuadsNoColor(osg.Vec3(0.0,0.0,0.0),1.0,1.0)
        #shared_geometry.setUseDisplayList(False)


    needGroup = not (cell._cells.empty())
    needTrees = not (cell._trees.empty())

    geode = 0
    group = 0

    if needTrees :
        geode = osg.Geode()

        shader_geometry = ShaderGeometry()
        shader_geometry.setGeometry(shared_geometry)


        for(TreeList.iterator itr=cell._trees.begin()
            not = cell._trees.end()
            ++itr)
            tree = **itr
            shader_geometry.addTree(tree)


        geode.setStateSet(stateset)
        geode.addDrawable(shader_geometry)

    if needGroup :
        group = osg.Group()
        for(Cell.CellList.iterator itr=cell._cells.begin()
            not = cell._cells.end()
            ++itr)
            group.addChild(createShaderGraph(itr,stateset))

        if geode : group.addChild(geode)

    if group : return group
    else return geode

osg.Node* ForestTechniqueManager.createHUDWithText( str str)
    geode = osg.Geode()

    timesFont = str("fonts/arial.ttf")

    # turn lighting off for the text and disable depth test to ensure its always ontop.
    stateset = geode.getOrCreateStateSet()
    stateset.setMode(GL_LIGHTING,osg.StateAttribute.OFF)

    # or disable depth test, and make sure that the hud is drawn after everything
    # else so that it always appears ontop.
    stateset.setMode(GL_DEPTH_TEST,osg.StateAttribute.OFF)
    stateset.setRenderBinDetails(11,"RenderBin")

    position = osg.Vec3(150.0,800.0,0.0)
    delta = osg.Vec3(0.0,-120.0,0.0)

        text = osgText.Text()
        geode.addDrawable( text )

        text.setFont(timesFont)
        text.setPosition(position)
        text.setText(str)

        position += delta


    # create the hud.
    modelview_abs = osg.MatrixTransform()
    modelview_abs.setReferenceFrame(osg.Transform.ABSOLUTE_RF)
    modelview_abs.setMatrix(osg.Matrix.identity())
    modelview_abs.addChild(geode)

    projection = osg.Projection()
    projection.setMatrix(osg.Matrix.ortho2D(0,1280,0,1024))
    projection.addChild(modelview_abs)

    return projection

osg.Node* ForestTechniqueManager.createScene(unsigned int numTreesToCreates, unsigned int maxNumTreesPerCell)
    origin = osg.Vec3(0.0,0.0,0.0)
    size = osg.Vec3(1000.0,1000.0,200.0)

    print "Creating terrain..."
    terrain = createTerrain(origin,size)
    print "done."

    print "Creating tree locations..."std.cout.flush()
    trees = TreeList()
    createTreeList(terrain,origin,size,numTreesToCreates,trees)
    print "done."

    print "Creating cell subdivision..."
    cell = Cell()
    cell.addTrees(trees)
    cell.divide(maxNumTreesPerCell)
    print "done."


    tex = osg.Texture2D()
    tex.setWrap( osg.Texture2D.WRAP_S, osg.Texture2D.CLAMP )
    tex.setWrap( osg.Texture2D.WRAP_T, osg.Texture2D.CLAMP )
    tex.setImage(osgDB.readImageFile("Images/tree0.rgba"))

    dstate = osg.StateSet()
        dstate.setTextureAttributeAndModes(0, tex, osg.StateAttribute.ON )

        dstate.setTextureAttribute(0, osg.TexEnv )()

        dstate.setAttributeAndModes( osg.BlendFunc, osg.StateAttribute.ON )()

        alphaFunc = osg.AlphaFunc()
        alphaFunc.setFunction(osg.AlphaFunc.GEQUAL,0.05)
        dstate.setAttributeAndModes( alphaFunc, osg.StateAttribute.ON )

        dstate.setMode( GL_LIGHTING, osg.StateAttribute.OFF )

        dstate.setRenderingHint( osg.StateSet.TRANSPARENT_BIN )


    _techniqueSwitch = osg.Switch()

        print "Creating osg.Billboard based forest..."
        group = osg.Group()
        group.addChild(createBillboardGraph(cell,dstate))
        group.addChild(createHUDWithText("Using osg.Billboard's to create a forest\n\nPress left cursor key to select geometry instancing with Texture Buffer Object\nPress right cursor key to select double quad based forest"))
        _techniqueSwitch.addChild(group)
        print "done."

        print "Creating double quad based forest..."
        group = osg.Group()
        group.addChild(createXGraph(cell,dstate))
        group.addChild(createHUDWithText("Using double quads to create a forest\n\nPress left cursor key to select osg.Billboard based forest\nPress right cursor key to select osg.MatrixTransform based forest\n"))
        _techniqueSwitch.addChild(group)
        print "done."

        print "Creating osg.MatrixTransform based forest..."
        group = osg.Group()
        group.addChild(createTransformGraph(cell,dstate))
        group.addChild(createHUDWithText("Using osg.MatrixTransform's to create a forest\n\nPress left cursor key to select double quad based forest\nPress right cursor key to select osg.Vertex/FragmentProgram based forest"))
        _techniqueSwitch.addChild(group)
        print "done."

        print "Creating osg.Vertex/FragmentProgram based forest..."
        group = osg.Group()

        stateset = osg.StateSet(*dstate, osg.CopyOp.DEEP_COPY_ALL)

            # vertex program
            vp_oss = std.ostringstream()
            vp_oss, " not  not ARBvp1.0\n"

                "ATTRIB vpos = vertex.position\n"
                "ATTRIB vcol = vertex.color\n"
                "ATTRIB tc = vertex.texcoord[", 0, "]"

                "PARAM mvp[4] =  state.matrix.mvp \n"
                "PARAM one =  1.0, 1.0, 1.0, 1.0 "

                "TEMP position\n"

                # vec3 position = gl_Vertex.xyz * gl_Color.w + gl_Color.xyz
                "MAD position, vpos, vcol.w, vcol\n"

                # gl_Position     = gl_ModelViewProjectionMatrix * vec4(position,1.0)
                "MOV position.w, one\n"
                "DP4 result.position.x, mvp[0], position\n"
                "DP4 result.position.y, mvp[1], position\n"
                "DP4 result.position.z, mvp[2], position\n"
                "DP4 result.position.w, mvp[3], position\n"

                # gl_FrontColor = vec4(1.0,1.0,1.0,1.0)
                "MOV result.color.front.primary, one\n"

                # texcoord = gl_MultiTexCoord0.st
                "MOV result.texcoord, tc\n"
                "END\n"


            # fragment program
            fp_oss = std.ostringstream()
            fp_oss, " not  not ARBfp1.0\n"
                "TEX result.color, fragment.texcoord[", 0, "], texture[", 0, "], 2D"
                "END\n"

            vp = osg.VertexProgram()
            vp.setVertexProgram(vp_oss.str())
            stateset.setAttributeAndModes(vp, osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)

            fp = osg.FragmentProgram()
            fp.setFragmentProgram(fp_oss.str())
            stateset.setAttributeAndModes(fp, osg.StateAttribute.OVERRIDE|osg.StateAttribute.ON)

        group.addChild(createShaderGraph(cell,stateset))
        group.addChild(createHUDWithText("Using osg.Vertex/FragmentProgram to create a forest\n\nPress left cursor key to select osg.MatrixTransform's based forest\nPress right cursor key to select OpenGL shader based forest"))
        _techniqueSwitch.addChild(group)
        print "done."

        print "Creating OpenGL shader based forest..."
        group = osg.Group()

        stateset = osg.StateSet(*dstate, osg.CopyOp.DEEP_COPY_ALL)

            program = osg.Program()
            stateset.setAttribute(program)

#if 1
            # use inline shaders

            #################################/
            # vertex shader using just Vec4 coefficients
            char vertexShaderSource[] =
                "varying vec2 texcoord\n"
                "\n"
                "void main(void)\n"
                "\n"
                "    vec3 position = gl_Vertex.xyz * gl_Color.w + gl_Color.xyz\n"
                "    gl_Position     = gl_ModelViewProjectionMatrix * vec4(position,1.0)\n"
                "    gl_FrontColor = vec4(1.0,1.0,1.0,1.0)\n"
                "    texcoord = gl_MultiTexCoord0.st\n"
                "\n"

            #################################
            # fragment shader
            #
            char fragmentShaderSource[] =
                "uniform sampler2D baseTexture \n"
                "varying vec2 texcoord \n"
                "\n"
                "void main(void) \n"
                " \n"
                "    gl_FragColor = texture2D( baseTexture, texcoord) \n"
                "\n"

            vertex_shader = osg.Shader(osg.Shader.VERTEX, vertexShaderSource)
            program.addShader(vertex_shader)

            fragment_shader = osg.Shader(osg.Shader.FRAGMENT, fragmentShaderSource)
            program.addShader(fragment_shader)

#else:

            # get shaders from source
            program.addShader(osg.Shader.readShaderFile(osg.Shader.VERTEX, osgDB.findDataFile("shaders/forest.vert")))
            program.addShader(osg.Shader.readShaderFile(osg.Shader.FRAGMENT, osgDB.findDataFile("shaders/forest.frag")))

#endif

            baseTextureSampler = osg.Uniform("baseTexture",0)
            stateset.addUniform(baseTextureSampler)

        group.addChild(createShaderGraph(cell,stateset))
        group.addChild(createHUDWithText("Using OpenGL Shader to create a forest\n\nPress left cursor key to select osg.Vertex/FragmentProgram based forest\nPress right cursor key to select osg.Vertex/Geometry/FragmentProgram based forest"))
        _techniqueSwitch.addChild(group)
        print "done."

        print "Creating Geometry Shader based forest..."

        stateset = osg.StateSet(*dstate, osg.CopyOp.DEEP_COPY_ALL)

        group = osg.Group()
        group.addChild(createGeometryShaderGraph(cell, stateset))
        group.addChild(createHUDWithText("Using osg.Vertex/Geometry/FragmentProgram to create a forest\n\nPress left cursor key to select OpenGL Shader based forest\nPress right cursor key to select geometry instancing with Texture Buffer Object"))

        _techniqueSwitch.addChild(group)
        print "done."

        print "Creating forest using geometry instancing and texture buffer objects ..."

        stateset = osg.StateSet(*dstate, osg.CopyOp.DEEP_COPY_ALL)
            program = osg.Program()
            stateset.setAttribute(program)

            char vertexShaderSource[] =
                "#version 420 compatibility\n"
                "uniform samplerBuffer dataBuffer\n"
                "layout(location = 0) in vec3 VertexPosition\n"
                "layout(location = 8) in vec3 VertexTexCoord\n"
                "out vec2 TexCoord\n"
                "out vec4 Color\n"
                "void main()\n"
                "\n"
                "   int instanceAddress = gl_InstanceID * 3\n"
                "   vec3 position = texelFetch(dataBuffer, instanceAddress).xyz\n"
                "   Color         = texelFetch(dataBuffer, instanceAddress + 1)\n"
                "   vec2 size     = texelFetch(dataBuffer, instanceAddress + 2).xy\n"
                "   mat4 mvpMatrix = gl_ModelViewProjectionMatrix *\n"
                "        mat4( size.x, 0.0, 0.0, 0.0,\n"
                "              0.0, size.x, 0.0, 0.0,\n"
                "              0.0, 0.0, size.y, 0.0,\n"
                "              position.x, position.y, position.z, 1.0)\n"
                "   gl_Position = mvpMatrix * vec4(VertexPosition,1.0) \n"
                "   TexCoord = VertexTexCoord.xy\n"
                "\n"

            char fragmentShaderSource[] =
                "#version 420 core\n"
                "uniform sampler2D baseTexture \n"
                "in vec2 TexCoord\n"
                "in vec4 Color\n"
                "layout(location = 0, index = 0) out vec4 FragData0\n"
                "void main(void) \n"
                "\n"
                "    FragData0 = Color*texture(baseTexture, TexCoord)\n"
                "\n"

            vertex_shader = osg.Shader(osg.Shader.VERTEX, vertexShaderSource)
            program.addShader(vertex_shader)

            fragment_shader = osg.Shader(osg.Shader.FRAGMENT, fragmentShaderSource)
            program.addShader(fragment_shader)

            baseTextureSampler = osg.Uniform("baseTexture",0)
            stateset.addUniform(baseTextureSampler)

            dataBufferSampler = osg.Uniform("dataBuffer",1)
            stateset.addUniform(dataBufferSampler)

        templateGeometry = createOrthogonalQuadsNoColor(osg.Vec3(0.0,0.0,0.0),1.0,1.0)
        templateGeometry.setUseVertexBufferObjects(True)
        templateGeometry.setUseDisplayList(False)
        textureBufferGraph = createTextureBufferGraph(cell, templateGeometry)
        textureBufferGraph.setStateSet( stateset )
        group = osg.Group()
        group.addChild(textureBufferGraph)
        group.addChild(createHUDWithText("Using geometry instancing to create a forest\n\nPress left cursor key to select osg.Vertex/Geometry/FragmentProgram based forest\nPress right cursor key to select osg.Billboard based forest"))

        _techniqueSwitch.addChild(group)

        print "done."


    _currentTechnique = 0
    _techniqueSwitch.setSingleChildOn(_currentTechnique)


    scene = osg.Group()

    scene.addChild(terrain)
    scene.addChild(_techniqueSwitch)

    return scene

def main(argv):

    

    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argv)

    # construct the viewer.
    viewer = osgViewer.Viewer(arguments)

    numTreesToCreate = 10000
    arguments.read("--trees",numTreesToCreate)

    maxNumTreesPerCell = sqrtf(static_cast<float>(numTreesToCreate))

    arguments.read("--trees-per-cell",maxNumTreesPerCell)

    ttm = ForestTechniqueManager()

    # add the stats handler
    viewer.addEventHandler(osgViewer.StatsHandler)()

    viewer.addEventHandler(TechniqueEventHandler(ttm))
    viewer.addEventHandler(osgGA.StateSetManipulator(viewer.getCamera().getOrCreateStateSet()))

    # add model to viewer.
    viewer.setSceneData( ttm.createScene(numTreesToCreate, maxNumTreesPerCell) )


    return viewer.run()


if __name__ == "__main__":
    main(sys.argv)
