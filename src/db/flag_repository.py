from src.server.repository import Repository

class FlagRepository(Repository):
    def selectBy(self, obj):
        f = obj['flag']
        p = obj['product']

        sql = f"SELECT to_jsonb(array_agg(flag)) FROM flag where flag_name = '{f}'' and product = '{p}'"

        return self.query(sql)