from BusinessLayer.Object.Category import Category
from DB.DTO.CategoryDTO import CategoryDTO
from DB.DTO.SubCategotyDTO import SubCategoryDTO
from DB.DTO.OfferDTO import OfferDTO
from DB.DAO.CategoriesDAO import CategoriesDAO
from DB.DAO.OfferDAO import OfferDAO
from DB.DAO.SubCategoriesDAO import SubCategoriesDAO
from BusinessLayer.Object.Product import Product
from BusinessLayer.Object.Purchase import Purchase
from BusinessLayer.Object.Step import Step
from BusinessLayer.Object.SubCategory import SubCategory
from BusinessLayer.Object.Offer import Offer
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


            self.category_dictionary = {}  # <category id, category>
            self.categoriesDAO = CategoriesDAO(conn)
            self.sub_categoriesDAO = SubCategoriesDAO(conn)
            self.offerDAO = OfferDAO(conn)

            self.category_id = self.categoriesDAO.load_category_id()
            self.sub_category_id = self.sub_categoriesDAO.load_sub_category_id()
            self.offer_id = self.offerDAO.load_offer_id()

            self.hot_deals = {}
            self.conn = conn

    def getme(self):
        print('return singelton')
        return self

    # no return, throw exceptions
    def add_category(self, name):
        if self.check_category_exist_by_name(name):
            raise Exception("Category Name Already Exist")
        category_to_add = Category(name, self.category_id)
        self.category_dictionary[self.category_id] = category_to_add
        self.category_id += 1
        # adding to DB
        self.categoriesDAO.insert(CategoryDTO(category_to_add))

    # no return, throw exceptions
    def remove_category(self, category_id):
        self.check_category_exist(category_id)
        category_to_remove = self.category_dictionary[category_id]
        self.category_dictionary.pop(category_id, None) # check
        #remove category from DB
        self.categoriesDAO.delete(CategoryDTO(category_to_remove))
        #self.categoriesDAO.delete(category_id)

    # no return, throw exceptions
    def add_sub_category(self, name, category_id):
        self.check_category_exist(category_id)
        sub_category_to_add = self.category_dictionary[category_id].add_sub_category(name, category_id)
        if sub_category_to_add is None :
            raise Exception("Sub Category already exist")
        # adding to DB (maybe do it in sub category)
        self.sub_categoriesDAO.insert(SubCategoryDTO(sub_category_to_add))

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
        self.sub_categoriesDAO.delete(SubCategoryDTO(sub_category_to_remove))


    # return offer that added, throw exceptions
    def add_offer(self, user_id, name, company, color, size, description, photos , category_id, sub_category_id, steps, end_date ):

        product = Product(self.offer_id, name, company, color, size, description, photos)
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

    def get_all_expired_offers(self):
        ans = []
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_all_expired_offers()
            if category_offers is not None:
                ans.extend(category_offers)
        for offer in ans:
            self.remove_offer(offer.offer_id)

        return ans

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
        self.sub_categoriesDAO.update(SubCategoryDTO(updated_sub_category))

   


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
        ans = []
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_product_name(product_name)
            if category_offers is not None:
                ans.extend(category_offers)
        return ans

    # return regular list, throw exceptions
    def get_offers_by_status(self, status):
        ans = []
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_status(status)
            if category_offers is not None:
                ans.extend(category_offers)
        return ans

    # return regular list, throw exceptions
    def get_offers_by_company_name(self, company_name):
        ans = []
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_company_name(company_name)
            if category_offers is not None:
                ans.extend(category_offers)
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

    def load(self):

        all_categories = self.categoriesDAO.load_all_categories()
        for c in all_categories:
            category = Category(c[1], c[0])
            self.category_dictionary[c[0]] = category

        #load_all_sub_categories for each category
        all_sub_categoties = self.sub_categoriesDAO.load_all_sub_categories()
        for sub_c in all_sub_categoties:
            sub_category = SubCategory(sub_c[2], sub_c[0], sub_c[1])
            self.category_dictionary[sub_c[1]].add_sub_category_for_load(sub_category)

        return self.load_all_offers()

    #return list of all offers
    def load_all_offers(self):
        all_offers_to_return = []

        # load_all offers for each sub category
        all_offers = self.offerDAO.load_all_offers()
        all_products = self.productDAO.load_all_products()
        all_steps = self.offerDAO.load_all_steps()
        all_current_buyers = self.offerDAO.load_buyers_in_offers()

        all_steps_dictionary = {}
        self.load_all_steps(all_steps, all_steps_dictionary)
        all_products_dictionary = {}
        self.load_all_products(all_products, all_products_dictionary)
        all_current_buyers_dict = {}
        self.load_all_current_buyers(all_current_buyers, all_current_buyers_dict)
        total_products_per_offer = {}
        self.load_all_total_products(total_products_per_offer, all_current_buyers_dict)


        for o in all_offers:
            if (len(all_current_buyers_dict) == 0):
                current_buyers = {}
                total_products = 0
            else:
                current_buyers = all_current_buyers_dict[o[0]]
                total_products = total_products_per_offer[o[0]]

            offer = Offer(o[0], o[1], all_products_dictionary[o[0]], o[7], o[8], o[4], all_steps_dictionary[o[0]], o[2],o[3], current_buyers, total_products)
            all_offers_to_return.append(offer)
            self.category_dictionary[o[7]].add_offer_for_load(offer, o[8])
            if (o[9] is True): #add to hot deals
                self.hot_deals[o[0]] = offer

        return all_offers_to_return

    def load_all_steps(self, all_steps, all_steps_dictionary):
        for s in all_steps:
            if s[0] not in all_steps_dictionary.keys():
                all_steps_dictionary[s[0]] = {}
            step = Step(s[2], s[3])
            all_steps_dictionary[s[0]][s[1]] = step

    def load_all_products(self, all_products, all_products_dictionary):
        for p in all_products:
            photos = []
            for i in range(6, 16):
                photos.append(p[i])
            product = Product(p[1], p[2], p[3], p[4], p[5], photos, p[0])
            all_products_dictionary[p[0]] = product

    def load_all_current_buyers(self,all_current_buyers , all_current_buyers_dict):
        for cb in all_current_buyers:
            if cb[0] not in all_current_buyers_dict.keys():
                all_current_buyers_dict[cb[0]] = {}
            purchase = Purchase(cb[2], cb[3])
            all_current_buyers_dict[cb[0]][cb[1]] = purchase

    def load_all_total_products(self,total_products_per_offer, all_current_buyers_dict):
        # initialize with zero
        for offer_id in all_current_buyers_dict.keys():
            total_products_per_offer[offer_id] = 0

        for offer_id in all_current_buyers_dict.keys():
            total_products_per_offer[offer_id] += all_current_buyers_dict[offer_id].get_quantity()