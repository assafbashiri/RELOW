from BussinessLayer.Object import *

class CategoryService:
    def __init__(self, name, id, con):
        self.name = name
        self.id = id
        self.sub_categories_dictionary  = None

    def __init__(self, business_category):
        self.name = business_category.get_name()
        self.id = business_category.get_id()
        self.sub_categories_dictionary = business_category.get_sub_category_dictionery()


    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_sub_categories_dict(self):
        return self.sub_categories_dictionary

