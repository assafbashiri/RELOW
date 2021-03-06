from assets.Service.Object.OfferService import OfferService
from assets.Response import Response


class UserService():
    # CLIENT
    def __init__(self, user_id, first_name, last_name, phone, email, password, birth_date, gender, seller, city, street,
                 apt, zip, floor,
                 id_number, credit_card_number, credit_exp, cvv, card_type,
                 history_buy_offers, history_sale_offers, liked_offers, active_sale_offers, active_buy_offers):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.birth_date = birth_date
        # gender - 0 / 1
        if gender is None:
            self.gender = None
        else:
            self.gender = gender


        self.seller = seller

        # user address
        self.city = city
        self.street = street
        self.apartment_number = apt
        self.zip_code = zip
        self.floor = floor

        # payment method
        self.id_number = id_number
        self.credit_card_number = credit_card_number
        self.credit_card_exp_date = credit_exp
        self.cvv = cvv
        self.card_type = card_type

        self.history_buy_offers = []
        for offer in history_buy_offers:
            offer_service = self.build_offer(offer)
            self.history_buy_offers.append(offer_service)

        self.history_sale_offers = []
        for offer in history_sale_offers:
            offer_service = self.build_offer(offer)
            self.history_sale_offers.append(offer_service)

        self.liked_offers = []
        for offer in liked_offers:
            self.liked_offers.append(offer['offer_id'])

        self.active_sale_offers = []
        for offer in active_sale_offers:
            offer_service = self.build_offer(offer)
            self.active_sale_offers.append(offer_service)

        self.active_buy_offers = []
        for offer in active_buy_offers:
            offer_service = self.build_offer(offer)
            self.active_buy_offers.append(offer_service)

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

    def get_address(self):
        if self.city is None:
            return Response(False, 'you need to add address first', False)
        if self.street is None:
            return Response(False, 'you need to add address first', False)
        if self.floor is None:
            return Response(False, 'you need to add address first', False)
        if self.apartment_number is None:
            return Response(False, 'you need to add address first', False)
        if self.zip_code is None:
            return Response(False, 'you need to add address first', False)
        adr_str = str(self.city) + ' ' + str(self.street) + ' ' + str(self.floor) + ' ' + str(self.apartment_number) +' ' + str(self.zip_code)
        return Response(adr_str, 'you have an address', True)

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
        return self.history_sale_offers

    def get_liked_offers(self):
        return self.liked_offers

    def get_active_sale_offers(self):
        return self.active_sale_offers

    def get_active_buy_offers(self):
        return self.active_buy_offers

    def set_password(self, password):
        self.password = password

    def build_offer(self, x):
        offer_temp = OfferService(x['offer_id'], x['user_id'], x['product'], x['category_id'], x['sub_category_id'],
                                  x['status'],
                                  x['steps'], x['start_date'], x['end_date'], x['current_step'],
                                  x['current_buyers'])
        return offer_temp

    # -------------------------------------------------------

    def is_a_buyer(self, offer_id):
        for offer in self.active_buy_offers:
            if offer_id == offer.offer_id:
                return True
        return False

    def is_a_liker(self, offer_id):
        for offer in self.liked_offers:
            if offer_id == offer:
                return True
        return False
