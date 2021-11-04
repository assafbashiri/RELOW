import json

from Service.Object.OfferService import OfferService


class UserService():
    # SERVER
    def __init__(self, business_user):
        self.user_id = business_user.user_id
        self.active = business_user.get_active()
        self.seller = business_user.get_seller()
        # CheckValidity.checkValidityName(first_name)
        # CheckValidity.date.today() - self.birth_date.checkValidityName(last_name)
        # CheckValidity.checkValidityEmail(email)
        # CheckValidity.checkValidityPassword(password)
        # self.user_id = business_user.get_next_user_id()
        self.first_name = business_user.get_first_name()
        self.last_name = business_user.get_last_name()
        self.phone = business_user.get_phone()
        self.email = business_user.get_email()
        self.password = business_user.get_password()
        self.birth_date = json.dumps(business_user.get_birth_date(), indent=4, sort_keys=True, default=str)
        self.birth_date=self.birth_date[1:-1]
        bussiness_gender = business_user.get_gender()
        self.gender = str(bussiness_gender)
        self.gender = self.gender[7:len(self.gender)]


        # user address
        self.city = business_user.get_city()
        self.street = business_user.get_street()
        self.apartment_number = business_user.get_apartment_number()
        self.zip_code = business_user.get_zip_code()
        self.floor = business_user.get_floor()

        # payment method
        self.id_number = business_user.get_id_number()
        self.credit_card_number = business_user.get_card_number()
        self.credit_card_exp_date = business_user.get_credit_card_exp_date()
        self.cvv = business_user.get_cvv()
        self.card_type = business_user.get_card_type()

        self.history_buy_offers = []
        for index in business_user.history_buy_offers:
            offer = business_user.history_buy_offers[index]
            self.history_buy_offers.append(vars(OfferService(offer)))

        self.history_sell_offers = []
        for index in business_user.history_sale_offers:
            offer = business_user.history_sale_offers[index]
            self.history_sell_offers.append(vars(OfferService(offer)))

        self.liked_offers = []
        for index in business_user.liked_offers:
            offer = business_user.liked_offers[index]
            self.liked_offers.append(vars(OfferService(offer)))

        self.active_sell_offers = []
        for index in business_user.active_sale_offers:
            offer = business_user.active_sale_offers[index]
            self.active_sell_offers.append(vars(OfferService(offer)))

        self.active_buy_offers = []
        for index in business_user.active_buy_offers:
            offer = business_user.active_buy_offers[index]
            self.active_buy_offers.append(vars(OfferService(offer)))

    # -------------------------------------------USER SUBMISSION-----------------------------------------------------------
    def get_active(self):
        return self.active

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone

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

    def get_credit_card_exp_date(self):
        return self.credit_card_exp_date

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
        return self.history_sell_offers

    def get_liked_offers(self):
        return self.liked_offers

    def get_active_sale_offers(self):
        return self.active_sell_offers

    def get_active_buy_offers(self):
        return self.active_buy_offers
