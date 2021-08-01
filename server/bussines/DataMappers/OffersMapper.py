from server.DB.DAO.OfferDAO import OfferDAO
from server.DB.DTO.OfferDTO import OfferDTO


class OffersMapper:

    def __init__(self, conn):
        self.dao = OfferDAO(conn)
      #  self.OfferMapper = singleton

    def addOffer(self, offer):
        offerDTO = OfferDTO(offer.offer_id,offer.current_step,offer.user_id,offer.category_id,offer.subCategory_id,offer.status,offer.start_date,offer.end_date)
        self.dao.insert(offerDTO)
        self.OfferMapper.put(offer)

    def removeOffer(self, offer):
        self.dao.delete(offer.offer_id)
        self.OfferMapper.remove(offer.offer_id)

    def updateCurrentStep(self, offer, current_step):
        self.dao.updateCurrentStep(offer.offer_id, current_step)
        self.OfferMapper.get(offer.offer_id).current_step = current_step

    def updateCategoryId(self, offer, category_id):
        self.dao.updateCategoryId(offer.offer_id, category_id)
        self.OfferMapper.get(offer.offer_id).category_id = category_id

    def updateSubCategoryId(self, offer, subCategory_id):
        self.dao.updateSubCategoryId(offer.offer_id, subCategory_id)
        self.OfferMapper.get(offer.offer_id).subCategory_id = subCategory_id

    def updateStatus(self, offer, status):
        self.dao.updateStatus(offer.offer_id, status)
        self.OfferMapper.get(offer.offer_id).status = status

    def updateEndDate(self, offer, end_date):
        self.dao.updateEndDate(offer.offer_id, end_date)
        self.OfferMapper.get(offer.offer_id).end_date = end_date