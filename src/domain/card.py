from random import Random

import copy
import random

class Card():
    visaPrefixList = [
            ['4', '5', '3', '9'],
            ['4', '5', '5', '6'],
            ['4', '9', '1', '6'],
            ['4', '5', '3', '2'],
            ['4', '9', '2', '9'],
            ['4', '0', '2', '4', '0', '0', '7', '1'],
            ['4', '4', '8', '6'],
            ['4', '7', '1', '6'],
            ['4']]

    mastercardPrefixList = [
            ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]
    
    amexPrefixList = [['3', '4'], ['3', '7']]
    
    discoverPrefixList = [['6', '0', '1', '1']]
    
    dinersPrefixList = [
            ['3', '0', '0'],
            ['3', '0', '1'],
            ['3', '0', '2'],
            ['3', '0', '3'],
            ['3', '6'],
            ['3', '8']]
    
    enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]
    
    jcbPrefixList = [['3', '5']]
    
    voyagerPrefixList = [['8', '6', '9', '9']]

    def completed_number(self, prefix, length):
        generator = Random()
        generator.seed()
        ccnumber = prefix
        # generate digits
        while len(ccnumber) < (length - 1):
            digit = str(generator.choice(range(0, 10)))
            ccnumber.append(digit)
        # Calculate sum
        sum = 0
        pos = 0
        reversedCCnumber = []
        reversedCCnumber.extend(ccnumber)
        reversedCCnumber.reverse()
        while pos < length - 1:
            odd = int(reversedCCnumber[pos]) * 2
            if odd > 9:
                odd -= 9
            sum += odd
            if pos != (length - 2):
                sum += int(reversedCCnumber[pos + 1])
            pos += 2
        # Calculate check digit
        checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
        ccnumber.append(str(checkdigit))
        return ''.join(ccnumber)

    def credit_card_number(self, rnd, prefixList, length, howMany):
        result = []
        while len(result) < howMany:
            ccnumber = copy.copy(rnd.choice(prefixList))
            result.append(Card().completed_number(ccnumber, length))
            s = str(result[0])[0:-2]
        return s
    
    def set_mask_cart(self, cart):
        if len(cart) >= 16:
            cm = cart[0:6]
            for c in range(len(cart[6:-4])):
                cm = cm + "X" 
            cm = cm + cart[-4:]
        elif len(cart) < 16 | len(cart) >= 13:
            cm = cart[0:4]
            for c in range(len(cart[4:-4])):
                cm = cm + "X" 
            cm = cm + cart[-4:] 

        return cm

    def getCart(flag):
        if flag == FLAG.VISA.VALUE:
            implementar lógica
        elif flag == FLAG.MASTER.VALUE:
            return  Card().set_mask_cart(Card().credit_card_number(random.seed, Card().mastercardPrefixList, 16, 1))
        elif flag == FLAG.AMEX.VALUE:
            return  Card().set_mask_cart(Card().credit_card_number(random.seed, Card().amexPrefixList, 15, 1))
        elif flag == FLAG.DISCOVER.VALUE:
            return  Card().set_mask_cart(Card().credit_card_number(random.seed, Card().discoverPrefixList, 16, 1))
        elif flag == FLAG.DINERS.VALUE:
            return  Card().set_mask_cart(Card().credit_card_number(random.seed, Card().dinersPrefixList, 14, 1))
        elif flag == FLAG.ENROUTE.VALUE:
            return  Card().set_mask_cart(Card().credit_card_number(random.seed, Card().enRoutePrefixList, 15, 1))
        elif flag == FLAG.JCB.VALUE:
            return  Card().set_mask_cart(Card().credit_card_number(random.seed, Card().jcbPrefixList, 16, 1))
        else flag == FLAG.VOYAGER.VALUE:
            return  Card().set_mask_cart(Card().credit_card_number(random.seed, Card().voyagerPrefixList, 15, 1))
        