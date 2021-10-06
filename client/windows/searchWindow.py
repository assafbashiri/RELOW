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
from windows.SideBar import SideBar
from kivymd.uix.menu import MDDropdownMenu
from Utils.Utils import Utils
from windows.SideBar import SideBar
from windows.offers_list import Offers_Screen


class SEARCHScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'search_screen'
        super(SEARCHScreen, self).__init__(**kwargs)
        self.mes = BoxLayout(orientation='horizontal', size_hint_y=.2)
        self.of = Offers_Screen(size_hint_y= 2)
        self.first_time_bad_search = True
        self.first_time_good_search = True
        self.lab = MDLabel(text="")
        self.category_name= None
        self.dialog = None

    def search_by_name(self):
        self.ids.search_box.ids.helper.remove_widget(self.lab)
        self.ids.search_box.ids.helper.remove_widget(self.of)
        prod_name = self.ids.search_box.ids.name.text
        ans = App.get_running_app().controller.get_offers_by_product_name(prod_name)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            # if self.first_time_bad_search is True:
            self.lab.text = "cant find offer"
            # self.mes.add_widget(self.lab)
            self.ids.search_box.ids.helper.add_widget(self.lab)
                # self.first_time_bad_search = False
            # else:
            #     self.lab.text = "cant find offer.."
        # good search
        else:
            # if self.first_time_bad_search is False:

            # if self.first_time_good_search is True:
            self.of.insert_offers(list=ans)
            self.ids.search_box.ids.helper.add_widget(self.of)
            # self.first_time_good_search = False
            # else:
            #     self.of.insert_offers(list=ans)

    def search_by_company(self):
        self.ids.search_box.ids.helper.remove_widget(self.lab)
        self.ids.search_box.ids.helper.remove_widget(self.of)
        prod_company = self.ids.search_box.ids.company.text
        ans = App.get_running_app().controller.get_offers_by_product_company(prod_company)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            # if self.first_time_bad_search is True:
            self.lab.text = "cant find offer"
            # self.mes.add_widget(self.lab)
            self.ids.search_box.ids.helper.add_widget(self.lab)
            # self.first_time_bad_search = False
            # else:
            #     self.lab.text = "cant find offer.."
        # good search
        else:
            # if self.first_time_bad_search is False:

            # if self.first_time_good_search is True:
            self.of.insert_offers(list=ans)
            self.ids.search_box.ids.helper.add_widget(self.of)
            # self.first_time_good_search = False
            # else:
            #     self.of.insert_offers(list=ans)

    def search_by_sub_category(self):
        self.ids.search_box.ids.helper.remove_widget(self.lab)
        self.ids.search_box.ids.helper.remove_widget(self.of)
        sub_cat_name = self.ids.search_box.ids.drop_sub_category.text
        # cat_name = self.ids.category.text
        if self.category_name is None:
            Utils.pop(self, 'have to choose sub category', 'alert')
            return
        cat_name = self.category_name
        ans = App.get_running_app().controller.get_offers_by_sub_category(cat_name, sub_cat_name)

        if len(ans) == 0:
            # self.of.insert_offers(list=[])
            # if self.first_time_bad_search is True:
            self.lab.text = sub_cat_name+" has 0 offers"
                # self.mes.add_widget(self.lab)
            self.ids.search_box.ids.helper.add_widget(self.lab)
            # self.first_time_bad_search = False
            # else:
            #     self.lab.text = sub_cat_name+" has 0 offers.."
        # good search
        else:
            # if self.first_time_bad_search is False:
            #     self.lab.text = ""
            # if self.first_time_good_search is True:
            self.of.insert_offers(list=ans)
            self.ids.search_box.ids.helper.add_widget(self.of)
                # self.first_time_good_search = False
            # else:
            #     self.of.insert_offers(list=ans)

    def show_dropdown_search_by_category(self):
        categories = App.get_running_app().controller.get_categories()
        menu_items=[]
        for cat in categories:
            menu_items.append(
                {"text": cat.name,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=cat.name: self.on_save_category(x),
                }
            )

        self.drop_down_category = MDDropdownMenu(
            caller=self.ids.search_box.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_category.open()

    def show_dropdown_category(self):
        categories = App.get_running_app().controller.get_categories()
        menu_items=[]
        for cat in categories:
            menu_items.append(
                {"text": cat.name,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=cat.get_sub_categories_names(), y=cat.name: self.show_dropdown_sub_category(x, y),
                }
            )

        self.drop_down_category = MDDropdownMenu(
            caller=self.ids.search_box.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_category.open()
    def show_dropdown_sub_category(self, sub_categories_names,cat_name):
        menu_items = []
        for sub_cat in sub_categories_names:
            menu_items.append(
                {"text": sub_cat,
                 "viewclass": "OneLineListItem",
                 # here we have to open page or the offers of this sub categories ya sharmutut
                 "on_release": lambda x=sub_cat, y=cat_name: self.on_save_sub_category(x, y) }
            )
        self.drop_down_sub_category = MDDropdownMenu(
            caller=self.ids.search_box.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_sub_category.open()
        self.drop_down_category.dismiss()
    def on_save_sub_category(self, sub_cat, cat_name):
        self.category_name = cat_name
        self.ids.search_box.ids.drop_sub_category.text = sub_cat
        self.drop_down_sub_category.dismiss()
    def on_save_category(self, sub_cat):
        self.ids.search_box.ids.drop_category.text = sub_cat
        self.drop_down_category.dismiss()

    def search_by_category(self):
        self.ids.search_box.ids.helper.remove_widget(self.lab)
        self.ids.search_box.ids.helper.remove_widget(self.of)
        cat_name = self.ids.search_box.ids.drop_category.text
        #if cat_name not in App.get_running_app().controller.get_categories().keys():
        if cat_name == 'search by category':
            Utils.pop(self, 'have to choose category')
            return
        ans = App.get_running_app().controller.get_offers_by_category(cat_name)
        if len(ans) == 0:
            # self.of.insert_offers(list=[])
            # if self.first_time_bad_search is True:
            self.lab.text = cat_name+" has 0 offers"
                # self.mes.add_widget(self.lab)
            self.ids.search_box.ids.helper.add_widget(self.of)
            # self.first_time_bad_search = False
            # else:
            #     self.lab.text = cat_name+" has 0 offers.."
        # good search
        else:
            # if self.first_time_bad_search is False:
            #     self.lab.text = ""
            # if self.first_time_good_search is True:
            self.of.insert_offers(list=ans)
            self.ids.search_box.ids.helper.add_widget(self.of)
                # self.first_time_good_search = False
            # else:
            #     self.of.insert_offers(list=ans)

class Search_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Search_box, self).__init__(**kwargs)
        self.name = 'search_box'
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    def change_to_cat(self):
        SideBar.change_to_cat(self)

class Sub_Category_box(BoxLayout):
    pass

class Category_box(BoxLayout):
    pass
