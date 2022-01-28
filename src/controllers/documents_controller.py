from src.db.document_data import DocumentData
from src.models.document_model import document
from src.tools.utils import Formats

from flask_restplus import Api, Resource
from src.server.instance import server


app, api = server.app, server.api

ns = api.namespace('Quality Assurance - Automation', path='/api/v1/automation')


@ns.route('/')
@ns.doc(
    responses={
        201: 'Created',
        400: 'Failed to insert data mass',
        500: 'Internal Error'
    },
    description='feature for storing documents for automations'
)
class RouteDocumentPost(Resource):
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
    
    @api.expect(document, valitade=True)
    def put(Self):
        repo = DocumentData()
        resp = Formats()

        try:

            payload = api.payload
            r = repo.updateById(payload)

            if r['return'] == 'sucess':
                return resp.formatResponse(200, r['return'], str(payload['document']).replace('\'', '"'))

            elif r['return'] == 'error':
                return resp.loadErrorInsertDocument(resp, r, payload)

        except Exception as e:
            err = str(e)
            if err.find('Failed to decode JSON') >= 0:
                return resp.formatResponse(500, err, '{}')


@ns.route('/<id>')
@ns.doc(
    responses={
        200: 'Sucess',
        404: 'Failed to found data mass',
        500: 'Internal Error'
    },
    description='feature for search documents the of automations'
)
class RouteDocumentsGet(Resource):
    def get(self, id):
        repo = DocumentData()
        resp = Formats()

        try:
            r = repo.selectById(id)

            if r['return'] == 'sucess' and len(r['obj']) > 0:
                return resp.formatResponse(200, r['return'],  str(r['obj'][0][0]).replace('\'', '"'))

            if r['return'] == 'sucess' and len(r['obj']) == 0:
                return resp.formatResponse(404, r['return'], '{}' )

        except Exception as e:
            if e.find('JSONDecodeError') >= 0:
                return resp.formatResponse(500, e.msg, '{}')