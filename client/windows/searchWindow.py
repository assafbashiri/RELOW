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

from client.windows.SideBar import SideBar
from client.windows.offers_list import Offers_Screen


class SEARCHScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'search_screen'
        super(SEARCHScreen, self).__init__(**kwargs)
        self.mes = BoxLayout(orientation='horizontal', size_hint_y=.2)
        self.of = Offers_Screen()
        self.first_time_bad_search = True
        self.first_time_good_search = True

    def search_by_name(self):
        prod_name = self.ids.name.text
        ans = App.get_running_app().controller.get_offers_by_product_name(prod_name)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text="cant find offer")
                self.mes.add_widget(self.lab)
                self.ids.zibi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = "cant find offer.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.zibi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)


    def search_by_sub_category(self):
        sub_cat_name = self.ids.sub_category.text
        # cat_name = self.ids.category.text
        cat_name = "sport"
        ans = App.get_running_app().controller.get_offers_by_sub_category(cat_name, sub_cat_name)

        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text=sub_cat_name+" has 0 offers")
                self.mes.add_widget(self.lab)
                self.ids.zibi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = sub_cat_name+" has 0 offers.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.zibi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)

    def search_by_category(self):
        cat_name = self.ids.category.text
        ans = App.get_running_app().controller.get_offers_by_category(cat_name)
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text=cat_name+" has 0 offers")
                self.mes.add_widget(self.lab)
                self.ids.zibi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = cat_name+" has 0 offers.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.zibi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)

class Search_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Search_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    def change_to_cat(self):
        self.side = self.children[0]
        self.remove_widget(self.side)
        self.add_widget(self.cat)
        # SideBar.change_to_cat(self)

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