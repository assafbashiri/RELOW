from BussinessLayer.Object import Offer
from BussinessLayer.Utils import CheckValidity
from BussinessLayer.Utils import OfferStatus
from datetime import date
class SubCategory:
    def _init_(self, name, id, father_category_id):
        self.name=name
        self.offers_dictionary = None
        self.id = id
        self.offer_id = 0
        self.father_category_id = father_category_id

    def add_offer(self, user_id, product, steps, end_date ):
        status = OfferStatus.OfferStatus.NOT_EXPIRED_UNCOMPLETED #initial state
        offer_to_add = Offer(self.offer_id, user_id, product, self.father_category_id, self.id, status,steps, date.today(), end_date , None)
        self.offers_dictionary[self.offer_id] = offer_to_add
        self.offer_id += 1



    def remove_offer(self, offer_id):
        offer_to_remove = self.offers_dictionary[offer_id]
        if offer_to_remove is None:
            raise Exception("Offer Does Not Exist")
        self.offers_dictionary.pop(offer_id, None)
        return offer_to_remove


    def set_name(self, new_name):
        self.name = new_name

    def get_offers(self):
        return self.offers_dictionary.values()

    def get_offers_by_product_name(self, product_name):
        ans = None
        for offer_id in self.offers_dictionary:
            all_offers = self.offers_dictionary[offer_id]
            for curr_offer in all_offers:
                if curr_offer.product.name == product_name:
                    ans.add(curr_offer)
        return ans

    def get_offers_by_company_name(self, company_name):
        ans = None
        for offer_id in self.offers_dictionary:
            all_offers = self.offers_dictionary[offer_id]
            for curr_offer in all_offers:
                if curr_offer.product.company == company_name:
                    ans.add(curr_offer)
        return ans

    def get_offers_by_status(self, status):
        ans = None
        for offer_id in self.offers_dictionary:
            all_offers = self.offers_dictionary[offer_id]
            for curr_offer in all_offers:
                if curr_offer.status == status:
                    ans.add(curr_offer)
        return ans

    def add_buyer_to_offer(self, offer_id, user_id):
        if not offer_id in self.offers_dictionary:
            raise Exception("No Such Offer")
        self.offers_dictionary[offer_id].add_buyer(user_id)

    def remove_buyer_from_offer(self, offer_id, user_id):
        if not offer_id in self.offers_dictionary:
            raise Exception("No Such Offer")
        self.offers_dictionary[offer_id].remove_buyer(user_id)