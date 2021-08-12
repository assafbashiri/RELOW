from BusinessLayer.Object import Offer
from BusinessLayer.Utils import OfferStatus
from datetime import date
class SubCategory:
    def __init__(self, name, id, father_category_id):
        self.name = name
        self.offers_dictionary = {}
        self.id = id
        self.father_category_id = father_category_id

    def add_offer(self,offer_id, user_id, product, steps, end_date):
        status = OfferStatus.OfferStatus.NOT_EXPIRED_UNCOMPLETED #initial state
        offer_to_add = Offer.Offer(offer_id, user_id, product, self.father_category_id, self.id, status,steps, date.today(), end_date)
        self.offers_dictionary[offer_id] = offer_to_add
        return offer_to_add


    def remove_offer(self, offer_id):
        offer_to_remove = self.offers_dictionary[offer_id]
        self.offers_dictionary.pop(offer_id, None)
        return offer_to_remove



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

    def get_offers_by_status(self, status):
        ans = []
        for offer_id in self.offers_dictionary.keys():
            curr_offer = self.offers_dictionary[offer_id]
            if curr_offer.get_status().name == status:
                ans.append(curr_offer)
        return ans


    def remove_buyer_from_offer(self, offer_id, user_id):
        if not offer_id in self.offers_dictionary:
            raise Exception("No Such Offer")
        self.offers_dictionary[offer_id].remove_buyer(user_id)

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
            if curr_offer.end_date <= date.today():
                ans.add(curr_offer)
        return ans