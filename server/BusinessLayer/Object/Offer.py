
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
        self.max_amount = self.steps[len(self.steps)].get_products_amount()

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

    def get_status(self):
        return self.status

    def get_user_id(self):
        return self.user_id

    def get_current_buyers(self):
        return self.current_buyers

    def update_step(self):
        step_1_wanters = 0
        for user_id in self.current_buyers.keys():
            # sum of all quantity of buyers from curr step and less
            curr_purchase = self.current_buyers[user_id]
            if curr_purchase.get_step() <= 1:
                step_1_wanters += curr_purchase.get_quantity()
        step_2_wanters = 0
        for user_id in self.current_buyers.keys():
            # sum of all quantity of buyers from curr step and less
            curr_purchase = self.current_buyers[user_id]
            if curr_purchase.get_step() <= 2:
                step_2_wanters += curr_purchase.get_quantity()
        step_3_wanters = 0
        for user_id in self.current_buyers.keys():
            # sum of all quantity of buyers from curr step and less
            curr_purchase = self.current_buyers[user_id]
            if curr_purchase.get_step() <= 3:
                step_3_wanters += curr_purchase.get_quantity()
        self.total_products = step_1_wanters
        if step_2_wanters >= self.steps[1].get_products_amount():
            self.current_step = 2
            self.total_products = step_2_wanters
        if step_3_wanters > self.max_amount:
            raise Exception("max amount - cant buy")
        if step_3_wanters >= self.steps[2].get_products_amount():
            self.current_step = 3
            self.total_products = step_3_wanters





