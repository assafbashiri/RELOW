class CategoryService:
    def __init__(self, name, id, con):
        self.name = name
        self.id = id
        self.sub_categories_dictionary  = None


    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_sub_categories_dict(self):
        return self.sub_categories_dictionary

