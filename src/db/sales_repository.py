import datetime
from src.server.repository import Repository

class SalesRepository(Repository):
    def save(self, obj):
        id = obj['id']
        doc = obj['document']
        create_date = datetime.datetime.now()
        sql = f"INSERT INTO public.sales_transaction(id, document, create_date) VALUES ({id}, '{doc}', '{create_date}')"
        self.execute(sql)
        return self.commit()

    def selectAll(self):
        sql = f"SELECT to_jsonb(array_agg(sales_transaction)) FROM sales_transaction"
        return self.query(sql)