// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "plane.pypp.hpp"

namespace bp = boost::python;

void register_Plane_class(){

    { //::osg::Plane
        typedef bp::class_< osg::Plane > Plane_exposer_t;
        Plane_exposer_t Plane_exposer = Plane_exposer_t( "Plane", "\n A plane class. It can be used to represent an infinite plane.\n\n The infinite plane is described by an implicit plane equation a*x+b*y+c*z+d = 0. Though it is not mandatory that\n a^2+b^2+c^2 = 1 is fulfilled in general some methods require it (aee osg::Plane::distance).\n", bp::init< >("\n Default constructor\n The default constructor initializes all values to zero.\n Warning: Although the method osg::Plane::valid() will return true after the default constructors call the plane\n          is mathematically invalid! Default data do not describe a valid plane.\n") );
        bp::scope Plane_scope( Plane_exposer );
        bp::scope().attr("num_components") = (int)osg::Plane::num_components;
        Plane_exposer.def( bp::init< osg::Plane const & >(( bp::arg("pl") )) );
        Plane_exposer.def( bp::init< double, double, double, double >(( bp::arg("a"), bp::arg("b"), bp::arg("c"), bp::arg("d") ), "\n Constructor\n The plane is described as a*x+b*y+c*z+d = 0.\n @remark You may call osg::Plane::MakeUnitLength afterwards if the passed values are not normalized.\n") );
        Plane_exposer.def( bp::init< osg::Vec4f const & >(( bp::arg("vec") ), "\n Constructor\n The plane can also be described as vec*[x,y,z,1].\n @remark You may call osg::Plane::MakeUnitLength afterwards if the passed values are not normalized.\n") );
        bp::implicitly_convertible< osg::Vec4f const &, osg::Plane >();
        Plane_exposer.def( bp::init< osg::Vec4d const & >(( bp::arg("vec") ), "\n Constructor\n The plane can also be described as vec*[x,y,z,1].\n @remark You may call osg::Plane::MakeUnitLength afterwards if the passed values are not normalized.\n") );
        bp::implicitly_convertible< osg::Vec4d const &, osg::Plane >();
        Plane_exposer.def( bp::init< osg::Vec3d const &, double >(( bp::arg("norm"), bp::arg("d") ), "\n Constructor\n This constructor initializes the internal values directly without any checking or manipulation.\n @param norm: The normal of the plane.\n @param d:    The negative distance from the point of origin to the plane.\n @remark You may call osg::Plane::MakeUnitLength afterwards if the passed normal was not normalized.\n") );
        Plane_exposer.def( bp::init< osg::Vec3d const &, osg::Vec3d const &, osg::Vec3d const & >(( bp::arg("v1"), bp::arg("v2"), bp::arg("v3") ), "\n Constructor\n This constructor calculates from the three points describing an infinite plane the internal values.\n @param v1: Point in the plane.\n @param v2: Point in the plane.\n @param v3: Point in the plane.\n @remark After this constructor call the planes normal is normalized in case the three points described a mathematically\n         valid plane.\n @remark The normal is determined by building the cross product of (v2-v1) ^ (v3-v2).\n") );
        Plane_exposer.def( bp::init< osg::Vec3d const &, osg::Vec3d const & >(( bp::arg("norm"), bp::arg("point") ), "\n Constructor\n This constructor initializes the internal values directly without any checking or manipulation.\n @param norm:  The normal of the plane.\n @param point: A point of the plane.\n @remark You may call osg::Plane::MakeUnitLength afterwards if the passed normal was not normalized.\n") );
        { //::osg::Plane::asVec4
        
            typedef ::osg::Vec4d ( ::osg::Plane::*asVec4_function_type )(  ) const;
            
            Plane_exposer.def( 
                "asVec4"
                , asVec4_function_type( &::osg::Plane::asVec4 ) );
        
        }
        { //::osg::Plane::calculateUpperLowerBBCorners
        
            typedef void ( ::osg::Plane::*calculateUpperLowerBBCorners_function_type )(  ) ;
            
            Plane_exposer.def( 
                "calculateUpperLowerBBCorners"
                , calculateUpperLowerBBCorners_function_type( &::osg::Plane::calculateUpperLowerBBCorners )
                , "\n calculate the upper and lower bounding box corners to be used\n in the intersect(BoundingBox&) method for speeding calculations.\n" );
        
        }
        { //::osg::Plane::distance
        
            typedef float ( ::osg::Plane::*distance_function_type )( ::osg::Vec3f const & ) const;
            
            Plane_exposer.def( 
                "distance"
                , distance_function_type( &::osg::Plane::distance )
                , ( bp::arg("v") )
                , "\n Calculate the distance between a point and the plane.\n @remark This method only leads to real distance values if the planes norm is 1.\n aa osg::Plane::makeUnitLength\n" );
        
        }
        { //::osg::Plane::distance
        
            typedef double ( ::osg::Plane::*distance_function_type )( ::osg::Vec3d const & ) const;
            
            Plane_exposer.def( 
                "distance"
                , distance_function_type( &::osg::Plane::distance )
                , ( bp::arg("v") )
                , "\n Calculate the distance between a point and the plane.\n @remark This method only leads to real distance values if the planes norm is 1.\n aa osg::Plane::makeUnitLength\n" );
        
        }
        { //::osg::Plane::dotProductNormal
        
            typedef float ( ::osg::Plane::*dotProductNormal_function_type )( ::osg::Vec3f const & ) const;
            
            Plane_exposer.def( 
                "dotProductNormal"
                , dotProductNormal_function_type( &::osg::Plane::dotProductNormal )
                , ( bp::arg("v") )
                , "\n calculate the dot product of the plane normal and a point.\n" );
        
        }
        { //::osg::Plane::dotProductNormal
        
            typedef double ( ::osg::Plane::*dotProductNormal_function_type )( ::osg::Vec3d const & ) const;
            
            Plane_exposer.def( 
                "dotProductNormal"
                , dotProductNormal_function_type( &::osg::Plane::dotProductNormal )
                , ( bp::arg("v") )
                , "\n calculate the dot product of the plane normal and a point.\n" );
        
        }
        { //::osg::Plane::flip
        
            typedef void ( ::osg::Plane::*flip_function_type )(  ) ;
            
            Plane_exposer.def( 
                "flip"
                , flip_function_type( &::osg::Plane::flip )
                , "\n flip/reverse the orientation of the plane.\n" );
        
        }
        { //::osg::Plane::getNormal
        
            typedef ::osg::Vec3d ( ::osg::Plane::*getNormal_function_type )(  ) const;
            
            Plane_exposer.def( 
                "getNormal"
                , getNormal_function_type( &::osg::Plane::getNormal ) );
        
        }
        { //::osg::Plane::intersect
        
            typedef int ( ::osg::Plane::*intersect_function_type )( ::std::vector< osg::Vec3f > const & ) const;
            
            Plane_exposer.def( 
                "intersect"
                , intersect_function_type( &::osg::Plane::intersect )
                , ( bp::arg("vertices") )
                , "\n intersection test between plane and vertex list\n            return 1 if the bs is completely above plane,\n            return 0 if the bs intersects the plane,\n            return -1 if the bs is completely below the plane.\n" );
        
        }
        { //::osg::Plane::intersect
        
            typedef int ( ::osg::Plane::*intersect_function_type )( ::std::vector< osg::Vec3d > const & ) const;
            
            Plane_exposer.def( 
                "intersect"
                , intersect_function_type( &::osg::Plane::intersect )
                , ( bp::arg("vertices") )
                , "\n intersection test between plane and vertex list\n            return 1 if the bs is completely above plane,\n            return 0 if the bs intersects the plane,\n            return -1 if the bs is completely below the plane.\n" );
        
        }
        { //::osg::Plane::intersect
        
            typedef int ( ::osg::Plane::*intersect_function_type )( ::osg::BoundingSphere const & ) const;
            
            Plane_exposer.def( 
                "intersect"
                , intersect_function_type( &::osg::Plane::intersect )
                , ( bp::arg("bs") )
                , "\n intersection test between plane and bounding sphere.\n            return 1 if the bs is completely above plane,\n            return 0 if the bs intersects the plane,\n            return -1 if the bs is completely below the plane.\n" );
        
        }
        { //::osg::Plane::intersect
        
            typedef int ( ::osg::Plane::*intersect_function_type )( ::osg::BoundingBox const & ) const;
            
            Plane_exposer.def( 
                "intersect"
                , intersect_function_type( &::osg::Plane::intersect )
                , ( bp::arg("bb") )
                , "\n intersection test between plane and bounding sphere.\n            return 1 if the bs is completely above plane,\n            return 0 if the bs intersects the plane,\n            return -1 if the bs is completely below the plane.\n" );
        
        }
        { //::osg::Plane::isNaN
        
            typedef bool ( ::osg::Plane::*isNaN_function_type )(  ) const;
            
            Plane_exposer.def( 
                "isNaN"
                , isNaN_function_type( &::osg::Plane::isNaN ) );
        
        }
        { //::osg::Plane::makeUnitLength
        
            typedef void ( ::osg::Plane::*makeUnitLength_function_type )(  ) ;
            
            Plane_exposer.def( 
                "makeUnitLength"
                , makeUnitLength_function_type( &::osg::Plane::makeUnitLength )
                , "\n This method multiplies the coefficients of the plane equation with a constant factor so that the\n equation a^2+b^2+c^2 = 1 holds.\n" );
        
        }
        Plane_exposer.def( bp::self != bp::self );
        Plane_exposer.def( bp::self < bp::self );
        { //::osg::Plane::operator=
        
            typedef ::osg::Plane & ( ::osg::Plane::*assign_function_type )( ::osg::Plane const & ) ;
            
            Plane_exposer.def( 
                "assign"
                , assign_function_type( &::osg::Plane::operator= )
                , ( bp::arg("pl") )
                , bp::return_self< >() );
        
        }
        Plane_exposer.def( bp::self == bp::self );
        { //::osg::Plane::operator[]
        
            typedef double & ( ::osg::Plane::*__getitem___function_type )( unsigned int ) ;
            
            Plane_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Plane::operator[] )
                , ( bp::arg("i") )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::Plane::operator[]
        
            typedef double ( ::osg::Plane::*__getitem___function_type )( unsigned int ) const;
            
            Plane_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::Plane::operator[] )
                , ( bp::arg("i") ) );
        
        }
        { //::osg::Plane::set
        
            typedef void ( ::osg::Plane::*set_function_type )( ::osg::Plane const & ) ;
            
            Plane_exposer.def( 
                "set"
                , set_function_type( &::osg::Plane::set )
                , ( bp::arg("pl") ) );
        
        }
        { //::osg::Plane::set
        
            typedef void ( ::osg::Plane::*set_function_type )( double,double,double,double ) ;
            
            Plane_exposer.def( 
                "set"
                , set_function_type( &::osg::Plane::set )
                , ( bp::arg("a"), bp::arg("b"), bp::arg("c"), bp::arg("d") ) );
        
        }
        { //::osg::Plane::set
        
            typedef void ( ::osg::Plane::*set_function_type )( ::osg::Vec4f const & ) ;
            
            Plane_exposer.def( 
                "set"
                , set_function_type( &::osg::Plane::set )
                , ( bp::arg("vec") ) );
        
        }
        { //::osg::Plane::set
        
            typedef void ( ::osg::Plane::*set_function_type )( ::osg::Vec4d const & ) ;
            
            Plane_exposer.def( 
                "set"
                , set_function_type( &::osg::Plane::set )
                , ( bp::arg("vec") ) );
        
        }
        { //::osg::Plane::set
        
            typedef void ( ::osg::Plane::*set_function_type )( ::osg::Vec3d const &,double ) ;
            
            Plane_exposer.def( 
                "set"
                , set_function_type( &::osg::Plane::set )
                , ( bp::arg("norm"), bp::arg("d") ) );
        
        }
        { //::osg::Plane::set
        
            typedef void ( ::osg::Plane::*set_function_type )( ::osg::Vec3d const &,::osg::Vec3d const &,::osg::Vec3d const & ) ;
            
            Plane_exposer.def( 
                "set"
                , set_function_type( &::osg::Plane::set )
                , ( bp::arg("v1"), bp::arg("v2"), bp::arg("v3") ) );
        
        }
        { //::osg::Plane::set
        
            typedef void ( ::osg::Plane::*set_function_type )( ::osg::Vec3d const &,::osg::Vec3d const & ) ;
            
            Plane_exposer.def( 
                "set"
                , set_function_type( &::osg::Plane::set )
                , ( bp::arg("norm"), bp::arg("point") ) );
        
        }
        { //::osg::Plane::transform
        
            typedef void ( ::osg::Plane::*transform_function_type )( ::osg::Matrix const & ) ;
            
            Plane_exposer.def( 
                "transform"
                , transform_function_type( &::osg::Plane::transform )
                , ( bp::arg("matrix") )
                , "\n Transform the plane by matrix.  Note, this operation carries out\n the calculation of the inverse of the matrix since a plane\n must be multiplied by the inverse transposed to transform it. This\n make this operation expensive.  If the inverse has been already\n calculated elsewhere then use transformProvidingInverse() instead.\n See http://www.worldserver.com/turk/computergraphics/NormalTransformations.pdf\n" );
        
        }
        { //::osg::Plane::transformProvidingInverse
        
            typedef void ( ::osg::Plane::*transformProvidingInverse_function_type )( ::osg::Matrix const & ) ;
            
            Plane_exposer.def( 
                "transformProvidingInverse"
                , transformProvidingInverse_function_type( &::osg::Plane::transformProvidingInverse )
                , ( bp::arg("matrix") )
                , "\n Transform the plane by providing a pre inverted matrix.\n see transform for details.\n" );
        
        }
        { //::osg::Plane::valid
        
            typedef bool ( ::osg::Plane::*valid_function_type )(  ) const;
            
            Plane_exposer.def( 
                "valid"
                , valid_function_type( &::osg::Plane::valid )
                , "\n Checks if all internal values describing the plane have valid numbers\n Warning: This method does not check if the plane is mathematically correctly described!\n @remark  The only case where all elements have valid numbers and the plane description is invalid occurs if the planes normal\n          is zero.\n" );
        
        }
        Plane_exposer.def( bp::self_ns::str( bp::self ) );
    }

}
