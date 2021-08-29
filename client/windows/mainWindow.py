from datetime import datetime

from kivy.app import App
from kivy.core.image import Image
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel

from windows.accountWindow import ACCOUNTScreen
from windows.connectWindow import CONNECTScreen
from windows.searchWindow import SEARCHScreen
from windows.addofferWindow import ADDOFFERScreen

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)




class MENUScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(MENUScreen, self).__init__(**kwargs)

    def www(self):
        m = MessageBox().open()


class Manager(ScreenManager):
    screen_main = ObjectProperty(None)
    screen_account = ObjectProperty(None)
    screen_connect = ObjectProperty(None)
    screen_search = ObjectProperty(None)
    def back_to_main(self):
        self.current = "menu_screen"


class MessageBox(Popup):
    def __init__(self, **kwargs):
        super(MessageBox, self).__init__(**kwargs)
        self.box = BoxLayout(orientation= 'vertical')
        self.carousel = Carousel()
        for photo in kwargs:
            image = Image(str(photo))
            self.carousel.add_widget(image)
        self.box.add_widget(self.carousel)
        self.name = Label(text= "name")
        self.box.add_widget(self.name)
        self.company = "company"
        self.description = "description"
        self.product_size = "size"
        self.color = "color"




class Side_box(BoxLayout):
    pass
class Category_box(BoxLayout):
    pass
class Sub_Category_box(BoxLayout):
    pass
class Offers_Screen_main(RecycleView):
    def __init__(self, **kwargs):
        super(Offers_Screen_main, self).__init__(**kwargs)
        self.insert_offers()

    def insert_offers(self, **kwargs):
        # get the offer liat from the user
        # loop all the offer and add them to the recycle

        self.data = [{} for x in range(2)]


class Menu_box(BoxLayout):
    def __init__(self,**kwargs):
        super(Menu_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()

    def change_to_cat(self):
        print(self.parent)
        self.side = self.ids.side_box
        self.remove_widget(self.side)
        print(self.parent)
        self.add_widget(self.cat)
        # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
        # print(self.parent)
        # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)
    def back_to_menu(self):
        # self.remove_widget(self.ids.category_box)
        self.add_widget(self.side)
        self.remove_widget(self.cat)

    def change_to_sub_cat(self):
        self.remove_widget(self.cat)
        self.add_widget(self.sub_cat)
    def back_to_cat(self):
        self.add_widget(self.cat)
        self.remove_widget(self.sub_cat)

    def message_box(self, message):
        p = MessageBox()
        p.message = message
        p.open()
        print('test press: ', message)


class RecycleViewRow(BoxLayout):
    text1 = StringProperty(name = "dd")
    def __init__(self,**kwargs):
        super(RecycleViewRow, self).__init__(**kwargs)
        self.car = Carousel(direction='left', size_hint_y= 2)
        # for photo in kwargs['photos']:
        for photo in kwargs:
            self.car.add_widget(photo)
        self.add_widget(self.car)
        # self.add_widget(Label(text=kwargs['name']))
        self.add_widget(MDLabel(text="name",size_hint_y= .5))
        # self.add_widget(Label(text=kwargs['company']))
        self.add_widget(MDLabel(text="company",size_hint_y= .5))
        # self.add_widget(Label(text=kwargs['description']))
        self.add_widget(MDLabel(text="description",size_hint_y= .5))
        # self.add_widget(Label(text=kwargs['size']))
        self.add_widget(MDLabel(text="size",size_hint_y= .5))
        # self.add_widget(Label(text=kwargs['photo']))
        self.more_details = Button(text="more details",size_hint_y=.5 ,on_press= lambda a:self.www())
        self.more = Button(text="more", size_hint_y=.5 ,on_press= lambda a:self.insert())
        self.add_widget(self.more_details)
        self.add_widget(self.more)
    def insert(self, **kwargs):
        im = AsyncImage(source="windows/images/e.png")
        im1 = AsyncImage(source="windows/images/c.png")
        self.car.add_widget(im)

    def www(self):
        m = MessageBox().open()



class Carousel1(Carousel):
    sourc = StringProperty()
    def __init__(self,**kwargs):
        super(Carousel1, self).__init__(**kwargs)
    def insert(self, **kwargs):
        im = AsyncImage(source="windows/images/e.png")
        im1 = AsyncImage(source="windows/images/c.png")
        self.add_widget(im)



class TestApp(MDApp):
    title = "RecycleView Direct Test"

    def __init__(self, controller, store):
        super(TestApp, self).__init__()
        self.controller = controller
        self.store = store

    def build(self):
        return Manager()

    def login(self):
        # self.root.ids.login_label.text = f'hi {self.root.ids.user.text}'
        username = self.root.ids.user.text
        password = self.root.ids.password.text
        # call to log in with username and password

    def clear_login(self):
        # self.root.ids.login_label.text="Log In"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def clear_register(self):
        # self.root.ids.login_label.text="Log In"
        self.root.ids.first_name.text = ""
        self.root.ids.last_name.text = ""
        self.root.ids.user_name.text = ""
        self.root.ids.email.text = ""
        self.root.ids.password.text = ""
        self.root.ids.birth_date.text = ""
        self.root.ids.gender.text = ""


