import requests


def sampleSendHttpRequests():
    r = requests.get('http://stackoverflow.com/questions/11322430/python-how-to-send-post-request')
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    r = requests.post(url)


def printAndSendReq(url):
    r = requests.get(url)
    print r.status_code
    return r.content


my_array = ['http://httpbin.org/get?a=1', 'http://httpbin.org/get?a=2', 'http://httpbin.org/get?a=3', 'http://httpbin.org/get?a=4']


from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(4)
results = pool.map(printAndSendReq, my_array)

print results