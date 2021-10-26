from kivy.app import App
from kivy.uix.screenmanager import Screen

from assets.Utils.CheckValidity import CheckValidity
from assets.Utils.Utils import Utils


class PasswordScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'change_password_screen'
        super(PasswordScreen, self).__init__(**kwargs)

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

    def back_to_account_window(self):
        App.get_running_app().root.current = 'account_screen'


