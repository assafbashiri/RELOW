class OfferDTO:
    def __init__(self,offer_id,current_step,user_id,category_id, subCategory_id, status,start_date,end_date,steps, total_products):
        self.offer_id = offer_id
        self.current_step = current_step
        self.user_id = user_id
        self.category_id = category_id
        self.sub_category_id = subCategory_id
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.steps = steps
        self.total_products = total_products

    def __init__(self, offer):
        self.offer_id = offer.offer_id
        self.current_step = offer.current_step
        self.user_id = offer.user_id
        self.category_id = offer.category_id
        self.sub_category_id = offer.sub_category_id
        self.status = offer.status
        self.start_date = offer.start_date
        self.end_date = offer.end_date
        self.steps = offer.steps
        self.total_products = offer.total_products