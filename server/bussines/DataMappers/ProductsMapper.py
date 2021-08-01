from server.DB.DAO.ProductDAO import ProductDAO
from server.DB.DTO.ProductDTO import ProductDTO


class ProductsMapper:

    def __init__(self, conn):
        self.dao = ProductDAO(conn)
      #  self.ProductsMapper = singleton



    def addProduct(self, product):
        productDTO = ProductDTO(product.offer_id,product.name, product.company, product.color, product.size, product.description, product.photos)
        self.dao.insert(productDTO)
        self.ProductsMapper.put(product)

    def updateName(self, product, name):
        self.dao.updateName(product.offer_id,name)
        self.ProductsMapper.get(product.offer_id).name = name

    def updateCompany(self, product, company):
        self.dao.updateCompany(product.offer_id,company)
        self.ProductsMapper.get(product.offer_id).company = company

    def updateColor(self, product, color):
        self.dao.updateColor(product.offer_id,color)
        self.ProductsMapper.get(product.offer_id).color = color

    def updateSize(self, product, size):
        self.dao.updateSize(product.offer_id,size)
        self.ProductsMapper.get(product.offer_id).size = size

    def updateDescription(self, product, description):
        self.dao.updateDescription(product.offer_id,description)
        self.ProductsMapper.get(product.offer_id).color = description

   # def updatePhoto(self, product, photo):
