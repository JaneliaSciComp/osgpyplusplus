// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "vec3i.pypp.hpp"

namespace bp = boost::python;

void register_Vec3i_class(){

    { //::osg::Vec3i
        typedef bp::class_< osg::Vec3i > Vec3i_exposer_t;
        Vec3i_exposer_t Vec3i_exposer = Vec3i_exposer_t( "Vec3i", "\n General purpose integer triple\n", bp::init< >() );
        bp::scope Vec3i_scope( Vec3i_exposer );
        bp::scope().attr("num_components") = (int)osg::Vec3i::num_components;
        Vec3i_exposer.def( bp::init< int, int, int >(( bp::arg("r"), bp::arg("g"), bp::arg("b") )) );
        Vec3i_exposer.def( bp::self != bp::self );
        Vec3i_exposer.def( bp::self * bp::other< int >() );
        Vec3i_exposer.def( bp::self * bp::self );
        Vec3i_exposer.def( bp::self + bp::other< int >() );
        Vec3i_exposer.def( bp::self + bp::self );
        Vec3i_exposer.def( bp::self - bp::other< int >() );
        Vec3i_exposer.def( bp::self - bp::self );
        Vec3i_exposer.def( bp::self / bp::other< int >() );
        Vec3i_exposer.def( bp::self < bp::self );
        Vec3i_exposer.def( bp::self == bp::self );
        { //::osg::Vec3i::operator[]
        
            typedef int & ( ::osg::Vec3i::*__getitem___function_type)( unsigned int ) ;
            
            Vec3i_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec3i::operator[] )
                , ( bp::arg("i") )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec3i::operator[]
        
            typedef int ( ::osg::Vec3i::*__getitem___function_type)( unsigned int ) const;
            
            Vec3i_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec3i::operator[] )
                , ( bp::arg("i") ) );
        
        }
        { //::osg::Vec3i::set
        
            typedef void ( ::osg::Vec3i::*set_function_type)( int,int,int ) ;
            
            Vec3i_exposer.def( 
                "set"
                , set_function_type( &::osg::Vec3i::set )
                , ( bp::arg("r"), bp::arg("g"), bp::arg("b") ) );
        
        }
        { //::osg::Vec3i::set
        
            typedef void ( ::osg::Vec3i::*set_function_type)( ::osg::Vec3i const & ) ;
            
            Vec3i_exposer.def( 
                "set"
                , set_function_type( &::osg::Vec3i::set )
                , ( bp::arg("rhs") ) );
        
        }
        { //property "x"[fget=::osg::Vec3i::x]
        
            typedef int & ( ::osg::Vec3i::*fget)(  ) ;
            
            Vec3i_exposer.add_property( 
                "x"
                , bp::make_function( 
                      fget( &::osg::Vec3i::x )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "x"[fget=::osg::Vec3i::x]
        
            typedef int ( ::osg::Vec3i::*fget)(  ) const;
            
            Vec3i_exposer.add_property( 
                "x"
                , fget( &::osg::Vec3i::x ) );
        
        }
        { //property "y"[fget=::osg::Vec3i::y]
        
            typedef int & ( ::osg::Vec3i::*fget)(  ) ;
            
            Vec3i_exposer.add_property( 
                "y"
                , bp::make_function( 
                      fget( &::osg::Vec3i::y )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "y"[fget=::osg::Vec3i::y]
        
            typedef int ( ::osg::Vec3i::*fget)(  ) const;
            
            Vec3i_exposer.add_property( 
                "y"
                , fget( &::osg::Vec3i::y ) );
        
        }
        { //property "z"[fget=::osg::Vec3i::z]
        
            typedef int & ( ::osg::Vec3i::*fget)(  ) ;
            
            Vec3i_exposer.add_property( 
                "z"
                , bp::make_function( 
                      fget( &::osg::Vec3i::z )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "z"[fget=::osg::Vec3i::z]
        
            typedef int ( ::osg::Vec3i::*fget)(  ) const;
            
            Vec3i_exposer.add_property( 
                "z"
                , fget( &::osg::Vec3i::z ) );
        
        }
        { //property "r"[fget=::osg::Vec3i::r]
        
            typedef int & ( ::osg::Vec3i::*fget)(  ) ;
            
            Vec3i_exposer.add_property( 
                "r"
                , bp::make_function( 
                      fget( &::osg::Vec3i::r )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "r"[fget=::osg::Vec3i::r]
        
            typedef int ( ::osg::Vec3i::*fget)(  ) const;
            
            Vec3i_exposer.add_property( 
                "r"
                , fget( &::osg::Vec3i::r ) );
        
        }
        { //property "g"[fget=::osg::Vec3i::g]
        
            typedef int & ( ::osg::Vec3i::*fget)(  ) ;
            
            Vec3i_exposer.add_property( 
                "g"
                , bp::make_function( 
                      fget( &::osg::Vec3i::g )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "g"[fget=::osg::Vec3i::g]
        
            typedef int ( ::osg::Vec3i::*fget)(  ) const;
            
            Vec3i_exposer.add_property( 
                "g"
                , fget( &::osg::Vec3i::g ) );
        
        }
        { //property "b"[fget=::osg::Vec3i::b]
        
            typedef int & ( ::osg::Vec3i::*fget)(  ) ;
            
            Vec3i_exposer.add_property( 
                "b"
                , bp::make_function( 
                      fget( &::osg::Vec3i::b )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "b"[fget=::osg::Vec3i::b]
        
            typedef int ( ::osg::Vec3i::*fget)(  ) const;
            
            Vec3i_exposer.add_property( 
                "b"
                , fget( &::osg::Vec3i::b ) );
        
        }
    }

}
