from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from assets.Utils.CheckValidity import CheckValidity
from assets.Utils.Utils import Utils

class LOGINScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'login_screen'
        super(LOGINScreen, self).__init__(**kwargs)


class Login_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Login_box, self).__init__(**kwargs)

    def back(self):
        App.get_running_app().root.change_screen("connect_screen")

    def move_to_register(self):
        App.get_running_app().root.change_screen("register_screen")

    def exit(self):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

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
                self.clear_login()
                App.get_running_app().root.screens[0].ids.side_box.close_offers_windows()

        else:
            if ans.message == "user is not active":
                App.get_running_app().root.change_screen("confirmation_screen")
            if ans.message == "there is no such an email address in the system":
                Utils.pop(self, "there is no such an email address in the system", "alert")
            if ans.message == "incorrect Password":
                Utils.pop(self, "incorrect Password", "alert")

    def clear_login(self):
        self.ids.email.text = ""
        self.ids.password.text = ""

    def forgot_password(self):
        email = self.ids.email.text
        ans = App.get_running_app().controller.forget_password(email)
        if ans.res is True:
            Utils.pop(self, "your new password send to your mail", 'alert')
        else:
            Utils.pop(self, "the email is not exist in out system", 'alert')

    def update_connect_logout_btn_text(self, text):
        App.get_running_app().root.screens[0].ids.side_box.ids.logout_register.text = text

    def update_hello_name(self, msg):
        App.get_running_app().root.screens[0].ids.side_box.ids.hello.text = msg

    def back_to_menu(self):
        App.get_running_app().root.change_screen("menu_screen")


class txt(TextInput):

    runner = 0

    # def insert_text(self,string, a):
    #     self.runner +=1
    #     self.text = string +  self.text
    #     self.cursor = (0,0)
    #     # return super(txt, self).insert_text(string, from_undo=False)
    #
    # def do_backspace(self,from_undo=False, mode='bkspc'):
    #     self.text = self.text[1:]
    #     self.cursor = (0, 0)