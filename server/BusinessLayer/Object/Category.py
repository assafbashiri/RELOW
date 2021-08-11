

from BusinessLayer.Object import SubCategory
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
        all_category_offers = []


        curr_sub_category_offers = []
        for sub_category_id in self.sub_categories_dictionary.keys():
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers()
            if curr_sub_category_offers is not None:
                all_category_offers.extend(curr_sub_category_offers)

        return all_category_offers

    def get_offers_by_sub_category(self, sub_category_id):
        #already checked if sub category exist
        s= self.sub_categories_dictionary[sub_category_id].get_offers()
        return s
    def get_offers_by_product_name(self, product_name):
        ans = []
        for sub_category_id in self.sub_categories_dictionary.keys():
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers_by_product_name(product_name)
            if curr_sub_category_offers is not None:
                ans.extend(curr_sub_category_offers)
        return ans

    def get_offers_by_company_name(self, company_name):
        ans = []
        for sub_category_id in self.sub_categories_dictionary.keys():
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers_by_company_name(company_name)
            if curr_sub_category_offers is not None:
                ans.extend(curr_sub_category_offers)
        return ans

    def get_offers_by_status(self, status):
        ans = []
        for sub_category_id in self.sub_categories_dictionary.keys():
            curr_sub_category_offers = self.sub_categories_dictionary[sub_category_id].get_offers_by_status(status)
            if  curr_sub_category_offers is not None:
                ans.extend(curr_sub_category_offers)
        return ans

    def get_offer_by_offer_id(self, offer_id):
        for sub_category_id in self.sub_categories_dictionary.keys():
            offer_to_return = self.sub_categories_dictionary[sub_categoty_id].get_offer_by_offer_id(offer_id)
            if offer_to_return is not None:
                return offer_to_return
        return None

    def update_category_for_offer(self, offer_to_move, new_category_id, new_sub_category_id):
        return  7

    def update_sub_category_for_offer(self, offer_to_move, new_sub_category_id):
        #already checked if new sub category exist
        if new_sub_category_id not in self.sub_categories_dictionary.keys():
            raise Exception("No Such Sub Category")
        self.sub_categories_dictionary[offer_to_move.sub_category_id].remove_offer_for_update_sub_category(offer_to_move.offer_id)
        self.sub_categories_dictionary[new_sub_category_id].add_offer_for_update_sub_category(offer_to_move)





#----------------------------------------------------private methods --------------------------------------------
    def is_exist_sub_category(self, sub_category_id):
        if sub_category_id in self.sub_categories_dictionary:
            return True
        return False
