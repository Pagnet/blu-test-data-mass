from src.tools.repository import Repository

class HooksData(Repository):
    def selectByTag(self,tag):
        try:
            sql = f"select document from hooks where config = '{tag}'"
            data = self.query(sql)
            
            return {'return': 'sucess', 'obj': data}
        except Exception as e:
            return {'return': 'error', 'obj': e}
    
    def selectAll(self):
        try:
            sql = f"select row_to_json(row) from (select config, document from hooks order by config asc) row"
            data = self.query(sql)
            
            return {'return': 'sucess', 'obj': data}
        except Exception as e:
            return {'return': 'error', 'obj': e}