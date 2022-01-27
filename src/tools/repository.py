import psycopg2 as db
import yaml

class Config:
    def __init__(self):
        with open('config.yaml', 'r') as stream:
            file = yaml.safe_load(stream)
            database = file['database']
            self.config = f"dbname={database['dbname']} user={database['user']} host={database['host']} password={database['password']}"

class Repository(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(self.config)
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão Postgres", e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()