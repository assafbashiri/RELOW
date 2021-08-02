class SubCategoriesDAO:

    def _init_(self, conn):
        self._conn = conn

    def insert(self, sub_category):
        self._conn.execute("""INSERT INTO SubCategories (id,name) VALUES (?,?)""",
                           [sub_category.id, sub_category.name])
        self._conn.commit()


       ############ check thissss
    def delete(self, sub_category_id, category_id):
        self._conn.execute("DELETE FROM %s \n" +
         "WHERE %s=\"%s\" AND %s=\"%s\";", "sub_categories", "category_id", category_id, "sub_category_id", sub_category_id);
        self._conn.commit()


    def update_name(self, sub_categoryDTO):
        self._conn.execute("""UPDATE sub_categories set name = ? where category_id = ? AND sub_category_id = ?""",
                           [sub_categoryDTO.name, sub_categoryDTO.categoty_id, sub_categoryDTO.id])
        self._conn.commit()

    def updateName(self, id, name):
        self._conn.execute("""UPDATE categories set name = ? where id = ?""",
                           [id, name])
        self._conn.commit()