from BusinessLayer.Object import *

class CategoryService:
    def __init__(self, business_category):
        self.name = business_category.get_name()
        self.sub_categories_names = business_category.get_sub_categories_names()





    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_sub_categories_dict(self):
        return self.sub_categories_dictionary

