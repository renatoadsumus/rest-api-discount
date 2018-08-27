

class Discount(object):
    #def __init__(self):

    def total_amount(self, purchase_total):
        discount = 0
        if purchase_total > 10:
            discount = 10

        if purchase_total > 20:
            discount = 20

        return discount