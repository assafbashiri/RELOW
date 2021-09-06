from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField
from windows.offers_list import RecycleViewRow


class SEARCHScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'search_screen'
        super(SEARCHScreen, self).__init__(**kwargs)




    def search_by_name(self):
        prod_name = "shoko"
        ans = App.get_running_app().controller.get_offers_by_product_name(prod_name)
        self.insert_offers(list=ans)

    def search_by_sub_category(self):
        cat_name = "sport"
        sub_cat_name = "swim"
        # cat_name = self.ids.zibi.ids.name
        # sub_cat_name = self.ids.zibi.ids.name
        ans = App.get_running_app().controller.get_offers_by_sub_category(cat_name, sub_cat_name)
        self.insert_offers(list=ans)

    def search_by_category(self):
        cat_name = "sport"
        # cat_name = self.ids.zibi.ids.name
        ans = App.get_running_app().controller.get_offers_by_category(cat_name)
        self.insert_offers(list=ans)


class Search_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Search_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    def change_to_cat(self):
        self.side = self.children[0]
        self.remove_widget(self.side)
        self.add_widget(self.cat)

    def back_to_menu(self):
        self.add_widget(self.side)
        self.remove_widget(self.cat)

    def change_to_sub_cat(self):
        self.remove_widget(self.cat)
        self.add_widget(self.sub_cat)

    def back_to_cat(self):
        self.add_widget(self.cat)
        self.remove_widget(self.sub_cat)

class Sub_Category_box(BoxLayout):
    pass


class Category_box(BoxLayout):
    pass