// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osganimation.h"
#include "inoutbackfunction.pypp.hpp"

namespace bp = boost::python;

void register_InOutBackFunction_class(){

    bp::class_< osgAnimation::InOutBackFunction >( "InOutBackFunction" )    
        .def( 
            "getValueAt"
            , (void (*)( float,float & ))( &::osgAnimation::InOutBackFunction::getValueAt )
            , ( bp::arg("t"), bp::arg("result") ) )    
        .staticmethod( "getValueAt" );

}
