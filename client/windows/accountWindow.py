from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from Service.Object.UserService import UserService
from kivymd.uix.picker import MDDatePicker

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
        self.sub_cat = Sub_Category_box()

    def exit(self):
        App.get_running_app().controller.exit()

    def change_to_cat(self):
        self.side = self.ids.side_box
        self.remove_widget(self.side)
        self.add_widget(self.cat)

    def back_to_menu(self):
        self.add_widget(self.side)
        self.remove_widget(self.cat)

    def change_to_sub_cat(self):
        self.remove_widget(self.cat)
        self.add_widget(self.sub_cat)

    def back_to_cat(self):
        self.add_widget(self.cat)
        self.remove_widget(self.sub_cat)

class Sub_Category_box(BoxLayout):
    pass
class BoxiLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxiLayout, self).__init__(**kwargs)
        self.flag = 1




    def generall(self):
        self.flag = 1
        if self.ids.first_name.hint_text == "first name":
            return
        self.ids.first_name.hint_text = "first name"
        self.ids.last_name.hint_text = "last_name"
        self.ids.user_name.hint_text = "user_name"
        self.ids.email.hint_text = "email"
        self.children[2].add_widget(self.ids.birth_date, 5)
        self.children[2].add_widget(self.ids.password,6)
        self.ids.gender.hint_text = "gender"

    def address(self):
        self.flag = 2
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
        self.flag = 3
        if self.ids.first_name.hint_text == "id_number":
            return
        self.ids.first_name.hint_text = "id_number"
        self.ids.last_name.hint_text = "card number"
        self.ids.user_name.hint_text = "exp date"
        self.ids.email.hint_text = "cvv"
        self.children[2].remove_widget(self.ids.password)
        self.children[2].remove_widget(self.ids.birth_date)
        self.ids.gender.hint_text = "card type"

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.ids.birth_date.text = str(value)
        # birth_date = value

    # click Cancel
    def on_cancel(self, instance, value):
        pass


    def update(self):
        if self.flag == 1:
            first_name = self.ids.first_name.text
            last_name = self.ids.last_name.text
            user_name = self.ids.user_name.text
            email = self.ids.email.text
            password = self.ids.password.text
            birth_date = self.ids.birth_date.text
            gender = self.ids.gender.text
            ans = App.get_running_app().controller.update(first_name, last_name, user_name, email, password, birth_date, gender)

        if self.flag == 2:
            city = self.ids.first_name.text
            street = self.ids.last_name.text
            zip_code = self.ids.email.text
            floor = self.ids.gender.text
            apt = self.ids.user_name.text
            ans = App.get_running_app().controller.add_address_details(city, street, zip_code, floor, apt)

        if self.flag == 3:
            credit_card_number = self.ids.last_name.text
            credit_card_exp_date = self.ids.user_name.text
            cvv = self.ids.email.text
            card_type = self.ids.gender.text
            id = self.ids.first_name.text
            ans = App.get_running_app().controller.add_payment_method(credit_card_number, credit_card_exp_date, cvv, card_type, id)

        print("999999999999999999999999")
        print(ans.message)
        # for error in ans.message:
        #     toast(error)
        if ans.res is True:
            self.parent.parent.manager.back_to_main()


        return ans



