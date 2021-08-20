from DB.DTO.ProductDTO import ProductDTO


class OfferDTO:
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
        self.hot_deals = offer.hot_deals
        self.productDTO = ProductDTO(offer.product)
