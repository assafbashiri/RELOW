
class Offer:
    def __init__(self, next_id, user_id, product, category_id, sub_category_id, status, price_per_step, amount_per_step, start_date, end_date,  current_buyers):
        self.offer_id = next_id
        self.current_step = -1
        self.user_id = user_id #seller
        self.product = product
        self.category_id = category_id
        self.subCategory_id = sub_category_id
        self.status = status

        #self.price_per_step = price_per_step
        #self.amount_per_step = amount_per_step
        self.steps = None # dictionary <int(numOfStep), Step)

        self.start_date = start_date
        self.end_date = end_date
        self.current_buyers = current_buyers

    def add_buyer(self, user_to_add):
        self.current_buyers[user.user_id] = user_to_add

    def remove_buyer(self, user_to_remove):
        self.current_buyers.pop(user_to_remove.user_id, None)