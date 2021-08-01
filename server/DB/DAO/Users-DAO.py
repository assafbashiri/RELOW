class Users_DAO:

    def __init__(self, conn):
        self._conn = conn

    def add(self, user):
        self._conn.execute("""INSERT INTO users (id, first_name, last_name, username, email, password) VALUES (?,?,?,?,?,?)""",
                           [user.id,user.first_name, user.last_name, user.username, user.email, user.password])
        self._conn.commit()


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






