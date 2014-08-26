#include "../default.h"

// Headers needed for osgUtil classes to compile
#include <osg/CoordinateSystemNode>
#include <osg/ClipNode>
#include <osg/TexGenNode>
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

// TODO - wrap more classes
#include <osgUtil/UpdateVisitor>
#include <osgUtil/IncrementalCompileOperation>
#include <osgUtil/SceneView>
#include <osgUtil/Optimizer>
#include <osgUtil/Version>

template class ::std::vector< std::pair<osg::ref_ptr<osg::StateAttribute const>, osg::ref_ptr<osg::RefMatrixd> > >;

namespace pyplusplus { namespace aliases {
    typedef ::std::vector< std::pair<osg::ref_ptr<osg::StateAttribute const>, osg::ref_ptr<osg::RefMatrixd> > > std_vector_pair_StateAttribute_RefMatrixd;
}}
