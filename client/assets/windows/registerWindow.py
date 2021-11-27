from datetime import datetime

from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from assets.Utils.CheckValidity import CheckValidity
from assets.Utils.Utils import Utils


class REGISTERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'register_screen'
        super(REGISTERScreen, self).__init__(**kwargs)


class Register_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Register_box, self).__init__(**kwargs)
        self.gender = 0
        self.dialog = None
        self.area = '052'
        self.orientation = 'vertical'

    def back(self):
        App.get_running_app().root.change_screen("connect_screen")

    def exit(self):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

    def clear_register(self):
        self.ids.phone_input.text = ""
        self.ids.first_name_input.text = ""
        self.ids.last_name_input.text = ""
        self.ids.email_input.text = ""
        self.ids.password_input.text = ""
        # self.ids.birth_date.text = ""

    def register(self):
        controller = App.get_running_app().controller
        if controller.user_service is not None:
            if controller.guest is False:
                Utils.pop(self, "you need to logout first", 'alert')
                return
        first_name = self.ids.first_name_input.text
        last_name = self.ids.last_name_input.text
        email = self.ids.email_input.text
        phone_number = self.ids.phone_input.text
        area_number = self.ids.area_input.text
        self.area = area_number
        phone_number = area_number + phone_number
        password = self.ids.password_input.text
        year = self.ids.year_input.text
        month = self.ids.month_input.text
        day = self.ids.day_input.text

        date_str = ''
        if year != '' and month != '' and day != '':
            date_str = f'{year}-{month}-{day}'

        if not CheckValidity.checkValidityName(self, first_name):
            return
        if not CheckValidity.checkValidityName(self, last_name):
            return
        if not CheckValidity.checkValidityEmail(self, email):
            return
        if not CheckValidity.checkValidityPhone(self, phone_number):
            return
        if not CheckValidity.checkValidityPassword(self, password):
            return
        if self.gender == 0:
            Utils.pop(self, "Please Choose Gender", "alert")
            return
        if date_str != "":
            ans = CheckValidity.checkValidityDateOfBirth(self, date_str)
            if ans is False:
                return
        ans = App.get_running_app().controller.register(first_name, last_name, phone_number, email, password, date_str,
                                                        self.gender)
        if ans.res is True:
            App.get_running_app().root.change_screen("confirmation_screen")
            self.clear_register()
        else:
            Utils.pop(self, "register failed, please try again", "alert")

    def show_dropdown_year(self):
        menu_items = []
        today_year = datetime.today().year
        for year in range(today_year, 1900, -1):
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
