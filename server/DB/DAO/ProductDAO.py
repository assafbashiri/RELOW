class ProductDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, productDTO):
        self._conn.execute(
            """INSERT INTO products (offer_id,name, company, color, size, description, photos) VALUES (?,?,?,?,?,?,?)""",
            [productDTO.offer_id, productDTO.name, productDTO.company, productDTO.color, productDTO.size, productDTO.description,
             productDTO.photos])
        self._conn.commit()

    def update(self, product):
        self._conn.execute(
            """UPDATE INTO products (offer_id,name, company, color, size, description, photos) VALUES (?,?,?,?,?,?,?)""",
            [product.offer_id, product.name, product.company, product.color, product.size, product.description,
             product.photos])
        self._conn.commit()

    def update_name(self, offer):
        self._conn.execute("UPDATE active_offers SET name = ? WHERE offer_id = ?",
                           [offer.name, offer.offer_id])
        self._conn.commit()

    def update_company(self, offer):
        self._conn.execute("UPDATE active_offers SET company = ? WHERE offer_id = ?",
                           [offer.company, offer.offer_id])
        self._conn.commit()

    def update_color(self, offer):
        self._conn.execute("UPDATE active_offers SET color = ? WHERE offer_id = ?",
                           [offer.color, offer.offer_id])
        self._conn.commit()

    def update_size(self, offer):
        self._conn.execute("UPDATE active_offers SET size = ? WHERE offer_id = ?",
                           [offer.size, offer.offer_id])
        self._conn.commit()

    def update_description(self, offer):
        self._conn.execute("UPDATE active_offers SET description = ? WHERE offer_id = ?",
                           [offer.description, offer.offer_id])
        self._conn.commit()

    def update_photo1(self, offer):
        self._conn.execute("UPDATE active_offers SET photo1 = ? WHERE offer_id = ?",
                           [offer.photo1, offer.offer_id])
        self._conn.commit()

    def update_photo2(self, offer):
        self._conn.execute("UPDATE active_offers SET photo2 = ? WHERE offer_id = ?",
                           [offer.photo2, offer.offer_id])
        self._conn.commit()

    def update_photo3(self, offer):
        self._conn.execute("UPDATE active_offers SET photo3 = ? WHERE offer_id = ?",
                           [offer.photo3, offer.offer_id])
        self._conn.commit()

    def update_photo4(self, offer):
        self._conn.execute("UPDATE active_offers SET photo3 = ? WHERE offer_id = ?",
                           [offer.photo4, offer.offer_id])
        self._conn.commit()

    def update_photo5(self, offer):
        self._conn.execute("UPDATE active_offers SET photo3 = ? WHERE offer_id = ?",
                           [offer.photo5, offer.offer_id])
        self._conn.commit()

    def update_photo6(self, offer):
        self._conn.execute("UPDATE active_offers SET photo3 = ? WHERE offer_id = ?",
                           [offer.photo6, offer.offer_id])
        self._conn.commit()

    def update_photo7(self, offer):
        self._conn.execute("UPDATE active_offers SET photo3 = ? WHERE offer_id = ?",
                           [offer.photo7, offer.offer_id])
        self._conn.commit()

    def update_photo8(self, offer):
        self._conn.execute("UPDATE active_offers SET photo3 = ? WHERE offer_id = ?",
                           [offer.photo8, offer.offer_id])
        self._conn.commit()

    def update_photo9(self, offer):
        self._conn.execute("UPDATE active_offers SET photo9 = ? WHERE offer_id = ?",
                           [offer.photo9, offer.offer_id])
        self._conn.commit()

    def update_photo10(self, offer):
        self._conn.execute("UPDATE active_offers SET photo10 = ? WHERE offer_id = ?",
                           [offer.photo10, offer.offer_id])
        self._conn.commit()

    def load_all_products(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  products")
        return this.fetchall()

    def get(self, product):
        pass

    def remove(self, product):
        pass