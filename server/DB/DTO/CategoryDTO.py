from BusinessLayer.Object import Category
class CategoryDTO:
    def __init__(self, category):
        self.id = category.get_id()
        self.name = category.get_name()