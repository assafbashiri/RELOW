from BussinessLayer.Utils import CheckValidity
from BussinessLayer.Object.User import User

from DB.DAO.OfferDAO import OfferDAO
from DB.DAO.ProductDAO import ProductDAO
from DB.DAO.UsersDAO import UsersDAO
from DB.DTO.OfferDTO import OfferDTO
from DB.DTO.UserDTO import UserDTO

from DB.DTO.ProductDTO import ProductDTO


class UserController:
    __instance = None

    def getInstance():
        """ Static access method. """
        if UserController.__instance == None:
            UserController()
        return UserController.__instance

    def __init__(self, conn):
        if UserController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserController.__instance = self
            self.user_id = 1
            self.users_dao = UsersDAO(conn)
            self.offers_dao = OfferDAO(conn)
            self.products_dao = ProductDAO(conn)
            self.usersDictionary = {}

    def getme(self):
        print('return singelton')
        return self

    def register(self, first_name, last_name, user_name, email, password, birth_date, gender):
        user = User(self.user_id, first_name, last_name, user_name, email, password, birth_date, gender)
        userDTO = UserDTO(self.user_id, user.first_name, user.last_name, user.user_name, user.email, user.password, user.birth_date, gender)
        self.usersDictionary[user.user_id]= user
        self.users_dao.insert(userDTO)
        self.user_id+=1
        self.log_in(user_name,password)

    def unregister(self, user_id):
        user = self.usersDictionary.get(user_id)
        if user is None:
            raise Exception("User does not exist")
        if user.active is not True:
            raise Exception("user is not active")
        if user.is_logged is not True:
            raise Exception("user is not logged")
        #check if the user is in offer
        self.log_out(user_id)
        self.usersDictionary.get(user_id).active = False  # check
        self.users_dao.unregister(user_id)
        #self.usersDictionary.get(user_id).key = None
        # dont sure that we really want to delete the user from DB
        # self.usersDictionary.remove(user_id)

    def log_in(self, user_name, password):
        if not self.exist_user_name1(user_name):
            raise Exception("User Name Not Exist")
        # user name exist in the dictionary
        password_of_user = self.get_password_by_user_name(user_name)
        if password_of_user != password:
            raise Exception("Illegal Password")
        user_to_log_in = self.get_user_by_user_name(user_name)
        user_to_log_in.log_in()  # check this line
        self.users_dao.log_in(user_to_log_in.user_id)
        return user_to_log_in

    def log_out(self, user_id):
        if user_id not in self.usersDictionary.keys():
            raise Exception("User Does Not Exist")
        self.usersDictionary[user_id].log_out()
        self.users_dao.log_out(user_id)

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

    def updatePassword(self, user_id, old_password, new_password):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        temp = self.usersDictionary.get(user_id)
        if not old_password == self.get_password_by_user_name(temp.user_name):
            raise Exception("incorrect old password")
        temp.set_password(new_password)
        self.users_dao.updatePassword(user_id, new_password)

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
        productDTO = ProductDTO(offer.product)
        self.offers_dao.insert(offerDTO, productDTO)

# add a buyer into an offer
    def add_active_buy_offer(self, user_id, offer, quantity, step):
        if not (self.exist_user_id(user_id)):
            raise Exception("User does not exist")
        buyer = self.usersDictionary.get(user_id)
        # add the quantity and the step to the active_buy_offers
        offer.add_buyer(buyer, quantity, step)
        buyer.active_buy_offers[offer.offer_id] = offer
        offerDTO = OfferDTO(offer)
        self.offers_dao.add_active_buy_offer(offerDTO, user_id, quantity, step)

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
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return True
        return False

    def exist_user_id(self, user_id):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_id == curr_user_id:
                return True
        return False

    def get_password_by_user_name(self, user_name):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return self.usersDictionary.get(curr_user_id).password
        return None

    def get_user_by_user_name(self, user_name):
        user_ids = self.usersDictionary.keys()
        for curr_user_id in user_ids:
            if user_name == self.usersDictionary.get(curr_user_id).user_name:
                return self.usersDictionary.get(curr_user_id)
        return None

    def get_user_by_id(self, user_id):
        print(self.usersDictionary.__len__())
        return self.usersDictionary[user_id]

