/*
Copyright (c) 2014, Howard Hughes Medical Institute, All rights reserved.
Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
  * Redistributions of source code must retain the above copyright notice, 
  this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice, 
  this list of conditions and the following disclaimer in the documentation 
  and/or other materials provided with the distribution.
  * Neither the name of the Howard Hughes Medical Institute nor the names of 
  its contributors may be used to endorse or promote products derived from 
  this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, ANY 
IMPLIED WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, OR FITNESS FOR A 
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
REASONABLE ROYALTIES; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

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

    static bool const has_copyable_iter = true;
    static bool const has_mutable_ref   = true;
    static bool const has_find          = true;
    static bool const has_insert        = true;
    static bool const has_erase         = true;
    static bool const has_pop_back      = false;
    static bool const has_push_back     = true;
    static bool const is_reorderable    = true;
  
    BOOST_STATIC_CONSTANT(
        method_set_type,
        supported_methods = (
              method_len
              | method_getitem
              | method_getitem_slice
        //      | method_index // compile error
              | method_setitem
              | method_setitem_slice
        //     | method_contains // compile error
        //    | method_count // compile error
              // | method_delitem // compile error
              // | method_delitem_slice
              // | method_reverse
              | method_append
              // | method_insert // compile error
              | method_extend
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
