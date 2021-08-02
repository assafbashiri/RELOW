from BussinesLayer import Controllers
from BussinesLayer.Controllers import UserController, CategoryController


class Protocol:
    from BussinesLayer import Controllers
    from BussinesLayer.Controllers import UserController, CategoryController
    def _init_(self):
        self.user = None
    #------------------------------------------------userController--------------------------------------------------------

    #-------------------------------------------------BASIC------------------------------------------------------------------
    def unregister(argument): #user_id
        response = UserController.unregister(argument['user_id'])
        return response
    def register(argument): #first_name, last_name , username , email , password, gender, date of birth
        response = UserController.register(argument['first_name'], argument['last_name'], argument['username'], argument['email'], argument['password'], argument['gender'], argument['date_of_birth'])
        return response
    def login(argument): #user_name , password
        response = UserController.login(argument['user_name'], argument['password'])
        return response
    def logout(argument): #user_id
        response = UserController.logout(argument['user_id'])
        return response


    #-------------------------------------------------ADD------------------------------------------------------------------

    def add_active_buy_offer(argument):
        pass
    def add_active_sell_offer(argument):
        pass
    def add_liked_offer(argument):
        pass
    def add_address_details(argument): #user_id city street zip code floor apt
        response = UserController.add_address_details(argument['user_id'], argument['city'], argument['street'], argument['zip_code'], argument['floor'], argument['apt'])
        return response
    # def update_city(argument): user_id *
    # def update_street(argument): user_id *
    # def update_zip_code(argument): user_id *
    # def update_floor(argument): user_id *
    # def update_apt(argument): user_id *
    def add_payment_method(argument): # user_id , cc number, cc expire date, cvv, card_type, id
        response = UserController.add_payment_method(argument['user_id'], argument['credit_card_number'], argument['expire_date'], argument['cvv'], argument['card_type'], argument['id_number'])
        return response
    # def update_card_number(argument): user_id *
    # def update_expire_date(argument): user_id *
    # def update_cvv(argument): user_id *
    # def update_id_number user_id *
    # def update_card_type(argument): user_id *
    #-------------------------------------------------REMOVE------------------------------------------------------------------
    def remove_liked_offer(argument):
        pass
    def remove_active_sell_offer(argument):
        pass
    def remove_active_buy_offer(argument):
        pass
    #-------------------------------------------------UPDATE------------------------------------------------------------------
    def update_first_name(argument): #user_id first name
        response = UserController.update_first_name(argument['user_id'], argument['first_name'])
        return response
    def update_last_name(argument):#user_id last name
        response = UserController.update_last_name(argument['user_id'], argument['last_name'])
        return response
    def update_username(argument): #user_id username
        response = UserController.update_username(argument['user_id'], argument['user_name'])
        return response
    def update_email(argument): #user_id email
        response = UserController.update_mail(argument['user_id'], argument['email'])
        return response
    def update_password(argument): #user_id old new
        response = UserController.update_password(argument['user_id'], argument['old_password'], argument['new_password'])
        return response
    def update_birth_date(argument): #user_id date of birth
        response = UserController.update_birth_date(argument['user_id'], argument['birth_date'])
        return response
    def update_gender(argument): #user-id gender
        response = UserController.gender(argument['user_id'], argument['gender'])
        return response
    #-------------------------------------------------GET------------------------------------------------------------------
    def get_all_history_buy_offers(argument):
        pass
    def get_all_history_sell_offers(argument):
        pass
    def get_history_buy_offer(argument):
        pass
    def get_history_sell_offer(argument):
        pass
    def get_all_active_buy_offers(argument):
        pass
    def get_all_active_sell_offers(argument):
        pass
    def get_active_buy_offer(argument):
        pass
    def get_active_sell_offer(argument):
        pass
    def get_liked_offers(argument):
        pass
    def get_all_liked_offers(argument):
        pass

    #--------------------------------------------------categoryController-------------------------------------------------------

    #-----------------------------------------------------ADD-------------------------------------------------------------------
    def add_category(argument):
        pass
    def add_aub_category(argument):
        pass
    def add_offer(argument):
        pass
    def add_photo(argument):
        pass
    def add_buyer_to_offer(argument):
        pass
    def add_to_hot_deals(argument):
        pass
    #------------------------------------------------REMOVE------------------------------------------------------------------
    def remove_category(argument):
        pass
    def remove_sub_category(argument):
        pass
    def remove_photo(argument):
        pass
    def remove_offer(argument):
        pass
    def remove_buyer_from_offer(argument):
        pass
    def remove_to_hot_deals(argument):
        pass
    #-------------------------------------------------------UPDATE----------------------------------------------------------------------
    def update_category_name(argument):
        pass
    def update_sub_category_name(argument):
        pass
    #def update_current_step automatic
    def update_category_for_offer(argument):
        pass
    def update_sub_category_for_offer(argument):
        pass
    #def update_status automatic

    def update_end_date(argument):
        pass
    def update_start_date(argument):
        pass
    def update_step(argument):
        pass
    def update_product_name(argument):
        pass
    def update_product_company(argument):
        pass
    def update_product_color(argument):
        pass
    def update_product_size(argument):
        pass
    def update_product_description(argument):
        pass
    #-------------------------------------------------------GET---------------------------------------------------------------
    def get_offers_by_category(argument):
        pass
    def get_offers_by_subcategory(argument):
        pass
    def get_offers_by_product_name(argument):
        pass
    def get_offers_by_status(argument):
        pass
    def get_hot_deals(argument):
        pass

    switcher = {1: register,
                2: unregister,
                3: login,
                4: logout,
                5: update_first_name,
                6: update_last_name,
                7: update_username,
                8: update_email,
                9: update_birth_date,
                10: update_gender,
                11: add_address_details,
                12: add_payment_method,
                13: get_all_history_buy_offers,
                14: get_all_history_sell_offers,
                15: get_history_buy_offer,
                16: get_history_sell_offer,
                17: get_all_active_buy_offers,
                18: get_all_active_sell_offers,
                19: get_active_buy_offer,
                20: get_active_sell_offer,
                21: get_liked_offers,
                22: get_all_liked_offers,
                23: add_active_buy_offer,
                24: add_active_sell_offer,
                25: add_liked_offer,
                26: remove_liked_offer,
                27: remove_active_sell_offer,
                28: remove_active_buy_offer,
                # for userController
                29: add_category,
                30: add_aub_category,
                31: add_offer,
                32: add_photo,
                33: remove_category,
                34: remove_sub_category,
                35: remove_photo,
                36: remove_offer,
                37: update_category_name,
                38: update_sub_category_name,
                39: update_current_step,
                40: update_category_for_offer,
                41: update_sub_category_for_offer,
                42: update_status,
                43: update_end_date,
                44: update_start_date,
                45: update_step,
                46: add_buyer_to_offer,
                47: remove_buyer_from_offer,
                48: update_product_name,
                49: update_product_company,
                50: update_product_color,
                51: update_product_size,
                52: update_product_description,
                53: get_offers_by_category,
                54: get_offers_by_subcategory,
                55: get_offers_by_product_name,
                56: get_offers_by_status,
                57: get_hot_deals,
                58: add_to_hot_deals,
                59: remove_to_hot_deals
                }

    def hendeling(self,argument):
        req = argument['op']
        func = switcher.get(req,"nothing")
        return func(argument)