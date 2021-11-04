from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from assets.Utils.Utils import Utils
from assets.windows.SideBar import SideBar
from assets.windows.offers_list import Offers_Screen

from assets.Utils.CheckValidity import CheckValidity


class SEARCHScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'search_screen'
        super(SEARCHScreen, self).__init__(**kwargs)
        self.mes = BoxLayout(orientation='horizontal', size_hint_y=.2)
        self.of = Offers_Screen(size_hint_y=0.4)
        self.first_time_bad_search = True
        self.lab = MDLabel(text="",size_hint_y = 0.009)
        self.lab.background_normal = ''
        self.lab.background_color = (24 / 255, 211 / 255, 199 / 255, 1)
        self.category_name = None
        self.dialog = None
        self.search_box = Search_box()
        self.show_search_by()


    def show_search_by(self):
        if len(self.ids)>0 and 'search_box' not in self.ids.main_search.ids:
            self.ids.main_search.clear_widgets()
            self.ids.main_search.add_widget(self.search_box)
            self.ids.main_search.ids['search_box']=self.search_box




    def search_by_name(self):
        prod_name = self.ids.main_search.ids.search_box.ids.name.text
        ans = App.get_running_app().controller.get_offers_by_product_name(prod_name)
        # bad search
        if len(ans) == 0:
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = "We are sorry, we cant find offers for you"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"]=self.lab
        # good search
        else:
            if "lab" in self.ids.main_search.ids:
                self.ids.main_search.remove_widget(self.lab)
                self.ids.main_search.ids.pop('lab', None)
            self.of.insert_offers(list=ans)
            self.ids.main_search.remove_widget(self.search_box)
            self.ids.main_search.ids.pop('search_box',None)
            self.ids.main_search.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_company(self):
        prod_company = self.ids.main_search.ids.search_box.ids.company.text
        ans = App.get_running_app().controller.get_offers_by_product_company(prod_company)
        # bad search
        if len(ans) == 0:
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = "   We are sorry, we cant find offers for you"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"] = self.lab
            # good search
        else:
            if "lab" in self.ids.main_search.ids:
                self.ids.main_search.remove_widget(self.lab)
                self.ids.main_search.ids.pop('lab', None)
            self.of.insert_offers(list=ans)
            self.ids.main_search.remove_widget(self.search_box)
            self.ids.main_search.ids.pop('search_box', None)
            self.ids.main_search.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_price(self):
        prod_price = self.ids.main_search.ids.price.text
        if not prod_price.isnumeric():
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = "   We are sorry, price has to be number"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"]=self.lab
            return
        ans = App.get_running_app().controller.get_offers_by_product_price(prod_price)
        # bad search
        if len(ans) == 0:
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = "   We are sorry, we cant find offers for you"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"]=self.lab
            # good search
        else:
            if "lab" in self.ids.main_search.ids:
                self.ids.main_search.remove_widget(self.lab)
                self.ids.main_search.ids.pop('lab', None)
            self.of.insert_offers(list=ans)
            self.ids.main_search.remove_widget(self.search_box)
            self.ids.main_search.ids.pop('search_box', None)
            self.ids.main_search.add_widget(self.of)

        self.first_time_bad_search = False

    def search_by_end_date(self):
        prod_date = self.ids.main_search.ids.date.text
        if not CheckValidity.checkEndDate(self, prod_date):
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = "   We are sorry, invalid end date"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"] = self.lab
            return
        ans = App.get_running_app().controller.get_offers_by_product_end_date(prod_date)
        # bad search
        if len(ans) == 0:
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = "   We are sorry, we cant find offers for you"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"]=self.lab

            # good search
        else:
            if "lab" in self.ids.main_search.ids:
                self.ids.main_search.remove_widget(self.lab)
                self.ids.main_search.ids.pop('lab', None)
            self.of.insert_offers(list=ans)
            self.ids.main_search.remove_widget(self.search_box)
            self.ids.main_search.ids.pop('search_box', None)
            self.ids.main_search.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_sub_category(self, cat_name, sub_cat_name):
        ans = App.get_running_app().controller.get_offers_by_sub_category(cat_name,sub_cat_name)
        # bad search
        if len(ans) == 0:
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = sub_cat_name + " has 0 offers"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"]=self.lab

        # good search
        else:
            if "lab" in self.ids.main_search.ids:
                self.ids.main_search.remove_widget(self.lab)
                self.ids.main_search.ids.pop('lab', None)
            self.of.insert_offers(list=ans)
            self.ids.main_search.ids.pop('search_box', None)
            self.ids.main_search.remove_widget(self.search_box)
            self.ids.main_search.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_category(self, cat_name):
        ans = App.get_running_app().controller.get_offers_by_category(cat_name)
        # bad search
        if len(ans) == 0:
            if "lab" not in self.ids.main_search.ids:
                self.lab.text = cat_name + " has 0 offers"
                self.ids.main_search.add_widget(self.lab)
                self.ids.main_search.ids["lab"]=self.lab

        # good search
        else:
            if "lab" in self.ids.main_search.ids:
                self.ids.main_search.remove_widget(self.lab)
                self.ids.main_search.ids.pop('lab', None)
            self.of.insert_offers(list=ans)
            self.ids.main_search.ids.pop('search_box', None)
            self.ids.main_search.remove_widget(self.search_box)
            self.ids.main_search.add_widget(self.of)
        self.first_time_bad_search = False











class Main_search_window(BoxLayout):
    pass
class Top_menu_box(BoxLayout):
    def back(self):
        App.get_running_app().root.change_screen("menu_screen")
        #App.get_running_app().root.current = "menu_screen"
class Search_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Search_box, self).__init__(**kwargs)
        self.name = 'search_box'
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    def change_to_cat(self):
        SideBar.change_to_cat(self)






class Offers_drop(BoxLayout):
    pass
class Sub_Category_box(BoxLayout):
    pass


class Category_box(BoxLayout):
    pass
