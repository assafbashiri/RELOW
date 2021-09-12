from datetime import datetime

from kivy.app import App
from kivy.core.image import Image
from kivy.event import EventDispatcher
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
from kivymd.uix.label import MDLabel
# from kivy.config import Config
# Config.set('kivy', 'exit_on_escape', '0')
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextFieldRound, MDTextField

from windows.accountWindow import ACCOUNTScreen
from windows.connectWindow import CONNECTScreen
from windows.searchWindow import SEARCHScreen
from windows.addofferWindow import ADDOFFERScreen
from windows.offers_list import RecycleViewRow
from windows.my_offersWindow import MY_OFFERS_Screen

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)




class MENUScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(MENUScreen, self).__init__(**kwargs)




class Manager(ScreenManager):
    screen_main = ObjectProperty(None)
    screen_account = ObjectProperty(None)
    screen_connect = ObjectProperty(None)
    screen_search = ObjectProperty(None)
    def back_to_main(self):
        self.current = "menu_screen"






class Side_box(BoxLayout):
    pass
class Category_box(BoxLayout):
    pass
class Sub_Category_box(BoxLayout):
    pass



class Menu_box(BoxLayout):
    def __init__(self,**kwargs):
        super(Menu_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
    def exit(self):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())
        # App.get_running_app().controller.exit()
    def insert_offers(self, **kwargs):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

    def change_to_cat(self):
        SideBar.change_to_cat(self)

    def change_to_sub_cat_tom(self, category_name_button, category):
        SideBar.change_to_sub_cat()





    def get_all_categories(self):
        App.get_running_app().controller.init_categories()



class TestApp(MDApp):
    title = "RecycleView Direct Test"
    def __init__(self, controller):
        super(TestApp, self).__init__()
        self.controller = controller

    def build(self):
        self.check_connection()
        return Manager()

    def check_connection(self):
        store = self.controller.store
        if store.exists('user'):
            user = store['user']['user_info']
            username = user['user_name']
            password = user['password']
            self.controller.login(username, password)
            print("welcome back")
        elif store.exists('user_guest'):
            guest = store['user_guest']['user_info']
            guest_id = guest['user_id']
            # guest_liked_offers = guest['liked_offers']
            self.controller.guest_login(guest_id)
        else:
            self.controller.guest_register()




