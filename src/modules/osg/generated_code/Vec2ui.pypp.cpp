// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "vec2ui.pypp.hpp"

namespace bp = boost::python;

void register_Vec2ui_class(){

    { //::osg::Vec2ui
        typedef bp::class_< osg::Vec2ui > Vec2ui_exposer_t;
        Vec2ui_exposer_t Vec2ui_exposer = Vec2ui_exposer_t( "Vec2ui", bp::init< >() );
        bp::scope Vec2ui_scope( Vec2ui_exposer );
        bp::scope().attr("num_components") = (int)osg::Vec2ui::num_components;
        Vec2ui_exposer.def( bp::init< unsigned int, unsigned int >(( bp::arg("x"), bp::arg("y") )) );
        { //::osg::Vec2ui::g
        
            typedef unsigned int & ( ::osg::Vec2ui::*g_function_type)(  ) ;
            
            Vec2ui_exposer.def( 
                "g"
                , g_function_type( &::osg::Vec2ui::g )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec2ui::g
        
            typedef unsigned int ( ::osg::Vec2ui::*g_function_type)(  ) const;
            
            Vec2ui_exposer.def( 
                "g"
                , g_function_type( &::osg::Vec2ui::g ) );
        
        }
        Vec2ui_exposer.def( bp::self != bp::self );
        Vec2ui_exposer.def( bp::self * bp::other< unsigned int >() );
        Vec2ui_exposer.def( bp::self * bp::self );
        Vec2ui_exposer.def( bp::self + bp::other< unsigned int >() );
        Vec2ui_exposer.def( bp::self + bp::self );
        Vec2ui_exposer.def( bp::self - bp::other< unsigned int >() );
        Vec2ui_exposer.def( bp::self - bp::self );
        Vec2ui_exposer.def( bp::self / bp::other< unsigned int >() );
        Vec2ui_exposer.def( bp::self < bp::self );
        Vec2ui_exposer.def( bp::self == bp::self );
        { //::osg::Vec2ui::operator[]
        
            typedef unsigned int & ( ::osg::Vec2ui::*__getitem___function_type)( int ) ;
            
            Vec2ui_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec2ui::operator[] )
                , ( bp::arg("i") )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec2ui::operator[]
        
            typedef unsigned int ( ::osg::Vec2ui::*__getitem___function_type)( int ) const;
            
            Vec2ui_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec2ui::operator[] )
                , ( bp::arg("i") ) );
        
        }
        { //::osg::Vec2ui::r
        
            typedef unsigned int & ( ::osg::Vec2ui::*r_function_type)(  ) ;
            
            Vec2ui_exposer.def( 
                "r"
                , r_function_type( &::osg::Vec2ui::r )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec2ui::r
        
            typedef unsigned int ( ::osg::Vec2ui::*r_function_type)(  ) const;
            
            Vec2ui_exposer.def( 
                "r"
                , r_function_type( &::osg::Vec2ui::r ) );
        
        }
        { //::osg::Vec2ui::set
        
            typedef void ( ::osg::Vec2ui::*set_function_type)( unsigned int,unsigned int ) ;
            
            Vec2ui_exposer.def( 
                "set"
                , set_function_type( &::osg::Vec2ui::set )
                , ( bp::arg("x"), bp::arg("y") ) );
        
        }
        { //::osg::Vec2ui::set
        
            typedef void ( ::osg::Vec2ui::*set_function_type)( ::osg::Vec2ui const & ) ;
            
            Vec2ui_exposer.def( 
                "set"
                , set_function_type( &::osg::Vec2ui::set )
                , ( bp::arg("rhs") ) );
        
        }
        { //::osg::Vec2ui::x
        
            typedef unsigned int & ( ::osg::Vec2ui::*x_function_type)(  ) ;
            
            Vec2ui_exposer.def( 
                "x"
                , x_function_type( &::osg::Vec2ui::x )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec2ui::x
        
            typedef unsigned int ( ::osg::Vec2ui::*x_function_type)(  ) const;
            
            Vec2ui_exposer.def( 
                "x"
                , x_function_type( &::osg::Vec2ui::x ) );
        
        }
        { //::osg::Vec2ui::y
        
            typedef unsigned int & ( ::osg::Vec2ui::*y_function_type)(  ) ;
            
            Vec2ui_exposer.def( 
                "y"
                , y_function_type( &::osg::Vec2ui::y )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec2ui::y
        
            typedef unsigned int ( ::osg::Vec2ui::*y_function_type)(  ) const;
            
            Vec2ui_exposer.def( 
                "y"
                , y_function_type( &::osg::Vec2ui::y ) );
        
        }
    }

}
