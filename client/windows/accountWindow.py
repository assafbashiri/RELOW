from Utils.Utils import Utils
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
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
import requests
import json

from windows.offers_list import Offers_Screen

from Utils.CheckValidity import CheckValidity


class Category_box(BoxLayout):
    pass

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class ACCOUNTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'account_screen'
        super(ACCOUNTScreen, self).__init__(**kwargs)


class Account_box(BoxLayout):

    def __init__(self, **kwargs):
        super(Account_box, self).__init__(**kwargs)
        self.personal_box = Personal_box()
        self.address_box = Address_box()
        self.password_box = Password_box()


        Clock.schedule_once(self.helper,4)
        # self.add_widget(self.current_box, len(self.children))
        # self.cat = Category_box()
        # self.sub_cat = Sub_Category_box()
        # self.dialog = None
    def helper(self, num):
        self.ids.choose_box.add_widget(self.personal_box)

    def remove_widgets(self):
        self.ids.choose_box.remove_widget(self.personal_box)
        self.ids.choose_box.remove_widget(self.address_box)
        self.ids.choose_box.remove_widget(self.password_box)
    def change_to_address(self):
        self.remove_widgets()
        self.ids.choose_box.add_widget(self.address_box)
    def change_to_personal(self):
        self.remove_widgets()
        self.ids.choose_box.add_widget(self.personal_box)
    def change_to_update_password(self):
        self.remove_widgets()
        self.ids.choose_box.add_widget(self.password_box)

    def init_fields(self):
        self.personal_box.init_fields()
        self.address_box.init_fields()

    def back(self):
        App.get_running_app().root.current = "menu_screen"


    def active_offers(self):
        ans = App.get_running_app().controller.get_all_active_buy_offers()
        self.act_buy_offers = Offers_Screen()
        self.act_buy_offers.insert_offers(list=ans)
        self.ids.boxi.add_widget(self.act_buy_offers)
    def exit(self):
        App.get_running_app().controller.exit()

    def change_to_cat(self):
        SideBar.change_to_cat(self)

class Personal_box(BoxLayout):

    def __init__(self, **kwargs):
        super(Personal_box, self).__init__(**kwargs)
        self.controller = App.get_running_app().controller
        self.user = self.controller.user_service

    def personal(self):
        first_name = self.ids.first_name_input.text
        last_name = self.ids.last_name_input.text
        email = self.ids.email_input.text
        #gender = self.ids.

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
        if ans.res is True:
            self.user = Struct(**ans.data)
            # update the json------------------------------------------------
            #self.parent.parent.manager.back_to_main()
            self.init_fields()
        return ans

    def clear_personal(self):
        self.ids.first_name.text = ""
        self.ids.last_name.text = ""
        self.ids.email.text = ""

    def init_fields(self):
        if (self.user is not None):
            if self.controller.guest is True:
                return
            if (self.user.first_name is None):
                self.ids.first_name_input.text = ""
            else:
                self.ids.first_name_input.text = self.user.first_name
            if (self.user.last_name is None):
                self.ids.last_name.text = ""
            else:
                self.ids.last_name_input.text = self.user.last_name
            if (self.user.phone is None):
                self.ids.phone.text = ""
            else:
                self.ids.phone_input.text = self.user.phone
            if (self.user.email is None):
                self.ids.email.text = ""
            else:
                self.ids.email_input.text = self.user.email

            if (self.user.gender is None):
                self.ids.gender.text = ""
            else:
                if self.user.gender =='male':
                    self.ids.male.active = True
                else:
                    self.ids.female.active = True

            if (self.user.birth_date is None):
                self.ids.birth_date.text = ""
            else:
                self.ids.birth_date_input.text = self.user.birth_date


    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # click OK
    def on_save(self, instance, value, date_range):
        self.ids.birth_date_input.text = str(value)

    # click Cancel
    def on_cancel(self, instance, value):
        pass
class Password_box(BoxLayout):

    def __init__(self, **kwargs):
        super(Password_box, self).__init__(**kwargs)
        controller = App.get_running_app().controller
        self.user = controller.user_service

    def change_password(self):
        old_password = self.ids.old_password.text
        new_password1 = self.ids.new_password1.text
        new_password2 = self.ids.new_password2.text
        if old_password == "":
            Utils.pop(self, 'please enter old password', 'alert')
            return
        if new_password1 == "":
            Utils.pop(self, 'please enter new password', 'alert')
            return
        if new_password2 == "":
            Utils.pop(self, 'please enter new password again', 'alert')
            return
        if not new_password1 == new_password2:
            Utils.pop(self, 'your new password is not match', 'alert')
            return
        if not CheckValidity.checkValidityPassword(self, new_password1):
            return
        ans = App.get_running_app().controller.update_password(old_password, new_password1)
        if ans.res is True:
            Utils.pop(self, 'your password has been successfully changed', 'success')
            self.back_to_account_window()
        else:
            Utils.pop(self, ans.message, 'alert')

class Address_box(BoxLayout):

    def __init__(self, **kwargs):
        super(Address_box, self).__init__(**kwargs)
        controller = App.get_running_app().controller
        self.user = controller.user_service
    def address(self):
        city = self.ids.city_input.text
        if not self.check_empty(city, 'city'):
            return

        street = self.ids.street_input.text
        if not self.check_empty(street, 'street'):
            return
        zip_code = self.ids.zip_code_input.text
        if not self.check_empty(zip_code, 'zip_code'):
            return
        # floor = self.ids.floor_input.text
        # if not self.check_empty(floor, 'floor'):
        #     return
        apt = self.ids.apt_number_input.text
        if not self.check_empty(apt, 'apt'):
            return
        ans = App.get_running_app().controller.add_address_details(city, street, zip_code, floor, apt)
        if ans.res is True:
            # update the json------------------------------------------------
            self.parent.parent.manager.back_to_main()
            self.init_fields()
        return ans

    def init_fields(self):
        if (self.user.city is None):
            self.ids.city_input.text = ""
        else:
            self.ids.city_input.text = self.user.city

        if (self.user.street is None):
            self.ids.street_input.text = ""
        else:
            self.ids.street_input.text = self.user.street

        if (self.user.zip_code is None):
            self.ids.zip_code_input.text = ""
        else:
            self.ids.zip_code_input.text = str(self.user.zip_code)

        # if (self.user.floor is None):
        #     self.ids.floor.text = ""

    def clear_address(self):
        self.ids.city.text = ""
        self.ids.street.text = ""
        self.ids.zip_code.text = ""
        self.ids.floor.text = ""
        self.ids.apt_number.text = ""

    def check_empty(self, to_check, obj):
        if to_check == '':
            Utils.pop(self, f'the {obj} is not valid', 'alert')
            # toast('the apt is not valid')
            return False
        return True



class Sub_Category_box(BoxLayout):
    pass


class BoxiLayout(BoxLayout):
    drop_down = ObjectProperty()

    def __init__(self, **kwargs):
        super(BoxiLayout, self).__init__(**kwargs)
        self.flag = 1  # 1 - update personal details   2 - add address details   3- add payment method
        self.gender = 0
        self.controller = App.get_running_app().controller
        Clock.schedule_once(self.insert_color, 0)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.rect = Rectangle(pos=self.pos, size=self.size)

        self.dialog = None

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

        # listen to size and position changes

        # self.insert_offers()

    def insert_color(self, num):
        with self.canvas.before:
            Color(251, 255, 230)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            print('done')

    def change_password(self):
        App.get_running_app().root.current = 'change_password_screen'

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
        if (self.user is not None):
            if controller.guest is True:
                return
            if (self.user.first_name is None):
                self.ids.first_name.text = ""
            else:
                self.ids.first_name.text = self.user.first_name
            if (self.user.last_name is None):
                self.ids.last_name.text = ""
            else:
                self.ids.last_name.text = self.user.last_name
            if (self.user.phone is None):
                self.ids.phone.text = ""
            else:
                self.ids.phone.text = self.user.phone
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

            # -----------------------------------------------------------------------------------------------------------

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

            # -----------------------------------------------------------------------------------------------------------

            # if (self.user.credit_card_number is None):
            #     self.ids.credit_card_number.text = ""
            # else:
            #     self.ids.credit_card_number.text = str(self.user.credit_card_number)
            #
            # if (self.user.credit_card_exp_date is None):
            #     self.ids.exp_date.text = ""
            # else:
            #     self.ids.exp_date.text = self.user.credit_card_exp_date
            #
            # if (self.user.cvv is None):
            #     self.ids.cvv.text = ""
            # else:
            #     self.ids.cvv.text = str(self.user.cvv)
            #
            # if (self.user.card_type is None):
            #     self.ids.card_type.text = ""
            # else:
            #     self.ids.card_type.text = self.user.card_type
            #
            # if (self.user.id_number is None):
            #     self.ids.id_number.text = ""
            # else:
            #     self.ids.id_number.text = str(self.user.id_number)

    def payment(self):
        credit_card_number = self.ids.credit_card_number.text
        if not self.check_empty(credit_card_number, 'credit_card_number'):
            return
        credit_card_exp_date = self.ids.exp_date.text
        if not self.check_empty(credit_card_exp_date, 'credit_card_exp_date'):
            return
        cvv = self.ids.cvv.text
        if not self.check_empty(cvv, 'cvv'):
            return
        card_type = self.ids.card_type.text
        if not self.check_empty(card_type, 'card_type'):
            return
        id = self.ids.id_number.text
        if not self.check_empty(id, 'id'):
            return
        ans = App.get_running_app().controller.add_payment_method(credit_card_number, credit_card_exp_date, cvv,
                                                                  card_type, id)
        if ans.res is True:
            # update the json------------------------------------------------
            self.parent.parent.manager.back_to_main()
            self.init_fields()

        return ans

    def clear_payment(self):
        self.ids.credit_card_number.text = ""
        self.ids.exp_date.text = ""
        self.ids.cvv.text = ""
        self.ids.card_type.text = ""
        self.ids.id_number.text = ""



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
                "on_release": lambda x=1: self.menu_callback(x, "male"),
            },
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
        addresses = {}
        addresses = self.get_address_list()
        # addresses = self.get_countries_cities_dict()
        menu_items = []
        for address in addresses:
            menu_items.append(
                {"text": address,
                 'font': 'Arial',
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
                 "on_release": lambda x=street, y=city: self.on_save_address(x, y)}
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

    def get_address_list(self):
        rows = {}
        # with open('city-street.csv', 'rb') as csvfile:
        #     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        # -------------------------------------------------------

        # with open('city-street.csv', 'r',encoding="utf8") as csv_file:
        with open('worldcities.csv', 'r', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file)
            city_dictionary = {}
            country_dictionary = {}
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
                country = line[4]
                street = line[2]
                # if city in city_dictionary.keys():
                #     city_dictionary[city].append(street)
                # else:
                #     city_dictionary[city] = []
                if country in country_dictionary.keys():
                    country_dictionary[country].append(city)
                else:
                    country_dictionary[country] = []
                    country_dictionary[country].append(city)

            return country_dictionary

    def get_countries_cities_dict(self):
        response = requests.get('https://countriesnow.space/api/v0.1/countries/population/cities')
        data = response.json()
        cities = {}
        for elem in data['data']:
            if elem['country'] not in cities.keys():
                cities[elem['country']] = []
                cities[elem['country']].append(elem['city'])
            else:
                cities[elem['country']].append(elem['city'])

        return cities

    def show_dropdown_address_gov_il(self):
        addresses = {}
        addresses = self.get_countries_cities_dict_gov_il()
        menu_items = []
        for address in addresses.keys():
            menu_items.append(
                {
                    'text': f"[font=Arial]{address[::-1]}[/font]",
                    'font_name': 'Arimo',
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=addresses[address], y=address: self.show_dropdown_cities_gov_il(x, y),
                }
            )

        self.drop_down_regoins_gov_il = MDDropdownMenu(
            caller=self.ids.drop_address,
            items=menu_items,
            width_mult=4,

        )
        self.drop_down_regoins_gov_il.open()

    def show_dropdown_cities_gov_il(self, cities, region):

        menu_items = []
        for city in cities.keys():
            menu_items.append(
                {'text': f"[font=Arial]{city[::-1]}[/font]",
                 "font_name": "Arial",
                 "viewclass": "OneLineListItem",
                 # here we have to open page or the offers of this sub categories ya sharmutut
                 "on_release": lambda x=cities[city], y=city, z=region: self.show_dropdown_streets_gov_il(x, y, z)}
            )
            #
        self.drop_down_cities_gov_il = MDDropdownMenu(
            caller=self.ids.drop_address,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_cities_gov_il.open()
        self.drop_down_regoins_gov_il.dismiss()

    def show_dropdown_streets_gov_il(self, streets, city, region):
        menu_items = []
        for street in streets:
            menu_items.append(

                {'text': f"[font=Arial]{street[::-1]}[/font]",
                 "viewclass": "OneLineListItem",
                 # here we have to open page or the offers of this sub categories ya sharmutut
                 "on_release": lambda x=street, y=city, z=region: self.on_save_address_gov_il(x, y, z)}
            )
            # self.on_save_address(x, y)
        self.drop_down_streets_gov_il = MDDropdownMenu(
            caller=self.ids.drop_address,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_streets_gov_il.open()
        self.drop_down_cities_gov_il.dismiss()

    def on_save_address_gov_il(self, street, city, region):
        self.region = region
        self.city = city
        self.street = street
        self.ids.city.text = city[::-1]
        self.ids.street.text = street[::-1]
        self.ids.region.text = region[::-1]
        self.drop_down_streets_gov_il.dismiss()

    def get_countries_cities_dict_gov_il(self):
        address_dict = {}
        res = requests.get(
            'https://data.gov.il/api/3/action/datastore_search?resource_id=1b14e41c-85b3-4c21-bdce-9fe48185ffca&limit=116621')
        data = json.loads(res.text)  # Here you have the data that you need
        for d in data['result']['records']:
            region = d['region_name']
            city = d['city_name']
            street = d['street_name']
            if region not in address_dict.keys():
                address_dict[region] = {}
            if city not in address_dict[region].keys():
                address_dict[region][city] = []
            address_dict[region][city].append(street)

        return address_dict
