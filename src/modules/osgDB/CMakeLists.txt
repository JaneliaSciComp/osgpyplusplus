find_library(OSG_DB_LIBRARY 
    NAME osgDB
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "")
OSGPYPP_WRAP_MODULE(osgDB)
target_link_libraries(osgDB 
    ${OSG_LIBRARY}
    ${OSG_DB_LIBRARY})
