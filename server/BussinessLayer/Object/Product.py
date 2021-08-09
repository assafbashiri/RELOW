class Product:
    def __init__(self, name, company, color, size, description, photos):
        self.name = name
        self.company = company
        self.color = color
        self.size = size
        self.description = description
        self.photos = photos
        self.offer_id = -1

    def set_name(self, name):
        self.name = name

    def set_company(self, company):
        self.company = company

    def set_color(self, color):
        self.color = color

    def set_size(self, size):
        self.size = size

    def set_description(self, description):
        self.description = description

    def set_photos(self, photos):
        self.photos = photos

    def set_offer_id(self, offer_id):
        self.offer_id = offer_id