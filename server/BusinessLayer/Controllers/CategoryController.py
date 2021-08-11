from BusinessLayer.Object import Category
from DB.DTO import CategoryDTO
from DB.DTO import SubCategotyDTO
from DB.DTO.OfferDTO import OfferDTO
from DB.DAO import CategoriesDAO
from DB.DAO import OfferDAO
from DB.DAO import SubCategoriesDAO
from BusinessLayer.Object import Product
from BusinessLayer.Object import Purchase
from BusinessLayer.Object.Step import Step
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
            self.offerDAO = OfferDAO.OfferDAO(conn)
            self.hot_deals = {}

            self.conn = conn

    def getme(self):
        print('return singelton')
        return self

    # no return, throw exceptions
    def add_category(self, name):
        if self.check_category_exist_by_name(name):
            raise Exception("Category Name Already Exist")
        category_to_add = Category.Category(name, self.category_id)
        self.category_dictionary[self.category_id] = category_to_add
        self.category_id += 1
        # adding to DB
        self.categoriesDAO.insert(CategoryDTO.CategoryDTO(category_to_add))

    # no return, throw exceptions
    def remove_category(self, category_id):
        self.check_category_exist(category_id)
        category_to_remove = self.category_dictionary[category_id]
        self.category_dictionary.pop(category_id, None) # check
        #remove category from DB
        self.categoriesDAO.delete(CategoryDTO.CategoryDTO(category_to_remove))
        #self.categoriesDAO.delete(category_id)

    # no return, throw exceptions
    def add_sub_category(self, name, category_id):
        self.check_category_exist(category_id)
        sub_category_to_add = self.category_dictionary[category_id].add_sub_category(name, category_id)
        if sub_category_to_add is None :
            raise Exception("Sub Category already exist")
        # adding to DB (maybe do it in sub category)
        self.sub_categoriesDAO.insert(SubCategotyDTO.SubCategoryDTO(sub_category_to_add))

    def add_sub_category_by_name(self, name, category_name):
        category = self.get_category_by_name(category_name)
        self.add_sub_category(name, category.id)

    # no return, throw exceptions
    def remove_sub_category(self, sub_category_id, category_id ):
        self.check_category_exist(category_id)
        sub_category_to_remove = self.category_dictionary[category_id].remove_sub_category(sub_category_id)
        if sub_category_to_remove is None:
            raise Exception("No Such Sub Category")
        #removing sub category from DB
        self.sub_categoriesDAO.delete(SubCategotyDTO.SubCategoryDTO(sub_category_to_remove))


    # return offer that added, throw exceptions
    def add_offer(self, user_id, name, company, color, size, description, photos , category_id, sub_category_id, steps, end_date ):

        product = Product.Product(name, company, color, size, description, photos)
        self.check_category_exist(category_id)
        if not self.category_dictionary[category_id].is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist")
        offer_to_add = self.category_dictionary[category_id].add_offer(self.offer_id, user_id, product, sub_category_id, steps, end_date )
        if offer_to_add is None:
            raise Exception("Fail To Add Offer")
        self.offer_id += 1
        return offer_to_add
        #add to the userrrrr


        # update total_products field
        self.get_sum_of_products_quantity()




    # return id of the offer to remove, throw exceptions
    def remove_offer(self, offer_id):
        offer_to_remove = self.get_offer_by_offer_id(offer_id)
        return self.category_dictionary[offer_to_remove.category_id].remove_offer(offer_id, offer_to_remove.sub_category_id)



    # no return, throw exceptions
    def add_to_hot_deals(self, offer_id):
        offer_to_add = self.get_offer_by_offer_id(offer_id)
        self.hot_deals[offer_id] = offer_to_add
        #update in db
        self.offerDAO.update(OfferDTO(offer_to_add))

    # no return, throw exceptions
    def remove_from_hot_deals(self, offer_id):
        if offer_id not in self.hot_deals:
            raise Exception("Offer Does Not Exist In Hot Deals")
        offer_to_remove = self.hot_deals[offer_id]
        self.hot_deals.pop(offer_id, None)
        self.offerDAO.update(OfferDTO(offer_to_remove))



    def add_step(self, products_amount, price):
        step = Step(products_amount, price)


    #------------------------------------------------update -----------------------------------------------------


    # check input validity in client layer
    # no return, throw exceptions
    def update_category_name(self, category_id, new_category_name):
        self.check_category_exist(category_id)
        self.category_dictionary[category_id].set_name(new_category_name)
        #update in DB
        self.categoriesDAO.update(CategoryDTO.CategoryDTO(self.category_dictionary[category_id]))

    # no return, throw exceptions
    def update_sub_category_name(self, category_id, sub_category_id, new_sub_category_name):
        self.check_category_exist(category_id)
        updated_sub_category = self.category_dictionary[category_id].update_sub_category_name(sub_category_id,new_sub_category_name)
        if updated_sub_category is None:
            raise Exception ("No Such Sub Category")
        # update in DB
        self.sub_categoriesDAO.update(SubCategotyDTO.SubCategoryDTO(updated_sub_category))

   


#--------------------------------------------getters-------------------------------------------------

    #return regular list, throw exceptions
    def get_offers_by_category(self, category_id):
        self.check_category_exist(category_id)
        return self.category_dictionary[category_id].get_offers()

    #return regular list, throw exceptions
    def get_offers_by_sub_category(self, category_id, sub_category_id):
        self.check_category_exist(category_id)
        if not self.category_dictionary[category_id].is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist")
        return self.category_dictionary[category_id].get_offers_by_sub_category(sub_category_id)

    # check if possible to replace those 3 functions with one generic function

    # return regular list, throw exceptions
    def get_offers_by_product_name(self, product_name):
        ans = None
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_product_name(product_name)
            if category_offers is not None:
                ans.extend(category_offers)
        return ans

    # return regular list, throw exceptions
    def get_offers_by_status(self, status):
        ans = None
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_status(status)
            if category_offers is not None:
                ans.add(category_offers)
        return ans

    # return regular list, throw exceptions
    def get_offers_by_company_name(self, company_name):
        ans = None
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_company_name(company_name)
            if category_offers is not None:
                ans.add(category_offers)
        return ans

    # return regular list, throw exceptions
    def get_offer_by_offer_id(self, offer_id):
        for category_id in self.category_dictionary.keys():
            offer_to_return = self.category_dictionary[category_id].get_offer_by_offer_id(offer_id)
            if offer_to_return is not None:
                return offer_to_return
        raise Exception("Offer Does Not Exist")

    # return regular list
    def get_hot_deals(self):
        return self.hot_deals.values()

    #return the updated offer, throw exceptions
    def update_category_for_offer(self, offer_id, new_category_id, new_sub_category_id):
        offer_to_move = self.get_offer_by_offer_id(offer_id)
        self.is_category_exist(new_category_id)
        if not self.category_dictionary[new_category_id].is_exist_sub_category(new_sub_category_id):
            raise Exception("No Such Sub Category")
        #removing the offer from the old category
        self.category_dictionary.pop(offer_to_move.offer_id, None)
        # adding the offer to the new sub category
        self.category_dictionary[new_category_id] = offer_to_move

        offer_to_move.set_category_id(new_category_id)
        offer_to_move.set_sub_category_id(new_category_id)
        return offer_to_move



        self.update_sub_category_for_offer(offer_id, new_sub_category_id)


    #return the updated offer, throw exceptions

    def update_sub_category_for_offer(self, offer_id, new_sub_category_id):
        offer_to_move = self.get_offer_by_offer_id(offer_id)
        self.category_dictionary[offer_to_move.category_id].update_sub_category_for_offer(offer_id, new_sub_category_id)

        offer_to_move.set_sub_category_id(new_sub_category_id)
        return offer_to_move










#-------------------------------------------------privatemethods ------------------------------------------
    def is_category_exist(self, category_id):
        if category_id in self.category_dictionary.keys():
            return True
        return False

    def check_category_exist(self, category_id):
        if category_id not in self.category_dictionary.keys():
            raise Exception("Category Does Not Exist")

    def get_category_by_name(self, category_name):
        for category_id in self.category_dictionary.keys():
            if self.category_dictionary[category_id].name == category_name:
                return self.category_dictionary[category_id]
        raise Exception("Category Does Not Exist")

    def check_category_exist_by_name(self, name):
        for id in self.category_dictionary.keys():
            if self.category_dictionary[id].name == name:
                return True
        return False



