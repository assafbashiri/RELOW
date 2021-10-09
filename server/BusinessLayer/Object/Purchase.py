
class Purchase:
    def __init__(self, quantity, step_id, buyer_id, color, size, address):
        self.quantity = quantity
        self.step_id = step_id
        self.buyer_id = buyer_id
        self.color = color
        self.size = size
        self.address = address

    def get_quantity(self):
        return self.quantity

    def get_step(self):
        return self.step_id

    def get_buyer_id(self):
        return self.buyer_id

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_address(self):
        return self.address