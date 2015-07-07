find_library(OSGDB_LIBRARY 
    NAME osgDB
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "wrap_osgDB.h")
OSGPYPP_WRAP_MODULE(_osgDB)
target_link_libraries(_osgDB 
    ${OSG_LIBRARY}
    ${OSGUTIL_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGDB_LIBRARY})

# Establish a linear chain of wrapper dependencies
# osg<-osgUtil<-osgDB<-osgGA<-osgText<-osgViewer
if(OSGPYPP_REGENERATE_BINDINGS)
	add_dependencies(Generate__osgDB_WrapperSources Generate__osgUtil_WrapperSources)
endif()
