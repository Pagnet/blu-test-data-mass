from flask_restplus import fields
from src.server.instance import server

customer = server.api.model('customer', {
    'id': fields.Integer(description = 'id do cliente'),
    'email':fields.String(description = "email do cliente"),
    'senha':fields.String(description = "senha do cliente"),
    'roles': fields.String(description = "tipo da conta 'Administrator' or 'Client'"),
    'status': fields.Boolean(description = "atividade do cliente se o usuario esta em uso ou livre"),
})