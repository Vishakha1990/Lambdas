from __future__ import print_function

import json
import random
import logging

print('Loading function')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        # 'body': err.message if err else json.dumps(res),
        'body': err.message if err else res,
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    # print (event)
    logger.info("Log Received event: " + json.dumps(event, indent=2))
    print("Print Received event: " + json.dumps(event, indent=2))
    # print("value1 = " + event['key1'])
    # print("value2 = " + event['key2'])
    # print("value3 = " + event['key3'])
    # return event['key1']  # Echo back the first key value
    # raise Exception('Something went wrong')

    num = event['num']
    print("num = ", num)
    my_randoms = random.sample(xrange(100), 10)
    my_sorted = sorted(my_randoms)

    # return json.dumps(event)  # Echo back the first key value
    # return respond(None, event)
    return respond(None, my_sorted)