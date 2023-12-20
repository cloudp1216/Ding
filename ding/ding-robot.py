#!/usr/bin/python3


import sys
import json

try:
    from config import *

    import requests
    requests.packages.urllib3.disable_warnings()

except Exception as e:
    raise e


def push_msg(messages):
    api = DingProxy
    body = {
        "messages": messages
    }
    result = requests.post("{}/robot".format(api), json=body)
    return result.text
    

if __name__ == "__main__":

    length = len(sys.argv)
    if length <= 1:
        print("Usage: {} \"First line message\" \"Second line message\" ...".format(sys.argv[0]))
        sys.exit(-1)
    
    users_id = sys.argv[1]

    messages = ""
    for num, arg in enumerate(sys.argv[1:], 2):
        messages += str(arg)
        if length != num:
            messages += "\n"
    try:
        result = push_msg(messages)
        print(result, end="")

    except Exception as e:
        print("Error: " + str(e))
        sys.exit(-1)


