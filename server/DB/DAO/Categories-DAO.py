class Categories_DAO:

    def __init__(self, conn):
        self._conn = conn

    def add(self, category):
        self._conn.execute("""INSERT INTO categories (id,name) VALUES (?,?)""",
                           [category.id, category.name])
        self._conn.commit()
