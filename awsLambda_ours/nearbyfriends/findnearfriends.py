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

def handler():
	"""
	This function puts into memcache and get from it.
	Memcache is hosted using elasticache
	"""
	#r = redis.Redis(
	#host='datanode-001.zumykb.0001.use2.cache.amazonaws.com',
	#port=6379)
	logging.info('created redis client')
	
	queryuserid = sys.argv[1]
	querylat = float(sys.argv[2])
	querylong = float(sys.argv[3])
	friendslist = r.smembers(queryuserid)
	
	dist = []
	for friend in friendslist:
	    #calculating distance for each friend
	    allLocations = r.smembers("userdata:"+friend)
	    tupleList = []
	    for location in allLocations:
	    	tupleList.append(tuple(location.split(',')))
	    if(len(tupleList)>0):		
	    	lat_location = max(tupleList,key=itemgetter(0))
	    	dist.append(get_distance(lat_location,querylat,querylong))
	
	if(len(dist)>0):
		minDistance = min(dist)
	    	print(minDistance)
	else:
	    	print ("No friends found")
	
	return "Fetched value from memcache: "



def main(argv):
    handler()


if __name__ == "__main__":
    main(sys.argv)


