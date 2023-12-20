

import os
import sys
import json

try:
    import requests
    requests.packages.urllib3.disable_warnings()

except Exception as e:
    raise e


class DingRobot(object):
    def __init__(self, config): 

        self.config = config
        self.webhook = None

        try:
            with open(self.config) as pf:
                self.webhook = json.load(pf)['webhook']

        except Exception as e:
            raise e

    def ding(self, msg=None):
        messages = {
            'msgtype': 'text', 
            'text': {
                'content': msg,
            },
        }
        try:
            result = requests.post(self.webhook, json=messages)
            return json.loads(result.text)

        except Exception as e:
            raise e


