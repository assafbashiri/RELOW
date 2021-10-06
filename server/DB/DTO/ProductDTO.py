class ProductDTO:
    def __init__(self, product):
        self.offer_id = product.get_offer_id()
        self.name = product.get_name()
        self.company = product.get_company()
        self.colors = product.get_colors()
        self.sizes = product.get_sizes()
        self.description = product.get_description()
        self.photos = product.get_photos()
