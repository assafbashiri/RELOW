
class StepService:
    def __init__(self, buyers_amount, price):
        self.buyers_amount = buyers_amount
        self.price = price

    def __init__(self, business_step):
        self.buyers_amount = business_step.get_buyers_amount()
        self.price = business_step.get_price()


    def get_buyers_amount(self):
        return self.buyers_amount

    def get_price(self):
        return self.price
