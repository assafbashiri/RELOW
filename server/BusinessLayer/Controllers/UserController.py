import smtplib
import ssl
from datetime import datetime

from BusinessLayer.Utils import CheckValidity
from BusinessLayer.Object.User import User

from DB.DAO.OfferDAO import OfferDAO
from DB.DAO.UsersDAO import UsersDAO
from DB.DTO.OfferDTO import OfferDTO
from DB.DTO.UserDTO import UserDTO

from DB.DTO.ProductDTO import ProductDTO

from BusinessLayer.Object.Purchase import Purchase

from BusinessLayer.Object.Offer import Offer
from BusinessLayer.Object.Product import Product
from BusinessLayer.Object.UserAddress import UserAddress
from BusinessLayer.Object.UserPayment import UserPayment
from BusinessLayer.Utils import OfferStatus

from BusinessLayer.Utils.OfferStatus import OfferStatus

from BusinessLayer.Utils.CheckValidity import checkValidity
from BusinessLayer.Utils.Gender import Gender

from BusinessLayer.emailHandler import emailHandler

from BusinessLayer.Utils.Utils import Utils


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
            self.users_dao = UsersDAO(conn)
            self.user_id = self.users_dao.load_user_id()
            self.offers_dao = OfferDAO(conn)
            self.usersDictionary = {}
            self.check = checkValidity()
            self.emailHandler = emailHandler()

    def getme(self):
        print('return singelton')
        return self

    def guest_register(self):
        user = User(self.user_id, None, None, None, None, None, None, Gender.male, False)
        userDTO = UserDTO(user)
        self.usersDictionary[user.user_id] = user
        self.users_dao.insert_guest(userDTO)
        self.user_id += 1
        return user

    def guest_login(self, guest_id):
        guest = self.usersDictionary[guest_id]
        return {'user': guest}

    def delete_guest(self, guest_id):
        self.usersDictionary.pop(guest_id)
        self.users_dao.delete_guest(guest_id)

    def merge_register(self, user_id, first_name, last_name, phone, email, password, birth_date, gender):
        if gender not in Gender._value2member_map_:
            raise Exception("bad gender")
        gender_to_add = Gender(gender)
        self.check.check_register(email, phone, self.usersDictionary)
        liked_offers = self.usersDictionary[user_id].liked_offers
        user = User(user_id, first_name, last_name, phone, email, password, birth_date, gender_to_add, False)
        user.set_liked_offers(liked_offers)
        userDTO = UserDTO(user)
        self.usersDictionary[user_id] = user
        self.users_dao.update(userDTO)
        self.user_id += 1
        msg = "welcome to Relow, your confirm code is: " + str(user.user_id)
        message = """\
        Subject: welcome to Relow

        """ + msg
        self.emailHandler.sendemail(email, message)
        return user

    def send_email(self):
        email = "moskoga02@gmail.com"
        msg = "welcome to Relow, your confirm code is: " + "5555"
        message = """\
        Subject: welcome to Relow

        """ + msg
        self.emailHandler.sendemail(email, message)

    def register(self, first_name, last_name, phone, email, password, birth_date, gender):
        if gender not in Gender._value2member_map_:
            raise Exception("bad gender")
        gender_to_add = Gender(gender)
        self.check.check_register(email, phone, self.usersDictionary)
        user = User(self.user_id, first_name, last_name, phone, email, password, birth_date, gender_to_add, False)
        userDTO = UserDTO(user)
        self.usersDictionary[user.user_id] = user
        self.users_dao.insert(userDTO)
        self.user_id += 1
        # send email
        msg = "welcome to Relow, your confirm code is: " + str(user.user_id)
        message = """\
        Subject: welcome to Relow

        """ + msg
        self.emailHandler.sendemail(email, message)
        return user

    def unregister(self, user_id):
        user = self.usersDictionary.get(user_id)
        self.check.check_unregister(user)
        self.logout(user_id)
        self.usersDictionary[user_id].active = False
        self.users_dao.unregister(user_id)

    def complete_register(self, user_id):
        self.usersDictionary[user_id].active = True
        self.users_dao.complete_register(user_id)
        self.log_in(self.usersDictionary[user_id].email, self.usersDictionary[user_id].password)

    def become_a_seller(self, user_id):
        self.usersDictionary[user_id].seller = True
        self.users_dao.become_a_seller(user_id)

    def log_in(self, email, password):
        user = self.get_user_by_email(email)
        if user is None:
            raise Exception("there is no such an email address in the system")
        password_of_user = user.get_password()
        if password_of_user != password:
            raise Exception("incorrect Password")
        if user.active == 0:
            raise Exception("user is not active")
        return user

    def logout(self, user_id):
        user = self.check_user_state(user_id)
        # user.logout()
        # self.users_dao.update(UserDTO(user))

    def forgot_password(self, email):
        user = self.get_user_by_email(email)
        if user is None:
            raise Exception("there is no such an email address in the system")
        new_password = Utils.generate_password(self)
        user.set_password(new_password)
        self.users_dao.update(UserDTO(user))
        # send email
        msg = "your new password is: " + str(new_password)
        message = """\
        Subject: your password has changed
        """ + msg
        self.emailHandler.sendemail(email, message)

    def add_payment_method(self, user_id, credit_card_number, credit_card_exp_date, cvv, card_type, id):
        user_to_add = self.check_user_state(user_id)
        payment_method = UserPayment()
        payment_method.add_card_details(id, credit_card_number, credit_card_exp_date, cvv, card_type)
        user_to_add.set_card_details(payment_method)
        self.users_dao.update(UserDTO(user_to_add))

    def add_address_details(self, user_id, city, street, zip_code, floor, apartment_number):
        user_to_add = self.check_user_state(user_id)
        address = UserAddress()
        address.add_address_details(city, street, apartment_number, zip_code, floor)
        user_to_add.set_address_details(address)
        self.users_dao.update(UserDTO(user_to_add))
        return user_to_add

    def update_first_name(self, user_id, new_first_name):
        if new_first_name == "":
            return
        else:
            user = self.check_user_state(user_id)
            user.set_first_name(new_first_name)
            self.users_dao.update(UserDTO(user))

    def update_last_name(self, user_id, new_last_name):
        if new_last_name == "":
            return
        else:
            user = self.check_user_state(user_id)
            user.set_last_name(new_last_name)
            self.users_dao.update(UserDTO(user))

    def update_phone(self, user_id, phone):
        user = self.check_user_state(user_id)
        user.set_phone(phone)
        self.users_dao.update(UserDTO(user))

    def update_password(self, user_id, old_password, new_password):
        user = self.check_user_state(user_id)
        if not old_password == self.get_password_by_email(user.email):
            raise Exception("incorrect old password")
        user.set_password(new_password)
        self.users_dao.update(UserDTO(user))

    def update_email(self, user_id, new_email):
        if new_email == "":
            return
        else:
            user = self.check_user_state(user_id)
            user.set_email(new_email)
            self.users_dao.update(UserDTO(user))

    def update_birth_date(self, user_id, new_birthdate):
        user = self.check_user_state(user_id)
        date = datetime.strptime(new_birthdate, "%Y-%m-%d")
        user.set_date_of_birth(date)
        self.users_dao.update(UserDTO(user))

    def update_gender(self, user_id, new_gender):
        user = self.check_user_state(user_id)
        user.set_gender(new_gender)
        self.users_dao.update(UserDTO(user))

    def update_city(self, user_id, new_city):
        user = self.check_user_state(user_id)
        user.set_city(new_city)
        self.users_dao.update(UserDTO(user))

    def update_street(self, user_id, new_street):
        user = self.check_user_state(user_id)
        user.set_street(new_street)
        self.users_dao.update(UserDTO(user))

    def update_zip_code(self, user_id, new_zip_code):
        user = self.check_user_state(user_id)
        user.set_zip_code(new_zip_code)
        self.users_dao.update(UserDTO(user))

    def update_floor(self, user_id, new_floor):
        user = self.check_user_state(user_id)
        user.set_floor(new_floor)
        self.users_dao.update(UserDTO(user))

    def update_apartment(self, user_id, new_apartmentNumber):
        user = self.check_user_state(user_id)
        user.set_apartment_number(new_apartmentNumber)
        self.users_dao.update(UserDTO(user))

    def update_card_number(self, user_id, new_card_number):
        user = self.check_user_state(user_id)
        user.set_card_number(new_card_number)
        self.users_dao.update(UserDTO(user))

    def update_exp_date(self, user_id, new_expire_date):
        user = self.check_user_state(user_id)
        user.set_exp_date(new_expire_date)
        self.users_dao.update(UserDTO(user))

    def update_cvv(self, user_id, new_cvv):
        user = self.check_user_state(user_id)
        user.set_cvv(new_cvv)
        self.users_dao.update(UserDTO(user))

    def update_card_type(self, user_id, new_card_type):
        user = self.check_user_state(user_id)
        user.set_card_type(new_card_type)
        self.users_dao.update(UserDTO(user))

    def update_id(self, user_id, new_id):
        user = self.check_user_state(user_id)
        user.set_id(new_id)
        self.users_dao.update(UserDTO(user))

    # -------------------------------- update offers

    def update_end_date(self, user_id, offer_id, new_end_date):
        offer = self.check_offer_state(user_id, offer_id)
        offer.set_end_date(new_end_date)
        self.offers_dao.update(OfferDTO(offer))

    def update_start_date(self, user_id, offer_id, new_start_date):
        offer = self.check_offer_state(user_id, offer_id)
        offer.set_start_date(new_start_date)
        self.offers_dao.update(OfferDTO(offer))

    def update_step_for_user(self, user_id, offer_id, new_step):
        offer = self.check_offer_state(user_id, offer_id)
        offer.set_current_step(new_step)
        self.offers_dao.update(OfferDTO(offer))

    def update_product_name(self, user_id, offer_id, name):
        offer = self.check_offer_state(user_id, offer_id)
        offer.product.set_name(name)
        self.offers_dao.update(OfferDTO(offer))

    def update_product_company(self, user_id, offer_id, company):
        offer = self.check_offer_state(user_id, offer_id)
        offer.product.set_company(company)
        self.offers_dao.update(OfferDTO(offer))

    def update_product_colors(self, user_id, offer_id, colors):
        offer = self.check_offer_state(user_id, offer_id)
        colors_list = offer.product.build_list_from_string(colors)
        offer.product.set_colors(colors_list)
        self.offers_dao.update(OfferDTO(offer))

    def update_product_size(self, user_id, offer_id, size):
        offer = self.check_offer_state(user_id, offer_id)
        offer.product.set_size(size)
        self.offers_dao.update(OfferDTO(offer))

    def update_product_sizes(self, user_id, offer_id, sizes):
        offer = self.check_offer_state(user_id, offer_id)
        sizes_list = offer.product.build_list_from_string(sizes)
        offer.product.set_sizes(sizes_list)
        self.offers_dao.update(OfferDTO(offer))

    def update_product_description(self, user_id, offer_id, description):
        offer = self.check_offer_state(user_id, offer_id)
        offer.product.set_description(description)
        self.offers_dao.update(OfferDTO(offer))

    # ------------------------------- offers

    def add_active_sale_offer(self, offer):
        seller = self.check_user_state(offer.user_id)
        seller.add_active_sale_offer(offer)
        offerDTO = OfferDTO(offer)
        productDTO = offerDTO.product
        self.offers_dao.insert(offerDTO, productDTO)
        msg = "thank you for selling "
        message = """\
        Subject: you add offer successfully

        """ + msg
        self.emailHandler.sendemail(seller.get_email(), message)

    # add a buyer into an offer
    def add_active_buy_offer(self, user_id, offer, quantity, step_id, color, size, address):
        if user_id == offer.get_user_id():
            raise Exception("seller cant buy is own product")
        if offer.is_a_buyer(user_id):
            raise Exception("the buyer is already subscribe to this offer")
        buyer = self.check_user_state(user_id)
        # add the quantity and the step to the active_buy_offers
        purchase = Purchase(quantity, step_id, user_id, color, size, address)
        offer.add_buyer(user_id, purchase)
        buyer.add_active_buy_offer(offer)
        offer_DTO = OfferDTO(offer)
        self.offers_dao.add_active_buy_offer(offer_DTO, user_id, quantity, step_id, color, size, address)
        self.update_curr_step(offer)
        msg = "thank you for buying "
        message = """\
        Subject: you joined successfully to offer

        """ + msg
        self.emailHandler.sendemail(buyer.get_email(), message)

    def add_like_offer(self, user_id, offer):
        user_temp = self.get_user_by_id(user_id)
        user_temp.add_like_offer(offer)
        self.offers_dao.add_like_offer(user_id, offer.offer_id)

    def remove_like_offer(self, user_id, offer_id_to_remove):
        user_temp = self.get_user_by_id(user_id)
        flag = user_temp.remove_from_liked_offers(offer_id_to_remove)
        if not flag:
            raise Exception("offer didnt exist in 'Liked Offers'")
        self.offers_dao.remove_like_offer(user_id, offer_id_to_remove)

    def remove_active_sale_offer(self, offer):
        seller_user_id = offer.get_user_id()
        seller = self.check_user_state(seller_user_id)
        if not seller.move_to_history_seller(offer):
            raise Exception("offer is not in the seller's sale offers")
        current_buyers = offer.get_current_buyers()
        user_ids = []
        user_ids.extend(current_buyers.keys())
        offer.set_status(OfferStatus.CANCELED_BY_SELLER)
        for i in range(0, len(user_ids)):
            self.remove_active_buy_offer(user_ids[i], offer, offer.get_status())
        # this function above update the DB
        self.offers_dao.delete_active_offer(offer.offer_id)
        self.offers_dao.insert_to_history_offers(OfferDTO(offer))

    def remove_active_buy_offer(self, user_id, offer_id):
        user = self.check_user_state(user_id)
        offer = user.get_active_buy_offer(offer_id)
        if not offer.remove_buyer(user_id):
            raise Exception("buyer not in the offer's buyers'")
        if not user.move_to_history_buyer(offer):
            raise Exception("offer didnt exist in user's active buy offers")
        self.offers_dao.delete_buy_offer(user_id, offer.get_offer_id())
        self.offers_dao.insert_to_history_buyers(user_id, offer_id, offer.get_status(), offer.get_current_step())
        self.update_curr_step(offer)
        return offer

    def update_active_buy_offer(self, user_id, offer, quantity, step, color, size, address):
        self.check_user_state(user_id)
        if not offer.update_active_buy_offer(user_id, quantity, step,color,size,address):
            raise Exception("User is not a buyer in this offer")
        self.offers_dao.update_active_buy_offer(user_id, offer.offer_id, quantity, step, color, size, address)
        self.update_curr_step(offer)

    def get_active_buy_offers(self, user_id):
        user_temp = self.check_user_state(user_id)
        return user_temp.get_active_buy_offers()

    def get_active_sale_offers(self, user_id):
        user_temp = self.check_user_state(user_id)
        return user_temp.get_active_sale_offers()

    def get_history_buy_offers(self, user_id):
        user_temp = self.check_user_state(user_id)
        return user_temp.get_history_buy_offers()

    def get_history_sell_offers(self, user_id):
        user_temp = self.check_user_state(user_id)
        return user_temp.get_history_sell_offers()

    def get_liked_offers(self, user_id):
        user_temp = self.get_user_by_id(user_id)
        return user_temp.get_liked_offers()

    def get_active_buy_offer(self, user_id, offer_id):
        user = self.check_user_state(user_id)
        offer = user.get_active_buy_offer(offer_id)
        if offer is None:
            raise Exception("Offer Does Not Exist in user's active buy offers")
        return offer

    def get_active_sale_offer(self, user_id, offer_id):
        user = self.check_user_state(user_id)
        offer = user.get_active_sell_offer(offer_id)
        if offer is None:
            raise Exception("Offer Does Not Exist in user's active sale offers")
        return offer

    def get_liked_offer(self, user_id, offer_id):
        user = self.check_user_state(user_id)
        offer = user.get_liked_offer(offer_id)
        if offer is None:
            raise Exception("Offer Does Not Exist in user's liked offers")
        return offer

    def get_history_buy_offer(self, user_id, offer_id):
        user = self.check_user_state(user_id)
        offer = user.get_history_buy_offer(offer_id)
        if offer is None:
            raise Exception("Offer Does Not Exist in user's history buy offers")
        return offer

    def get_history_sale_offer(self, user_id, offer_id):
        user = self.check_user_state(user_id)
        offer = user.get_history_sale_offer(offer_id)
        if offer is None:
            raise Exception("Offer Does Not Exist in user's history sale offers")
        return offer

    # ----------------------------------------------------------------------------------------------------------
    def move_all_expired_to_history(self, expired_offers):  # expired_offers - regular list
        # move all expired offers
        for curr_offer in expired_offers:
            for user_id in self.usersDictionary:
                try:
                    self.remove_like_offer(user_id, curr_offer.offer_id)
                except Exception as e:
                    pass
            seller = self.check_user_state(curr_offer.user_id)
            curr_offer.check_exp_status()
            curr_offer.set_hot_deals(False)
            if not seller.move_to_history_seller(curr_offer):
                raise Exception("offer is not in the seller's sale offers")
            current_buyers = curr_offer.get_current_buyers()
            for user_id in current_buyers.keys():
                curr_buyer = self.check_user_state(user_id)
                if not curr_buyer.move_to_history_buyer(curr_offer):
                    raise Exception("offer is not in the buyer's offers")
                self.offers_dao.delete_buy_offer(user_id, curr_offer.get_offer_id())
                self.offers_dao.insert_to_history_buyers(user_id, curr_offer.get_offer_id(),
                                                         curr_offer.get_status(),
                                                         curr_offer.get_current_step())
            self.offers_dao.delete_active_offer(curr_offer.offer_id)
            self.offers_dao.insert_to_history_offers(OfferDTO(curr_offer))

    # -------------------------- private functions -------------------------------------------------------------

    # def exist_user_name1(self, user_name):
    #     user_ids = self.usersDictionary.keys()
    #     for curr_user_id in user_ids:
    #         if user_name == self.usersDictionary.get(curr_user_id).user_name:
    #             return True
    #     return False

    def exist_user_id(self, user_id):
        if user_id in self.usersDictionary.keys():
            return True
        return False

    def get_password_by_email(self, email):
        user = self.get_user_by_email(email)
        if user is None:
            return None
        return user.password

    # def get_user_by_user_name(self, user_name):
    #     user_ids = self.usersDictionary.keys()
    #     for curr_user_id in user_ids:
    #         if user_name == self.usersDictionary.get(curr_user_id).user_name:
    #             return self.usersDictionary.get(curr_user_id)
    #     return None

    def get_user_by_email(self, email):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            us = self.usersDictionary[curr_user_id]
            if email == us.email:
                return us
        return None

    def get_user_id_by_email(self, email):
        user = self.get_user_by_email(email)
        if user is None:
            raise Exception("no such an email")
        return user.user_id

    def get_user_by_id(self, user_id):
        return self.usersDictionary[user_id]

    def exist_offer_id_in_user(self, user_id, offer_id):
        user = self.usersDictionary[user_id]
        if offer_id in user.active_sale_offers.keys():
            return True
        return False

    def update_curr_step(self, offer):
        offer.update_step()
        offerDTO = OfferDTO(offer)
        self.offers_dao.update(offerDTO)

    def load_users(self, offers, history_offers):
        users_submission_db = self.users_dao.load_users_sub()
        for user in users_submission_db:
            if user[6] is not None:
                date = datetime.strptime(user[6], "%Y-%m-%d %H:%M:%S")
            gender_to_add = Gender(int(user[7]))
            user_temp = User(user[0], user[1], user[2], user[3], user[4], user[5], date, gender_to_add,user[9])
            user_temp.active = user[8]
            self.usersDictionary[user[0]] = user_temp

        users_payment_db = self.users_dao.load_users_payment()
        for pay in users_payment_db:
            pay_temp = UserPayment()
            pay_temp.add_card_details(pay[1], pay[2], pay[3], pay[4], pay[5])
            self.usersDictionary[pay[0]].set_card_details(pay_temp)

        users_address_db = self.users_dao.load_users_address()
        for adr in users_address_db:
            adr_temp = UserAddress()
            adr_temp.add_address_details(adr[1], adr[2], adr[5], adr[3], adr[4])
            self.usersDictionary[adr[0]].set_address_details(adr_temp)

        # add loading from users extra details
        # ----------------- users details done --------------------------------
        # loading offers lists for each user

        buyers_in_offer_per_buyer_db = self.offers_dao.load_buyers_in_offers()
        liked_offers_from_db = self.offers_dao.load_liked_offers()

        history_offers_db = self.offers_dao.load_history_offers()
        history_buyers_db = self.offers_dao.load_history_buyers()

        for user_id in self.usersDictionary.keys():
            # active sell offers
            user = self.usersDictionary[user_id]
            for offer_id in offers.keys():
                offer = offers[offer_id]
                if offer.user_id == user_id:
                    user.add_active_sale_offer(offer)
            # active buy offers - can change with the offers
            for buyerInOffer in buyers_in_offer_per_buyer_db:
                if user_id == buyerInOffer[1]:
                    user.add_active_buy_offer(offers[buyerInOffer[0]])
            # history seller
            for history_offer in history_offers_db:
                if user_id == history_offer[1]:
                    user.add_to_history_seller(history_offers[history_offer[0]])
            # history buyer
            for history_buyer in history_buyers_db:
                if user_id == history_buyer[0]:
                    user.add_to_history_buyer(history_offers[history_buyer[1]])
            # liked offers
            for like_offer in liked_offers_from_db:
                if like_offer[1] == user_id:
                    user.add_like_offer(offers[like_offer[0]])

    def check_user_state(self, user_id):
        if not self.exist_user_id(user_id):
            raise Exception("User Does Not Exist")
        user = self.get_user_by_id(user_id)
        if user.active == 0:
            raise Exception("user is not active")
        return user

    def check_offer_state(self, user_id, offer_id):
        user = self.check_user_state(user_id)
        if not (self.exist_offer_id_in_user(user_id, offer_id)):
            raise Exception("Offer does not belong to this user")
        offer = user.active_sale_offers[offer_id]
        return offer
