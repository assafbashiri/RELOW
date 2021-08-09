
class Offer:
    def __init__(self, next_id, user_id, product, category_id, sub_category_id, status, price_per_step, amount_per_step, start_date, end_date):
        self.offer_id = next_id
        self.current_step = 1
        self.user_id = user_id #seller
        self.product = product
        self.category_id = category_id
        self.subCategory_id = sub_category_id
        self.status = status
        self.steps = {} # dictionary <int(numOfStep), Step)
        self.start_date = start_date
        self.end_date = end_date
        self.current_buyers = {} # with buyer_id, quantity and step

    def add_buyer(self, user_to_add, quantity, step):
        self.current_buyers[user_to_add.user_id] = user_to_add
        # have to add the quantity and the step

    def remove_buyer(self, user_to_remove):
        self.current_buyers.pop(user_to_remove.user_id, None)