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
        cat_lis = App.get_running_app().controller.categories
        self.categories = BoxLayout(orientation='vertical', size_hint=(.2 , .2), pos_hint={'top':1})
        for category in cat_lis:
            self.category_name = Button(text=category.name, on_press=lambda a:self.change_to_sub_cat_tom(self.category_name, category))
            self.categories.add_widget(self.category_name)




        self.side = self.ids.side_box
        self.remove_widget(self.side)
        self.add_widget(self.categories)
        # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
        # print(self.parent)
        # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)
    def change_to_sub_cat_tom(self, category_name_button, category):
        sub_category_names = category.get_sub_categories_names()

        for sub_category_name in sub_category_names:
            self.sub_category = Button(text=sub_category_name, on_press=lambda x:self.show_offers_for_sub_cat(category.name, sub_category_name))
            self.categories.add_widget(self.sub_category)

        self.categories.remove_widget(self.category_name)


    def show_offers_for_sub_cat(self,cat_name,  sub_cat_name):
        controller =  App.get_running_app().controller
        offers = controller.get_offers_by_sub_category(cat_name, sub_cat_name)
        a=6

    def back_to_menu(self):
        # self.remove_widget(self.ids.category_box)
        self.add_widget(self.side)
        self.remove_widget(self.cat)

    def back_to_cat(self):
        self.add_widget(self.cat)
        self.remove_widget(self.sub_cat)


    def get_all_categories(self):
        App.get_running_app().controller.init_categories()



class TestApp(MDApp):
    title = "RecycleView Direct Test"
    def __init__(self, controller):
        super(TestApp, self).__init__()
        self.controller = controller

    def build(self):
        #self.check_connection()
        return Manager()

    def check_connection(self):
        store = self.controller.store
        if store.exists('user'):
            user = store['user']['user_info']
            username = user['user_name']
            password = user['password']
            self.controller.login(username, password)
            print("welcome back")


