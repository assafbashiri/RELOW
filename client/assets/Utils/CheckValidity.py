import re
import datetime

from assets.Utils.Utils import Utils

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
from kivymd.toast import toast


class CheckValidity:
    def contains_only_digits(self, str, obj):
        if not str.isdecimal():
            Utils.pop(self, f'{obj} must contain only digits', 'alert')
            return False
        return True

    def contains_only_letters(self, str, obj):
        if not str.isalpha():
            Utils.pop(self, f'{obj} must contain only digits', 'alert')
            return False
        return True

    def checkValidityName(self, name):
        if ' ' in name:
            res = "Name Shouldnt contain any spaces"
            Utils.pop(self, res, 'alert')
            return False
        if len(name) <= 1:
            res = "name is too short - less/equal then 1"
            Utils.pop(self, res, 'alert')
            return False
        if name.replace(" ", "").isalpha():
            res = "Good Name"

            return True
        else:
            res = "Bad Name - name should contain only letters"
            Utils.pop(self, res, 'alert')
            return False

    def check_validity_product_company_name(self,product_name):
        MAX_LENGTH = 20
        if len(product_name) <= 1:
            res = "product name is too short - less/equal then 1"
            Utils.pop(self, res, 'alert')
            return False
        if len(product_name) > MAX_LENGTH:
            res = f'product name is too long - more then {MAX_LENGTH}'
            Utils.pop(self, res, 'alert')
            return False
        if not product_name[0].isalpha():
            res = "product name have to start with a letter"
            Utils.pop(self, res, 'alert')
            return False

        return True

    #add more constraints by demand
    def check_validity_description(self,description):
        MAX_LENGTH = 200
        if len(description) <= 1:
            res = "description is too short - less/equal then 1"
            Utils.pop(self, res, 'alert')
            return False
        if len(description) > MAX_LENGTH:
            res = f'description is too long - more then {MAX_LENGTH}'
            Utils.pop(self, res, 'alert')
            return False
        if not description[0].isalpha():
            res = "description have to start with a letter"
            Utils.pop(self, res, 'alert')
            return False

        return True

    # user name length is 8-20 letters
    def checkValidityPhone(self, phone):
        if len(phone) != 10:
            res = "phone Must contain 10 digits"
            Utils.pop(self, res, 'alert')
            return False
        for i in range(0, 10):
            if not phone[i].isdigit():
                res = "phone contatins only digits"
                Utils.pop(self, res, 'alert')
                return False
        if phone[0] != "0" or phone[1] != "5":
            res = "Phone must start with 05"
            Utils.pop(self, res, 'alert')
            return False
        else:
            res = "Good User Name"
            # Utils.pop(self, res, 'succes')
            # toast(res)
            return True

    # def checkValidityUserName(self, user_name):
    #     if len(user_name)<4:
    #         res = "User Name Must contain at least 4 letters"
    #         Utils.pop(self, res, 'alert')
    #         #toast(res)
    #         return False
    #     if len(user_name)>20:
    #         res = "User Name Must contain maximum of 20 letters"
    #         Utils.pop(self, res, 'alert')
    #         #toast(res)
    #         return False
    #     if not user_name[0].isalpha():
    #         res = "User Name Should Start With letter"
    #         Utils.pop(self, res, 'alert')
    #         #toast(res)
    #         return False
    #     if ' ' in user_name:
    #         res = "User Name Shouldnt contain any spaces"
    #         Utils.pop(self, res, 'alert')
    #         #toast(res)
    #         return False
    #     else:
    #         res = "Good User Name"
    #         # Utils.pop(self, res, 'succes')
    #         #toast(res)
    #         return  True

    def checkValidityEmail(self, email):
        # have to check if email exist in the world
        if not re.match(regex, email):
            res = "Bad Email"
            Utils.pop(self, res, 'alert')
            return False
        res = "Good Email"
        # Utils.pop(self, res, 'succes')
        # toast(res)
        return True

    # password length 8-20
    def checkValidityPassword(self, password):
        if len(password) < 8:
            res = "Make sure your password is at lest 8 letters"
            Utils.pop(self, res, 'alert')
            return False
        elif len(password) > 20:
            res = "Make sure your password is less then 20 letters"
            Utils.pop(self, res, 'alert')
            return False
        elif not any(char.isdigit() for char in password):
            res = "Make sure your password has a digit"
            Utils.pop(self, res, 'alert')
            return False
        elif not any(char.isupper() for char in password):
            res = "Make sure your password has a capital letter in it"
            Utils.pop(self, res, 'alert')
            return False
        elif not any(char.islower() for char in password):
            res = "Make sure your password has a lower letter in it"
            Utils.pop(self, res, 'alert')
            return False
        for ch in password:
            if (not ch.isdigit()) and (not ch.isupper()) and (not ch.islower()):
                res = "Only english letters and digits"
                Utils.pop(self, res, 'alert')
                return False
        else:
            return True

    # check if this function is important due to date picker
    def checkValidityDateOfBirth(self, date):
        min_age = 12.0
        if ' ' in date:
            date, e = date.split(' ')
        year, month, day = date.split('-')
        isValidDate = True
        try:
            x = datetime.datetime(int(year), int(month), int(day))
            a = 6
        except Exception as e:
            isValidDate = False
        if not isValidDate:
            toast("Input date is not valid..")
            return False
        difference = datetime.datetime.now() - datetime.datetime(int(year), int(month), int(day))
        difference_in_years = (difference.days + difference.seconds / 86400) / 365.2425
        if difference_in_years < min_age:
            toast(
                f'Sorry, Your are too young, your age is {int(difference_in_years)} years old, you have to be at least {int(min_age)} years old')
            return False

    def checkEndDate(self, end_date):
        isValidDate = True
        try:
            year, month, day = end_date.split('-')
            a = datetime.datetime(int(year), int(month), int(day))
        except ValueError as v:
            isValidDate = False
        if not isValidDate:
            toast("Input date is not valid..")
            return False
        today = datetime.datetime.now()
        today_day = today.day.real
        today_month = today.month.real
        today_year = today.year.real

        year = int(year)
        month = int(month)
        day = int(day)

        if month == 2:
            if day > 28:
                return False
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day > 31:
                return False
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                return False

        if today_year > year:
            toast("bad year")
            return False
        if today_year < year:
            return True
        if today_month > month:
            toast("bad month")
            return False
        if today_month < month:
            return True
        if today_day > day:
            toast("bad day")
            return False
        return True
