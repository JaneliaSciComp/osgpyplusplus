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

#ifndef OSGPYPP_WRAP_REFERENCED_H
#define OSGPYPP_WRAP_REFERENCED_H

#include <osg/ref_ptr>
#include <osg/CopyOp>
#include <osg/StateAttribute>
#include <osg/DisplaySettings>
#include "boost/python.hpp"

// Tell boost::python that osg::ref_ptr is a smart pointer class
namespace boost { namespace python {
  template <class T> struct pointee< osg::ref_ptr<T> >
  { typedef T type; };
} } // namespace boost::python

// Work around pyplusplus deficiency in defining default argument values
static int SHALLOW_COPY = osg::CopyOp::SHALLOW_COPY;
static int ON = ::osg::StateAttribute::ON;
static int OFF = ::osg::StateAttribute::OFF;
static int DEFAULT_IMPLICIT_BUFFER_ATTACHMENT = ::osg::DisplaySettings::DEFAULT_IMPLICIT_BUFFER_ATTACHMENT;

#endif // OSGPYPP_WRAP_REFERENCED_H
