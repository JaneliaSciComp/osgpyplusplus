find_library(OSGVIEWER_LIBRARY 
    NAME osgViewer
    PATHS ${OSG_DIR}/lib
)

set(MODULE_OTHER_SRCS "wrap_osgViewer.h")
OSGPYPP_WRAP_MODULE(osgViewer)
target_link_libraries(osgViewer 
    ${OPENTHREADS_LIBRARY}
    ${OSG_LIBRARY}
    ${OSGGA_LIBRARY}
    ${OSGVIEWER_LIBRARY})

# Establish a linear chain of wrapper dependencies
# osg<-osgDB<-osgGA<-osgUtil<-osgViewer<-?
if(OSGPYPP_REGENERATE_BINDINGS)
	add_dependencies(Generate_osgViewer_WrapperSources Generate_osg_WrapperSources)
	add_dependencies(Generate_osgViewer_WrapperSources Generate_osgUtil_WrapperSources)
	add_dependencies(Generate_osgViewer_WrapperSources Generate_osgDB_WrapperSources)
	add_dependencies(Generate_osgViewer_WrapperSources Generate_osgGA_WrapperSources)
	add_dependencies(Generate_osgViewer_WrapperSources Generate_osgText_WrapperSources)
endif()
