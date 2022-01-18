from src.server.repository import Repository

class BankRepository(Repository):
    def selectAll(self):
        sql = f'SELECT to_jsonb(array_agg(bank)) FROM bank'
        return self.query(sql)