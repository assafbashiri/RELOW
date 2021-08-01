class Product_DAO:

    def __init__(self, conn):
        self._conn = conn

    def add(self, product):
        self._conn.execute("""INSERT INTO products (offer_id,name, company, color, size, description, photos) VALUES (?,?,?,?,?,?,?)""",
                           [product.offer_id, product.name, product.company, product.color, product.size, product.description, product.photos])
        self._conn.commit()
