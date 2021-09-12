from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

from client.windows.offers_list import Offers_Screen


class MY_OFFERS_Screen(Screen):
    def __init__(self, **kwargs):
        self.name = 'my_offers_screen'
        super(MY_OFFERS_Screen, self).__init__(**kwargs)
        self.mes = BoxLayout(orientation='horizontal', size_hint_y=.2)
        self.of = Offers_Screen()
        self.first_time_bad_search = True
        self.first_time_good_search = True

    def active_buy(self):
        ans = App.get_running_app().controller.get_all_active_buy_offers()
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text="0 active buy offers")
                self.mes.add_widget(self.lab)
                self.ids.offi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = "0 active buy offers.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.offi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)

    def active_sell(self):
        ans = App.get_running_app().controller.get_all_active_sell_offers()
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text="0 active sell offers")
                self.mes.add_widget(self.lab)
                self.ids.offi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = "0 active sell offers.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.offi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)

    def like_offers(self):
        ans = App.get_running_app().controller.get_all_liked_offers()
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text="0 liked offers")
                self.mes.add_widget(self.lab)
                self.ids.offi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = "0 liked offers.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.offi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)
    def history_buy(self):
        ans = App.get_running_app().controller.get_all_history_buy_offers()
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text="0 history buy offers")
                self.mes.add_widget(self.lab)
                self.ids.offi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = "0 history buy offers.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.offi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)

    def history_sell(self):
        ans = App.get_running_app().controller.get_all_history_sell_offers()
        # bad search
        if len(ans) == 0:
            self.of.insert_offers(list=[])
            if self.first_time_bad_search is True:
                self.lab = MDLabel(text="0 history sell offers")
                self.mes.add_widget(self.lab)
                self.ids.offi.add_widget(self.mes)
                self.first_time_bad_search = False
            else:
                self.lab.text = "0 history sell offers.."
        # good search
        else:
            if self.first_time_bad_search is False:
                self.lab.text = ""
            if self.first_time_good_search is True:
                self.of.insert_offers(list=ans)
                self.ids.offi.add_widget(self.of)
                self.first_time_good_search = False
            else:
                self.of.insert_offers(list=ans)


class Offers_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Offers_box, self).__init__(**kwargs)
