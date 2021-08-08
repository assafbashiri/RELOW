import sqlite3




class repository:
    def _init_(self, conn):
        self._conn = conn #sqlite3.connect('database.db')

    # create the tables for SQL
    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS users_submission (
                user_id INTEGER PRIMARY KEY UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                user_name TEXT NOT NULL,
                email TEXT NOT NULL  UNIQUE,
                password TEXT NOT NULL,
                birth_date	DATETIME,
                gender	TEXT,
                is_logged BOOLEAN NOT NULL,
                active BOOLEAN NOT NULL
            );

            CREATE TABLE IF NOT EXISTS users_extra_details (
                user_id	INTEGER NOT NULL,
                PRIMARY KEY(user_id),
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS users_address (
                user_id	INTEGER NOT NULL UNIQUE,
                city TEXT NOT NULL,
                street TEXT,
                zip_code INTEGER,
                floor INTEGER,
                apt TEXT,
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS users_payment (
                user_id	INTEGER NOT NULL UNIQUE,
                id_number INTEGER  UNIQUE,
                card_number TEXT UNIQUE,
                expire_date DATETIME,
                cvv INTEGER,
                card_type TEXT,
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS saved_offers (
                offer_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS offer_main (
                offer_id INTEGER PRIMARY KEY  UNIQUE,
                user_id INTEGER NOT NULL,
                start_date DATETIME NOT NULL,
                end_date DATETIME NOT NULL,
                status TEXT NOT NULL,
                current_step INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                sub_category_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
                FOREIGN KEY(category_id) REFERENCES category(category_id)
                FOREIGN KEY(sub_category_id) REFERENCES sub_category(sub_category_id)
            );

            CREATE TABLE IF NOT EXISTS price_per_step (
                offer_id INTEGER PRIMARY KEY  UNIQUE,
                step INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS offer_product (
                offer_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                company TEXT NOT NULL,
                color TEXT NOT NULL,
                size TEXT NOT NULL,
                description TEXT NOT NULL,
                photo1 BOLB,
                photo2 BOLB,
                photo3 BOLB,
                photo4 BOLB, 
                photo5 BOLB, 
                photo6 BOLB, 
                photo7 BOLB, 
                photo8 BOLB,
                PHOTO9 BOLB,
                photo10 BOLB,
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
            );

            CREATE TABLE IF NOT EXISTS category (
                category_id INTEGER PRIMARY KEY  UNIQUE,
                name TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS sub_category (
                sub_category_id INTEGER PRIMARY KEY  UNIQUE,
                category_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                FOREIGN KEY(category_id) REFERENCES category(category_id)
            );

            CREATE TABLE IF NOT EXISTS buyers_in_offer_per_buyer (
                offer_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                step INTEGER NOT NULL,
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS buyers_in_offer_total (
                offer_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                total_quantity INTEGER NOT NULL,
                step INTEGER NOT NULL,
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS history_buyers (
                user_id INTEGER NOT NULL,
                offer_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                step INTEGER NOT NULL,
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );

            CREATE TABLE IF NOT EXISTS history_sellers (
                user_id INTEGER NOT NULL,
                offer_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                step INTEGER NOT NULL,
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );
        """)

    def close(self):
        self._conn.commit()
        self._conn.close()