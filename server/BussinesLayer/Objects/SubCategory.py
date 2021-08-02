from BussinesLayer.Objects import Offer
class SubCategory:
    def __init__(self, name, nextId):
        self.name=name
        self.offer_list = None
        self.id = nextId
        self.offer_id = 0

    def add_offer(self, user_id, product,category_id, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers )
        #status =
        #offer_to_add = Offer(self.offer_id, user_id, product, category_id, sub_category_id, status, )
        self.offer_id += 1