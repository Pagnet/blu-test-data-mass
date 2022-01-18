from flask_restplus import Resource
from src.server.instance import server
from src.db.customer_repository import CustomerRepository
from src.models.customer_model import customer

from src.server.exceptions import Exceptions_errors

app, api = server.app, server.api
ns = api.namespace('QA Automation', path='/api/v1/customer')


@ns.route('/')
class RouteCustomerPost(Resource):
    @api.expect(customer, valitade=True)
    def post(Self):
        try:
            payload = api.payload
            repo = CustomerRepository()
            er = Exceptions_errors()
                
            repo.save(payload)
            
            status_code = 200
            message = "Sucesso!"
            return er.make_error(status_code, message, payload)
        except Exception as e:
            status_code = 400
            message = e.pgerror
            return er.make_error(status_code, message, payload)


@ns.route('/<role>')
class RouteCustomerGetEmail(Resource):
    def get(self, role):
        repo = CustomerRepository()
        er = Exceptions_errors()

        query = repo.selectByRole(role)
        if query[0][0] is None:
                status_code = 404
                message = "Usuario não localizado!"
                return er.make_error(status_code, message, query)
        
        elif query[0][0] is not None:
                status_code = 200
                message = "Sucesso!"
                return er.make_error(status_code, message, query[0][0])