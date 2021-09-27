class OfferDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, offerDTO, productDTO):
        s = offerDTO.status
        self._conn.execute("""INSERT INTO active_offers (offer_id,user_id,start_date,end_date,current_step,total_products,category_id,sub_category_id,hot_deals,confirm)
         VALUES (?,?,?,?,?,?,?,?,?,?)""",
                           [offerDTO.offer_id,offerDTO.user_id, offerDTO.start_date, offerDTO.end_date,offerDTO.current_step,offerDTO.total_products, offerDTO.category_id,
                            offerDTO.sub_category_id, offerDTO.hot_deals,offerDTO.confirm])
        self._conn.commit()
        colors = self.build_string_from_list(productDTO.colors)
        sizes = self.build_string_from_list(productDTO.sizes)

        photos_to_write = []
        for i in range(0,len(productDTO.photos)):
            photos_to_write.append(productDTO.photos[i])
        for i in range(len(productDTO.photos),10):
            photos_to_write.append(None)


        self._conn.execute(
            """INSERT INTO products (offer_id,name, company, colors, sizes, description,photo1,photo2,photo3,photo4,photo5, photo6,photo7,photo8,photo9,photo10) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            # [productDTO.offer_id, productDTO.name, productDTO.company, colors, sizes,productDTO.description,
             [int(2),"name" ,'company', 'colors', 'sizes', 'description', photos_to_write[0],photos_to_write[1],photos_to_write[2],photos_to_write[3],
             photos_to_write[4],photos_to_write[5],photos_to_write[6],photos_to_write[7],photos_to_write[8],photos_to_write[9]])
        self._conn.commit()
        for numOfStep in offerDTO.steps.keys():
            currStep = offerDTO.steps[numOfStep]
            self._conn.execute("""INSERT INTO steps_per_offer (offer_id ,step , step_limit, current_buyers, price)
            VALUES (?,?,?,?,?)""",
                               [offerDTO.offer_id, numOfStep, currStep.get_limit(),currStep.get_buyers_amount(), currStep.get_price()])
            self._conn.commit()

    def update(self, offerDTO):
        self._conn.execute("""UPDATE active_offers set user_id=?,start_date=?,end_date=?,current_step=?,total_products=?,category_id=?,sub_category_id=?,hot_deals=?,confirm=?
         where offer_id=?""",
                           [offerDTO.user_id, offerDTO.start_date, offerDTO.end_date, offerDTO.current_step, offerDTO.total_products, offerDTO.category_id,
                            offerDTO.sub_category_id, offerDTO.hot_deals, offerDTO.offer_id,offerDTO.confirm])
        self._conn.commit()
        productDTO = offerDTO.product
        colors = self.build_string_from_list(productDTO.colors)
        sizes = self.build_string_from_list(productDTO.sizes)
        self._conn.execute(
            """UPDATE products SET name=?, company=?, colors=?, sizes=?, description=? WHERE offer_id=?""",
            [productDTO.name, productDTO.company,colors, sizes,
             productDTO.description, productDTO.offer_id])
        self._conn.commit()
        for numOfStep in offerDTO.steps.keys():
            currStep = offerDTO.steps[numOfStep]
            self._conn.execute("""UPDATE steps_per_offer set step_limit=?,current_buyers=?, price=? where offer_id=? AND step=? """,
                               [currStep.get_limit(), currStep.get_buyers_amount(), currStep.get_price(), offerDTO.offer_id, numOfStep])
            self._conn.commit()

    def get(self, offer):
        self._conn.execute("SELECT * FROM active_offers WHERE offer_id=?", [offer.offer_id])
        self._conn.commit()

    def delete_active_offer(self, offer_id):
        self._conn.execute("DELETE FROM active_offers WHERE offer_id=?", [offer_id])
        self._conn.commit()

    def add_active_buy_offer(self, offerDTO, user_id, quantity, step, color, size, address):
        self._conn.execute("""INSERT INTO active_buyers (offer_id, user_id, quantity, step, color, size, address)
         VALUES (?,?,?,?,?,?,?)""", [offerDTO.offer_id, user_id, quantity, step, color, size, address])
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
        self._conn.execute("DELETE FROM active_buyers WHERE offer_id = ? AND user_id = ?",
                           [offer_id, user_id])
        self._conn.commit()

    # def update_end_date(self, offer_id, new_end_date):
    #     self._conn.execute("""UPDATE active_offers set end_date = ? WHERE offer_id = ?""",
    #                        [new_end_date, offer_id])
    #     self._conn.commit()
    #
    # def update_start_date(self, offer_id, new_start_date):
    #     self._conn.execute("""UPDATE active_offers set start_date = ? WHERE offer_id = ?""",
    #                        [new_start_date, offer_id])
    #     self._conn.commit()
    #
    # def update_step(self, offer_id, step):
    #     self._conn.execute("""UPDATE active_offers set current_step = ? WHERE offer_id = ?""",
    #                        [step, offer_id])
    #     self._conn.commit()
    #
    # def update_step(self, offer_id, step):
    #     self._conn.execute("""UPDATE active_offers set current_step = ? WHERE offer_id = ?""",
    #                        [step, offer_id])
    #     self._conn.commit()
    #
    # def update_product_name(self, offer_id, name):
    #     self._conn.execute("""UPDATE products set name = ? WHERE offer_id = ?""",
    #                        [name, offer_id])
    #     self._conn.commit()
    #
    # def update_product_company(self, offer_id, company):
    #     self._conn.execute("""UPDATE products set company = ? WHERE offer_id = ?""",
    #                        [company, offer_id])
    #     self._conn.commit()
    #
    # def update_product_colors(self, offer_id, colors1):
    #     colors = self.build_string_from_list(colors1)
    #     self._conn.execute("""UPDATE products set colors = ? WHERE offer_id = ?""",
    #                        [colors, offer_id])
    #     self._conn.commit()
    #
    # def update_product_sizes(self, offer_id, sizes1):
    #     sizes = self.build_string_from_list(sizes1)
    #     self._conn.execute("""UPDATE products set sizes = ? WHERE offer_id = ?""",
    #                        [sizes, offer_id])
    #     self._conn.commit()
    #
    # def update_product_description(self, offer_id, description):
    #     self._conn.execute("""UPDATE products set description = ? WHERE offer_id = ?""",
    #                        [description, offer_id])
    #     self._conn.commit()

    def insert_to_history_buyers(self, user_id, offer_id, status, step):
        self._conn.execute(
            """INSERT INTO history_buyers (user_id,offer_id,status,step) VALUES (?,?,?,?)""",
            [user_id, offer_id, status.name, step])

    def insert_to_history_offers(self, offer_dto):
        self._conn.execute(
            """INSERT INTO history_offers (offer_id,user_id,start_date,end_date,status,step,sold_products,category_id,sub_category_id,hot_deals,confirm) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            [offer_dto.offer_id, offer_dto.user_id, offer_dto.start_date, offer_dto.end_date, offer_dto.status.name,
             offer_dto.current_step, offer_dto.total_products, offer_dto.category_id, offer_dto.sub_category_id,
             offer_dto.hot_deals,offer_dto.confirm])

    def update_active_buy_offer(self, user_id, offer_id, quantity, step):
        self._conn.execute("""UPDATE active_buyers set quantity = ?, step =? WHERE offer_id = ? AND user_id = ?""",
                           [quantity, step, offer_id, user_id])
        self._conn.commit()

    def load_all_offers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM active_offers")
        return this.fetchall()

    def load_liked_offers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM liked_offers")
        return this.fetchall()

    def load_all_steps(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM steps_per_offer")
        return this.fetchall()

    def load_buyers_in_offers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM active_buyers")
        return this.fetchall()

    def load_history_sellers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  history_offers")
        return this.fetchall()

    def load_history_buyers(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  history_buyers")
        return this.fetchall()

    def load_offer_id(self):
        this = self._conn.cursor()
        this.execute("SELECT MAX(offer_id) FROM active_offers")
        output = this.fetchone()[0]
        if output is None:
            output = 0

        return output + 1

    def load_all_products(self):
        this = self._conn.cursor()
        m= this.execute("SELECT * FROM  products")
        # for x in m:
        #     rec = x[6]
        # with open("a.jpg","wb") as f:
        #     f.write(rec)
        return this.fetchall()

    def build_string_from_list(self, list):
        answer = list[0]
        i = 0
        for item in list:
            if i != 0:
                answer = answer + ", " + item
            i = i + 1
        return answer