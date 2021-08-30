from server.Service.Object.ProductService import ProductService


class OfferService:
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

    def __init__(self, business_offer):
        self.offer_id = business_offer.get_offer_id()
        self.current_step = business_offer.get_current_step()
        self.user_id = business_offer.get_user_id()  # seller
        self.product = ProductService(business_offer.get_product())
        self.category_id = business_offer.get_category_id()
        self.subCategory_id = business_offer.get_sub_category_id()
        self.status = None

        # self.price_per_step = price_per_step
        # self.amount_per_step = amount_per_step
        self.steps = business_offer.get_steps()  # dictionary <int(numOfStep), Step)
        self.steps = None
        self.start_date = business_offer.get_start_date()
        self.end_date = business_offer.get_end_date()
        self.current_buyers = None


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

    def get_subCategory_id(self):
        return self.subCategory_id

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