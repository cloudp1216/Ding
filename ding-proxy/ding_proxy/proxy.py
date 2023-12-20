

import os
import sys
import json

try:
    import requests
    requests.packages.urllib3.disable_warnings()

except Exception as e:
    raise e


class Ding(object):
    def __init__(self, config): 

        self.config = config

        self.api_gettoken = 'https://oapi.dingtalk.com/gettoken'
        self.api_msg_send = 'https://oapi.dingtalk.com/message/send'
        self.access_token = '/tmp/.access_token'

        try:
            with open(self.config) as pf:
                app = json.load(pf)

                aps = app['appliction']
                self.agent_id = aps['agent_id']
                self.app_key = aps['app_key']
                self.app_secret = aps['app_secret']

                self.users_dict = app['users_id']                

        except Exception as e:
            raise e

    def _update_access_token(self):
        try:
            payload = {
                'appkey': self.app_key,
                'appsecret': self.app_secret,
            }
            result = requests.get(self.api_gettoken, params=payload)
            access_token = json.loads(result.text)['access_token']

            with open(self.access_token, 'w') as fp:
                fp.write(access_token)

            return access_token

        except Exception as e:
            raise e

    def _get_access_token(self):
        if os.path.isfile(self.access_token):
            access_token = None
            with open(self.access_token, 'r') as fp:
                access_token = fp.read()
            return access_token
        else:
            return self._update_access_token()

    def _ding(self, users_id=None, msg=None):
        messages = {
            'touser': self.users_dict.get(str(users_id)),
            'msgtype': 'text',
            'agentid': int(self.agent_id),
            'text': {
                'content': msg,
            },
        }
        try:
            payload = {'access_token': self._get_access_token()}
            result = requests.post(self.api_msg_send, json=messages, params=payload)
            return json.loads(result.text)

        except Exception as e:
            raise e

    def ding(self, users_id=None, msg=None):
        if users_id is None or msg is None:
            return {"proxyStatus": -1}

        try:
            result = self._ding(users_id, msg)
            if result['errcode'] == 0:
                return result
            else:
                self._update_access_token()
                result = self._ding(users_id, msg)
                return result

        except Exception as e:
            raise e


