import json
from src.db.document_data import DocumentData
from src.models.document_model import document
from src.tools.utils import Formats

from flask_restplus import Api, Resource
from src.server.instance import server


app, api = server.app, server.api
ns = api.namespace('Quality Assurance - Automation', path='/api/v1/automation/documents')

@ns.route('/')
class RouteDocument(Resource):
    @ns.doc(
        responses={
            201: 'Created',
            400: 'Failed to insert data mass',
            500: 'Internal Error'
        },
        description='feature for storing documents for automations')
    @api.expect(document, valitade=True)
    def post(Self):
        repo = DocumentData()
        resp = Formats()

        try:

            payload = api.payload
            r = repo.save(payload)

            if r['return'] == 'sucess':
                return resp.formatResponse(201, r['return'], str(payload['document']).replace('\'', '"'))

            elif r['return'] == 'error':
                return resp.loadErrorInsertDocument(resp, r, payload)

        except Exception as e:
            err = str(e)
            if err.find('Failed to decode JSON') >= 0:
                return resp.formatResponse(500, err, '{}')


@ns.route('/<int:id>')
class RouteDocumentsById(Resource):
    @ns.doc(
        responses={
            200: 'Sucess',
            404: 'Failed to found data mass',
            500: 'Internal Error'
        },
        description='feature for search documents the of automations by id')
    def get(self, id):
        repo = DocumentData()
        resp = Formats()

        try:
            if not isinstance(id, int):
                return resp.formatResponse(400, 'Id must be an integer value ', '{}')

            r = repo.selectById(id)
            msg = r['return']

            if len(r['obj']) > 0:
                d = []
               
                for item in r['obj']:
                    d.append(item[0])

                return resp.formatResponse(200, msg,  json.dumps(d, indent=4))

            if len(r['obj']) == 0:
                return resp.formatResponse(404, 'Not found test case id', '{}')

        except Exception as e:
            if e.find('JSONDecodeError') >= 0:
                return resp.formatResponse(500, e.msg, '{}')