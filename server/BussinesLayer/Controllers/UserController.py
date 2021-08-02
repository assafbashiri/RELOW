from BussinesLayer.Utils import CheckValidity
from BussinesLayer.Objects.User import User


class UserController():
    def __init__(self):
        self.users_list = None # dictionary userId to user
        self.user_id = 0

    def add_user(self, first_name, last_name, user_name, user_id, email, password):
        user_to_add = User(self.user_id, first_name, last_name, user_name, email, password)
        user_to_add.active = True
        self.users_list.add(user_id, user_to_add)
        self.user_id += 1
        # add to DB

    def remove_user(self, user_id):
        if self.users_list.get(user_id) is None:
            raise Exception ("User does not exist")

        self.users_list.get(user_id).active = False #check
        self.users_list.get(user_id).key = None
        # remove in DB

    def update_first_name(self, user_id, new_first_name):
        user_to_update = self.getUserById(self,user_id)
        user_to_update.set_first_name(new_first_name)

    def update_last_name(self,user_id, new_last_name):
        user_to_update = self.getUserById(self, user_id)
        user_to_update.set_last_name(new_last_name)

    def update_user_name(self, user_id, new_user_name):
        user_to_update = self.getUserById(self, user_id)
        user_to_update.set_user_name(new_user_name)

    def get_user_by_id(self, user_id):
        if user_id not in self.users_list.keys:
            raise Exception("User Does Not Exist")
        return self.users_list.get(user_id)

    def register(self, first_name, last_name, user_name, email, password):
        self.add_user(first_name, last_name, user_name, email, password)
        # in add user change field "active" in user to add
        # in "add_user" add the new user to DB

    def log_in(self, user_name, password):
        if not self.exist_user_name(self, user_name):
            raise Exception("User Name Not Exist")
        # user name exist in the dictionary
        password_of_user = self.get_password_by_user_name(self, user_name)
        if password_of_user != password:
            raise Exception("Illegal Password")
        user_to_log_in = self.get_user_by_user_name(self, user_name)
        user_to_log_in.log_in(self) # check this line

    def exist_user_name(self, user_name):
        user_ids = self.users_list.keys
        for curr_user_id in user_ids:
            if user_name == self.users_list.get(curr_user_id).user_name:
                return True
        return False

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

    def log_out(self, user_id):
        if user_id not in self.users_list.keys:
            raise Exception("UserDoes Not Exist")
        self.users_list.get(user_id).log_out(self)





