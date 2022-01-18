from flask_restplus import fields
from src.server.instance import server

bank = server.api.model('bank', {
    'id_client': fields.Integer(description='id do banco'),
    'code': fields.Integer(description='codigo do banco'),
    'name': fields.String(description='descricao do banco'),
    'agency': fields.Integer(description='agencia'),
    'account': fields.Integer(description='conta'),
    'create_date': fields.Date(description='data de criacao do registro')
})