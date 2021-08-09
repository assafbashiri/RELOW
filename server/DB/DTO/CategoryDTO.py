from BussinessLayer.Object import Category
class CategoryDTO:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __init__(self, category):
        self.id = category.id
        self.name = category.name