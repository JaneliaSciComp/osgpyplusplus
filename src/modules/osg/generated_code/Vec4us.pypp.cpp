// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "vec4us.pypp.hpp"

namespace bp = boost::python;

void register_Vec4us_class(){

    { //::osg::Vec4us
        typedef bp::class_< osg::Vec4us > Vec4us_exposer_t;
        Vec4us_exposer_t Vec4us_exposer = Vec4us_exposer_t( "Vec4us", bp::init< >() );
        bp::scope Vec4us_scope( Vec4us_exposer );
        bp::scope().attr("num_components") = (int)osg::Vec4us::num_components;
        Vec4us_exposer.def( bp::init< short unsigned int, short unsigned int, short unsigned int, short unsigned int >(( bp::arg("x"), bp::arg("y"), bp::arg("z"), bp::arg("w") )) );
        { //::osg::Vec4us::a
        
            typedef short unsigned int & ( ::osg::Vec4us::*a_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "a"
                , a_function_type( &::osg::Vec4us::a )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::a
        
            typedef short unsigned int ( ::osg::Vec4us::*a_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "a"
                , a_function_type( &::osg::Vec4us::a ) );
        
        }
        { //::osg::Vec4us::b
        
            typedef short unsigned int & ( ::osg::Vec4us::*b_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "b"
                , b_function_type( &::osg::Vec4us::b )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::b
        
            typedef short unsigned int ( ::osg::Vec4us::*b_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "b"
                , b_function_type( &::osg::Vec4us::b ) );
        
        }
        { //::osg::Vec4us::g
        
            typedef short unsigned int & ( ::osg::Vec4us::*g_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "g"
                , g_function_type( &::osg::Vec4us::g )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::g
        
            typedef short unsigned int ( ::osg::Vec4us::*g_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "g"
                , g_function_type( &::osg::Vec4us::g ) );
        
        }
        Vec4us_exposer.def( bp::self != bp::self );
        Vec4us_exposer.def( bp::self * bp::other< short unsigned int >() );
        Vec4us_exposer.def( bp::self * bp::self );
        Vec4us_exposer.def( bp::self *= bp::other< short unsigned int >() );
        Vec4us_exposer.def( bp::self + bp::self );
        Vec4us_exposer.def( bp::self += bp::self );
        Vec4us_exposer.def( bp::self - bp::self );
        Vec4us_exposer.def( bp::self -= bp::self );
        Vec4us_exposer.def( bp::self / bp::other< short unsigned int >() );
        Vec4us_exposer.def( bp::self /= bp::other< short unsigned int >() );
        Vec4us_exposer.def( bp::self < bp::self );
        Vec4us_exposer.def( bp::self == bp::self );
        { //::osg::Vec4us::operator[]
        
            typedef short unsigned int & ( ::osg::Vec4us::*__getitem___function_type)( unsigned int ) ;
            
            Vec4us_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec4us::operator[] )
                , ( bp::arg("i") )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::operator[]
        
            typedef short unsigned int ( ::osg::Vec4us::*__getitem___function_type)( unsigned int ) const;
            
            Vec4us_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec4us::operator[] )
                , ( bp::arg("i") ) );
        
        }
        { //::osg::Vec4us::r
        
            typedef short unsigned int & ( ::osg::Vec4us::*r_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "r"
                , r_function_type( &::osg::Vec4us::r )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::r
        
            typedef short unsigned int ( ::osg::Vec4us::*r_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "r"
                , r_function_type( &::osg::Vec4us::r ) );
        
        }
        { //::osg::Vec4us::set
        
            typedef void ( ::osg::Vec4us::*set_function_type)( short unsigned int,short unsigned int,short unsigned int,short unsigned int ) ;
            
            Vec4us_exposer.def( 
                "set"
                , set_function_type( &::osg::Vec4us::set )
                , ( bp::arg("x"), bp::arg("y"), bp::arg("z"), bp::arg("w") ) );
        
        }
        { //::osg::Vec4us::w
        
            typedef short unsigned int & ( ::osg::Vec4us::*w_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "w"
                , w_function_type( &::osg::Vec4us::w )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::w
        
            typedef short unsigned int ( ::osg::Vec4us::*w_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "w"
                , w_function_type( &::osg::Vec4us::w ) );
        
        }
        { //::osg::Vec4us::x
        
            typedef short unsigned int & ( ::osg::Vec4us::*x_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "x"
                , x_function_type( &::osg::Vec4us::x )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::x
        
            typedef short unsigned int ( ::osg::Vec4us::*x_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "x"
                , x_function_type( &::osg::Vec4us::x ) );
        
        }
        { //::osg::Vec4us::y
        
            typedef short unsigned int & ( ::osg::Vec4us::*y_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "y"
                , y_function_type( &::osg::Vec4us::y )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::y
        
            typedef short unsigned int ( ::osg::Vec4us::*y_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "y"
                , y_function_type( &::osg::Vec4us::y ) );
        
        }
        { //::osg::Vec4us::z
        
            typedef short unsigned int & ( ::osg::Vec4us::*z_function_type)(  ) ;
            
            Vec4us_exposer.def( 
                "z"
                , z_function_type( &::osg::Vec4us::z )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec4us::z
        
            typedef short unsigned int ( ::osg::Vec4us::*z_function_type)(  ) const;
            
            Vec4us_exposer.def( 
                "z"
                , z_function_type( &::osg::Vec4us::z ) );
        
        }
    }

}
