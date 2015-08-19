# Copyright (c) 2014, Howard Hughes Medical Institute, All rights reserved.
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright notice, 
#   this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation 
#   and/or other materials provided with the distribution.
#   * Neither the name of the Howard Hughes Medical Institute nor the names of 
#   its contributors may be used to endorse or promote products derived from 
#   this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, ANY 
# IMPLIED WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, OR FITNESS FOR A 
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# REASONABLE ROYALTIES; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Find OpenSceneGraph, and incorporate OSG version into osgpypp version
find_path(OSG_DIR "include/osg/Node")
find_program(OSGVERSION_EXE osgversion PATHS "${OSG_DIR}/bin" NO_DEFAULT_PATH)
execute_process(COMMAND "${OSGVERSION_EXE}" OUTPUT_VARIABLE OSGVERSION_EXE_OUT)
# message(STATUS ${OSGVERSION_EXE_OUT})
string(REGEX MATCH "[0-9\\.]+" OSG_VERSION_STRING ${OSGVERSION_EXE_OUT})
message(STATUS "OpenSceneGraph version " ${OSG_VERSION_STRING})

# Increment OSGPYPP_PATCH_VERSION with each release of osgpyplusplus
set(OSGPYPP_PATCH_VERSION 04)
set(OSGPYPP_VERSION_STRING ${OSG_VERSION_STRING}${OSGPYPP_PATCH_VERSION})

configure_file(setup.py.in "${STAGING_FOLDER}/setup.py" @ONLY)

# Copy python source modules to staging area
file(GLOB PY_SRCS "osgpypp/*.py")
foreach(SRC ${PY_SRCS})
    file(COPY ${SRC} DESTINATION "${STAGING_FOLDER}/osgpypp/")
endforeach()
file(GLOB PY_IN_SRCS "osgpypp/*.py.in")
foreach(SRC ${PY_IN_SRCS})
    get_filename_component(BASENAME ${SRC} NAME_WE)
    configure_file(${SRC} "${STAGING_FOLDER}/osgpypp/${BASENAME}.py" @ONLY)
endforeach()

# Copy binary exension modules into second level staging folder
set(MODULE_STAGING_FOLDER ${STAGING_FOLDER}/osgpypp)
add_subdirectory(modules)
