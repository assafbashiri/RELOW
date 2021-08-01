from bussines.Object import Category
class categoryController():
    def __init__(self):
        self.category_list = None
        self.category_id = 0
    def add_category(self, name):
        category_to_add = Category(name, self.category_id)
        self.category_list.add(self.category_id,category_to_add)
        self.category_id += 1

    def remove_category(self, category_id):
        if self.category_list.get(category_id) is None:
            raise Exception("category does not exist");
        self.category_list.get(category_id).key = None

    #addOffer
    #removeOffer