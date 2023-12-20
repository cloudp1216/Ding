

import os
from flask import Blueprint, request
from flask_restful import Api, Resource

from .proxy import Ding
from .proxy_robot import DingRobot


root = Blueprint('root', __name__)
api = Api(root)


config = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")


@api.resource('/')
class Proxy(Resource):
    def get(self):
        return {'proxyStatus': 0}
    
    def post(self):
        result = {'proxyStatus': -1}
        args = request.get_json()
        if args:
            try:
                result = Ding(config).ding(args.get('users_id'), args.get('messages'))
            except Exception as e:
                raise e
        return result


@api.resource('/robot')
class ProxyRobot(Resource):
    def get(self):
        return {'proxyStatus': 0}

    def post(self):
        result = {'proxyStatus': -1}
        args = request.get_json()
        if args:
            try:
                result = DingRobot(config).ding(args.get('messages'))

            except Exception as e:
                raise e
        return result


