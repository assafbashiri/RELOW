from tkinter import Button

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField

from admin.Utils.CheckValidity import CheckValidity


class PasswordScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'change_password_screen'
        super(PasswordScreen, self).__init__(**kwargs)


    def change_password(self):
        old_password = self.ids.old_password.text
        new_password1 = self.ids.new_password1.text
        new_password2 = self.ids.new_password2.text
        if old_password == "":
            toast("please enter old password")
            return
        if new_password1 == "":
            toast("please enter new password")
            return
            if new_password2 == "":
                toast("please enter new password again")
                return
        if new_password1 != new_password2:
            toast("your new password is not match")
            return
        if not CheckValidity.checkValidityPassword(self, new_password1):
            return
        ans = App.get_running_app().controller.update_password(old_password,new_password1)
        if ans.res is True:
            toast("your password has been successfully changed")
            self.back_to_account_window()
        else:
            toast(ans.message)

    def back_to_account_window(self):
        App.get_running_app().root.current = 'account_screen'


