from kivy.app import App
from kivy.uix.screenmanager import Screen
from assets.Utils.Utils import Utils

class CONFIRMATIONScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'confirmation_screen'
        super(CONFIRMATIONScreen, self).__init__(**kwargs)

    def complete_register(self):
        email = self.manager.ids.login.ids.login_box.ids.email.text
        password = self.manager.ids.login.ids.login_box.ids.password.text
        if email == '' and password == '':
            email = App.get_running_app().root.screens[6].children[0].children[0].ids.email_input.text
            password = App.get_running_app().root.screens[6].children[0].children[0].ids.password_input.text
        code = self.ids.code_input.text
        if code == '':
            Utils.pop(self, 'you need to insert code', 'alert')
            return
        else:
            ans = App.get_running_app().controller.complete_register(code, email)
            if ans.res is True:
                self.manager.change_screen("menu_screen")
                App.get_running_app().controller.login_from_exist_user(email, password)
                self.manager.ids.menu.ids.side_box.update_hello_name("        Hello, " + App.get_running_app().controller.user_service.first_name)
                self.manager.ids.menu.ids.side_box.update_connect_logout_btn_text("LOGOUT")
                App.get_running_app().root.screens[2].ids.account_box.ids.choose_box.children[0].init_account_window_fields()
                App.get_running_app().root.screens[0].ids.side_box.close_offers_windows()
            else:
                Utils.pop(self, "Incorrect code", 'alert')
                return
