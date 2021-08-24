from client.Backend_controller import Backend_controller
from client.Service.Object.UserService import UserService
from client.main import Struct


class accountWindow:
    def __init__(self, controller):
        self.controller = controller
        self.user = UserService()

    def update_first_name(self):
        first_name = ""
        ans = self.controller.update_first_name(first_name)
        res = Struct(**ans)

    def update_last_name(self):
        last_name = ""
        ans = self.controller.update_last_name(last_name)
        res = Struct(**ans)

    def update_user_name(self):
        user_name = ""
        ans = self.controller.update_user_name(user_name)
        res = Struct(**ans)

    def update_birth_date(self):
        birth_date = ""
        ans = self.controller.update_birth_date(birth_date)
        res = Struct(**ans)

    def update_email(self):
        email = ""
        ans = self.controller.update_email(email)
        res = Struct(**ans)

    def update_password(self):
        old_password = ""
        new_password = ""
        ans = self.controller.update_password(old_password, new_password)
        res = Struct(**ans)

    def update_gender(self):
        gender = ""
        ans = self.controller.update_gender(gender)
        res = Struct(**ans)

    def add_payment_method(self):
        credit_card_number = ""
        credit_card_exp_date = ""
        cvv = ""
        card_type= ""
        id = ""
        ans = self.controller.add_payment_method(credit_card_number, credit_card_exp_date, cvv, card_type, id)
        res = Struct(**ans)

    def add_address_details(self):
        city = ""
        street = ""
        zip_code = ""
        floor = ""
        apt = ""
        ans = self.controller.add_address_details(city, street, zip_code, floor, apt)
        res = Struct(**ans)


