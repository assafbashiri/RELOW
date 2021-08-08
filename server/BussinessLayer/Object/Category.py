from BussinessLayer.Object.SubCategory import SubCategory
from BussinessLayer.DataMappers import SubCategoriesMapper


from BussinessLayer.Object.SubCategory import SubCategory
class Category:
    def _init_(self, name, id, con):
        self.name = name
        self.id = id
        self.sub_categories_dictionary  = None

    def add_sub_category(self, name, sub_category_id):
        sub_category_to_add = SubCategory(name, self.id, sub_category_id)
        if sub_category_id in self.sub_categories_dictionary:
            return None
        self.sub_categories_dictionary[sub_category_id] = sub_category_to_add
        return sub_category_to_add

    def remove_sub_category(self, sub_category_id):

        if sub_category_id not in self.sub_categories_dictionary:
            return None
        sub_category_to_remove = self.sub_categories_dictionary[sub_category_id]
        self.sub_categories_dictionary.pop(sub_category_id, None)
        return sub_category_to_remove

    def add_offer(self, user_id, product, sub_category_id, status, steps, end_date, current_buyers ):
        # already checked if sub category exist
        self.sub_categories_dictionary[sub_category_id].add_offer(user_id, product, status, steps, end_date, current_buyers )

    def remove_offer(self, offer_id, sub_category_id):
        #already checked if sub category exist
        try:
            return self.sub_categories_dictionary[sub_category_id].remove_offer(offer_id)
        except Exception as e:
            raise e


    def set_name(self, new_name):
        self.name = new_name

    def update_sub_category_name(self, sub_category_id,new_sub_category_name):
        if not self.is_exist_sub_category(sub_category_id):
            return None
        self.sub_categories_dictionary[sub_category_id].set_name(new_sub_category_name)
        return self.sub_categories_dictionary[sub_category_id]

    def add_buyer_to_offer(self, offer_id, offer_sub_category_id , user_id):
        try:
            self.sub_categories_dictionary[offer_sub_category_id].add_buyer_to_offer(offer_id, user_id)
        except Exception as e:
            raise e

    def remove_buyer_from_offer(self, offer_id, offer_sub_category_id , user_id):
        try:
            self.sub_categories_dictionary[offer_sub_category_id].remove_buyer_from_offer(offer_id, user_id)
        except Exception as e:
            raise e


#----------------------------------------------------getters----------------------------------------------------

    def get_offers(self):
        all_category_offers = None
        curr_sub_category_offers = None
        for sub_category_id in self.sub_categories_dictionary.keys:
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers()
            if not curr_sub_category_offers is None:
                all_category_offers.extend(curr_sub_category_offers)

        return all_category_offers

    def get_offers_by_sub_category(self, sub_category_id):
        #already checked if sub category exist
        return self.sub_categories_dictionary[sub_category_id].get_offers()

    def get_offers_by_product_name(self, product_name):
        ans = None
        for sub_category_id in self.sub_categories_dictionary.keys():
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers_by_product_name(product_name)
            if not curr_sub_category_offers is None:
                ans.extend(curr_sub_category_offers)
        return ans

    def get_offers_by_company_name(self, company_name):
        ans = None
        for sub_category_id in self.sub_categories_dictionary.keys():
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers_by_company_name(company_name)
            if not curr_sub_category_offers is None:
                ans.extend(curr_sub_category_offers)
        return ans

    def get_offers_by_status(self, status):
        ans = None
        for sub_category_id in self.sub_categories_dictionary.keys():
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers_by_status(status)
            if not curr_sub_category_offers is None:
                ans.extend(curr_sub_category_offers)
        return ans




#----------------------------------------------------private methods --------------------------------------------
    def is_exist_sub_category(self, sub_category_id):
        if sub_category_id in self.sub_categories_dictionary:
            return True
        return False