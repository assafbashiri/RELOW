class ProductDTO:
    def __init__(self, offer_id,name, company, color, size, description, photos):
        self.offer_id = offer_id
        self.name = name
        self.company = company
        self.color = color
        self.size = size
        self.description = description
        self.photos

    def __init__(self, product):
        self.offer_id = product.get_offer_id()
        self.name = product.get_name()
        self.company = product.get_company()
        self.color = product.get_color()
        self.size = product.get_size()
        self.description = product.get_description()
        self.photos = product.get_photos()
