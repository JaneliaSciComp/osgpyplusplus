#ifndef OSGPYPP_INDEXING_HELPERS_HPP_
#define OSGPYPP_INDEXING_HELPERS_HPP_

#include "indexing_suite/container_suite.hpp"
#include "indexing_suite/suite_utils.hpp"
#include "indexing_suite/list.hpp"

using namespace boost::python::indexing;

// Pyplusplus includes a copy of the unreleased boost.python indexing_suite version 2,
// which wraps python-like indexing behavior onto C++ containers.
// This indexing suite requires the construction of a special "container_traits" struct
// for each wrapped container.  The following SimTKVec_container_traits template struct
// is intended to help with the creation of this struct.  This struct will be invoked 
// in "add_registration_code" calls in generate_whatever_source.py wrapping scripts.

template<class VecType, class ElemType, class IndexType> struct OsgArray_container_traits {
    typedef VecType                        container;
    typedef int                            size_type;
    typedef ElemType                       value_type;
    typedef value_type*                    iterator;

    typedef value_type&                    reference;
    typedef value_type                     key_type;
    typedef IndexType                      index_type; // signed!

    typedef value_type                     value_param;
    typedef key_type                       key_param;
    typedef index_type                     index_param;

    static bool const has_copyable_iter = false;
    static bool const has_mutable_ref   = true;
    static bool const has_find          = true;
    static bool const has_insert        = false;
    static bool const has_erase         = false;
    static bool const has_pop_back      = false;
    static bool const has_push_back     = false;
    static bool const is_reorderable    = false;
  
    BOOST_STATIC_CONSTANT(
        method_set_type,
        supported_methods = (
              method_len
              | method_getitem
              | method_getitem_slice
        //    | method_index // requires begin and end methods, which Vec3 lacks
              | method_setitem
              | method_setitem_slice
        //    | method_contains // requires begin and end methods, which Vec3 lacks
        //    | method_count // compile error
        ));

    static boost::python::indexing::index_style_t const index_style
        = boost::python::indexing::index_style_linear;

    struct value_traits_ {
        // Traits information for our value_type
        static bool const equality_comparable = true;
        static bool const lessthan_comparable = false;
    };

    template<typename PythonClass, typename Policy>
        static void visit_container_class (PythonClass &, Policy const &)
    {
        // Empty
    }
};

#endif // OSGPYPP_INDEXING_HELPERS_HPP_
