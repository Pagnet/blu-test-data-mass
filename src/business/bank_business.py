from src.db.bank_repository import BankRepository

class Bank():
    def getBank(self):
        repo = BankRepository()
        return repo.selectAll()