class ProductService:

    def __init__(self, name, company, color, size, description, photos, offer_id):
        self.name = name
        self.company = company
        self.color = color
        self.size = size
        self.description = description
        self.photos = photos
        self.offer_id=offer_id

    # ---------------------------------------------GETTERS-----------------------------------------------------------------

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_description(self):
        return self.description

    def get_photos(self):
        return self.photos

    def get_offer_id(self):
        return self.offer_id


# ---------------------------------------------SETTERS-----------------------------------------------------------------


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