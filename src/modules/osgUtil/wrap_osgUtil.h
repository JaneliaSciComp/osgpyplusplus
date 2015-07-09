/**
 * wrap_osgUtil.h
 *
 * C++ header shared by all source files used to build _osgUtil extension module in osgpyplusplus
 * OpenSceneGraph python API bindings.
 */

// Headers shared by all osgpyplusplus modules
#include "../default.h"

// External headers needed for osgUtil classes to compile
#include <osg/Array>
#include <osg/CoordinateSystemNode>
#include <osg/ClipNode>
#include <osg/CameraView>
#include <osg/PositionAttitudeTransform>
#include <osg/Sequence>
#include <osg/OcclusionQueryNode>
#include <osg/Billboard>
#include <osg/Geode>
#include <osg/LOD>
#include <osg/MatrixTransform>
#include <osg/PagedLOD>
#include <osg/ProxyNode>
#include <osg/TexGenNode>

// Full set of OSG 3.2.1 osgUtil headers
#include <osgUtil/ConvertVec>
#include <osgUtil/CubeMapGenerator>
#include <osgUtil/CullVisitor>
#include <osgUtil/DelaunayTriangulator>
#include <osgUtil/DisplayRequirementsVisitor>
#include <osgUtil/DrawElementTypeSimplifier>
#include <osgUtil/EdgeCollector>
#include <osgUtil/Export>
#include <osgUtil/GLObjectsVisitor>
#include <osgUtil/HalfWayMapGenerator>
#include <osgUtil/HighlightMapGenerator>
#include <osgUtil/IncrementalCompileOperation>
#include <osgUtil/IntersectionVisitor>
#include <osgUtil/IntersectVisitor>
#include <osgUtil/LineSegmentIntersector>
#include <osgUtil/MeshOptimizers>
#include <osgUtil/OperationArrayFunctor>
#include <osgUtil/Optimizer>
#include <osgUtil/PerlinNoise>
#include <osgUtil/PlaneIntersector>
#include <osgUtil/PolytopeIntersector>
#include <osgUtil/PositionalStateContainer>
#include <osgUtil/PrintVisitor>
#include <osgUtil/ReflectionMapGenerator>
#include <osgUtil/RenderBin>
#include <osgUtil/RenderLeaf>
#include <osgUtil/RenderStage>
#include <osgUtil/ReversePrimitiveFunctor>
#include <osgUtil/SceneGraphBuilder>
#include <osgUtil/SceneView>
#include <osgUtil/ShaderGen>
#include <osgUtil/Simplifier>
#include <osgUtil/SmoothingVisitor>
#include <osgUtil/StateGraph>
#include <osgUtil/Statistics>
#include <osgUtil/TangentSpaceGenerator>
#include <osgUtil/Tessellator>
#include <osgUtil/TransformAttributeFunctor>
#include <osgUtil/TransformCallback>
#include <osgUtil/TriStripVisitor>
#include <osgUtil/UpdateVisitor>
#include <osgUtil/Version>
/* */

// Avoid compile errors with insufficiently scoped templates
static int UIntArrayType = osg::Array::UIntArrayType; 

// Instantiate template classes that will be aliased farther down
template class ::std::vector< std::pair<osg::ref_ptr<osg::StateAttribute const>, osg::ref_ptr<osg::RefMatrixd> > >;
template class ::std::list< osg::ref_ptr<osg::TemplateIndexArray<unsigned int, osg::Array::UIntArrayType, 1, 5125> > >;

// Aliases defined within this block will influence the generated wrapper source file names for those classes
namespace pyplusplus { namespace aliases {
    // Shorten long alias names
    typedef ::std::vector< std::pair<osg::ref_ptr<osg::StateAttribute const>, osg::ref_ptr<osg::RefMatrixd> > > std_vector_pair_StateAttribute_RefMatrixd;
    typedef ::std::list< osg::ref_ptr<osg::TemplateIndexArray<unsigned int, osg::Array::UIntArrayType, 1, 5125> > > std_list_tiarray_uint_5125;

    // Avoid duplicate aliases
    typedef osgUtil::PolytopeIntersector::Intersection PolytopeIntersection;
    typedef osgUtil::PlaneIntersector::Intersection PlaneIntersection;
    typedef osgUtil::PolytopeIntersector::Intersections PolytopeIntersections;
    typedef osgUtil::PlaneIntersector::Intersections PlaneIntersections;
}}
