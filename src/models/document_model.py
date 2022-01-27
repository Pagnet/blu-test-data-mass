from flask_restplus import fields
from src.server.instance import server

document = server.api.model('document', {
    'id': fields.String(description='id do caso de teste'),
    'document': fields.String(description='Massa de dados para o cenario')
})