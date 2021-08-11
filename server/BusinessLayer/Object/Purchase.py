
class Purchase:
    def __init__(self, quantity, step):
        self.quantity = quantity
        self.step = step

    def get_quantity(self):
        return self.quantity

    def get_step(self):
        return self.step
