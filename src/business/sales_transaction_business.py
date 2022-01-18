from datetime import datetime
import json
import random

from src.business.card_business import Card
from src.business.bank_business import Bank
from src.business.flag_business import Flag

from src.business.enumerators_business import Launch, Product, Capture


class SalesTransaction():
    def createTransaction(self, obj):
        type = int(obj['split'])
        ec = obj['ec']
        launch = obj['launch']
        modality = obj['modality']
        flag = obj['flag']
        value = obj['value']
        capture = obj['capture']
        tax = obj['tax']
        bank = obj['bank']

        if type == 0:
            self.lineSalesNotSplit(
                ec, launch,  modality, flag, value, capture, tax, bank)

    def setValues(self, value, tax):
        if value == 0:
            v = random.randrange(1, 9999)
        else:
            v = value

        gross_sale_value = str(v).zfill(11)

        d = int(round((v / 100) * tax, 0))
        discount_value = str(d).zfill(11)

        net_sale_value = str(v - d).zfill(11)

        return {"gross_sale_value": gross_sale_value, "discount_value": discount_value, "net_sale_value": net_sale_value}

    def lineSalesNotSplit(self, ec, launch,  modality, flag, value, capture, tax, bank):
        card = Card()
        bankObject = Bank()
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

        v = self.setValues(value, tax)

        self.gross_sale_value = v['gross_sale_value']
        self.discount_value = v['discount_value']
        self.net_sale_value = v['net_sale_value']

        self.card_number = card.getCart(flag)

        self.parcel_number = str(00)
        self.total_parcel_number = str(00).zfill(2)
        self.NSU_parcel_host = str(00).zfill(12)

        self.gross_amount_parcel = str(00).zfill(11)
        self.parcel_discount_amount = str(00).zfill(11)
        self.net_amount_parcel = str(00).zfill(11)

        b = bankObject.getClientAndBank(self.store_identification, bank)
        b = b.json['payload'][0]

        self.bank = b['code']
        self.agency = str(b['agency']).zfill(6)
        self.account = str(b['account']).zfill(11)

        self.authorization_code = str(random.randrange(1, 999999)).ljust(12)

        f = flagObject.getFlagAndProduct(flag, modality)
        f = f.json['payload'][0]

        self.flag_code = str(f['code'])
        self.flag_product = str(f['product'])

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