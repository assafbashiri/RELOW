from functools import partial
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






class SideBar:
    def change_to_cat(self):
        self.back_to_main = Button(text="Back To Main",on_press=lambda a:SideBar.back_to_main(self))
        cat_list = App.get_running_app().controller.categories
        self.categories = BoxLayout(orientation='vertical', size_hint=(.2, .2), pos_hint={'top': 1})
        cat_list_names={}
        for category in cat_list:
            cat_list_names[category.name]=category.get_sub_categories_names()

        for cat_name in cat_list_names:
            bt1 = Button(text=cat_name,on_press=partial(SideBar.change_to_sub_cat,self,cat_list_names[cat_name], cat_list, cat_name))
            self.categories.add_widget(bt1)


        self.categories.add_widget(self.back_to_main)
        self.side = self.ids.side_box
        self.remove_widget(self.side)
        self.add_widget(self.categories)
        # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
        # print(self.parent)
        # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)


    def change_to_sub_cat(*args):
        a=6
        cat = args[0]
        cat.categories.clear_widgets()
        back_to_main = Button(text="Back To Category", on_press=lambda a: SideBar.back_to_category(args))

        for sub_category_name in args[1]:
            bt1 = Button(text=sub_category_name,on_press=partial(SideBar.show_offers_for_sub_cat,args, sub_category_name))
            cat.categories.add_widget(bt1)

        cat.categories.add_widget(back_to_main)



    def show_offers_for_sub_cat(*args):
        controller = App.get_running_app().controller
        cat_name = args[0][3]
        sub_cat_name = args[1]
        offers = controller.get_offers_by_sub_category(cat_name, sub_cat_name)
        a = 6

    def back_to_main(self):
        self.remove_widget(self.categories)
        self.add_widget(self.side)


    def back_to_category(args):
        cat = args[0]
        cat.categories.clear_widgets()
        cat_list=args[2]
        cat_list_names = {}
        for category in cat_list:
            cat_list_names[category.name] = category.get_sub_categories_names()

        for cat_name in cat_list_names:
            bt1 = Button(text=cat_name, on_press=partial(SideBar.change_to_sub_cat, cat, cat_list_names[cat_name], cat_list))
            cat.categories.add_widget(bt1)

        cat.categories.add_widget(cat.back_to_main)
