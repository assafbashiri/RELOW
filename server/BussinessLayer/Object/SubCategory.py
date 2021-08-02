from BussinesLayer.Objects import Offer
from BussinesLayer.Utils import CheckValidity
class SubCategory:
    def _init_(self, name, nextId, father_category_id):
        self.name=name
        self.offer_list = None
        self.id = nextId
        self.offer_id = 0
        self.father_category_id = father_category_id

    def add_offer(self, user_id, product,category_id, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers )
        #status =
        #offer_to_add = Offer(self.offer_id, user_id, product, category_id, sub_category_id, status, )
        self.offer_id += 1

    def set_name(self, new_name):
        if not CheckValidity.checkValidityName(new_name):
            raise Exception("Illegal Name")
        self.name = new_name