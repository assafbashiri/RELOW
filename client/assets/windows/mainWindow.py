from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
# from kivy.config import Config
# Config.set('kivy', 'exit_on_escape', '0')
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.popup import Popup
from kivy.core.window import Window
from assets.windows.SideBar import SideBar
from assets.windows.accountWindow import ACCOUNTScreen
from assets.windows.connectWindow import CONNECTScreen
from assets.windows.searchWindow import SEARCHScreen
from assets.windows.registerWindow import REGISTERScreen
from assets.windows.loginWindow import LOGINScreen
from assets.windows.addofferWindow import ADDOFFERScreen
from assets.windows.offers_list import RecycleViewRow
from assets.windows.my_offersWindow import MY_OFFERS_Screen
from assets.windows.contactWindow import CONTACTScreen
from assets.windows.confirmationWindow import CONFIRMATIONScreen
from assets.windows.changePasswordWindow import PasswordScreen
from assets.windows.sellerWindow import SellerScreen
from assets.windows.paymentWindow import PAYMENTScreen
from assets.windows.termsWindow import TERMSScreen
from assets.windows.updateOfferWindow import UPDATEOFFERScreen
from assets.windows.offerWindow import OfferScreen
from assets.Utils.Utils import Utils


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class MENUScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(MENUScreen, self).__init__(**kwargs)

    def get_all_categories(self):
        return App.get_running_app().controller.get_categories()

    def search_by_name(self):
        search_word = self.children[2].children[0].children[1].text
        App.get_running_app().root.screens[3].ids.side_box.children[0].children[1].text = search_word
        App.get_running_app().root.screens[3].search_by_prod_name(search_word)
        App.get_running_app().root.change_screen("search_screen")
        # App.get_running_app().root.current = 'search_screen'


class Manager(ScreenManager):
    def __init__(self, **kwargs):

        self.name = 'home'
        super(Manager, self).__init__(**kwargs)
        # self.add_widget(ADDOFFERScreen)
        self.screen_list = []

    def change_screen(self, next_screen):
        if App.get_running_app().root.current not in self.screen_list:
            self.screen_list.append(App.get_running_app().root.current)
        App.get_running_app().root.current = next_screen
        if next_screen == 'search_screen':
            SEARCHScreen.show_search_by(App.get_running_app().root.current_screen)

    def on_back_btn(self):

        if self.screen_list:
            App.get_running_app().root.current = self.screen_list.pop()

            return True
        return False

    def back_to_main(self):
        App.get_running_app().root.change_screen("menu_screen")


class Side_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Side_box, self).__init__(**kwargs)
        self.dialog = None
    def back_to_main(self):
        App.get_running_app().root.change_screen("menu_screen")

    def open_cat_drop(self):
        categories = self.get_all_categories()
        cat_grid = GridLayout(cols=1, size_hint=(.8, .8), pos_hint={'top': 1})
        categories_names = GridLayout(cols=len(categories), size_hint_y=.3)
        max_sub_cat = 0
        for cat in categories:
            categories_names.add_widget(Button(text=cat.name, size_hint=(.3, .3), color=(1, 1, 1, 1),
                                               background_color=(24 / 255, 211 / 255, 199 / 255, 1),
                                               on_press=lambda x=cat: self.open_offers_category(x)))
            if (len(cat.sub_categories_list_names) > max_sub_cat):
                max_sub_cat = len(cat.sub_categories_list_names)
        cat_grid.add_widget(categories_names)
        sub_cat_names = GridLayout(cols=len(categories))
        for cat in categories:
            one_cat_grid = GridLayout(cols=1)
            for sub_cat in cat.sub_categories_list_names:
                one_cat_grid.add_widget(Button(pos_hint={'top': 1}, background_color=(0, 0, 0, 0), text=sub_cat,
                                               on_press=lambda x=sub_cat, y=cat: self.open_offers_sub_category(x, y)))
            for i in range(0, max_sub_cat - len(cat.sub_categories_list_names)):
                one_cat_grid.add_widget(GridLayout(cols=1))
            sub_cat_names.add_widget(one_cat_grid)
        cat_grid.add_widget(sub_cat_names)
        self.popup = Popup(title="Categories",title_align='center',title_size='18sp', content=cat_grid, background_color=(1, 1, 1, 1), size_hint=(.8, .8))
        self.popup.open()

    def open_offers_category(self, cat_button):
        self.popup.dismiss()
        App.get_running_app().root.change_screen("search_screen")
        SEARCHScreen.search_by_category(App.get_running_app().root.current_screen, cat_button.text)

    def open_offers_sub_category(self, sub_cat_button, cat):
        self.popup.dismiss()
        App.get_running_app().root.change_screen("search_screen")
        # App.get_running_app().root.current = "search_screen"
        SEARCHScreen.search_by_sub_category(App.get_running_app().root.current_screen, cat.name, sub_cat_button.text)

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
            return "        Hello, " + "guest"
        return "        Hello, " + App.get_running_app().controller.user_service.first_name

    def connect(self):
        App.get_running_app().root.change_screen("connect_screen")
        # App.get_running_app().root.current = 'connect_screen'

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

            App.get_running_app().root.change_screen("menu_screen")
            # App.get_running_app().root.current = "menu_screen"
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

    def move_to_terms(self):
        App.get_running_app().root.change_screen('terms_screen')


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
        App.get_running_app().root.change_screen("contact_us_screen")
        # App.get_running_app().root.current = 'contact_us_screen'

    def move_to_add_offer(self):
        controller = App.get_running_app().controller
        if controller.guest is True:
            Utils.pop(self, 'guest cant go to add offer window', 'alert')
            # toast("guest cant go to add offer window")
            return
        if controller.seller == 0:
            App.get_running_app().root.change_screen("seller_screen")
            # App.get_running_app().root.current = 'seller_screen'
        else:
            App.get_running_app().root.change_screen("add_screen")

    def move_to_my_offers(self):
        App.get_running_app().root.change_screen("my_offers_screen")
        # App.get_running_app().root.current = 'my_offers_screen'

    def move_to_account(self):
        controller = App.get_running_app().controller
        if controller.guest is True:
            Utils.pop(self, 'guest cant go to account window', 'alert')
            # toast("guest cant go to account window")
            return
        App.get_running_app().root.change_screen("account_screen")
        # App.get_running_app().root.current = 'account_screen'
        App.get_running_app().root.ids.account.ids.account_box.init_fields()

    def is_seller(self):
        seller = App.get_running_app().controller.user_service.seller
        if seller == 0:
            return 'BECOME A SELLER'
        else:
            return 'ADD OFFER'

    def move_to_search(self):
        App.get_running_app().root.change_screen("search_screen")

    def back_to_main(self):
        App.get_running_app().root.change_screen("menu_screen")


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
        Window.bind(on_keyboard=self.on_back_btn)

    def on_back_btn(self, window, key, *args):
        if key in [27, 1001]:
            return self.root.on_back_btn()

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
            f = open('assets/hello.json', 'r+')
            f.truncate(0)
            self.controller.store = JsonStore('assets/hello.json')
            self.check_connection()
