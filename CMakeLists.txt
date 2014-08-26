project(OsgPyPlusPlus)

cmake_minimum_required(VERSION 2.8)

enable_testing()

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMakeModules")

set(STAGING_FOLDER "${PROJECT_BINARY_DIR}/stage")

add_subdirectory(src)

add_subdirectory(test)
