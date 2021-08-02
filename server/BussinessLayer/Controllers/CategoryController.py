from BussinesLayer.Objects import Category
from BussinesLayer.DataMappers import CategoriesMapper
from BussinesLayer.Objects import SubCategory
class categoryController():
    def _init_(self, con):
        self.category_id = 0
        self.category_mapper = CategoriesMapper(con) #################

    def add_category(self, name):
        category_to_add = Category(name, self.category_id)
        self.category_id += 1
        self.category_mapper.add_category(category_to_add)
        # adding to DB in CategoriesMapper

    def remove_category(self, category_id):
        self.category_mapper.remove_category(category_id)

    def add_sub_category(self, name, category_id):
        category = self.category_mapper.get_category(category_id)
        if category is None:
            raise Exception("No Such Category")
        category.add_sub_category(name, category_id)
        # adding to DB in Category

    def remove_sub_category(self, sub_category_id, category_id ):
        category = self.category_mapper.get_category(category_id)
        if category is None:
            raise Exception("No Such Category")
        category.remove_sub_category(sub_category_id, category_id)





    # return offer that added
    def add_offer(self, user_id, product, category_id, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers ):
        if category_id not in self.category_list.keys():
            raise Exception("No Such Category")
        self.category_list.get(category_id).add_offer(self, user_id, product, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers )
        #add to the userrrrr

    # return id of the offer to remove
    def remove_offer(self,offer_to_remove):
        if offer_to_remove.category_id not in self.category_list.keys:
            raise Exception("Category Does Not Exist")
        if offer_to_remove.sub_category_id not in self.category_list.get(offer_to_remove.category_id).keys:
            raise Exception("Sub Category Does Not Exist")
        self.category_list.get(offer_to_remove.category_id).get(offer_to_remove.sub_category_id).offer_list.remove(offer_to_remove.offer_id, offer_to_remove)


#------------------------------------------------update -----------------------------------------------------

    def update_category_name(self, category_id, new_category_name):
        self.category_mapper.update_category_name(category_id, new_category_name)

    def update_sub_category_name(self, category_id, sub_category_id, new_sub_category_name):
        category = self.category_mapper.get_category(category_id)
        category.update_sub_category_name(category_id, sub_category_id, new_sub_category_name)

    def update_current_step(self, offer, current_step):
        return 3
    def update_category_for_offer(self, offer, category_id):
        return 3
    def update_sub_category_for_offer(self, offer, subCategory_id):
        return 3
    def update_status(self, offer, status):
        return 2
    def update_start_date(self, offer, subCategory_id):
        return 3
    def update_end_date(self, offer, end_date):
        return 2
    def update_step(self, offer, category_id):
        return 3
    def update_product_name(self, offer, subCategory_id):
        return 3
    def update_product_company(self, offer, subCategory_id):
        return 3
    def update_product_color(self, offer, subCategory_id):
        return 3
    def update_product_size(self, offer, subCategory_id):
        return 3
    def update_product_description(self, offer, subCategory_id):
        return 3
    def add_product_photo(self, offer, subCategory_id):
        return 3
    def remove_product_photo(self, offer, subCategory_id):
        return 3


#--------------------------------------------getters-------------------------------------------------
    def get_offers_by_category(self, name):
        return 5
    def get_offers_by_sub_category(self, name):
        return 5
    def get_offers_by_product_name(self, name):
        return 5
    def get_offers_by_status(self, name):
        return 5
    def get_offers_by_company(self, name):
        return 5






    def add_buyer_to_offer(self, offer, status):
        return 2
    def remove_buyer_from_offer(self, offer, status):
        return 2

#-------------------------------------------------privatemethods ------------------------------------------