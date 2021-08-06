from bussines.Utils import CheckValidity
from bussines.Object.User import User

from server.DB.DAO.OfferDAO import OfferDAO
from server.DB.DAO.ProductDAO import ProductDAO
from server.DB.DAO.UsersDAO import UsersDAO
from server.DB.DTO.OfferDTO import OfferDTO
from server.DB.DTO.UserDTO import UserDTO


class UserController():


    def __init__(self, conn):
        self.user_id = 1
        self.users_dao = UsersDAO(conn)
        self.offers_dao = OfferDAO(conn)
        self.products_dao = ProductDAO(conn)
        self.usersDictionary = None  # dictionary [id,user]

    def register(self, user_id, first_name, last_name, email, password, gender, date_of_birth):
        user = User(user_id, first_name, last_name, email, password, gender, date_of_birth)
        userDTO = UserDTO(user.user_id, user.first_name, user.last_name, user.email, user.password, user.gender,
                          user.date_of_birth)
        self.usersDictionary.add(user.user_id, user)
        self.users_dao.insert(userDTO)

    def removeUser(self, user_id):
        if self.usersDictionary.get(user_id) is None:
            raise Exception("User does not exist")
        self.usersDictionary.get(user_id).active = False  # check
        self.usersDictionary.get(user_id).key = None
        # dont sure that we really want to delete the user from DB
        # self.users_dao.delete(user_id)
        self.usersDictionary.remove(user_id)

    def log_in(self, user_name, password):
        if not self.exist_user_name1(user_name):
            raise Exception("User Name Not Exist")
        # user name exist in the dictionary
        password_of_user = self.get_password_by_user_name(user_name)
        if password_of_user != password:
            raise Exception("Illegal Password")
        user_to_log_in = self.get_user_by_user_name(user_name)
        user_to_log_in.log_in(self)  # check this line

    def log_out(self, user_id):
        if user_id not in self.usersDictionary.keys:
            raise Exception("User Does Not Exist")
        self.usersDictionary.get(user_id).log_out()

    def add_payment_method(self, user_id, credit_card_number, credit_card_experation_date, cvv, card_type, id):
        user_to_add = self.get_user_by_id(user_id)
        user_to_add.set_card_details(id, credit_card_number, credit_card_experation_date, cvv, card_type)
        self.users_dao.add_payment_method(user_id, credit_card_number, credit_card_experation_date, cvv, card_type, id)

    def add_address(self, user_id, city, street, zip_code, floor, apartmentNumber):
        user_to_add = self.get_user_by_id(user_id)
        user_to_add.add_address_details(city, street, apartmentNumber, zip_code, floor)
        self.users_dao.add_address(user_id, city, street, zip_code, floor, apartmentNumber)
        # update users_submission

    def updateFirstname(self, user_id, firstname):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_first_name(firstname)
        self.users_dao.updateFirstname(user_id, firstname)

    def updateLastname(self, user_id, lastname):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_last_name(lastname)
        self.users_dao.updateLastname(user_id, lastname)

    def updateUsername(self, user_id, username):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_user_name(username)
        self.users_dao.updateUsername(user_id, username)

    def updatePassword(self, user_id, old_password, new_passsord):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        if not old_password == self.get_password_by_user_name(temp.user_name):
            raise Exception("incorrect old password")

        temp.set_password(new_passsord)
        self.users_dao.updatePassword(user_id, new_passsord)

    def updateEmail(self, user_id, new_email):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_email(new_email)
        self.users_dao.updateEmail(user_id, new_email)

    def updateBirthdate(self, user_id, new_birthdate):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_date_of_birth(new_birthdate)
        self.users_dao.updateBirthdate(user_id, new_birthdate)

    def updateGender(self, user_id, new_gender):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_gender(new_gender)
        self.users_dao.updateGender(user_id, new_gender)

    def updateCity(self, user_id, new_city):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_city(new_city)
        self.users_dao.updateCity(user_id, new_city)

    def updateStreet(self, user_id, new_street):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_street(new_street)
        self.users_dao.updateStreet(user_id, new_street)

    def updateZipcode(self, user_id, new_zip_code):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_zip_code(new_zip_code)
        self.users_dao.updateZipcode(user_id, new_zip_code)

    def updateFloor(self, user_id, new_floor):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_floor(new_floor)
        self.users_dao.updateFloor(user_id, new_floor)

    def updateApartment(self, user_id, new_apartmentNumber):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_apartment_number(new_apartmentNumber)
        self.users_dao.updateApartmentNumber(user_id, new_apartmentNumber)

    def updateCardNumber(self, user_id, new_card_number):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_card_number(new_card_number)
        self.users_dao.updateCardNumber(user_id, new_card_number)

    def updateExpDate(self, user_id, new_expire_date):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_exp_date(new_expire_date)
        self.users_dao.updateExpireDate(user_id, new_expire_date)

    def updateCvv(self, user_id, new_cvv):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_cvv(new_cvv)
        self.users_dao.updateCvv(user_id, new_cvv)

    def updateCardType(self, user_id, new_card_type):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_card_type(new_card_type)
        self.users_dao.updateCard_type(user_id, new_card_type)

    def updateId(self, user_id, new_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.set_id(new_id)
        self.users_dao.updateId(user_id, new_id)

        # ------------------------------- offers

    def add_active_sale_offer(self, offer):
        if not (self.exist_user_id(offer.user_id)):
            raise Exception("User does not exist")
        saler = self.usersDictionary.get(offer.user_id)
        saler.active_sale_offers.add(offer.offer_id, offer)
        offerDTO = OfferDTO(offer)
        self.offers_dao.add_active_sale_offer(offerDTO)

    def add_active_buy_offer(self, user_id, offer):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.active_buy_offers.add(offer.offer_id, offer)
        offerDTO = OfferDTO(offer)
        self.offers_dao.add_active_buy_offer(offerDTO, user_id)

    def add_like_offer(self, user_id, offer):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.liked_offers.add(offer.offer_id, offer)
        self.offers_dao.add_like_offer()

    def move_to_history(self):
        pass

    def remove_active_sale_offer(self, user_id, offer_id):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        temp.active_sale_offers.remove(offer_id)
        self.offers_dao.delete_sale_offer(user_id, offer_id)

        # -------------------------- private functions -- to implement!!!

    def exist_user_name1(self, user_name):
        user_ids = self.usersDictionary.keys
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return True
        return False

    def exist_user_id(self, user_id):
        return False

    def get_password_by_user_name(self, user_name):
        user_ids = self.usersDictionary.keys
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return self.usersDictionary.get(curr_user_id).password
        return None

    def get_user_by_user_name(self, user_name):
        user_ids = self.usersDictionary.keys
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return self.usersDictionary.get(curr_user_id)
        return None

    def get_user_by_id(self, user_id):
        return self.usersDictionary.get(user_id)

