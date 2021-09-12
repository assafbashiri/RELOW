from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from Service.Object.UserService import UserService
from kivymd.uix.picker import MDDatePicker

from client.windows.offers_list import Offers_Screen


class Category_box(BoxLayout):
    pass

class ACCOUNTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'account_screen'
        super(ACCOUNTScreen, self).__init__(**kwargs)



class Account_box(BoxLayout):

    def __init__(self,**kwargs):
        super(Account_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()


    def active_offers(self):
        ans = App.get_running_app().controller.get_all_active_buy_offers()
        self.act_buy_offers = Offers_Screen()
        self.act_buy_offers.insert_offers(list=ans)
        self.ids.boxi.add_widget(self.act_buy_offers)

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
    drop_down = ObjectProperty()

    def __init__(self, **kwargs):
        super(BoxiLayout, self).__init__(**kwargs)
        self.flag = 1 # 1 - update personal details   2 - add address details   3- add payment method
        self.gender = 0




    def personal(self):
        first_name = self.ids.first_name.text
        last_name = self.ids.last_name.text
        user_name = self.ids.user_name.text
        email = self.ids.email.text
        password = self.ids.password.text
        birth_date = self.ids.birth_date.text
        gender = self.gender
        ans = App.get_running_app().controller.update(first_name, last_name, user_name, email, password, birth_date,
                                                      gender)
        print(ans.message)
        if ans.res is True:
            # update the json------------------------------------------------
            self.parent.parent.manager.back_to_main()
        return ans


    def clear_personal(self):
        self.ids.first_name.text=""
        self.ids.last_name.text=""
        self.ids.user_name.text=""
        self.ids.email.text=""
        self.ids.password.text=""
        self.ids.birth_date.text=""


    def address(self):
        city = self.ids.city.text
        street = self.ids.street.text
        zip_code = self.ids.zip_code.text
        floor = self.ids.floor.text
        apt = self.ids.apt_number.text
        ans = App.get_running_app().controller.add_address_details(city, street, zip_code, floor, apt)
        print(ans.message)
        if ans.res is True:
            # update the json------------------------------------------------
            self.parent.parent.manager.back_to_main()
        return ans


    def clear_address(self):
        self.ids.city.text=""
        self.ids.street.text=""
        self.ids.zip_code.text=""
        self.ids.floor.text=""
        self.ids.apt_number.text=""


    def payment(self):
        credit_card_number = self.ids.credit_card_number.text
        credit_card_exp_date = self.ids.exp_date.text
        cvv = self.ids.cvv.text
        card_type = self.ids.card_type.text
        id = self.ids.id_number.text
        ans = App.get_running_app().controller.add_payment_method(credit_card_number, credit_card_exp_date, cvv,
                                                                  card_type, id)
        print(ans.message)
        if ans.res is True:
            # update the json------------------------------------------------
            self.parent.parent.manager.back_to_main()

        return ans

    def clear_payment(self):
        self.ids.credit_card_number.text=""
        self.ids.exp_date.text=""
        self.ids.cvv.text=""
        self.ids.card_type.text=""
        self.ids.id_number.text=""


    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # click OK
    def on_save(self, instance, value, date_range):
        self.ids.birth_date.text = str(value)


    # click Cancel
    def on_cancel(self, instance, value):
        pass


    def show_date_picker_exp_date(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save_exp_date, on_cancel=self.on_cancel)
        date_dialog.open()

    # click OK
    def on_save_exp_date(self, instance, value, date_range):
        self.ids.exp_date.text = str(value)



    def show_dropdown(self):

        menu_items = [
            {
                "text": "male",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=1: self.menu_callback(x,"male"),
            } ,
            {
                "text": "female",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=2: self.menu_callback(x, "female"),
            }
        ]
        self.drop_down = MDDropdownMenu(
            caller=self.ids.drop,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down.open()

    def menu_callback(self, gender_int, gender_string):
        self.gender = gender_int
        self.ids.drop.text = gender_string
        self.drop_down.dismiss()







