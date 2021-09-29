class SubCategoryDTO:
    def __init__(self, sub_category):
        self.id = sub_category.get_id()
        self.father_category_id = sub_category.get_father_category_id()
        self.name = sub_category.get_name()