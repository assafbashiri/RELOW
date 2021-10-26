from tkinter import Button

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField

from assets.Utils.CheckValidity import CheckValidity
from assets.Utils.Utils import Utils


class SellerScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'seller_screen'
        super(SellerScreen, self).__init__(**kwargs)

    def become_seller(self):
        email = App.get_running_app().controller.user_service.email
        ans = App.get_running_app().controller.become_a_seller(email)
        if ans.res is True:
            App.get_running_app().controller.seller = True
            Utils.pop(self, 'welcome seller', 'success')
            self.back_to_main()
        else:
            Utils.pop(self, ans.message, 'alert')


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

    def back_to_main(self):
        App.get_running_app().root.current = 'menu_screen'
        a = App.get_running_app().root.screens[0].ids.Main_page_box.ids.side_box.ids.add_offer.text = 'ADD OFFER'
        b = 5

class seller_terms(Popup):
    def __init__(self, **kwargs):
        super(seller_terms, self).__init__(**kwargs)
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


