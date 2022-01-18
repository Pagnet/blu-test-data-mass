import datetime
from src.server.repository import Repository


class BankRepository(Repository):
    def selectAll(self):
        sql = f'select to_jsonb(array_agg(bank)) FROM bank'
        return self.query(sql)

    def selectByClientId(self, client_id):
        sql = f"select to_jsonb(array_agg(bank)) FROM bank where id_client = '{client_id}'"
        return self.query(sql)

    def selectByInfoForBankAndClient(self, client_id, name):
        sql = f"select to_jsonb(array_agg(bank)) FROM bank where id_client = '{client_id}' and name = '{name}'"
        return self.query(sql)

    def save(self, obj):
        id_client = obj['id_client']
        code = obj['code']
        name = obj['name']
        agency = obj['agency']
        account = obj['account']
        create_date = datetime.datetime.now()
        sql = f"insert into bank (id, id_client, code, name, agency, account, create_date) values ( default, '{id_client}', '{code}', '{name}', '{agency}', '{account}', '{create_date}' )"
        self.execute(sql)
        return self.commit()
