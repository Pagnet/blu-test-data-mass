from src.util.create_card import CreateCard

class Card():
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

    def getCart(self, flag):
        util = CreateCard()

        if flag == "visa".casefold():

            return self.set_mask_cart(
                util.credit_card_number(
                    util.visaPrefixList, 16, 1))