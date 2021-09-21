from datetime import datetime
from kivymd.uix.picker import MDDatePicker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from Utils.CheckValidity import CheckValidity
from Utils.Utils import Utils
from windows.SideBar import SideBar


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class CONNECTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'connect_screen'
        super(CONNECTScreen, self).__init__(**kwargs)


class Category_box(BoxLayout):
    pass

class Sub_Category_box(BoxLayout):
    pass

class Connect_box(BoxLayout):

    def exit(self):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

    def __init__(self, **kwargs):
        super(Connect_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        self.gender = 0

    def register_new(self):
        App.get_running_app().root.current = 'register_screen'

    def login_new(self):
        App.get_running_app().root.current = 'login_screen'

    def change_to_cat(self):
        SideBar.change_to_cat(self)


    def clear_register(self):
        self.ids.user_name.text=""
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
                toast('you need to logout first')
                return
        user_name = self.ids.user_name.text
        user_name_bool  = CheckValidity.checkValidityUserName(self, user_name)

        if not user_name_bool:
            return


        first_name = self.ids.first_name.text
        bool_ans=self.validate_name(first_name)
        if not bool_ans:
            return

        last_name = self.ids.last_name.text
        bool_ans = self.validate_name(last_name)
        if not bool_ans:
            return

        email = self.ids.email.text
        email_bool = CheckValidity.checkValidityEmail(self,email)
        if not email_bool:
            return

        password = self.ids.password.text
        password_bool = CheckValidity.checkValidityPassword(self,password)
        if not password_bool:
            return

        birth_date_str = self.ids.birth_date.text
        birth_date = Utils.string_to_datetime_without_hour(self, birth_date_str)
        gender = self.gender
        ans = App.get_running_app().controller.register(first_name, last_name, user_name, email, password, birth_date,
                                                        gender)
        if ans.res is True:
            self.parent.parent.back_to_main()

    def validate_name(self,name):
        name_bool = CheckValidity.checkValidityName(self,name)
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
        username = self.ids.user_name.text
        password = self.ids.password.text
        ans = App.get_running_app().controller.login(username, password)
        # after logout back to the main menu
        if ans.res is True:
            self.parent.parent.back_to_main()


    def clear_login(self):
        self.ids.log_in_username.text=""
        self.ids.log_in_password.text=""

    def logout(self):

        ans = App.get_running_app().controller.logout()

        # after logout back to the main menu
        if ans.res is True:
            self.parent.parent.back_to_main()





    # orientation: "horizontal"
    # BoxLayout:
    #     orientation: "vertical"
    #     padding:20
    #     spacing:20
    #     MDGridLayout:
    #         cols: 1
    #         spacing:5
    #         adaptive_height: True
    #         #adaptive_width: True
    #         #daptive_size: True
    #         MDLabel:
    #             id: register_label
    #             text: "Register"
    #
    #         MDTextFieldRound:
    #             text : "tom"
    #             id:first_name
    #             hint_text: "first name"
    #             icon_right: "account"
    #
    #
    #         MDTextFieldRound:
    #             text : "nisim"
    #             id:last_name
    #             hint_text: "last name"
    #             icon_right: "account"
    #
    #         MDTextFieldRound:
    #             text : "tomnis1234"
    #             id:user_name
    #             hint_text: "username"
    #             icon_right: "account"
    #
    #
    #         MDTextFieldRound:
    #             text : "tomnisim@gmail.com"
    #             id:email
    #             hint_text: "email"
    #             icon_right: "account"
    #
    #
    #         MDTextFieldRound:
    #             text : "12345678Tn"
    #             id:password
    #             hint_text: "password"
    #             icon_right: "eye-off"
    #             password : True
    #
    #
    #         MDTextFieldRound:
    #             text : "2022-11-11"
    #             id:birth_date
    #             hint_text: "birth date"
    #             icon_right: "account"
    #             on_focus:root.show_date_picker()
    #
    #
    #
    #         MDDropDownItem:
    #             id: drop
    #             pos_hint: {'center_x': .5, 'center_y': .5}
    #             text: 'gender'
    #             on_release: root.show_dropdown()
    #
    #     MDGridLayout:
    #         cols:3
    #
    #         MDRoundFlatButton:
    #             text:"Register"
    #             font_size: 12
    #             on_press:root.register()
    #
    #         MDRoundFlatButton:
    #             text:"Unregister"
    #             font_size: 12
    #             on_press:root.unregister()
    #
    #         MDRoundFlatButton:
    #             text:"clear_register"
    #             font_size: 12
    #             on_press:root.clear_register()
    #
    #
    #
        # MDGridLayout:
        #     cols: 1
        #     MDLabel:
        #         id: login_label
        #         text: "LOGIN"
        #
        #     MDTextFieldRound:
        #         text:'tomnis'
        #         id:log_in_username
        #         hint_text: "user name"
        #         icon_right: "account"
        #
        #
        #     MDTextFieldRound:
        #         text:'123'
        #         id:log_in_password
        #         hint_text: "password"
        #         icon_right: "account"
        # MDGridLayout:
        #     cols:3
        #
        #     MDRoundFlatButton:
        #         text:"Login"
        #         font_size: 12
        #         on_press:root.login()
        #
        #     MDRoundFlatButton:
        #         text:"Logout"
        #         font_size: 12
        #         on_press:root.logout()
        #
        #     MDRoundFlatButton:
        #         text:"clear_login"
        #         font_size: 12
        #         on_press:root.clear_login()