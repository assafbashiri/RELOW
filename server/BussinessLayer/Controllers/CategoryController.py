from BussinessLayer.Object import Category
from DB.DTO import CategoryDTO
from DB.DTO import SubCategotyDTO
from DB.DAO import CategoriesDAO
from DB.DAO import SubCategoriesDAO
class CategoryController:
    __instance = None

    def getInstance():
        """ Static access method. """
        if CategoryController.__instance == None:
            CategoryController
        return CategoryController.__instance

    def __init__(self, conn):
        if CategoryController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CategoryController.__instance = self
            self.category_id = 0
            self.sub_category_id = 0
            self.offer_id = 0
            self.category_dictionary = {}  # <category id, category>
            self.categoriesDAO = CategoriesDAO.CategoriesDAO(conn)
            self.sub_categoriesDAO = SubCategoriesDAO.SubCategoriesDAO(conn)
            self.hot_deals = {}
            self.conn = conn

    def getme(self):
        print('return singelton')
        return self

    def add_category(self, name):
        if self.check_category_exist_by_name(name):
            raise Exception("Category Name Already Exist")
        category_to_add = Category.Category(name, self.category_id)
        self.category_dictionary[self.category_id] = category_to_add
        self.category_id += 1
        # adding to DB
        self.categoriesDAO.insert(CategoryDTO.CategoryDTO(category_to_add))

    def remove_category(self, category_id):
        self.check_category_exist(category_id)
        category_to_remove = self.category_dictionary[category_id]
        self.category_dictionary.pop(category_id, None) # check
        #remove category from DB
        self.categoriesDAO.delete(CategoryDTO.CategoryDTO(category_to_remove))
        #self.categoriesDAO.delete(category_id)

    def add_sub_category(self, name, category_id):
        self.check_category_exist(category_id)
        sub_category_to_add = self.category_dictionary[category_id].add_sub_category(name, category_id)
        if sub_category_to_add is None :
            raise Exception("Sub Category already exist")
        # adding to DB (maybe do it in sub category)
        self.sub_categoriesDAO.insert(SubCategotyDTO.SubCategoryDTO(sub_category_to_add))

    def remove_sub_category(self, sub_category_id, category_id ):
        self.check_category_exist(category_id)
        sub_category_to_remove = self.category_dictionary[category_id].remove_sub_category(sub_category_id)
        if sub_category_to_remove is None:
            raise Exception("No Such Sub Category")
        #removing sub category from DB
        self.sub_categoriesDAO.delete(SubCategotyDTO.SubCategoryDTO(sub_category_to_remove))


    # return offer that added
    def add_offer(self, user_id, product, category_id, sub_category_id, steps, end_date ):
        self.check_category_exist(category_id)
        if not self.category_dictionary[category_id].is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist")

        offer_to_add = self.category_dictionary[category_id].add_offer(self.offer_id, user_id, product, sub_category_id, steps, end_date )
        #checkif needed
        if offer_to_add is None:
            raise Exception("Fail To Add Offer")
        self.offer_id += 1
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

    def add_photo(self, argument):
        pass

    def remove_photo(self, argument):
        pass

    def add_to_hot_deals(self, argument):
        pass

    def remove_from_hot_deals(self, argument):
        pass

    def remove_buyer_from_offer(self):
        return 6


#------------------------------------------------update -----------------------------------------------------



















        # -------------------------------------------------------UPDATE----------------------------------------------------------------------









        # -------------------------------------------------------GET---------------------------------------------------------------









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

    def get_offer_by_offer_id(self, offer_id):
        for category_id in self.category_dictionary.keys():
            offer_to_return = self.category_dictionary[category_id].get_offer_by_offer_id(offer_id)
            if offer_to_return is not None:
                return offer_to_return
        raise Exception("Offer Does Not Exist")

    def get_hot_deals(self, argument):
        pass

    def update_category_for_offer(self, argument):
        pass

    def update_sub_category_for_offer(self, argument):
        pass

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

    def check_category_exist_by_name(self, name):
        for id in self.category_dictionary.keys():
            if self.category_dictionary[id].name == name:
                return True
        return False


