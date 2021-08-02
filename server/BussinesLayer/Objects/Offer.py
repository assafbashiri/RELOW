from datetime import date
class Offer:
    def __init__(self, next_id, user_id, product, category_id, sub_category_id, status, price_per_step, amount_per_step, end_date,  current_buyers):
        self.offer_id = next_id
        self.current_step = -1
        self.user_id = user_id #seller
        self.product = product
        self.category_id = category_id
        self.sub_category_id = sub_category_id
        self.status = status
        self.price_per_step = price_per_step
        self.amount_per_step = amount_per_step
        self.start_date = date.today()
        self.end_date = end_date
        self.current_buyers = current_buyers
