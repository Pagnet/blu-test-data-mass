import datetime
import json
from src.server.repository import Repository

class SalesRepository(Repository):
    def save(self, tags, obj):
        id = obj['id']
        create_date = datetime.now()
        sql = f"INSERT INTO sales_transaction (id, document, create_date) VALUES ('{id}','{obj}','{create_date}')"
        self.execute(sql)
        return self.commit()