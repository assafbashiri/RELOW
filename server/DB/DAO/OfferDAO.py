class OfferDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, offerDTO, productDTO):
        self._conn.execute("""INSERT INTO offers_main (offer_id,current_step,user_id,category_id,sub_category_id,status,start_date, end_date, total_products)
         VALUES (?,?,?,?,?,?,?,?,?)""",
                           [offerDTO.offer_id, offerDTO.current_step, offerDTO.user_id, offerDTO.category_id, offerDTO.sub_category_id,
                            "aa", offerDTO.start_date, "aaaa", offerDTO.total_products])
        self._conn.commit()
        self._conn.execute(
            """INSERT INTO products (offer_id,name, company, color, size, description) VALUES (?,?,?,?,?,?)""",
            [productDTO.offer_id, productDTO.name, productDTO.company, productDTO.color, productDTO.size, productDTO.description
             ])
        self._conn.commit()
        for numOfStep in offerDTO.steps.keys():
            currStep = offerDTO.steps[numOfStep]
            self._conn.execute("""INSERT INTO steps_per_offer (offer_id ,step , quantity, price)
            VALUES (?,?,?,?)""",
                           [offerDTO.offer_id, numOfStep, currStep.get_products_amount(), currStep.get_price()])
            self._conn.commit()

    def get(self, offer):
        self._conn.execute("SELECT * FROM offers_main WHERE offer_main.offer_id=?", [offer.offer_id])
        self._conn.commit()

    def remove(self, offer):
        self._conn.execute("DELETE FROM offers_main WHERE offer_main.offer_id=?", [offer.offer_id])
        self._conn.commit()

    def update(self, offerDTO):
        self._conn.execute("""UPDATE offers_main set current_step=?,user_id=?,category_id=?,sub_category_id=?,status=?,start_date=?, end_date=?, total_products=?
         WHERE offer_id=?""",
                           [ offerDTO.current_step, offerDTO.user_id, offerDTO.category_id, offerDTO.sub_category_id,
                            offerDTO.status, offerDTO.start_date, offerDTO.end_date, offerDTO.total_products , offerDTO.offer_id])
        self._conn.commit()

    def add_active_buy_offer(self, offerDTO, user_id, quantity, step):
        self._conn.execute("""INSERT INTO buyers_in_offer_per_buyer (offer_id,user_id,quantity,step)
         VALUES (?,?,?,?)""",
                           [offerDTO.offer_id, user_id, quantity, step])
        self._conn.commit()


    def add_like_offer(self, user_id, offer_id):
        self._conn.execute("""INSERT INTO liked_offers (offer_id,user_id)
         VALUES (?,?)""",
                           [offer_id, user_id])
        self._conn.commit()

    def remove_like_offer(self, user_id, offer_id):
        self._conn.execute("DELETE FROM liked_offers WHERE offer_id = ? AND user_id = ?",
                           [offer_id, user_id])
        self._conn.commit()

    def delete_sale_offer(self, user_id, offer_id):
        self._conn.execute("""UPDATE users_submission set active = ? WHERE user_id = ?""",
                           [False, user_id])
        self._conn.commit()
        self._conn.execute("DELETE FROM liked_offers WHERE offer_id = ? AND user_id = ?",
                           [offer_id, user_id])
        self._conn.commit()


    def update_end_date(self,offer_id, new_end_date):
        self._conn.execute("""UPDATE offers_main set end_date = ? WHERE offer_id = ?""",
                           [new_end_date, offer_id])
        self._conn.commit()

    def update_start_date(self, offer_id, new_start_date):
        self._conn.execute("""UPDATE offers_main set start_date = ? WHERE offer_id = ?""",
                           [new_start_date, offer_id])
        self._conn.commit()

    def update_step(self, offer_id, step):
        self._conn.execute("""UPDATE offers_main set current_step = ? WHERE offer_id = ?""",
                           [step, offer_id])
        self._conn.commit()

    def update_step(self, offer_id, step):
        self._conn.execute("""UPDATE offers_main set current_step = ? WHERE offer_id = ?""",
                           [step, offer_id])
        self._conn.commit()

    def update_status(self, offer_id, status):
        self._conn.execute("""UPDATE offers_main set status = ? WHERE offer_id = ?""",
                           [status, offer_id])
        self._conn.commit()

    def update_product_name(self, offer_id, name):
        self._conn.execute("""UPDATE products set name = ? WHERE offer_id = ?""",
                           [name, offer_id])
        self._conn.commit()

    def update_product_company(self, offer_id, company):
        self._conn.execute("""UPDATE products set company = ? WHERE offer_id = ?""",
                           [company, offer_id])
        self._conn.commit()

    def update_product_color(self, offer_id, color):
        self._conn.execute("""UPDATE products set color = ? WHERE offer_id = ?""",
                           [color, offer_id])
        self._conn.commit()

    def update_product_size(self, offer_id, size):
        self._conn.execute("""UPDATE products set size = ? WHERE offer_id = ?""",
                           [size, offer_id])
        self._conn.commit()

    def update_product_description(self, offer_id, description):
        self._conn.execute("""UPDATE products set description = ? WHERE offer_id = ?""",
                           [description, offer_id])
        self._conn.commit()

    def update_status(self, offer_id, status):
        self._conn.execute("""UPDATE offers_main set status = ? WHERE offer_id = ?""",
                           [status, offer_id])
        self._conn.commit()



