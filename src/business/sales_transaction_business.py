from datetime import datetime
import random
from src.business.bank_business import Bank
from src.business.flag_business import Flag

from src.business.enumerators_business import Launch, Product, Capture
from src.business.card_business import Card


class SalesTransaction():
    def setValues(self, value, tax):
        if value == 0:
            v = random.randrange(1, 9999)
        else:
            v = value

        self.gross_sale_value = str(v).zfill(11)

        d = int(round((v / 100) * tax, 0))
        self.discount_value = str(d).zfill(11)

        self.net_sale_value = str(v - d).zfill(11)

        return self

    def lineSalesNotSplit(self, ec, launch,  modality, flag, value, capture, tax):
        sales = SalesTransaction()
        bank = Bank()
        flagObject = Flag()

        self.register_code = "CV"
        self.store_identification = ec
        self.NSU_transaction_host = str(random.randrange(1, 999999999999))
        self.transaction_date = datetime.now().strftime("%Y%m%d")
        self.transaction_hour = datetime.now().strftime("%H%M%S")
        self.launch_type = Launch.getLaunch(self, launch)
        self.launch_date = datetime.now().strftime("%Y%m%d")
        self.product_type = Product.getProduct(self, modality)
        self.means_capture = Capture.getCapture(self, capture)
        sales.setValues(value, tax)
        self.card_number = Card.getCart(flag)
        self.parcel_number = str(00)
        self.total_parcel_number = str(00).zfill(2)
        self.NSU_parcel_host = str(00).zfill(12)

        self.gross_amount_parcel = str(00).zfill(11)
        self.parcel_discount_amount = str(00).zfill(11)
        self.net_amount_parcel = str(00).zfill(11)

        jsonArrayBank = bank.getBank()
        self.bank = jsonArrayBank['code']
        self.agency = str(jsonArrayBank['agency']).zfill(6)
        self.account = str(jsonArrayBank['account']).zfill(11)

        self.authorization_code = str(random.randrange(1, 999999)).rjust(6)

        jsonArrayFlag = flagObject.getFlagAndProduct(flag, modality)
        self.flag_code = str(jsonArrayFlag['code'])
        self.flag_product= str(jsonArrayFlag['product'])

        # self.value_tx_interchange_tariff= "00000002270"
        # self.value_tx_administration= "00000000350"
        # self.value_tx_interchange_tariff_parcel= "00000000227"
        # self.value_tx_administration_parcel= "00000000035"
        # self.multi_border_reducing_value= "00000000000"
        # self.value_tx_anticipation= "00000000000"
        # self.anticipated_net_amount= "00000000000"

        # self.transition_type= "02"
        # self.order_code= "200112422008                  "
        # self.country_acronym= "BRA"
        # self.terminal_number= "GT043BB1"
        # self.reserved= "                                           "

        # self.NSEQ= "000002"

        return self


if __name__ == '__main__':
    s = SalesTransaction()
    s.lineSalesNotSplit("12345678913", "", "", "", "previsao", "", "")
