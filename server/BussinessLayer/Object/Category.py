

from BussinessLayer.Object import SubCategory
class Category:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.sub_categories_dictionary  = {}

    def add_sub_category(self, name, sub_category_id):
        sub_category_to_add = SubCategory.SubCategory(name, sub_category_id, self.id)

        if sub_category_id in self.sub_categories_dictionary.keys():
            return None
        self.sub_categories_dictionary[sub_category_id] = sub_category_to_add
        return sub_category_to_add

    def remove_sub_category(self, sub_category_id):

        if sub_category_id not in self.sub_categories_dictionary:
            return None
        sub_category_to_remove = self.sub_categories_dictionary[sub_category_id]
        self.sub_categories_dictionary.pop(sub_category_id, None)
        return sub_category_to_remove


    def add_offer(self,offer_id, user_id, product, sub_category_id, steps, end_date ):
        # already checked if sub category exist
        return self.sub_categories_dictionary[sub_category_id].add_offer(offer_id, user_id, product, steps, end_date )

    def remove_offer(self, offer_id, sub_category_id):
        #already checked if sub category exist
        return self.sub_categories_dictionary[sub_category_id].remove_offer(offer_id)


    def set_name(self, new_name):
        self.name = new_name

    def update_sub_category_name(self, sub_category_id,new_sub_category_name):
        if not self.is_exist_sub_category(sub_category_id):
            return None
        self.sub_categories_dictionary[sub_category_id].set_name(new_sub_category_name)
        return self.sub_categories_dictionary[sub_category_id]






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

    def get_offer_by_offer_id(self, offer_id):
        for sub_categoty_id in self.sub_categories_dictionary.keys():
            offer_to_return = self.sub_categories_dictionary[sub_categoty_id].get_offer_by_offer_id(offer_id)
            if offer_to_return is not None:
                return offer_to_return
        return None







#----------------------------------------------------private methods --------------------------------------------
    def is_exist_sub_category(self, sub_category_id):
        if sub_category_id in self.sub_categories_dictionary:
            return True
        return False