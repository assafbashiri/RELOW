table_name = "sub_category"


class SubCategoriesDAO:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, sub_categoryDTO):
        self._conn.execute("""INSERT INTO sub_category (sub_category_id, category_id,name) VALUES (?,?,?)""",
                           [sub_categoryDTO.id, sub_categoryDTO.father_category_id, sub_categoryDTO.name])
        self._conn.commit()

    def delete(self, sub_category_to_remove):
        self._conn.execute("""DELETE FROM sub_category WHERE  sub_category_id = ? """, [sub_category_to_remove.id])
        self._conn.commit()

    def update(self, sub_category):
        self._conn.execute("""UPDATE sub_category set category_id = ? , name = ? where sub_category_id = ?""",
                           [sub_category.father_category_id, sub_category.name, sub_category.id])
        self._conn.commit()

    def load_sub_category_id(self):
        this = self._conn.cursor()
        this.execute("SELECT MAX(sub_category_id) FROM sub_category")
        output = this.fetchone()[0]
        if output is None:
            output = 0
        return output + 1

    def load_all_sub_categories(self):
        this = self._conn.cursor()
        this.execute("SELECT * FROM  sub_category")
        return this.fetchall()
