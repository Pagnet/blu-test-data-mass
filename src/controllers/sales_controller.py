import json
from os import abort
from types import MethodType
from flask_restplus import Resource
from flask import request
from src.server.instance import server

from src.db.sales_repository import SalesRepository
from src.models.sales_model import sales

app, api = server.app, server.api
ns = api.namespace('QA Automation', path='/api/v1/sales')


@ns.route('/')
class RouteSalesPost(Resource):
    @api.expect(sales, valitade=True)
    def post(Self):
        try:
            payload = api.payload
            repo = SalesRepository()
            query = repo.save(payload)
            return {"msg": "Sucesso!", "obj": payload}
        except Exception as e:
            return {"msg": "Falha ao adicionar item!", "insert": payload}