from datetime import date
from BussinesLayer.Objects import Offer
from BussinesLayer.Utils import CheckValidity


class User():
    def __init__(self, next_user_id, first_name, last_name, user_name, email, password, gender, date_of_birth):
        self.active = True
        self.is_logged = False
        CheckValidity.checkValidityName(first_name)
        CheckValidity.date.today() - self.date_of_birthcheckValidityName(last_name)
        CheckValidity.checkValidityEmail(email)
        CheckValidity.checkValidityPassword(password)
        self.user_id = next_user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.age = date.today() - self.date_of_birth

        # user address
        self.city = None
        self.street = None
        self.apartment_number = None
        self.zip_code = None
        self.floor = None

        # payment method
        self.id = None
        self.credit_card_number = None
        self.credit_card_experation_date = None
        self.cvv = None
        self.card_type = None

        self.history_buy_offers = None
        self.history_sale_offers = None
        self.liked_offers = None
        self.active_sale_offers = None
        self.active_buy_offers = None

    def log_in(self):
        self.is_logged = True

    def log_out(self):
        self.is_logged = False

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
        self.id = id
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
        CheckValidity.checkValidityName(first_name)
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
        CheckValidity.checkValidityCvv(cvv)
        self.cvv = cvv

    def set_card_type(self, card_type):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityCardType(card_type)
        self.card_type = card_type

    def set_id(self, id):
        if self.is_logged is False:
            raise Exception("User Is Not Logged In")
        CheckValidity.checkValidityId(id)
        self.id = id
