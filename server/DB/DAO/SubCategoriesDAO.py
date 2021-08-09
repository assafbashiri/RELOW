table_name = "sub_category"
class SubCategoriesDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, sub_category):
        self._conn.execute("""INSERT INTO sub_category (sub_category_id, category_id,name) VALUES (?,?,?)""",
                           [sub_category.id,sub_category.father_category_id, sub_category.name])
        self._conn.commit()



    def delete(self, sub_category_to_remove):
        self._conn.execute("""DELETE FROM sub_category WHERE  sub_category_id = ? """, [sub_category_to_remove.id])
        self._conn.commit()


    def update(self,sub_category):
        self._conn.execute("""UPDATE sub_category set category_id = ? , name = ? where sub_category_id = ?""",
                           [sub_category.father_category_id, sub_category.name, sub_category.id])
        self._conn.commit()

