// This file has been generated by Py++.

#include "boost/python.hpp"
#include "wrap_osg.h"
#include "mixinvector_less__unsigned_char__greater_.pypp.hpp"

namespace bp = boost::python;

void register_MixinVector_less__unsigned_char__greater__class(){

    { //::osg::MixinVector< unsigned char >
        typedef bp::class_< osg::MixinVector< unsigned char > > MixinVector_less__unsigned_char__greater__exposer_t;
        MixinVector_less__unsigned_char__greater__exposer_t MixinVector_less__unsigned_char__greater__exposer = MixinVector_less__unsigned_char__greater__exposer_t( "MixinVector_less__unsigned_char__greater_", bp::init< >() );
        bp::scope MixinVector_less__unsigned_char__greater__scope( MixinVector_less__unsigned_char__greater__exposer );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::init< size_t, bp::optional< unsigned char const & > >(( bp::arg("initial_size"), bp::arg("fill_value")=typename std::vector<T, std::allocator<_Elem> >::value_type() )) );
        bp::implicitly_convertible< size_t, osg::MixinVector< unsigned char > >();
        MixinVector_less__unsigned_char__greater__exposer.def( bp::init< std::vector< unsigned char > const & >(( bp::arg("other") )) );
        bp::implicitly_convertible< std::vector< unsigned char > const &, osg::MixinVector< unsigned char > >();
        MixinVector_less__unsigned_char__greater__exposer.def( bp::init< osg::MixinVector< unsigned char > const & >(( bp::arg("other") )) );
        { //::osg::MixinVector< unsigned char >::asVector
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::vector< unsigned char > & ( exported_class_t::*asVector_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "asVector"
                , asVector_function_type( &::osg::MixinVector< unsigned char >::asVector )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::MixinVector< unsigned char >::asVector
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::vector< unsigned char > const & ( exported_class_t::*asVector_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "asVector"
                , asVector_function_type( &::osg::MixinVector< unsigned char >::asVector )
                , bp::return_internal_reference< >() );
        
        }
        { //::osg::MixinVector< unsigned char >::assign
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*assign_function_type)( ::size_t,unsigned char const & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "assign"
                , assign_function_type( &::osg::MixinVector< unsigned char >::assign )
                , ( bp::arg("count"), bp::arg("value") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::at
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char const & ( exported_class_t::*at_function_type)( ::size_t ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "at"
                , at_function_type( &::osg::MixinVector< unsigned char >::at )
                , ( bp::arg("index") )
                , bp::return_value_policy< bp::copy_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::at
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char & ( exported_class_t::*at_function_type)( ::size_t ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "at"
                , at_function_type( &::osg::MixinVector< unsigned char >::at )
                , ( bp::arg("index") )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::back
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char const & ( exported_class_t::*back_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "back"
                , back_function_type( &::osg::MixinVector< unsigned char >::back )
                , bp::return_value_policy< bp::copy_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::back
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char & ( exported_class_t::*back_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "back"
                , back_function_type( &::osg::MixinVector< unsigned char >::back )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::begin
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::_Vector_const_iterator< unsigned char, std::allocator< unsigned char > > ( exported_class_t::*begin_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "begin"
                , begin_function_type( &::osg::MixinVector< unsigned char >::begin ) );
        
        }
        { //::osg::MixinVector< unsigned char >::begin
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > ( exported_class_t::*begin_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "begin"
                , begin_function_type( &::osg::MixinVector< unsigned char >::begin ) );
        
        }
        { //::osg::MixinVector< unsigned char >::capacity
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::size_t ( exported_class_t::*capacity_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "capacity"
                , capacity_function_type( &::osg::MixinVector< unsigned char >::capacity ) );
        
        }
        { //::osg::MixinVector< unsigned char >::clear
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*clear_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "clear"
                , clear_function_type( &::osg::MixinVector< unsigned char >::clear ) );
        
        }
        { //::osg::MixinVector< unsigned char >::empty
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef bool ( exported_class_t::*empty_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "empty"
                , empty_function_type( &::osg::MixinVector< unsigned char >::empty ) );
        
        }
        { //::osg::MixinVector< unsigned char >::end
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::_Vector_const_iterator< unsigned char, std::allocator< unsigned char > > ( exported_class_t::*end_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "end"
                , end_function_type( &::osg::MixinVector< unsigned char >::end ) );
        
        }
        { //::osg::MixinVector< unsigned char >::end
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > ( exported_class_t::*end_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "end"
                , end_function_type( &::osg::MixinVector< unsigned char >::end ) );
        
        }
        { //::osg::MixinVector< unsigned char >::erase
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > ( exported_class_t::*erase_function_type)( ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "erase"
                , erase_function_type( &::osg::MixinVector< unsigned char >::erase )
                , ( bp::arg("where") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::erase
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > ( exported_class_t::*erase_function_type)( ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > >,::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "erase"
                , erase_function_type( &::osg::MixinVector< unsigned char >::erase )
                , ( bp::arg("first"), bp::arg("last") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::front
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char const & ( exported_class_t::*front_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "front"
                , front_function_type( &::osg::MixinVector< unsigned char >::front )
                , bp::return_value_policy< bp::copy_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::front
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char & ( exported_class_t::*front_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "front"
                , front_function_type( &::osg::MixinVector< unsigned char >::front )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::get_allocator
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::allocator< unsigned char > ( exported_class_t::*get_allocator_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "get_allocator"
                , get_allocator_function_type( &::osg::MixinVector< unsigned char >::get_allocator ) );
        
        }
        { //::osg::MixinVector< unsigned char >::insert
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > ( exported_class_t::*insert_function_type)( ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > >,unsigned char const & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "insert"
                , insert_function_type( &::osg::MixinVector< unsigned char >::insert )
                , ( bp::arg("where"), bp::arg("value") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::insert
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*insert_function_type)( ::std::_Vector_iterator< unsigned char, std::allocator< unsigned char > >,::size_t,unsigned char const & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "insert"
                , insert_function_type( &::osg::MixinVector< unsigned char >::insert )
                , ( bp::arg("where"), bp::arg("count"), bp::arg("value") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::max_size
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::size_t ( exported_class_t::*max_size_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "max_size"
                , max_size_function_type( &::osg::MixinVector< unsigned char >::max_size ) );
        
        }
        { //::osg::MixinVector< unsigned char >::operator=
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::osg::MixinVector< unsigned char > & ( exported_class_t::*assign_function_type)( ::std::vector< unsigned char > const & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "assign"
                , assign_function_type( &::osg::MixinVector< unsigned char >::operator= )
                , ( bp::arg("other") )
                , bp::return_self< >() );
        
        }
        { //::osg::MixinVector< unsigned char >::operator=
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::osg::MixinVector< unsigned char > & ( exported_class_t::*assign_function_type)( ::osg::MixinVector< unsigned char > const & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "assign"
                , assign_function_type( &::osg::MixinVector< unsigned char >::operator= )
                , ( bp::arg("other") )
                , bp::return_self< >() );
        
        }
        { //::osg::MixinVector< unsigned char >::operator[]
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char const & ( exported_class_t::*__getitem___function_type)( ::size_t ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::MixinVector< unsigned char >::operator[] )
                , ( bp::arg("index") )
                , bp::return_value_policy< bp::copy_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::operator[]
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef unsigned char & ( exported_class_t::*__getitem___function_type)( ::size_t ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::osg::MixinVector< unsigned char >::operator[] )
                , ( bp::arg("index") )
                , bp::return_value_policy< bp::copy_non_const_reference >() );
        
        }
        { //::osg::MixinVector< unsigned char >::pop_back
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*pop_back_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "pop_back"
                , pop_back_function_type( &::osg::MixinVector< unsigned char >::pop_back ) );
        
        }
        { //::osg::MixinVector< unsigned char >::push_back
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*push_back_function_type)( unsigned char const & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "push_back"
                , push_back_function_type( &::osg::MixinVector< unsigned char >::push_back )
                , ( bp::arg("value") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::rbegin
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::reverse_iterator< std::_Vector_const_iterator< unsigned char, std::allocator< unsigned char > > > ( exported_class_t::*rbegin_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "rbegin"
                , rbegin_function_type( &::osg::MixinVector< unsigned char >::rbegin ) );
        
        }
        { //::osg::MixinVector< unsigned char >::rbegin
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::reverse_iterator< std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > > ( exported_class_t::*rbegin_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "rbegin"
                , rbegin_function_type( &::osg::MixinVector< unsigned char >::rbegin ) );
        
        }
        { //::osg::MixinVector< unsigned char >::rend
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::reverse_iterator< std::_Vector_const_iterator< unsigned char, std::allocator< unsigned char > > > ( exported_class_t::*rend_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "rend"
                , rend_function_type( &::osg::MixinVector< unsigned char >::rend ) );
        
        }
        { //::osg::MixinVector< unsigned char >::rend
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::std::reverse_iterator< std::_Vector_iterator< unsigned char, std::allocator< unsigned char > > > ( exported_class_t::*rend_function_type)(  ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "rend"
                , rend_function_type( &::osg::MixinVector< unsigned char >::rend ) );
        
        }
        { //::osg::MixinVector< unsigned char >::reserve
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*reserve_function_type)( ::size_t ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "reserve"
                , reserve_function_type( &::osg::MixinVector< unsigned char >::reserve )
                , ( bp::arg("new_capacity") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::resize
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*resize_function_type)( ::size_t,unsigned char const & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "resize"
                , resize_function_type( &::osg::MixinVector< unsigned char >::resize )
                , ( bp::arg("new_size"), bp::arg("fill_value")=typename std::vector<T, std::allocator<_Elem> >::value_type() ) );
        
        }
        { //::osg::MixinVector< unsigned char >::size
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef ::size_t ( exported_class_t::*size_function_type)(  ) const;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "size"
                , size_function_type( &::osg::MixinVector< unsigned char >::size ) );
        
        }
        { //::osg::MixinVector< unsigned char >::swap
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*swap_function_type)( ::std::vector< unsigned char > & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "swap"
                , swap_function_type( &::osg::MixinVector< unsigned char >::swap )
                , ( bp::arg("other") ) );
        
        }
        { //::osg::MixinVector< unsigned char >::swap
        
            typedef osg::MixinVector< unsigned char > exported_class_t;
            typedef void ( exported_class_t::*swap_function_type)( ::osg::MixinVector< unsigned char > & ) ;
            
            MixinVector_less__unsigned_char__greater__exposer.def( 
                "swap"
                , swap_function_type( &::osg::MixinVector< unsigned char >::swap )
                , ( bp::arg("other") ) );
        
        }
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self != bp::other< std::vector< unsigned char > >() );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self != bp::self );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self < bp::other< std::vector< unsigned char > >() );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self < bp::self );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self <= bp::other< std::vector< unsigned char > >() );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self <= bp::self );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self == bp::other< std::vector< unsigned char > >() );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self == bp::self );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self > bp::other< std::vector< unsigned char > >() );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self > bp::self );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self >= bp::other< std::vector< unsigned char > >() );
        MixinVector_less__unsigned_char__greater__exposer.def( bp::self >= bp::self );
    }

}
