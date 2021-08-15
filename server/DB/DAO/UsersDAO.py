class UsersDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, userDTO):
        print("in insert in UserDAO step 1")
        self._conn.execute(
            """INSERT INTO users_submission (user_id, first_name, last_name, user_name, email, password, birth_date, gender, is_logged, active) VALUES (?,?,?,?,?,?,?,?,?,?)""",
            [userDTO.user_id, userDTO.first_name, userDTO.last_name, userDTO.user_name, userDTO.email, userDTO.password,
             userDTO.birth_date, userDTO.gender, True, True])
        self._conn.commit()
        print("in insert in UserDAO step 2")

        self._conn.execute(
            """INSERT INTO users_extra_details (user_id) VALUES (?)""",
            [userDTO.user_id])
        self._conn.commit()
        print("in insert in UserDAO step 3")

        self._conn.execute(
            """INSERT INTO users_address (user_id,city,street,zip_code,floor,apt) VALUES (?,?,?,?,?,?)""",
            [userDTO.user_id, userDTO.city, userDTO.street, userDTO.zip_code, userDTO.floor, userDTO.apartment_number])
        self._conn.commit()
        print("in insert in UserDAO step 4")

        self._conn.execute(
            """INSERT INTO users_payment (user_id,card_number,expire_date,cvv,card_type, id_number) VALUES (?,?,?,?,?,?)""",
            [userDTO.user_id, userDTO.credit_card_number, userDTO.credit_card_experation_date, userDTO.cvv,
             userDTO.card_type, userDTO.id_number])
        self._conn.commit()
        print("in insert in UserDAO step 5")

    def load_user_id(self):
        this = self._conn.cursor()
        this.execute("SELECT MAX(user_id) FROM users_submission")
        output = this.fetchone()[0]
        if output is None:
            output = 0
        return output + 1

    def load_users_sub(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users_submission")
        output = this.fetchall()
        return output

    def load_users_payment(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users_payment")
        output = this.fetchall()
        return output

    def load_users_address(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users_address")
        output = this.fetchall()
        return output

    def add_address(self, user_id, city, street, zip_code, floor, apartment_number):
        self.updateCity(user_id, city)
        self.updateStreet(user_id, street)
        self.updateZipcode(user_id, zip_code)
        self.updateFloor(user_id, floor)
        self.updateApartmentNumber(user_id, apartment_number)
        # self._conn.execute(
        # """INSERT INTO users_address (user_id, city, street, zip_code, floor, apt) VALUES (?,?,?,?,?,?)""",
        # [user_id, city, street, zip_code, floor, apartmentNumber])
        # self._conn.commit()

    def add_payment_method(self, user_id, credit_card, exp_date, cvv, card_type, id):
        self.updateCardNumber(user_id, credit_card)
        self.updateExpireDate(user_id, exp_date)
        self.updateCvv(user_id, cvv)
        self.updateCard_type(user_id, card_type)
        self.updateId(user_id, id)
        # self._conn.execute(
        # """UPDATE users_payment set card_number = ? ,expire_date = ? ,cvv = ? ,card_type = ? , id_number = ? WHERE user_id = ?""",
        # [credit_card, exp_date, cvv, card_type, id, user_id])
        # self._conn.commit()

    # update users_submission

    def unregister(self, user_id):
        self._conn.execute("""UPDATE users_submission set active = ? WHERE user_id = ?""",
                           [False, user_id])
        self._conn.commit()

    def log_in(self, user_id):
        self._conn.execute("""UPDATE users_submission set is_logged = ? WHERE user_id = ?""",
                           [True, user_id])
        self._conn.commit()

    def log_out(self, user_id):
        self._conn.execute("""UPDATE users_submission set is_logged = ? WHERE user_id = ?""",
                           [False, user_id])
        self._conn.commit()

    def updateFirstname(self, id, name):
        self._conn.execute("""UPDATE users_submission set first_name = ? where user_id = ?""",
                           [name, id])
        self._conn.commit()

    def updateLastname(self, id, name):
        self._conn.execute("""UPDATE users_submission set last_name = ? where user_id = ?""",
                           [name, id])
        self._conn.commit()

    def updateUsername(self, id, name):
        self._conn.execute("""UPDATE users_submission set user_name = ? where user_id = ?""",
                           [name, id])
        self._conn.commit()

    def updatePassword(self, id, password):
        self._conn.execute("""UPDATE users_submission set password = ? where user_id = ?""",
                           [password, id])
        self._conn.commit()

    def updateEmail(self, user_id, new_email):
        self._conn.execute("""UPDATE users_submission set email = ? where user_id = ?""",
                           [new_email, user_id])
        self._conn.commit()

    # update users_extra_details

    def updateBirthdate(self, id, date):
        self._conn.execute("""UPDATE users_extra_details set birth_date = ? where user_id = ?""",
                           [date, id])
        self._conn.commit()

    def updateGender(self, id, gender):
        self._conn.execute("""UPDATE users_extra_details set gender = ? where user_id = ?""",
                           [gender, id])
        self._conn.commit()

    # update users_address

    def updateCity(self, id, city):
        self._conn.execute("""UPDATE users_address set city = ? where user_id = ?""",
                           [city, id])
        self._conn.commit()

    def updateStreet(self, id, street):
        self._conn.execute("""UPDATE users_address set street = ? where user_id = ?""",
                           [street, id])
        self._conn.commit()

    def updateZipcode(self, id, zip_code):
        self._conn.execute("""UPDATE users_address set zip_code = ? where user_id = ?""",
                           [zip_code, id])
        self._conn.commit()

    def updateFloor(self, id, floor):
        self._conn.execute("""UPDATE users_address set floor = ? where user_id = ?""",
                           [floor, id])
        self._conn.commit()

    def updateApartmentNumber(self, id, apartmentNumber):
        self._conn.execute("""UPDATE users_address set apt = ? where user_id = ?""",
                           [apartmentNumber, id])
        self._conn.commit()

    # update users_payment
    def updateCardNumber(self, id, card_number):
        self._conn.execute("""UPDATE users_payment set card_number = ? where user_id = ?""",
                           [card_number, id])
        self._conn.commit()

    def updateExpireDate(self, id, expire_date):
        self._conn.execute("""UPDATE users_payment set expire_date = ? where user_id = ?""",
                           [expire_date, id])
        self._conn.commit()

    def updateCvv(self, id, cvv):
        self._conn.execute("""UPDATE users_payment set cvv = ? where user_id = ?""",
                           [cvv, id])
        self._conn.commit()

    def updateCard_type(self, id, card_type):
        self._conn.execute("""UPDATE users_payment set card_type = ? where user_id = ?""",
                           [card_type, id])
        self._conn.commit()

    def updateId(self, user_id, id):
        self._conn.execute("""UPDATE users_payment set id_number = ? where user_id = ?""",
                           [id, user_id])
        self._conn.commit()

    # getters

    def usersFirst_Name(self, name):
        this = self._conn.cursor()
        output1 = this.execute("SELECT * FROM users_submission WHERE first_name=?", [name])
        output = this.fetchone()

        return output

    def usersLast_Name(self, name):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users_submission WHERE last_name=?", [name])
        output = this.fetchone()[0]

        return output

    def usersPassword(self, password):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users_submission WHERE country=?", [password])
        output = this.fetchone()[0]

        return output

    def users_email(self, email):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users_submission WHERE email=?", [email])
        output = this.fetchone()[0]

        return output
