

class CategoriesDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, category):
        self._conn.execute("""INSERT INTO categories (id,name) VALUES (?,?)""",
                           [category.id, category.name])
        self._conn.commit()


    def delete(self, category):
        ###################################################### FIX
        self._conn.execute("""DELETE FROM categories WHERE  (id,name) VALUES (?,?)""",
                           [category.id, category.name])
        self._conn.commit()


    def updateName(self, id, name):
        self._conn.execute("""UPDATE categories set name = ? where id = ?""",
                           [id, name])
        self._conn.commit()