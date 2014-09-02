osgpyplusplus
=============

Python bindings for OpenSceneGraph 3D graphics API, created using Boost.Python and Py++

There exist already two projects that provide python bindings for OpenSceneGraph: osgswig and osgboostpython. 
So why am I trying to create yet another?

Currency: osgswig has not been updated for a couple of years. So I created a fork of osgswig here on github,
and I modified osgswig to work with OpenSceneGraph version 3.2.1. I also added support to osgswig for the osgVolume
module. I learned enough about osgswig in this process to convince me that I would prefer to work with bindings
based on Boost.Python, rather than on SWIG.

Completeness: The osgboostpython project contains impressive manually coded bindings based on Boost.Python. I
predict that osgboostpython will never be complete, because manually coding those bindings is an overly ambitious
goal. So I have chosen to use the Py++ code generator to automate the creation of Boost.Python bindings for
OpenSceneGraph. I am fortunate to have the osgboostpython project available, to serve as a gold-standard touchstone
for what those automatically generated bindings should look like.

Control: I am maintaining an application (Neuroptikon) that depends critically on Python bindings for OpenSceneGraph.
I appreciate having both projects controlled by me, so I can improve them together, without necessarily needing to
negotiate features with others.

The Janelia Farm Research Campus Software Copyright 1.1
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
