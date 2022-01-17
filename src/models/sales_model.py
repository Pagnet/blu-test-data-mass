from flask_restplus import fields
from src.server.instance import server

sales = server.api.model('customer', {
    'id': fields.Integer(description = 'id do cliente'),
    'document':fields.String(description = "linhas de venda"),
    'create_date': fields.DateTime(description = 'Data de criacao do regristro')
})