from datetime import date
from bussines.Utils import CheckValidity

class User():
    def __init__(self,next_user_id,first_name, last_name,user_name, email, password):
        self.active = False
        self.isLogged = False
        CheckValidity.checkValidityName(first_name)
        CheckValidity.checkValidityName(last_name)
        CheckValidity.checkValidityEmail(email)
        CheckValidity.checkValidityPassword(password)
        self.user_id = next_user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password

        self.date_of_birth = None
        self.gender = None
        self.age = None

        # user address
        self.city = None
        self.street = None
        self.apartmentNumber = None

        # payment method
        self.id = None
        self.credit_car_number = None
        self.credit_card_experation_date=None
        self.cvv = None
        self.card_type = None

        self.historyPurches = None
        self.likedOffers = None
        self.itemSold= None
        self.activeOffers = None

    def log_in(self, user_name, password):
        self.isLogged = True

    def log_out(self, user_id):
        self.isLogged = False

    def add_address_details(self, city, street, apartment_number):
        self.city = city
        self.street = street
        self.apartmentNumber = apartment_number

    def set_date_of_birth(self, date_of_birth):
        self.checkValidityDateOfBirth(date_of_birth)
        self.date_of_birth = date_of_birth
        self.age = date.today() - self.date_of_birth

    def set_gender(self, gender):
        self.gender = gender

    def set_card_details(self,id,  credit_card_number,credit_card_experation_date, cvv, card_type):
        self.id = id
        self.credit_car_number = credit_card_number
        self.credit_card_experation_date = credit_card_experation_date
        self.cvv = cvv
        self.card_type = card_type

    def add_to_history_purches(self, offer_to_add):
        # check if the offer valid
        self.historyPurches.add(offer_to_add)

    def add_to_liked_offers(self, offer):
        # check if the offer valid
        self.likedOffers.add(offer)

    def remove_from_liked_offers(self, offer_to_remove):
        if not offer_to_remove in self.likedOffers:
            raise Exception ("offer didnt exist in 'Liked Offers'")
        self.likedOffers.remove(offer_to_remove)

    def add_to_item_sold(self, offer):
        # check if the offer valid
        self.itemSold.add(offer)

    def add_to_active_offers(self, offer_to_add):
        # check if the offer valid
        self.activeOffers.add(offer_to_add)

    def remove_from_active_offers(self, offer_to_remove):
        if not offer_to_remove in self.activeOffers:
            raise Exception ("offer didnt exist in 'Active Offers'")
        self.activeOffers.remove(offer_to_remove)

    def set_first_name(self,first_name):
        CheckValidity.checkValidityName(first_name)
        self.first_name = first_name
        # update DB

    def set_last_name(self,last_name):
        CheckValidity.checkValidityName(last_name)
        self.last_name = last_name
        # update DB

    def set_user_name(self,user_name):
        CheckValidity.checkValidityName(user_name)
        self.user_name= user_name
        # update DB

