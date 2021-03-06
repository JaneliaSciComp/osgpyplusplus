// This file has been generated by Py++.

#include "boost/python.hpp"
#include "indexing_suite/container_suite.hpp"
#include "indexing_suite/map.hpp"
#include "wrap_osg.h"
#include "_FrameBufferAttachment__value_traits.pypp.hpp"
#include "attachmentmap.pypp.hpp"

namespace bp = boost::python;

void register_AttachmentMap_class(){

    bp::class_< std::map< osg::Camera::BufferComponent, osg::FrameBufferAttachment > >( "AttachmentMap" )    
        .def( bp::indexing::map_suite< std::map< osg::Camera::BufferComponent, osg::FrameBufferAttachment > >() );

}
