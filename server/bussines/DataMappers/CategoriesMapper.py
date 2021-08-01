
from server.DB.DAO.CategoriesDAO import CategoriesDAO
from server.DB.DTO.CategoryDTO import CategoryDTO


class CategoriesMapper:

    def __init__(self, conn):
        self.dao = CategoriesDAO(conn)
      #  self.CategoriesMapper = singleton

    def addCategory(self, category):
        categoryDTO = CategoryDTO(category.category_id,category.name)
        self.dao.insert(categoryDTO)
        self.CategoriesMapper.put(category)


