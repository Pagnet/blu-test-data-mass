import datetime
import json
from src.server.repository import Repository

class CustomerRepository(Repository):
    def save(self, obj):
        id = obj['id']
        user = obj['email']
        senha = obj['senha']
        roles = obj['roles']
        status = obj['status']
        create_date = datetime.datetime.now()
        sql = f"INSERT INTO public.customer(id, email, senha, roles, create_date, status) VALUES ({id}, '{user}', '{senha}', '{roles}', '{create_date}', {status} )"
        self.execute(sql)
        return self.commit()
    
    def selectByRole(self, role):
        sql = f"SELECT to_jsonb(array_agg(customer)) FROM customer  where roles = '{role}'"
        return self.query(sql)