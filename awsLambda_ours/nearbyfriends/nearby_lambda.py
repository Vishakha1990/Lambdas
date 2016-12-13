from __future__ import print_function
import time
import uuid
import sys
import socket
import logging
import gpxpy.geo
import redis
from operator import itemgetter

 
r = redis.Redis(
     host='datanode-001.zumykb.0001.use2.cache.amazonaws.com',
     port=6379)
 

 
def get_distance(lat,querylat,querylong):
	splitloc = lat
	friendts = splitloc[0]
	friendlat = float(splitloc[1])
	friendlog = float(splitloc[2])
	return gpxpy.geo.haversine_distance(friendlat, friendlog, querylat, querylong)

def handler(event, context):
    #print("started")
	queryuserid = event['userid']
	print("Lambda Started")
	querylat = float(event['latitude'])
	querylong = float(event['longitude'])
	peoplelist = event['peopleinfo']
	#friendslist = r.smembers(queryuserid)
	dist = []
	for friend in peoplelist:
	    #calculating distance for each friend
	    allLocations = r.smembers(friend)
	    tupleList = []
	    for location in allLocations:
	    	tupleList.append(tuple(location.split(',')))
	    if(len(tupleList)>0):		
	    	lat_location = max(tupleList,key=itemgetter(0))
	    	dist.append(get_distance(lat_location,querylat,querylong))
	
	if(len(dist)>0):
		return min(dist)
	    	#print(minDistance)
	else:
	    	return 0
	

