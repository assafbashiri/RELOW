from BussinesLayer.Utils import CheckValidity
from BussinesLayer.Objects.User import User

from server.BussinesLayer.DataMappers.UsersMapper import UsersMapper


class UserController():
    def __init__(self, conn):
        self.usersMapper = UsersMapper(conn)
        self.user_id = 0

    def register(self, first_name, last_name, user_name, email, password, gender, date_of_birth):
        user_to_add = User(self.user_id, first_name, last_name, user_name, email, password, gender, date_of_birth)
        user_to_add.active = True
        self.usersMapper.addUser(user_to_add)
        self.user_id += 1
    def unregister(self, user_id):
        self.usersMapper.removeUser(user_id)
    def log_in(self, user_name, password):
        self.usersMapper.log_in(user_name, password)
    def log_out(self, user_id):
        self.usersMapper.log_out(user_id)
    def add_payment_method(self,user_id,credit_card_number, credit_card_experation_date,cvv,card_type,id):
        self.usersMapper.add_payment_method(user_id,credit_card_number, credit_card_experation_date,cvv,card_type,id )
    def add_address_details(self,user_id, city, street, zip_code, floor, apartmentNumber):
        self.usersMapper.add_address(user_id, city, street, zip_code, floor, apartmentNumber)




    # join client to an offer
    def add_active_buy_offer(self, user_id, offer):
        self.usersMapper.add_active_buy_offer(user_id, offer)
    # add new offer - after adding offer in sub-category
    def add_active_sale_offer(self, offer):
        self.usersMapper.add_active_sale_offer(offer)
    def add_like_offer(self, user_id, offer):
        self.usersMapper.add_like_offer(user_id,offer)
    # automatic function
    def move_to_history(self):
        self.usersMapper.move_to_history()


    # remove complete offer - think if this function should be from here or from category controller
    def remove_active_sale_offer(self, user_id, offer_id):
        self.usersMapper.remove_active_sale_offer(user_id, offer_id)
    # a buyer cancel his subscribe in an offer
    def remove_active_buy_offer(self, user_id, offer_id):
        return 5

    def remove_like_offer(self, user_id, offer_id):
        return 5

    # get all offers by user
    def get_all_active_buy_offers(self, user_id):
        return 5

    def get_all_active_sale_offers(self, user_id):
        return 5

    def get_all_liked_offers(self, user_id):
        return 5

    def get_all_history_buy_offers(self, user_id):
        return 5

    def get_all_history_sale_offers(self, user_id):
        return 5

    # get one specific offers by user
    def get_offerO(self,user_id):
        return 5

    def get_history_buy_offer(self, user_id):
        return 5

    def get_history_sale_offer(self, user_id):
        return 5

    # update

    def update_first_name(self, user_id, new_first_name):
        self.usersMapper.updateFirstname(user_id,new_first_name)
    def update_last_name(self, user_id, new_last_name):
        self.usersMapper.updateLastname(user_id,new_last_name)
    def update_user_name(self, user_id, new_user_name):
        self.usersMapper.updateUsername(user_id,new_user_name)
    def update_email(self, user_id, new_email):
        self.usersMapper.updateEmail(user_id,new_email)
    def update_password(self, user_id, old_password, new_password):
        self.usersMapper.updatePassword(user_id, old_password, new_password)
    def update_birthdate(self, user_id, new_birthdate):
        self.usersMapper.updateBirthdate(user_id,new_birthdate)
    def update_gender(self, user_id, new_gender):
        self.usersMapper.updateGender(user_id,new_gender)
    def updateCity(self, user_id, new_city):
        self.usersMapper.updateCity(user_id,new_city)
    def updateStreet(self, user_id, new_street):
        self.usersMapper.updateStreet(user_id,new_street)
    def updateZipcode(self, user_id, new_zip_code):
        self.usersMapper.updateZipcode(user_id,new_zip_code)
    def updateFloor(self, user_id, new_floor):
        self.usersMapper.updateFloor(user_id,new_floor)
    def updateApartmentNumber(self, user_id, new_apartmentNumber):
        self.usersMapper.updateApartment(user_id,new_apartmentNumber)
    def updateCardNumber(self, user_id, new_card_number):
        self.usersMapper.updateCardNumber(user_id,new_card_number)
    def updateExpireDate(self, user_id, new_expire_date):
        self.usersMapper.updateExpDate(user_id,new_expire_date)
    def updateCvv(self, user_id, new_cvv):
        self.usersMapper.updateCvv(user_id,new_cvv)
    def updateCard_type(self, user_id, new_card_type):
        self.usersMapper.updateCardType(user_id,new_card_type)
    def updateId(self, user_id, new_id):
        self.usersMapper.updateId(user_id,new_id)

    # complete......


    # getters

    def get_password_by_user_name(self, user_name):
        user_ids = self.users_list.keys
        for curr_user_id in user_ids:
            if user_name == self.users_list.get(curr_user_id).user_name:
                return self.users_list.get(curr_user_id).password
        return None
    def get_user_by_user_name(self, user_name):
        user_ids = self.users_list.keys
        for curr_user_id in user_ids:
            if user_name == self.users_list.get(curr_user_id).user_name:
                return self.users_list.get(curr_user_id)
        return None
    def get_user_by_id(self, user_id):
        if user_id not in self.users_list.keys:
            raise Exception("User Does Not Exist")
        return self.users_list.get(user_id)
    def exist_user_name(self, user_name):
        user_ids = self.users_list.keys
        for curr_user_id in user_ids:
            if user_name == self.users_list.get(curr_user_id).user_name:
                return True
        return False