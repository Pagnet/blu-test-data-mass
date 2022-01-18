import json
from flask_restplus import Resource
from src.business.sales_transaction_business import SalesTransaction
from src.server.instance import server

from src.models.sales_model import sales

app, api = server.app, server.api
ns = api.namespace('Sales', path='/api/v1/sales')


@ns.route('/')
class RouteBankPost(Resource):
    @api.expect(sales, valitade=True)
    def post(Self):
        payload = api.payload
        domain = SalesTransaction()
        return  domain.createTransaction(payload)