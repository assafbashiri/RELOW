from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast

from Utils.Utils import Utils

from Service.Object.OfferService import OfferService
from Service.Object.PurchaseService import PurchaseService


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class PAYMENTScreen(Popup):
    def __init__(self, offer_id, quantity, step, colors, sizes, new_address, user, offer, screen_name, photo_list, **kwargs):
        self.name = 'payment_screen'
        self.offer_id = offer_id
        self.quantity = quantity
        self.step = step
        self.colors = colors
        self.sizes = sizes
        self.new_address = new_address
        self.user = user
        self.offer = offer
        self.screen_name = screen_name
        self.photo_list = photo_list
        super(PAYMENTScreen, self).__init__(**kwargs)

    def pay(self):
        print("pay pay")
        payment_done = True
        if payment_done:
            ans = App.get_running_app().controller.add_purchase(self.offer_id, self.quantity, self.step,
                                                                        self.colors, self.sizes, self.new_address, self.user)
            if ans != False:
                Utils.pop(self, "payment done", "success")
                self.offer = ans
                # self.offer.current_buyers[self.user.user_id] = PurchaseService()
                self.dismiss()
                self.change_offer_screen_to_buyer()
            if ans is False:
                # have to cancel the payment
                pass
        else:
            Utils.pop(self, "payment failed", "alert")

    def back(self):
        self.dismiss()

    def change_offer_screen_to_buyer(self):
        screens = App.get_running_app().root.screens
        for screen in screens:
            if self.screen_name in screen.name:
                screen.remove_widget(screen.box)
                screen.init_offer(self.offer, self.photo_list)
