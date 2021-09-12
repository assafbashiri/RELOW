from datetime import datetime
from kivymd.uix.picker import MDDatePicker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
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

    def __init__(self, **kwargs):
        super(Connect_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        self.gender = 0

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

    def clear_register(self):
        self.ids.user_name.text=""
        self.ids.first_name.text=""
        self.ids.last_name.text=""
        self.ids.email.text=""
        self.ids.password.text=""
        self.ids.birth_date.text=""




    def unregister(self):
        print('unregister')
        ans = App.get_running_app().controller.unregister()

        if ans.res is True:
            self.parent.parent.back_to_main()

        print(ans.message)

    def register(self):
        user_name = self.ids.user_name.text
        first_name = self.ids.first_name.text
        last_name =  self.ids.last_name.text
        email = self.ids.email.text
        password =  self.ids.password.text
        birth_date = datetime.datetime(1996, 12, 15)
        # birth_date = self.ids.birth_date.text
        gender = self.gender
        ans = App.get_running_app().controller.register(first_name, last_name, user_name, email, password, birth_date,
                                                        gender)
        if ans.res is True:
            self.parent.parent.back_to_main()

        print(ans.message)



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

        print(ans.message)

    def clear_login(self):
        self.ids.log_in_username.text=""
        self.ids.log_in_password.text=""

    def logout(self):
        print("po")
        # user = App.get_running_app().controller.store['user']
        # user_info = user['user_info']
        # user_id = user_info['user_id']
        # print(user_id)
        ans = App.get_running_app().controller.logout()

        # after logout back to the main menu
        if ans.res is True:
            self.parent.parent.back_to_main()

        print(ans.message+"aaaaaa")

