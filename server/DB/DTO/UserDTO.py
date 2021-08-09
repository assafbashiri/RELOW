
class UserDTO:
    def __init__(self, user_id, first_name, last_name, user_name, email, password, birth_date, gender):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.gender = gender
        self.active = True
        self.is_logged = False
