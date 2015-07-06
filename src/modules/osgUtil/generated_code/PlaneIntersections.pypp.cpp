// This file has been generated by Py++.

#include "boost/python.hpp"
#include "indexing_suite/container_suite.hpp"
#include "indexing_suite/vector.hpp"
#include "wrap_osgutil.h"
#include "_PlaneIntersection__value_traits.pypp.hpp"
#include "planeintersections.pypp.hpp"

namespace bp = boost::python;

void register_PlaneIntersections_class(){

    { //::std::vector< osgUtil::PlaneIntersector::Intersection >
        typedef bp::class_< std::vector< osgUtil::PlaneIntersector::Intersection > > PlaneIntersections_exposer_t;
        PlaneIntersections_exposer_t PlaneIntersections_exposer = PlaneIntersections_exposer_t( "PlaneIntersections" );
        bp::scope PlaneIntersections_scope( PlaneIntersections_exposer );
        PlaneIntersections_exposer.def( bp::indexing::vector_suite< std::vector< osgUtil::PlaneIntersector::Intersection > >() );
    }

}
