from kivy.uix.textinput import TextInput

from assets.Utils.Utils import Utils
from urllib.parse import urlencode
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivymd.uix.textfield import MDTextField
from assets.windows.SideBar import SideBar
import csv
import requests
import json

from functools import partial
from kivy.uix.button import Button
from assets.windows.offers_list import Offers_Screen
from langdetect import detect, DetectorFactory
from assets.Utils.CheckValidity import CheckValidity
from textblob import TextBlob
import langid
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

        Clock.schedule_once(self.helper, 4)
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
        App.get_running_app().root.change_screen("menu_screen")
        #App.get_running_app().root.current = "menu_screen"

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
        self.area = '052'

    def personal(self):
        first_name = self.ids.first_name_input.text
        last_name = self.ids.last_name_input.text
        email = self.ids.email_input.text
        phone_number = self.ids.phone_input.text
        area_number = self.ids.area_input.text
        self.area = area_number
        phone_number =area_number+phone_number
        year = self.ids.year_input.text
        month = self.ids.month_input.text
        day = self.ids.day_input.text


        date_str = ''
        if year != '' and month != '' and day != '':
            date_str = f'{year}-{month}-{day}'

        ans = CheckValidity.checkValidityName(self, first_name)
        if ans is False:
            return

        ans = CheckValidity.checkValidityName(self, last_name)
        if ans is False:
            return

        ans = CheckValidity.checkValidityEmail(self, email)
        if ans is False:
            return

        ans = CheckValidity.checkValidityPhone(self, phone_number)
        if ans is False:
            return
        if self.gender == 0:
            Utils.pop(self, "Please Choose Gender", "alert")
            return
        # ---------------------------------------------haveee toooo checkkk birthdateeee----------------------
        if date_str != "":
            try:
                ans = CheckValidity.checkValidityDateOfBirth(self, date_str)
            except Exception as e:
                print(str(e))
                Utils.pop(self, str(e), "alert")
                return
            if ans is False:
                return

        ans = App.get_running_app().controller.update_user_details(first_name, last_name, email, phone_number, date_str,
                                                                   self.gender)
        if ans.res is True:
            # update the json------------------------------------------------
            self.user = ans.data
            Utils.pop(self, 'your personal details has been successfully changed', 'success')
            App.get_running_app().root.back_to_main()
            self.init_fields()
        else:
            Utils.pop(self, 'update details has failed: ' + ans.message, 'alert')
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
                self.ids.last_name_input.text = ""
            else:
                self.ids.last_name_input.text = self.user.last_name
            if (self.user.phone is None):
                self.ids.phone_input.text = ""
            else:
                phone_with_area = self.user.phone
                self.ids.phone_input.text = phone_with_area[3:len(phone_with_area)]
                self.ids.area_input.text = phone_with_area[0:3]
            if (self.user.email is None):
                self.ids.email_input.text = ""
            else:
                self.ids.email_input.text = self.user.email



            if self.user.gender=="male" :
                self.ids.male.active = True
            else:
                self.ids.female.active = True

            if (self.user.birth_date is None):
                self.ids.year_input.text = ""
                self.ids.month_input.text = ""
                self.ids.day_input.text = ""
            else:
                date = self.user.birth_date
                if ' ' in date:
                    date, e = date.split(' ')
                year, month, day = date.split('-')
                self.ids.year_input.text = year
                self.ids.month_input.text = month
                self.ids.day_input.text = day
            if(self.user.gender == 'male'):
                self.gender=1
            else:
                self.gender = 2

    def show_dropdown_year(self):
        menu_items = []
        for year in range(2021, 1900, -1):
            menu_items.append(
                {
                    'text': str(year),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(year): self.save_year(x),
                }
            )

        self.drop_down_years = MDDropdownMenu(
            caller=self.ids.year_input,
            items=menu_items,
            width_mult=4,

        )
        self.drop_down_years.open()

    def save_year(self, year):
        self.ids.year_input.text = year
        self.drop_down_years.dismiss()

    def show_dropdown_month(self):
        menu_items = []
        for month in range(12, 0, -1):
            menu_items.append(
                {
                    'text': str(month),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(month): self.save_month(x),
                }
            )

        self.drop_down_months = MDDropdownMenu(
            caller=self.ids.month_input,
            items=menu_items,
            width_mult=4,

        )
        self.drop_down_months.open()

    def save_month(self, month):
        self.ids.month_input.text = month
        self.drop_down_months.dismiss()

    def show_dropdown_day(self):
        if self.ids.month_input.text == "Month":
            month = "1"
        else:
            month = self.ids.month_input.text
        if month == "2":
            max_day = 28
        if month == "1" or month == "3" or month == "5" or month == "7" or month == "8" or month == "10" or month == "12":
            max_day = 31
        if month == "4" or month == "6" or month == "9" or month == "11":
            max_day = 30
        menu_items = []
        for day in range(max_day, 0, -1):
            menu_items.append(
                {
                    'text': str(day),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(day): self.save_day(x),
                }
            )

        self.drop_down_days = MDDropdownMenu(
            caller=self.ids.day_input,
            items=menu_items,
            width_mult=4,

        )

        self.drop_down_days.open()

    def save_day(self, day):
        self.ids.day_input.text = day
        self.drop_down_days.dismiss()

    def show_dropdown_area(self):
        menu_items = []
        areas = ['050', '052', '054', '055', '057', '058']
        for area in areas:
            menu_items.append(
                {
                    'text': area,
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=area: self.save_area(x),
                }
            )

        self.drop_down_areas = MDDropdownMenu(
            caller=self.ids.area_input,
            items=menu_items,
            width_mult=4,

        )

        self.drop_down_areas.open()

    def save_area(self, area):
        self.ids.area_input.text = area
        self.area = area
        self.drop_down_areas.dismiss()

    # click Cancel
    def on_cancel(self, instance, value):
        pass

    def save_male(self, instance, value):
        if (value):
            # male
            self.gender = 1
        else:
            # female
            self.gender = 2

    def save_female(self, instance, value):
        if (value):
            # male
            self.gender = 2
        else:
            # female
            self.gender = 1


class Password_box(BoxLayout):

    def __init__(self, **kwargs):
        super(Password_box, self).__init__(**kwargs)
        controller = App.get_running_app().controller
        self.user = controller.user_service

    def change_password(self):
        old_password = self.ids.old_password_input.text
        new_password1 = self.ids.new_password_input.text
        new_password2 = self.ids.new_password_verification_input.text
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
            self.clear_fields()
        else:
            Utils.pop(self, "change password failed", 'alert')

    def back_to_account_window(self):
        App.get_running_app().root.change_screen("account_screen")
        #App.get_running_app().root.current = 'account_screen'
        # App.get_running_app().root.prev = 'menu_screen'

    def clear_fields(self):
        self.ids.old_password_input.text = ""
        self.ids.new_password_input.text = ""
        self.ids.new_password_verification_input.text = ""
class txt_address(TextInput):
    runner = 0

    def insert_text(self, string, a):
        self.runner += 1
        self.text = string + self.text
        self.cursor = (0, 0)
        # return super(txt, self).insert_text(string, from_undo=False)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.text = self.text[1:]
        self.cursor = (0, 0)
class Address_box(BoxLayout):

    def __init__(self, **kwargs):
        super(Address_box, self).__init__(**kwargs)
        controller = App.get_running_app().controller
        self.user = controller.user_service
        self.chosen_city_lat = 0
        self.chosen_city_lng = 0
        self.open = True



    def drop_cities_autocomplete(self, text):

        if hasattr(self, 'drop_down_cities_autocomplete'):
            self.drop_down_cities_autocomplete.dismiss()

        menu_items = []
        input = text[::-1]
        api_key = 'AIzaSyCl3vD9sHXfJic-nNgxAGXmfA1g7Ymf_Rc'
        params = {
            'input': input,
            'key': api_key,
        }
        params_encoded = urlencode(params)

        url = f'https://maps.googleapis.com/maps/api/place/autocomplete/json?{params_encoded}&components=country:isr&types=(cities)&language=iw'#&language=iw'
        res = requests.get(url)
        result = res.json()
        addresses = result['predictions']
        for address in addresses:
            t=address['description']
            t=t[::-1]
            menu_items.append(

                {"text":f"[font=Arial]{t}[/font]" ,
                 'font': 'Arial',
                 "viewclass": "OneLineListItem",
                 "on_release": lambda x=t, y=address['place_id']: self.save_city(x, y),
                 }
            )

        self.drop_down_cities_autocomplete = MDDropdownMenu(
            caller=self.ids.city_input,
            items=menu_items,
            width_mult=10,
        )

        self.drop_down_cities_autocomplete.open()
    def save_city(self, chosen_city, place_id):
        self.drop_down_cities_autocomplete.dismiss()
        api_key = 'AIzaSyCl3vD9sHXfJic-nNgxAGXmfA1g7Ymf_Rc'
        self.get_lat_lng(api_key, place_id)
        self.ids.city_input.on_text = self.do_nothing()
        self.ids.city_input.text = chosen_city
        self.ids.city_input.on_text = self.drop_cities_autocomplete(self.ids.city_input.text)

    def do_nothing(self):
        print("kkkkkkkkkk")

    def check_lang(self, text):
        a = langid.classify(text)
        if (a[0] == 'he'):
            self.english = False
    def drop_streets_autocomplete(self, text):
        if hasattr(self, 'drop_down_streets_autocomplete'):
            self.drop_down_streets_autocomplete.dismiss()
        menu_items = []
        if self.ids.city_input.text =='':
            self.chosen_city_lat=0
            self.chosen_city_lng=0
        input = text[::-1]
        api_key = 'AIzaSyCl3vD9sHXfJic-nNgxAGXmfA1g7Ymf_Rc'
        params = {
            'input': input,
            'key': api_key,
        }
        params_encoded = urlencode(params)
        if (self.chosen_city_lng == 0 or self.chosen_city_lat == 0):
            url = f'https://maps.googleapis.com/maps/api/place/autocomplete/json?{params_encoded}&components=country:isr&types=address&language=iw&radius=500'
        else:
            url = f'https://maps.googleapis.com/maps/api/place/autocomplete/json?{params_encoded}&components=country:isr&types=address&language=iw&location={self.chosen_city_lat}%2C{self.chosen_city_lng}&radius=500'
        res = requests.get(url)
        result = res.json()
        addresses = result['predictions']
        for address in addresses:
            t = address['description']
            t = t[::-1]
            # a = langid.classify(t)
            # if (a[0] == 'he'):
            #     t=t[::-1]
            menu_items.append(
                {"text":f"[font=Arial]{t}[/font]",
                 'font': 'Arial',
                 "viewclass": "OneLineListItem",
                 "on_release": lambda x=t: self.save_street(x),
                 }
            )

        self.drop_down_streets_autocomplete = MDDropdownMenu(
            caller=self.ids.street_input,
            items=menu_items,
            width_mult=10,
        )
        self.drop_down_streets_autocomplete.open()
    def save_street(self, chosen_street):
        self.drop_down_streets_autocomplete.dismiss()
        self.ids.street_input.text = chosen_street
        self.drop_down_streets_autocomplete.dismiss()
        #self.ids.city_input.on_text= self.do_nothing()

    def get_lat_lng(self, api_key, place_id):
        params_details = {
            'place_id': place_id,
            'key': api_key,
        }
        params_encoded_details = urlencode(params_details)
        url_place_details = f'https://maps.googleapis.com/maps/api/place/details/json?{params_encoded_details}'
        res_details = requests.get(url_place_details)
        result_details = res_details.json()
        self.chosen_city_lat = result_details['result']['geometry']['location']['lat']
        self.chosen_city_lng = result_details['result']['geometry']['location']['lng']

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
        if not CheckValidity.contains_only_digits(self,zip_code, 'zip_code'):
            return
        building = self.ids.building_input.text
        if not CheckValidity.contains_only_digits(self,building, 'building'):
            return
        if not self.check_empty(building, 'building'):
            return
        apt = self.ids.apt_input.text
        if not CheckValidity.contains_only_digits(self, apt, 'apt'):
            return
        if not self.check_empty(apt, 'apt'):
            return

        ans = App.get_running_app().controller.add_address_details(city, street, zip_code, building, apt)
        if ans.res is True:
            # update the json------------------------------------------------
            self.user = ans.data
            Utils.pop(self, 'your address has been successfully changed', 'success')
            App.get_running_app().root.back_to_main()
            self.init_fields()
        else:
            Utils.pop(self, 'update address has failed', 'alert')
        return ans

    def init_fields(self):
        if (self.user.city is None):
            self.ids.city_input.text = ""
        else:
            self.ids.city_input.text = self.user.city
            self.drop_down_cities_autocomplete.dismiss()

        if (self.user.street is None):
            self.ids.street_input.text = ""
            #self.drop_down_streets_autocomplete.dismiss()
        else:
            self.ids.street_input.text = self.user.street

        if (self.user.zip_code is None):
            self.ids.zip_code_input.text = ""
        else:
            self.ids.zip_code_input.text = str(self.user.zip_code)

        if (self.user.floor is None):
            self.ids.building_input.text = ""
        else:
            self.ids.building_input.text = str(self.user.floor)

        if (self.user.apartment_number is None):
            self.ids.apt_input.text = ""
        else:
            self.ids.apt_input.text = str(self.user.apartment_number)

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
        App.get_running_app().root.change_screen("change_password_screen")
        #App.get_running_app().root.current = 'change_password_screen'

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
            # change gender initiallization
            if (self.user.gender is None):
                self.ids.gender.text = ""
            else:
                self.ids.gender.text = self.user.gender
            # change gender initiallization
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



