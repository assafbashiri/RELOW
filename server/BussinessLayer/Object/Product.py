class Product:
    def __init__(self, name, company, color, size, description, photos):
        self.name = name
        self.company = company
        self.color = color
        self.size = size
        self.description = description
        self.photos = photos
        self.offer_id = -1

    def set_offer_id(self,offer_id):
        self.offer_id = offer_id