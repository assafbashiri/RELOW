class UserAddress:
    def __init__(self):
        self.city = None
        self.street = None
        self.apartment_number = None
        self.zip_code = None
        self.floor = None

    def add_address_details(self, city, street, apartment_number, zip_code, floor):

        # tool bar to choose the address
        self.city = city
        self.street = street
        self.apartment_number = apartment_number
        self.zip_code = zip_code
        self.floor = floor

    def set_city(self, city):
        self.city = city

    def set_street(self, street):
        self.street = street

    def set_apartment_number(self, apartment_number):
        self.apartment_number = apartment_number

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_floor(self, floor):
        self.floor = floor

    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def get_apartment_number(self):
        return self.apartment_number

    def get_zip_code(self):
        return self.zip_code

    def get_floor(self):
        return self.floor
