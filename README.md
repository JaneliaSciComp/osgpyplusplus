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
