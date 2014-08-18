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
find_path(OSG_DIR "include/osg/Node")
find_path(OSG_INCLUDE_DIR "osg/Node"
    PATHS ${OSG_DIR})
include_directories(${OSG_INCLUDE_DIR})
find_library(OSG_LIBRARY 
    NAME osg
    PATHS ${OSG_DIR}/lib
)

set(OSGPYPP_REGENERATE_BINDINGS FALSE CACHE BOOL "Whether to regenerate boost python C++ binding source code")

SET(OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/stage")
SET( CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG "${OUTPUT_DIRECTORY}")
SET( CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE "${OUTPUT_DIRECTORY}")
SET( CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG "${OUTPUT_DIRECTORY}")
SET( CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE "${OUTPUT_DIRECTORY}")
SET( CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG "${OUTPUT_DIRECTORY}")
SET( CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE "${OUTPUT_DIRECTORY}")

add_definitions("-DBOOST_PYTHON_MAX_ARITY=18")

################

# Define function to wrap each module the same way, within each module's subfolder
function (OSGPYPP_WRAP_MODULE MODULE_NAME)
    file(GLOB MODULE_GENERATED_SRCS "generated_code/*.cpp" "generated_code/*.hpp")

    include_directories(${CMAKE_CURRENT_SOURCE_DIR})
    include_directories(${CMAKE_CURRENT_SOURCE_DIR}/generated_code)

    set(MODULE_SRCS ${MODULE_GENERATED_SRCS} ${MODULE_OTHER_SRCS})
    add_library(${MODULE_NAME} SHARED ${MODULE_SRCS})
    target_link_libraries(${MODULE_NAME} 
        ${PYTHON_LIBRARY_RELEASE}
        ${Boost_PYTHON_LIBRARY}
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
                ${MODULE_OTHER_SRCS}
            WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
            COMMENT "Creating ${MODULE_NAME} wrapper source files.  Examine generate_greet_source.err file for details"
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

add_subdirectory(osg)
add_subdirectory(osgDB)
