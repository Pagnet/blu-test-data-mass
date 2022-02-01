import json
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

        index = 0
        i = len(r['obj']) - 1

        for item in r['obj']:
            k = item[0]
            nk = ''

            if index < i:
                nk = r['obj'][index + 1][0]

            if index == 0:
                if k == nk:
                    la.append(item[1])
                else:
                    v = item[1]
                    l.update({k: v})

            else:
                pk = r['obj'][index - 1][0]

                if k == nk:
                    if len(la) > 0 and k == pk:
                        la.append(item[1])

                if k == pk:
                    la.append(item[1])

                if k != pk:
                    v = item[1]
                    
                    if k != nk:
                        l.update({k: v})

                        if len(la) > 0:
                            l.update({pk: la})
                            la = []

                if  index == i and len(la) > 0:
                    l.update({k: la})  

            index += 1
            
        return l