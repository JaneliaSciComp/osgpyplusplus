// This file has been generated by Py++.

#include "boost/python.hpp"
#include "indexing_suite/container_suite.hpp"
#include "indexing_suite/map.hpp"
#include "wrap_osgdb.h"
#include "map_less__std_scope_string_comma__std_scope_string__greater_.pypp.hpp"

namespace bp = boost::python;

void register_map_less__std_scope_string_comma__std_scope_string__greater__class(){

    bp::class_< std::map< std::string, std::string > >( "map_less__std_scope_string_comma__std_scope_string__greater_" )    
        .def( bp::indexing::map_suite< std::map< std::string, std::string > >() );

}