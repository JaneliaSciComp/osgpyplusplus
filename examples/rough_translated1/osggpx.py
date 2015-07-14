#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "osggpx"
# !!! This program will need manual tuning before it will work. !!!

import sys

from osgpypp import osg
from osgpypp import osgDB
from osgpypp import osgGA
from osgpypp import osgText
from osgpypp import osgViewer


# Translated from file 'osggpx.cpp'

# OpenSceneGraph example, osggpx.
#*
#*  Permission is hereby granted, free of charge, to any person obtaining a copy
#*  of this software and associated documentation files (the "Software"), to deal
#*  in the Software without restriction, including without limitation the rights
#*  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#*  copies of the Software, and to permit persons to whom the Software is
#*  furnished to do so, subject to the following conditions:
#*
#*  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#*  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#*  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#*  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#*  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#*  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#*  THE SOFTWARE.
#

#include <osg/Node>
#include <osg/Geometry>
#include <osg/Notify>
#include <osg/MatrixTransform>
#include <osg/Texture2D>
#include <osg/DrawPixels>
#include <osg/PolygonOffset>
#include <osg/Geode>
#include <osg/CoordinateSystemNode>

#include <osgDB/Registry>
#include <osgDB/ReadFile>
#include <osgDB/FileUtils>
#include <osgDB/FileNameUtils>
#include <osgDB/XmlParser>

#include <osgText/Text>

#include <osgGA/TerrainManipulator>
#include <osgViewer/Viewer>

class TrackSegment (osg.Object) :
    TrackSegment() 

    TrackSegment( TrackSegment ts,  osg.CopyOp=osg.CopyOp.SHALLOW_COPY) 

    META_Object(osg, TrackSegment)

    class TrackPoint :
TrackPoint():
            latitude(0.0),
            longitude(0.0),
            elevation(0.0),
            time(0.0) 

        latitude = double()
        longitude = double()
        elevation = double()
        time = double()
    

    typedef std.vector< TrackPoint > TrackPoints

    def addTrackPoint(trackPoint):

         _trackPoints.push_back(trackPoint) 

    def getTrackPoints():

         return _trackPoints 
    def getTrackPoints():
         return _trackPoints 
    virtual ~TrackSegment() 

    _trackPoints = TrackPoints()


class Track (osg.Object) :
    Track() 

    Track( Track track,  osg.CopyOp=osg.CopyOp.SHALLOW_COPY) 

    META_Object(osg, Track)

    typedef std.vector< TrackSegment > TrackSegments

    def addTrackSegment(trackSegment):

         _trackSegments.push_back(trackSegment) 

    def getTrackSegments():

         return _trackSegments 
    def getTrackSegments():
         return _trackSegments 

    virtual ~Track() 

    _trackSegments = TrackSegments()


def convertTime(timestr):

    
    osg.notify(osg.NOTICE), "       time = ", timestr
    return 0

def readTrack(filename):

    
    foundFilename = osgDB.findDataFile(filename)
    if foundFilename.empty() : return 0

    ext = osgDB.getFileExtension(foundFilename)
    if ext not ="gpx" : return 0

    input = osgDB.XmlNode.Input()
    input.open(foundFilename)
    input.readAllDataIntoBuffer()

    doc = osgDB.XmlNode()
    doc.read(input)

    root = 0
    for(osgDB.XmlNode.Children.iterator itr = doc.children.begin()
        not = doc.children.end()  and   not root
        ++itr)
        if *itr :.name=="gpx" : root = itr

    if  not root : return 0

    latitude = str("lat")
    longitude = str("lon")

    for(osgDB.XmlNode.Children.iterator itr = root.children.begin()
        not = root.children.end()
        ++itr)
        if *itr :.name=="rte" :
            track = Track()
            track.setName(filename)

            trackSegment = TrackSegment()
            for(osgDB.XmlNode.Children.iterator sitr = (*itr).children.begin()
                not = (*itr).children.end()
                ++sitr)
                if *sitr :.name=="rtept"  :
                    trkpt = sitr
                    point = TrackSegment.TrackPoint()
                    valid = False
                    if trkpt.properties.count(latitude) not =0 :
                        valid = True
                        point.latitude = osg.asciiToDouble(trkpt.properties[latitude].c_str())
                    if trkpt.properties.count(longitude) not =0 :
                        valid = True
                        point.longitude = osg.asciiToDouble(trkpt.properties[longitude].c_str())

                    for(osgDB.XmlNode.Children.iterator pitr = trkpt.children.begin()
                        not = trkpt.children.end()
                        ++pitr)
                        if *pitr :.name=="ele" : point.elevation = osg.asciiToDouble((*pitr).contents.c_str())
                        elif *pitr :.name=="time" : point.time = convertTime((*pitr).contents)

                    if valid :
                        osg.notify(osg.NOTICE), "  point.latitude=", point.latitude, ", longitude=", point.longitude, ", elev=", point.elevation, ", time=", point.time
                        trackSegment.addTrackPoint(point)


            if  not trackSegment.getTrackPoints().empty() :
                track.addTrackSegment(trackSegment)

            return track.release()
        elif *itr :.name=="trk" :
            track = Track()
            track.setName(filename)

            for(osgDB.XmlNode.Children.iterator citr = (*itr).children.begin()
                not = (*itr).children.end()
                ++citr)
                if *citr :.name=="trkseg" :
                    trackSegment = TrackSegment()
                    for(osgDB.XmlNode.Children.iterator sitr = (*citr).children.begin()
                        not = (*citr).children.end()
                        ++sitr)
                        if *sitr :.name=="trkpt"  or  (*sitr).name=="rtept"  :
                            trkpt = sitr
                            point = TrackSegment.TrackPoint()
                            valid = False
                            if trkpt.properties.count(latitude) not =0 :
                                valid = True
                                point.latitude = osg.asciiToDouble(trkpt.properties[latitude].c_str())
                            if trkpt.properties.count(longitude) not =0 :
                                valid = True
                                point.longitude = osg.asciiToDouble(trkpt.properties[longitude].c_str())

                            for(osgDB.XmlNode.Children.iterator pitr = trkpt.children.begin()
                                not = trkpt.children.end()
                                ++pitr)
                                if *pitr :.name=="ele" : point.elevation = osg.asciiToDouble((*pitr).contents.c_str())
                                elif *pitr :.name=="time" : point.time = convertTime((*pitr).contents)

                            if valid :
                                # osg.notify(osg.NOTICE), "  point.latitude=", point.latitude, ", longitude=", point.longitude, ", elev=", point.elevation, ", time=", point.time
                                trackSegment.addTrackPoint(point)
                    if  not trackSegment.getTrackPoints().empty() :
                        track.addTrackSegment(trackSegment)
            return track.release()

    return 0

def computeSmoothedTrackSegment(ts):

    
    if  not ts : return 0

    orig_points = ts.getTrackPoints()

    if orig_points.size()>2 :
        # only do smoothing if we have more than two points.
        new_ts = TrackSegment()

        new_points = new_ts.getTrackPoints()
        new_points.resize(orig_points.size())

        new_points[0] = orig_points[0]
        new_points[orig_points.size()-1] = orig_points[orig_points.size()-1]

        for(unsigned int i=1 i<orig_points.size()-1 ++i)
            new_points[i].latitude = (orig_points[i-1].latitude+orig_points[i].latitude+orig_points[i+1].latitude)/3.0
            new_points[i].longitude = (orig_points[i-1].longitude+orig_points[i].longitude+orig_points[i+1].longitude)/3.0
            new_points[i].elevation = (orig_points[i-1].elevation+orig_points[i].elevation+orig_points[i+1].elevation)/3.0
            new_points[i].time = (orig_points[i-1].time+orig_points[i].time+orig_points[i+1].time)/3.0
        return new_ts.release()
    else:
        # we have two or less points and can't do smoothing, so will just return original TrackSegment
        return ts


def computeAveragedSpeedTrackSegment(ts):

    
    if  not ts : return 0

    em = osg.EllipsoidModel()
    orig_points = ts.getTrackPoints()

    if orig_points.size()>2 :
        # only do smoothing if we have more than two points.
        new_ts = TrackSegment()


        # compute overall distance
        total_distance = 0
        for(unsigned int i=1 i<orig_points.size()-1 ++i)
            osg.Vec3d point_a, point_b
            em.convertLatLongHeightToXYZ(osg.DegreesToRadians(orig_points[i].latitude), osg.DegreesToRadians(orig_points[i].longitude), orig_points[i].elevation,
                                          point_a.x(), point_a.y(), point_a.z())
            em.convertLatLongHeightToXYZ(osg.DegreesToRadians(orig_points[i+1].latitude), osg.DegreesToRadians(orig_points[i+1].longitude), orig_points[i+1].elevation,
                                          point_b.x(), point_b.y(), point_b.z())
            total_distance += (point_b-point_a).length()

        total_time = orig_points[orig_points.size()-1].time - orig_points[0].time
        average_speed = total_distance/total_time

        OSG_NOTICE, "total_time = ", total_time
        OSG_NOTICE, "total_distance = ", total_distance
        OSG_NOTICE, "average_speed = ", average_speed

        new_points = new_ts.getTrackPoints()
        new_points.resize(orig_points.size())
        new_points[0] = orig_points[0]

        accumulated_distance = 0.0
        for(unsigned int i=0 i<orig_points.size()-1 ++i)
            osg.Vec3d point_a, point_b
            em.convertLatLongHeightToXYZ(osg.DegreesToRadians(orig_points[i].latitude), osg.DegreesToRadians(orig_points[i].longitude), orig_points[i].elevation,
                                          point_a.x(), point_a.y(), point_a.z())
            em.convertLatLongHeightToXYZ(osg.DegreesToRadians(orig_points[i+1].latitude), osg.DegreesToRadians(orig_points[i+1].longitude), orig_points[i+1].elevation,
                                          point_b.x(), point_b.y(), point_b.z())

            accumulated_distance += (point_b-point_a).length()

            new_points[i+1] = orig_points[i+1]
            new_points[i+1].time = accumulated_distance / average_speed
        return new_ts.release()
    else:
        # we have two or less points and can't do smoothing, so will just return original TrackSegment
        return ts


def computeAveragedSpeedTrack(track):

    
    new_track = Track()

    for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
        not = track.getTrackSegments().end()
        ++itr)
        new_track.addTrackSegment(computeAveragedSpeedTrackSegment(itr))

    return new_track.release()


def computeSmoothedTrack(track):


    
    new_track = Track()

    for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
        not = track.getTrackSegments().end()
        ++itr)
        new_track.addTrackSegment(computeSmoothedTrackSegment(itr))

    return new_track.release()

def createTrackModel(track, colour):

    
    em = osg.EllipsoidModel()

    geode = osg.Geode()

    for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
        not = track.getTrackSegments().end()
        ++itr)
        points = (*itr).getTrackPoints()
        if points.size()<2 : continue

        geometry = osg.Geometry()
        vertices = osg.Vec3Array()
        geometry.setVertexArray(vertices)
        vertices.resize(points.size())
        for(unsigned int i=0 i<points.size() ++i)
            point = osg.Vec3d()
            em.convertLatLongHeightToXYZ(osg.DegreesToRadians(points[i].latitude), osg.DegreesToRadians(points[i].longitude), points[i].elevation,
                                          point.x(), point.y(), point.z())

           (*vertices)[i] = point

        colours = osg.Vec4Array()
        colours.push_back(colour)
        geometry.setColorArray(colours, osg.Array.BIND_OVERALL)

        geometry.addPrimitiveSet(osg.DrawArrays(GL_LINE_STRIP, 0, points.size()))

        geode.addDrawable(geometry)

    geode.getOrCreateStateSet().setMode(GL_LIGHTING, osg.StateAttribute.OFF)

    return geode.release()

def main(argv, argc):

    
    arguments = osg.ArgumentParser(argv, argc)

    typedef std.list< Track > Tracks
    tracks = Tracks()

    average = False
    while arguments.read("-a")  or  arguments.read("--average") : average = True

    smooth = False
    while arguments.read("-s")  or  arguments.read("--smooth") : smooth = True

    outputFilename = str()
    while arguments.read("-o",outputFilename) : 

    trackFilename = str()
    while arguments.read("-t",trackFilename) :
        track = readTrack(trackFilename)
        if track.valid() : tracks.push_back(track)

    em = osg.EllipsoidModel()

    group = osg.Group()

    loadedModel = osgDB.readNodeFiles(arguments)
    if loadedModel.valid() : group.addChild(loadedModel)

    for(Tracks.iterator itr = tracks.begin()
        not = tracks.end()
        ++itr)
        track = itr

        group.addChild(createTrackModel(track, osg.Vec4(1.0,1.0,1.0,1.0)))

        # smooth the track
        if average :
            for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
                not = track.getTrackSegments().end()
                ++itr)
                *itr = computeAveragedSpeedTrackSegment(itr)

        # smooth the track
        if smooth :
            for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
                not = track.getTrackSegments().end()
                ++itr)
                *itr = computeSmoothedTrackSegment(itr)

            for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
                not = track.getTrackSegments().end()
                ++itr)
                *itr = computeSmoothedTrackSegment(itr)

            for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
                not = track.getTrackSegments().end()
                ++itr)
                *itr = computeSmoothedTrackSegment(itr)

            for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
                not = track.getTrackSegments().end()
                ++itr)
                *itr = computeSmoothedTrackSegment(itr)

        totalDistance = 0.0
        totalAscent = 0.0
        totalDescent = 0.0

        osg.notify(osg.NOTICE), "Track read ", track.getName()
        for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
            not = track.getTrackSegments().end()
            ++itr)
            ts = itr

            points = ts.getTrackPoints()
            if points.size()>1 :
                pitr = ts.getTrackPoints().begin()
                previousPos = osg.Vec3d()
                previousElevation = pitr.elevation
                em.convertLatLongHeightToXYZ(osg.DegreesToRadians(pitr.latitude), osg.DegreesToRadians(pitr.longitude), 0.0,
                                              previousPos.x(), previousPos.y(), previousPos.z())
                ++pitr

                for(
                    not = ts.getTrackPoints().end()
                    ++pitr)
                    newPos = osg.Vec3d()
                    newElevation = pitr.elevation
                    em.convertLatLongHeightToXYZ(osg.DegreesToRadians(pitr.latitude), osg.DegreesToRadians(pitr.longitude), 0.0,
                                                newPos.x(), newPos.y(), newPos.z())

                    distance = (newPos-previousPos).length()

                    totalDistance += distance
                    if newElevation>previousElevation : totalAscent += (newElevation-previousElevation)
                    else totalDescent += (previousElevation-newElevation)

                    osg.notify(osg.NOTICE), "     distance=", distance, ", ", newElevation-previousElevation

                    previousPos = newPos
                    previousElevation = newElevation

        metersToFeet = 1 / 0.3048
        metersToMiles = 1.0 / 1609.344

        osg.notify(osg.NOTICE), "totalDistance = ", totalDistance, "m, ", totalDistance*metersToMiles, " miles"
        osg.notify(osg.NOTICE), "totalAscent = ", totalAscent, "m, ", totalAscent*metersToFeet, "ft"
        osg.notify(osg.NOTICE), "totalDescent = ", totalDescent, "m, ", totalDescent*metersToFeet, "ft"


    if  not outputFilename.empty() :
        fout = std.ofstream(outputFilename.c_str())

         xml version=\"1.0\" encoding=\"utf-8\"?><gpx version=\"1.0\" creator=\"osggpx\" xmlns:xsi=\"http:#www.w3.org/2001/XMLSchema-instance\" xmlns=\"http:#www.topografix.com/GPX/1/0\" xsi:schemaLocation=\"http:#www.topografix.com/GPX/1/0 http:#www.topografix.com/GPX/1/0/gpx.xsd\">", std: if (fout, "<) else endl

        for(Tracks.iterator itr = tracks.begin()
            not = tracks.end()
            ++itr)
            track = itr

            fout, "<trk>"
            fout, "<desc>The track description</desc>"
            for(Track.TrackSegments.iterator itr = track.getTrackSegments().begin()
                not = track.getTrackSegments().end()
                ++itr)
                ts = itr
                fout, "<trkseg>"

                for(TrackSegment.TrackPoints.iterator pitr = ts.getTrackPoints().begin()
                    not = ts.getTrackPoints().end()
                    ++pitr)
                    fout, "<trkpt lat=\"", pitr.latitude, "\" lon=\"", pitr.longitude, "\">"
                    fout, "<ele>", pitr.elevation, "</ele>"
                    fout, "<time>", pitr.time, "</time>"
                    fout, "</trkpt>"

                fout, "</trkseg>"

            fout, "</trk>"
        fout, "</gpx>"

    viewer = osgViewer.Viewer(arguments)
    viewer.setCameraManipulator(osgGA.TerrainManipulator)()
    viewer.setSceneData(group)
    return viewer.run()



if __name__ == "__main__":
    main(sys.argv)
