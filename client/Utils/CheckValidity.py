import re
import datetime
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class CheckValidity:
    def checkValidityName(self,name):
        if len(name)<=1:
            return "name is too short", False
        if name.replace(" ", "").isalpha():
            return "Good Name" ,True
        else:
            return "Bad Name - name should contain only letters",False

    # user name length is 8-20 letters
    def checkValidityUserName(self, user_name):
        if len(user_name)<4:
            return "User Name Must contain at least 4 letters", False
        if len(user_name)>20:
            return "User Name Must contain maximum of 20 letters", False
        if not user_name[0].isalpha():
            return "User Name Should Start With letter"
        if ' ' in user_name:
            return "User Name Shouldnt contain any spaces"
        #add an regex to validate that the user name contain only letters and numbers
        else:
            return "Good User Name", True

    def checkValidityEmail(self, email):
        # have to check if email exist in the world
        if not re.match(regex, email):
            return "Bad Email",False
        return "Good Email",True

    #password length 8-20
    def checkValidityPassword(self, password):
            if len(password) < 8:
                return "Make sure your password is at lest 8 letters", False
            elif len(password) > 20:
                return "Make sure your password is less then 20 letters", False
            elif not any(char.isdigit() for char in password):
                return "Make sure your password has a number in it", False
            elif not any(char.isupper() for char in password):
                return "Make sure your password has a lower letter in it", False
            elif not any(char.islower() for char in password):
                return "Make sure your password has a capital letter in it", False
            else:
                return "Your password seems fine", True

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

