from tkinter import Label

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from Service.Object.UserService import UserService
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from windows.SideBar import SideBar
from datetime import datetime
from kivymd.toast import toast
import csv

from windows.offers_list import Offers_Screen

from Utils.CheckValidity import CheckValidity


class Category_box(BoxLayout):
    pass

class CONTACTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'contact_us_screen'
        super(CONTACTScreen, self).__init__(**kwargs)

class Contact_box1(BoxLayout):

    def __init__(self,**kwargs):
        super(Contact_box1, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    def exit(self):
        App.get_running_app().controller.exit()

    def change_to_cat(self):
        SideBar.change_to_cat(self)


class Sub_Category_box(BoxLayout):
    pass
class BoxiLayout1(BoxLayout):
    drop_down = ObjectProperty()

    def __init__(self, **kwargs):
        super(BoxiLayout1, self).__init__(**kwargs)
        self.flag = 1 # 1 - update personal details   2 - add address details   3- add payment method
        self.gender = 0
        self.controller = App.get_running_app().controller
        self.label = MDLabel(text="")


    def send(self):
        if self.controller.guest is True:
            toast("have to log in or register to contact us")
            return

        subject = self.ids.subject.text
        description = self.ids.description.text
        self.label.text = ""
        if subject == "":
            toast("please write a subject ")
            return
        if description == "":
            toast("please write a description")
            return

        ans = App.get_running_app().controller.contact_us(subject, description)
        if ans.res is True:
            toast("thank you for contact us, we will answer you soon via your mail")
            self.ids.subject.text = ""
            self.ids.description.text = ""
            App.get_running_app().root.current = 'menu_screen'


