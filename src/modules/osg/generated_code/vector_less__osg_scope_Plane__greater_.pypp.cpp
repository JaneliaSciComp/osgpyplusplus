// This file has been generated by Py++.

#include "boost/python.hpp"
#include "boost/python/suite/indexing/vector_indexing_suite.hpp"
#include "wrap_osg.h"
#include "vector_less__osg_scope_plane__greater_.pypp.hpp"

namespace bp = boost::python;

void register_vector_less__osg_scope_Plane__greater__class(){

    { //::std::vector< osg::Plane >
        typedef bp::class_< std::vector< osg::Plane > > vector_less__osg_scope_Plane__greater__exposer_t;
        vector_less__osg_scope_Plane__greater__exposer_t vector_less__osg_scope_Plane__greater__exposer = vector_less__osg_scope_Plane__greater__exposer_t( "vector_less__osg_scope_Plane__greater_" );
        bp::scope vector_less__osg_scope_Plane__greater__scope( vector_less__osg_scope_Plane__greater__exposer );
        vector_less__osg_scope_Plane__greater__exposer.def( bp::vector_indexing_suite< ::std::vector< osg::Plane > >() );
    }

}
