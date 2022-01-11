from src.server.repository import Repository

class CustomerRepository(Repository):
    def selectById(self, id):
        sql = f"Select * from customer where 'id'='{id}'"
        data = self.query(sql)
        return data