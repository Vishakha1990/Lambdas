import requests
import json
import random
import time
import sys
import heapq
from multiprocessing.dummy import Pool as ThreadPool

generateAndSortUrl = "https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/sort/generate"
sortInputUrl = "https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/sort/input"

# Generate and Sort

def generateAndSort(num):
    my_randoms = random.sample(xrange(num*100), num)
    my_sorted = sorted(my_randoms)
    return my_sorted

def postToGenerateAndSort(num):
    params = json.dumps({'num':num})
    r = requests.post(generateAndSortUrl, data=params)
    print r.status_code
    return json.loads(r.content)

def generateAndSortMain(num):
    startTime = time.time()
    results = generateAndSort(num)
    endTime = time.time()
    print "Time", endTime - startTime

    numDivs = 4
    my_array = [num / numDivs] * numDivs  # [2500, 2500, 2500, 2500]

    pool = ThreadPool(numDivs)
    startTime = time.time()
    sorted_lists = pool.map(postToGenerateAndSort, my_array)

    sorted_final = list(heapq.merge(*sorted_lists))

    endTime = time.time()
    print "Time", endTime - startTime
    print sorted_final

# Sort Input

def postToSortInput(num_list):
    params = json.dumps({'numbers': num_list})
    # print "num_list", num_list
    # print "params", params
    r = requests.post(sortInputUrl, data=params)
    print r.status_code
    return json.loads(r.content)

def sortInputsMain(num):
    my_randoms = random.sample(xrange(num * 100), num)

    startTime = time.time()
    my_sorted = sorted(my_randoms)
    endTime = time.time()
    print "Num:\t{}\tTime:\t{}".format(num, endTime - startTime)

    # numDivs = 5
    # my_array = [num / numDivs] * numDivs  # [2500, 2500, 2500, 2500]
    #
    # pool = ThreadPool(numDivs)
    # startTime = time.time()
    # sorted_lists = pool.map(postToGenerateAndSort, my_array)

    # sorted_final = list(heapq.merge(*sorted_lists))




def main(argv):
    sortInputsMain(100)
    sortInputsMain(1000)
    sortInputsMain(10000)
    sortInputsMain(100000)
    sortInputsMain(1000000)
    # sortInputsMain(10000000)
    # sortInputsMain(100000000)



if __name__ == "__main__":
    main(sys.argv)

