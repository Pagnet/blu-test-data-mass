from flask_restplus import fields
from src.server.instance import server

customer = server.api.model('customer', {
    'email':fields.String(description="email do cliente"),
    'senha':fields.String(description="senha do cliente"),
    'client': fields.String(description= "tipo da conta 'Administrator' or 'Client'"),
})