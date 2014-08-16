// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "clearnode.pypp.hpp"

namespace bp = boost::python;

struct ClearNode_wrapper : osg::ClearNode, bp::wrapper< osg::ClearNode > {

    ClearNode_wrapper( )
    : osg::ClearNode( )
      , bp::wrapper< osg::ClearNode >(){
        // null constructor
    
    }

    ClearNode_wrapper(::osg::ClearNode const & cs, ::osg::CopyOp const & copyop=SHALLOW_COPY )
    : osg::ClearNode( boost::ref(cs), boost::ref(copyop) )
      , bp::wrapper< osg::ClearNode >(){
        // constructor
    
    }

    virtual void accept( ::osg::NodeVisitor & nv ) {
        if( bp::override func_accept = this->get_override( "accept" ) )
            func_accept( boost::ref(nv) );
        else{
            this->osg::ClearNode::accept( boost::ref(nv) );
        }
    }
    
    void default_accept( ::osg::NodeVisitor & nv ) {
        osg::ClearNode::accept( boost::ref(nv) );
    }

    virtual char const * className(  ) const  {
        if( bp::override func_className = this->get_override( "className" ) )
            return func_className(  );
        else{
            return this->osg::ClearNode::className(  );
        }
    }
    
    char const * default_className(  ) const  {
        return osg::ClearNode::className( );
    }

    virtual ::osg::Object * clone( ::osg::CopyOp const & copyop ) const  {
        if( bp::override func_clone = this->get_override( "clone" ) )
            return func_clone( boost::ref(copyop) );
        else{
            return this->osg::ClearNode::clone( boost::ref(copyop) );
        }
    }
    
    ::osg::Object * default_clone( ::osg::CopyOp const & copyop ) const  {
        return osg::ClearNode::clone( boost::ref(copyop) );
    }

    virtual ::osg::Object * cloneType(  ) const  {
        if( bp::override func_cloneType = this->get_override( "cloneType" ) )
            return func_cloneType(  );
        else{
            return this->osg::ClearNode::cloneType(  );
        }
    }
    
    ::osg::Object * default_cloneType(  ) const  {
        return osg::ClearNode::cloneType( );
    }

    virtual bool isSameKindAs( ::osg::Object const * obj ) const  {
        if( bp::override func_isSameKindAs = this->get_override( "isSameKindAs" ) )
            return func_isSameKindAs( boost::python::ptr(obj) );
        else{
            return this->osg::ClearNode::isSameKindAs( boost::python::ptr(obj) );
        }
    }
    
    bool default_isSameKindAs( ::osg::Object const * obj ) const  {
        return osg::ClearNode::isSameKindAs( boost::python::ptr(obj) );
    }

    virtual char const * libraryName(  ) const  {
        if( bp::override func_libraryName = this->get_override( "libraryName" ) )
            return func_libraryName(  );
        else{
            return this->osg::ClearNode::libraryName(  );
        }
    }
    
    char const * default_libraryName(  ) const  {
        return osg::ClearNode::libraryName( );
    }

    virtual bool addChild( ::osg::Node * child ) {
        if( bp::override func_addChild = this->get_override( "addChild" ) )
            return func_addChild( boost::python::ptr(child) );
        else{
            return this->osg::Group::addChild( boost::python::ptr(child) );
        }
    }
    
    bool default_addChild( ::osg::Node * child ) {
        return osg::Group::addChild( boost::python::ptr(child) );
    }

    virtual ::osg::Camera * asCamera(  ) {
        if( bp::override func_asCamera = this->get_override( "asCamera" ) )
            return func_asCamera(  );
        else{
            return this->osg::Node::asCamera(  );
        }
    }
    
    ::osg::Camera * default_asCamera(  ) {
        return osg::Node::asCamera( );
    }

    virtual ::osg::Camera const * asCamera(  ) const  {
        if( bp::override func_asCamera = this->get_override( "asCamera" ) )
            return func_asCamera(  );
        else{
            return this->osg::Node::asCamera(  );
        }
    }
    
    ::osg::Camera const * default_asCamera(  ) const  {
        return osg::Node::asCamera( );
    }

    virtual ::osg::Geode * asGeode(  ) {
        if( bp::override func_asGeode = this->get_override( "asGeode" ) )
            return func_asGeode(  );
        else{
            return this->osg::Node::asGeode(  );
        }
    }
    
    ::osg::Geode * default_asGeode(  ) {
        return osg::Node::asGeode( );
    }

    virtual ::osg::Geode const * asGeode(  ) const  {
        if( bp::override func_asGeode = this->get_override( "asGeode" ) )
            return func_asGeode(  );
        else{
            return this->osg::Node::asGeode(  );
        }
    }
    
    ::osg::Geode const * default_asGeode(  ) const  {
        return osg::Node::asGeode( );
    }

    virtual ::osg::Group * asGroup(  ) {
        if( bp::override func_asGroup = this->get_override( "asGroup" ) )
            return func_asGroup(  );
        else{
            return this->osg::Group::asGroup(  );
        }
    }
    
    ::osg::Group * default_asGroup(  ) {
        return osg::Group::asGroup( );
    }

    virtual ::osg::Group const * asGroup(  ) const  {
        if( bp::override func_asGroup = this->get_override( "asGroup" ) )
            return func_asGroup(  );
        else{
            return this->osg::Group::asGroup(  );
        }
    }
    
    ::osg::Group const * default_asGroup(  ) const  {
        return osg::Group::asGroup( );
    }

    virtual ::osg::Switch * asSwitch(  ) {
        if( bp::override func_asSwitch = this->get_override( "asSwitch" ) )
            return func_asSwitch(  );
        else{
            return this->osg::Node::asSwitch(  );
        }
    }
    
    ::osg::Switch * default_asSwitch(  ) {
        return osg::Node::asSwitch( );
    }

    virtual ::osg::Switch const * asSwitch(  ) const  {
        if( bp::override func_asSwitch = this->get_override( "asSwitch" ) )
            return func_asSwitch(  );
        else{
            return this->osg::Node::asSwitch(  );
        }
    }
    
    ::osg::Switch const * default_asSwitch(  ) const  {
        return osg::Node::asSwitch( );
    }

    virtual ::osgTerrain::Terrain * asTerrain(  ) {
        if( bp::override func_asTerrain = this->get_override( "asTerrain" ) )
            return func_asTerrain(  );
        else{
            return this->osg::Node::asTerrain(  );
        }
    }
    
    ::osgTerrain::Terrain * default_asTerrain(  ) {
        return osg::Node::asTerrain( );
    }

    virtual ::osgTerrain::Terrain const * asTerrain(  ) const  {
        if( bp::override func_asTerrain = this->get_override( "asTerrain" ) )
            return func_asTerrain(  );
        else{
            return this->osg::Node::asTerrain(  );
        }
    }
    
    ::osgTerrain::Terrain const * default_asTerrain(  ) const  {
        return osg::Node::asTerrain( );
    }

    virtual ::osg::Transform * asTransform(  ) {
        if( bp::override func_asTransform = this->get_override( "asTransform" ) )
            return func_asTransform(  );
        else{
            return this->osg::Node::asTransform(  );
        }
    }
    
    ::osg::Transform * default_asTransform(  ) {
        return osg::Node::asTransform( );
    }

    virtual ::osg::Transform const * asTransform(  ) const  {
        if( bp::override func_asTransform = this->get_override( "asTransform" ) )
            return func_asTransform(  );
        else{
            return this->osg::Node::asTransform(  );
        }
    }
    
    ::osg::Transform const * default_asTransform(  ) const  {
        return osg::Node::asTransform( );
    }

    virtual void ascend( ::osg::NodeVisitor & nv ) {
        if( bp::override func_ascend = this->get_override( "ascend" ) )
            func_ascend( boost::ref(nv) );
        else{
            this->osg::Node::ascend( boost::ref(nv) );
        }
    }
    
    void default_ascend( ::osg::NodeVisitor & nv ) {
        osg::Node::ascend( boost::ref(nv) );
    }

    virtual ::osg::BoundingSphere computeBound(  ) const  {
        if( bp::override func_computeBound = this->get_override( "computeBound" ) )
            return func_computeBound(  );
        else{
            return this->osg::Group::computeBound(  );
        }
    }
    
    ::osg::BoundingSphere default_computeBound(  ) const  {
        return osg::Group::computeBound( );
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

    virtual bool insertChild( unsigned int index, ::osg::Node * child ) {
        if( bp::override func_insertChild = this->get_override( "insertChild" ) )
            return func_insertChild( index, boost::python::ptr(child) );
        else{
            return this->osg::Group::insertChild( index, boost::python::ptr(child) );
        }
    }
    
    bool default_insertChild( unsigned int index, ::osg::Node * child ) {
        return osg::Group::insertChild( index, boost::python::ptr(child) );
    }

    virtual void releaseGLObjects( ::osg::State * arg0=0 ) const  {
        if( bp::override func_releaseGLObjects = this->get_override( "releaseGLObjects" ) )
            func_releaseGLObjects( boost::python::ptr(arg0) );
        else{
            this->osg::Group::releaseGLObjects( boost::python::ptr(arg0) );
        }
    }
    
    void default_releaseGLObjects( ::osg::State * arg0=0 ) const  {
        osg::Group::releaseGLObjects( boost::python::ptr(arg0) );
    }

    virtual bool removeChildren( unsigned int pos, unsigned int numChildrenToRemove ) {
        if( bp::override func_removeChildren = this->get_override( "removeChildren" ) )
            return func_removeChildren( pos, numChildrenToRemove );
        else{
            return this->osg::Group::removeChildren( pos, numChildrenToRemove );
        }
    }
    
    bool default_removeChildren( unsigned int pos, unsigned int numChildrenToRemove ) {
        return osg::Group::removeChildren( pos, numChildrenToRemove );
    }

    virtual bool replaceChild( ::osg::Node * origChild, ::osg::Node * newChild ) {
        if( bp::override func_replaceChild = this->get_override( "replaceChild" ) )
            return func_replaceChild( boost::python::ptr(origChild), boost::python::ptr(newChild) );
        else{
            return this->osg::Group::replaceChild( boost::python::ptr(origChild), boost::python::ptr(newChild) );
        }
    }
    
    bool default_replaceChild( ::osg::Node * origChild, ::osg::Node * newChild ) {
        return osg::Group::replaceChild( boost::python::ptr(origChild), boost::python::ptr(newChild) );
    }

    virtual void resizeGLObjectBuffers( unsigned int maxSize ) {
        if( bp::override func_resizeGLObjectBuffers = this->get_override( "resizeGLObjectBuffers" ) )
            func_resizeGLObjectBuffers( maxSize );
        else{
            this->osg::Group::resizeGLObjectBuffers( maxSize );
        }
    }
    
    void default_resizeGLObjectBuffers( unsigned int maxSize ) {
        osg::Group::resizeGLObjectBuffers( maxSize );
    }

    virtual bool setChild( unsigned int i, ::osg::Node * node ) {
        if( bp::override func_setChild = this->get_override( "setChild" ) )
            return func_setChild( i, boost::python::ptr(node) );
        else{
            return this->osg::Group::setChild( i, boost::python::ptr(node) );
        }
    }
    
    bool default_setChild( unsigned int i, ::osg::Node * node ) {
        return osg::Group::setChild( i, boost::python::ptr(node) );
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
            this->osg::Group::setThreadSafeRefUnref( threadSafe );
        }
    }
    
    void default_setThreadSafeRefUnref( bool threadSafe ) {
        osg::Group::setThreadSafeRefUnref( threadSafe );
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

    virtual void traverse( ::osg::NodeVisitor & nv ) {
        if( bp::override func_traverse = this->get_override( "traverse" ) )
            func_traverse( boost::ref(nv) );
        else{
            this->osg::Group::traverse( boost::ref(nv) );
        }
    }
    
    void default_traverse( ::osg::NodeVisitor & nv ) {
        osg::Group::traverse( boost::ref(nv) );
    }

};

void register_ClearNode_class(){

    { //::osg::ClearNode
        typedef bp::class_< ClearNode_wrapper, bp::bases< osg::Group >, boost::noncopyable > ClearNode_exposer_t;
        ClearNode_exposer_t ClearNode_exposer = ClearNode_exposer_t( "ClearNode", bp::no_init );
        bp::scope ClearNode_scope( ClearNode_exposer );
        ClearNode_exposer.def( bp::init< >() );
        ClearNode_exposer.def( bp::init< osg::ClearNode const &, bp::optional< osg::CopyOp const & > >(( bp::arg("cs"), bp::arg("copyop")=SHALLOW_COPY )) );
        bp::implicitly_convertible< osg::ClearNode const &, osg::ClearNode >();
        { //::osg::ClearNode::accept
        
            typedef void ( ::osg::ClearNode::*accept_function_type)( ::osg::NodeVisitor & ) ;
            typedef void ( ClearNode_wrapper::*default_accept_function_type)( ::osg::NodeVisitor & ) ;
            
            ClearNode_exposer.def( 
                "accept"
                , accept_function_type(&::osg::ClearNode::accept)
                , default_accept_function_type(&ClearNode_wrapper::default_accept)
                , ( bp::arg("nv") ) );
        
        }
        { //::osg::ClearNode::className
        
            typedef char const * ( ::osg::ClearNode::*className_function_type)(  ) const;
            typedef char const * ( ClearNode_wrapper::*default_className_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "className"
                , className_function_type(&::osg::ClearNode::className)
                , default_className_function_type(&ClearNode_wrapper::default_className) );
        
        }
        { //::osg::ClearNode::clone
        
            typedef ::osg::Object * ( ::osg::ClearNode::*clone_function_type)( ::osg::CopyOp const & ) const;
            typedef ::osg::Object * ( ClearNode_wrapper::*default_clone_function_type)( ::osg::CopyOp const & ) const;
            
            ClearNode_exposer.def( 
                "clone"
                , clone_function_type(&::osg::ClearNode::clone)
                , default_clone_function_type(&ClearNode_wrapper::default_clone)
                , ( bp::arg("copyop") )
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::ClearNode::cloneType
        
            typedef ::osg::Object * ( ::osg::ClearNode::*cloneType_function_type)(  ) const;
            typedef ::osg::Object * ( ClearNode_wrapper::*default_cloneType_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "cloneType"
                , cloneType_function_type(&::osg::ClearNode::cloneType)
                , default_cloneType_function_type(&ClearNode_wrapper::default_cloneType)
                , bp::return_value_policy< bp::reference_existing_object >() );
        
        }
        { //::osg::ClearNode::getClearColor
        
            typedef ::osg::Vec4 const & ( ::osg::ClearNode::*getClearColor_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "getClearColor"
                , getClearColor_function_type( &::osg::ClearNode::getClearColor )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::ClearNode::getClearMask
        
            typedef ::GLbitfield ( ::osg::ClearNode::*getClearMask_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "getClearMask"
                , getClearMask_function_type( &::osg::ClearNode::getClearMask ) );
        
        }
        { //::osg::ClearNode::getRequiresClear
        
            typedef bool ( ::osg::ClearNode::*getRequiresClear_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "getRequiresClear"
                , getRequiresClear_function_type( &::osg::ClearNode::getRequiresClear ) );
        
        }
        { //::osg::ClearNode::isSameKindAs
        
            typedef bool ( ::osg::ClearNode::*isSameKindAs_function_type)( ::osg::Object const * ) const;
            typedef bool ( ClearNode_wrapper::*default_isSameKindAs_function_type)( ::osg::Object const * ) const;
            
            ClearNode_exposer.def( 
                "isSameKindAs"
                , isSameKindAs_function_type(&::osg::ClearNode::isSameKindAs)
                , default_isSameKindAs_function_type(&ClearNode_wrapper::default_isSameKindAs)
                , ( bp::arg("obj") ) );
        
        }
        { //::osg::ClearNode::libraryName
        
            typedef char const * ( ::osg::ClearNode::*libraryName_function_type)(  ) const;
            typedef char const * ( ClearNode_wrapper::*default_libraryName_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "libraryName"
                , libraryName_function_type(&::osg::ClearNode::libraryName)
                , default_libraryName_function_type(&ClearNode_wrapper::default_libraryName) );
        
        }
        { //::osg::ClearNode::setClearColor
        
            typedef void ( ::osg::ClearNode::*setClearColor_function_type)( ::osg::Vec4 const & ) ;
            
            ClearNode_exposer.def( 
                "setClearColor"
                , setClearColor_function_type( &::osg::ClearNode::setClearColor )
                , ( bp::arg("color") ) );
        
        }
        { //::osg::ClearNode::setClearMask
        
            typedef void ( ::osg::ClearNode::*setClearMask_function_type)( ::GLbitfield ) ;
            
            ClearNode_exposer.def( 
                "setClearMask"
                , setClearMask_function_type( &::osg::ClearNode::setClearMask )
                , ( bp::arg("mask") ) );
        
        }
        { //::osg::ClearNode::setRequiresClear
        
            typedef void ( ::osg::ClearNode::*setRequiresClear_function_type)( bool ) ;
            
            ClearNode_exposer.def( 
                "setRequiresClear"
                , setRequiresClear_function_type( &::osg::ClearNode::setRequiresClear )
                , ( bp::arg("requiresClear") ) );
        
        }
        { //::osg::Group::addChild
        
            typedef bool ( ::osg::Group::*addChild_function_type)( ::osg::Node * ) ;
            typedef bool ( ClearNode_wrapper::*default_addChild_function_type)( ::osg::Node * ) ;
            
            ClearNode_exposer.def( 
                "addChild"
                , addChild_function_type(&::osg::Group::addChild)
                , default_addChild_function_type(&ClearNode_wrapper::default_addChild)
                , ( bp::arg("child") ) );
        
        }
        { //::osg::Node::asCamera
        
            typedef ::osg::Camera * ( ::osg::Node::*asCamera_function_type)(  ) ;
            typedef ::osg::Camera * ( ClearNode_wrapper::*default_asCamera_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "asCamera"
                , asCamera_function_type(&::osg::Node::asCamera)
                , default_asCamera_function_type(&ClearNode_wrapper::default_asCamera)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asCamera
        
            typedef ::osg::Camera const * ( ::osg::Node::*asCamera_function_type)(  ) const;
            typedef ::osg::Camera const * ( ClearNode_wrapper::*default_asCamera_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "asCamera"
                , asCamera_function_type(&::osg::Node::asCamera)
                , default_asCamera_function_type(&ClearNode_wrapper::default_asCamera)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asGeode
        
            typedef ::osg::Geode * ( ::osg::Node::*asGeode_function_type)(  ) ;
            typedef ::osg::Geode * ( ClearNode_wrapper::*default_asGeode_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "asGeode"
                , asGeode_function_type(&::osg::Node::asGeode)
                , default_asGeode_function_type(&ClearNode_wrapper::default_asGeode)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asGeode
        
            typedef ::osg::Geode const * ( ::osg::Node::*asGeode_function_type)(  ) const;
            typedef ::osg::Geode const * ( ClearNode_wrapper::*default_asGeode_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "asGeode"
                , asGeode_function_type(&::osg::Node::asGeode)
                , default_asGeode_function_type(&ClearNode_wrapper::default_asGeode)
                    /* undefined call policies */ );
        
        }
        { //::osg::Group::asGroup
        
            typedef ::osg::Group * ( ::osg::Group::*asGroup_function_type)(  ) ;
            typedef ::osg::Group * ( ClearNode_wrapper::*default_asGroup_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "asGroup"
                , asGroup_function_type(&::osg::Group::asGroup)
                , default_asGroup_function_type(&ClearNode_wrapper::default_asGroup)
                    /* undefined call policies */ );
        
        }
        { //::osg::Group::asGroup
        
            typedef ::osg::Group const * ( ::osg::Group::*asGroup_function_type)(  ) const;
            typedef ::osg::Group const * ( ClearNode_wrapper::*default_asGroup_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "asGroup"
                , asGroup_function_type(&::osg::Group::asGroup)
                , default_asGroup_function_type(&ClearNode_wrapper::default_asGroup)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asSwitch
        
            typedef ::osg::Switch * ( ::osg::Node::*asSwitch_function_type)(  ) ;
            typedef ::osg::Switch * ( ClearNode_wrapper::*default_asSwitch_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "asSwitch"
                , asSwitch_function_type(&::osg::Node::asSwitch)
                , default_asSwitch_function_type(&ClearNode_wrapper::default_asSwitch)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asSwitch
        
            typedef ::osg::Switch const * ( ::osg::Node::*asSwitch_function_type)(  ) const;
            typedef ::osg::Switch const * ( ClearNode_wrapper::*default_asSwitch_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "asSwitch"
                , asSwitch_function_type(&::osg::Node::asSwitch)
                , default_asSwitch_function_type(&ClearNode_wrapper::default_asSwitch)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asTerrain
        
            typedef ::osgTerrain::Terrain * ( ::osg::Node::*asTerrain_function_type)(  ) ;
            typedef ::osgTerrain::Terrain * ( ClearNode_wrapper::*default_asTerrain_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "asTerrain"
                , asTerrain_function_type(&::osg::Node::asTerrain)
                , default_asTerrain_function_type(&ClearNode_wrapper::default_asTerrain)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asTerrain
        
            typedef ::osgTerrain::Terrain const * ( ::osg::Node::*asTerrain_function_type)(  ) const;
            typedef ::osgTerrain::Terrain const * ( ClearNode_wrapper::*default_asTerrain_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "asTerrain"
                , asTerrain_function_type(&::osg::Node::asTerrain)
                , default_asTerrain_function_type(&ClearNode_wrapper::default_asTerrain)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asTransform
        
            typedef ::osg::Transform * ( ::osg::Node::*asTransform_function_type)(  ) ;
            typedef ::osg::Transform * ( ClearNode_wrapper::*default_asTransform_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "asTransform"
                , asTransform_function_type(&::osg::Node::asTransform)
                , default_asTransform_function_type(&ClearNode_wrapper::default_asTransform)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::asTransform
        
            typedef ::osg::Transform const * ( ::osg::Node::*asTransform_function_type)(  ) const;
            typedef ::osg::Transform const * ( ClearNode_wrapper::*default_asTransform_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "asTransform"
                , asTransform_function_type(&::osg::Node::asTransform)
                , default_asTransform_function_type(&ClearNode_wrapper::default_asTransform)
                    /* undefined call policies */ );
        
        }
        { //::osg::Node::ascend
        
            typedef void ( ::osg::Node::*ascend_function_type)( ::osg::NodeVisitor & ) ;
            typedef void ( ClearNode_wrapper::*default_ascend_function_type)( ::osg::NodeVisitor & ) ;
            
            ClearNode_exposer.def( 
                "ascend"
                , ascend_function_type(&::osg::Node::ascend)
                , default_ascend_function_type(&ClearNode_wrapper::default_ascend)
                , ( bp::arg("nv") ) );
        
        }
        { //::osg::Group::computeBound
        
            typedef ::osg::BoundingSphere ( ::osg::Group::*computeBound_function_type)(  ) const;
            typedef ::osg::BoundingSphere ( ClearNode_wrapper::*default_computeBound_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "computeBound"
                , computeBound_function_type(&::osg::Group::computeBound)
                , default_computeBound_function_type(&ClearNode_wrapper::default_computeBound) );
        
        }
        { //::osg::Object::computeDataVariance
        
            typedef void ( ::osg::Object::*computeDataVariance_function_type)(  ) ;
            typedef void ( ClearNode_wrapper::*default_computeDataVariance_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "computeDataVariance"
                , computeDataVariance_function_type(&::osg::Object::computeDataVariance)
                , default_computeDataVariance_function_type(&ClearNode_wrapper::default_computeDataVariance) );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced * ( ::osg::Object::*getUserData_function_type)(  ) ;
            typedef ::osg::Referenced * ( ClearNode_wrapper::*default_getUserData_function_type)(  ) ;
            
            ClearNode_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&ClearNode_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Object::getUserData
        
            typedef ::osg::Referenced const * ( ::osg::Object::*getUserData_function_type)(  ) const;
            typedef ::osg::Referenced const * ( ClearNode_wrapper::*default_getUserData_function_type)(  ) const;
            
            ClearNode_exposer.def( 
                "getUserData"
                , getUserData_function_type(&::osg::Object::getUserData)
                , default_getUserData_function_type(&ClearNode_wrapper::default_getUserData)
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::Group::insertChild
        
            typedef bool ( ::osg::Group::*insertChild_function_type)( unsigned int,::osg::Node * ) ;
            typedef bool ( ClearNode_wrapper::*default_insertChild_function_type)( unsigned int,::osg::Node * ) ;
            
            ClearNode_exposer.def( 
                "insertChild"
                , insertChild_function_type(&::osg::Group::insertChild)
                , default_insertChild_function_type(&ClearNode_wrapper::default_insertChild)
                , ( bp::arg("index"), bp::arg("child") ) );
        
        }
        { //::osg::Group::releaseGLObjects
        
            typedef void ( ::osg::Group::*releaseGLObjects_function_type)( ::osg::State * ) const;
            typedef void ( ClearNode_wrapper::*default_releaseGLObjects_function_type)( ::osg::State * ) const;
            
            ClearNode_exposer.def( 
                "releaseGLObjects"
                , releaseGLObjects_function_type(&::osg::Group::releaseGLObjects)
                , default_releaseGLObjects_function_type(&ClearNode_wrapper::default_releaseGLObjects)
                , ( bp::arg("arg0")=bp::object() ) );
        
        }
        { //::osg::Group::removeChildren
        
            typedef bool ( ::osg::Group::*removeChildren_function_type)( unsigned int,unsigned int ) ;
            typedef bool ( ClearNode_wrapper::*default_removeChildren_function_type)( unsigned int,unsigned int ) ;
            
            ClearNode_exposer.def( 
                "removeChildren"
                , removeChildren_function_type(&::osg::Group::removeChildren)
                , default_removeChildren_function_type(&ClearNode_wrapper::default_removeChildren)
                , ( bp::arg("pos"), bp::arg("numChildrenToRemove") ) );
        
        }
        { //::osg::Group::replaceChild
        
            typedef bool ( ::osg::Group::*replaceChild_function_type)( ::osg::Node *,::osg::Node * ) ;
            typedef bool ( ClearNode_wrapper::*default_replaceChild_function_type)( ::osg::Node *,::osg::Node * ) ;
            
            ClearNode_exposer.def( 
                "replaceChild"
                , replaceChild_function_type(&::osg::Group::replaceChild)
                , default_replaceChild_function_type(&ClearNode_wrapper::default_replaceChild)
                , ( bp::arg("origChild"), bp::arg("newChild") ) );
        
        }
        { //::osg::Group::resizeGLObjectBuffers
        
            typedef void ( ::osg::Group::*resizeGLObjectBuffers_function_type)( unsigned int ) ;
            typedef void ( ClearNode_wrapper::*default_resizeGLObjectBuffers_function_type)( unsigned int ) ;
            
            ClearNode_exposer.def( 
                "resizeGLObjectBuffers"
                , resizeGLObjectBuffers_function_type(&::osg::Group::resizeGLObjectBuffers)
                , default_resizeGLObjectBuffers_function_type(&ClearNode_wrapper::default_resizeGLObjectBuffers)
                , ( bp::arg("maxSize") ) );
        
        }
        { //::osg::Group::setChild
        
            typedef bool ( ::osg::Group::*setChild_function_type)( unsigned int,::osg::Node * ) ;
            typedef bool ( ClearNode_wrapper::*default_setChild_function_type)( unsigned int,::osg::Node * ) ;
            
            ClearNode_exposer.def( 
                "setChild"
                , setChild_function_type(&::osg::Group::setChild)
                , default_setChild_function_type(&ClearNode_wrapper::default_setChild)
                , ( bp::arg("i"), bp::arg("node") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( ::std::string const & ) ;
            typedef void ( ClearNode_wrapper::*default_setName_function_type)( ::std::string const & ) ;
            
            ClearNode_exposer.def( 
                "setName"
                , setName_function_type(&::osg::Object::setName)
                , default_setName_function_type(&ClearNode_wrapper::default_setName)
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Object::setName
        
            typedef void ( ::osg::Object::*setName_function_type)( char const * ) ;
            
            ClearNode_exposer.def( 
                "setName"
                , setName_function_type( &::osg::Object::setName )
                , ( bp::arg("name") ) );
        
        }
        { //::osg::Group::setThreadSafeRefUnref
        
            typedef void ( ::osg::Group::*setThreadSafeRefUnref_function_type)( bool ) ;
            typedef void ( ClearNode_wrapper::*default_setThreadSafeRefUnref_function_type)( bool ) ;
            
            ClearNode_exposer.def( 
                "setThreadSafeRefUnref"
                , setThreadSafeRefUnref_function_type(&::osg::Group::setThreadSafeRefUnref)
                , default_setThreadSafeRefUnref_function_type(&ClearNode_wrapper::default_setThreadSafeRefUnref)
                , ( bp::arg("threadSafe") ) );
        
        }
        { //::osg::Object::setUserData
        
            typedef void ( ::osg::Object::*setUserData_function_type)( ::osg::Referenced * ) ;
            typedef void ( ClearNode_wrapper::*default_setUserData_function_type)( ::osg::Referenced * ) ;
            
            ClearNode_exposer.def( 
                "setUserData"
                , setUserData_function_type(&::osg::Object::setUserData)
                , default_setUserData_function_type(&ClearNode_wrapper::default_setUserData)
                , ( bp::arg("obj") ) );
        
        }
        { //::osg::Group::traverse
        
            typedef void ( ::osg::Group::*traverse_function_type)( ::osg::NodeVisitor & ) ;
            typedef void ( ClearNode_wrapper::*default_traverse_function_type)( ::osg::NodeVisitor & ) ;
            
            ClearNode_exposer.def( 
                "traverse"
                , traverse_function_type(&::osg::Group::traverse)
                , default_traverse_function_type(&ClearNode_wrapper::default_traverse)
                , ( bp::arg("nv") ) );
        
        }
    }

}
