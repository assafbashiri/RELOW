class StepService:
    def __init__(self, business_step, step_number):
        self.buyers_amount = business_step.get_buyers_amount()
        self.price = business_step.get_price()
        self.step_number = step_number
        self.limit = business_step.get_limit()

    def get_buyers_amount(self):
        return self.buyers_amount

    def get_price(self):
        return self.price
