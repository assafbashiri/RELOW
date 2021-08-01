from server.DB.DAO.SubCategoriesDAO import SubCategoriesDAO
from server.DB.DTO.CategoryDTO import CategoryDTO


class SubCategoriesMapper:

    def __init__(self, conn):
        self.dao = SubCategoriesDAO(conn)
      #  self.subCategoriesMapper = singleton

    def addSubCategory(self, subCategory):
        categoryDTO = CategoryDTO(subCategory.category_id,subCategory.name)
        self.dao.insert(categoryDTO)
        self.subCategoriesMapper.put(subCategory)