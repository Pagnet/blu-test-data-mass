from src.server.exceptions import Exceptions_errors
from src.db.bank_repository import BankRepository

class Bank():
    def insertBank(self, payload):
        try:
            repo = BankRepository()
            er = Exceptions_errors()

            repo.save(payload)
                
            status_code = 200
            message = "Sucesso!"
            
            return er.make_error(status_code, message, payload)

        except Exception as e:
            status_code = 400
            message = e.pgerror
            return er.make_error(status_code, message, payload)

    def GetAllBank(self):
        try:
            repo = BankRepository()
            er = Exceptions_errors()

            query  = repo.selectAll()
                
            status_code = 200
            message = "Sucesso!"
            
            return er.make_error(status_code, message, query[0][0])

        except Exception as e:
            status_code = 400
            message = e.pgerror
            return er.make_error(status_code, message, query[0][0])
    
    def GetBankClientId(self, client_id):
        try:
            repo = BankRepository()
            er = Exceptions_errors()

            query  = repo.selectByClientId(client_id)
                
            status_code = 200
            message = "Sucesso!"
            
            return er.make_error(status_code, message, query[0][0])

        except Exception as e:
            status_code = 400
            message = e.pgerror
            return er.make_error(status_code, message, query[0][0])