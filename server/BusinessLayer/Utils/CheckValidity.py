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


    def check_register(self, email, phone, usersDictionary):
        for user_id in usersDictionary.keys():
            user = usersDictionary[user_id]
            if user.get_phone() == phone:
                raise Exception("phone is already exist")
        for user_id in usersDictionary.keys():
            user = usersDictionary[user_id]
            if user.get_email() == email:
                raise Exception("email is already exist")

    def check_unregister(self, user):
        if user is None:
            raise Exception("User does not exist")
        # if user.active is not True:
        #     raise Exception("user is not active")
        if user.is_active_buyer():
            raise Exception("the user is subscribe to an offer as a buyer")
        if user.is_active_seller():
            raise Exception("the user is subscribe to an offer as a buyer")

