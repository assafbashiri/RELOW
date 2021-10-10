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
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextFieldRound, MDTextField

from Utils.Utils import Utils
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
from windows.changePasswordWindow import PasswordScreen
from windows.sellerWindow import SellerScreen
from windows.paymentWindow import PAYMENTScreen
from windows.termsWindow import TERMSScreen
from windows.SideBar import SideBar
from windows.updateOfferWindow import UPDATEOFFERScreen

from Utils.Utils import Utils


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
        self.dialog = None

    #     self.bind(pos=self.update_rect, size=self.update_rect)
    #     self.rect = Rectangle(pos=self.pos, size=self.size)
    #
    # def update_rect(self, instance, value):
    #     self.rect.pos = self.pos
    #     self.rect.size = self.size

    def show_user_name(self, name):
        self.ids.hello.text = name

    def get_user_name(self):
        answer = App.get_running_app().controller.user_service.first_name
        if answer is None:
            return "        Hello, "+"guest"
        return "        Hello, "+App.get_running_app().controller.user_service.first_name


    def is_seller(self):
        seller = App.get_running_app().controller.user_service.seller
        if seller == 0:
            return 'BECOME A SELLER'
        else:
            return 'ADD OFFER'

    def move_to_account(self):
        a = App.get_running_app()
        b = a.controller
        if b.guest is True:
            Utils.pop(self, 'guest cant go to account window', 'alert')
            # toast("guest cant go to account window")
            return
        App.get_running_app().root.current = 'account_screen'
        App.get_running_app().root.ids.account.ids.account_box.ids.boxi.init_fields()

    def move_to_add_offer(self):
        a = App.get_running_app()
        b = a.controller
        if b.guest is True:
            Utils.pop(self, 'guest cant go to add offer window', 'alert')
            # toast("guest cant go to add offer window")
            return
        if b.seller == 0:
            App.get_running_app().root.current = 'seller_screen'
        else:
            App.get_running_app().root.current = 'add_offer_screen'



    def move_to_contact_us(self):
        a = App.get_running_app()
        b = a.controller
        if b.guest is True:
            Utils.pop(self, 'guest cant go to contact us window', 'alert')
            return
        App.get_running_app().root.current = 'contact_us_screen'

    def logout(self):
        ans = App.get_running_app().controller.logout()
        # after logout back to the main menu
        if ans.res is True:
            self.parent.parent.parent.back_to_main()
            if App.get_running_app().root is not None:
                self.update_hello_name("        Hello, " + "guest")

    def update_hello_name(self, msg):
        # menu screen 0
        App.get_running_app().root.screens[0].ids.menu_box.ids.side_box.ids.hello.text = msg
        # connect screen 1
        App.get_running_app().root.screens[1].children[0].ids.side_box.ids.hello.text = msg
        # account screen 2
        App.get_running_app().root.screens[2].children[0].ids.side_box.ids.hello.text = msg
        # search screen 3
        App.get_running_app().root.screens[3].children[0].ids.side_box.ids.hello.text = msg
        # add offer screen 4
        App.get_running_app().root.screens[4].children[0].ids.side_box.ids.hello.text = msg
        # my offers screen 5
        App.get_running_app().root.screens[5].children[0].ids.side_box.ids.hello.text = msg
        # update offers screen 6
        App.get_running_app().root.screens[6].children[0].ids.side_box.ids.hello.text = msg
        # register screen 7
        App.get_running_app().root.screens[7].ids.side_box.ids.hello.text = msg
        # login screen 8
        App.get_running_app().root.screens[8].ids.side_box.ids.hello.text = msg
        # # contact screen 9
        # App.get_running_app().root.screens[9].children[0].ids.side_box.ids.hello.text = msg
        # # confirmation screen 10
        # z = App.get_running_app().root.screens[10].children[0].ids.side_box.ids.hello.text = msg
        # # password screen 11
        # z = App.get_running_app().root.screens[11].children[0].ids.side_box.ids.hello.text = msg
        # seller screen 12
        App.get_running_app().root.screens[12].ids.side_box.ids.hello.text = msg



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
            email = user['email']
            password = user['password']
            # if answer is False?
            ans = self.controller.login_from_exist_user(email, password)
            print("welcome back")
        elif store.exists('user_guest'):
            guest = store.get('user_guest')
            guest_id = guest['user_id']
            self.controller.guest_login(guest_id)
        else:
            self.controller.guest_register()
            self.controller.guest_login(self.controller.user_service.user_id)
        if self.controller.user_service is None:
            print("login failed")
            f = open('hello.json', 'r+')
            f.truncate(0)
            self.check_connection()


