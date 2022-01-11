from types import MethodType
from flask_restplus import Resource
from flask import request
from src.server.instance import server

from src.db.customer_repository import CustomerRepository
from src.models.customer_model import customer

app, api = server.app, server.api
ns = api.namespace('QA Automation', path='/api/v1/customer')

@ns.route('/<id>')
@ns.doc(responses={200:'Sucess', 404: 'Not Found'},
        description='recurso para consulta clientes utilizados para os testes automatizados',
        params={'email': {'description':'email do client'}}
        )
class RouteCustomerGet(Resource):
    def get(self, id):
        repository = CustomerRepository()
        return repository.selectById(id)