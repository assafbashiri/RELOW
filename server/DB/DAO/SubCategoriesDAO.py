class SubCategoriesDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, SubCategory):
        self._conn.execute("""INSERT INTO SubCategories (id,name) VALUES (?,?)""",
                           [SubCategory.id, SubCategory.name])
        self._conn.commit()
