
class StepService:
    def __init__(self, buyers_amount, price, step_number, limit):
        self.buyers_amount = buyers_amount
        self.price = price
        self.step_number = step_number
        self.limit = limit

    def get_step_number(self):
        return self.step_number

    def get_buyers_amount(self):
        return self.buyers_amount

    def get_price(self):
        return self.price

    def get_limit(self):
        return self.limit
