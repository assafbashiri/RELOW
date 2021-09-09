
class StepService:
    def __init__(self, buyers_amount, price, step_number):
        self.buyers_amount = buyers_amount
        self.price = price
        self.step_number = step_number

    def get_step_number(self):
        return self.step_number

    def get_buyers_amount(self):
        return self.buyers_amount

    def get_price(self):
        return self.price
