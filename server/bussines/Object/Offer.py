offer_id_counter = 1;
def inc(offer_id):
    offer_id += 1

class Offer():
    def __init__(self, offer_id, user_id, product, category_id, subCategory_id, status, price_per_step, amount_per_step, start_date, end_date,  current_buyers):
        self.offer_id = offer_id_counter
        inc(offer_id_counter)
        current_step = 0
        self.user_id = user_id
        self.product
        self.category_id = category_id
        self.subCategory_id = subCategory_id
        self.status = status
        self.price_per_step = price_per_step
        self.amount_per_step = amount_per_step
        self.start_date = start_date
        self.end_date = end_date
        self.current_buyers = current_buyers
