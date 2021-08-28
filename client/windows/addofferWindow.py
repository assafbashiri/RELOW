from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


class ADDOFFERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(ADDOFFERScreen, self).__init__(**kwargs)

class Category_box(BoxLayout):
    pass

class Add_offer_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Add_offer_box, self).__init__(**kwargs)
        self.cat = Category_box()

    def change(self):
        print(self.parent)
        self.side = self.ids.side_box
        self.remove_widget(self.side)
        print(self.parent)
        self.add_widget(self.cat)
        # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
        # print(self.parent)
        # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)

    def back(self):
        # self.remove_widget(self.ids.category_box)
        self.add_widget(self.side)
        self.remove_widget(self.cat)