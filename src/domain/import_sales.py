
import random
import json

from enum import Enum
from datetime import datetime

from domain.card import Card

class LAUNCHTYPE(Enum):
    PREVISAO = '0'
    LIQUIDACAO_NORMAL = '1'
    LIQUIDACAO_ANTECIPADA = '2'

class MODALITY(Enum):
    CREDITO = 'C'
    DEBITO = 'D'

class MEANSCAPTURE(Enum):
    MANUAL = '1'
    POS = '2'
    PDV = '3'
    TRNOFF = '4'
    INTERNET = '5'
 

class ImportSales():
    def __init__(self):
        self.register_code = ''


    def createTransactionCash(self, ec, modality, flag, values):
        sales = ImportSales()
        sales.consoliationSales(self, ec, modality, '' , flag, values)
    
    def createTransactonParcial(ec, modality, split, flag, values):
        sales = ImportSales()
        sales.consoliationSales(ec, modality, split, flag, values)


    def consoliationSales(self, ec, modality, split, flag, value, typeLaunch, capture, tax):
        self.register_code = "CV"
        self.store_identification = ec
        self.NSU_transaction_host = random.randrange(1, 999999999999)

        self.transaction_date = datetime.now().strftime("%Y%m%d")
        self.transaction_hour = datetime.now().strftime("%H%M%S")

        if typeLaunch == '':
            self.launch_type = LAUNCHTYPE.LIQUIDACAO_NORMAL.value
        else:    
            self.launch_type = typeLaunch

        self.launch_date = datetime.now().strftime("%Y%m%d")
        
        if modality == MODALITY.CREDITO.value:
            self.product_type = modality
        elif modality == MODALITY.DEBITO.value:
            self.product_type = modality

        if capture == '':
            self.means_capture = MEANSCAPTURE.PDV.value
        else:
           self.means_capture = capture

        
        if value == '':
            v = random.randrange(1, 9999)

        self.gross_sale_value = str(v).zfill(11)

        d = int(round((v / 100) * tax, 0))
        self.discount_value = str(d).zfill(11)

        self.net_sale_value = str(v - d).zfill(11)

        self.card_number = Card().getCart(flag)

        # parcel_number= "00"
        # total_parcel_number= "00"
        # NSU_parcel_host= "205971670001"
        # gross_amount_parcel= grossSaleValue
        # parcel_discount_amount= discountValue
        # net_amount_parcel= netSaleValue

        # bank= "341"
        # agency= "008541"
        # account= "00000482264"

        # authorization_code= "772377      "
        # flag_code= "001"
        # flag_product= "003"

        # value_tx_interchange_tariff= "00000002270"
        # value_tx_administration= "00000000350"
        # value_tx_interchange_tariff_parcel= "00000000227"
        # value_tx_administration_parcel= "00000000035"
        # multi_border_reducing_value= "00000000000"
        # value_tx_anticipation= "00000000000"
        # anticipated_net_amount= "00000000000"

        # transition_type= "02"
        # order_code= "200112422008                  "
        # country_acronym= "BRA"
        # terminal_number= "GT043BB1"
        # reserved= "                                           "

        # NSEQ= "00000" + indice

        print('')

        # return register_code + store_identification + NSU_transaction_host + transaction_date + transaction_hour + launch_type + launch_date + product_type + means_capture + gross_sale_value + discount_value + "0000000" + net_sale_value + card_number + parcel_number + total_parcel_number + NSU_parcel_host + gross_amount_parcel + parcel_discount_amount + net_amount_parcel + bank + agency + account + authorization_code + flag_code + flag_product + value_tx_interchange_tariff + value_tx_administration + value_tx_interchange_tariff_parcel + value_tx_administration_parcel + multi_border_reducing_value + value_tx_anticipation + anticipated_net_amount + transition_type + order_code + country_acronym + terminal_number + reserved + NSEQ


if __name__=='__main__':
    sale = ImportSales()
    sale.consoliationSales("","","","","","","", 2.62)

    json_object = json.dumps(sale.__dict__)
    print(json_object)
        