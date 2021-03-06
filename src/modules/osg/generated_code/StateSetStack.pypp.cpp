// This file has been generated by Py++.

#include "boost/python.hpp"
#include "indexing_suite/container_suite.hpp"
#include "indexing_suite/vector.hpp"
#include "wrap_osg.h"
#include "statesetstack.pypp.hpp"

namespace bp = boost::python;

void register_StateSetStack_class(){

    { //::std::vector< osg::StateSet const* >
        typedef bp::class_< std::vector< osg::StateSet const* > > StateSetStack_exposer_t;
        StateSetStack_exposer_t StateSetStack_exposer = StateSetStack_exposer_t( "StateSetStack" );
        bp::scope StateSetStack_scope( StateSetStack_exposer );
        StateSetStack_exposer.def( bp::indexing::vector_suite< std::vector< osg::StateSet const* > >::with_policies(bp::return_internal_reference< >()) );
    }

}
