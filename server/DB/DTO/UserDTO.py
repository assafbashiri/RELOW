from server.BusinessLayer.Object.User import User


class UserDTO:
    def __init__(self, user_id, first_name, last_name, user_name, email, password, birth_date, gender):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.gender = gender
        self.active = True
        self.is_logged = False

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

    def __init__(self, user):
        user = User()
        self.user_id = user.get_user_id()
        self.first_name = user.get_first_name()
        self.last_name = user.get_last_name()
        self.user_name = user.get_user_name()
        self.email = user.get_email()
        self.password = user.get_password()
        self.birth_date = user.get_birth_date()
        self.gender = user.get_gender()
        self.active = user.get_active()
        self.is_logged = user.get_is_logged()

        # user address
        self.city = user.get_city()
        self.street = user.get_street()
        self.apartment_number = user.get_apartment_number()
        self.zip_code = user.get_zip_code()
        self.floor = user.get_floor()

        # payment method
<<<<<<< HEAD
        self.id_number = user.payment.id_number
        self.credit_card_number = user.payment.credit_card_number
        self.credit_card_expiration_date = user.payment.credit_card_exp_date
        self.cvv = user.payment.cvv
        self.card_type = user.payment.card_type
=======
        self.id_number = user.get_id_number()
        self.credit_card_number = user.get_card_number()
        self.credit_card_exp_date = user.get_credit_card_exp_date()
        self.cvv = user.get_cvv()
        self.card_type = user.get_card_type()
>>>>>>> f234e919ea03dfd333c657f9b74b83beeb56921e


