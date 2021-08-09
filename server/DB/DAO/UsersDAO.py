class UsersDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, user):
        print( "in insert in UserDAO step 1")
        self._conn.execute(
            """INSERT INTO users_submission (user_id, first_name, last_name, user_name, email, password, birth_date, gender, is_logged, active) VALUES (?,?,?,?,?,?,?,?,?,?)""",
                           [user.user_id, user.first_name, user.last_name, user.user_name, user.email, user.password, user.birth_date, user.gender, True, True])
        self._conn.commit()
        print( "in insert in UserDAO step 2")

        self._conn.execute(
            """INSERT INTO users_extra_details (user_id) VALUES (?)""",
            [user.user_id])
        self._conn.commit()
        print( "in insert in UserDAO step 3")

        self._conn.execute(
            """INSERT INTO users_address (user_id,city,street,zip_code,floor,apt) VALUES (?,?,?,?,?,?)""",
            [user.user_id, user.city, user.street, user.zip_code, user.floor, user.apartment_number])
        self._conn.commit()
        print( "in insert in UserDAO step 4")

        self._conn.execute(
            """INSERT INTO users_payment (user_id,card_number,expire_date,cvv,card_type, id_number) VALUES (?,?,?,?,?,?)""",
            [user.user_id, user.credit_card_number, user.credit_card_experation_date, user.cvv, user.card_type, user.id_number])
        self._conn.commit()
        print( "in insert in UserDAO step 5")


    def add_address(self, user_id, city, street, zip_code, floor, apartmentNumber):
        self._conn.execute(
            """INSERT INTO users_address (user_id, city, street, zip_code, floor, apt) VALUES (?,?,?,?,?,?)""",
            [user_id, city, street, zip_code, floor, apartmentNumber])
        self._conn.commit()
    def add_payment_method(self,user_id,credit_card,exp_date,cvv,card_type,id):
        self._conn.execute(
            """INSERT INTO users_payment (user_id,card_number,expire_date,cvv,card_type,id) VALUES (?,?,?,?,?,?)""",
            [user_id,credit_card, exp_date, cvv, card_type, id])
        self._conn.commit()
# update users_submission

    def unregister(self, user_id):
        self._conn.execute("""UPDATE users_submission set active = ? WHERE user_id = ?""",
                           [False, user_id])
        self._conn.commit()

    def log_in(self, user_id):
        self._conn.execute("""UPDATE user_submission set is_logged = ? WHERE user_id = ?""",
                           [True, user_id])
        self._conn.commit()

    def updateFirstname(self, id, name):
        self._conn.execute("""UPDATE users_submission set first_name = ? where user_id = ?""",
                           [name,id])
        self._conn.commit()
    def updateLastname(self, id, name):
        self._conn.execute("""UPDATE users_submission set last_name = ? where user_id = ?""",
                           [name,id])
        self._conn.commit()
    def updateUsername(self, id, name):
        self._conn.execute("""UPDATE users_submission set user_name = ? where user_id = ?""",
                           [name,id])
        self._conn.commit()
    def updatePassword(self, id, password):
        self._conn.execute("""UPDATE users_submission set password = ? where user_id = ?""",
                           [password,id])
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
        self._conn.execute("""UPDATE users_payment set id = ? where user_id = ?""",
                           [id, user_id])
        self._conn.commit()



# getters

    def usersFirst_Name(self, name):
        this = self._conn.cursor()
        output1 = this.execute("SELECT * FROM users WHERE users.first_name=?", [name])
        output = this.fetchone()

        return output

    def usersLast_Name(self, name):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users WHERE users.last_name=?", [name])
        output = this.fetchone()[0]

        return output

    def usersPassword(self, password):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users WHERE users.country=?", [password])
        output = this.fetchone()[0]

        return output

    def users_email(self, email):
        this = self._conn.cursor()
        this.execute("SELECT * FROM users WHERE users.email=?", [email])
        output = this.fetchone()[0]

        return output








