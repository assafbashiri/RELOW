from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField

from assets.Utils.CheckValidity import CheckValidity
from assets.windows.SideBar import SideBar
from assets.Utils.Utils import Utils
class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class REGISTERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'register_screen'
        super(REGISTERScreen, self).__init__(**kwargs)

class Category_box(BoxLayout):
    pass

class Sub_Category_box(BoxLayout):
    pass

class Register_box(BoxLayout):

    def exit(self):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

    def __init__(self, **kwargs):
        super(Register_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        self.gender = 0
        self.dialog=None
        self.gender=0
        self.area='052'
        self.orientation='vertical'

    def change_to_cat(self):
        SideBar.change_to_cat(self)

    def back(self):
        App.get_running_app().root.change_screen("connect_screen")
        #App.get_running_app().root.current ="connect_screen"

    def clear_register(self):
        self.ids.phone.text=""
        self.ids.first_name.text=""
        self.ids.last_name.text=""
        self.ids.email.text=""
        self.ids.password.text=""
        self.ids.birth_date.text=""

    def unregister(self):
        ans = App.get_running_app().controller.unregister()

        if ans.res is True:
            self.parent.parent.back_to_main()

    def register(self):
        controller = App.get_running_app().controller
        if controller.user_service is not None:
            if controller.guest is False:
                Utils.pop(self,"you need to logout first", 'alert')
                #toast('you need to logout first')
                return

        if self.area=='':
            Utils.pop(self,"Please Choose area code","alert")
            return
        phone = self.ids.phone_input.text
        phone_with_area = f'{self.area}{phone}'
        phone_bool  = CheckValidity.checkValidityPhone(self, phone_with_area)

        if not phone_bool:
            return


        first_name = self.ids.first_name_input.text
        bool_ans=self.validate_name(first_name)
        if not bool_ans:
            return

        last_name = self.ids.last_name_input.text
        bool_ans = self.validate_name(last_name)
        if not bool_ans:
            return

        email = self.ids.email_input.text
        email_bool = CheckValidity.checkValidityEmail(self,email)
        if not email_bool:
            return

        password = self.ids.password_input.text
        password_bool = CheckValidity.checkValidityPassword(self,password)
        if not password_bool:
            return

        gender = self.gender
        if gender==0:
            Utils.pop(self,"Please Choose Gender","alert")
            return

        year = self.ids.year_input.text
        month = self.ids.month_input.text
        day = self.ids.day_input.text
        date_str = ''
        if year != '' and month != '' and day != '':
            date_str = f'{year}-{month}-{day}'
        birth_date = Utils.string_to_datetime_without_hour(self, date_str)
        ans = App.get_running_app().controller.register(first_name, last_name, phone_with_area, email, password, birth_date,
                                                        gender)
        if ans.res is True:
            App.get_running_app().root.change_screen("confirmation_screen")
            #App.get_running_app().root.current = 'confirmation_screen'
            # self.parent.parent.parent.back_to_main()

    def validate_name(self,name):
        name_bool = CheckValidity.checkValidityName(self,name)
        return name_bool

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
        menu_items = []
        for day in range(31, 0, -1):
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
        areas = ['050','052','054','055','057','058']
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
        self.area=area
        self.drop_down_areas.dismiss()

    # click Cancel
    def on_cancel(self, instance, value):
        pass

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

    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text
        ans = App.get_running_app().controller.login(email, password)
        # after logout back to the main menu
        if ans.res is True:
            self.parent.parent.back_to_main()


    def clear_login(self):
        self.ids.log_in_email.text=""
        self.ids.log_in_password.text=""

    def logout(self):

        ans = App.get_running_app().controller.logout()

        # after logout back to the main menu
        if ans.res is True:
            self.parent.parent.back_to_main()

    def save_male(self, instance, value):
        if (value):
            #male
            self.gender = 1
        else:
            #female
            self.gender = 2
    def save_female(self, instance, value):
        if (value):
            #male
            self.gender = 2
        else:
            #female
            self.gender = 1

class buyer_terms(Popup):
    def __init__(self, **kwargs):
        super(buyer_terms, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.address = MDTextField(hint_text='ADDRESS')
        self.box.add_widget(self.address)
        self.insert = Button(text="INSERT")
        self.insert.bind(on_press=lambda x:self.insert_add())
        self.box.add_widget(self.insert)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x:self.out())
        self.box.add_widget(self.back)
        self.add_widget(self.box)

    def out(self):
        self.dismiss()

    def insert_add(self):
        self.parent.children[1].new_address = self.address.text
        self.parent.children[1].other_address.text = self.address.text
        self.parent.children[1].change = True
        self.dismiss()


