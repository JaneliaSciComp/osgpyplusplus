// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "wrap_referenced.h"
#include "drawarrays.pypp.hpp"

namespace bp = boost::python;

struct DrawArrays_wrapper : osg::DrawArrays, bp::wrapper< osg::DrawArrays > {

    DrawArrays_wrapper(::GLenum mode=0 )
    : osg::DrawArrays( mode )
      , bp::wrapper< osg::DrawArrays >(){
        // constructor
    
    }

    DrawArrays_wrapper(::GLenum mode, ::GLint first, ::GLsizei count, int numInstances=0 )
    : osg::DrawArrays( mode, first, count, numInstances )
      , bp::wrapper< osg::DrawArrays >(){
        // constructor
    
    }

    virtual void accept( ::osg::PrimitiveFunctor & functor ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(functor) );
        else{
            this->osg::DrawArrays::accept( boost::ref(functor) );
        }
    }
    
    void default_accept( ::osg::PrimitiveFunctor & functor ) const  {
        osg::DrawArrays::accept( boost::ref(functor) );
    }

    virtual void accept( ::osg::PrimitiveIndexFunctor & functor ) const  {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(functor) );
        else{
            this->osg::DrawArrays::accept( boost::ref(functor) );
        }
    }
    
    void default_accept( ::osg::PrimitiveIndexFunctor & functor ) const  {
        osg::DrawArrays::accept( boost::ref(functor) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::DrawArrays::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::DrawArrays::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::DrawArrays::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::DrawArrays::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::DrawArrays::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::DrawArrays::cloneType( );
    }

    virtual void draw( ::osg::State & state, bool useVertexBufferObjects ) const  {
        if( bp::override func_draw = this->get_override( "draw" ) )
            func_draw( boost::ref(state), useVertexBufferObjects );
        else{
            this->osg::DrawArrays::draw( boost::ref(state), useVertexBufferObjects );
        }
    }
    
    void default_draw( ::osg::State & state, bool useVertexBufferObjects ) const  {
        osg::DrawArrays::draw( boost::ref(state), useVertexBufferObjects );
    }

    virtual unsigned int getNumIndices(  ) const  {
        if( bp::override func_getNumIndices = this->get_override( "getNumIndices" ) )
            return func_getNumIndices(  );
        else{
            return this->osg::DrawArrays::getNumIndices(  );
        }
    }
    
    unsigned int default_getNumIndices(  ) const  {
        return osg::DrawArrays::getNumIndices( );
    }

    virtual unsigned int index( unsigned int pos ) const  {
        if( bp::override func_index = this->get_override( "index" ) )
            return func_index( pos );
        else{
            return this->osg::DrawArrays::index( pos );
        }
    }
    
    unsigned int default_index( unsigned int pos ) const  {
        return osg::DrawArrays::index( pos );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::DrawArrays::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::DrawArrays::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::DrawArrays::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::DrawArrays::libraryName( );
    }

    virtual void offsetIndices( int offset ) {
        if( bp::override func_offsetIndices = this->get_override( "offsetIndices" ) )
            func_offsetIndices( offset );
        else{
            this->osg::DrawArrays::offsetIndices( offset );
        }
    }
    
    void default_offsetIndices( int offset ) {
        osg::DrawArrays::offsetIndices( offset );
    }

    virtual ::osg::Array * asArray(  ) {
        if( bp::override func_asArray = this->get_override( "asArray" ) )
            return func_asArray(  );
        else{
            return this->osg::BufferData::asArray(  );
        }
    }
    
    ::osg::Array * default_asArray(  ) {
        return osg::BufferData::asArray( );
    }

    virtual ::osg::Array const * asArray(  ) const  {
        if( bp::override func_asArray = this->get_override( "asArray" ) )
            return func_asArray(  );
        else{
            return this->osg::BufferData::asArray(  );
        }
    }
    
    ::osg::Array const * default_asArray(  ) const  {
        return osg::BufferData::asArray( );
    }

    virtual ::osg::PrimitiveSet * asPrimitiveSet(  ) {
        if( bp::override func_asPrimitiveSet = this->get_override( "asPrimitiveSet" ) )
            return func_asPrimitiveSet(  );
        else{
            return this->osg::PrimitiveSet::asPrimitiveSet(  );
        }
    }
    
    ::osg::PrimitiveSet * default_asPrimitiveSet(  ) {
        return osg::PrimitiveSet::asPrimitiveSet( );
    }

    virtual ::osg::PrimitiveSet const * asPrimitiveSet(  ) const  {
        if( bp::override func_asPrimitiveSet = this->get_override( "asPrimitiveSet" ) )
            return func_asPrimitiveSet(  );
        else{
            return this->osg::PrimitiveSet::asPrimitiveSet(  );
        }
    }
    
    ::osg::PrimitiveSet const * default_asPrimitiveSet(  ) const  {
        return osg::PrimitiveSet::asPrimitiveSet( );
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

    virtual void computeRange(  ) const  {
        if( bp::override func_computeRange = this->get_override( "computeRange" ) )
            func_computeRange(  );
        else{
            this->osg::PrimitiveSet::computeRange(  );
        }
    }
    
    void default_computeRange(  ) const  {
        osg::PrimitiveSet::computeRange( );
    }

    virtual ::GLvoid const * getDataPointer(  ) const  {
        if( bp::override func_getDataPointer = this->get_override( "getDataPointer" ) )
            return func_getDataPointer(  );
        else{
            return this->osg::PrimitiveSet::getDataPointer(  );
        }
    }
    
    ::GLvoid const * default_getDataPointer(  ) const  {
        return osg::PrimitiveSet::getDataPointer( );
    }

    virtual ::osg::DrawElements * getDrawElements(  ) {
        if( bp::override func_getDrawElements = this->get_override( "getDrawElements" ) )
            return func_getDrawElements(  );
        else{
            return this->osg::PrimitiveSet::getDrawElements(  );
        }
    }
    
    ::osg::DrawElements * default_getDrawElements(  ) {
        return osg::PrimitiveSet::getDrawElements( );
    }

    virtual ::osg::DrawElements const * getDrawElements(  ) const  {
        if( bp::override func_getDrawElements = this->get_override( "getDrawElements" ) )
            return func_getDrawElements(  );
        else{
            return this->osg::PrimitiveSet::getDrawElements(  );
        }
    }
    
    ::osg::DrawElements const * default_getDrawElements(  ) const  {
        return osg::PrimitiveSet::getDrawElements( );
    }

    virtual unsigned int getNumPrimitives(  ) const  {
        if( bp::override func_getNumPrimitives = this->get_override( "getNumPrimitives" ) )
            return func_getNumPrimitives(  );
        else{
            return this->osg::PrimitiveSet::getNumPrimitives(  );
        }
    }
    
    unsigned int default_getNumPrimitives(  ) const  {
        return osg::PrimitiveSet::getNumPrimitives( );
    }

    virtual unsigned int getTotalDataSize(  ) const  {
        if( bp::override func_getTotalDataSize = this->get_override( "getTotalDataSize" ) )
            return func_getTotalDataSize(  );
        else{
            return this->osg::PrimitiveSet::getTotalDataSize(  );
        }
    }
    
    unsigned int default_getTotalDataSize(  ) const  {
        return osg::PrimitiveSet::getTotalDataSize( );
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

    virtual void resizeGLObjectBuffers( unsigned int maxSize ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( maxSize );
        else{
            this->osg::BufferData::resizeGLObjectBuffers( maxSize );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int maxSize ) {
        osg::BufferData::resizeGLObjectBuffers( maxSize );
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

    virtual bool supportsBufferObject(  ) const  {
        if( bp::override func_supportsBufferObject = this->get_override( "supportsBufferObject" ) )
            return func_supportsBufferObject(  );
        else{
            return this->osg::PrimitiveSet::supportsBufferObject(  );
        }
    }
    
    bool default_supportsBufferObject(  ) const  {
        return osg::PrimitiveSet::supportsBufferObject( );
    }

};

void register_DrawArrays_class(){

    bp::class_< DrawArrays_wrapper, bp::bases< osg::PrimitiveSet >, osg::ref_ptr< ::osg::DrawArrays >, boost::noncopyable >( "DrawArrays", bp::no_init )    
        .def( bp::init< bp::optional< GLenum > >(( bp::arg("mode")=(::GLenum)(0) )) )    
        .def( bp::init< GLenum, GLint, GLsizei, bp::optional< int > >(( bp::arg("mode"), bp::arg("first"), bp::arg("count"), bp::arg("numInstances")=(int)(0) )) )    
        .def( 
            "accept"
            , (void ( ::osg::DrawArrays::* )( ::osg::PrimitiveFunctor & )const)(&::osg::DrawArrays::accept)
            , (void ( DrawArrays_wrapper::* )( ::osg::PrimitiveFunctor & )const)(&DrawArrays_wrapper::default_accept)
            , ( bp::arg("functor") ) )    
        .def( 
            "accept"
            , (void ( ::osg::DrawArrays::* )( ::osg::PrimitiveIndexFunctor & )const)(&::osg::DrawArrays::accept)
            , (void ( DrawArrays_wrapper::* )( ::osg::PrimitiveIndexFunctor & )const)(&DrawArrays_wrapper::default_accept)
            , ( bp::arg("functor") ) )    
        .def( 
            "className"
            , (char const * ( ::osg::DrawArrays::* )(  )const)(&::osg::DrawArrays::className)
            , (char const * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_className) )    
        .def( 
            "clone"
            , (::osg::Object * ( ::osg::DrawArrays::* )( ::osg::CopyOp const & )const)(&::osg::DrawArrays::clone)
            , (::osg::Object * ( DrawArrays_wrapper::* )( ::osg::CopyOp const & )const)(&DrawArrays_wrapper::default_clone)
            , ( bp::arg("copyop") )
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "cloneType"
            , (::osg::Object * ( ::osg::DrawArrays::* )(  )const)(&::osg::DrawArrays::cloneType)
            , (::osg::Object * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_cloneType)
            , bp::return_value_policy< bp::reference_existing_object >() )    
        .def( 
            "draw"
            , (void ( ::osg::DrawArrays::* )( ::osg::State &,bool )const)(&::osg::DrawArrays::draw)
            , (void ( DrawArrays_wrapper::* )( ::osg::State &,bool )const)(&DrawArrays_wrapper::default_draw)
            , ( bp::arg("state"), bp::arg("useVertexBufferObjects") ) )    
        .def( 
            "getCount"
            , (::GLsizei ( ::osg::DrawArrays::* )(  )const)( &::osg::DrawArrays::getCount ) )    
        .def( 
            "getFirst"
            , (::GLint ( ::osg::DrawArrays::* )(  )const)( &::osg::DrawArrays::getFirst ) )    
        .def( 
            "getNumIndices"
            , (unsigned int ( ::osg::DrawArrays::* )(  )const)(&::osg::DrawArrays::getNumIndices)
            , (unsigned int ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_getNumIndices) )    
        .def( 
            "index"
            , (unsigned int ( ::osg::DrawArrays::* )( unsigned int )const)(&::osg::DrawArrays::index)
            , (unsigned int ( DrawArrays_wrapper::* )( unsigned int )const)(&DrawArrays_wrapper::default_index)
            , ( bp::arg("pos") ) )    
        .def( 
            "isSameKindAs"
            , (bool ( ::osg::DrawArrays::* )( ::osg::Object const * )const)(&::osg::DrawArrays::isSameKindAs)
            , (bool ( DrawArrays_wrapper::* )( ::osg::Object const * )const)(&DrawArrays_wrapper::default_isSameKindAs)
            , ( bp::arg("obj") ) )    
        .def( 
            "libraryName"
            , (char const * ( ::osg::DrawArrays::* )(  )const)(&::osg::DrawArrays::libraryName)
            , (char const * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_libraryName) )    
        .def( 
            "offsetIndices"
            , (void ( ::osg::DrawArrays::* )( int ))(&::osg::DrawArrays::offsetIndices)
            , (void ( DrawArrays_wrapper::* )( int ))(&DrawArrays_wrapper::default_offsetIndices)
            , ( bp::arg("offset") ) )    
        .def( 
            "set"
            , (void ( ::osg::DrawArrays::* )( ::GLenum,::GLint,::GLsizei ))( &::osg::DrawArrays::set )
            , ( bp::arg("mode"), bp::arg("first"), bp::arg("count") ) )    
        .def( 
            "setCount"
            , (void ( ::osg::DrawArrays::* )( ::GLsizei ))( &::osg::DrawArrays::setCount )
            , ( bp::arg("count") ) )    
        .def( 
            "setFirst"
            , (void ( ::osg::DrawArrays::* )( ::GLint ))( &::osg::DrawArrays::setFirst )
            , ( bp::arg("first") ) )    
        .def( 
            "asArray"
            , (::osg::Array * ( ::osg::BufferData::* )(  ))(&::osg::BufferData::asArray)
            , (::osg::Array * ( DrawArrays_wrapper::* )(  ))(&DrawArrays_wrapper::default_asArray)
            , bp::return_internal_reference< >() )    
        .def( 
            "asArray"
            , (::osg::Array const * ( ::osg::BufferData::* )(  )const)(&::osg::BufferData::asArray)
            , (::osg::Array const * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_asArray)
            , bp::return_internal_reference< >() )    
        .def( 
            "asPrimitiveSet"
            , (::osg::PrimitiveSet * ( ::osg::PrimitiveSet::* )(  ))(&::osg::PrimitiveSet::asPrimitiveSet)
            , (::osg::PrimitiveSet * ( DrawArrays_wrapper::* )(  ))(&DrawArrays_wrapper::default_asPrimitiveSet)
            , bp::return_internal_reference< >() )    
        .def( 
            "asPrimitiveSet"
            , (::osg::PrimitiveSet const * ( ::osg::PrimitiveSet::* )(  )const)(&::osg::PrimitiveSet::asPrimitiveSet)
            , (::osg::PrimitiveSet const * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_asPrimitiveSet)
            , bp::return_internal_reference< >() )    
        .def( 
            "computeDataVariance"
            , (void ( ::osg::Object::* )(  ))(&::osg::Object::computeDataVariance)
            , (void ( DrawArrays_wrapper::* )(  ))(&DrawArrays_wrapper::default_computeDataVariance) )    
        .def( 
            "computeRange"
            , (void ( ::osg::PrimitiveSet::* )(  )const)(&::osg::PrimitiveSet::computeRange)
            , (void ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_computeRange) )    
        .def( 
            "getDataPointer"
            , (::GLvoid const * ( ::osg::PrimitiveSet::* )(  )const)(&::osg::PrimitiveSet::getDataPointer)
            , (::GLvoid const * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_getDataPointer)
            , bp::return_value_policy< bp::return_opaque_pointer >() )    
        .def( 
            "getDrawElements"
            , (::osg::DrawElements * ( ::osg::PrimitiveSet::* )(  ))(&::osg::PrimitiveSet::getDrawElements)
            , (::osg::DrawElements * ( DrawArrays_wrapper::* )(  ))(&DrawArrays_wrapper::default_getDrawElements)
            , bp::return_internal_reference< >() )    
        .def( 
            "getDrawElements"
            , (::osg::DrawElements const * ( ::osg::PrimitiveSet::* )(  )const)(&::osg::PrimitiveSet::getDrawElements)
            , (::osg::DrawElements const * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_getDrawElements)
            , bp::return_internal_reference< >() )    
        .def( 
            "getNumPrimitives"
            , (unsigned int ( ::osg::PrimitiveSet::* )(  )const)(&::osg::PrimitiveSet::getNumPrimitives)
            , (unsigned int ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_getNumPrimitives) )    
        .def( 
            "getTotalDataSize"
            , (unsigned int ( ::osg::PrimitiveSet::* )(  )const)(&::osg::PrimitiveSet::getTotalDataSize)
            , (unsigned int ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_getTotalDataSize) )    
        .def( 
            "getUserData"
            , (::osg::Referenced * ( ::osg::Object::* )(  ))(&::osg::Object::getUserData)
            , (::osg::Referenced * ( DrawArrays_wrapper::* )(  ))(&DrawArrays_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "getUserData"
            , (::osg::Referenced const * ( ::osg::Object::* )(  )const)(&::osg::Object::getUserData)
            , (::osg::Referenced const * ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_getUserData)
            , bp::return_internal_reference< >() )    
        .def( 
            "resizeGLObjectBuffers"
            , (void ( ::osg::BufferData::* )( unsigned int ))(&::osg::BufferData::resizeGLObjectBuffers)
            , (void ( DrawArrays_wrapper::* )( unsigned int ))(&DrawArrays_wrapper::default_resizeGLObjectBuffers)
            , ( bp::arg("maxSize") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( ::std::string const & ))(&::osg::Object::setName)
            , (void ( DrawArrays_wrapper::* )( ::std::string const & ))(&DrawArrays_wrapper::default_setName)
            , ( bp::arg("name") ) )    
        .def( 
            "setName"
            , (void ( ::osg::Object::* )( char const * ))( &::osg::Object::setName )
            , ( bp::arg("name") ) )    
        .def( 
            "setThreadSafeRefUnref"
            , (void ( ::osg::Object::* )( bool ))(&::osg::Object::setThreadSafeRefUnref)
            , (void ( DrawArrays_wrapper::* )( bool ))(&DrawArrays_wrapper::default_setThreadSafeRefUnref)
            , ( bp::arg("threadSafe") ) )    
        .def( 
            "setUserData"
            , (void ( ::osg::Object::* )( ::osg::Referenced * ))(&::osg::Object::setUserData)
            , (void ( DrawArrays_wrapper::* )( ::osg::Referenced * ))(&DrawArrays_wrapper::default_setUserData)
            , ( bp::arg("obj") ) )    
        .def( 
            "supportsBufferObject"
            , (bool ( ::osg::PrimitiveSet::* )(  )const)(&::osg::PrimitiveSet::supportsBufferObject)
            , (bool ( DrawArrays_wrapper::* )(  )const)(&DrawArrays_wrapper::default_supportsBufferObject) );

}
