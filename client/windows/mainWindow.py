from datetime import datetime
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.event import EventDispatcher
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
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
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDIconButton
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
from windows.offerWindow import OfferScreen

from Utils.Utils import Utils


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class MENUScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(MENUScreen, self).__init__(**kwargs)


    def open_cat_drop(self):
        categories = self.get_all_categories()
        menu_items = []
        for cat in categories:
            menu_items.append(
                {
                    'text': cat.name,
                    "viewclass": "TwoLineListItem",
                    "on_release": lambda x=cat: self.open_offers_category(x),
                }
            )
            for sub_cat in cat.sub_categories_list_names:
                menu_items.append(
                    {
                        'text': sub_cat,
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=sub_cat: self.open_offers_category(x),
                    }
                )

        self.drop_down_cat = MDDropdownMenu(
            caller=self.ids.categories,
            items=menu_items,
            width_mult=10,

        )

        self.drop_down_cat.open()

    def get_all_categories(self):
        return App.get_running_app().controller.get_categories()
    def search_by_name(self):
        search_word = self.children[2].children[0].children[1].text
        App.get_running_app().root.screens[3].ids.side_box.children[0].children[1].text = search_word
        App.get_running_app().root.screens[3].search_by_prod_name(search_word)
        App.get_running_app().root.current = 'search_screen'


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



    def open_cat_drop(self):
        categories = self.get_all_categories()
        menu_items = []
        for cat in categories:
            menu_items.append(
                {
                    'text': cat.name,
                    "viewclass": "TwoLineListItem",
                    "on_release": lambda x=cat: self.open_offers_category(x),
                }
            )
            for sub_cat in cat.sub_categories_list_names:
                menu_items.append(
                    {
                        'text': sub_cat,
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=sub_cat: self.open_offers_category(x),
                    }
                )

        self.drop_down_cat = MDDropdownMenu(
            caller=self.ids.categories,
            items=menu_items,
            width_mult=10,

        )

        self.drop_down_cat.open()

    def get_all_categories(self):
        return App.get_running_app().controller.get_categories()

    def login_or_connect(self):
        # for the btn text
        controller = App.get_running_app().controller
        if controller.guest is True:
            return "CONNECT"
        else:
            return "LOGOUT"

    def logout_connect(self):
        # apply the method for the btn
        controller = App.get_running_app().controller
        if controller.guest is True:
            self.connect()
        else:
            self.logout()

    def show_user_name(self, name):
        self.ids.hello.text = name

    def get_user_name(self):
        answer = App.get_running_app().controller.user_service.first_name
        if answer is None:
            return "        Hello, "+"guest"
        return "        Hello, "+App.get_running_app().controller.user_service.first_name

    def connect(self):
        App.get_running_app().root.current = 'connect_screen'

    def close_offers_windows(self):
        screens = App.get_running_app().root.screens
        screen_name = 'offer_screen'
        counter = 0
        for screen in screens:
            if screen_name in screen.name and len(screen_name) != len(screen.name):
                screens.pop(counter)
            counter = counter + 1

    def logout(self):
        if App.get_running_app().controller.guest is True:
            Utils.pop(self, "guest cant logout", "alert")
            return
        ans = App.get_running_app().controller.logout()
        # after logout back to the main menu
        if ans.res is True:
            App.get_running_app().root.current = "menu_screen"
            if App.get_running_app().root is not None:
                self.update_hello_name("        Hello, " + "guest")
                self.update_connect_logout_btn_text("CONNECT")
                App.get_running_app().controller.guest_register()
                # this method is the solution for moving from buyer/viewer modes
                self.close_offers_windows()

    def update_connect_logout_btn_text(self, text):
        self.ids.logout_register.text = text

    def update_hello_name(self, msg):
        self.ids.hello.text = msg

class Category_box(BoxLayout):
    pass


class Sub_Category_box(BoxLayout):
    pass


class Down_menu(BoxLayout):
    def __init__(self, **kwargs):
        super(Down_menu, self).__init__(**kwargs)

    def move_to_contact_us(self):
        controller = App.get_running_app().controller
        if controller.guest is True:
            Utils.pop(self, 'guest cant go to contact us window', 'alert')
            return
        App.get_running_app().root.current = 'contact_us_screen'

    def move_to_add_offer(self):
        controller = App.get_running_app().controller
        if controller.guest is True:
            Utils.pop(self, 'guest cant go to add offer window', 'alert')
            # toast("guest cant go to add offer window")
            return
        if controller.seller == 0:
            App.get_running_app().root.current = 'seller_screen'
        else:
            App.get_running_app().root.current = 'add_offer_screen'

    def move_to_my_offers(self):
        App.get_running_app().root.current = 'my_offers_screen'

    def move_to_account(self):
        controller = App.get_running_app().controller
        if controller.guest is True:
            Utils.pop(self, 'guest cant go to account window', 'alert')
            # toast("guest cant go to account window")
            return
        App.get_running_app().root.current = 'account_screen'
        App.get_running_app().root.ids.account.ids.account_box.init_fields()

    def is_seller(self):
        seller = App.get_running_app().controller.user_service.seller
        if seller == 0:
            return 'BECOME A SELLER'
        else:
            return 'ADD OFFER'

    def move_to_search(self):
        App.get_running_app().root.current = 'search_screen'


class Main_page_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Main_page_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
    
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
        b = self.root.current_screen.ids.Main_page_box.ids.recycle1.insert_offers(
            list=App.get_running_app().controller.hot_deals)

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
            self.controller.store = JsonStore('hello.json')
            self.check_connection()


