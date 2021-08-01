import sqlite3

from DB.database import users


class repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self._users = users(self._conn)

#create the tabels for SQL
    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            );
        """)



    def close(self):
        self._conn.commit()
        self._conn.close()

