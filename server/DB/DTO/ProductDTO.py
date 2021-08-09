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
        self.offer_id = product.offer_id
        self.name = product.name
        self.company = product.company
        self.color = product.color
        self.size = product.size
        self.description = product.description
        self.photos = product.photos
