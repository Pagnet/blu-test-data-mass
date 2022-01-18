from enum import Enum


class Launch(Enum):
    PREVISAO = '0'
    LIQUIDACAO_NORMAL = '1'
    LIQUIDACAO_ANTECIPADA = '2'

    def getLaunch(self, type):
        if type == "PREVISAO".casefold():
            return Launch.PREVISAO.value
        elif type == "LIQUIDACAO NORMAL".casefold():
            return Launch.LIQUIDACAO_NORMAL.value
        elif type == "LIQUIDACAO ANTECIPADA".casefold():
            return Launch.LIQUIDACAO_ANTECIPADA.value


class Product(Enum):
    CREDITO = 'C'
    DEBITO = 'D'

    def getProduct(self, modality):
        if modality == "credito".casefold():
            return Product.CREDITO.value
        elif modality == "debito".casefold():
            return Product.DEBITO.value

class Capture(Enum):
    MANUAL = '1'
    POS = '2'
    PDV = '3'

    def getCapture(self, capture):
            if capture == 'manual'.casefold():
                return Capture.MANUAL.value
            elif capture == 'pos'.casefold():
                return Capture.POS.value
            elif capture == 'pdv'.casefold():
                return Capture.PDV.value