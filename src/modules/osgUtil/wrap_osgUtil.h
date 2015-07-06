#include "../default.h"

// Headers needed for osgUtil classes to compile
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

// TODO - wrap more classes
#include <osgUtil/CullVisitor>
#include <osgUtil/DisplayRequirementsVisitor>
#include <osgUtil/DrawElementTypeSimplifier>
#include <osgUtil/GLObjectsVisitor>
#include <osgUtil/IncrementalCompileOperation>
#include <osgUtil/IntersectionVisitor>
#include <osgUtil/IntersectVisitor>
#include <osgUtil/LineSegmentIntersector>
#include <osgUtil/Optimizer>
#include <osgUtil/PlaneIntersector>
#include <osgUtil/PolytopeIntersector>
#include <osgUtil/PrintVisitor>
#include <osgUtil/SceneView>
#include <osgUtil/ShaderGen>
#include <osgUtil/Simplifier>
#include <osgUtil/SmoothingVisitor>
#include <osgUtil/Statistics>
#include <osgUtil/TriStripVisitor>
#include <osgUtil/UpdateVisitor>
#include <osgUtil/Version>

template class ::std::vector< std::pair<osg::ref_ptr<osg::StateAttribute const>, osg::ref_ptr<osg::RefMatrixd> > >;

namespace pyplusplus { namespace aliases {
    typedef ::std::vector< std::pair<osg::ref_ptr<osg::StateAttribute const>, osg::ref_ptr<osg::RefMatrixd> > > std_vector_pair_StateAttribute_RefMatrixd;

    // Avoid duplicate aliases
    typedef osgUtil::PolytopeIntersector::Intersection PolytopeIntersection;
    typedef osgUtil::PlaneIntersector::Intersection PlaneIntersection;
    typedef osgUtil::PolytopeIntersector::Intersections PolytopeIntersections;
    typedef osgUtil::PlaneIntersector::Intersections PlaneIntersections;
}}
