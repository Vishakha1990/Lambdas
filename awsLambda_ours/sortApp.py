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
    if r.status_code != 200:
        print "PROBLEM!!!! return code not 200, is ",r.status_code
        print "returned:", json.loads(r.content)[:10]
    return json.loads(r.content)

def sortInputsMainLocal(num):
    my_randoms = random.sample(xrange(num * 5), num)

    startTime = time.time()
    my_sorted = sorted(my_randoms)
    endTime = time.time()
    print "Num:\t{}\tTime:\t{}".format(num, endTime - startTime)

def sortInputsMainLambda(num, numDivs):
    # my_randoms = random.sample(xrange(num * 100), num)
    pool = ThreadPool(numDivs)
    numPerDiv = num / numDivs
    print "Num Per Div: ", numPerDiv

    function_param_array = []
    for i in xrange(0, numDivs):
        # function_param_array.append(my_randoms[(i*numPerDiv):(i+1)*numPerDiv])
        function_param_array.append(random.sample(xrange(numPerDiv * 5), numPerDiv))

    startTime = time.time()
    sorted_lists = pool.map(postToSortInput, function_param_array)
    recvdTime = time.time()
    sorted_final = list(heapq.merge(*sorted_lists))
    mergeTime = time.time()
    print "Num:\t{}\tRecvdTime:\t{}\tTotalTime:\t{}".format(num, recvdTime - startTime, mergeTime - startTime)
    # print sorted_final



def main(argv):
    lol = sys.argv[1]
    num = int(sys.argv[2])
    numDivs = -1
    if len(sys.argv) > 3:
        numDivs = int(sys.argv[3])

    if lol == 'local':
        sortInputsMainLocal(num)
    else:
        sortInputsMainLambda(num, numDivs)




if __name__ == "__main__":
    main(sys.argv)

