from flask_restplus import fields
from src.server.instance import server

sales = server.api.model('sales',{
    'ec': fields.String(description = 'id do cliente'),
    'modality': fields.String(description = 'modalidade de credito ( credito ou debito)'),
    'split': fields.Integer(description = 'parcelado ou a vista'),
    'flag': fields.String(description = 'bandeira da transacao'),
    'value': fields.Float(description = 'valor da transacao'),
    'launch': fields.String(description = 'tipo de lancamento (previsao, liquidacao antecipada ou liquidacao normal)'),
    'capture': fields.String(description = 'meios de captura (manual, pos ou pdv)'),
    'tax': fields.Float(description = 'taxa de desconto'),
    'bank': fields.Float(description = 'banco'),
})