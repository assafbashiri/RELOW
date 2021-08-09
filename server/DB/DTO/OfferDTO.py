class OfferDTO:
    def __init__(self,offer_id,current_step,user_id,category_id, subCategory_id, status,start_date,end_date):
        self.offer_id = offer_id
        self.current_step = current_step
        self.user_id = user_id
        self.category_id = category_id
        self.subCategory_id = subCategory_id
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
