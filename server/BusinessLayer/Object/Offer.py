
class Offer:

    def __init__(self, next_id, user_id, product, category_id, sub_category_id, status, steps, start_date, end_date):
        self.offer_id = next_id
        self.current_step = 1
        self.user_id = user_id #seller
        self.product = product
        self.category_id = category_id
        self.sub_category_id = sub_category_id
        self.status = status
        self.steps = steps #
        self.start_date = start_date
        self.end_date = end_date
        self.current_buyers = {} # with buyer_id, quantity and step
        self.total_products = 0

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

    def set_category_id(self,new_category_id):
        self.category_id = new_category_id

    def set_sub_category_id(self,new_sub_category_id):
        self.sub_category_id = new_sub_category_id

    def get_offer_id(self):
        return self.offer_id

    def get_current_step(self):
        return self.current_step

    def update_curr_step(self):
        ans = 0
        for user_id in self.current_buyers.keys():
            # sum of all quantity of buyers from curr step and less
            curr_purchase = self.current_buyers[user_id]
            if curr_purchase.get_step() <= self.current_step:
                ans += curr_purchase.get_quantity()
        self.total_products = ans
        for step in self.steps.keys():
            if self.total_products < self.steps[step].products_amount:
                self.current_step = step
                break


