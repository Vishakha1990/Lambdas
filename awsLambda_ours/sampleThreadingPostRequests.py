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
    return json.loads(r.content) # return list<int>

def generateAndSortMain(num):

    startTime = time.time()
    results = generateAndSort(num)
    endTime = time.time()
    print "Local Run time", endTime - startTime

    numDivs = 4 # numthreads
    my_array = [num / numDivs] * numDivs  # [2500, 2500, 2500, 2500]

    pool = ThreadPool(numDivs)
    startTime = time.time()
    sorted_lists = pool.map(postToGenerateAndSort, my_array) # array[list<int>] of size 4

    sorted_final = list(heapq.merge(*sorted_lists)) # takes multiple collections, merges them

    endTime = time.time()
    print "Time", endTime - startTime
    print sorted_final



def main(argv):
    generateAndSortMain(100)



if __name__ == "__main__":
    main(sys.argv)

