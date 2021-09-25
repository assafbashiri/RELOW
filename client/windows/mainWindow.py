from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.event import EventDispatcher
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
# from kivy.config import Config
# Config.set('kivy', 'exit_on_escape', '0')
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextFieldRound, MDTextField

from windows.accountWindow import ACCOUNTScreen
from windows.connectWindow import CONNECTScreen
from windows.searchWindow import SEARCHScreen
from windows.registerWindow import REGISTERScreen
from windows.loginWindow import LOGINScreen
from windows.addofferWindow import ADDOFFERScreen
from windows.offers_list import RecycleViewRow
from windows.my_offersWindow import MY_OFFERS_Screen
from windows.contactWindow import CONTACTScreen
from windows.confirmationWindow import CONFIRMATIONScreen

from windows.SideBar import SideBar
from windows.updateOfferWindow import UPDATEOFFERScreen

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class MENUScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(MENUScreen, self).__init__(**kwargs)


class Manager(ScreenManager):
    # def __init__(self, **kwargs):
    #     self.name = 'home'
    #     super(Manager, self).__init__(**kwargs)
    #     self.add_widget(ADDOFFERScreen)
    def back_to_main(self):
        self.current = "menu_screen"


class Side_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Side_box, self).__init__(**kwargs)
    #     self.bind(pos=self.update_rect, size=self.update_rect)
    #     self.rect = Rectangle(pos=self.pos, size=self.size)
    #
    # def update_rect(self, instance, value):
    #     self.rect.pos = self.pos
    #     self.rect.size = self.size


    def move_to_account(self):
        a = App.get_running_app()
        b = a.controller
        if b.guest is True:
            toast("guest cant go to account window")
            return
        App.get_running_app().root.current = 'account_screen'
        App.get_running_app().root.ids.account.ids.account_box.ids.boxi.init_fields()

    def move_to_add_offer(self):
        a = App.get_running_app()
        b = a.controller
        if b.guest is True:
            toast("guest cant go to add offer window")
            return
        App.get_running_app().root.current = 'add_offer_screen'

    def move_to_contact_us(self):
        a = App.get_running_app()
        b = a.controller
        if b.guest is True:
            toast("guest cant go to contact us window")
            return
        App.get_running_app().root.current = 'contact_us_screen'


class Category_box(BoxLayout):
    pass


class Sub_Category_box(BoxLayout):
    pass


class Menu_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Menu_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    # def exit(self):
    #     self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())
    #     # App.get_running_app().controller.exit()
    # def insert_offers(self, **kwargs):
    #     a = 5
    #     self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

    def change_to_cat(self):
        SideBar.change_to_cat(self)

    def get_all_categories(self):
        App.get_running_app().controller.init_categories()


class TestApp(MDApp):
    title = "RecycleView Direct Test"

    def __init__(self, controller):
        super(TestApp, self).__init__()
        self.controller = controller

    def on_start(self):
        print(Clock.max_iteration)
        # Clock.max_iteration = 5000
        print(Clock.max_iteration)

        b = self.root.current_screen.ids.menu_box.ids.recycle1.insert_offers(
            list=App.get_running_app().controller.get_hot_deals())


    def on_stop(self):
        print('fuck we stoped')

    def build(self):
        self.check_connection()
        return Manager()

    def check_connection(self):
        store = self.controller.store
        if store.exists('user'):
            user = store.get('user')
            username = user['username']
            password = user['password']
            self.controller.login_from_exist_user(username, password)
            a = 8
            print("welcome back")
        elif store.exists('user_guest'):
            guest = store.get('user_guest')
            guest_id = guest['user_id']
            self.controller.guest_login(guest_id)
        else:
            self.controller.guest_register()
            self.controller.guest_login(self.controller.user_service.user_id)
