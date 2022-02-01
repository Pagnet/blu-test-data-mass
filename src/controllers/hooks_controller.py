import json
from operator import index
from src.db.hooks_data import HooksData
from src.tools.utils import Formats

from flask_restplus import Api, Resource
from src.server.instance import server


app, api = server.app, server.api
ns = api.namespace('Quality Assurance - Automation',
                   path='/api/v1/automation/hooks')


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
                l = resp.formatResponseContract(r)
                return resp.formatResponse(200, msg,  json.dumps(l, indent=4))

            if len(r['obj']) == 0:
                return resp.formatResponse(404, 'Not found Config', '{}')

        except Exception as e:
            if e.find('JSONDecodeError') >= 0:
                return resp.formatResponse(500, e.msg, '{}')
