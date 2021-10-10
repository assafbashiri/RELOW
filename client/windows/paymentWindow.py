from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast

from Utils.Utils import Utils

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class PAYMENTScreen(Popup):
    def __init__(self, offer_id, quantity, step, colors, sizes, new_address, user, offer, **kwargs):
        self.name = 'payment_screen'
        self.offer_id = offer_id
        self.quantity = quantity
        self.step = step
        self.colors = colors
        self.sizes = sizes
        self.new_address = new_address
        self.user = user
        self.offer = offer
        super(PAYMENTScreen, self).__init__(**kwargs)

    def pay(self):
        print("pay pay")
        payment_done = True
        if payment_done:
            ans = App.get_running_app().controller.add_active_buy_offer(self.offer_id, self.quantity, self.step,
                                                                        self.colors, self.sizes, self.new_address)
            if ans.res is True:
                self.user.get_active_buy_offers().append(self.offer)
                self.offer = ans.data
                data = App.get_running_app().root.current_screen.ids.menu_box.children[1].data
                for object in data:
                    offer = object['offer']
                    if offer[0].offer_id == self.offer_id:
                        a = ans.data.current_buyers
                        to_return = {}
                        for buyer in ans.data.current_buyers:
                            to_return[buyer['buyer_id']] = Struct(**buyer)
                        offer[0].current_buyers = to_return
                Utils.pop(self, "payment done", "success")
                self.dismiss()
            if ans.res is False:
                # have to cancel the payment
                pass
        else:
            Utils.pop(self, "payment failed", "alert")

    def back(self):
        self.dismiss()
