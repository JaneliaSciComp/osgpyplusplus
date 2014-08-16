// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "observer_ptr_less__osg_scope_operationqueue__greater_.pypp.hpp"

namespace bp = boost::python;

void register_observer_ptr_less__osg_scope_OperationQueue__greater__class(){

    { //::osg::observer_ptr< osg::OperationQueue >
        typedef bp::class_< osg::observer_ptr< osg::OperationQueue > > observer_ptr_less__osg_scope_OperationQueue__greater__exposer_t;
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer_t observer_ptr_less__osg_scope_OperationQueue__greater__exposer = observer_ptr_less__osg_scope_OperationQueue__greater__exposer_t( "observer_ptr_less__osg_scope_OperationQueue__greater_", bp::init< >() );
        bp::scope observer_ptr_less__osg_scope_OperationQueue__greater__scope( observer_ptr_less__osg_scope_OperationQueue__greater__exposer );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::init< osg::ref_ptr< osg::OperationQueue > const & >(( bp::arg("rp") )) );
        bp::implicitly_convertible< osg::ref_ptr< osg::OperationQueue > const &, osg::observer_ptr< osg::OperationQueue > >();
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::init< osg::OperationQueue * >(( bp::arg("rp") )) );
        bp::implicitly_convertible< osg::OperationQueue *, osg::observer_ptr< osg::OperationQueue > >();
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::init< osg::observer_ptr< osg::OperationQueue > const & >(( bp::arg("wp") )) );
        { //::osg::observer_ptr< osg::OperationQueue >::get
        
            typedef osg::observer_ptr< osg::OperationQueue > exported_class_t;
            typedef ::osg::OperationQueue * ( exported_class_t::*get_function_type)(  ) const;
            
            observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( 
                "get"
                , get_function_type( &::osg::observer_ptr< osg::OperationQueue >::get )
                    /* undefined call policies */ );
        
        }
        { //::osg::observer_ptr< osg::OperationQueue >::lock
        
            typedef osg::observer_ptr< osg::OperationQueue > exported_class_t;
            typedef bool ( exported_class_t::*lock_function_type)( ::osg::ref_ptr< osg::OperationQueue > & ) const;
            
            observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( 
                "lock"
                , lock_function_type( &::osg::observer_ptr< osg::OperationQueue >::lock )
                , ( bp::arg("rptr") ) );
        
        }
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( !bp::self );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self != bp::self );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self != bp::other< osg::OperationQueue const * >() );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self < bp::self );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self < bp::other< osg::OperationQueue const * >() );
        { //::osg::observer_ptr< osg::OperationQueue >::operator=
        
            typedef osg::observer_ptr< osg::OperationQueue > exported_class_t;
            typedef ::osg::observer_ptr< osg::OperationQueue > & ( exported_class_t::*assign_function_type)( ::osg::observer_ptr< osg::OperationQueue > const & ) ;
            
            observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( 
                "assign"
                , assign_function_type( &::osg::observer_ptr< osg::OperationQueue >::operator= )
                , ( bp::arg("wp") )
                , bp::return_self< >() );
        
        }
        { //::osg::observer_ptr< osg::OperationQueue >::operator=
        
            typedef osg::observer_ptr< osg::OperationQueue > exported_class_t;
            typedef ::osg::observer_ptr< osg::OperationQueue > & ( exported_class_t::*assign_function_type)( ::osg::ref_ptr< osg::OperationQueue > const & ) ;
            
            observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( 
                "assign"
                , assign_function_type( &::osg::observer_ptr< osg::OperationQueue >::operator= )
                , ( bp::arg("rp") )
                , bp::return_self< >() );
        
        }
        { //::osg::observer_ptr< osg::OperationQueue >::operator=
        
            typedef osg::observer_ptr< osg::OperationQueue > exported_class_t;
            typedef ::osg::observer_ptr< osg::OperationQueue > & ( exported_class_t::*assign_function_type)( ::osg::OperationQueue * ) ;
            
            observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( 
                "assign"
                , assign_function_type( &::osg::observer_ptr< osg::OperationQueue >::operator= )
                , ( bp::arg("rp") )
                , bp::return_self< >() );
        
        }
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self == bp::self );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self == bp::other< osg::OperationQueue const * >() );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self > bp::self );
        observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( bp::self > bp::other< osg::OperationQueue const * >() );
        { //::osg::observer_ptr< osg::OperationQueue >::valid
        
            typedef osg::observer_ptr< osg::OperationQueue > exported_class_t;
            typedef bool ( exported_class_t::*valid_function_type)(  ) const;
            
            observer_ptr_less__osg_scope_OperationQueue__greater__exposer.def( 
                "valid"
                , valid_function_type( &::osg::observer_ptr< osg::OperationQueue >::valid ) );
        
        }
    }

}
