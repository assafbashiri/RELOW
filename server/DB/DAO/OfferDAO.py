class OfferDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, offer):
        self._conn.execute("""INSERT INTO offers (offer_id,current_step,user_id,category_id,subCategory_id,status,start_date,end_date)
         VALUES (?,?,?,?,?,?,?,?)""",
                           [offer.offer_id,offer.current_step,offer.user_id,offer.category_id,offer.subCategory_id,offer.status,offer.start_date,offer.end_date])
        self._conn.commit()
