from BusinessLayer.Utils import CheckValidity
from BusinessLayer.Object.User import User

from DB.DAO.OfferDAO import OfferDAO
from DB.DAO.ProductDAO import ProductDAO
from DB.DAO.UsersDAO import UsersDAO
from DB.DTO.OfferDTO import OfferDTO
from DB.DTO.UserDTO import UserDTO

from DB.DTO.ProductDTO import ProductDTO

from BusinessLayer.Object import Purchase

from BusinessLayer.Utils.OfferStatus import OfferStatus


class UserController:
    __instance = None

    def getInstance():
        """ Static access method. """
        if UserController.__instance == None:
            UserController()
        return UserController.__instance

    def __init__(self, conn):
        if UserController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserController.__instance = self
            self.user_id = 1
            self.users_dao = UsersDAO(conn)
            self.offers_dao = OfferDAO(conn)
            self.products_dao = ProductDAO(conn)
            self.usersDictionary = {}

    def getme(self):
        print('return singelton')
        return self

    def register(self, first_name, last_name, user_name, email, password, birth_date, gender):
        user = User(self.user_id, first_name, last_name, user_name, email, password, birth_date, gender)
        userDTO = UserDTO(self.user_id, user.first_name, user.last_name, user.user_name, user.email, user.password,
                          user.birth_date, gender)
        self.usersDictionary[user.user_id] = user
        self.users_dao.insert(userDTO)
        self.user_id += 1
        self.log_in(user_name, password)
        return user
    def unregister(self, user_id):
        user = self.usersDictionary.get(user_id)
        if user is None:
            raise Exception("User does not exist")
        if user.active is not True:
            raise Exception("user is not active")
        if user.is_logged is not True:
            raise Exception("user is not logged")
        # check if the user is in offer
        self.log_out(user_id)
        self.usersDictionary.get(user_id).active = False  # check
        self.users_dao.unregister(user_id)
        # self.usersDictionary.get(user_id).key = None
        # dont sure that we really want to delete the user from DB
        # self.usersDictionary.remove(user_id)
    def log_in(self, user_name, password):
        if not self.exist_user_name1(user_name):
            raise Exception("User Name Not Exist")
        # user name exist in the dictionary
        password_of_user = self.get_password_by_user_name(user_name)
        if password_of_user != password:
            raise Exception("Illegal Password")
        user_to_log_in = self.get_user_by_user_name(user_name)
        user_to_log_in.log_in()  # check this line
        self.users_dao.log_in(user_to_log_in.user_id)
        return user_to_log_in
    def log_out(self, user_id):
        if user_id not in self.usersDictionary.keys():
            raise Exception("User Does Not Exist")
        self.usersDictionary[user_id].log_out()
        self.users_dao.log_out(user_id)
    def add_payment_method(self, user_id, credit_card_number, credit_card_experation_date, cvv, card_type, id):
        user_to_add = self.get_user_by_id(user_id)
        user_to_add.set_card_details(id, credit_card_number, credit_card_experation_date, cvv, card_type)
        self.users_dao.add_payment_method(user_id, credit_card_number, credit_card_experation_date, cvv, card_type, id)
    def add_address(self, user_id, city, street, zip_code, floor, apartmentNumber):
        user_to_add = self.get_user_by_id(user_id)
        user_to_add.add_address_details(city, street, apartmentNumber, zip_code, floor)
        self.users_dao.add_address(user_id, city, street, zip_code, floor, apartmentNumber)
        # update users_submission
    def update_first_name(self, user_id, firstname):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_first_name(firstname)
        self.users_dao.updateFirstname(user_id, firstname)
    def update_last_name(self, user_id, lastname):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_last_name(lastname)
        self.users_dao.updateLastname(user_id, lastname)
    def update_user_name(self, user_id, username):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_user_name(username)
        self.users_dao.updateUsername(user_id, username)
    def update_password(self, user_id, old_password, new_password):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        if not old_password == self.get_password_by_user_name(temp.user_name):
            raise Exception("incorrect old password")
        temp.set_password(new_password)
        self.users_dao.updatePassword(user_id, new_password)
    def update_email(self, user_id, new_email):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_email(new_email)
        self.users_dao.updateEmail(user_id, new_email)
    def update_birth_date(self, user_id, new_birthdate):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_date_of_birth(new_birthdate)
        self.users_dao.updateBirthdate(user_id, new_birthdate)
    def update_gender(self, user_id, new_gender):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_gender(new_gender)
        self.users_dao.updateGender(user_id, new_gender)
    def update_city(self, user_id, new_city):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_city(new_city)
        self.users_dao.updateCity(user_id, new_city)
    def update_street(self, user_id, new_street):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_street(new_street)
        self.users_dao.updateStreet(user_id, new_street)
    def update_zip_code(self, user_id, new_zip_code):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_zip_code(new_zip_code)
        self.users_dao.updateZipcode(user_id, new_zip_code)
    def update_floor(self, user_id, new_floor):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_floor(new_floor)
        self.users_dao.updateFloor(user_id, new_floor)
    def update_apartment(self, user_id, new_apartmentNumber):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_apartment_number(new_apartmentNumber)
        self.users_dao.updateApartmentNumber(user_id, new_apartmentNumber)
    def update_card_number(self, user_id, new_card_number):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_card_number(new_card_number)
        self.users_dao.updateCardNumber(user_id, new_card_number)
    def update_exp_date(self, user_id, new_expire_date):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_exp_date(new_expire_date)
        self.users_dao.updateExpireDate(user_id, new_expire_date)
    def update_cvv(self, user_id, new_cvv):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_cvv(new_cvv)
        self.users_dao.updateCvv(user_id, new_cvv)
    def update_card_type(self, user_id, new_card_type):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_card_type(new_card_type)
        self.users_dao.updateCard_type(user_id, new_card_type)
    def update_id(self, user_id, new_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_id(new_id)
        self.users_dao.updateId(user_id, new_id)

        # -------------------------------- update offers
    def update_end_date(self, user_id, offer_id, new_end_date):
            if not (self.exist_user_id(user_id)):
                raise Exception("User does not exist")
            if not (self.exist_offer_id_in_user(user_id, offer_id)):
                raise Exception("Offer does not exist")
            offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
            offer_temp.set_end_date(new_end_date)
            self.offers_dao.update_end_date(offer_id, new_end_date)
    def update_start_date(self, user_id, offer_id, new_start_date):
            if not (self.exist_user_id(user_id)):
                raise Exception("User does not exist")
            if not (self.exist_offer_id_in_user(user_id, offer_id)):
                raise Exception("Offer does not exist")
            offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
            offer_temp.set_start_date(new_start_date)
            self.offers_dao.update_start_date(offer_id, new_start_date)
    def update_step(self, user_id, offer_id, step):
            if not (self.exist_user_id(user_id)):
                raise Exception("User does not exist")
            if not (self.exist_offer_id_in_user(user_id, offer_id)):
                raise Exception("Offer does not exist")
            offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
            offer_temp.set_step(step)
            self.offers_dao.update_step(offer_id, step)
    def update_status(self, user_id, offer_id, status):
            if not (self.exist_user_id(user_id)):
                raise Exception("User does not exist")
            if not (self.exist_offer_id_in_user(user_id, offer_id)):
                raise Exception("Offer does not exist")
            offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
            offer_temp.set_status(status)
            self.offers_dao.update_status(offer_id, status)
    def update_product_name(self, user_id, offer_id, name):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        if not (self.exist_offer_id_in_user(user_id, offer_id)):
            raise Exception("Offer does not exist")
        offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
        offer_temp.product.set_name(name)
        self.offers_dao.update_product_name(offer_id, name)
    def update_product_company(self, user_id, offer_id, company):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        if not (self.exist_offer_id_in_user(user_id, offer_id)):
            raise Exception("Offer does not exist")
        offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
        offer_temp.product.set_company(company)
        self.offers_dao.update_product_company(offer_id, company)
    def update_product_color(self, user_id, offer_id, color):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        if not (self.exist_offer_id_in_user(user_id, offer_id)):
            raise Exception("Offer does not exist")
        offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
        offer_temp.product.set_color(color)
        self.offers_dao.update_product_color(offer_id, color)
    def update_product_size(self, user_id, offer_id, size):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        if not (self.exist_offer_id_in_user(user_id, offer_id)):
            raise Exception("Offer does not exist")
        offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
        offer_temp.product.set_size(size)
        self.offers_dao.update_product_size(offer_id, size)
    def update_product_description(self, user_id, offer_id, description):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        if not (self.exist_offer_id_in_user(user_id, offer_id)):
            raise Exception("Offer does not exist")
        offer_temp = self.usersDictionary[user_id].active_sale_offers[offer_id]
        offer_temp.product.set_description(description)
        self.offers_dao.update_product_description(offer_id, description)

    # ------------------------------- offers

    def add_active_sale_offer(self, offer):
        if not (self.exist_user_id(offer.user_id)):
            raise Exception("User does not exist")
        saler = self.usersDictionary.get(offer.user_id)
        saler.active_sale_offers[offer.offer_id] = offer
        offerDTO = OfferDTO(offer)
        productDTO = ProductDTO(offer.product)
        self.offers_dao.insert(offerDTO, productDTO)
    # add a buyer into an offer
    def add_active_buy_offer(self, user_id, offer, quantity, step):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        buyer = self.usersDictionary.get(user_id)
        # add the quantity and the step to the active_buy_offers
        purchase = Purchase.Purchase(quantity, step)
        offer.add_buyer(user_id, purchase)
        buyer.active_buy_offers[offer.offer_id] = offer
        offerDTO = OfferDTO(offer)
        self.offers_dao.add_active_buy_offer(offerDTO, user_id, quantity, step)
        self.update_curr_step(offer)
        
        
        # update buyers_in_offer_total :::
        # offer.updateStep()
    def add_like_offer(self, user_id, offer):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        user_temp.liked_offers[offer.offer_id] = offer
        self.offers_dao.add_like_offer(user_id, offer.offer_id)
    def remove_like_offer(self, user_id, offer):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        user_temp.liked_offers.pop(offer.offer_id, None)
        self.offers_dao.remove_like_offer(user_id, offer.offer_id)
    def remove_active_sale_offer(self,  offer):
        user_id = offer.get_user_id()
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user = self.usersDictionary[user_id]
        user.move_to_history_seller(offer)
        current_buyers = offer.get_current_buyers()
        user_ids = []
        user_ids.extend(current_buyers.keys())
        for i in range(0, len(user_ids)):
            self.remove_active_buy_offer(user_ids[i], offer)

            # this function above update the DB
        offer.set_status(OfferStatus.OfferStatus.EXPIRED_UNCOMPLETED)
        self.offers_dao.update(OfferDTO(offer))
        self.offers_dao.insert_to_history_sellers(offer.get_user_id(), offer.get_offer_id(), offer.get_status(), offer.get_current_step())
    def remove_active_buy_offer(self, user_id, offer):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        offer.remove_buyer(user_id)
        user = self.usersDictionary[user_id]
        user.move_to_history_buyer(offer)
        self.offers_dao.delete_buy_offer(user_id, offer.get_offer_id())
        self.offers_dao.insert_to_history_buyers(offer.get_user_id(), offer.get_offer_id(), OfferStatus.OfferStatus.EXPIRED_UNCOMPLETED,
                                                 offer.get_current_step())
        self.update_curr_step(offer)

    def update_active_buy_offer(self, user_id, offer, quantity, step):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        offer.update_active_buy_offer(user_id, quantity, step)
        self.offers_dao.update_active_buy_offer(user_id,offer.offer_id, quantity, step)
        self.update_curr_step(offer)
    def get_active_buy_offers(self,user_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        return user_temp.active_buy_offers
    def get_active_sell_offers(self, user_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        return user_temp.active_sale_offers
    def get_history_buy_offers(self,user_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        return user_temp.history_buy_offers
    def get_history_sell_offers(self, user_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        return user_temp.history_sale_offers
    def get_liked_offers(self, user_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        return user_temp.liked_offers
    def get_active_buy_offer(self, user_id, offer_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        if offer_id not in user_temp.active_buy_offers.keys():
            raise Exception("offer does not exist")
        return user_temp.active_buy_offers[offer_id]
    def get_active_sell_offer(self, user_id, offer_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        if offer_id not in user_temp.active_sale_offers.keys():
            raise Exception("offer does not exist")
        return user_temp.active_sale_offers[offer_id]
    def get_liked_offer(self, user_id, offer_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        if offer_id not in user_temp.liked_offers.keys():
            raise Exception("offer does not exist")
        return user_temp.liked_offers[offer_id]
    def get_history_buy_offer(self, user_id, offer_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        if offer_id not in user_temp.history_buy_offers.keys():
            raise Exception("offer does not exist")
        return user_temp.history_buy_offers[offer_id]
    def get_history_sell_offer(self, user_id, offer_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user_temp = self.usersDictionary[user_id]
        if offer_id not in user_temp.history_sale_offers.keys():
            raise Exception("offer does not exist")
        return user_temp.history_sale_offers[offer_id]
    #----------------------------------------------------------------------------------------------------------
    def move_all_expired_to_history(self, expired_offers):#expired_offers - regular list
        # move all expired offers
        for curr_offer in expired_offers:
            self.usersDictionary[curr_offer.user_id].move_to_history_seller(curr_offer)
            current_buyers = curr_offer.get_current_buyers()
            curr_offer.set_status(OfferStatus.OfferStatus.EXPIRED_COMPLETED)
            for user_id in current_buyers.keys():
                if not (self.exist_user_id(user_id)):
                    raise Exception("User does not exist")
                self.usersDictionary[user_id].move_to_history_buyer(curr_offer)
                self.offers_dao.delete_buy_offer(user_id, curr_offer.get_offer_id())
                self.offers_dao.insert_to_history_buyers(curr_offer.get_user_id(), curr_offer.get_offer_id(),
                                                         curr_offer.get_status(),
                                                         curr_offer.get_current_step())
            self.offers_dao.update(OfferDTO(curr_offer))
            self.offers_dao.insert_to_history_sellers(curr_offer.get_user_id(), curr_offer.get_offer_id(), curr_offer.get_status(),
                                                      curr_offer.get_current_step())


    # maybe delete those 2 functions
    def add_to_history_buyer(self,user_id, offer_to_add):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user = self.usersDictionary[user_id]
        user.add_to_history_buyer(offer_to_add)

    def add_to_history_seller(self, user_id, offer_to_add):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        user = self.usersDictionary[user_id]
        user.add_to_history_seller(offer_to_add)
    #----------------------------------------------------------------------------------------------------------
        # -------------------------- private functions -- to implement!!!

    def exist_user_name1(self, user_name):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return True
        return False
    def exist_user_id(self, user_id):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_id == curr_user_id:
                return True
        return False
    def get_password_by_user_name(self, user_name):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return self.usersDictionary.get(curr_user_id).password
        return None
    def get_user_by_user_name(self, user_name):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return self.usersDictionary.get(curr_user_id)
        return None
    def get_user_by_id(self, user_id):
        print(self.usersDictionary.__len__())
        return self.usersDictionary[user_id]

    def exist_offer_id_in_user(self, user_id, offer_id):
        user = self.usersDictionary[user_id]
        if offer_id in user.active_sale_offers:
            return True
        return False

    def update_curr_step(self, offer):
        offer.update_step()
        offerDTO = OfferDTO(offer)
        self.offers_dao.update(offerDTO)


