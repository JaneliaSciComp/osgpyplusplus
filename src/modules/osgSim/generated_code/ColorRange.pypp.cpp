// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgsim.h"
#include "wrap_referenced.h"
#include "colorrange.pypp.hpp"

namespace bp = boost::python;

struct ColorRange_wrapper : osgSim::ColorRange, bp::wrapper< osgSim::ColorRange > {

    ColorRange_wrapper(float min, float max )
    : osgSim::ColorRange( min, max )
      , bp::wrapper< osgSim::ColorRange >(){
        // constructor
    
    }

    ColorRange_wrapper(float min, float max, ::std::vector< osg::Vec4f > const & colors )
    : osgSim::ColorRange( min, max, boost::ref(colors) )
      , bp::wrapper< osgSim::ColorRange >(){
        // constructor
    
    }

    virtual ::osg::Vec4 getColor( float scalar ) const  {
        if( bp::override func_getColor = this->get_override( "getColor" ) )
            return func_getColor( scalar );
        else{
            return this->osgSim::ColorRange::getColor( scalar );
        }
    }
    
    ::osg::Vec4 default_getColor( float scalar ) const  {
        return osgSim::ColorRange::getColor( scalar );
    }

    virtual void setThreadSafeRefUnref( bool threadSafe ) {
        if( bp::override func_setThreadSafeRefUnref = this->get_override( "setThreadSafeRefUnref" ) )
            func_setThreadSafeRefUnref( threadSafe );
        else{
            this->osg::Referenced::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Referenced::setThreadSafeRefUnref( threadSafe );
    }

};

void register_ColorRange_class(){

    bp::class_< ColorRange_wrapper, bp::bases< osgSim::ScalarsToColors >, osg::ref_ptr< ColorRange_wrapper >, boost::noncopyable >( "ColorRange", "\nColorRange is a ScalarsToColors object to define a color spectrum\nfor a scalar range. An optional vector of colors may be passed in at\nconstruction time. The range of colors will be mapped to the scalar range,\nand interpolation between the colors will be performed as necessary.\nBy default, the color range will run Red-Yellow-Green-Cyan-Blue.\n", bp::init< float, float >(( bp::arg("min"), bp::arg("max") ), "\n Constructor for a ColorRange with a default list of colors set to Red-Yellow-Green-Blue-Cyan\n    @param min:      minimum scalar value\n    @param max:      maximum scalar value\n") )    
        .def( bp::init< float, float, std::vector< osg::Vec4f > const & >(( bp::arg("min"), bp::arg("max"), bp::arg("colors") ), "\n Constructor for a ColorRange\n    @param min:      minimum scalar value\n    @param max:      maximum scalar value\n    @param colors:   optional range of colors,\n") )    
        .def( 
            "getColor"
            , (::osg::Vec4 ( ::osgSim::ColorRange::* )( float )const)(&::osgSim::ColorRange::getColor)
            , (::osg::Vec4 ( ColorRange_wrapper::* )( float )const)(&ColorRange_wrapper::default_getColor)
            , ( bp::arg("scalar") ) )    
        .def( 
            "getColors"
            , (::std::vector< osg::Vec4f > const & ( ::osgSim::ColorRange::* )(  )const)( &::osgSim::ColorRange::getColors )
            , bp::return_internal_reference< >()
            , " Get the range of colors" )    
        .def( 
            "setColors"
            , (void ( ::osgSim::ColorRange::* )( ::std::vector< osg::Vec4f > const & ))( &::osgSim::ColorRange::setColors )
            , ( bp::arg("colors") )
            , " Set the range of colors." );

}