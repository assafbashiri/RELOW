class Product:
    def __init__(self, offer_id, name, company, colors, sizes, description, photos):
        self.name = name
        self.company = company
        self.colors = colors
        self.sizes = sizes
        self.description = description
        self.photos = photos
        self.offer_id = offer_id

    # ------------ SETTERS

    def set_name(self, name):
        self.name = name

    def set_company(self, company):
        self.company = company

    def set_colors(self, colors):
        self.colors = colors

    def set_sizes(self, sizes):
        self.sizes = sizes

    def set_description(self, description):
        self.description = description

    def set_photos(self, photos):
        self.photos = photos

    def set_offer_id(self, offer_id):
        self.offer_id = offer_id

    # ------------ GETTERS

    def get_company(self):
        return self.company

    def get_name(self):
        return self.name

    def get_colors(self):
        return self.colors

    def get_sizes(self):
        return self.sizes

    def get_description(self):
        return self.description

    def get_photos(self):
        return self.photos

    def get_offer_id(self):
        return self.offer_id

    def build_list_from_string(self, str):
        x=6
        answer = str.split(", ")
        return answer

