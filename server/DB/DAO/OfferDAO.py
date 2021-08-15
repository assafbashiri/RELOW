class OfferDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, offerDTO, productDTO):
        s = offerDTO.status
        self._conn.execute("""INSERT INTO offers_main (offer_id,current_step,user_id,category_id,sub_category_id,status,start_date,end_date,total_products,hot_deals)
         VALUES (?,?,?,?,?,?,?,?,?,?)""",
                           [offerDTO.offer_id, offerDTO.current_step, offerDTO.user_id, offerDTO.category_id, offerDTO.sub_category_id,
                            offerDTO.status.name, offerDTO.start_date, offerDTO.end_date, offerDTO.total_products,0])
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
                           [offerDTO.current_step, offerDTO.user_id, offerDTO.category_id, offerDTO.sub_category_id,
                            offerDTO.status.name, offerDTO.start_date, offerDTO.end_date, offerDTO.total_products , offerDTO.offer_id])
        self._conn.commit()

    def add_active_buy_offer(self, offerDTO, user_id, quantity, step):
        self._conn.execute("""INSERT INTO buyers_in_offer_per_buyer (offer_id,user_id,quantity,step)
         VALUES (?,?,?,?)""", [offerDTO.offer_id,user_id,quantity,step])
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
        self._conn.execute("DELETE FROM liked_offers WHERE offer_id = ? AND user_id = ?",
                           [offer_id, user_id])
        self._conn.commit()

    def delete_buy_offer(self, user_id, offer_id):
        self._conn.execute("DELETE FROM buyers_in_offer_per_buyer WHERE offer_id = ? AND user_id = ?",
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
                           [status.name, offer_id])
        self._conn.commit()

    def insert_to_history_buyers(self, user_id, offer_id, status, step):
        self._conn.execute(
            """INSERT INTO history_buyers (user_id,offer_id,status,step) VALUES (?,?,?,?)""",
            [user_id, offer_id, status.name, step])

    def insert_to_history_sellers(self, user_id, offer_id, status, step):
        self._conn.execute(
            """INSERT INTO history_sellers (user_id,offer_id,status,step) VALUES (?,?,?,?)""",
            [user_id, offer_id, status.name, step])

    def update_active_buy_offer(self, user_id, offer_id, quantity, step):
        self._conn.execute("""UPDATE buyers_in_offer_per_buyer set quantity = ?, step =? WHERE offer_id = ? AND user_id = ?""",
                           [quantity, step, offer_id, user_id])
        self._conn.commit()

    def load_all_offers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  offers_main")
        return this.fetchall()

    def load_liked_offers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  liked_offers")
        return this.fetchall()

    def load_all_steps(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  steps")
        return this.fetchall()


    def load_buyers_in_offers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  buyers_in_offer_per_buyer")
        return this.fetchall()

    def load_history_sellers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  history_sellers")
        return this.fetchall()

    def load_history_buyers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  history_buyers")
        return this.fetchall()

    def load_offer_id(self):
        this = self._conn.cursor()
        this.execute("SELECT MAX(offer_id) FROM offers_main")
        output = this.fetchone()[0]
        if output is None:
            output = 0

        return output + 1