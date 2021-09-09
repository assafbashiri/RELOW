
class Purchase:
    def __init__(self, quantity, step_id, buyer_id):
        self.quantity = quantity
        self.step_id = step_id
        self.buyer_id = buyer_id

    def get_quantity(self):
        return self.quantity

    def get_step(self):
        return self.step_id

    def get_buyer_id(self):
        return self.buyer_id