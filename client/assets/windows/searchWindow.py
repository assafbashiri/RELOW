from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
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
        self.lab = MDLabel(text="")
        self.lab.size_hint_y = 0.4
        self.category_name = None
        self.dialog = None
        self.search_box = Search_box()

    def show_search_by(self):
        if 'search_box' not in self.ids.main_search.ids:
            self.ids.main_search.add_widget(self.search_box)
            self.ids.main_search.ids['search_box']=self.search_box

    def hide_search_by(self):
        self.ids.main_search.remove_widget(self.search_box)

    def search_by_name(self):
        if self.first_time_bad_search:
            pass
            # tempi = self.ids.search_box.ids.tempi
            # self.ids.search_box.remove_widget(tempi)
        #self.ids.search_box.remove_widget(self.lab)
        #self.ids.search_box.remove_widget(self.of)
        prod_name = self.ids.main_search.ids.search_box.ids.name.text
        ans = App.get_running_app().controller.get_offers_by_product_name(prod_name)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            self.lab.text = "We are sorry, we cant find offers for you"
            #self.ids.main_search.remove_widget(self.search_box)
            self.ids.main_search.add_widget(self.lab)
        # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.main_search.remove_widget(self.search_box)
            # remove the id from theids dict
            self.ids.main_search.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_company(self):
        if self.first_time_bad_search:
            tempi = self.ids.search_box.ids.tempi
            self.ids.search_box.remove_widget(tempi)
        self.ids.search_box.remove_widget(self.lab)
        self.ids.search_box.remove_widget(self.of)
        prod_company = self.ids.search_box.ids.company.text
        ans = App.get_running_app().controller.get_offers_by_product_company(prod_company)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            self.lab.text = "   We are sorry, we cant find offers for you"
            self.ids.search_box.add_widget(self.lab)
            # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.search_box.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_price(self):
        if self.first_time_bad_search:
            tempi = self.ids.search_box.ids.tempi
            self.ids.search_box.remove_widget(tempi)
        self.ids.search_box.remove_widget(self.lab)
        self.ids.search_box.remove_widget(self.of)
        prod_price = self.ids.search_box.ids.price.text
        if not prod_price.isnumeric():
            self.of.insert_offers(list=[])
            self.lab.text = "   We are sorry, price has to be number"
            self.ids.search_box.add_widget(self.lab)
            return
        ans = App.get_running_app().controller.get_offers_by_product_price(prod_price)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            self.lab.text = "   We are sorry, we cant find offers for you"
            self.ids.search_box.add_widget(self.lab)
            # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.search_box.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_end_date(self):
        if self.first_time_bad_search:
            tempi = self.ids.search_box.ids.tempi
            self.ids.search_box.remove_widget(tempi)
        self.ids.search_box.remove_widget(self.lab)
        self.ids.search_box.remove_widget(self.of)
        prod_date = self.ids.search_box.ids.date.text
        if not CheckValidity.checkEndDate(self, prod_date):
            self.of.insert_offers(list=[])
            self.lab.text = "   We are sorry, invalid end date"
            self.ids.search_box.add_widget(self.lab)
            return
        ans = App.get_running_app().controller.get_offers_by_product_end_date(prod_date)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            self.lab.text = "   We are sorry, we cant find offers for you"
            self.ids.search_box.add_widget(self.lab)
            # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.search_box.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_sub_category(self, cat_name, sub_cat_name):
        if self.first_time_bad_search:
            tempi = self.ids.search_box.ids.tempi
            self.ids.search_box.remove_widget(tempi)
        self.ids.search_box.remove_widget(self.lab)
        self.ids.search_box.remove_widget(self.of)
        ans = App.get_running_app().controller.get_offers_by_sub_category(cat_name,sub_cat_name)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            self.lab.text = sub_cat_name + " has 0 offers"
            self.ids.search_box.add_widget(self.lab)
        # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.search_box.add_widget(self.of)
        self.first_time_bad_search = False

    def search_by_category(self, cat_name):
        if self.first_time_bad_search:
            tempi = self.ids.search_box.ids.tempi
            self.ids.search_box.remove_widget(tempi)
        self.ids.search_box.remove_widget(self.lab)
        self.ids.search_box.remove_widget(self.of)
        ans = App.get_running_app().controller.get_offers_by_category(cat_name)
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            self.lab.text = cat_name + " has 0 offers"
            self.ids.search_box.add_widget(self.lab)
        # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.search_box.add_widget(self.of)
        self.first_time_bad_search = False







    def show_dropdown_search_by_category(self):
        categories = App.get_running_app().controller.get_categories()
        menu_items = []
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
        menu_items = []
        for cat in categories:
            menu_items.append(
                {"text": cat.name,
                 "viewclass": "OneLineListItem",
                 "on_release": lambda x=cat.get_sub_categories_names(), y=cat.name: self.show_dropdown_sub_category(x,
                                                                                                                    y),
                 }
            )

        self.drop_down_category = MDDropdownMenu(
            caller=self.ids.search_box.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_category.open()

    def show_dropdown_sub_category(self, sub_categories_names, cat_name):
        menu_items = []
        for sub_cat in sub_categories_names:
            menu_items.append(
                {"text": sub_cat,
                 "viewclass": "OneLineListItem",
                 # here we have to open page or the offers of this sub categories ya sharmutut
                 "on_release": lambda x=sub_cat, y=cat_name: self.on_save_sub_category(x, y)}
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


















        # self.ids.search_box.ids.helper.remove_widget(self.lab)
        # self.ids.search_box.ids.helper.remove_widget(self.of)
        #
        # ans = App.get_running_app().controller.get_offers_by_category(cat_name)
        # if len(ans) == 0:
        #     self.lab.text = cat_name + " has 0 offers"
        #     self.ids.search_box.ids.helper.add_widget(self.of)
        # else:
        #     self.of.insert_offers(list=ans)
        #     self.ids.search_box.ids.helper.add_widget(self.of)
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
