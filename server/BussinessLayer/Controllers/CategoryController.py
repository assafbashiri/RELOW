from BussinessLayer.Object import Category
from BussinessLayer.Object import SubCategory
from DB.DAO import CategoriesDAO
from DB.DAO import SubCategoriesDAO
class categoryController:

    def __init__(self, conn):
        print('starting category')
        self.category_id = 0
        self.sub_category_id = 0
        self.category_dictionary = None # <category id, category>
        self.categoriesDAO = CategoriesDAO
        self.sub_categoriesDAO = SubCategoriesDAO

    def getme(self):
        print('return singelton')
        return self

    def add_category(self, name):
        category_to_add = Category(name, self.category_id)
        self.category_dictionary[self.category_id] = category_to_add
        self.category_id += 1
        # adding to DB
        self.categoriesDAO.insert(category_to_add)

    def remove_category(self, category_id):
        self.check_category_exist(category_id)
        category_to_remove = self.category_dictionary[category_id]
        self.category_dictionary.pop(category_id, None) # check
        #remove category from DB
        self.categoriesDAO.delete(category_to_remove)
        #self.categoriesDAO.delete(category_id)

    def add_sub_category(self, name, category_id):
        self.check_category_exist(category_id)
        sub_category_to_add = self.category_dictionary[category_id].add_sub_category(name, category_id)
        if sub_category_to_add is None :
            raise Exception("Sub Category already exist")
        # adding to DB (maybe do it in sub category)
        self.sub_categoriesDAO.insert(sub_category_to_add)


    def remove_sub_category(self, sub_category_id, category_id ):
        self.check_category_exist(category_id)
        sub_category_to_remove = self.category_dictionary[category_id].remove_sub_category(sub_category_id)
        if sub_category_to_remove is None:
            raise Exception("No Such Sub Category")
        #removing sub category from DB
        self.sub_categoriesDAO.remove(sub_category_to_remove)


    # return offer that added
    def add_offer(self, user_id, product, category_id, sub_category_id, status, steps, end_date, current_buyers ):
        self.check_category_exist(category_id)
        if not self.category_dictionary[category_id].is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist")
        offer_to_add = self.category_dictionary[category_id].add_offer(user_id, product, sub_category_id, status, steps, end_date, current_buyers )
        #checkif needed
        if offer_to_add is None:
            raise Exception("Fail To Add Offer")
        return offer_to_add
        #add to the userrrrr

    # return id of the offer to remove
    def remove_offer(self, offer_id, category_id, sub_category_id):
        self.check_category_exist(category_id)
        if not self.category_dictionary[category_id].is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist")
        try:
            offer_to_remove = self.category_dictionary[category_id].remove_offer(offer_id, sub_category_id)
        except Exception as e:
            raise e

        #remove offer from DB
        self.sub_categoriesDAO.remove(offer_to_remove)


#------------------------------------------------update -----------------------------------------------------

    def update_current_step(self, offer, current_step):
        self.check_category_exist(offer.category_id)
        self.category_dictionary[offer.category_id].update_current_step(offer, current_step)
        # update in DB

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









#----------------------------------------------------------------------------------------------------------------



    # check input validity in client layer
    def update_category_name(self, category_id, new_category_name):
        self.check_category_exist(category_id)
        self.category_dictionary[category_id].set_name(new_category_name)
        #update in DB
        self.categoriesDAO.update(self.category_dictionary[category_id])


    def update_sub_category_name(self, category_id, sub_category_id, new_sub_category_name):
        self.check_category_exist(category_id)
        updated_sub_category = self.category_dictionary[category_id].update_sub_category_name(sub_category_id,new_sub_category_name)
        if updated_sub_category is None:
            raise Exception ("No Such Sub Category")
        # update in DB
        self.sub_categoriesDAO.update(updated_sub_category)

   


#--------------------------------------------getters-------------------------------------------------
    #return regular list
    def get_offers_by_category(self, category_id):
        self.check_category_exist(category_id)
        return self.category_dictionary[category_id].get_offers()

    #return regular list
    def get_offers_by_sub_category(self, category_id, sub_category_id):
        self.check_category_exist(category_id)
        if not self.category_dictionary[category_id].is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist")
        return self.category_dictionary[category_id].get_offers_by_sub_category(sub_category_id)


    def get_offers_by_product_name(self, product_name):
        ans = None
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_product_name(product_name)
            if not category_offers is None:
                ans.add(category_offers)
        return ans


    def get_offers_by_status(self, status):
        ans = None
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_status(status)
            if not category_offers is None:
                ans.add(category_offers)
        return ans

    def get_offers_by_company_name(self, company_name):
        ans = None
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_company_name(company_name)
            if not category_offers is None:
                ans.add(category_offers)
        return ans

#check if possible to replace 3 functions them with one generic function




    def add_buyer_to_offer(self, offer_id, offer_category_id,offer_sub_category_id , user_id):
        self.check_category_exist(offer_category_id)
        if not self.category_dictionary[offer_category_id].is_exist_sub_category(offer_sub_category_id):
            raise Exception("Sub Category Does Not Exist")
        try:
            self.category_dictionary[offer_category_id].add_buyer_to_offer(offer_id, offer_sub_category_id, user_id)
        except Exception as e:
            raise e
        # update offer in DB - "buyers in offer" table

    def remove_buyer_from_offer(self, offer_id, offer_category_id,offer_sub_category_id , user_id):
        self.check_category_exist(offer_category_id)
        if not self.category_dictionary[offer_category_id].is_exist_sub_category(offer_sub_category_id):
            raise Exception("Sub Category Does Not Exist")
        try:
            self.category_dictionary[offer_category_id].remove_buyer_from_offer(offer_id, offer_sub_category_id, user_id)
        except Exception as e:
            raise e
        # update offer in DB - "buyers in offer" table

#-------------------------------------------------privatemethods ------------------------------------------
    def is_category_exist(self, category_id):
        if category_id in self.category_dictionary:
            return True
        return False

    def check_category_exist(self, category_id):
        if category_id not in self.category_dictionary:
            raise Exception("Category Does Not Exist")