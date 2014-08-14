add_library(greet SHARED greet_wrap.cpp)
target_link_libraries(greet 
    ${PYTHON_LIBRARY_RELEASE}
    ${Boost_PYTHON_LIBRARY}
)
# On Windows python extension modules have suffix ".pyd"
set_target_properties(greet PROPERTIES SUFFIX .pyd)
