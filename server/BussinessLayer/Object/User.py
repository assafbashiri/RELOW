from datetime import date
from BussinessLayer.Object import Offer
from BussinessLayer.Utils import CheckValidity


class User():
    def __init__(self, next_user_id, first_name, last_name, user_name, email, password, birth_date, gender):
        self.active = True
        self.is_logged = False
        #CheckValidity.checkValidityName(first_name)
        #CheckValidity.date.today() - self.birth_date.checkValidityName(last_name)
        #CheckValidity.checkValidityEmail(email)
        #CheckValidity.checkValidityPassword(password)
        self.user_id = next_user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.gender = gender


        # user address
        self.city = None
        self.street = None
        self.apartment_number = None
        self.zip_code = None
        self.floor = None

        # payment method
        self.id_number = None
        self.credit_card_number = None
        self.credit_card_experation_date = None
        self.cvv = None
        self.card_type = None

        self.history_buy_offers = {}
        self.history_sale_offers = {}
        self.liked_offers = {}
        self.active_sale_offers = {}
        self.active_buy_offers = {} # with quantity and step


    def log_in(self):
        self.is_logged = True

    def log_out(self):
        self.is_logged = False
        print("log out.. done")

    def add_address_details(self, city, street, apartment_number, zip_code, floor):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        # tool bar to choose the address
        self.city = city
        self.street = street
        self.apartment_number = apartment_number
        self.zip_code = zip_code
        self.floor = floor

    def set_card_details(self, id, credit_card_number, credit_card_experation_date, cvv, card_type):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        self.id_number = id
        self.credit_card_number = credit_card_number
        self.credit_card_experation_date = credit_card_experation_date
        self.cvv = cvv
        self.card_type = card_type

    def add_to_history_purches(self, offer_to_add):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        # check if the offer valid
        self.history_buy_offers.add(offer_to_add.offer_id, offer_to_add)

    def add_to_liked_offers(self, liked_offer):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        # check if the offer valid
        self.liked_offers.add(liked_offer.offer_id, liked_offer)

    def remove_from_liked_offers(self, offer_to_remove):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        if offer_to_remove not in self.liked_offers:
            raise Exception("offer didnt exist in 'Liked Offers'")
        self.liked_offers.remove(offer_to_remove.offer_id)

    def add_to_item_sold(self, offer_sold):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        # check if the offer valid
        self.active_sale_offers.add(offer_sold.offer_id, offer_sold)

    def add_to_active_offers(self, offer_to_add):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        # check if the offer valid
        self.active_buy_offers.add(offer_to_add.offer_id, offer_to_add)

    def remove_from_active_offers(self, offer_to_remove):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        if offer_to_remove not in self.active_buy_offers:
            raise Exception("offer didnt exist in 'Active Offers'")
        self.active_buy_offers.remove(offer_to_remove.offer_id)

    def set_first_name(self, first_name):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        #CheckValidity.checkValidityName(first_name) - to fix !
        self.first_name = first_name

    def set_last_name(self, last_name):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityName(last_name)
        self.last_name = last_name
        # update DB

    def set_user_name(self, user_name):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityName(user_name)
        self.user_name = user_name
        # update DB

    def set_password(self, password):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityPassword(password)
        self.password = password

    def set_date_of_birth(self, date_of_birth):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        # tool bar to choose date of birth
        self.checkValidityDateOfBirth(date_of_birth)
        self.date_of_birth = date_of_birth
        self.age = date.today() - self.date_of_birth

    def set_gender(self, gender):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        # tool bar to choose gender
        self.gender = gender

    def set_age(self, age):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityAge(age)
        self.age = age

    def set_email(self, email):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityEmail(email)
        self.email = email

    def set_city(self, city):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityCity(city)
        self.city = city

    def set_street(self, street):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityStreet(street)
        self.street = street

    def set_apartment_number(self, apartment_number):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityNumber(apartment_number)
        self.apartment_number = apartment_number

    def set_zip_code(self, zip_code):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityZipCode(zip_code)
        self.zip_code = zip_code

    def set_floor(self, floor):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityNumber(floor)
        self.floor = floor

    def set_credit_card_number(self, credit_card_number):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityCreditCardNumber(credit_card_number)
        self.credit_card_number = credit_card_number

    def set_credit_card_experation_date(self, credit_card_experation_date):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityExpDate(credit_card_experation_date)
        self.credit_card_experation_date = credit_card_experation_date

    def set_cvv(self, cvv):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        #CheckValidity.checkValidityCvv(cvv)
        self.cvv = cvv

    def set_card_type(self, card_type):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityCardType(card_type)
        self.card_type = card_type

    def set_id(self, id_number):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityId(id_number)
        self.id_number = id_number



    # -------------------- get
        # -------------------------------------------USER SUBMISSION-----------------------------------------------------------
        def get_is_logged(self):
            return self.is_logged

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
            return self.city

        def get_street(self):
            return self.street

        def get_apartment_number(self):
            return self.apartment_number

        def get_zip_code(self):
            return self.zip_code

        def get_floor(self):
            return self.floor

        # -------------------------------------------USER PAYMENT-----------------------------------------------------------

        def get_card_number(self):
            return self.credit_card_number

        def get_credit_card_expiration_date(self):
            return self.credit_card_experation_date

        def get_cvv(self):
            return self.cvv

        def get_id_number(self):
            return self.id_number

        def get_card_type(self):
            return self.card_type

        # -------------------------------------------USER OFFERS-----------------------------------------------------------

        def get_history_buy_offers(self):
            return self.history_buy_offers

        def get_history_sell_offer(self):
            return self.history_sale_offers

        def get_liked_offers(self):
            return self.liked_offers

        def get_active_sale_offers(self):
            return self.active_sale_offers

        def get_active_buy_offers(self):
            return self.active_buy_offers
