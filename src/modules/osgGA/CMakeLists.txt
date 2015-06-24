find_library(OSGGA_LIBRARY 
    NAME osgGA
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "wrap_osgGA.h")
OSGPYPP_WRAP_MODULE(_osgGA)
target_link_libraries(_osgGA 
    ${OSG_LIBRARY}
    ${OPENTHREADS_LIBRARY}
    ${OSGGA_LIBRARY})

# Establish a linear chain of wrapper dependencies
# osg<-osgDB<-osgGA<-osgUtil<-osgViewer<-?
if(OSGPYPP_REGENERATE_BINDINGS)
	add_dependencies(Generate__osgGA_WrapperSources Generate__osgUtil_WrapperSources)
	add_dependencies(Generate__osgGA_WrapperSources Generate__osg_WrapperSources)
endif()
