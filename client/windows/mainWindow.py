from datetime import datetime

from kivy.app import App
from kivy.core.image import Image
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
# from kivy.config import Config
# Config.set('kivy', 'exit_on_escape', '0')
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextFieldRound, MDTextField

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




class Manager(ScreenManager):
    screen_main = ObjectProperty(None)
    screen_account = ObjectProperty(None)
    screen_connect = ObjectProperty(None)
    screen_search = ObjectProperty(None)
    def back_to_main(self):
        self.current = "menu_screen"


class MessageBox(Popup):
    def __init__(self, name, company, description, product_size, color, steps,  photo_lis, current_buyers, offer_id, **kwargs):
        super(MessageBox, self).__init__(**kwargs)
        self.offer_id = offer_id
        self.title = name
        self.box = BoxLayout(orientation= 'vertical')
        self.carousel = Carousel(size_hint_y= 6)
        for photo in photo_lis:
            # image = Image(str(photo))
            self.carousel.add_widget(photo)
        image = AsyncImage(source="windows/images/a.png")
        self.carousel.add_widget(image)
        self.box.add_widget(self.carousel)
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 150
        self.slider.value = 15
        for step in steps:
            pass
        self.slider.min = 0
        self.slider.max = 100 #steps[-1][1]
        self.slider.value = current_buyers
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation = 'horizontal', size_hint_y=.2)
        for step in steps:
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step[0])))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step in steps:
            self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x = .1))
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step[1])))
        self.box.add_widget(self.price_per_step)
        self.name = Label(text = name)
        self.box.add_widget(self.name)
        self.company = Label(text = company)
        self.box.add_widget(self.company)
        self.description = Label(text = description)
        self.box.add_widget(self.description)
        self.product_size = Label(text = product_size)
        self.box.add_widget(self.product_size)
        self.color = Label(text = color)
        self.box.add_widget(self.color)
        self.join_offer = BoxLayout(orientation='horizontal')
        self.quantity = MDTextField(hint_text='QUANTITY')
        self.join = Button(text= "JOIN")
        print(self)
        self.join.bind(on_press= lambda x:print(self.join_()))
        self.join_offer.add_widget(self.quantity)
        self.join_offer.add_widget(self.join)
        self.box.add_widget(self.join_offer)
        self.back = Button(text="BACK")
        self.back.bind(on_press = lambda x:self.out())
        self.box.add_widget(self.back)
        self.add_widget(self.box)

    def out(self):
        self.dismiss()

    def join_(self):
        print('bolo')
        step = 0
        for checkbox in self.price_per_step.children:
            if type(checkbox) is MDCheckbox:
                if checkbox.active:
                    App.get_running_app().controller.add_active_buy_offer(self.offer_id, self.quantity, step)
                step +=1




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

    def insert_offers(self,hot_deals, **kwargs):
        # get the offer liat from the user
        # loop all the offer and add them to the recycl
        offers_list = []
        for offer in hot_deals:
            name = offer['name']
            company = offer['company']
            description = offer['description']
            product_size = offer['product_size']
            color = offer['color']
            photo_lis = []
            lis = offer['photos']
            steps = offer['steps']
            offer_id = offer['offer_id']
            current_buyers = offer['current_buyers']
            for photo in lis:
                image = AsyncImage(source = str(photo))
            photo_lis.append(image)
            offers_list.append({'name':name,
                                'company': company,
                                'description': description,
                                'product_size' : product_size,
                                'color' : color,
                                'photo_lis' : photo_lis,
                                'steps' : steps,
                                'current_buyers' : current_buyers,
                                'offer_id' : offer_id})
        offers_list.append({'name': "korki",
                            'company': "inokim",
                            'description': "good korki",
                            'product_size': "bolo",
                            'color': "green",
                            'photo_lis': [AsyncImage(source= 'windows/images/a.png'),
                                          AsyncImage(source= 'windows/images/b.png')],
                            'steps': [[10,4000] , [20,3500] , [30,3000]],
                            'current_buyers': 20,
                            'offer_id' : 1})
        # for on offers lis
        # create oofer
        # add offer to lis
        # set data to be lis
        self.data = offers_list
        # self.data[0]['more_details'].text = "bolo"



class Menu_box(BoxLayout):
    def __init__(self,**kwargs):
        super(Menu_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
    def exit(self):
        App.get_running_app().controller.exit()
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



class RecycleViewRow(RecycleDataViewBehavior,BoxLayout):
    name = StringProperty()
    company = StringProperty()
    description = StringProperty()
    product_size = StringProperty()
    color = StringProperty()
    photo_lis = ListProperty()
    steps = ListProperty()
    current_buyers = NumericProperty()
    offer_id = NumericProperty()
    # def __init__(self,**kwargs):
    #     super(RecycleViewRow, self).__init__(**kwargs)
    #     self.car = Carousel(direction='left', size_hint_y= 2)
    #     # for photo in kwargs['photos']:
    #     for photo in kwargs:
    #         self.car.add_widget(photo)
    #     self.add_widget(self.car)
    #     self.more_details = Button(text="more details",size_hint_y=.5 ,on_press= lambda a:self.www())
    #     self.more = Button(text="more", size_hint_y=.5 ,on_press= lambda a:self.insert())
    #     self.add_widget(self.more_details)
    #     self.add_widget(self.more)
    def insert(self, **kwargs):
        im = AsyncImage(source="windows/images/e.png")
        im1 = AsyncImage(source="windows/images/c.png")
        self.car.add_widget(im)

    def www(self,
            name,
            company,
            description,
            product_size,
            color, steps, photo_lis, current_buyers, offer_id):

        if hasattr(self, 'm'):
            self.m.open()
        else:
            self.m = MessageBox(name,
                           company,
                           description,
                           product_size,
                           color,
                           photo_lis,
                           steps,
                           current_buyers,
                           offer_id)
            self.m.open()



class Carousel2(Carousel):
    sourc = StringProperty()
    def __init__(self,**kwargs):
        super(Carousel2, self).__init__(**kwargs)



    def insert(self,  text):
        im = AsyncImage(source="windows/images/e.png")
        im1 = AsyncImage(source="windows/images/c.png")
        self.add_widget(im)

class Carousel1(Carousel):
    sourc = StringProperty()
    def __init__(self,**kwargs):
        super(Carousel1, self).__init__(**kwargs)

    def insert(self, **kwargs):
        print('name')
        im = AsyncImage(source="windows/images/e.png")
        im1 = AsyncImage(source="windows/images/c.png")
        self.add_widget(im)


class TestApp(MDApp):
    title = "RecycleView Direct Test"
    def __init__(self, controller):
        super(TestApp, self).__init__()
        self.controller = controller

    def build(self):
        #self.check_connection()
        return Manager()

    def check_connection(self):
        store = self.controller.store
        if store.exists('user'):
            user = store['user']['user_info']
            username = user['user_name']
            password = user['password']
            self.controller.login(username, password)
            print("welcome back")


