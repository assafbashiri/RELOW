from BussinessLayer.Controllers.UserController import  UserController
from BussinessLayer.Controllers.CategoryController import CategoryController


class Protocol:

    def __init__(self, conn):
        self.conn = conn
        self.user = None
        self.category_controller = CategoryController(conn)
        self.user_controller = UserController(conn)
        self.switcher =  {1: self.register,
                          2: self.unregister,
                          3: self.log_in,
                    # 4: self.logout(argument),
                    # 5: self.update_first_name(argument),
                    # 6: self.update_last_name(argument),
                    # 7: self.update_username(argument),
                    # 8: self.update_email(argument),
                    # 9: self.update_birth_date(argument),
                    # 10: self.update_gender(argument),
                    # 11: self.add_address_details(argument),
                    # 12: self.add_payment_method(argument),
                    # 13: self.get_all_history_buy_offers(argument),
                    # 14: self.get_all_history_sell_offers(argument),
                    # 15: self.get_history_buy_offer(argument),
                    # 16: self.get_history_sell_offer(argument),
                    # 17: self.get_all_active_buy_offers(argument),
                    # 18: self.get_all_active_sell_offers(argument),
                    # 19: self.get_active_buy_offer(argument),
                    # 20: self.get_active_sell_offer(argument),
                    # 21: self.get_liked_offers(argument),
                    # 22: self.get_all_liked_offers(argument),
                    # 23: self.add_active_buy_offer(argument),
                    # 24: self.add_active_sell_offer(argument),
                    # 25: self.add_liked_offer(argument),
                    # 26: self.remove_liked_offer(argument),
                    # 27: self.remove_active_sell_offer(argument),
                    # 28: self.remove_active_buy_offer(argument),
                    # # for userController
                    # 29: self.add_category(argument),
                    # 30: self.add_aub_category(argument),
                    # 31: self.add_offer(argument),
                    # 32: self.add_photo(argument),
                    # 33: self.remove_category(argument),
                    # 34: self.remove_sub_category(argument),
                    # 35: self.remove_photo(argument),
                    # 36: self.remove_offer(argument),
                    # 37: self.update_category_name(argument),
                    # 38: self.update_sub_category_name(argument),
                    # # 39: update_current_step,
                    # 40: self.update_category_for_offer(argument),
                    # 41: self.update_sub_category_for_offer(argument),
                    # 42: 'update_status',
                    # 43: self.update_end_date(argument),
                    # 44: self.update_start_date(argument),
                    # 45: self.update_step(argument),
                    # 46: self.add_buyer_to_offer(argument),
                    # 47: self.remove_buyer_from_offer(argument),
                    # 48: self.update_product_name(argument),
                    # 49: self.update_product_company(argument),
                    # 50: self.update_product_color(argument),
                    # 51: self.update_product_size(argument),
                    # 52: self.update_product_description(argument),
                    # 53: self.get_offers_by_category(argument),
                    # 54: self.get_offers_by_subcategory(argument),
                    # 55: self.get_offers_by_product_name(argument),
                    # 56: self.get_offers_by_status(argument),
                    # 57: self.get_hot_deals(argument),
                    # 58: self.add_to_hot_deals(argument),
                    # 59: self.remove_to_hot_deals(argument)
                    }

    # ------------------------------------------------userController----------------------------------------------------

    # -------------------------------------------------BASIC------------------------------------------------------------

    def unregister(self, argument): #user_id
        response = self.user_controller.unregister(argument['user_id'])
        return response

    def register(self, argument): #first_name, last_name , username , email , password, gender, date of birth
        self.user_controller.register(
                                      argument['first_name'],
                                      argument['last_name'],
                                      argument['user_name'],
                                      argument['email'],
                                      argument['password'],
                                      argument['birth_date'],
                                      argument['gender'])
        print("in register in protocol step 2")
        return {'op':1}

    def log_in(self, argument): #user_name , password
        user = self.user_controller.log_in(argument['user_name'], argument['password'])
        self.user = user
        return 1

    def logout(self, argument): #user_id
        response = UserController.logout(argument['user_id'])
        return response


    #-------------------------------------------------ADD------------------------------------------------------------------

    def add_active_buy_offer(self, argument):
        pass

    def add_active_sell_offer(self, argument):
        pass

    def add_liked_offer(self, argument):
        pass

    def add_address_details(self, argument): #user_id city street zip code floor apt
        response = UserController.add_address_details(argument['user_id'], argument['city'], argument['street'], argument['zip_code'], argument['floor'], argument['apt'])
        return response

    # def update_city(argument): user_id *
    # def update_street(argument): user_id *
    # def update_zip_code(argument): user_id *
    # def update_floor(argument): user_id *
    # def update_apt(argument): user_id *

    def add_payment_method(self, argument): # user_id , cc number, cc expire date, cvv, card_type, id
        response = UserController.add_payment_method(argument['user_id'], argument['credit_card_number'], argument['expire_date'], argument['cvv'], argument['card_type'], argument['id_number'])
        return response

    # def update_card_number(argument): user_id *
    # def update_expire_date(argument): user_id *
    # def update_cvv(argument): user_id *
    # def update_id_number user_id *
    # def update_card_type(argument): user_id *
    # -------------------------------------------------REMOVE------------------------------------------------------------------

    def remove_liked_offer(self, argument):
        pass

    def remove_active_sell_offer(self, argument):
        pass

    def remove_active_buy_offer(self, argument):
        pass

    #-------------------------------------------------UPDATE------------------------------------------------------------------

    def update_first_name(self, argument): #user_id first name
        response = UserController.update_first_name(argument['user_id'], argument['first_name'])
        return response

    def update_last_name(self, argument):#user_id last name
        response = self.UserController.update_last_name(argument['user_id'], argument['last_name'])
        return response

    def update_username(self, argument): #user_id username
        response = UserController.update_username(argument['user_id'], argument['user_name'])
        return response

    def update_email(self, argument): #user_id email
        response = UserController.update_mail(argument['user_id'], argument['email'])
        return response
    def update_password(self, argument): #user_id old new
        response = UserController.update_password(argument['user_id'], argument['old_password'], argument['new_password'])
        return response
    def update_birth_date(self, argument): #user_id date of birth
        response = UserController.update_birth_date(argument['user_id'], argument['birth_date'])
        return response
    def update_gender(self, argument): #user-id gender
        response = UserController.gender(argument['user_id'], argument['gender'])
        return response
    #-------------------------------------------------GET------------------------------------------------------------------
    def get_all_history_buy_offers(self, argument):
        pass
    def get_all_history_sell_offers(self, argument):
        pass
    def get_history_buy_offer(self, argument):
        pass
    def get_history_sell_offer(self, argument):
        pass
    def get_all_active_buy_offers(self, argument):
        pass
    def get_all_active_sell_offers(self, argument):
        pass
    def get_active_buy_offer(self, argument):
        pass
    def get_active_sell_offer(self, argument):
        pass
    def get_liked_offers(self, argument):
        pass
    def get_all_liked_offers(self, argument):
        pass

    # --------------------------------------------------categoryController-------------------------------------------------------

    # -----------------------------------------------------ADD-------------------------------------------------------------------

    def add_category(self, argument):
        pass

    def add_aub_category(self, argument):
        pass

    def add_offer(self, argument):
        pass

    def add_photo(self, argument):
        pass

    def add_buyer_to_offer(self, argument):
        pass

    def add_to_hot_deals(self, argument):
        pass

    #------------------------------------------------REMOVE------------------------------------------------------------------

    def remove_category(self, argument):
        pass

    def remove_sub_category(self, argument):
        pass

    def remove_photo(self, argument):
        pass

    def remove_offer(self, argument):
        pass

    def remove_buyer_from_offer(self, argument):
        pass

    def remove_to_hot_deals(self, argument):
        pass

    # -------------------------------------------------------UPDATE----------------------------------------------------------------------

    def update_category_name(self, argument):
        pass

    def update_sub_category_name(self, argument):
        pass

    #def update_current_step automatic
    
    def update_category_for_offer(self, argument):
        pass

    def update_sub_category_for_offer(self, argument):
        pass

    #def update_status automatic

    def update_end_date(self, argument):
        pass

    def update_start_date(self, argument):
        pass

    def update_step(self, argument):
        pass

    def update_product_name(self, argument):
        pass

    def update_product_company(self, argument):
        pass

    def update_product_color(self, argument):
        pass

    def update_product_size(self, argument):
        pass

    def update_product_description(self, argument):
        pass

    # -------------------------------------------------------GET---------------------------------------------------------------

    def get_offers_by_category(self, argument):
        pass

    def get_offers_by_subcategory(self, argument):
        pass

    def get_offers_by_product_name(self, argument):
        pass

    def get_offers_by_status(self, argument):
        pass

    def get_hot_deals(self, argument):
        pass

    def handling(self, argument):
        print("in protocol handling step 1")
        req = argument['op']
        func = self.switcher.get(int(req), "nada")
        print("in protocol handling step 2")
        return func(argument)