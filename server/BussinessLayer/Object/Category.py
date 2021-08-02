from BussinesLayer.Objects.SubCategory import SubCategory
from BussinesLayer.DataMappers import SubCategoriesMapper


from server.BussinessLayer.Object.SubCategory import SubCategory
class Category:
    def _init_(self, name, nextId, con):
        self.sub_category_id = 0
        self.name = name
        self.category_id = nextId
        self.sub_category_mapper = SubCategoriesMapper(con)  #################

    def add_sub_category(self, name, category_id):
        sub_category_to_add = SubCategory(name, self.sub_category_id, category_id)
        self.sub_category_id += 1
        self.sub_category_mapper.add_sub_category(sub_category_to_add)


    def remove_sub_category(self, sub_category_id, category_id):
        if not self.sub_category_mapper.is_exist_sub_category(sub_category_id):
            raise Exception("Sub Category does not exist")
        self.sub_category_mapper.remove_sub_category(sub_category_id, category_id)

    def add_offer(self, user_id, product, category_id, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers ):
        if sub_category_id not in self.sub_list.keys():
            raise Exception("No Such Sub Category")
        self.sub_list.get(sub_category_id).add_offer(self, user_id, product,category_id, sub_category_id, status, price_per_step, amount_per_step, end_date, current_buyers )

    def update_sub_category_name(self, category_id, sub_category_id, new_sub_category_name):
        self.sub_category_mapper.update_sub_category_name(category_id, sub_category_id, new_sub_category_name)
        self.sub_list.remove(sub_category_id)