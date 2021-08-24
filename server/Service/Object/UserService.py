

class UserService():
    def __init__(self, first_name, last_name, user_name, email, password, birth_date, gender):
        self.active = True
        self.is_logged = False
        #CheckValidity.checkValidityName(first_name)
        #CheckValidity.date.today() - self.birth_date.checkValidityName(last_name)
        #CheckValidity.checkValidityEmail(email)
        #CheckValidity.checkValidityPassword(password)
        # self.user_id = next_user_id
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
        self.credit_card_exp_date = None
        self.cvv = None
        self.card_type = None

        self.history_buy_offers = None
        self.history_sale_offers = None
        self.liked_offers = None
        self.active_sale_offers = None
        self.active_buy_offers = None

    def __init__(self, business_user):
        self.active = business_user.get_active()
        self.is_logged = business_user.get_is_logged()
        #CheckValidity.checkValidityName(first_name)
        #CheckValidity.date.today() - self.birth_date.checkValidityName(last_name)
        #CheckValidity.checkValidityEmail(email)
        #CheckValidity.checkValidityPassword(password)
        # self.user_id = business_user.get_next_user_id()
        self.first_name = business_user.get_first_name()
        self.last_name = business_user.get_last_name()
        self.user_name = business_user.get_user_name()
        self.email = business_user.get_email()
        self.password = business_user.get_password()
        self.birth_date = business_user.get_birth_date()
        self.gender = business_user.get_gender()


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

        self.history_buy_offers = None
        self.history_sell_offers = None
        self.liked_offers = business_user.get_liked_offers()
        self.active_sell_offers = business_user.get_active_sale_offers()
        self.active_buy_offers = business_user.get_active_buy_offers()


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
