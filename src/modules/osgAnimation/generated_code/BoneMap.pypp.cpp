// This file has been generated by Py++.

#include "boost/python.hpp"
#include "indexing_suite/container_suite.hpp"
#include "indexing_suite/map.hpp"
#include "wrap_osganimation.h"
#include "_ref_ptr_less__osgAnimation_scope_Bone__greater___value_traits.pypp.hpp"
#include "bonemap.pypp.hpp"

namespace bp = boost::python;

void register_BoneMap_class(){

    bp::class_< std::map< std::string, osg::ref_ptr<osgAnimation::Bone> > >( "BoneMap" )    
        .def( bp::indexing::map_suite< std::map< std::string, osg::ref_ptr<osgAnimation::Bone> > >() );

}