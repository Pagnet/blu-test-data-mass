from pyexpat import model
from flask_restplus import fields
from src.server.instance import server

sales = server.api,model('sales',{
    'ec': fields.Integer(description = 'id da transação'),
    'modality': fields.Integer(description = 'id da transação'),
    'split': fields.Integer(description = 'id da transação'),
    'flag': fields.Integer(description = 'id da transação'),
    'value': fields.Integer(description = 'id da transação'),
    'typeLaunch': fields.Integer(description = 'id da transação'),
    'capture': fields.String(description = 'json da transação'),
    'tax': fields.String(description = 'json da transação')
})