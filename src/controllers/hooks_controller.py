import json
from src.db.hooks_data import HooksData
from src.tools.utils import Formats

from flask_restplus import Api, Resource
from src.server.instance import server


app, api = server.app, server.api
ns = api.namespace('Quality Assurance - Automation', path='/api/v1/automation/hooks')

@ns.route('/<string:tag>')
class RouteHooksByTag(Resource):
    @ns.doc(
        responses={
            200: 'Sucess',
            404: 'Failed to found config',
            500: 'Internal Error'
        },
        description='feature for search configuration the of automations')
    def get(self, tag):
        repo = HooksData()
        resp = Formats()
        
        try:
            if not isinstance(tag, str):
                return resp.formatResponse(400, 'Tag must be an String value ', '{}')

            r = repo.selectByTag(tag)
            msg = r['return']

            if len(r['obj']) > 0:
                d = []
               
                for item in r['obj']:
                    d.append(item[0])

                return resp.formatResponse(200, msg,  json.dumps(d, indent=4))

            if len(r['obj']) == 0:
                return resp.formatResponse(404, 'Not found Config', '{}')

        except Exception as e:
            if e.find('JSONDecodeError') >= 0:
                return resp.formatResponse(500, e.msg, '{}')


@ns.route('/')
class RouteHooks(Resource):
    @ns.doc(
        responses={
            200: 'Sucess',
            404: 'Failed to found config',
            500: 'Internal Error'
        },
        description='feature for search configuration the of automations')
    def get(self):
        repo = HooksData()
        resp = Formats()
        
        try:
            r = repo.selectAll()
            msg = r['return']

            if len(r['obj']) > 0:
                d = {}

                for item in r['obj']:
                    a = item[0]
                    b = item[1]

                    if a in d.keys():
                         print()
                    else:
                        d.update({a:b})

                return resp.formatResponse(200, msg,  json.dumps(d, indent=4))

            if len(r['obj']) == 0:
                return resp.formatResponse(404, 'Not found Config', '{}')

        except Exception as e:
            if e.find('JSONDecodeError') >= 0:
                return resp.formatResponse(500, e.msg, '{}')

