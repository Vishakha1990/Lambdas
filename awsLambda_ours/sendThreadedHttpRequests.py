import requests
import json


def sampleSendHttpRequests(url):
    r = requests.get('http://stackoverflow.com/questions/11322430/python-how-to-send-post-request')
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    r = requests.post(url)


def printAndSendReq(url):
    r = requests.get(url)
    print r.status_code
    return r.content


my_array = ['http://httpbin.org/get?a=1', 'http://httpbin.org/get?a=2', 'http://httpbin.org/get?a=3', 'http://httpbin.org/get?a=4']

#
# from multiprocessing.dummy import Pool as ThreadPool
# pool = ThreadPool(4)
# results = pool.map(printAndSendReq, my_array)

payload = json.dumps({'num': 5, 'name':'adbhat'})
print "Payload: ", payload
print "Going to send request: "

r = requests.post('https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/sort/generate', data=payload)
# r = requests.post('https://jkf02xx1kl.execute-api.us-east-2.amazonaws.com/prod/api/sort/generate')

print "Reply Status code: ", r.status_code
# print "Reply Content: \n", r.content
parsed = json.loads(r.content)
print "Reply Content: \n", json.dumps(parsed, indent=4, sort_keys=True)


