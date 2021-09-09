from Service.Object.OfferService import OfferService


class UserService():
    # CLIENT
    def __init__(self, user_id, first_name, last_name, user_name, email, password, birth_date, gender, city, street, apt, zip, floor,
                 id_number, credit_card_number, credit_exp, cvv, card_type,
                 history_buy_offers, history_sale_offers, liked_offers, active_sale_offers, active_buy_offers):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        # gender - 0 / 1
        self.gender = gender

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
            offer_service = self.build_offer(offer)
            self.liked_offers.append(offer_service)

        self.active_sale_offers = []
        for offer in active_sale_offers:
            offer_service = self.build_offer(offer)
            self.active_sale_offers.append(offer_service)

        self.active_buy_offers = []
        for offer in active_buy_offers:
            offer_service = self.build_offer(offer)
            self.active_buy_offers.append(offer_service)


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
            if offer_id == offer.offer_id:
                return True
        return False
