from src.server.exceptions import Exceptions_errors
from src.db.flag_repository import FlagRepository


class Flag():
    def getFlagAndProduct(self, flag, product):
        try:
            repo = FlagRepository()
            er = Exceptions_errors()

            product = flag + " " + product

            query = repo.selectByInfoByFlagAndProduct(flag, product)

            status_code = 200
            message = "Sucesso!"

            return er.make_error(status_code, message, query[0][0])

        except Exception as e:
            status_code = 400
            message = e.pgerror
            return er.make_error(status_code, message, query[0][0])