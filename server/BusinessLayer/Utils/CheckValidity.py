import re
import datetime
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class checkValidity:

    def checkValidityName(self,name):
        if name.replace(" ", "").isalpha():
            print
            "Name is valid"
        else:
            raise Exception("Name is invalid")

    def checkValidityEmail(self, email):
        # have to check if email exist in the world
        if not re.match(regex, email):
            raise Exception("Invalid Email")

    def checkValidityPassword(self, password):
            if len(password) < 8:
                raise Exception("Make sure your password is at lest 8 letters")
            elif len(password) > 20:
                raise Exception("Make sure your password is less then 20 letters")
            elif password.isdigit():
                raise Exception("Make sure your password has a number in it")
            elif password.isupper():
                raise Exception("Make sure your password has a lower letter in it")
            elif password.islower():
                raise Exception("Make sure your password has a capital letter in it")
            else:
                raise Exception("Your password seems fine")

    def checkValidityDateOfBirth(self, date):
        day, month, year = date.split('/')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False
        if not isValidDate:
            raise Exception ("Input date is not valid..")
        difference = datetime.datetime.now() - datetime.datetime(int(year), int(month), int(day))
        difference_in_years = (difference.days + difference.seconds / 86400) / 365.2425
        if difference_in_years > 12.0:
            raise Exception("Input date is not valid..")
        elif difference_in_years > 100.0:
            raise Exception("Input date is not valid..")


    def check_register(self, email, user_name, usersDictionary):
        for user_id in usersDictionary.keys():
            user = usersDictionary[user_id]
            if user.get_user_name == user_name:
                raise Exception("user_name is already exist")
        for user_id in usersDictionary.keys():
            user = usersDictionary[user_id]
            if user.get_email == email:
                raise Exception("email is already exist")

    def check_unregister(self, user):
        if user is None:
            raise Exception("User does not exist")
        if user.active is not True:
            raise Exception("user is not active")
        if user.is_logged is not True:
            raise Exception("user is not logged in")
        if user.is_active_buyer():
            raise Exception("the user is subscribe to an offer as a buyer")
        if user.is_active_seller():
            raise Exception("the user is subscribe to an offer as a buyer")











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

    def exist_offer_id_in_user(self, user_id, offer_id):
        user = self.usersDictionary[user_id]
        if offer_id in user.active_sale_offers:
            return True
        return False