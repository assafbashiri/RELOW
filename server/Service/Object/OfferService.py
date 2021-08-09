
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
