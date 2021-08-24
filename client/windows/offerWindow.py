from kivy.uix.screenmanager import Screen

from client.Backend_controller import Backend_controller
from client.Service.Object.OfferService import OfferService
from client.main import Struct


class offerWindow(Screen):
    def __init__(self, controller):
        self.controller = Backend_controller()
        self.offer = OfferService()
        # self.controller = controller

    # seller methods

    def update_sub_category_for_offer(self):
        offer_id = self.offer.get_offer_id()
        sub_category_id = ""
        ans = self.controller.update_sub_category_for_offer(offer_id, sub_category_id)
        res = Struct(**ans)

    def update_end_date(self):
        end_date = ""
        offer_id = self.offer.get_offer_id()
        ans = self.controller.update_end_date(offer_id, end_date)
        res = Struct(**ans)

    def update_product_company(self):
        company = ""
        offer_id = self.offer.get_offer_id()
        ans = self.controller.update_product_company(offer_id, company)
        res = Struct(**ans)

    def update_product_name(self):
        offer_id = self.offer.get_offer_id()
        name = ""
        ans = self.controller.update_product_name(offer_id, name)
        res = Struct(**ans)

    def update_product_color(self):
        offer_id = self.offer.get_offer_id()
        color = ""
        ans = self.controller.update_product_color(offer_id, color)
        res = Struct(**ans)

    def update_product_size(self):
        offer_id = self.offer.get_offer_id()
        size = ""
        ans = self.controller.update_product_size(offer_id, size)
        res = Struct(**ans)

    def update_product_description(self):
        offer_id = self.offer.get_offer_id()
        description = ""
        ans = self.controller.update_product_description(offer_id, description)
        res = Struct(**ans)

    def add_photo(self):
        offer_id = self.offer.get_offer_id()
        photo = ""
        ans = self.controller.add_photo(offer_id, photo)
        res = Struct(**ans)

    def remove_photo(self):
        offer_id = self.offer.get_offer_id()
        photo = ""
        ans = self.controller.remove_photo(offer_id, photo)
        res = Struct(**ans)

    # buyer methods

    def update_step(self):
        offer_id = self.offer.get_offer_id()
        step = ""
        ans = self.controller.update_step(offer_id, step)
        res = Struct(**ans)

    def add_liked_offer(self):
        offer_id = self.offer.get_offer_id()
        ans = self.controller.add_liked_offer(offer_id)
        res = Struct(**ans)

    def remove_liked_offer(self):
        offer_id = self.offer.get_offer_id()
        ans = self.controller.remove_liked_offer(offer_id)
        res = Struct(**ans)


