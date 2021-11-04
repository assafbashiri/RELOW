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

from BusinessLayer.Utils.OfferStatus import OfferStatus


class CategoryController:
    __instance = None

    def getInstance():
        """ Static access method. """
        if CategoryController.__instance == None:
            CategoryController()
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
    def remove_category(self, category_name):
        category_to_remove = self.get_category_by_name(category_name)
        if category_to_remove.is_contain_sub_categories():
            raise Exception("Can not remove category while it contains sub categories")
        self.category_dictionary.pop(category_to_remove.get_id(), None)  # check
        # remove category from DB
        self.categoriesDAO.delete(CategoryDTO(category_to_remove))
        # self.categoriesDAO.delete(category_to_remove.get_id())

    # no return, throw exceptions
    def add_sub_category(self, name, category_name):
        category = self.get_category_by_name(category_name)
        sub_category_to_add = category.add_sub_category(name, self.sub_category_id)
        if sub_category_to_add is None:
            raise Exception("Sub Category name is already exist")
        # adding to DB
        self.sub_category_id += 1
        self.sub_categoriesDAO.insert(SubCategoryDTO(sub_category_to_add))

    def add_sub_category_by_name(self, name, category_name):
        category = self.get_category_by_name(category_name)
        self.add_sub_category(name, category.id)

    # no return, throw exceptions
    def remove_sub_category(self, sub_category_name, category_name):
        sub_category_id = self.get_sub_category_by_name(sub_category_name)
        category = self.get_category_by_name(category_name)
        category_id = category.get_id()
        if category.is_contained_offers(sub_category_id):
            raise Exception("Can not remove sub category while it contains offers")
        sub_category_to_remove = self.category_dictionary[category_id].remove_sub_category(sub_category_id)
        if sub_category_to_remove is None:
            raise Exception("No Such Sub Category")
        # removing sub category from DB
        self.sub_categoriesDAO.delete(SubCategoryDTO(sub_category_to_remove))

    # return offer that added, throw exceptions
    def add_offer(self, user_id, name, company, colors, sizes, description, photos, category_name, sub_category_name, steps, end_date, hot_deals):
        category = self.get_category_by_name(category_name)
        sub_category = self.get_sub_category_by_name(sub_category_name)
        sub_category_id = sub_category.get_id()
        if not category.is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist in this category")
        product = Product(self.offer_id, name, company, colors, sizes, description, photos)
        offer_to_add = category.add_offer(self.offer_id, user_id, product, sub_category_id, steps, end_date, hot_deals)
        self.offer_id += 1
        self.add_to_hot_deals(offer_to_add.offer_id)
        return offer_to_add

    # return offer to remove, throw exceptions
    def remove_offer(self, offer_id):
        offer_to_remove = self.get_offer_by_offer_id(offer_id)
        category = self.get_category_by_id(offer_to_remove.category_id)
        return category.remove_offer(offer_id, offer_to_remove.sub_category_id)

    # no return, throw exceptions
    def add_to_hot_deals(self, offer_id):
        print('added to hot deals')
        offer_to_add = self.get_offer_by_offer_id(offer_id)
        self.hot_deals[offer_id] = offer_to_add
        offer_to_add.set_hot_deals(True)
        # update in db
        self.offerDAO.update(OfferDTO(offer_to_add))

    # no return, throw exceptions
    def remove_from_hot_deals(self, offer_id):
        if offer_id not in self.hot_deals:
            raise Exception("Offer Does Not Exist In Hot Deals")
        offer_to_remove = self.hot_deals[offer_id]
        self.hot_deals.pop(offer_id, None)
        offer_to_remove.set_hot_deals(False)
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

    def get_offers_to_confirm(self):
        ans = []
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers()
            if category_offers is not None:
                ans.extend(category_offers)
        return ans

    def confirm_offer(self, offer):
        offer.confirm = True
        offer_update = self.offerDAO.update(OfferDTO(offer))
        return offer
    # ------------------------------------------------update -----------------------------------------------------
    # check input validity in client layer
    # no return, throw exceptions
    def update_category_name(self, category_name, new_category_name):
        category = self.get_category_by_name(category_name)
        category.set_name(new_category_name)
        category_id = category.get_id()
        # update in DB
        self.categoriesDAO.update(CategoryDTO.CategoryDTO(self.category_dictionary[category_id]))

    # no return, throw exceptions
    def update_sub_category_name(self, category_name, sub_category_name, new_sub_category_name):
        category = self.get_category_by_name(category_name)
        sub_category = self.get_sub_category_by_name(sub_category_name)
        sub_category_id = sub_category.get_id()
        updated_sub_category = category.update_sub_category_name(sub_category_id, new_sub_category_name)
        if updated_sub_category is None:
            raise Exception("No Such Sub Category")
        # update in DB
        self.sub_categoriesDAO.update(SubCategoryDTO(updated_sub_category))

    def update_step_for_offer(self, offer_id,step_number, quantity, price):
        offer_to_update = self.get_offer_by_offer_id(offer_id)
        offer_to_update.set_steps(step_number, quantity, price)
    # --------------------------------------------getters-------------------------------------------------

    # return regular list, throw exceptions
    def get_offers_by_category(self, category_name):
        category = self.get_category_by_name(category_name)
        return category.get_offers()

    # return regular list, throw exceptions
    def get_offers_by_sub_category(self, catgory_name, sub_catgory_name):
        category = self.get_category_by_name(catgory_name)
        sub_category = self.get_sub_category_by_name(sub_catgory_name)
        category_id = category.get_id()
        sub_category_id = sub_category.get_id()
        if not category.is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category Does Not Exist in this category")
        return category.get_offers_by_sub_category(sub_category_id)

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
    def get_offers_by_price(self, price):
        ans = []
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_price(price)
            if category_offers is not None:
                ans.extend(category_offers)
        return ans

    # return regular list, throw exceptions
    def get_offers_by_end_date(self, end_date):
        ans = []
        for category_id in self.category_dictionary.keys():
            category_offers = self.category_dictionary[category_id].get_offers_by_end_date(end_date)
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
        ans = []
        ans.extend(self.hot_deals.values())
        return ans

    # # return the updated offer, throw exceptions
    # def update_sub_category_for_offer(self, offer_id, new_category_id, new_sub_category_id):
    #     offer_to_move = self.get_offer_by_offer_id(offer_id)
    #     old_sub_category_id = offer_to_move.get_sub_category_id()
    #     old_category = self.get_category_by_id(offer_to_move.category_id)
    #     new_category = self.get_category_by_id(new_category_id)
    #     if not new_category.is_exist_sub_category(new_sub_category_id):
    #         raise Exception("No Such Sub Category")
    #     # removing the offer from the old category
    #     old_category.remove_offer(offer_id, old_sub_category_id)
    #     # adding the offer to the new sub category
    #     offer_to_move.set_category_id(new_category_id)
    #     offer_to_move.set_sub_category_id(new_category_id)
    #     new_category.add_exist_offer(offer_to_move, new_sub_category_id)
    #     self.offerDAO.update(OfferDTO(offer_to_move))
    #     return offer_to_move
    #

    def update_sub_category_for_offer(self, offer_id, new_category_name, new_sub_category_name):
        offer_to_move = self.get_offer_by_offer_id(offer_id)
        old_sub_category_id = offer_to_move.get_sub_category_id()
        old_category = self.get_category_by_id(offer_to_move.category_id)
        new_category = self.get_category_by_name(new_category_name)
        new_sub_category = self.get_sub_category_by_name(new_sub_category_name)
        if not new_category.is_exist_sub_category_by_name(new_sub_category_name):
            raise Exception("No Such Sub Category")
        # removing the offer from the old category
        old_category.remove_offer(offer_id, old_sub_category_id)
        # adding the offer to the new sub category

        offer_to_move.set_category_id(new_category.id)
        offer_to_move.set_sub_category_id(new_sub_category.id)
        new_category.add_exist_offer(offer_to_move, new_sub_category.id)
        self.offerDAO.update(OfferDTO(offer_to_move))
        return offer_to_move

    def get_sub_cat_name(self, cat_id, sub_cat_id):
        return [self.category_dictionary[cat_id].sub_categories_dictionary[sub_cat_id].name,
        self.category_dictionary[cat_id].name]

    # -------------------------------------------------load methods -----------------------------------------
    def load(self):
        all_categories = self.categoriesDAO.load_all_categories()
        for c in all_categories:
            category = Category(c[1], c[0])
            self.category_dictionary[c[0]] = category
        # load_all_sub_categories for each category
        all_sub_categoties = self.sub_categoriesDAO.load_all_sub_categories()
        for sub_c in all_sub_categoties:
            sub_category = SubCategory(sub_c[2], sub_c[0], sub_c[1])
            self.category_dictionary[sub_c[1]].add_sub_category_for_load(sub_category)
        return self.load_all_offers()

    # return list of all offers
    def load_all_offers(self):
        # all_history_offers = self.offerDAO.load_history_sellers()
        # all_history_buyers = self.offerDAO.load_history_buyers()
        all_offers_to_return = {}
        history_offers_to_return = {}
        # load_all offers for each sub category
        all_offers = self.offerDAO.load_all_offers()
        all_history_offers = self.offerDAO.load_history_offers()
        all_products = self.offerDAO.load_all_products()
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
            if o[0] not in all_current_buyers_dict.keys():
                current_buyers = {}
                total_products = 0
            else:
                current_buyers = all_current_buyers_dict[o[0]]
                total_products = total_products_per_offer[o[0]]

            hot = False
            if o[8] == 1:
                hot = True

            confirm = False
            if o[9] == 1:
                confirm = True

            offer = Offer(o[0], o[1], all_products_dictionary[o[0]], o[6], o[7], OfferStatus.ACTIVE, all_steps_dictionary[o[0]], o[2],
                          o[3], current_buyers, total_products,hot, confirm)

            all_offers_to_return[o[0]] = offer
            self.category_dictionary[o[6]].add_offer_for_load(offer, o[7])
            if hot is True:  # add to hot deals
                self.hot_deals[o[0]] = offer

        for o in all_history_offers:
            if o[0] not in all_current_buyers_dict.keys():
                current_buyers = {}
                total_products = 0
            else:
                current_buyers = all_current_buyers_dict[o[0]]
                total_products = total_products_per_offer[o[0]]

            hot = False
            if o[8] == 1:
                hot = True

            status = self.build_status(o[4])

            offer = Offer(o[0], o[1], all_products_dictionary[o[0]], o[6], o[7], status, all_steps_dictionary[o[0]], o[2],
                          o[3], current_buyers, total_products,hot, True)

            history_offers_to_return[o[0]] = offer


        return all_offers_to_return, history_offers_to_return

    def load_all_steps(self, all_steps, all_steps_dictionary):
        for s in all_steps:
            if s[0] not in all_steps_dictionary.keys():
                all_steps_dictionary[s[0]] = {}
            step = Step(s[3], s[4], s[2])
            all_steps_dictionary[s[0]][s[1]] = step

    def load_all_products(self, all_products, all_products_dictionary):
        for p in all_products:
            photos = []
            for i in range(6, 16):
                photos.append(p[i])
            product = Product(p[0], p[1], p[2], p[3], p[4], p[5], photos)
            all_products_dictionary[p[0]] = product

    def load_all_current_buyers(self, all_current_buyers, all_current_buyers_dict):
        for cb in all_current_buyers:
            if cb[0] not in all_current_buyers_dict.keys():
                all_current_buyers_dict[cb[0]] = {}
            purchase = Purchase(cb[2], cb[3], cb[1], cb[4], cb[5], cb[6])
            all_current_buyers_dict[cb[0]][cb[1]] = purchase

    def load_all_total_products(self, total_products_per_offer, all_current_buyers_dict):
        # initialize with zero
        for offer_id in all_current_buyers_dict.keys():
            total_products_per_offer[offer_id] = 0

        for offer_id in all_current_buyers_dict.keys():
            for user_id in all_current_buyers_dict[offer_id].keys():
                total_products_per_offer[offer_id] += all_current_buyers_dict[offer_id][user_id].get_quantity()

        # -------------------------------------------------private methods -----------------------------------------
    def get_category_by_id(self, category_id):
        if category_id not in self.category_dictionary.keys():
            raise Exception("Category Does Not Exist")
        return self.category_dictionary[category_id]

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

    # check !!!!
    def get_sub_category_by_name(self, sub_category_name):
        for catID in self.category_dictionary.keys():
            cat = self.get_category_by_id(catID)
            for sub_catID in cat.sub_categories_dictionary.keys():
                sub_cat = cat.sub_categories_dictionary[sub_catID]
                if sub_cat.get_name() == sub_category_name:
                    return sub_cat
        raise Exception("not exist sub category with this name")

    def get_all_categories(self):
        # categories_dict = {} # key:name of category, value: dict-key:name_of_sub_category, value:
        # for category in self.category_dictionary.values():
        #     categories_dict[category.get_name] = category.get_sub_categories_names()
        ans = []
        categories = self.category_dictionary.values()
        for cat in categories:
            ans.append(cat)
        return ans

    def build_status(self, status_string):
        if status_string == "ACTIVE":
            return 1
        if status_string == "DONE":
            return 2
        if status_string == "CANCELED_BY_SELLER":
            return 3
        if status_string == "CANCELED_BY_BUYER":
            return 4
        if status_string == "EXPIRED_ZERO_BUYERS":
            return 5



