from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from assets.windows.SideBar import SideBar

from assets.windows.offers_list import Offers_Screen


class MY_OFFERS_Screen(Screen):
    def __init__(self, **kwargs):
        self.name = 'my_offers_screen'
        super(MY_OFFERS_Screen, self).__init__(**kwargs)
        self.mes = BoxLayout(orientation='vertical')
        self.lab = MDLabel(text='')
        self.of = Offers_Screen()
        self.first_time_bad_search = True
        self.first_time_good_search = True

    def active_buy(self):
        self.ids.offers_box.ids.offi.remove_widget(self.lab)
        self.ids.offers_box.ids.offi.remove_widget(self.of)
        ans = App.get_running_app().controller.get_all_active_buy_offers()
        self.set_btn_colors()
        self.ids.offers_box.ids.buttons.children[0].children[0].children[4].color = [24/255,211/255,199/255,1]

        # bad search
        if len(ans) == 0:
            toast("0 active buy offers")
        # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.offers_box.ids.offi.add_widget(self.of)

    def active_sell(self):
        self.ids.offers_box.ids.offi.remove_widget(self.lab)
        self.ids.offers_box.ids.offi.remove_widget(self.of)
        ans = App.get_running_app().controller.get_all_active_sell_offers()
        self.set_btn_colors()
        self.ids.offers_box.ids.buttons.children[0].children[0].children[3].color = [24/255,211/255,199/255,1]

        # bad search
        if len(ans) == 0:
            toast("0 active sell offers")
        # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.offers_box.ids.offi.add_widget(self.of)

    def like_offers(self):
        self.ids.offers_box.ids.offi.remove_widget(self.lab)
        self.ids.offers_box.ids.offi.remove_widget(self.of)
        ans = App.get_running_app().controller.get_all_liked_offers()
        self.set_btn_colors()
        self.ids.offers_box.ids.buttons.children[0].children[0].children[2].color = [24/255,211/255,199/255,1]

        # bad search
        if len(ans) == 0:
            toast("0 liked offers")
        # good search
        else:
            self.of.insert_offers(list=ans)
            self.of.size_hint = 1,.5
            self.ids.offers_box.ids.offi.add_widget(self.of)

    def history_buy(self):
        self.ids.offers_box.ids.offi.remove_widget(self.lab)
        self.ids.offers_box.ids.offi.remove_widget(self.of)
        ans = App.get_running_app().controller.get_all_history_buy_offers()
        self.set_btn_colors()
        self.ids.offers_box.ids.buttons.children[0].children[0].children[1].color = [24/255,211/255,199/255,1]

        # bad search
        if len(ans) == 0:
            toast("0 history buy offers")
        # good search
        else:
            self.of.insert_offers(list=ans)
            # self.ids.offers_box.ids.offi.size_hint_x =
            self.ids.offers_box.ids.offi.add_widget(self.of)

    def history_sell(self):
        self.ids.offers_box.ids.offi.remove_widget(self.lab)
        self.ids.offers_box.ids.offi.remove_widget(self.of)
        ans = App.get_running_app().controller.get_all_history_sell_offers()
        self.set_btn_colors()
        self.ids.offers_box.ids.buttons.children[0].children[0].children[0].color = [24/255,211/255,199/255,1]

        # bad search
        if len(ans) == 0:
            toast("0 history sell offers")
        # good search
        else:
            self.of.insert_offers(list=ans)
            self.ids.offers_box.ids.offi.add_widget(self.of)

    def set_btn_colors(self):
        for i in range (0, 5):
            self.ids.offers_box.ids.buttons.children[0].children[0].children[i].color = [0,0,0,1]


class Offers_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Offers_box, self).__init__(**kwargs)

    def change_to_cat(self):
        SideBar.change_to_cat(self)

    def back(self):
        App.get_running_app().root.current = "menu_screen"

