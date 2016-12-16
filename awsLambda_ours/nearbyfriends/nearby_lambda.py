from __future__ import print_function
import time
import uuid
import sys
import socket
import logging
import random
import gpxpy.geo
import redis
from operator import itemgetter

r = redis.Redis(
    host='datanode-001.zumykb.0001.use2.cache.amazonaws.com',
    port=6379)


def sortInputsMainLocal(num):
    startTime = time.time()
    my_randoms = random.sample(xrange(num * 5), num)
    my_sorted = sorted(my_randoms)
    endTime = time.time()
    return endTime - startTime


def get_distance(lat, querylat, querylong):
    splitloc = lat
    friendts = splitloc[0]
    friendlat = float(splitloc[1])
    friendlog = float(splitloc[2])
    return gpxpy.geo.haversine_distance(friendlat, friendlog, querylat, querylong)


def handler(event, context):
    startTime = time.time()
    print("startTime", time.time())

    queryuserid = event['userid']
    querylat = float(event['latitude'])
    querylong = float(event['longitude'])
    # queryuserid = "user:0"
    # querylat = float(30)
    # querylong = float(-10)
    # peoplelist = event['peopleinfo']
    paramsParsedTime = time.time()
    print("paramsParsedTime ", time.time())

    # print(peoplelist)
    peoplelist = r.keys('userdata*')
    # friendslist = r.smembers(queryuserid)
    peopleListRetrievedTime = time.time()
    print("peopleListRetrievedTime ", time.time())
    print("People List size : ", len(peoplelist))

    dist = []
    i = 0
    redisTime = 0
    postRedisProcessingTime = 0
    sortTime = 0
    for friend in peoplelist:
        i = i + 1
        if (i % 1000) == 0:
            print("iter: \t", i, "\ttime: \t", time.time(), "\tredisTime: \t", redisTime, "\tavg: \t", redisTime / i, "\tpostRedisProcessTime: \t", postRedisProcessingTime, "\tavg: \t", postRedisProcessingTime / i)

        # calculating distance for each friend
        preRedisTime = time.time()
        allLocations = r.smembers(friend)

        # print("numLocations: ",len(allLocations)) # temp

        postRedisTime = time.time()
        redisTime += (postRedisTime - preRedisTime)
        tupleList = []
        for location in allLocations:
            tupleList.append(tuple(location.split(',')))
        if (len(tupleList) > 0):
            lat_location = max(tupleList, key=itemgetter(0))
            dist.append(get_distance(lat_location, querylat, querylong))
        sortInputsMainLocal(1000)
        iterEndTime = time.time()
        postRedisProcessingTime += (iterEndTime - postRedisTime)

    if (len(dist) > 0):
        minDistance = min(dist)
        postMinDistTime = time.time()
        totalTime = postMinDistTime - startTime;
        print("\tTotal time: \t", totalTime, "\tpeopleListRetrievedTime: \t", peopleListRetrievedTime - startTime, "\tredisTime: \t", redisTime, "\tpostRedisProcessingTime: \t", postRedisProcessingTime, "\tpostMinDistTime: \t",
              postMinDistTime - iterEndTime)
        print("\tStart time: \t", startTime, "\tEndtime: \t", postMinDistTime, "\tRedis percent: \t", (redisTime * 100) / totalTime, "Processing percent: \t", (postRedisProcessingTime * 100) / totalTime)
        return (minDistance)
    else:
        return 0

# return "Nearest person is at distnce: " + str(minDistance)

