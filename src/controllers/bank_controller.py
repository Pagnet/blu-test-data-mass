from flask_restplus import Resource
from src.business.bank_business import Bank
from src.server.instance import server
from src.models.bank_model import bank

app, api = server.app, server.api
ns = api.namespace('QA Automation', path='/api/v1/bank')

@ns.route('/')
class RouteBankPost(Resource):
    @api.expect(bank, valitade=True)
    def post(Self):
        payload = api.payload
        domain = Bank()
        return domain.insertBank(payload)

    def get(Self):
        domain = Bank()
        return domain.GetAllBank()


@ns.route('/<clientid>')
class RouteCustomerGetEmail(Resource):
    def get(self, clientid):
        domain = Bank()
        return domain.GetBankClientId(clientid)