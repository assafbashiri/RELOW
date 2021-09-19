

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from Service.Object.UserService import UserService
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from windows.SideBar import SideBar
from datetime import datetime
from kivymd.toast import toast
import csv

from windows.offers_list import Offers_Screen

from Utils.CheckValidity import CheckValidity


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
        SideBar.change_to_cat(self)


class Sub_Category_box(BoxLayout):
    pass
class BoxiLayout(BoxLayout):
    drop_down = ObjectProperty()

    def __init__(self, **kwargs):
        super(BoxiLayout, self).__init__(**kwargs)
        self.flag = 1 # 1 - update personal details   2 - add address details   3- add payment method
        self.gender = 0
        self.controller = App.get_running_app().controller

    def change_password(self):
        temp1 = MDTextField(hint_text="old password")
        temp2 = MDTextField(hint_text="new password")
        temp3 = MDTextField(hint_text="new password again")
        btn = Button(text='change!!', size_hint=(None, None), height=40)
        btn.bind(on_release=lambda btn: self.controller.update_password(temp1.text, temp2.text))
        # CHEK INPUT

        self.ids.counti.add_widget(temp1)
        self.ids.counti.add_widget(temp2)
        self.ids.counti.add_widget(temp3)
        self.ids.counti.add_widget(btn)

    def init_fields(self):
        controller = App.get_running_app().controller
        self.user = controller.user_service
        if(self.user is not None):
            if controller.guest is True:
                toast("is a guest")
                return
            if (self.user.first_name is None):
                self.ids.first_name.text = ""
            else:
                self.ids.first_name.text = self.user.first_name
            if (self.user.last_name is None):
                self.ids.last_name.text = ""
            else:
                self.ids.last_name.text = self.user.last_name
            if (self.user.user_name is None):
                self.ids.user_name.text = ""
            else:
                self.ids.user_name.text = self.user.user_name
            if (self.user.email is None):
                self.ids.email.text = ""
            else:
                self.ids.email.text = self.user.email

            if (self.user.gender is None):
                self.ids.gender.text = ""
            else:
                self.ids.gender.text = self.user.gender


            if (self.user.birth_date is None):
                self.ids.birth_date.text = ""
            else:
                self.ids.birth_date.text = self.user.birth_date

            #-----------------------------------------------------------------------------------------------------------

            if (self.user.city is None):
                self.ids.city.text = ""
            else:
                self.ids.city.text = self.user.city

            if (self.user.street is None):
                self.ids.street.text = ""
            else:
                self.ids.street.text = self.user.street

            if (self.user.zip_code is None):
                self.ids.zip_code.text = ""
            else:
                self.ids.zip_code.text = str(self.user.zip_code)

            if (self.user.floor is None):
                self.ids.floor.text = ""
            else:
                self.ids.floor.text = str(self.user.floor)


            # if (self.user.apartment_number is None):
            #     self.ids.apt_number.text = ""
            # else:
            #     self.ids.apt_number.text = str(self.user.apartment_number)


            #-----------------------------------------------------------------------------------------------------------

            if (self.user.credit_card_number is None):
                self.ids.credit_card_number.text = ""
            else:
                self.ids.credit_card_number.text = str(self.user.credit_card_number)

            if (self.user.credit_card_exp_date is None):
                self.ids.exp_date.text = ""
            else:
                self.ids.exp_date.text = self.user.credit_card_exp_date

            if (self.user.cvv is None):
                self.ids.cvv.text = ""
            else:
                self.ids.cvv.text = str(self.user.cvv)

            if (self.user.card_type is None):
                self.ids.card_type.text = ""
            else:
                self.ids.card_type.text = self.user.card_type

            if (self.user.id_number is None):
                self.ids.id_number.text = ""
            else:
                self.ids.id_number.text = str(self.user.id_number)

    def personal(self):
        first_name = self.ids.first_name.text
        last_name = self.ids.last_name.text
        email = self.ids.email.text

        if first_name != "":
            ans = CheckValidity.checkValidityName(self, first_name)
            if ans is False:
                return

        if last_name != "":
            ans = CheckValidity.checkValidityName(self, last_name)
            if ans is False:
                return

        if email != "":
            ans = CheckValidity.checkValidityEmail(self, email)
            if ans is False:
                return

        ans = App.get_running_app().controller.update(first_name, last_name, email)
        print(ans.message)
        if ans.res is True:
            # update the json------------------------------------------------
            self.parent.parent.manager.back_to_main()
            self.init_fields()
        return ans


    def clear_personal(self):
        self.ids.first_name.text=""
        self.ids.last_name.text=""
        self.ids.email.text=""

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
            self.init_fields()
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
            self.init_fields()

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
            caller=self.ids.gender,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down.open()

    def menu_callback(self, gender_int, gender_string):
        self.gender = gender_int
        self.ids.gender.text = gender_string
        self.drop_down.dismiss()


    def show_dropdown_address(self):
        addresses={}
        addresses = self.get_adress_list()
        menu_items = []
        for address in addresses:
            menu_items.append(
                {"text": address,
                 "viewclass": "OneLineListItem",
                 "on_release": lambda x=addresses[address], y=address: self.show_dropdown_streets(x, y),
                 }
            )

        self.drop_down_cities = MDDropdownMenu(
            caller=self.ids.drop_address,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_cities.open()

    def show_dropdown_streets(self, streets, city):

        menu_items = []
        for street in streets:
            menu_items.append(
                {"text": street,
                 "viewclass": "OneLineListItem",
                 # here we have to open page or the offers of this sub categories ya sharmutut
                 "on_release": lambda x=street, y=city: self.on_save_address(x, y) }
            )
        self.drop_down_streets = MDDropdownMenu(
            caller=self.ids.drop_address,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_streets.open()
        self.drop_down_cities.dismiss()

    def on_save_address(self, street, city):
        self.city = city
        self.street = street
        self.ids.city.text = city
        self.ids.street.text = street
        self.drop_down_streets.dismiss()

    def get_adress_list(self):
        rows={}
        # with open('city-street.csv', 'rb') as csvfile:
        #     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            #-------------------------------------------------------

        with open('city-street.csv', 'r',encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file)
            city_dictionary = {}
            # with open('city-street.csv', 'r') as csv_file:
            #     csv_reader = csv.reader(csv_file)
            #
            #     for line in csv_reader:
            #         a = 5
            #         # if line[0] == '9000‭':
            #         print("\n  עיר:  " + line[1])
            #         print(' רחוב: ' + line[2])
            for line in csv_reader:

                city = line[1]
                city = ','.join(city)
                street = line[2]
                if city in city_dictionary.keys():
                    city_dictionary[city].append(street)
                else:
                    city_dictionary[city] = []



            return city_dictionary












