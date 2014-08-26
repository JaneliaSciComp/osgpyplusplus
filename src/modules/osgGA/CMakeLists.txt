find_library(OSGGA_LIBRARY 
    NAME osgGA
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "wrap_osgGA.h")
OSGPYPP_WRAP_MODULE(osgGA)
target_link_libraries(osgGA 
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGGA_LIBRARY})

# Establish a linear chain of wrapper dependencies
# osg<-osgDB<-osgGA<-osgUtil<-osgViewer<-?
if(OSGPYPP_REGENERATE_BINDINGS)
	add_dependencies(Generate_osgGA_WrapperSources Generate_osgDB_WrapperSources)
endif()
