// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "vec2s.pypp.hpp"

namespace bp = boost::python;

void register_Vec2s_class(){

    { //::osg::Vec2s
        typedef bp::class_< osg::Vec2s > Vec2s_exposer_t;
        Vec2s_exposer_t Vec2s_exposer = Vec2s_exposer_t( "Vec2s", bp::init< >("\n Constructor that sets all components of the vector to zero\n") );
        bp::scope Vec2s_scope( Vec2s_exposer );
        bp::scope().attr("num_components") = (int)osg::Vec2s::num_components;
        Vec2s_exposer.def( bp::init< short int, short int >(( bp::arg("x"), bp::arg("y") )) );
        Vec2s_exposer.def( bp::self != bp::self );
        Vec2s_exposer.def( bp::self * bp::other< short int >() );
        Vec2s_exposer.def( bp::self * bp::self );
        Vec2s_exposer.def( bp::self *= bp::other< short int >() );
        Vec2s_exposer.def( bp::self + bp::self );
        Vec2s_exposer.def( bp::self += bp::self );
        Vec2s_exposer.def( bp::self - bp::self );
        Vec2s_exposer.def( -bp::self );
        Vec2s_exposer.def( bp::self -= bp::self );
        Vec2s_exposer.def( bp::self / bp::other< short int >() );
        Vec2s_exposer.def( bp::self /= bp::other< short int >() );
        Vec2s_exposer.def( bp::self < bp::self );
        Vec2s_exposer.def( bp::self == bp::self );
        { //::osg::Vec2s::operator[]
        
            typedef short int & ( ::osg::Vec2s::*__getitem___function_type )( int ) ;
            
            Vec2s_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec2s::operator[] )
                , ( bp::arg("i") )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Vec2s::operator[]
        
            typedef short int ( ::osg::Vec2s::*__getitem___function_type )( int ) const;
            
            Vec2s_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Vec2s::operator[] )
                , ( bp::arg("i") ) );
        
        }
        { //::osg::Vec2s::set
        
            typedef void ( ::osg::Vec2s::*set_function_type )( short int,short int ) ;
            
            Vec2s_exposer.def( 
                "set"
                , set_function_type( &::osg::Vec2s::set )
                , ( bp::arg("x"), bp::arg("y") ) );
        
        }
        { //::osg::Vec2s::set
        
            typedef void ( ::osg::Vec2s::*set_function_type )( ::osg::Vec2s const & ) ;
            
            Vec2s_exposer.def( 
                "set"
                , set_function_type( &::osg::Vec2s::set )
                , ( bp::arg("rhs") ) );
        
        }
        { //property "x"[fget=::osg::Vec2s::x]
        
            typedef short int & ( ::osg::Vec2s::*fget )(  ) ;
            
            Vec2s_exposer.add_property( 
                "x"
                , bp::make_function( 
                      fget( &::osg::Vec2s::x )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "x"[fget=::osg::Vec2s::x]
        
            typedef short int ( ::osg::Vec2s::*fget )(  ) const;
            
            Vec2s_exposer.add_property( 
                "x"
                , fget( &::osg::Vec2s::x ) );
        
        }
        { //property "y"[fget=::osg::Vec2s::y]
        
            typedef short int & ( ::osg::Vec2s::*fget )(  ) ;
            
            Vec2s_exposer.add_property( 
                "y"
                , bp::make_function( 
                      fget( &::osg::Vec2s::y )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "y"[fget=::osg::Vec2s::y]
        
            typedef short int ( ::osg::Vec2s::*fget )(  ) const;
            
            Vec2s_exposer.add_property( 
                "y"
                , fget( &::osg::Vec2s::y ) );
        
        }
        { //property "r"[fget=::osg::Vec2s::r]
        
            typedef short int & ( ::osg::Vec2s::*fget )(  ) ;
            
            Vec2s_exposer.add_property( 
                "r"
                , bp::make_function( 
                      fget( &::osg::Vec2s::r )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "r"[fget=::osg::Vec2s::r]
        
            typedef short int ( ::osg::Vec2s::*fget )(  ) const;
            
            Vec2s_exposer.add_property( 
                "r"
                , fget( &::osg::Vec2s::r ) );
        
        }
        { //property "g"[fget=::osg::Vec2s::g]
        
            typedef short int & ( ::osg::Vec2s::*fget )(  ) ;
            
            Vec2s_exposer.add_property( 
                "g"
                , bp::make_function( 
                      fget( &::osg::Vec2s::g )
                    , bp::return_value_policy< bp::copy_non_const_reference >() )  );
        
        }
        { //property "g"[fget=::osg::Vec2s::g]
        
            typedef short int ( ::osg::Vec2s::*fget )(  ) const;
            
            Vec2s_exposer.add_property( 
                "g"
                , fget( &::osg::Vec2s::g ) );
        
        }
        Vec2s_exposer.def( bp::self_ns::str( bp::self ) );
        Vec2s_exposer.def( bp::self_ns::str(bp::self) );
    }

}
