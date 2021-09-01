
class SubCategoryService:

    def __init__(self, business_sub_category):
        self.name = business_sub_category.get_name()
        self.offers_dictionary = business_sub_category.get_offers_dictionery()
        self.id = business_sub_category.get_id()
        self.father_category_id = business_sub_category.get_father_category_id()

    def get_name(self):
        return self.name

    def get_offers_dictionery(self):
        return self.offers_dictionary

    def get_father_category_id(self):
        return self.father_category_id

