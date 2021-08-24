
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
        self.credit_card_expiration_date = None
        self.cvv = None
        self.card_type = None

    def __init__(self, user):
        self.user_id = user.user_id
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.user_name = user.user_name
        self.email = user.email
        self.password = user.password
        self.birth_date = user.birth_date
        self.gender = user.gender
        self.active = user.active
        self.is_logged = user.is_logged

        # user address
        self.city = user.address.city
        self.street = user.address.street
        self.apartment_number = user.address.apartment_number
        self.zip_code = user.address.zip_code
        self.floor = user.address.floor

        # payment method
        self.id_number = user.payment.id_number
        self.credit_card_number = user.payment.credit_card_number
        self.credit_card_expiration_date = user.payment.credit_card_exp_date
        self.cvv = user.payment.cvv
        self.card_type = user.payment.card_type


