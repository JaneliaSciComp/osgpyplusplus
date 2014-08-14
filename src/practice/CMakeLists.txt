include_directories(${CMAKE_CURRENT_SOURCE_DIR})
add_library(greet SHARED generated_code/greet_wrapped.cpp greet.cpp greet.h)
target_link_libraries(greet 
    ${PYTHON_LIBRARY_RELEASE}
    ${Boost_PYTHON_LIBRARY}
)
# On Windows python extension modules have suffix ".pyd"
set_target_properties(greet PROPERTIES SUFFIX .pyd)
