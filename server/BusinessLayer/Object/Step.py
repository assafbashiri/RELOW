
class Step:
    def __init__(self, limit, price):
        self.buyers_amount = 0
        self.price = price
        self.limit = limit

    def get_buyers_amount(self):
        return self.buyers_amount

    def get_price(self):
        return self.price

    def get_limit(self):
        return self.limit

