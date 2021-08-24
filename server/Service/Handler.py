

from Object.UserService import UserService
from Object.CategoryService import CategoryService
from Object.StepService import StepService
from Object.SubCategoryService import SubCategoryService
from Object.OfferService import OfferService
from Object.ProductService import ProductService
from server.BusinessLayer.Controllers.CategoryController import CategoryController

from server.BusinessLayer.Controllers.UserController import UserController
from server.Response import Response


class Handler:

    def __init__(self, conn):
        self.conn = conn
        self.user = None

        self. category_controller = CategoryController.getInstance()
        self.user_controller = UserController.getInstance()
        self.switcher = {1: self.register,
                         2: self.unregister,
                         3: self.log_in,
                         4: self.logout,
                         5: self.update_first_name,
                         6: self.update_last_name,
                         7: self.update_user_name,
                         8: self.update_email,
                         9: self.update_birth_date,
                         10: self.update_gender,
                         11: self.add_address_details,
                         12: self.add_payment_method,
                         13: self.get_all_history_buy_offers,
                         14: self.get_all_history_sell_offers,
                         15: self.get_history_buy_offer,
                         16: self.get_history_sell_offer,
                         17: self.get_all_active_buy_offers,
                         18: self.get_all_active_sell_offers,
                         19: self.get_active_buy_offer,
                         20: self.get_active_sell_offer,
                         21: self.get_liked_offer,
                         22: self.get_all_liked_offers,
                         23: self.add_active_buy_offer,
                         24: self.add_active_sell_offer,
                         25: self.add_liked_offer,
                         26: self.remove_liked_offer,
                         27: self.remove_active_sell_offer,
                         28: self.remove_active_buy_offer,
                         29: self.add_category,
                         30: self.add_sub_category,
                         31: self.add_photo,
                         32: self.remove_category,
                         33: self.remove_sub_category,
                         34: self.remove_photo,
                         35: self.update_category_name,
                         36: self.update_sub_category_name,
                         37: self.update_category_for_offer,
                         38: self.update_sub_category_for_offer,
                         39: self.update_end_date,
                         40: self.update_start_date,
                         41: self.update_step,
                         42: self.update_product_name,
                         43: self.update_product_company,
                         44: self.update_product_color,
                         45: self.update_product_size,
                         46: self.update_product_description,
                         47: self.get_offers_by_category,
                         48: self.get_offers_by_sub_category,
                         49: self.get_offers_by_product_name,
                         50: self.get_offers_by_status,
                         51: self.get_hot_deals,
                         52: self.add_to_hot_deals,
                         53: self.remove_from_hot_deals,
                         54: self.update_step_for_offer,
                         55: self.update_password}

    # ------------------------------------------------userController----------------------------------------------------

    # -------------------------------------------------BASIC------------------------------------------------------------

    def unregister(self, argument):
        try:
            self.user_controller.unregister(self.user.user_id)
            return Response(None, 'Unregistered Successfully', True)
        except Exception as e:
            return Response(None, str(e), False)

    def register(self, argument):
        try:
            user = self.user_controller.register(
                                          argument['first_name'],
                                          argument['last_name'],
                                          argument['user_name'],
                                          argument['email'],
                                          argument['password'],
                                          argument['birth_date'],
                                          argument['gender'])
            return Response(user.user_id, "Registered Successfully", True), True
        except Exception as e:
            return Response(None, str(e), False), True

    def log_in(self, argument):
        try:
            user = self.user_controller.log_in(argument['user_name'], argument['password'])
            self.user = user
            return Response(user.user_id, "Log-In Successfully", True), False
        except Exception as e:
            return Response(None, str(e), False), False

    def logout(self, argument):
        try:
            self.user_controller.logout(self.user.user_id)
            return Response(None, "Log-Out Successfully", True), False
        except Exception as e:
            return Response(None, str(e), False), False

# -------------------------------------------------ADD------------------------------------------------------------------

    def add_active_buy_offer(self, argument):
        try:
            offer = self.category_controller.get_offer_by_offer_id(argument['offer_id'])
            self.user_controller.add_active_buy_offer(self.user.user_id, offer, argument['quantity'], argument['step'])
            return Response(OfferService(offer), "Joined To Offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def add_active_sell_offer(self, argument):
        offer = None
        try:
            offer = self.category_controller.add_offer(self.user.user_id,
                                                       argument['name'],
                                                       argument['company'],
                                                       argument['color'],
                                                       argument['size'],
                                                       argument['description'],
                                                       argument['photos'],
                                                       argument['category_id'],
                                                       argument['sub_category_id'],
                                                       argument['steps'],
                                                       argument['end_date'],)
            self.user_controller.add_active_sale_offer(offer)
            return Response(OfferService(offer), "Offer Added Successfully", True)
        except Exception as e:
            if str(e) == "wow":
                self.category_controller.remove_offer(offer)
            return Response(None, str(e), False)

    def add_liked_offer(self, argument):
        try:
            offer = self.category_controller.get_offer_by_offer_id(argument['offer_id'])
            self.user_controller.add_like_offer(self.user.user_id, offer)
            return Response(OfferService(offer), "Offer Added SuccessfullyTo Liked Offers", True)
        except Exception as e:
            return Response(None, str(e), False)

    def add_address_details(self, argument):
        try:
            self.user_controller.add_address_details(self.user.user_id,
                                                     argument['city'],
                                                     argument['street'],
                                                     argument['zip_code'],
                                                     argument['floor'],
                                                     argument['apt'])
            return Response(None, "Address Details Added Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    # def update_city(argument): user_id *
    # def update_street(argument): user_id *
    # def update_zip_code(argument): user_id *
    # def update_floor(argument): user_id *
    # def update_apt(argument): user_id *

    def add_payment_method(self, argument):
        try:
            self.user_controller.add_payment_method(self.user.user_id,
                                                    argument['credit_card_number'],
                                                    argument['expire_date'],
                                                    argument['cvv'],
                                                    argument['card_type'],
                                                    argument['id_number'])
            return Response(None, "Payment Added Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    # def update_card_number(argument): user_id *
    # def update_expire_date(argument): user_id *
    # def update_cvv(argument): user_id *
    # def update_id_number user_id *
    # def update_card_type(argument): user_id *
    # -------------------------------------------------REMOVE------------------------------------------------------------------

    def remove_liked_offer(self, argument):
        try:
            self.user_controller.remove_like_offer(self.user.user_id, argument['offer_id'])
            return Response(None, "Offer Removed From Liked Offers", True)
        except Exception as e:
            return Response(None, str(e), False)

    def remove_active_sell_offer(self, argument):
        try:
            offer = self.category_controller.remove_offer(argument['offer_id'])
            self.user_controller.remove_active_sale_offer(offer)
            return Response(OfferService(offer), "Offer Removed Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def remove_active_buy_offer(self, argument):
        try:
            self.user_controller.remove_active_buy_offer(self.user.user_id, argument['offer_id'])
            return Response(None, "Offer Removed Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

# -------------------------------------------------UPDATE----------------------------------------------------------------

    def update_first_name(self, argument):
        try:
            self.user_controller.update_first_name(self.user.user_id, argument['first_name'])
            return Response(None, "First Name Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_last_name(self, argument):
        try:
            self.user_controller.update_last_name(self.user.user_id, argument['last_name'])
            return Response(None, "Last Name Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_user_name(self, argument):
        try:
            self.user_controller.update_username(self.user.user_id, argument['user_name'])
            return Response(None, "Username Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_email(self, argument):
        try:
            self.user_controller.update_email(self.user.user_id,
                                              argument['email'])
            return Response(None, "Email Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_password(self, argument):
        try:
            self.user_controller.update_password(self.user.user_id,
                                                 argument['old_password'],
                                                 argument['new_password'])
            return Response(None, "Password Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_birth_date(self, argument):
        try:
            self.user_controller.update_birth_date(self.user.user_id,
                                                   argument['birth_date'])
            return Response(None, "Birth Date Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_gender(self, argument):
        try:
            self.user_controller.gender(self.user.user_id,
                                        argument['gender'])
            return Response(None, "gender Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

# -------------------------------------------------GET------------------------------------------------------------------

    def get_all_history_buy_offers(self, argument):
        try:
            lis = []
            offer_list = self.user_controller.get_all_history_buy_offer(self.user.user_id)
            for offer in offer_list:
                lis.append(offer)
            return Response(lis, 'All History Sell Offers', True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_all_history_sell_offers(self, argument):
        try:
            offers_list = self.user_controller.get_all_history_sell_offer(self.user.user_id)
            lis = []
            for offer in offers_list:
                lis.append(OfferService(offer))
            return Response(lis, "All History Sell Offers", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_history_buy_offer(self, argument):
        try:
            offer = self.user_controller.get_history_buy_offer(argument['offer_id'])
            return Response(OfferService(offer), "Got offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_history_sell_offer(self, argument):
        try:
            offer = self.user_controller(argument['offer_id'])
            return Response(OfferService(offer), "Got Offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_all_active_buy_offers(self, argument):
        try:
            offer_buy_list = self.user_controller.get_all_buy_offer(self.user.user_id)
            lis = []
            for offer in offer_buy_list:
                lis.append(OfferService(offer))
            return Response(lis, "All Active Buy Offers", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_all_active_sell_offers(self, argument):
        try:
            offer_sell_list = self.user_controller.get_all_sell_offer(self.user.user_id)
            lis = []
            for offer in offer_sell_list:
                lis.append(OfferService(offer))
            return Response(lis, "All Active Sell Offers", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_active_buy_offer(self, argument):
        try:
            offer = self.user_controller.get_buy_offer(self.user.user_id, argument['offer_id'])
            return Response(OfferService(offer), "Got Offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_active_sell_offer(self, argument):
        try:
            offer = self.user_controller.get_sell_offer(self.user.user_id, argument['offer_id'])
            return Response(OfferService(offer), "Got Offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_liked_offer(self, argument):
        try:
            offer = self.user_controller.get_liked_offer(self.user.user_id, argument['offer_id'])
            return Response(OfferService(offer), "Update Sub-Category Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_all_liked_offers(self, argument):
        try:
            liked_offers_list = self.user_controller.get_all_liked_offer(self.user.user_id)
            lis = []
            for offer in liked_offers_list:
                lis.append(OfferService(offer))
            return Response(lis, "All Liked Sell Offers", True)
        except Exception as e:
            return Response(None, str(e), False)

# --------------------------------------------------categoryController-------------------------------------------------------

# -----------------------------------------------------ADD-------------------------------------------------------------------

    def add_category(self, argument):
        try:
            self.category_controller.add_category(argument['name'])
            return Response(None, "Category Added Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def add_sub_category(self, argument):
        try:
            self.category_controller.add_sub_category(argument['name'], argument['category_id'])
            return Response(None, "Sub-Category Added Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def add_photo(self, argument):
        pass

    def add_to_hot_deals(self, argument):
        response = self.category_controller.add_to_hot_deals(argument['offer_id'])
        return response

# ------------------------------------------------REMOVE------------------------------------------------------------

    def remove_category(self, argument):
        try:
            self.category_controller.remove_category(argument['category_id'])
            return Response(None, "Category Removed Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def remove_sub_category(self, argument):
        try:
            self.category_controller.remove_category(argument['sub_category_id'],
                                                     argument['category_id'])
            return Response(None, "Sub-Category Removed Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def remove_photo(self, argument):
        pass

    def remove_from_hot_deals(self, argument):
        try:
            self.category_controller.remove_from_hot_deals(argument['offer_id'])
            return Response(None, "Offer Removed Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)


    # -------------------------------------------------------UPDATE----------------------------------------------------------------------
    def update_category_name(self, argument):
        try:
            self.category_controller.update_category_name(argument['category_id'],
                                                          argument['name'])
            return Response(None, "Category Name Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_sub_category_name(self, argument):
        try:
            self.category_controller.update_sub_category_name(argument['category_id'],
                                                              argument['sub_category_id'],
                                                              argument['name'])
            return Response(None, "Update Sub-Category Name Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_category_for_offer(self, argument):
        try:
            offer = self.category_controller.update_category_for_offer(argument['offer_id'],
                                                                           argument['category_id'],
                                                                           argument['sub_category_id'])
            return Response(OfferService(offer), "Update Category Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_sub_category_for_offer(self, argument):
        try:
            offer = self.category_controller.update_sub_category_for_offer(argument['offer_id'],
                                                                           argument['sub_category_id'])
            return Response(OfferService(offer), "Update Sub-Category For Offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_end_date(self, argument):
        try:
            self.user_controller.update_end_date(argument['offer_id'], argument['end_date'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_start_date(self, argument):
        try:
            self.user_controller.update_start_date(argument['offer_id'], argument['start_date'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_step(self, argument):
        try:
            self.user_controller.update_step_for_user(self.user.user_id, argument['offer_id'], argument['step'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_product_name(self, argument):
        try:
            self.user_controller.update_product_name(argument['offer_id'], argument['name'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_product_company(self, argument):
        try:
            self.user_controller.update_product_company(argument['offer_id'], argument['company'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_product_color(self, argument):
        try:
            self.user_controller.update_product_color(argument['offer_id'], argument['color'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_product_size(self, argument):
        try:
            self.user_controller.update_size(argument['offer_id'], argument['size'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_product_description(self, argument):
        try:
            self.user_controller.update_product_description(argument['offer_id'], argument['description'])
            return Response(None, "Update Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    # -------------------------------------------------------GET---------------------------------------------------------------

    def get_offers_by_category(self, argument):
        try:
            offers_list = self.category_controller.get_offers_by_category(argument['category_id'])
            return Response(offers_list, "Offers Lists Received Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_offers_by_sub_category(self, argument):
        try:
            offers_list = self.category_controller.get_offers_by_sub_category(argument['category_id'],
                                                                              argument['sub_category_id'])
            return Response(offers_list, "Offers Lists Received Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_offers_by_product_name(self, argument):
        try:
            offers_list = self.category_controller.get_offers_by_product_name(argument['name'])
            return Response(offers_list, "Offers Lists Received Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_offers_by_status(self, argument):
        try:
            offers_list = self.category_controller.get_offers_by_status(argument['status'])
            return Response(offers_list, "Offers Lists Received Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def get_hot_deals(self, argument):
        try:
            offers_list = self.category_controller.get_hot_deals()
            return Response(offers_list, "Offers Lists Received Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_step_for_offer(self, argument):
        try:
            self.category_controller.update_step_for_offer(argument['offer_id'],argument['step_number'],argument['quantity'],argument['price'])
            return Response(None, "Step Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def handling(self, argument):
        req = argument['op']
        func = self.switcher.get(int(req), "nada")
        return func(argument)
