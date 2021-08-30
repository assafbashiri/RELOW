from datetime import date, datetime
from BusinessLayer.Utils.Gender import Gender
from BusinessLayer.Object import Offer
from BusinessLayer.Object.UserAddress import UserAddress
from BusinessLayer.Object.UserPayment import UserPayment
from BusinessLayer.Utils import CheckValidity


class User():
    def __init__(self, next_user_id, first_name, last_name, user_name, email, password, birth_date, gender):
        # ---------- user submission
        self.active = True
        self.is_logged = False
        self.user_id = next_user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.gender = gender
        #self.age = datetime.today() - self.birth_date
        today = date.today()
        born =self.birth_date
        self.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))





        # ---------- user extra details
        self.address = UserAddress()
        self.payment = UserPayment()
        # ---------- user's offers lists
        self.history_buy_offers = {}
        self.history_sale_offers = {}
        self.liked_offers = {}
        self.active_sale_offers = {}
        self.active_buy_offers = {}

    def log_in(self):
        self.is_logged = True

    def logout(self):
        self.is_logged = False

    def set_address_details(self, user_address):
        self.address = user_address

    def set_card_details(self, user_payment):
        self.payment = user_payment

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name
        # update DB

    def set_user_name(self, user_name):
        self.user_name = user_name
        # update DB

    def set_password(self, password):
        self.password = password

    def set_date_of_birth(self, date_of_birth):
        self.birth_date = date_of_birth
        self.age = datetime.today() - self.birth_date

    def set_gender(self, gender):
        self.gender = Gender(int(gender))


    def set_email(self, email):
        self.email = email

    def set_city(self, city):
        self.address.set_city(city)

    def set_street(self, street):
        self.address.set_city(street)

    def set_apartment_number(self, apartment_number):
        self.address.set_city(apartment_number)

    def set_zip_code(self, zip_code):
        self.address.set_city(zip_code)

    def set_floor(self, floor):
        self.address.set_city(floor)

    def set_credit_card_number(self, credit_card_number):
        self.payment.set_credit_card_number(credit_card_number)

    def set_credit_card_exp_date(self, credit_card_exp_date):
        self.payment.set_credit_card_exp_date(credit_card_exp_date)

    def set_cvv(self, cvv):
        self.payment.set_cvv(cvv)

    def set_card_type(self, card_type):
        self.payment.set_card_type(card_type)

    def set_id(self, id_number):
        self.payment.set_id_number(id_number)


    def add_like_offer(self, liked_offer):
        self.liked_offers[liked_offer.offer_id] = liked_offer

    def remove_from_liked_offers(self, offer_id_to_remove):
        if offer_id_to_remove not in self.liked_offers.keys():
            return False
        self.liked_offers.pop(offer_id_to_remove, None)
        return True

    def add_active_sale_offer(self, offer_sold):
        self.active_sale_offers[offer_sold.offer_id] = offer_sold

    def add_active_buy_offer(self, offer_to_add):
        self.active_buy_offers[offer_to_add.offer_id] = offer_to_add

    def move_to_history_buyer(self, offer_to_move):
        if offer_to_move.offer_id not in self.active_buy_offers.keys():
            return False
        self.active_buy_offers.pop(offer_to_move.offer_id, None)
        self.add_to_history_buyer(offer_to_move)
        return True

    def move_to_history_seller(self, offer_to_move):
        if offer_to_move.offer_id not in self.active_sale_offers.keys():
            return False
        self.active_sale_offers.pop(offer_to_move.offer_id, None)
        self.add_to_history_seller(offer_to_move)

    def add_to_history_buyer(self, offer_to_add):
        if offer_to_add.offer_id in self.history_buy_offers:
            raise Exception("Offer Already Exist In History Buyer")
        self.history_buy_offers[offer_to_add.offer_id] = offer_to_add

    def add_to_history_seller(self, offer_to_add):
        if offer_to_add.offer_id in self.history_sale_offers:
            raise Exception("Offer Already Exist In History Buyer")
        self.history_sale_offers[offer_to_add.offer_id] = offer_to_add



    # -------------------- get

    def is_active_buyer(self):
        if len(self.active_buy_offers) == 0:
            return False
        return True

    def is_active_seller(self):
        if len(self.active_sale_offers) == 0:
            return False
        return True


    # -------------------------------------------USER SUBMISSION-----------------------------------------------------------
    def get_is_logged(self):
        return self.is_logged

    def get_user_id(self):
        return self.user_id

    def get_active(self):
        return self.active

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_name(self):
        return self.user_name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_birth_date(self):
        return self.birth_date

    def get_gender(self):
        return self.gender

        # -------------------------------------------USER ADDRESS-----------------------------------------------------------

    def get_city(self):
        return self.address.get_city()

    def get_street(self):
        return self.address.get_street()

    def get_apartment_number(self):
        return self.address.get_apartment_number()

    def get_zip_code(self):
        return self.address.get_zip_code()

    def get_floor(self):
        return self.address.get_floor()

        # -------------------------------------------USER PAYMENT-----------------------------------------------------------

    def get_card_number(self):
        return self.payment.get_card_number()

    def get_credit_card_exp_date(self):
        return self.payment.get_credit_card_exp_date()

    def get_cvv(self):
        return self.payment.get_cvv()

    def get_id_number(self):
        return self.payment.get_id_number()

    def get_card_type(self):
        return self.payment.get_card_type()

        # -------------------------------------------USER OFFERS-----------------------------------------------------------

    def get_history_buy_offers(self):
        ans = []
        ans.extend(self.history_buy_offers.values())
        return ans

    def get_history_sell_offers(self):
        ans = []
        ans.extend(self.history_sale_offers.values())
        return ans

    def get_liked_offers(self):
        ans = []
        ans.extend(self.liked_offers.values())
        return ans

    def get_active_sale_offers(self):
        ans = []
        ans.extend(self.active_sale_offers.values())
        return ans

    def get_active_buy_offers(self):
        ans = []
        ans.extend(self.active_buy_offers.values())
        return ans

    def get_active_buy_offer(self, offer_id):
        if offer_id not in self.active_buy_offers.keys():
            return None
        return self.active_buy_offers[offer_id]

    def get_active_sale_offer(self, offer_id):
        if offer_id not in self.active_sale_offers.keys():
            return None
        return self.active_sale_offers[offer_id]

    def get_liked_offer(self, offer_id):
        if offer_id not in self.liked_offers.keys():
            return None
        return self.liked_offers[offer_id]

    def get_history_buy_offer(self, offer_id):
        if offer_id not in self.history_buy_offers.keys():
            return None
        return self.history_buy_offers[offer_id]

    def get_history_sale_offer(self, offer_id):
        if offer_id not in self.history_sale_offers.keys():
            return None
        return self.history_sale_offers[offer_id]