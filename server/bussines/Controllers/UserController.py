from bussines import Object
from bussines.Object.User import User


class UserController():
    def __init__(self):
        self.users_list = None

    def addUser(self, first_name, last_name, email, password):
        user1 = User(first_name, last_name, email, password)
        self.users_list.add(user1)
        #add to DB