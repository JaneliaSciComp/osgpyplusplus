#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osg2cpp"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB

#include <osg/ArgumentParser>
#include <osg/ApplicationUsage>

#include <osgDB/ReadFile>
#include <osgDB/FileNameUtils>
#include <osgDB/fstream>

#include <iostream>

# Search in str for all occurences of spat and replace them with rpat.
def searchAndReplace(str, spat, rpat):
    pos =  0
    while pos = str.find(spat, pos) : != str.npos :
        str.replace(pos, spat.length(), rpat)
        pos += rpat.length()

def writeShader(shader, cppFileName, variableName):
    fout = osgDB.ofstream(cppFileName.c_str())
    if !fout :
        print "Error: could not open file `", cppFileName, "` for writing."

    shaderSource =  shader.getShaderSource()
    searchAndReplace(shaderSource, "\r\n", "\n")
    searchAndReplace(shaderSource, "\r", "\n")
    searchAndReplace(shaderSource, "\"", "\\\"")
 
    variableString =  str("char ")+variableName+str("[] = ")
    
    startOfLine =  0
    endOfLine =  shaderSource.find_first_of('\n', startOfLine)
    
    if endOfLine==str.npos : 
        fout, variableString, shaderSource, "\\n\""
    else:
        padding = str(variableString.size(),' ')

        fout, variableString, "\"", shaderSource.substr(startOfLine,endOfLine-startOfLine), "\\n\""
        startOfLine = endOfLine+1
        endOfLine = shaderSource.find_first_of('\n', startOfLine)

        while endOfLine != str.npos :
            fout, padding, "\"", shaderSource.substr(startOfLine,endOfLine-startOfLine), "\\n\""
            startOfLine = endOfLine + 1
            endOfLine = shaderSource.find_first_of('\n', startOfLine)
        fout, padding, "\"", shaderSource.substr(startOfLine,endOfLine-startOfLine), "\\n\""
    print "Written shader to `", cppFileName, "`"

def main(argc, argv):
    # use an ArgumentParser object to manage the program arguments.
    arguments = osg.ArgumentParser(argc,argv)
    
    # set up the usage document, in case we need to print out how to use this program.
    arguments.getApplicationUsage().setApplicationName(arguments.getApplicationName())
    arguments.getApplicationUsage().setDescription(arguments.getApplicationName()+" is a utility for converting glsl shader files into char arrays that can be compiled into applications.")
    arguments.getApplicationUsage().setCommandLineUsage(arguments.getApplicationName()+" [options] filename ...")
    arguments.getApplicationUsage().addCommandLineOption("--shader <filename>","Shader file to create a .cpp file for.")
    arguments.getApplicationUsage().addCommandLineOption("-h or --help","Display command line parameters")

    # if user request help write it out to cout.
    if arguments.read("-h") || arguments.read("--help") :
        arguments.getApplicationUsage().write(std.cout)
        return 1
    
    filename = str()
    if arguments.read("--shader",filename) :
        osg.ref_ptr<osg.Shader> shader = osgDB.readShaderFile(filename)
        if shader.valid() :
            name =  osgDB.getStrippedName(filename)
            path =  osgDB.getFilePath(filename)
            invalidCharacters =  "-+/\\*=()[]:<>,.?@'~#`!\""
            numbericCharacters =  "0123456789"
            pos =  name.find_first_of(invalidCharacters)
            while pos != str.npos :
                name[pos] = '_'
                pos = name.find_first_of(invalidCharacters)
            
            ext =  osgDB.getFileExtension(filename)
            cppFileName =  osgDB.concatPaths(path, name + "_" + ext + ".cpp")
            variableName =  name + "_" + ext
            writeShader(shader.get(), cppFileName, variableName)

            return 0
        else:
            print "Error: could not find file '", filename, "'"
            return 1
        

    print "No appropriate command line options used."

    arguments.getApplicationUsage().write(std.cout)
    return 1


if __name__ == "__main__":
    main(sys.argv)
