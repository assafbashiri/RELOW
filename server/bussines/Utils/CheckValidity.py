import re
import datetime
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class checkValidity():
    def checkValidityName(name):
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
            elif not password.isdigit():
                raise Exception("Make sure your password has a number in it")
            elif not password.isupper():
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
