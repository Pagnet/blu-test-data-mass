import json
from operator import contains
from flask import jsonify


class Formats():
    def formatResponse(self, status_code, message, obj):
        response = jsonify({
            'status_code': status_code,
            'message': message,
            'payload': json.loads(obj)
        })
        response.status_code = status_code
        return response

    def loadErrorInsertDocument(Self, resp, obj, payload):
        err = str(obj['obj'])

        payload = payload['document']
        payload = str(payload).replace('\'', '"')

        if err.find('syntax error') >= 0:
            return resp.formatResponse(400, err, payload)
        if err.find('duplicate key value') >= 0:
            return resp.formatResponse(400, err, payload)
        if err.find('but expression is of type') >= 0:
            return resp.formatResponse(400, err, payload)

    def formatResponseContract(self, r):
        l = {}
        la = []

        configurations = len( r['obj'])

        if configurations > 0:
            for item in r['obj']:
                v = item[0]['document']
                la.append(v)
        
        l.update({'config':la})
        
        return l