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

# Python
find_package(PythonLibs REQUIRED)
mark_as_advanced(CLEAR PYTHON_INCLUDE_DIRS)
mark_as_advanced(CLEAR PYTHON_LIBRARIES)
include_directories(${PYTHON_INCLUDE_DIRS})
message(STATUS "Python version: ${PYTHONLIBS_VERSION_STRING}")
message(STATUS "Python library: ${PYTHON_LIBRARY_RELEASE}")

# Boost is required because we need boost python to build bindings
set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON)
set(Boost_ADDITIONAL_VERSIONS 1.56 1.56.0)
find_package(Boost COMPONENTS python REQUIRED)
# Avoid exposing confusing Cmake variables
mark_as_advanced(Boost_DIR)
mark_as_advanced(Boost_LIB_DIAGNOSTIC_DEFINITIONS)
mark_as_advanced(CLEAR Boost_INCLUDE_DIR)
mark_as_advanced(CLEAR Boost_PYTHON_LIBRARY_DEBUG)
mark_as_advanced(CLEAR Boost_PYTHON_LIBRARY_RELEASE)

include_directories(${Boost_INCLUDE_DIR})

# OpenSceneGraph TODO make this finding process more general
find_path(OSG_INCLUDE_DIR "osg/Node"
    PATHS ${OSG_DIR})
include_directories(${OSG_INCLUDE_DIR})
find_library(OPENTHREADS_LIBRARY 
    NAME OpenThreads
    PATHS ${OSG_DIR}/lib
)
find_library(OSG_LIBRARY 
    NAME osg
    PATHS ${OSG_DIR}/lib
)
find_library(OSGGA_LIBRARY 
    NAME osgGA
    PATHS ${OSG_DIR}/lib
)

# Copy DLLs to staging area for newborn python extension modules
# 1) OpenSceneGraph
file(GLOB OSG_RUNTIME_LIBS "${OSG_DIR}/bin/*.dll")
file(GLOB OSG_RUNTIME_DEBUG_LIBS "${OSG_DIR}/bin/*d.dll")
set(OSG_PLUGIN_FOLDER "osgPlugins-${OSG_VERSION_STRING}")
file(GLOB OSG_PLUGIN_LIBS "${OSG_DIR}/bin/${OSG_PLUGIN_FOLDER}/*.dll")
file(GLOB OSG_PLUGIN_DEBUG_LIBS "${OSG_DIR}/bin/${OSG_PLUGIN_FOLDER}/*d.dll")
# Copy release libraries, but not debug libraries
list(REMOVE_ITEM OSG_RUNTIME_LIBS ${OSG_RUNTIME_DEBUG_LIBS})
list(REMOVE_ITEM OSG_PLUGIN_LIBS ${OSG_PLUGIN_DEBUG_LIBS})
foreach(LIB ${OSG_RUNTIME_LIBS})
    file(COPY ${LIB} DESTINATION "${STAGING_FOLDER}/osgpypp")
endforeach()
foreach(LIB ${OSG_PLUGIN_LIBS})
    file(COPY ${LIB} DESTINATION "${STAGING_FOLDER}/osgpypp/${OSG_PLUGIN_FOLDER}/")
endforeach()
# 2) ZLIB - Maybe copy libs on Windows only? - needed by osgDB
find_package(ZLIB)
if (ZLIB_FOUND)
    message(STATUS "${ZLIB_INCLUDE_DIR}/../bin/")
    find_file(
        ZLIB_RUNTIME_LIBRARY
        NAMES zlib1.dll
        PATHS "${ZLIB_INCLUDE_DIR}/../bin/"
    )
    find_library(
        ZLIB_RUNTIME_LIBRARY
        NAMES zlib1 z
        PATHS "${ZLIB_INCLUDE_DIR}/../bin/"
    )
    file(COPY "${ZLIB_RUNTIME_LIBRARY}" DESTINATION "${STAGING_FOLDER}/osgpypp")
endif()
# 3) boost python 
get_filename_component(BOOSTPYTHON_LIB_BASE "${Boost_PYTHON_LIBRARY_RELEASE}" NAME_WE)
find_file(
    BOOST_PYTHON_RUNTIME_LIBRARY
    NAMES "${BOOSTPYTHON_LIB_BASE}.dll"
    PATHS "${Boost_LIBRARY_DIR}"
)
file(COPY "${BOOST_PYTHON_RUNTIME_LIBRARY}" DESTINATION "${STAGING_FOLDER}/osgpypp")
# 4) Collada library, needed for DAE loader plugin; OSG must have been built with DAE plugin too...
find_file(
    COLLADA_RUNTIME_LIBRARY
    NAMES libcollada14dom21.dll)
file(COPY "${COLLADA_RUNTIME_LIBRARY}" DESTINATION "${STAGING_FOLDER}/osgpypp")

set(OSGPYPP_REGENERATE_BINDINGS FALSE CACHE BOOL "Whether to regenerate boost python C++ binding source code")

SET( CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG "${MODULE_STAGING_FOLDER}")
SET( CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE "${MODULE_STAGING_FOLDER}")
SET( CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG "${MODULE_STAGING_FOLDER}")
SET( CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE "${MODULE_STAGING_FOLDER}")
SET( CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG "${MODULE_STAGING_FOLDER}")
SET( CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE "${MODULE_STAGING_FOLDER}")

add_definitions("-DBOOST_PYTHON_MAX_ARITY=18")

# So we can include "wrap_referenced.h"
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

################

# Define function to wrap each module the same way, within each module's subfolder
function (OSGPYPP_WRAP_MODULE MODULE_NAME)
    file(GLOB MODULE_GENERATED_SRCS "generated_code/*.cpp" "generated_code/*.hpp")

    include_directories(${CMAKE_CURRENT_SOURCE_DIR})
    include_directories(${CMAKE_CURRENT_SOURCE_DIR}/generated_code)

    set(MODULE_SRCS ${MODULE_GENERATED_SRCS} ${MODULE_OTHER_SRCS})
    add_library(${MODULE_NAME} SHARED ${MODULE_SRCS})
    target_link_libraries(${MODULE_NAME} 
        ${Boost_PYTHON_LIBRARY}
        ${PYTHON_LIBRARY_RELEASE}
        ${OSG_LIBRARY}
    )
    # On Windows python extension modules have suffix ".pyd"
    if(WIN32)
        set_target_properties(${MODULE_NAME} PROPERTIES SUFFIX .pyd)
    endif()

    # Maybe generate boost python C++ wrapping code, using pyplusplus
    if(OSGPYPP_REGENERATE_BINDINGS)
        find_program(PYTHON_EXECUTABLE 
            NAMES python27 python)
        set(WRAP_SCRIPT wrap_module.py)
        # Create file generate_std.stamp to indicate successful completion of 
        # generate step. Because it is possible that no generated sources will be updated.
        set(GEN_STAMP "${CMAKE_CURRENT_SOURCE_DIR}/generated_code/generate_module.stamp")
        add_custom_command(
            COMMAND "${PYTHON_EXECUTABLE}" ${WRAP_SCRIPT}
                > "${CMAKE_CURRENT_BINARY_DIR}/generate_${MODULE_NAME}_source.log"
                2> "${CMAKE_CURRENT_BINARY_DIR}/generate_${MODULE_NAME}_source.err"
            OUTPUT "${GEN_STAMP}"
            DEPENDS
                ${WRAP_SCRIPT}
                "${CMAKE_SOURCE_DIRECTORY}/src/modules/wrap_helpers.py"
                ${MODULE_OTHER_SRCS}
            WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
            COMMENT "Creating ${MODULE_NAME} wrapper source files.  Examine generate_${MODULE_NAME}_source.err file for details"
        )

        add_custom_target(Generate_${MODULE_NAME}_WrapperSources
            DEPENDS "${GEN_STAMP}"
            SOURCES
                ${WRAP_SCRIPT}
                ${MODULE_OTHER_SRCS}
        )
        add_dependencies(${MODULE_NAME} Generate_${MODULE_NAME}_WrapperSources)
    endif()
endfunction()

####################

# For initial testing and debugging only...
# add_subdirectory(greet)

# Add module subdirectories in inverse order of linear dependency chain
add_subdirectory(osg)
add_subdirectory(osgUtil)
add_subdirectory(osgDB)
add_subdirectory(osgText)
add_subdirectory(osgGA)
add_subdirectory(osgViewer)
add_subdirectory(osgManipulator)
add_subdirectory(osgWidget)
add_subdirectory(osgFX)

# InstallOsgPyPPLocally is used as a prerequisite for unit tests
add_custom_target(InstallOsgPyPPLocally DEPENDS 
    _osg _osgDB _osgGA _osgUtil _osgViewer _osgText
    _osgManipulator _osgWidget)

# Only use the first two values in the python version for the install version, e.g. "2.7"
string(REGEX MATCH "^[0-9]+\\.[0-9]+" PY_TARGET_VERSION ${PYTHONLIBS_VERSION_STRING})
# message(${PY_TARGET_VERSION})
add_custom_target(InstallerWin32 ALL
    # We shoehorned version into X.Y.Z format so we can use msi instead of wininst
    ${PYTHON_EXECUTABLE} setup.py bdist_msi --target-version=${PY_TARGET_VERSION}
    DEPENDS InstallOsgPyPPLocally
    WORKING_DIRECTORY "${MODULE_STAGING_FOLDER}/.."
    COMMENT Creating Windows installer...
    SOURCES CMakeLists.txt "${PROJECT_SOURCE_DIR}/src/setup.py.in"
)    
