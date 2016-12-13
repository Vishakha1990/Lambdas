import requests
import json
import random
import time
import sys
import heapq
from multiprocessing.dummy import Pool as ThreadPool

generateAndSortUrl = "https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/sort/generate"
sortInputUrl = "https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/sort/input"
minInputUrl = "https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/min/input"

# Min Input

def postToMinInput(num_list):
    params = json.dumps({'numbers': num_list})
    # print "num_list", num_list
    # print "params", params
    r = requests.post(minInputUrl, data=params)
    if r.status_code != 200:
        print "PROBLEM!!!! return code not 200, is ",r.status_code
        print "returned:", json.loads(r.content)[:10]
    return json.loads(r.content)

def minInputsMainLocal(num):
    inputStartTime = time.time()
    my_randoms = random.sample(xrange(num * 5), num)
    # print my_randoms
    startTime = time.time()
    my_min = min(my_randoms)
    endTime = time.time()
    print "{}\t{}\t{}".format(num, startTime-inputStartTime,endTime - startTime)
    # print my_min

def minInputsMainLambda(num, numDivs):
    pool = ThreadPool(numDivs)
    numPerDiv = num / numDivs
    # print "Num Per Div: ", numPerDiv
    startTime = time.time()
    function_param_array = []
    for i in xrange(0, numDivs):
        function_param_array.append(random.sample(xrange(numPerDiv * 5), numPerDiv))
    startSendTime = time.time()
    min_list = pool.map(postToMinInput, function_param_array)
    recvdTime = time.time()
    min_final = min(min_list)
    mergeTime = time.time()
    print "{}\t{}\t{}\t{}\t{}".format(numDivs, num, startSendTime-startTime, recvdTime - startSendTime, mergeTime - recvdTime)
    # print min_list
    # print min_final



def main(argv):
    lol = sys.argv[1]
    num = int(sys.argv[2])
    numDivs = -1
    if len(sys.argv) > 3:
        numDivs = int(sys.argv[3])

    if lol == 'local':
        # print "Local\t",num
        # print "Num\tTotaltime"
        minInputsMainLocal(num)
    else:
        # print "Lambda\t",num,"\t",numDivs
        # print "NumDivs\tNum\tStartSendTime\tRecvdtime\tTotaltime"
        minInputsMainLambda(num, numDivs)




if __name__ == "__main__":
    main(sys.argv)

