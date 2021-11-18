# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivymd.uix.label import MDLabel
# from assets.windows.offers_list import Offers_Screen
#
#
#
#
#
#
# class SideBar:
#
#
#     def change_to_cat(self):
#         self.of = Offers_Screen()
#         self.first_time_bad_search = True
#         self.first_time_good_search = True
#         self.back_to_main = Button(text="Back To Main",on_press=lambda a:SideBar.back_to_main(self))
#         cat_list = App.get_running_app().controller.categories
#         self.categories = BoxLayout(orientation='vertical', size_hint=(.2, .2), pos_hint={'top': 1})
#         cat_list_names={}
#         for category in cat_list:
#             cat_list_names[category.name]=category.get_sub_categories_names()
#         for cat_name in cat_list_names:
#             bt1 = Button(text=cat_name,on_press= lambda x=cat_list_names[cat_name], y=cat_name, z=cat_list : SideBar.change_to_sub_cat(self, x,y, z))
#             self.categories.add_widget(bt1)
#
#
#         self.categories.add_widget(self.back_to_main)
#         self.side = self.ids.side_box
#         self.remove_widget(self.side)
#         self.add_widget(self.categories)
#         # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
#         # print(self.parent)
#         # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)
#
#
#
#     def change_to_sub_cat(self, sub_cat_list, cat_name, cat_list):
#         a=6
#         sub_cat_names = SideBar.get_sub_categories(cat_list, cat_name)
#         self.categories.clear_widgets()
#         self.categories.add_widget(MDLabel(text=cat_name))
#         back_to_main = Button(text="Back To Category", on_press=lambda a:SideBar.back_to_category(self, cat_list))
#         for sub_category_name in sub_cat_names:
#             bt1 = Button(text=sub_category_name,on_press= lambda x=sub_category_name,z=cat_name, y=sub_category_name: SideBar.show_offers_for_sub_cat(self, x,z, y))
#             self.categories.add_widget(bt1)
#
#         self.categories.add_widget(back_to_main)
#
#     def get_sub_categories(cat_list, cat_name):
#         for cat in cat_list:
#             if cat.name == cat_name:
#                 return cat.get_sub_categories_names()
#
#     def show_offers_for_sub_cat(self,bt1, cat_name, sub_cat_name):
#         offers = App.get_running_app().controller.get_offers_by_sub_category(cat_name, sub_cat_name)
#
#         parent = self.parent
#         #parent.remove_widget(self)
#         self.clear_widgets()
#         if len(offers) == 0:
#             self.of.insert_offers(list=[])
#             if self.first_time_bad_search is True:
#                 self.lab = MDLabel(text=cat_name+" has 0 offers")
#                 #self.add_widget(self.of)
#                 self.add_widget(self.lab)
#                 self.add_widget(self.side)
#                 self.first_time_bad_search = False
#             else:
#                 self.lab.text = cat_name+" has 0 offers.."
#         # good search
#         else:
#             if self.first_time_bad_search is False:
#                 self.lab.text = ""
#             if self.first_time_good_search is True:
#                 self.of.insert_offers(list=offers)
#                 #self.parent.add_widget(self.of)
#                 self.add_widget(self.of)
#                 self.add_widget(self.side)
#                 self.first_time_good_search = False
#             else:
#                 self.of.insert_offers(list=offers)
#
#     def back_to_main(self):
#         self.remove_widget(self.categories)
#         self.add_widget(self.side)
#
#
#     def back_to_category(self, cat_list):
#         self.categories.clear_widgets()
#         cat_list_names = {}
#         for category in cat_list:
#             cat_list_names[category.name] = category.get_sub_categories_names()
#
#         for cat_name in cat_list_names:
#             bt1 = Button(text=cat_name,on_press= lambda x=cat_list_names[cat_name], y=cat_name, z=cat_list : SideBar.change_to_sub_cat(self, x,y, z))
#             self.categories.add_widget(bt1)
#
#         self.categories.add_widget(self.back_to_main)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # class SideBar:
# #     def change_to_cat(self):
# #         self.back_to_main = Button(text="Back To Main",on_press=lambda a:SideBar.back_to_main(self))
# #         cat_list = App.get_running_app().controller.categories
# #         self.categories = BoxLayout(orientation='vertical', size_hint=(.2, .2), pos_hint={'top': 1})
# #         cat_list_names={}
# #         for category in cat_list:
# #             cat_list_names[category.name]=category.get_sub_categories_names()
# #
# #         for cat_name in cat_list_names:
# #             bt1 = Button(text=cat_name,on_press=partial(SideBar.change_to_sub_cat,self,cat_list_names[cat_name], cat_list, cat_name))
# #             self.categories.add_widget(bt1)
# #
# #
# #
# #
# #         self.categories.add_widget(self.back_to_main)
# #         self.side = self.ids.side_box
# #         self.remove_widget(self.side)
# #         self.add_widget(self.categories)
# #         # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
# #         # print(self.parent)
# #         # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)
# #
# #
# #     def change_to_sub_cat(*args):
# #         a=6
# #         cat = args[0]
# #         cat.categories.clear_widgets()
# #         back_to_main = Button(text="Back To Category", on_press=lambda a: SideBar.back_to_category(args))
# #
# #         for sub_category_name in args[1]:
# #             bt1 = Button(text=sub_category_name,on_press=partial(SideBar.show_offers_for_sub_cat,args, sub_category_name))
# #             cat.categories.add_widget(bt1)
# #
# #         cat.categories.add_widget(back_to_main)
# #
# #
# #
# #     def show_offers_for_sub_cat(*args):
# #         controller = App.get_running_app().controller
# #         cat_name = args[0][3]
# #         sub_cat_name = args[1]
# #
# #         offers = controller.get_offers_by_sub_category(cat_name, sub_cat_name)
# #         a = 6
# #
# #     def back_to_main(self):
# #         self.remove_widget(self.categories)
# #         self.add_widget(self.side)
# #
# #
# #     def back_to_category(args):
# #         cat = args[0]
# #         cat.categories.clear_widgets()
# #         cat_list=args[2]
# #         cat_list_names = {}
# #         for category in cat_list:
# #             cat_list_names[category.name] = category.get_sub_categories_names()
# #
# #         for cat_name in cat_list_names:
# #             bt1 = Button(text=cat_name, on_press=partial(SideBar.change_to_sub_cat, cat, cat_list_names[cat_name], cat_list))
# #             cat.categories.add_widget(bt1)
# #
# #         cat.categories.add_widget(cat.back_to_main)
#
