class OfferDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, offerDTO, productDTO):
        self._conn.execute("""INSERT INTO offers_main (offer_id,current_step,user_id,category_id,subCategory_id,status,start_date, end_date)
         VALUES (?,?,?,?,?,?,?,?)""",
                           [offerDTO.offer_id, offerDTO.current_step, offerDTO.user_id, offerDTO.category_id, offerDTO.subCategory_id,
                            offerDTO.status, offerDTO.start_date, offerDTO.end_date])
        self._conn.commit()
        self._conn.execute(
            """INSERT INTO products (offer_id,name, company, color, size, description, photos) VALUES (?,?,?,?,?,?,?)""",
            [productDTO.offer_id, productDTO.name, productDTO.company, productDTO.color, productDTO.size, productDTO.description,
             productDTO.photos])
        self._conn.commit()

    def get(self, offer):
        self._conn.execute("SELECT * FROM offers_main WHERE offer_main.offer_id=?", [offer.offer_id])
        self._conn.commit()

    def remove(self, offer):
        self._conn.execute("DELETE FROM offers_main WHERE offer_main.offer_id=?", [offer.offer_id])
        self._conn.commit()

    def add_active_buy_offer(self, offerDTO, user_id, quantity, step):
        self._conn.execute("""INSERT INTO buyers_in_offer_per_buyer (offer_id,user_id,quantity,step)
         VALUES (?,?,?,?)""",
                           [offerDTO.offer_id, user_id, quantity, step])
        self._conn.commit()

