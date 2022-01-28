from datetime import datetime
from src.tools.repository import Repository

class KeyData(Repository):
    def save(self, obj):
        try:
            id = obj['id']
            
            doc = str(obj['document'])
            doc = doc.replace('\'', '"')
            
            create_date = datetime.now()
            
            sql = f"insert into keys(id, document, create_date, update_date) values ({id}, '{doc}', '{create_date}', '{create_date}')"
            self.execute(sql)
            self.commit()

            return {'return': 'sucess'}
        except Exception as e:
            return {'return': 'error', 'obj': e}
    
    def selectAll(self, id):
        try:
            sql = f"select * from Keys"
            data = self.query(sql)
            
            return {'return': 'sucess', 'obj': data}
        except Exception as e:
            return {'return': 'error', 'obj': e}
    

    def updateById(self, obj):
        try:
            id = obj['id']
            
            doc = str(obj['document'])
            doc = doc.replace('\'', '"')
            
            update_date = datetime.now()
            
            sql = f"update keys set document= '{doc}',  update_date='{update_date}'where id = {id}"
            self.execute(sql)
            self.commit()

            return {'return': 'sucess'}
        except Exception as e:
            return {'return': 'error', 'obj': e}