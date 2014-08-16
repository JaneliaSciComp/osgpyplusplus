// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "vertexattribalias.pypp.hpp"

namespace bp = boost::python;

void register_VertexAttribAlias_class(){

    bp::class_< osg::VertexAttribAlias >( "VertexAttribAlias", bp::init< >() )    
        .def( bp::init< osg::VertexAttribAlias const & >(( bp::arg("rhs") )) )    
        .def( bp::init< GLuint, std::string, std::string, std::string const & >(( bp::arg("location"), bp::arg("glName"), bp::arg("osgName"), bp::arg("declaration") )) )    
        .def_readwrite( "_declaration", &osg::VertexAttribAlias::_declaration )    
        .def_readwrite( "_glName", &osg::VertexAttribAlias::_glName )    
        .def_readwrite( "_location", &osg::VertexAttribAlias::_location )    
        .def_readwrite( "_osgName", &osg::VertexAttribAlias::_osgName );

}
