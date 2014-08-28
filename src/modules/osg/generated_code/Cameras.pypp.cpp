// This file has been generated by Py++.

#include "boost/python.hpp"
#include "indexing_suite/container_suite.hpp"
#include "indexing_suite/list.hpp"
#include "wrap_osg.h"
#include "cameras.pypp.hpp"

namespace bp = boost::python;

void register_Cameras_class(){

    { //::std::list< osg::Camera* >
        typedef bp::class_< std::list< osg::Camera* > > Cameras_exposer_t;
        Cameras_exposer_t Cameras_exposer = Cameras_exposer_t( "Cameras" );
        bp::scope Cameras_scope( Cameras_exposer );
        Cameras_exposer.def( bp::indexing::list_suite< std::list< osg::Camera* > >::with_policies(bp::return_internal_reference< >()) );
    }

}