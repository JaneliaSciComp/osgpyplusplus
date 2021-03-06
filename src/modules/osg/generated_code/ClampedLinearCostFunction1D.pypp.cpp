// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "clampedlinearcostfunction1d.pypp.hpp"

namespace bp = boost::python;

void register_ClampedLinearCostFunction1D_class(){

    { //::osg::ClampedLinearCostFunction1D
        typedef bp::class_< osg::ClampedLinearCostFunction1D > ClampedLinearCostFunction1D_exposer_t;
        ClampedLinearCostFunction1D_exposer_t ClampedLinearCostFunction1D_exposer = ClampedLinearCostFunction1D_exposer_t( "ClampedLinearCostFunction1D", bp::init< bp::optional< double, double, unsigned int > >(( bp::arg("cost0")=0.0, bp::arg("dcost_di")=0.0, bp::arg("min_input")=(unsigned int)(0) )) );
        bp::scope ClampedLinearCostFunction1D_scope( ClampedLinearCostFunction1D_exposer );
        bp::implicitly_convertible< double, osg::ClampedLinearCostFunction1D >();
        { //::osg::ClampedLinearCostFunction1D::operator()
        
            typedef double ( ::osg::ClampedLinearCostFunction1D::*__call___function_type)( unsigned int ) const;
            
            ClampedLinearCostFunction1D_exposer.def( 
                "__call__"
                , __call___function_type( &::osg::ClampedLinearCostFunction1D::operator() )
                , ( bp::arg("input") ) );
        
        }
        { //::osg::ClampedLinearCostFunction1D::set
        
            typedef void ( ::osg::ClampedLinearCostFunction1D::*set_function_type)( double,double,unsigned int ) ;
            
            ClampedLinearCostFunction1D_exposer.def( 
                "set"
                , set_function_type( &::osg::ClampedLinearCostFunction1D::set )
                , ( bp::arg("cost0"), bp::arg("dcost_di"), bp::arg("min_input") ) );
        
        }
        ClampedLinearCostFunction1D_exposer.def_readwrite( "_cost0", &osg::ClampedLinearCostFunction1D::_cost0 );
        ClampedLinearCostFunction1D_exposer.def_readwrite( "_dcost_di", &osg::ClampedLinearCostFunction1D::_dcost_di );
        ClampedLinearCostFunction1D_exposer.def_readwrite( "_min_input", &osg::ClampedLinearCostFunction1D::_min_input );
    }

}
