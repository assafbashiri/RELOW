from kivymd.uix.picker import MDDatePicker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from assets.Utils.CheckValidity import CheckValidity
from assets.Utils.Utils import Utils
from assets.windows.SideBar import SideBar


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class LOGINScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'login_screen'
        super(LOGINScreen, self).__init__(**kwargs)


class Category_box(BoxLayout):
    pass


class Sub_Category_box(BoxLayout):
    pass


class Login_box(BoxLayout):

    def back(self):
        App.get_running_app().root.current ="connect_screen"

    def exit(self):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

    def __init__(self, **kwargs):
        super(Login_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        self.gender = 0

    def change_to_cat(self):
        SideBar.change_to_cat(self)

    def clear_register(self):
        self.ids.phone.text = ""
        self.ids.first_name.text = ""
        self.ids.last_name.text = ""
        self.ids.email.text = ""
        self.ids.password.text = ""
        self.ids.birth_date.text = ""

    def unregister(self):
        ans = App.get_running_app().controller.unregister()

        if ans.res is True:
            self.parent.parent.back_to_main()

    def register(self):
        controller = App.get_running_app().controller
        if controller.user_service is not None:
            if controller.guest is False:
                Utils.pop(self, 'you need to logout first', 'alert')
                # toast('you need to logout first')
                return
        phone = self.ids.phone.text
        phone_bool = CheckValidity.checkValidityPhone(self, phone)

        if not phone_bool:
            return

        first_name = self.ids.first_name.text
        bool_ans = self.validate_name(first_name)
        if not bool_ans:
            return

        last_name = self.ids.last_name.text
        bool_ans = self.validate_name(last_name)
        if not bool_ans:
            return

        email = self.ids.email.text
        email_bool = CheckValidity.checkValidityEmail(self, email)
        if not email_bool:
            return

        password = self.ids.password.text
        password_bool = CheckValidity.checkValidityPassword(self, password)
        if not password_bool:
            return

        birth_date_str = self.ids.birth_date.text
        birth_date = Utils.string_to_datetime_without_hour(self, birth_date_str)
        gender = self.gender
        ans = App.get_running_app().controller.register(first_name, last_name, phone, email, password, birth_date,
                                                        gender)
        if ans.res is True:
            self.parent.parent.back_to_main()

    def validate_name(self, name):
        name_bool = CheckValidity.checkValidityName(self, name)
        return name_bool

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # click OK
    def on_save(self, instance, value, date_range):
        self.ids.birth_date.text = str(value)
        # birth_date = value

    # click Cancel
    def on_cancel(self, instance, value):
        pass

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
        if App.get_running_app().controller.user_service is None:
            ans = App.get_running_app().controller.login_from_exist_user(email, password)
        else:
            ans = App.get_running_app().controller.login(email, password)
        # after logout back to the main menu
        if ans.res is True:
            self.parent.parent.parent.back_to_main()
            if App.get_running_app().root is not None:
                answer = App.get_running_app().controller.user_service.first_name
                if answer is None:
                    self.update_hello_name("        Hello, " + "guest")
                else:
                    self.update_hello_name("        Hello, " + App.get_running_app().controller.user_service.first_name)
                    self.update_connect_logout_btn_text("LOGOUT")
                App.get_running_app().root.screens[0].ids.side_box.close_offers_windows()


        else:
            if ans.message == "user is not active":
                App.get_running_app().root.current = "confirmation_screen"
            if ans.message == "there is no such an email address in the system":
                Utils.pop(self, "there is no such an email address in the system", "alert")
            if ans.message == "incorrect Password":
                Utils.pop(self, "incorrect Password", "alert")


    def clear_login(self):
        self.ids.email.text = ""
        self.ids.password.text = ""



    def forgot_password(self):
        email = self.ids.email.text
        ans = App.get_running_app().controller.forgot_password(email)
        if ans.res is True:
            Utils.pop(self, "your new password send to your mail", 'alert')
        else:
            Utils.pop(self, "the email is not exist in out system", 'alert')

    def update_connect_logout_btn_text(self, text):
        App.get_running_app().root.screens[0].ids.side_box.ids.logout_register.text = text

    def update_hello_name(self, msg):
        App.get_running_app().root.screens[0].ids.side_box.ids.hello.text = msg
        # # menu screen 0
        # App.get_running_app().root.screens[0].ids.menu_box.ids.side_box.ids.hello.text = msg
        # # connect screen 1
        # App.get_running_app().root.screens[1].children[0].ids.side_box.ids.hello.text = msg
        # # account screen 2
        # App.get_running_app().root.screens[2].children[0].ids.side_box.ids.hello.text = msg
        # # search screen 3
        # App.get_running_app().root.screens[3].children[0].ids.side_box.ids.hello.text = msg
        # # add offer screen 4
        # App.get_running_app().root.screens[4].children[0].ids.side_box.ids.hello.text = msg
        # # my offers screen 5
        # App.get_running_app().root.screens[5].children[0].ids.side_box.ids.hello.text = msg
        # # update offers screen 6
        # App.get_running_app().root.screens[6].children[0].ids.side_box.ids.hello.text = msg
        # # register screen 7
        # App.get_running_app().root.screens[7].ids.side_box.ids.hello.text = msg
        # # login screen 8
        # App.get_running_app().root.screens[8].ids.side_box.ids.hello.text = msg
        # # # contact screen 9
        # # App.get_running_app().root.screens[9].children[0].ids.side_box.ids.hello.text = msg
        # # # confirmation screen 10
        # # z = App.get_running_app().root.screens[10].children[0].ids.side_box.ids.hello.text = msg
        # # # password screen 11
        # # z = App.get_running_app().root.screens[11].children[0].ids.side_box.ids.hello.text = msg
        # # seller screen 12
        # App.get_running_app().root.screens[12].ids.side_box.ids.hello.text = msg
    def back_to_menu(self):
        App.get_running_app().root.current = 'menu_screen'
