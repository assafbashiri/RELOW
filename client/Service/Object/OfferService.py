from Service.Object.ProductService import ProductService

from client.Service.Object.PurchaseService import PurchaseService
from client.Service.Object.StepService import StepService


class OfferService:
    # CLIENT
    def __init__(self, offer_id, user_id, product, category_id, sub_category_id, status, steps, start_date, end_date,
                 current_step, current_buyers):
        self.offer_id = offer_id
        self.current_step = current_step
        # seller
        self.user_id = user_id
        self.category_id = category_id
        self.sub_category_id = sub_category_id
        self.start_date = start_date
        self.end_date = end_date

        # build service objects
        self.product = ProductService(product['name'], product['company'], product['color'], product['size'],
                                      product['description'],
                                      product['photos'], product['offer_id'])
        # dictionary <int(numOfStep), Step)
        self.steps = {}
        for step in steps:
            self.steps[step['step_number']] = StepService(step['buyers_amount'], step['price'], step['step_number'])

        self.status = status

        self.current_buyers = {}
        for buyer in current_buyers:
            self.current_buyers[buyer['buyer_id']] = PurchaseService(buyer['buyer_id'], buyer['step_id'], buyer['quantity'], buyer['color'], buyer['size'])




    # --------------------------------------------GETTERS--------------------------------------------------------------
    def get_offer_id(self):
        return self.offer_id

    def get_current_step(self):
        return self.current_step

    def get_user_id(self):
        return self.user_id

    def get_product(self):
        return self.product

    def get_category_id(self):
        return self.category_id

    def get_sub_category_id(self):
        return self.sub_category_id

    def get_status(self):
        return self.status

    def get_steps(self):
        return self.steps

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_current_buyers(self):
        return self.current_buyers

    # ---------------------------------------------SETTERS-----------------------------------------------------------------

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
        self.sub_category_id = sub_category_id

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

    # ----------------------------------------------------------------

    def is_a_seller(self, user_id):
        return self.user_id == user_id

