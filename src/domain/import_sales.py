from src.domain.enums.register_code import RegisterCode
from src.domain.enums.launch_type import LaunchType
from src.domain.enums.transaction_type import TransactionType
from src.domain.enums.means_capture import MeansCapture
from src.domain.card import Card

import datetime 
import random

class ImportSales():
    def getTransactionsCash(self):
        register_code = RegisterCode.CONSILIATION_BUY.value
        store_identification = customer
        NSU_transaction_host= random.randrange(1, 999999999999)    

        transaction_date = datetime.datetime.now().strftime("%Y%m%d")
        transaction_hour = datetime.datetime.now().strftime("%H%M%S")
        launch_type= launchType.LIQUIDACAO_NORMAL.value
        launch_date = datetime.datetime.now().strftime("%Y%m%d")
        product_type = TransactionType.CREDITO.value 
        means_capture= MeansCapture.PDV.value

        v = random.randrange(1, 9999)    
        gross_sale_value = str(v).zfill(11) 

        d = int(round((v / 100) * 2.63 , 0))
        discount_value = str(d).zfill(11) 

        net_sale_value = str(v - d).zfill(11)

        card_number = blu.set_mask_cart(Card().credit_card_number(random.seed, Card().mastercardPrefixList, 16, 100))

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

        return register_code + store_identification + NSU_transaction_host + transaction_date + transaction_hour + launch_type + launch_date + product_type + means_capture + gross_sale_value + discount_value + "0000000" + net_sale_value + card_number + parcel_number + total_parcel_number + NSU_parcel_host + gross_amount_parcel + parcel_discount_amount + net_amount_parcel + bank + agency + account + authorization_code + flag_code + flag_product + value_tx_interchange_tariff + value_tx_administration + value_tx_interchange_tariff_parcel + value_tx_administration_parcel + multi_border_reducing_value + value_tx_anticipation + anticipated_net_amount + transition_type + order_code + country_acronym + terminal_number + reserved + NSEQ