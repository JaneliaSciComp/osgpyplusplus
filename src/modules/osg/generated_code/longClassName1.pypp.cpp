// This file has been generated by Py++.

#include "boost/python.hpp"
#include "boost/python/suite/indexing/map_indexing_suite.hpp"
#include "wrap_osg.h"
#include "longclassname1.pypp.hpp"

namespace bp = boost::python;

void register_longClassName1_class(){

    bp::class_< std::map< std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > >( "longClassName1" )    
        .def( bp::map_indexing_suite< ::std::map< std::pair<osg::StateAttribute::Type, unsigned int>, std::pair<osg::ref_ptr<osg::StateAttribute>, unsigned int> > >() );

}