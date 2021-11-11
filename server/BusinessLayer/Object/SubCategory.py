from BusinessLayer.Object.Offer import Offer
from BusinessLayer.Utils.OfferStatus import OfferStatus
from datetime import date, datetime


class SubCategory:
    def __init__(self, name, id, father_category_id):
        self.name = name
        self.offers_dictionary = {}
        self.id = id
        self.father_category_id = father_category_id

    def add_offer(self, offer_id, user_id, product, steps, end_date, hot_deals):
        status = OfferStatus.ACTIVE
        offer_to_add = Offer(offer_id, user_id, product, self.father_category_id, self.id, status, steps, date.today(), end_date, {}, 0, hot_deals, False)
        self.offers_dictionary[offer_id] = offer_to_add
        return offer_to_add

    def add_offer_for_load(self, offer):
        self.offers_dictionary[offer.offer_id] = offer

    def remove_offer(self, offer_id):
        offer_to_remove = self.offers_dictionary[offer_id]
        self.offers_dictionary.pop(offer_id, None)
        return offer_to_remove

    def add_exist_offer(self, offer_to_move):
        self.offers_dictionary[offer_to_move.offer_id] = offer_to_move

    def set_name(self, new_name):
        self.name = new_name

    def get_offers(self):
        ans = []
        ans.extend(self.offers_dictionary.values())
        return ans

    def get_offers_by_product_name(self, product_name):
        ans = []
        for offer_id in self.offers_dictionary.keys():
            curr_offer = self.offers_dictionary[offer_id]
            if curr_offer.product.name == product_name:
                ans.append(curr_offer)
        return ans

    def get_offers_by_company_name(self, company_name):
        ans = []
        for offer_id in self.offers_dictionary.keys():
            curr_offer = self.offers_dictionary[offer_id]
            if curr_offer.get_product().get_company() == company_name:
                ans.append(curr_offer)
        return ans

    def get_offers_by_price(self, price):
        ans = []
        for offer_id in self.offers_dictionary.keys():
            curr_offer = self.offers_dictionary[offer_id]
            curr_step = curr_offer.get_current_step()
            curr_price = curr_offer.steps[curr_step].get_price()
            if curr_price <= price:
                ans.append(curr_offer)
        return ans

    def get_offers_by_end_date(self, end_date):
        ans = []
        for offer_id in self.offers_dictionary.keys():
            curr_offer = self.offers_dictionary[offer_id]
            # change to compare-to
            if curr_offer.get_end_date() <= end_date:
                ans.append(curr_offer)
        return ans

    def get_offers_by_status(self, status):
        ans = []
        for offer_id in self.offers_dictionary.keys():
            curr_offer = self.offers_dictionary[offer_id]
            if curr_offer.get_status().name == status.name:
                ans.append(curr_offer)
        return ans

    def get_offer_by_offer_id(self, offer_id):
        if offer_id in self.offers_dictionary:
            return self.offers_dictionary[offer_id]
        return None

    def remove_offer_for_update_sub_category(self, offer_id):
        self.offers_dictionary.pop(offer_id, None)


    def add_offer_for_update_sub_category(self, offer_to_add):
        #have to check if the offer already exist
        self.offers_dictionary[offer_to_add.offer_id] = offer_to_add

    def get_all_expired_offers(self):
        ans = []
        for offer_id in self.offers_dictionary.keys():
            curr_offer = self.offers_dictionary[offer_id]
            if curr_offer.end_date <= datetime.today():
                ans.append(curr_offer)
        return ans

    def is_contained_offers(self):
        return len(self.offers_dictionary) != 0

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_father_category_id(self):
        return self.father_category_id