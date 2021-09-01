
class CategoryService:
    def __init__(self, data):
        self.name = data['name']
        self.sub_categories_list_names = data['sub_categories_names']

    def get_name(self):
        return self.name

    def get_sub_categories_names(self):
        return self.sub_categories_list_names

