from datetime import datetime

from itsdangerous import json
import json
from src.tools.repository import Repository


class DocumentData(Repository):
    def save(self, obj):
        try:
            id = obj['id']
            
            doc = str(obj['document'])
            doc = doc.replace('\'', '"')
            
            create_date = datetime.now()
            
            sql = f"insert into documents(id, document, create_date, update_date) values ({id}, '{doc}', '{create_date}', '{create_date}')"
            self.execute(sql)
            self.commit()

            return {'return': 'sucess'}
        except Exception as e:
            return {'return': 'error', 'obj': e}
    
    def selectById(self, id):
        try:
            sql = f"select document from documents where id = {id};"
            data = self.query(sql)
            
            return {'return': 'sucess', 'obj': data}
        except Exception as e:
            return {'return': 'error', 'obj': e}

