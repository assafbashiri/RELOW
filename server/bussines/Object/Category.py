
from bussines.Object import SubCategory

class Category:
    def __init__(self, name, nextId):
        self.sub_category_id = 0
        self.name = name
        self.category_id = nextId
        self.sub_list = None

    def add_sub_category(self, name):
        sub_category = SubCategory(name, self.sub_category_id)
        self.sub_list.add(self.sub_category_id, sub_category)
        self.sub_category_id += 1

    def remove_sub_category(self, sub_category_id):
        if self.sub_list.get(sub_category_id) is None:
            raise Exception("Sub Category does not exist")
        self.sub_list.remove(sub_category_id)
