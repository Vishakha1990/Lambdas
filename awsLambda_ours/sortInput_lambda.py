from __future__ import print_function

import json
import random
import logging

print('Loading function')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def respond(err, res=None):
    return res


def lambda_handler(event, context):
    print("Print Received event: " + json.dumps(event, indent=2))

    num_list = event['numbers']
    # print("num_str : ", type(num_str), num_str)
    # print("num_str[0] : ", type(num_str[0]), num_str[0])

    my_sorted = sorted(num_list)

    return respond(None, my_sorted)