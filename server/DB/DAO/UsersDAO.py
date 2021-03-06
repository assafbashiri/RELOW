class UsersDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert_guest(self, userDTO):
        self._conn.execute(
            """INSERT INTO users_submission (user_id, first_name, last_name, phone, email, password, birth_date, gender, active,seller) VALUES (?,?,?,?,?,?,?,?,?,?)""",
            [userDTO.user_id, userDTO.first_name, userDTO.last_name, userDTO.phone, userDTO.email, userDTO.password,
             userDTO.birth_date, userDTO.gender.value, userDTO.active, False])
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
            [userDTO.user_id, userDTO.credit_card_number, userDTO.credit_card_exp_date, userDTO.cvv,
             userDTO.card_type, userDTO.id_number])
        self._conn.commit()
        print("in insert in UserDAO step 5")

    def insert(self, userDTO):
        print("in insert in UserDAO step 1")
        self._conn.execute(
            """INSERT INTO users_submission (user_id, first_name, last_name, phone, email, password, birth_date, gender, active,seller) VALUES (?,?,?,?,?,?,?,?,?,?)""",
            [userDTO.user_id, userDTO.first_name, userDTO.last_name, userDTO.phone, userDTO.email, userDTO.password,
             userDTO.birth_date, userDTO.gender.value, userDTO.active, userDTO.seller])
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
            [userDTO.user_id, userDTO.credit_card_number, userDTO.credit_card_exp_date, userDTO.cvv,
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

    # def add_address(self, user_id, city, street, zip_code, floor, apartment_number):
    #     self.updateCity(user_id, city)
    #     self.updateStreet(user_id, street)
    #     self.updateZipcode(user_id, zip_code)
    #     self.updateFloor(user_id, floor)
    #     self.updateApartmentNumber(user_id, apartment_number)
    #     # self._conn.execute(
    #     # """INSERT INTO users_address (user_id, city, street, zip_code, floor, apt) VALUES (?,?,?,?,?,?)""",
    #     # [user_id, city, street, zip_code, floor, apartmentNumber])
    #     # self._conn.commit()
    #
    # def add_payment_method(self, user_id, credit_card, exp_date, cvv, card_type, id):
    #     self.updateCardNumber(user_id, credit_card)
    #     self.updateExpireDate(user_id, exp_date)
    #     self.updateCvv(user_id, cvv)
    #     self.updateCard_type(user_id, card_type)
    #     self.updateId(user_id, id)
    #     # self._conn.execute(
    #     # """UPDATE users_payment set card_number = ? ,expire_date = ? ,cvv = ? ,card_type = ? , id_number = ? WHERE user_id = ?""",
    #     # [credit_card, exp_date, cvv, card_type, id, user_id])
    #     # self._conn.commit()

    # update users_submission
    def complete_register(self, user_id):
        self._conn.execute("""UPDATE users_submission set active = ? WHERE user_id = ?""",
                           [True, user_id])
        self._conn.commit()

    def become_a_seller(self, user_id):
        self._conn.execute("""UPDATE users_submission set seller = ? WHERE user_id = ?""",
                           [True, user_id])
        self._conn.commit()

    def unregister(self, user_id):
        self._conn.execute("""UPDATE users_submission set active = ? WHERE user_id = ?""",
                           [False, user_id])
        self._conn.commit()

    def update(self, userDTO):
        self._conn.execute(
            """UPDATE users_submission SET first_name=?, last_name=?, phone=?, email=?, password=?, birth_date=?, gender=?, active=?, seller=? WHERE user_id=?""",
            [userDTO.first_name, userDTO.last_name, userDTO.phone, userDTO.email, userDTO.password,
             userDTO.birth_date, userDTO.gender.value, userDTO.active, userDTO.seller, userDTO.user_id])
        self._conn.commit()

        self._conn.execute(
            """UPDATE users_address SET city=?,street=?,zip_code=?,floor=?,apt=? WHERE user_id=? """,
            [userDTO.city, userDTO.street, userDTO.zip_code, userDTO.floor, userDTO.apartment_number, userDTO.user_id])
        self._conn.commit()

        self._conn.execute(
            """UPDATE users_payment SET card_number=?,expire_date=?,cvv=?,card_type=?, id_number=? WHERE user_id=?""",
            [userDTO.credit_card_number, userDTO.credit_card_exp_date, userDTO.cvv,
             userDTO.card_type, userDTO.id_number, userDTO.user_id])
        self._conn.commit()

    def delete_guest(self, guest_id):
        self._conn.execute("DELETE FROM users_submission WHERE user_id=?", [guest_id])
        self._conn.commit()
        self._conn.execute("DELETE FROM users_address WHERE user_id=?", [guest_id])
        self._conn.commit()
        self._conn.execute("DELETE FROM users_payment WHERE user_id=?", [guest_id])
        self._conn.commit()
        self._conn.execute("DELETE FROM users_extra_details WHERE user_id=?", [guest_id])
        self._conn.commit()
