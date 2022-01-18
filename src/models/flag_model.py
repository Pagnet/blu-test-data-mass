from flask_restplus import fields
from src.server.instance import server

flag = server.api.model('flag',{
    'code': fields.String(description = 'codigo da bandeira'),
    'name_bandeira': fields.String(description = 'nome da bandeira'),
    'product': fields.Integer(description = 'produto'),
})