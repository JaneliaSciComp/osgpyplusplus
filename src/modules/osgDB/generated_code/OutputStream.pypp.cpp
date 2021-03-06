// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osgdb.h"
#include "outputstream.pypp.hpp"

namespace bp = boost::python;

void register_OutputStream_class(){

    { //::osgDB::OutputStream
        typedef bp::class_< osgDB::OutputStream, boost::noncopyable > OutputStream_exposer_t;
        OutputStream_exposer_t OutputStream_exposer = OutputStream_exposer_t( "OutputStream", bp::init< osgDB::Options const * >(( bp::arg("options") )) );
        bp::scope OutputStream_scope( OutputStream_exposer );
        bp::enum_< osgDB::OutputStream::WriteImageHint>("WriteImageHint")
            .value("WRITE_USE_IMAGE_HINT", osgDB::OutputStream::WRITE_USE_IMAGE_HINT)
            .value("WRITE_USE_EXTERNAL", osgDB::OutputStream::WRITE_USE_EXTERNAL)
            .value("WRITE_INLINE_DATA", osgDB::OutputStream::WRITE_INLINE_DATA)
            .value("WRITE_INLINE_FILE", osgDB::OutputStream::WRITE_INLINE_FILE)
            .value("WRITE_EXTERNAL_FILE", osgDB::OutputStream::WRITE_EXTERNAL_FILE)
            .export_values()
            ;
        bp::enum_< osgDB::OutputStream::WriteType>("WriteType")
            .value("WRITE_UNKNOWN", osgDB::OutputStream::WRITE_UNKNOWN)
            .value("WRITE_SCENE", osgDB::OutputStream::WRITE_SCENE)
            .value("WRITE_IMAGE", osgDB::OutputStream::WRITE_IMAGE)
            .value("WRITE_OBJECT", osgDB::OutputStream::WRITE_OBJECT)
            .export_values()
            ;
        bp::implicitly_convertible< osgDB::Options const *, osgDB::OutputStream >();
        { //::osgDB::OutputStream::compress
        
            typedef void ( ::osgDB::OutputStream::*compress_function_type)( ::std::ostream * ) ;
            
            OutputStream_exposer.def( 
                "compress"
                , compress_function_type( &::osgDB::OutputStream::compress )
                , ( bp::arg("ostream") ) );
        
        }
        { //::osgDB::OutputStream::getException
        
            typedef ::osgDB::OutputException const * ( ::osgDB::OutputStream::*getException_function_type)(  ) const;
            
            OutputStream_exposer.def( 
                "getException"
                , getException_function_type( &::osgDB::OutputStream::getException )
                , bp::return_internal_reference< >() );
        
        }
        { //::osgDB::OutputStream::getFileVersion
        
            typedef int ( ::osgDB::OutputStream::*getFileVersion_function_type)( ::std::string const & ) const;
            
            OutputStream_exposer.def( 
                "getFileVersion"
                , getFileVersion_function_type( &::osgDB::OutputStream::getFileVersion )
                , ( bp::arg("d")=std::basic_string<char, std::char_traits<char>, std::allocator<char> >() ) );
        
        }
        { //::osgDB::OutputStream::getOptions
        
            typedef ::osgDB::Options const * ( ::osgDB::OutputStream::*getOptions_function_type)(  ) const;
            
            OutputStream_exposer.def( 
                "getOptions"
                , getOptions_function_type( &::osgDB::OutputStream::getOptions )
                , bp::return_internal_reference< >() );
        
        }
        { //::osgDB::OutputStream::getSchemaName
        
            typedef ::std::string const & ( ::osgDB::OutputStream::*getSchemaName_function_type)(  ) const;
            
            OutputStream_exposer.def( 
                "getSchemaName"
                , getSchemaName_function_type( &::osgDB::OutputStream::getSchemaName )
                , bp::return_value_policy< bp::copy_const_reference >() );
        
        }
        { //::osgDB::OutputStream::getWriteImageHint
        
            typedef ::osgDB::OutputStream::WriteImageHint ( ::osgDB::OutputStream::*getWriteImageHint_function_type)(  ) const;
            
            OutputStream_exposer.def( 
                "getWriteImageHint"
                , getWriteImageHint_function_type( &::osgDB::OutputStream::getWriteImageHint ) );
        
        }
        { //::osgDB::OutputStream::isBinary
        
            typedef bool ( ::osgDB::OutputStream::*isBinary_function_type)(  ) const;
            
            OutputStream_exposer.def( 
                "isBinary"
                , isBinary_function_type( &::osgDB::OutputStream::isBinary ) );
        
        }
        { //::osgDB::OutputStream::setFileVersion
        
            typedef void ( ::osgDB::OutputStream::*setFileVersion_function_type)( ::std::string const &,int ) ;
            
            OutputStream_exposer.def( 
                "setFileVersion"
                , setFileVersion_function_type( &::osgDB::OutputStream::setFileVersion )
                , ( bp::arg("d"), bp::arg("v") ) );
        
        }
        { //::osgDB::OutputStream::setOutputIterator
        
            typedef void ( ::osgDB::OutputStream::*setOutputIterator_function_type)( ::osgDB::OutputIterator * ) ;
            
            OutputStream_exposer.def( 
                "setOutputIterator"
                , setOutputIterator_function_type( &::osgDB::OutputStream::setOutputIterator )
                , ( bp::arg("oi") ) );
        
        }
        { //::osgDB::OutputStream::setWriteImageHint
        
            typedef void ( ::osgDB::OutputStream::*setWriteImageHint_function_type)( ::osgDB::OutputStream::WriteImageHint ) ;
            
            OutputStream_exposer.def( 
                "setWriteImageHint"
                , setWriteImageHint_function_type( &::osgDB::OutputStream::setWriteImageHint )
                , ( bp::arg("hint") ) );
        
        }
        { //::osgDB::OutputStream::start
        
            typedef void ( ::osgDB::OutputStream::*start_function_type)( ::osgDB::OutputIterator *,::osgDB::OutputStream::WriteType ) ;
            
            OutputStream_exposer.def( 
                "start"
                , start_function_type( &::osgDB::OutputStream::start )
                , ( bp::arg("outIterator"), bp::arg("type") ) );
        
        }
        { //::osgDB::OutputStream::throwException
        
            typedef void ( ::osgDB::OutputStream::*throwException_function_type)( ::std::string const & ) ;
            
            OutputStream_exposer.def( 
                "throwException"
                , throwException_function_type( &::osgDB::OutputStream::throwException )
                , ( bp::arg("msg") ) );
        
        }
        { //::osgDB::OutputStream::writeArray
        
            typedef void ( ::osgDB::OutputStream::*writeArray_function_type)( ::osg::Array const * ) ;
            
            OutputStream_exposer.def( 
                "writeArray"
                , writeArray_function_type( &::osgDB::OutputStream::writeArray )
                , ( bp::arg("a") ) );
        
        }
        { //::osgDB::OutputStream::writeCharArray
        
            typedef void ( ::osgDB::OutputStream::*writeCharArray_function_type)( char const *,unsigned int ) ;
            
            OutputStream_exposer.def( 
                "writeCharArray"
                , writeCharArray_function_type( &::osgDB::OutputStream::writeCharArray )
                , ( bp::arg("s"), bp::arg("size") ) );
        
        }
        { //::osgDB::OutputStream::writeImage
        
            typedef void ( ::osgDB::OutputStream::*writeImage_function_type)( ::osg::Image const * ) ;
            
            OutputStream_exposer.def( 
                "writeImage"
                , writeImage_function_type( &::osgDB::OutputStream::writeImage )
                , ( bp::arg("img") ) );
        
        }
        { //::osgDB::OutputStream::writeObject
        
            typedef void ( ::osgDB::OutputStream::*writeObject_function_type)( ::osg::Object const * ) ;
            
            OutputStream_exposer.def( 
                "writeObject"
                , writeObject_function_type( &::osgDB::OutputStream::writeObject )
                , ( bp::arg("obj") ) );
        
        }
        { //::osgDB::OutputStream::writeObjectFields
        
            typedef void ( ::osgDB::OutputStream::*writeObjectFields_function_type)( ::osg::Object const * ) ;
            
            OutputStream_exposer.def( 
                "writeObjectFields"
                , writeObjectFields_function_type( &::osgDB::OutputStream::writeObjectFields )
                , ( bp::arg("obj") ) );
        
        }
        { //::osgDB::OutputStream::writePrimitiveSet
        
            typedef void ( ::osgDB::OutputStream::*writePrimitiveSet_function_type)( ::osg::PrimitiveSet const * ) ;
            
            OutputStream_exposer.def( 
                "writePrimitiveSet"
                , writePrimitiveSet_function_type( &::osgDB::OutputStream::writePrimitiveSet )
                , ( bp::arg("p") ) );
        
        }
        { //::osgDB::OutputStream::writeSchema
        
            typedef void ( ::osgDB::OutputStream::*writeSchema_function_type)( ::std::ostream & ) ;
            
            OutputStream_exposer.def( 
                "writeSchema"
                , writeSchema_function_type( &::osgDB::OutputStream::writeSchema )
                , ( bp::arg("fout") ) );
        
        }
        { //::osgDB::OutputStream::writeWrappedString
        
            typedef void ( ::osgDB::OutputStream::*writeWrappedString_function_type)( ::std::string const & ) ;
            
            OutputStream_exposer.def( 
                "writeWrappedString"
                , writeWrappedString_function_type( &::osgDB::OutputStream::writeWrappedString )
                , ( bp::arg("str") ) );
        
        }
        OutputStream_exposer.def_readwrite( "BEGIN_BRACKET", &osgDB::OutputStream::BEGIN_BRACKET );
        OutputStream_exposer.def_readwrite( "END_BRACKET", &osgDB::OutputStream::END_BRACKET );
        OutputStream_exposer.def_readwrite( "PROPERTY", &osgDB::OutputStream::PROPERTY );
    }

}
