
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from Service.Object.UserService import UserService

class Category_box(BoxLayout):
    pass

class ACCOUNTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(ACCOUNTScreen, self).__init__(**kwargs)


class Account_box(BoxLayout):
    def __init__(self,**kwargs):
        super(Account_box, self).__init__(**kwargs)
        self.cat = Category_box()
    def change(self):
        print(self.parent)
        self.side = self.ids.side_box
        self.remove_widget(self.side)
        print(self.parent)
        self.add_widget(self.cat)
        # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
        # print(self.parent)
        # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)

    def back(self):
        # self.remove_widget(self.ids.category_box)
        self.add_widget(self.side)
        self.remove_widget(self.cat)


class BoxiLayout(BoxLayout):
    def address(self):
        if self.ids.first_name.hint_text == "city":
            return
        self.ids.first_name.hint_text = "city"
        self.ids.last_name.hint_text = "street"
        self.ids.user_name.hint_text = "apt. number"
        self.ids.email.hint_text = "zip code"
        self.children[2].remove_widget(self.ids.password)
        self.children[2].remove_widget(self.ids.birth_date)
        self.ids.gender.hint_text = "floor"

    def payment(self):
        if self.ids.first_name.hint_text == "id_number":
            return
        self.ids.first_name.hint_text = "id_number"
        self.ids.last_name.hint_text = "card number"
        self.ids.user_name.hint_text = "exp date"
        self.ids.email.hint_text = "cvv"
        self.children[2].remove_widget(self.ids.password)
        self.children[2].remove_widget(self.ids.birth_date)
        self.ids.gender.hint_text = "card type"

    def generall(self):
        if self.ids.first_name.hint_text == "first name":
            return
        self.ids.first_name.hint_text = "first name"
        self.ids.last_name.hint_text = "last_name"
        self.ids.user_name.hint_text = "user_name"
        self.ids.email.hint_text = "email"
        self.children[2].add_widget(self.ids.birth_date, 5)
        self.children[2].add_widget(self.ids.password,6)
        self.ids.gender.hint_text = "gender"


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


