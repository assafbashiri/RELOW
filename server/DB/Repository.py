import sqlite3

class repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')

    # create the tabels for SQL
    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS users_submission (
                user_id INTEGER PRIMARY KEY UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL  UNIQUE,
                password TEXT NOT NULL,
                valid BOOLEAN NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS users_extra_details (
                user_id	INTEGER NOT NULL,
                birth_date	INTEGER,
                gender	TEXT,
                PRIMARY KEY(user_id),
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );
            
            CREATE TABLE IF NOT EXISTS users_address (
                user_id	INTEGER NOT NULL UNIQUE,
                city TEXT NOT NULL,
                street TEXT NOT NULL,
                zip_code INTEGER NOT NULL,
                floor INTEGER NOY NULL,
                apt TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );
            
            CREATE TABLE IF NOT EXISTS users_payment (
                user_id	INTEGER NOT NULL UNIQUE,
                id_number INTGER NOT NULL  UNIQUE,
                card_number TEXT NOT NULL  UNIQUE,
                expire_date TEXT NOT NULL,
                cvv INTEGER NOT NULL,
                card_type TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );
            
            CREATE TABLE IF NOT EXISTS saved_offers (
                offer_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );
            
            CREATE TABLE IF NOT EXISTS offer_main (
                offer_id INTEGER PRIMART KEY  UNIQUE,
                user_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                status INTEGER NOT NULL,
                current_step INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                sub_category_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
                FOREIGN KEY(category_id) REFERENCES category(category_id)
                FOREIGN KEY(sub_category_id) REFERENCES sub_category(sub_category_id)
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
                PHOTO9 bolb,
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
                FOREIGN KEY(offer_id) REFERENCES offer_main(offer_id)
                FOREIGN KEY(user_id) REFERENCES users_submission(user_id)
            );
        """)



    def close(self):
        self._conn.commit()
        self._conn.close()
