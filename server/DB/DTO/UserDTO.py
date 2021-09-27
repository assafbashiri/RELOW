from BusinessLayer.Object.User import User


class UserDTO:
    def __init__(self, user):
        self.user_id = user.get_user_id()
        self.first_name = user.get_first_name()
        self.last_name = user.get_last_name()
        self.user_name = user.get_user_name()
        self.email = user.get_email()
        self.password = user.get_password()
        self.birth_date = user.get_birth_date()
        self.gender = user.get_gender()
        self.active = user.get_active()

        # user address
        self.city = user.get_city()
        self.street = user.get_street()
        self.apartment_number = user.get_apartment_number()
        self.zip_code = user.get_zip_code()
        self.floor = user.get_floor()

        # payment method
        self.id_number = user.get_id_number()
        self.credit_card_number = user.get_card_number()
        self.credit_card_exp_date = user.get_credit_card_exp_date()
        self.cvv = user.get_cvv()
        self.card_type = user.get_card_type()