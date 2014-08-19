// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgdb.h"
#include "osgdb_enumerations.pypp.hpp"

namespace bp = boost::python;

void register_enumerations(){

    bp::enum_< osgDB::CaseSensitivity>("CaseSensitivity")
        .value("CASE_SENSITIVE", osgDB::CASE_SENSITIVE)
        .value("CASE_INSENSITIVE", osgDB::CASE_INSENSITIVE)
        .export_values()
        ;

}