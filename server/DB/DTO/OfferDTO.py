from DB.DTO.ProductDTO import ProductDTO


class OfferDTO:
    def __init__(self, offer):
        self.offer_id = offer.get_offer_id()
        self.current_step = offer.get_current_step()
        self.user_id = offer.get_user_id()
        self.category_id = offer.get_category_id()
        self.sub_category_id = offer.get_sub_category_id()
        self.status = offer.get_status()
        self.start_date = offer.get_start_date()
        self.end_date = offer.get_end_date()
        self.steps = offer.get_steps()
        self.total_products = offer.get_total_products()
        self.hot_deals = offer.get_hot_deals()
        self.productDTO = ProductDTO(offer.product)
        self.confirm = offer.confirm