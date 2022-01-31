from flask_restplus import fields
from src.server.instance import server

hooks = server.api.model('hooks', {
    'id': fields.String(description='id do caso de teste'),
    'document': fields.String(description='Massa de dados para o cenario'),
})