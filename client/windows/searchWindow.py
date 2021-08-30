from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen



class SEARCHScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'search_screen'
        super(SEARCHScreen, self).__init__(**kwargs)



class Offers_Screen_search(RecycleView):
    def __init__(self, **kwargs):
        super(Offers_Screen_search, self).__init__(**kwargs)
    def insert_offers(self):
        # get the offer liat from the user
        # loop all the offer and add them to the recycle
        self.data = [{} for x in range(20)]



class MessageBox(Popup):
    message1 = ObjectProperty()
    message2 = ObjectProperty()
    message2 = "windows/images/a.png"
    message1 = "ddd"

class Carousel1(Carousel):
    sourc = StringProperty()
    def __init__(self, **kwargs):
        super(Carousel1, self).__init__(**kwargs)

    def insert(self, **kwargs):
        im = AsyncImage(source="windows/images/e.png")
        im1 = AsyncImage(source="windows/images/c.png")
        self.add_widget(im)

class RecycleViewRow_search(BoxLayout):
    pass

class Category_box(BoxLayout):
    pass

class Search_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Search_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    def change_to_cat(self):
        self.side = self.children[0]
        self.remove_widget(self.side)
        self.add_widget(self.cat)

    def back_to_menu(self):
        self.add_widget(self.side)
        self.remove_widget(self.cat)

    def change_to_sub_cat(self):
        self.remove_widget(self.cat)
        self.add_widget(self.sub_cat)

    def back_to_cat(self):
        self.add_widget(self.cat)
        self.remove_widget(self.sub_cat)

    def search_by_name(self):
        prod_name = self.ids.name.text
        ans = App.get_running_app().controller.get_offers_by_product_name(prod_name)
        print('hello')

class Sub_Category_box(BoxLayout):
    pass

    def www(self):
        m = MessageBox().open("rrff")