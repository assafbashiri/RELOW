
class Offer:
    def __init__(self, next_id, user_id, product, category_id, sub_category_id, status, price_per_step, amount_per_step, start_date, end_date):
        self.offer_id = next_id
        self.current_step = 1
        self.user_id = user_id #seller
        self.product = product
        self.category_id = category_id
        self.sub_category_id = sub_category_id
        self.status = status
        self.steps = {} # dictionary <int(numOfStep), Step)
        self.start_date = start_date
        self.end_date = end_date
        self.current_buyers = {} # with buyer_id, quantity and step

    def add_buyer(self, user_id, purchase):
        self.current_buyers[user_id] = purchase

    def remove_buyer(self, user_id):
        self.current_buyers.pop(user_id, None)

    def set_offer_id(self, offer_id):
        self.offer_id = offer_id

    def set_current_step(self, current_step):
        self.current_step = current_step

    def set_user_id(self, ):
        return self.user_id

    # def set_product(self):
    #     return self.product

    def set_category_id(self, category_id):
        self.category_id = category_id

    def set_sub_category_id(self, sub_category_id):
        self.subCategory_id = sub_category_id

    def set_status(self, status):
        self.status = status

    def set_steps(self, steps):
        self.steps = self

    def set_start_date(self, start_days):
        self.start_date = self

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_current_buyers(self, current_buyers):
        self.current_buyers = current_buyers