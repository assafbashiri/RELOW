
from BusinessLayer.Controllers.UserController import UserController
from BusinessLayer.Controllers.CategoryController import CategoryController
import Response

from Response import Response
from Service.Object.UserService import UserService
from Service.Object.CategoryService import CategoryService
from Service.Object.StepService import StepService
from Service.Object.SubCategoryService import SubCategoryService
from Service.Object.OfferService import OfferService
from Service.Object.ProductService import ProductService
class Protocol:

    def __init__(self, conn):
        self.conn = conn
        self.user = None

        self. category_controller = CategoryController.getInstance()
        self.user_controller = UserController.getInstance()
        self.switcher =  {1: self.register,
                          2: self.unregister,
                          3: self.log_in,
                          4: self.logout,
                          5: self.update_first_name,
                          6: self.update_last_name,
                          7: self.update_username,
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
                     ## for userController
                         29: self.add_category,
                         30: self.add_sub_category,
                         31: self.add_offer,
                         32: self.add_photo,
                         33: self.remove_category,
                         34: self.remove_sub_category,
                         35: self.remove_photo,
                         36: self.remove_offer,
                         37: self.update_category_name,
                         38: self.update_sub_category_name,
                    # # 39: update_current_step,
                         40: self.update_category_for_offer,
                         41: self.update_sub_category_for_offer,
                    # 42: 'update_status',
                         43: self.update_end_date,
                         44: self.update_start_date,
                         45: self.update_step,
                         46: self.add_buyer_to_offer,
                         47: self.remove_buyer_from_offer,
                         48: self.update_product_name,
                         49: self.update_product_company,
                         50: self.update_product_color,
                         51: self.update_product_size,
                         52: self.update_product_description,
                         53: self.get_offers_by_category,
                         54: self.get_offers_by_subcategory,
                         55: self.get_offers_by_product_name,
                         56: self.get_offers_by_status,
                         57: self.get_hot_deals,
                         58: self.add_to_hot_deals,
                         59: self.remove_to_hot_deals
                    }

    # ------------------------------------------------userController----------------------------------------------------

    # -------------------------------------------------BASIC------------------------------------------------------------

    def unregister(self, argument): #user_id
        try:
            self.user_controller.unregister(argument['user_id'])
            return Response(None, 'Unregistered Successfully', True)
        except Exception as e:
            return Response(None,str(e), False)



    def register(self, argument): #first_name, last_name , username , email , password, gender, date of birth
        try:
            user = self.user_controller.register(
                                          argument['first_name'],
                                          argument['last_name'],
                                          argument['user_name'],
                                          argument['email'],
                                          argument['password'],
                                          argument['birth_date'],
                                          argument['gender'])
            return Response(user, "Registered Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def log_in(self, argument): #user_name , password
        try:
            user = self.user_controller.log_in(argument['user_name'], argument['password'])
            self.user = user
            return Response(UserService(user), "Log-In Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def logout(self, argument): #user_id
        try:
            self.user_controller.logout(argument['user_id'])
            return Response(None, "Log-Out Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)


# -------------------------------------------------ADD------------------------------------------------------------------
    def add_active_buy_offer(self, argument):
        try:
            offer = self.category_controller.get_offer_by_offer_id(argument['offer_id'])
            self.user_controller.add_active_buy_offer(self.user.user_id, offer, argument['quantity'], argument['step'])
            self.category_controller.add_buyer_to_offer(offer,
                                                        self.user.user_id,
                                                        argument['quantity'],
                                                        argument['step'])
            return Response(OfferService(offer), "Joined To Offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def add_active_sell_offer(self, argument):
        try:
            offer = self.category_controller.add_offer(argument['user_id'],
                                                          argument['product'],
                                                          argument['category_id'],
                                                          argument['sub_category_id'],
                                                          argument['status'],
                                                          argument['steps'],
                                                          argument['end_date'],
                                                          0)
            self.user_controller.add_active_sale_offer(offer)
            return Response(None, "Offer Added Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def add_liked_offer(self, argument):
        try:
            offer = self.category_controller.get_offer_by_offer_id(argument['offer_id'])
            self.user_controller.add_like_offer(self.user.user_id, offer)
            return Response(OfferService(offer), "Offer Added Successfully")
        except Exception as e:
            return Response(None, str(e), False)

    def add_address_details(self, argument): #user_id city street zip code floor apt
        try:
            self.user_controller.add_address_details(argument['user_id'],
                                                                argument['city'],
                                                                argument['street'],
                                                                argument['zip_code'],
                                                                argument['floor'],
                                                                argument['apt'])
            return Response(None, "Address Added Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    # def update_city(argument): user_id *
    # def update_street(argument): user_id *
    # def update_zip_code(argument): user_id *
    # def update_floor(argument): user_id *
    # def update_apt(argument): user_id *

    def add_payment_method(self, argument): # user_id , cc number, cc expire date, cvv, card_type, id
        try:
            self.user_controller.add_payment_method(argument['user_id'],
                                                               argument['credit_card_number'],
                                                               argument['expire_date'],
                                                               argument['cvv'],
                                                               argument['card_type'],
                                                               argument['id_number'])
            return Response(None, "Payment Adedd Successfully", True)
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
            self.user_controller.remove_like_offer(self.user.user_id)
            return Response(None, "Offer Removed")
        except Exception as e:
            return Response(None, str(e), False)

    def remove_active_sell_offer(self, argument):
        try:
            self.user_controller.remove_active_sale_offer(self.user.user_id, argument['offer_id'])
            offer_id = self.category_controller.remove_offer(argument['offer_id'],
                                                             argument['category_id'],
                                                             argument['sub_category_id'])
            return Response(offer_id, "Offer Removed Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def remove_active_buy_offer(self, argument):
        try:
            self.user_controller.remove_active_sale_offer(self.user.user_id, argument['offer_id'])
            self.category_controller.remove_buyer_from_offer(self.user.user_id, argument['offer_id'])
            return Response(None, "Offer Removed Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

# -------------------------------------------------UPDATE----------------------------------------------------------------

    def update_first_name(self, argument): #user_id first name
        try:
            self.user_controller.update_first_name(argument['user_id'], argument['first_name'])
            return Response(None, "First Name Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_last_name(self, argument):#user_id last name
        try:
            self.user_controller.update_last_name(argument['user_id'], argument['last_name'])
            return Response(None, "Last Name Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_user_name(self, argument): #user_id username
        try:
            self.user_controller.update_username(argument['user_id'], argument['user_name'])
            return Response(None, "Username Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_email(self, argument): #user_id email
        try:
            self.user_controller.update_email(argument['user_id'], argument['email'])
            return Response(None, "Email Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_password(self, argument): #user_id old new
        try:
            self.user_controller.update_password(argument['user_id'], argument['old_password'], argument['new_password'])
            return Response(None, "Password Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_birth_date(self, argument): #user_id date of birth
        try:
            self.user_controller.update_birth_date(argument['user_id'], argument['birth_date'])
            return Response(None, "Birth Date Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_gender(self, argument): #user-id gender
        try:
            self.user_controller.gender(argument['user_id'], argument['gender'])
            return Response(None, "gender Updated Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

# -------------------------------------------------GET------------------------------------------------------------------

    def get_all_history_buy_offers(self, argument):
        try:
            lis  = []
            offer_list = self.user_controller.get_all_history_buy_offer(self.user.user_id)
            # for offer in offer_list:
            #     lis.append()
        except Exception as e:
            return Response(None, str(e), False)

    def get_all_history_sell_offers(self, argument):
        response = self.user_controller.get_all_history_sell_offer(self.user.user_id)
        return response

    def get_history_buy_offer(self, argument):
        pass

    def get_history_sell_offer(self, argument):
        pass

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

    def add_offer(self, argument): #implemented in user_controller
        pass

    def add_photo(self, argument):
        pass

    def add_buyer_to_offer(self, argument):#implemented in user_controller
        pass

    def add_to_hot_deals(self, argument):
        response = self.category_controller.add_to_hot_deals(argument['offer_id'])
        return response

    #------------------------------------------------REMOVE------------------------------------------------------------------

    def remove_category(self, argument):
        response = self.category_controller.remove_category(argument['category_id'])
        return response

    def remove_sub_category(self, argument):
        response = self.category_controller.remove_category(argument['sub_category_id'],
                                                            argument['category_id'])
        return response

    def remove_photo(self, argument):
        pass

    def remove_offer(self, argument): #implemented in user_controller
        pass

    def remove_buyer_from_offer(self, argument):#implemented in user_controller
        pass

    def remove_from_hot_deals(self, argument):
        response = self.category_controller.remove_from_hot_deals(argument['offer_id'])
        return response

    # -------------------------------------------------------UPDATE----------------------------------------------------------------------
    def update_category_name(self, argument):
        response = self.category_controller.update_category_name(argument['category_id'],
                                                                 argument['name'])
        return response

    def update_sub_category_name(self, argument):
        try:
            self.category_controller.update_sub_category_name(argument['category_id'],
                                                                     argument['sub_category_id'],
                                                                     argument['name'])
            return Response(None, "Update Sub-Category Name Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    #def update_current_step automatic
    
    def update_category_for_offer(self, argument):
        try:
            response = self.category_controller(argument['offer_id'],
                                            argument['category_id'],
                                            argument['sub_category_id'])
            return Response(None, "Update Category Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def update_sub_category_for_offer(self, argument):
        try:
            offer = self.category_controller.update_sub_category_for_offer(argument['offer_id'],
                                                                          argument['sub_category_id'])
            return Response(OfferService(offer), "Update Sub-Category For Offer Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    #def update_status automatic

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
            self.user_controller.update_step(argument['offer_id'], argument['step'])
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

    def get_offers_by_subcategory(self, argument):
        try:
            offers_list = self.category_controller.get_offers_by_sub_category(argument['category_id'], argument['sub_category_id'])
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

    def remove_to_hot_deals(self, argument):
        try:
            self.category_controller.remove_from_hot_deals(argument['offer_id'])
            return Response(None, "Offers Lists Received Successfully", True)
        except Exception as e:
            return Response(None, str(e), False)

    def handling(self, argument):
        print("in protocol handling step 1")
        req = argument['op']
        func = self.switcher.get(int(req), "nada")
        print("in protocol handling step 2")
        return func(argument)