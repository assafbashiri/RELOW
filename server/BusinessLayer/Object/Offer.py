from BusinessLayer.Object.Purchase import Purchase

from BusinessLayer.Utils.OfferStatus import OfferStatus
from BusinessLayer.Object.Step import Step



class Offer:

    def __init__(self, next_id, user_id, product, category_id, sub_category_id, status, steps, start_date, end_date, current_buyers, total_product):
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
        self.current_buyers = current_buyers # with buyer_id, purchase(quantity and step)
        self.total_products = total_product
        self.hot_deals = False
        if len(self.steps) == 0:
            raise Exception("steps cant be empty - have to be checked in client")
        self.max_amount = self.steps[len(self.steps)].get_products_amount()

    def add_buyer(self, user_id, purchase):
        self.current_buyers[user_id] = purchase

    def remove_buyer(self, user_id):
        if user_id not in self.current_buyers.keys():
            return False
        self.current_buyers.pop(user_id, None)
        return True

    def set_offer_id(self, offer_id):
        self.offer_id = offer_id

    def set_current_step(self, current_step):
        self.current_step = current_step

    def set_user_id(self, ):
        return self.user_id

    def set_total_products(self, total_products):
        self.total_products = total_products
    # def set_product(self):
    #     return self.product

    def set_category_id(self, category_id):
        self.category_id = category_id

    def set_sub_category_id(self, sub_category_id):
        self.subCategory_id = sub_category_id

    def set_status(self, status):
        self.status = status

    def set_steps(self, step_number, quantity, price):
        new_step = Step(quantity , price)
        self.steps[step_number] = new_step

    def set_start_date(self, start_days):
        self.start_date = self

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_current_buyers(self, current_buyers):
        self.current_buyers = current_buyers

    def set_category_id(self, new_category_id):
        self.category_id = new_category_id

    def set_sub_category_id(self, new_sub_category_id):
        self.sub_category_id = new_sub_category_id

    def set_hot_deals(self, hot):
        self.hot_deals = hot

    def get_offer_id(self):
        return self.offer_id

    def get_category_id(self):
        return self.category_id

    def get_sub_category_id(self):
        return self.sub_category_id

    def get_current_step(self):
        return self.current_step

    def get_product(self):
        return self.product

    def get_status(self):
        return self.status

    def get_user_id(self):
        return self.user_id

    def get_current_buyers(self):
        return self.current_buyers

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_steps(self):
        return self.steps

    def get_total_products(self):
        return self.total_products

    def get_hot_deals(self):
        return self.hot_deals

    def update_active_buy_offer(self, user_id, quantity, step):
        if user_id not in self.current_buyers.keys():
            return False
        purchase = Purchase(quantity, step)
        self.current_buyers[user_id] = purchase
        return True

    def is_a_buyer(self, user_id):
        if user_id in self.current_buyers.keys():
            return True
        return False

    def check_exp_status(self):
        self.set_status(OfferStatus.DONE)
        if self.total_products == 0:
            self.set_status(OfferStatus.EXPIRED_ZERO_BUYERS)

    def update_step(self):
        num_of_buyers_for_each_step = {}
        for step in self.steps.keys():
            num_of_buyers_for_each_step[step] = 0
        for i in range(1, len(num_of_buyers_for_each_step)+1):
            for user_id in self.current_buyers.keys():
            # sum of all quantity of buyers from curr step and less
                curr_purchase = self.current_buyers[user_id]
                if curr_purchase.get_step() <= i:
                    num_of_buyers_for_each_step[i] += curr_purchase.get_quantity()
        if num_of_buyers_for_each_step[len(num_of_buyers_for_each_step)] > self.max_amount:
            raise Exception("Cant buy more then Max Amount")
        updated_step = 1
        updated_total_products = num_of_buyers_for_each_step[1]
        for step in range(2, len(num_of_buyers_for_each_step)+1):
            if num_of_buyers_for_each_step[step] >= self.steps[step-1].get_products_amount():
                updated_step = step
                updated_total_products = num_of_buyers_for_each_step[step]
        self.current_step = updated_step
        self.total_products = updated_total_products


