from server.bussines.Object.SubCategory import SubCategory

category_id_counter = 0

def inc(num):
    num+=1
    category_id_counter = num


class Category:
    def __init__(self,name):
        self.category_id = category_id_counter
        inc(category_id_counter)
        self.sub_list = None

    def validName(self,name):

    def addSubCategory(self,name):
        self.sub_list.add(SubCategory(name))