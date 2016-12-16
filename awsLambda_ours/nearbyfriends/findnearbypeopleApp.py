from __future__ import print_function
import time
import uuid
import sys
import socket
import logging
import gpxpy.geo
import redis
from operator import itemgetter
import requests
import json
import random
import heapq
from multiprocessing.dummy import Pool as ThreadPool

NearbyFriendsUrl = "https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/findnearbypeople"

 
r = redis.Redis(
     host='datanode-001.zumykb.0001.use2.cache.amazonaws.com',
     port=6379)

def postToLambda(peoplelist):
#	queryuserid = sys.argv[1]
#        querylat = float(sys.argv[2])
#        querylong = float(sys.argv[3])
	params = json.dumps({'userid':'user:0' ,'latitude':'40','longitude':'50','peopleinfo': peoplelist})
	r = requests.post(NearbyFriendsUrl, data=params)
	#print("status" + str(r.status_code))

	#print("content" + str(r.content))
	return json.loads(r.content)


def postToNearbyPeople(peoplelist):
	numDivs = 10
	pool = ThreadPool(numDivs)
	length = (len(peoplelist))/numDivs
	startTime = time.time()
	newList=[]
	for i in range(0,numDivs):
		newList.append(peoplelist[(i*length):((i+1)*length)-1])
	#newList.append(peoplelist[0:length-1])
	#newList.append(peoplelist[length:2*length-1])
	#newList.append(peoplelist[2*length:3*length-1])
	#newList.append(peoplelist[3*length:4*length-1])
	#newList = [peoplelist[0:length-1], peoplelist[length, 2*length-1], peoplelist[2*length, 3*length-1], peoplelist[3*length, 4*length-1]]
	sorted_lists = pool.map(postToLambda, newList)
	print(sorted_lists)
	endTime = time.time()
	
	

def handler():
	"""
	This function puts into memcache and get from it.
	Memcache is hosted using elasticache
	"""
	#r = redis.Redis(
	#host='datanode-001.zumykb.0001.use2.cache.amazonaws.com',
	#port=6379)
	peoplelist = r.keys('userdata*')
	print(len(peoplelist))
	dist = []
	postToNearbyPeople(peoplelist)	
	return "Nearby Friends Completed "



def main(argv):
    handler()


if __name__ == "__main__":
    main(sys.argv)


