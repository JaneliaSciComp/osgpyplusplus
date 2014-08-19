// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "constvaluevisitor.pypp.hpp"

namespace bp = boost::python;

struct ConstValueVisitor_wrapper : osg::ConstValueVisitor, bp::wrapper< osg::ConstValueVisitor > {

    ConstValueVisitor_wrapper(osg::ConstValueVisitor const & arg )
    : osg::ConstValueVisitor( arg )
      , bp::wrapper< osg::ConstValueVisitor >(){
        // copy constructor
        
    }

    ConstValueVisitor_wrapper( )
    : osg::ConstValueVisitor( )
      , bp::wrapper< osg::ConstValueVisitor >(){
        // null constructor
    
    }

    virtual void apply( ::GLbyte const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( ::GLbyte const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( ::GLshort const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( ::GLshort const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( ::GLint const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( ::GLint const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( ::GLushort const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( ::GLushort const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( ::GLubyte const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( ::GLubyte const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( ::GLuint const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( ::GLuint const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( ::GLfloat const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( ::GLfloat const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( double const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( arg0 );
        else{
            this->osg::ConstValueVisitor::apply( arg0 );
        }
    }
    
    void default_apply( double const & arg0 ) {
        osg::ConstValueVisitor::apply( arg0 );
    }

    virtual void apply( ::osg::Vec2b const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2b const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3b const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3b const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4b const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4b const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec2s const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2s const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3s const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3s const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4s const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4s const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec2i const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2i const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3i const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3i const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4i const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4i const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec2ub const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2ub const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3ub const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3ub const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4ub const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4ub const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec2us const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2us const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3us const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3us const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4us const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4us const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec2ui const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2ui const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3ui const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3ui const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4ui const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4ui const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec2 const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2 const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3 const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3 const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4 const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4 const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec2d const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec2d const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec3d const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec3d const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Vec4d const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Vec4d const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Matrixf const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Matrixf const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

    virtual void apply( ::osg::Matrixd const & arg0 ) {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(arg0) );
        else{
            this->osg::ConstValueVisitor::apply( boost::ref(arg0) );
        }
    }
    
    void default_apply( ::osg::Matrixd const & arg0 ) {
        osg::ConstValueVisitor::apply( boost::ref(arg0) );
    }

};

void register_ConstValueVisitor_class(){

    bp::class_< ConstValueVisitor_wrapper >( "ConstValueVisitor", bp::init< >() )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::GLbyte const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::GLbyte const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::GLshort const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::GLshort const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::GLint const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::GLint const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::GLushort const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::GLushort const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::GLubyte const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::GLubyte const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::GLuint const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::GLuint const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::GLfloat const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::GLfloat const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( double const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( double const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2b const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2b const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3b const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3b const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4b const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4b const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2s const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2s const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3s const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3s const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4s const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4s const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2i const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2i const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3i const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3i const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4i const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4i const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2ub const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2ub const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3ub const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3ub const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4ub const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4ub const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2us const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2us const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3us const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3us const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4us const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4us const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2ui const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2ui const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3ui const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3ui const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4ui const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4ui const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2 const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2 const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3 const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3 const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4 const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4 const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec2d const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec2d const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec3d const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec3d const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Vec4d const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Vec4d const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Matrixf const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Matrixf const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) )    
        .def( 
            "apply"
            , (void ( ::osg::ConstValueVisitor::* )( ::osg::Matrixd const & ))(&::osg::ConstValueVisitor::apply)
            , (void ( ConstValueVisitor_wrapper::* )( ::osg::Matrixd const & ))(&ConstValueVisitor_wrapper::default_apply)
            , ( bp::arg("arg0") ) );

}