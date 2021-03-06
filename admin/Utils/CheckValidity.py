import re
import datetime
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
from kivymd.toast import toast

class CheckValidity:
    def checkValidityName(self,name):
        if ' ' in name:
            res = "Name Shouldnt contain any spaces"
            toast(res)
            return False
        if len(name)<=1:
            res =  "name is too short"
            toast(res)
            return False
        if name.replace(" ", "").isalpha():
            res =  "Good Name"
            toast(res)
            return True
        else:
            res =  "Bad Name - name should contain only letters"
            toast(res)
            return False

    # user name length is 8-20 letters
    def checkValidityUserName(self, user_name):
        if len(user_name)<4:
            res = "User Name Must contain at least 4 letters"
            toast(res)
            return False
        if len(user_name)>20:
            res = "User Name Must contain maximum of 20 letters"
            toast(res)
            return False
        if not user_name[0].isalpha():
            res = "User Name Should Start With letter"
            toast(res)
            return False
        if ' ' in user_name:
            res = "User Name Shouldnt contain any spaces"
            toast(res)
            return False
        else:
            res = "Good User Name"
            toast(res)
            return  True

    def checkValidityEmail(self, email):
        # have to check if email exist in the world
        if not re.match(regex, email):
            res = "Bad Email"
            toast(res)
            return False
        res= "Good Email"
        toast(res)
        return True

    #password length 8-20
    def checkValidityPassword(self, password):
            if len(password) < 8:
                res= "Make sure your password is at lest 8 letters"
                toast(res)
                return False
            elif len(password) > 20:
                res= "Make sure your password is less then 20 letters"
                toast(res)
                return False
            elif not any(char.isdigit() for char in password):
                res = "Make sure your password has a number in it"
                toast(res)
                return False
            elif not any(char.isupper() for char in password):
                res= "Make sure your password has a lower letter in it"
                toast(res)
                return False
            elif not any(char.islower() for char in password):
                res= "Make sure your password has a capital letter in it"
                toast(res)
                return False
            else:
                res ="Your password seems fine"
                toast(res)
                return True

    #check if this function is important due to date picker
    def checkValidityDateOfBirth(self, date):
        day, month, year = date.split('-')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False
        if not isValidDate:
            raise Exception("Input date is not valid..")
        difference = datetime.datetime.now() - datetime.datetime(int(year), int(month), int(day))
        difference_in_years = (difference.days + difference.seconds / 86400) / 365.2425
        if difference_in_years > 12.0:
            raise Exception("Input date is not valid..")
        elif difference_in_years > 100.0:
            raise Exception("Input date is not valid..")

