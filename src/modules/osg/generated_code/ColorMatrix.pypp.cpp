// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "colormatrix.pypp.hpp"

namespace bp = boost::python;

struct ColorMatrix_wrapper : osg::ColorMatrix, bp::wrapper< osg::ColorMatrix > {

    ColorMatrix_wrapper( )
    : osg::ColorMatrix( )
      , bp::wrapper< osg::ColorMatrix >(){
        // null constructor
    
    }

    virtual void apply( ::osg::State & state ) const  {
        if( bp::override func_apply = this->get_override( "apply" ) )
            func_apply( boost::ref(state) );
        else{
            this->osg::ColorMatrix::apply( boost::ref(state) );
        }
    }
    
    void default_apply( ::osg::State & state ) const  {
        osg::ColorMatrix::apply( boost::ref(state) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::ColorMatrix::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::ColorMatrix::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::ColorMatrix::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::ColorMatrix::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::ColorMatrix::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::ColorMatrix::cloneType( );
    }

    virtual ::osg::StateAttribute::Type getType(  ) const  {
        if( bp::override func_getType = this->get_override( "getType" ) )
            return func_getType(  );
        else{
            return this->osg::ColorMatrix::getType(  );
        }
    }
    
    ::osg::StateAttribute::Type default_getType(  ) const  {
        return osg::ColorMatrix::getType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::ColorMatrix::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::ColorMatrix::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::ColorMatrix::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::ColorMatrix::libraryName( );
    }

    virtual ::osg::Texture * asTexture(  ) {
        if( bp::override func_asTexture = this->get_override( "asTexture" ) )
            return func_asTexture(  );
        else{
            return this->osg::StateAttribute::asTexture(  );
        }
    }
    
    ::osg::Texture * default_asTexture(  ) {
        return osg::StateAttribute::asTexture( );
    }

    virtual ::osg::Texture const * asTexture(  ) const  {
        if( bp::override func_asTexture = this->get_override( "asTexture" ) )
            return func_asTexture(  );
        else{
            return this->osg::StateAttribute::asTexture(  );
        }
    }
    
    ::osg::Texture const * default_asTexture(  ) const  {
        return osg::StateAttribute::asTexture( );
    }

    virtual bool checkValidityOfAssociatedModes( ::osg::State & arg0 ) const  {
        if( bp::override func_checkValidityOfAssociatedModes = this->get_override( "checkValidityOfAssociatedModes" ) )
            return func_checkValidityOfAssociatedModes( boost::ref(arg0) );
        else{
            return this->osg::StateAttribute::checkValidityOfAssociatedModes( boost::ref(arg0) );
        }
    }
    
    bool default_checkValidityOfAssociatedModes( ::osg::State & arg0 ) const  {
        return osg::StateAttribute::checkValidityOfAssociatedModes( boost::ref(arg0) );
    }

    virtual void compileGLObjects( ::osg::State & arg0 ) const  {
        if( bp::override func_compileGLObjects = this->get_override( "compileGLObjects" ) )
            func_compileGLObjects( boost::ref(arg0) );
        else{
            this->osg::StateAttribute::compileGLObjects( boost::ref(arg0) );
        }
    }
    
    void default_compileGLObjects( ::osg::State & arg0 ) const  {
        osg::StateAttribute::compileGLObjects( boost::ref(arg0) );
    }

    virtual void computeDataVariance(  ) {
        if( bp::override func_computeDataVariance = this->get_override( "computeDataVariance" ) )
            func_computeDataVariance(  );
        else{
            this->osg::Object::computeDataVariance(  );
        }
    }
    
    void default_computeDataVariance(  ) {
        osg::Object::computeDataVariance( );
    }

    virtual unsigned int getMember(  ) const  {
        if( bp::override func_getMember = this->get_override( "getMember" ) )
            return func_getMember(  );
        else{
            return this->osg::StateAttribute::getMember(  );
        }
    }
    
    unsigned int default_getMember(  ) const  {
        return osg::StateAttribute::getMember( );
    }

    virtual bool getModeUsage( ::osg::StateAttribute::ModeUsage & arg0 ) const  {
        if( bp::override func_getModeUsage = this->get_override( "getModeUsage" ) )
            return func_getModeUsage( boost::ref(arg0) );
        else{
            return this->osg::StateAttribute::getModeUsage( boost::ref(arg0) );
        }
    }
    
    bool default_getModeUsage( ::osg::StateAttribute::ModeUsage & arg0 ) const  {
        return osg::StateAttribute::getModeUsage( boost::ref(arg0) );
    }

    virtual ::osg::Referenced * getUserData(  ) {
        if( bp::override func_getUserData = this->get_override( "getUserData" ) )
            return func_getUserData(  );
        else{
            return this->osg::Object::getUserData(  );
        }
    }
    
    ::osg::Referenced * default_getUserData(  ) {
        return osg::Object::getUserData( );
    }

    virtual ::osg::Referenced const * getUserData(  ) const  {
        if( bp::override func_getUserData = this->get_override( "getUserData" ) )
            return func_getUserData(  );
        else{
            return this->osg::Object::getUserData(  );
        }
    }
    
    ::osg::Referenced const * default_getUserData(  ) const  {
        return osg::Object::getUserData( );
    }

    virtual bool isTextureAttribute(  ) const  {
        if( bp::override func_isTextureAttribute = this->get_override( "isTextureAttribute" ) )
            return func_isTextureAttribute(  );
        else{
            return this->osg::StateAttribute::isTextureAttribute(  );
        }
    }
    
    bool default_isTextureAttribute(  ) const  {
        return osg::StateAttribute::isTextureAttribute( );
    }

    virtual void resizeGLObjectBuffers( unsigned int arg0 ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( arg0 );
        else{
            this->osg::StateAttribute::resizeGLObjectBuffers( arg0 );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int arg0 ) {
        osg::StateAttribute::resizeGLObjectBuffers( arg0 );
    }

    virtual void setName( ::std::string const & name ) {
        if( bp::override func_setName = this->get_override( "setName" ) )
            func_setName( name );
        else{
            this->osg::Object::setName( name );
        }
    }
    
    void default_setName( ::std::string const & name ) {
        osg::Object::setName( name );
    }

    virtual void setThreadSafeRefUnref( bool threadSafe ) {
        if( bp::override func_setThreadSafeRefUnref = this->get_override( "setThreadSafeRefUnref" ) )
            func_setThreadSafeRefUnref( threadSafe );
        else{
            this->osg::Object::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Object::setThreadSafeRefUnref( threadSafe );
    }

    virtual void setUserData( ::osg::Referenced * obj ) {
        if( bp::override func_setUserData = this->get_override( "setUserData" ) )
            func_setUserData( boost::python::ptr(obj) );
        else{
            this->osg::Object::setUserData( boost::python::ptr(obj) );
        }
    }
    
    void default_setUserData( ::osg::Referenced * obj ) {
        osg::Object::setUserData( boost::python::ptr(obj) );
    }

};

void register_ColorMatrix_class(){

    bp::class_< ColorMatrix_wrapper, bp::bases< osg::StateAttribute >, osg::ref_ptr< ::osg::ColorMatrix >, boost::noncopyable >( "ColorMatrix", "\n Encapsulates OpenGL color matrix functionality.\n", bp::no_init )    
        .def( bp::init< >("\n Encapsulates OpenGL color matrix functionality.\n") )    
        .def( 
            "apply"
            , (void ( ::osg::ColorMatrix::* )( ::osg::State & )const)(&::osg::ColorMatrix::apply)
            , (void ( ColorMatrix_wrapper::* )( ::osg::State & )const)(&ColorMatrix_wrapper::default_apply)
            , ( bp::arg("state") ) )    
        .def( 
            "className"
            , (char const * ( ::osg::ColorMatrix::* )(  )const)(&::osg::ColorMatrix::className)
            , (char const * ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osg::ColorMatrix::* )( ::osg::CopyOp const & )const)(&::osg::ColorMatrix::clone)
            , (::osg::Object * ( ColorMatrix_wrapper::* )( ::osg::CopyOp const & )const)(&ColorMatrix_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osg::ColorMatrix::* )(  )const)(&::osg::ColorMatrix::cloneType)
            , (::osg::Object * ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "getMatrix"
            , (::osg::Matrix & ( ::osg::ColorMatrix::* )(  ))( &::osg::ColorMatrix::getMatrix )
            , bp::return_internal_reference< >()
            , " Gets the color matrix." )    
        .def( 
            "getMatrix"
            , (::osg::Matrix const & ( ::osg::ColorMatrix::* )(  )const)( &::osg::ColorMatrix::getMatrix )
            , bp::return_internal_reference< >()
            , " Gets the const color matrix." )    
        .def( 
            "getType"
            , (::osg::StateAttribute::Type ( ::osg::ColorMatrix::* )(  )const)(&::osg::ColorMatrix::getType)
            , (::osg::StateAttribute::Type ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_getType) )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osg::ColorMatrix::* )( ::osg::Object const * )const)(&::osg::ColorMatrix::isSameKindAs)
            , (bool ( ColorMatrix_wrapper::* )( ::osg::Object const * )const)(&ColorMatrix_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osg::ColorMatrix::* )(  )const)(&::osg::ColorMatrix::libraryName)
            , (char const * ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_libraryName) )    
        .def( 
            "setMatrix"
            , (void ( ::osg::ColorMatrix::* )( ::osg::Matrix const & ))( &::osg::ColorMatrix::setMatrix )
            , ( bp::arg("matrix") )
            , " Sets the color matrix." )    
        .def( 
            "asTexture"
            , (::osg::Texture * ( ::osg::StateAttribute::* )(  ))(&::osg::StateAttribute::asTexture)
            , (::osg::Texture * ( ColorMatrix_wrapper::* )(  ))(&ColorMatrix_wrapper::default_asTexture)
            , bp::return_internal_reference< >() )    
        .def( 
            "asTexture"
            , (::osg::Texture const * ( ::osg::StateAttribute::* )(  )const)(&::osg::StateAttribute::asTexture)
            , (::osg::Texture const * ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_asTexture)
            , bp::return_internal_reference< >() )    
        .def( 
            "checkValidityOfAssociatedModes"
            , (bool ( ::osg::StateAttribute::* )( ::osg::State & )const)(&::osg::StateAttribute::checkValidityOfAssociatedModes)
            , (bool ( ColorMatrix_wrapper::* )( ::osg::State & )const)(&ColorMatrix_wrapper::default_checkValidityOfAssociatedModes)
            , ( bp::arg("arg0") ) )    
        .def( 
            "compileGLObjects"
            , (void ( ::osg::StateAttribute::* )( ::osg::State & )const)(&::osg::StateAttribute::compileGLObjects)
            , (void ( ColorMatrix_wrapper::* )( ::osg::State & )const)(&ColorMatrix_wrapper::default_compileGLObjects)
            , ( bp::arg("arg0") ) )    
        .def( 
            "computeDataVariance"
            , (void ( ::osg::Object::* )(  ))(&::osg::Object::computeDataVariance)
            , (void ( ColorMatrix_wrapper::* )(  ))(&ColorMatrix_wrapper::default_computeDataVariance) )    
        .def( 
            "getMember"
            , (unsigned int ( ::osg::StateAttribute::* )(  )const)(&::osg::StateAttribute::getMember)
            , (unsigned int ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_getMember) )    
        .def( 
            "getModeUsage"
            , (bool ( ::osg::StateAttribute::* )( ::osg::StateAttribute::ModeUsage & )const)(&::osg::StateAttribute::getModeUsage)
            , (bool ( ColorMatrix_wrapper::* )( ::osg::StateAttribute::ModeUsage & )const)(&ColorMatrix_wrapper::default_getModeUsage)
            , ( bp::arg("arg0") ) )    
        .def( 
            "getUserData"
            , (::osg::Referenced * ( ::osg::Object::* )(  ))(&::osg::Object::getUserData)
            , (::osg::Referenced * ( ColorMatrix_wrapper::* )(  ))(&ColorMatrix_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "getUserData"
            , (::osg::Referenced const * ( ::osg::Object::* )(  )const)(&::osg::Object::getUserData)
            , (::osg::Referenced const * ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "isTextureAttribute"
            , (bool ( ::osg::StateAttribute::* )(  )const)(&::osg::StateAttribute::isTextureAttribute)
            , (bool ( ColorMatrix_wrapper::* )(  )const)(&ColorMatrix_wrapper::default_isTextureAttribute) )    
        .def( 
            "resizeGLObjectBuffers"
            , (void ( ::osg::StateAttribute::* )( unsigned int ))(&::osg::StateAttribute::resizeGLObjectBuffers)
            , (void ( ColorMatrix_wrapper::* )( unsigned int ))(&ColorMatrix_wrapper::default_resizeGLObjectBuffers)
            , ( bp::arg("arg0") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( ::std::string const & ))(&::osg::Object::setName)
            , (void ( ColorMatrix_wrapper::* )( ::std::string const & ))(&ColorMatrix_wrapper::default_setName)
            , ( bp::arg("name") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( char const * ))( &::osg::Object::setName )
            , ( bp::arg("name") )
            , " Set the name of object using a C style string." )    
        .def( 
            "setThreadSafeRefUnref"
            , (void ( ::osg::Object::* )( bool ))(&::osg::Object::setThreadSafeRefUnref)
            , (void ( ColorMatrix_wrapper::* )( bool ))(&ColorMatrix_wrapper::default_setThreadSafeRefUnref)
            , ( bp::arg("threadSafe") ) )    
        .def( 
            "setUserData"
            , (void ( ::osg::Object::* )( ::osg::Referenced * ))(&::osg::Object::setUserData)
            , (void ( ColorMatrix_wrapper::* )( ::osg::Referenced * ))(&ColorMatrix_wrapper::default_setUserData)
            , ( bp::arg("obj") ) );

}
