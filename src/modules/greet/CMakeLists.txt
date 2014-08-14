file(GLOB MODULE_GENERATED_SRCS "generated_code/*.cpp" "generated_code/*.hpp")
set(MODULE_OTHER_SRCS greet.cpp greet.h)

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/generated_code)

file(GLOB MODULE_GENERATED_SRCS "generated_code/*.cpp" "generated_code/*.hpp")
set(MODULE_SRCS ${MODULE_GENERATED_SRCS} ${MODULE_OTHER_SRCS})
add_library(greet SHARED ${MODULE_SRCS})
target_link_libraries(greet 
    ${PYTHON_LIBRARY_RELEASE}
    ${Boost_PYTHON_LIBRARY}
)
# On Windows python extension modules have suffix ".pyd"
if(WIN32)
    set_target_properties(greet PROPERTIES SUFFIX .pyd)
endif()

# Maybe generate boost python C++ wrapping code, using pyplusplus
if(OSGPYPP_REGENERATE_BINDINGS)
    find_program(PYTHON_EXECUTABLE 
        NAMES python27 python)
    set(WRAP_SCRIPT wrap_greet.py)
    # Create file generate_std.stamp to indicate successful completion of 
    # generate step. Because it is possible that no generated sources will be updated.
    set(GEN_STAMP "${CMAKE_CURRENT_SOURCE_DIR}/generated_code/generate_greet.stamp")
    add_custom_command(
        COMMAND "${PYTHON_EXECUTABLE}" ${WRAP_SCRIPT}
            > "${CMAKE_CURRENT_BINARY_DIR}/generate_greet_source.log"
            2> "${CMAKE_CURRENT_BINARY_DIR}/generate_greet_source.err"
        OUTPUT "${STDGEN_STAMP}"
        DEPENDS
            ${WRAP_SCRIPT}
            ${MODULE_OTHER_SRCS}
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
        COMMENT "Creating greet wrapper source files.  Examine generate_greet_source.err file for details"
    )

    add_custom_target(GenerateGreetWrapperSources
        DEPENDS "${STDGEN_STAMP}"
        SOURCES
            ${WRAP_SCRIPT}
            ${MODULE_OTHER_SRCS}
    )
    add_dependencies(greet GenerateGreetWrapperSources) # TODO - not working?
endif()
