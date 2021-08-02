from BussinesLayer.Objects import Category
class categoryController():
    def __init__(self):
        self.category_list = None
        self.category_id = 0

    def add_category(self, name):
        category_to_add = Category(name, self.category_id)
        self.category_list.add(self.category_id, category_to_add)
        self.category_id += 1

    def remove_category(self, category_id):
        if self.category_list.get(category_id) is None:
            raise Exception("category does not exist");
        self.category_list.get(category_id).key = None

    def add_offer(self, user_id, product, category_id, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers ):
        if category_id not in self.category_list.keys():
            raise Exception("No Such Category")
        self.category_list.get(category_id).add_offer(self, user_id, product, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers )
        #add to the userrrrr

    def remove_offer(self,offer_to_remove):
        if offer_to_remove.category_id not in self.category_list.keys:
            raise Exception("Category Does Not Exist")
        if offer_to_remove.sub_category_id not in self.category_list.get(offer_to_remove.category_id).keys:
            raise Exception("Sub Category Does Not Exist")
        self.category_list.get(offer_to_remove.category_id).get(offer_to_remove.sub_category_id).offer_list.remove(offer_to_remove.offer_id, offer_to_remove)


    #addOffer
    #removeOffer