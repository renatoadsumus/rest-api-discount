

class Discount(object):

    def get_discount(self, purchase_total):
        parse_purchase_total = int(purchase_total)
        discount = 0
        if parse_purchase_total > 10:
            discount = 10

        if parse_purchase_total > 20:
            discount = 20

        if parse_purchase_total > 25:
            discount = 22

        if parse_purchase_total > 30:
            discount = 25

        return discount