#ifndef OSGPYPP_WRAP_REFERENCED_H
#define OSGPYPP_WRAP_REFERENCED_H

#include <osg/ref_ptr>
#include <osg/CopyOp>
#include "boost/python.hpp"

// Tell boost::python that osg::ref_ptr is a smart pointer class
namespace boost { namespace python {
  template <class T> struct pointee< osg::ref_ptr<T> >
  { typedef T type; };
} } // namespace boost::python

// Work around pyplusplus deficiency in defining default argument values
static int SHALLOW_COPY = osg::CopyOp::SHALLOW_COPY;

#endif // OSGPYPP_WRAP_REFERENCED_H
