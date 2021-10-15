import io

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.image import Image, CoreImage
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from windows.offerWindow import OfferScreen


class Offers_Screen(RecycleView):
    def __init__(self, **kwargs):
        super(Offers_Screen, self).__init__(**kwargs)
        a = App.get_running_app()
    def insert_offers(self, **kwargs):
        # get the offer list from the user
        # loop all the offer and add them to the recycle
        offers_list = []
        for offer in kwargs['list']:
            name = offer.product.name
            company = offer.product.company
            description = offer.product.description
            photo_lis = []
            # for photo in offer.product.photos:
            #     photo_lis.append(photo)
            lis = offer.product.photos
            steps = [[10, 1000], [20, 500]]  # offer.steps
            offer_id = offer.offer_id
            if offer.current_buyers is None:
                current_buyers = 10
            else:
                current_buyers = offer.current_buyers
            # for photo in lis:
            #     image = AsyncImage(source = str(photo))
            #     photo_lis.append(image)
            for photo in lis:
                photo_lis.append(photo)
            offers_list.append({'offer': [offer],
                                'photo_lis': photo_lis})
        self.data = offers_list
        # need to add the photos here



class RecycleViewRow(RecycleDataViewBehavior,BoxLayout):
    # caro = ObjectProperty()
    name = StringProperty()
    company = StringProperty()
    description = StringProperty()
    product_size = StringProperty()
    color = StringProperty()
    photo_lis = ListProperty()
    steps = ListProperty()
    current_buyers = NumericProperty()
    offer_id = NumericProperty()
    offer = ListProperty()

    def __init__(self, **kwargs):
        super(RecycleViewRow, self).__init__(**kwargs)
        Clock.schedule_once(self.insert, 0)
    #     self.car = Carousel(direction='left', size_hint_y= 2)
    #     # for photo in kwargs['photos']:
    #     for photo in kwargs:
    #         self.car.add_widget(photo)
    #     self.add_widget(self.car)
    #     self.more_details = Button(text="more details",size_hint_y=.5 ,on_press= lambda a:self.www())
    #     self.more = Button(text="more", size_hint_y=.5 ,on_press= lambda a:self.insert())
    #     self.add_widget(self.more_details)
    #     self.add_widget(self.more)

    def insert(self, num):
        self.ids.car.insert(self.photo_lis)
        print('bolo')


    def www(self,offer, photo_list):
        offer_id = offer[0].offer_id
        screens_len = len(App.get_running_app().root.screens)
        screens = App.get_running_app().root.screens
        screen_name = 'offer_screen'+str(offer_id)
        for screen in screens:
            if screen.name == screen_name:
                App.get_running_app().root.current = screen_name
                return
        screens.append(OfferScreen())
        screens[screens_len].init_offer(offer, photo_list)
        App.get_running_app().root.current = screen_name


    def move_right(self):
        self.ids.car.load_next(mode='next')

    def move_left(self):
        self.ids.car.load_previous()


class Carousel2(Carousel):
    def __init__(self,**kwargs):
        super(Carousel2, self).__init__(**kwargs)

    def insert(self,  photos):
        for photo in photos:
            if photo is not None:
                image = photo
                data = io.BytesIO(image)
                data.seek(0)
                img = CoreImage(data, ext="png").texture

                new_img = Image()
                new_img.texture = img
                new_img.allow_stretch = True
                self.add_widget(new_img)
