find_library(OSGDB_LIBRARY 
    NAME osgDB
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "wrap_osgDB.h")
OSGPYPP_WRAP_MODULE(osgDB)
target_link_libraries(osgDB 
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGDB_LIBRARY})

# Establish a linear chain of wrapper dependencies
# osg<-osgDB<-osgGA<-osgUtil<-osgViewer<-?
if(OSGPYPP_REGENERATE_BINDINGS)
	add_dependencies(Generate_osgDB_WrapperSources Generate_osg_WrapperSources)
endif()
