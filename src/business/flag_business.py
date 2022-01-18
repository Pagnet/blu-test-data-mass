import json
from math import prod
from src.db.flag_repository import FlagRepository

class Flag():
    def getFlagAndProduct(self, flag, product):
        repo = FlagRepository()
        
        obj = {'falg': flag, 'product': product }

        return repo.selectBy(obj)