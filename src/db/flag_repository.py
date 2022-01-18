from src.server.repository import Repository

class FlagRepository(Repository):
    def selectByInfoByFlagAndProduct(self, flag, product):
        sql = f"select to_jsonb(array_agg(flag)) FROM flag where flag_name = '{flag}' and product = '{product}'"
        return self.query(sql)