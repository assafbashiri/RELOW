import re
import datetime

from assets.Utils.Utils import Utils

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
from kivymd.toast import toast


class CheckValidity:
    def checkValidityName(self, name):
        if ' ' in name:
            res = "Name Shouldnt contain any spaces"
            Utils.pop(self, res, 'alert')
            return False
        if len(name) <= 1:
            res = "name is too short"
            Utils.pop(self, res, 'alert')
            return False
        if name.replace(" ", "").isalpha():

            res =  "Good Name"
            # Utils.pop(self, res, 'success')
            #toast(res)

            return True
        else:
            res = "Bad Name - name should contain only letters"
            Utils.pop(self, res, 'alert')
            return False

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
            #toast(res)
            return  True


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
        res= "Good Email"
        # Utils.pop(self, res, 'succes')
        #toast(res)
        return True

    # password length 8-20
    def checkValidityPassword(self, password):
            if len(password) < 8:
                res= "Make sure your password is at lest 8 letters"
                Utils.pop(self, res, 'alert')
                #toast(res)
                return False
            elif len(password) > 20:
                res= "Make sure your password is less then 20 letters"
                Utils.pop(self, res, 'alert')
                #toast(res)
                return False
            elif not any(char.isdigit() for char in password):
                res = "Make sure your password has a number in it"
                Utils.pop(self, res, 'alert')
                #toast(res)
                return False
            elif not any(char.isupper() for char in password):
                res= "Make sure your password has a lower letter in it"
                Utils.pop(self, res, 'alert')
                #toast(res)
                return False
            elif not any(char.islower() for char in password):
                res= "Make sure your password has a capital letter in it"
                Utils.pop(self, res, 'alert')
                #toast(res)
                return False
            else:
                res ="Your password seems fine"
                # Utils.pop(self, res, 'succes')
                #toast(res)
                return True


    # check if this function is important due to date picker
    def checkValidityDateOfBirth(self, date):
        if ' ' in date:
            date, e = date.split(' ')
        year, month, day = date.split('-')
        isValidDate = True
        try:
            x=datetime.datetime(int(year), int(month), int(day))
            a=6
        except Exception as e:
            isValidDate = False
        if not isValidDate:
            raise Exception("Input date is not valid..")
        difference = datetime.datetime.now() - datetime.datetime(int(year), int(month), int(day))
        difference_in_years = (difference.days + difference.seconds / 86400) / 365.2425
        if difference_in_years > 12.0:
            raise Exception("Input date is not valid..")
        elif difference_in_years > 100.0:
            raise Exception("Input date is not valid..")

    def checkEndDate(self, end_date):
        isValidDate = True
        try:
            year, month, day = end_date.split('-')
            a = datetime.datetime(int(year), int(month), int(day))
        except ValueError as v:
            isValidDate = False
        if not isValidDate:
            toast("Input date is not valid..")
            print("Input date is not valid..")
            return False
        today = datetime.datetime.now()
        today_day = today.day.real
        today_month = today.month.real
        today_year = today.year.real
        # difference = datetime.datetime.now() - datetime.datetime(int(year), int(month), int(day))
        if today_year > int(year):
            toast("bad year")
            return False
        if today_year < int(year):
            return True
        if today_month > int(month):
            toast("bad month")
            return False
        if today_month < int(month):
            return True
        if today_day > int(day):
            toast("bad day")
            return False
        return True
