from BusinessLayer.Controllers.UserController import UserController
from BusinessLayer.Controllers.CategoryController import CategoryController
import Response

class Protocol:

    def __init__(self, conn):
        self.conn = conn
        self.user = None

        self.category_controller = CategoryController.getInstance()
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
                         21: self.get_liked_offers,
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
        # try:
        response = self.user_controller.unregister(argument['user_id'])
        # except Exception as e:
        #     out = Response.Response(None,str(e), False)
        #     return out
        # out = Response.Response(response, , True)
        return response


    def register(self, argument): #first_name, last_name , username , email , password, gender, date of birth
        response = self.user_controller.register(
                                      argument['first_name'],
                                      argument['last_name'],
                                      argument['user_name'],
                                      argument['email'],
                                      argument['password'],
                                      argument['birth_date'],
                                      argument['gender'])
        print("in register in protocol step 2")
        return response

    def log_in(self, argument): #user_name , password
        user = self.user_controller.log_in(argument['user_name'], argument['password'])
        self.user = user
        return 1

    def logout(self, argument): #user_id
        response = UserController.logout(argument['user_id'])
        return response


# -------------------------------------------------ADD------------------------------------------------------------------
    def add_active_buy_offer(self, argument):
        offer = self.categoryController.get_offer_by_offer_id(argument['offer_id'])
        response = self.user_controller.add_active_buy_offer(self.user.user_id, offer, argument['quantity'], argument['step'])
        if response.get_response != 'ACK':
            return response
        else:
            response = self.category_controller.add_buyer_to_offer(offer,
                                                                   self.user.user_id,
                                                                   argument['quantity'],
                                                                   argument['step'])
        return response

    def add_active_sell_offer(self, argument):
        response = self.category_controller.add_offer(argument['user_id'],
                                                      argument['product'],
                                                      argument['category_id'],
                                                      argument['sub_category_id'],
                                                      argument['status'],
                                                      argument['steps'],
                                                      argument['end_date'],
                                                      0)
        if response.get_response() != 'ACK':
            return response
        else:
            response = self.user_controller.add_active_sale_offer(response.get_data())
            if response != 'ACK':
                self.category_controller.remove_offer(argument['offer_id'], argument['category_id'],
                                                      argument['sub_category_id'])
        return response



    def add_liked_offer(self, argument):
        offer = self.category_controller.get_offer_by_offer_id(argument['offer_id'])
        response = self.user_controller.add_like_offer(self.user.user_id, offer)
        return response

    def add_address_details(self, argument): #user_id city street zip code floor apt
        response = self.user_controller.add_address_details(argument['user_id'],
                                                            argument['city'],
                                                            argument['street'],
                                                            argument['zip_code'],
                                                            argument['floor'],
                                                            argument['apt'])
        return response

    # def update_city(argument): user_id *
    # def update_street(argument): user_id *
    # def update_zip_code(argument): user_id *
    # def update_floor(argument): user_id *
    # def update_apt(argument): user_id *

    def add_payment_method(self, argument): # user_id , cc number, cc expire date, cvv, card_type, id
        response = self.user_controller.add_payment_method(argument['user_id'],
                                                           argument['credit_card_number'],
                                                           argument['expire_date'],
                                                           argument['cvv'],
                                                           argument['card_type'],
                                                           argument['id_number'])
        return response

    # def update_card_number(argument): user_id *
    # def update_expire_date(argument): user_id *
    # def update_cvv(argument): user_id *
    # def update_id_number user_id *
    # def update_card_type(argument): user_id *
    # -------------------------------------------------REMOVE------------------------------------------------------------------

    def remove_liked_offer(self, argument):
        response = self.user_controller.remove_liked_offer(self.user.user_id)
        return response

    def remove_active_sell_offer(self, argument):
        response = self.user_controller.remove_active_sale_offer(self.user.user_id, argument['offer_id'])
        if response.get_response() != 'ACK':
            return response
        else:
            response = self.category_controller.remove_offer(argument['offer_id'], argument['category_id'], argument['sub_category_id'])
        return response

    def remove_active_buy_offer(self, argument):
        response = self.user_controller.remove_active_sale_offer(self.user.user_id, argument['offer_id'])
        if response.get_response != 'ACK':
            return response
        else:
            response = self.category_controller.remove_buyer_from_offer(self.user.user_id, argument['offer_id'])
        return response

# -------------------------------------------------UPDATE----------------------------------------------------------------

    def update_first_name(self, argument): #user_id first name
        response = self.user_controller.update_first_name(argument['user_id'], argument['first_name'])
        return response

    def update_last_name(self, argument):#user_id last name
        response = self.user_controller.update_last_name(argument['user_id'], argument['last_name'])
        return response

    def update_username(self, argument): #user_id username
        response = self.user_controller.update_username(argument['user_id'], argument['user_name'])
        return response

    def update_email(self, argument): #user_id email
        response = self.user_controller.update_email(argument['user_id'], argument['email'])
        return response

    def update_password(self, argument): #user_id old new
        response = self.user_controller.update_password(argument['user_id'], argument['old_password'], argument['new_password'])
        return response

    def update_birth_date(self, argument): #user_id date of birth
        response = self.user_controller.update_birth_date(argument['user_id'], argument['birth_date'])
        return response

    def update_gender(self, argument): #user-id gender
        response = self.user_controller.gender(argument['user_id'], argument['gender'])
        return response

# -------------------------------------------------GET------------------------------------------------------------------

    def get_all_history_buy_offers(self, argument):
        response = self.user_controller.get_all_history_buy_offer(self.user.user_id)
        return response

    def get_all_history_sell_offers(self, argument):
        response = self.user_controller.get_all_history_sell_offer(self.user.user_id)
        return response

    def get_history_buy_offer(self, argument):
        pass

    def get_history_sell_offer(self, argument):
        pass

    def get_all_active_buy_offers(self, argument):
        response = self.user_controller.get_all_buy_offer(self.user.user_id)
        return response

    def get_all_active_sell_offers(self, argument):
        response = self.user_controller.get_all_sell_offer(self.user.user_id)
        return response

    def get_active_buy_offer(self, argument):
        response = self.user_controller.get_buy_offer(self.user.user_id, argument['offer_id'])
        return response

    def get_active_sell_offer(self, argument):
        response = self.user_controller.get_sell_offer(self.user.user_id, argument['offer_id'])
        return response

    def get_liked_offers(self, argument):
        response = self.user_controller.get_liked_offer(self.user.user_id, argument['offer_id'])
        return response

    def get_all_liked_offers(self, argument):
        response = self.user_controller.get_all_liked_offer(self.user.user_id)
        return response

# --------------------------------------------------categoryController-------------------------------------------------------

# -----------------------------------------------------ADD-------------------------------------------------------------------

    def add_category(self, argument):
        response = self.category_controller.add_category(argument['name'])
        return response

    def add_sub_category(self, argument):
        response = self.category_controller.add_sub_category(argument['name'], argument['category_id'])
        return response

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
        response = self.category_controller.update_sub_category_name(argument['category_id'],
                                                                     argument['sub_category_id'],
                                                                     argument['name'])
        return response

    #def update_current_step automatic
    
    def update_category_for_offer(self, argument):
        response = self.category_controller(argument['offer_id'],
                                            argument['category_id'],
                                            argument['sub_category_id'])
        return response

    def update_sub_category_for_offer(self, argument):
        response = self.category_controller.update_sub_category_for_offer(argument['offer_id'],
                                                                          argument['sub_category_id'])
        return response

    #def update_status automatic

    def update_end_date(self, argument):
        response = self.user_controller.update_end_date(argument['offer_id'], argument['end_date'])
        return response

    def update_start_date(self, argument):
        response = self.user_controller.update_start_date(argument['offer_id'], argument['start_date'])
        return response

    def update_step(self, argument):
        response = self.user_controller.update_step(argument['offer_id'], argument['step'])
        return response

    def update_product_name(self, argument):
        response = self.user_controller.update_product_name(argument['offer_id'], argument['name'])
        return response

    def update_product_company(self, argument):
        response = self.user_controller.update_product_company(argument['offer_id'], argument['company'])
        return response

    def update_product_color(self, argument):
        response = self.user_controller.update_product_color(argument['offer_id'], argument['color'])
        return response

    def update_product_size(self, argument):
        response = self.user_controller.update_size(argument['offer_id'], argument['size'])
        return response

    def update_product_description(self, argument):
        response = self.user_controller.update_product_description(argument['offer_id'], argument['description'])
        return response

    # -------------------------------------------------------GET---------------------------------------------------------------

    def get_offers_by_category(self, argument):
        response = self.category_controller.get_offers_by_category(argument['category_id'])
        return response

    def get_offers_by_subcategory(self, argument):
        response = self.category_controller.get_offers_by_sub_category(argument['category_id'], argument['sub_categoru_id'])
        return response

    def get_offers_by_product_name(self, argument):
        response = self.category_controller.get_offers_by_product_name(argument['name'])
        return response

    def get_offers_by_status(self, argument):
        response = self.category_controller.get_offers_by_status(argument['status'])

    def get_hot_deals(self, argument):
        response = self.category_controller.get_hot_deals()
        return response

    def remove_to_hot_deals(self, argument):
        response = self.category_controller.remove_from_hot_deals(argument['offer_id'])
        return response

    def handling(self, argument):
        print("in protocol handling step 1")
        req = argument['op']
        func = self.switcher.get(int(req), "nada")
        print("in protocol handling step 2")
        return func(argument)