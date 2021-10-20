import io

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, CoreImage
from kivy.properties import StringProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.scrollview import ScrollView

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from windows.offerWindow import OfferScreen
from windows.updateOfferWindow import UPDATEOFFERScreen


class Offers_Screen(ScrollView):
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
            offer_to_add = RecycleViewRow(offer, photo_lis)
            self.ids.scroll_box.add_widget(offer_to_add)
        # self.data = offers_list
        # need to add the photos here
        Clock.schedule_once(self.bolo,0)
    def bolo(self, num):
        print('fuck')



class RecycleViewRow(GridLayout):
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
    offer = ObjectProperty()

    def __init__(self,offer, photo_lis, **kwargs):
        super(RecycleViewRow, self).__init__(**kwargs)
        # Clock.schedule_once(self.insert, 0)
        self.offer = offer
        self.photo_lis = photo_lis
        self.insert()


    def insert(self):
        self.ids.car.insert(self.photo_lis)


    def www(self,offer_list, photo_list):
        offer = self.offer
        offer_id = offer.offer_id
        screens_len = len(App.get_running_app().root.screens)
        screens = App.get_running_app().root.screens
        if offer.is_a_seller(App.get_running_app().controller.user_service.user_id):
            screen_name = 'update_offer_screen' + str(offer_id)
            for screen in screens:
                if screen.name == screen_name:
                    # screen.init_offer(offer, photo_list)
                    App.get_running_app().root.current = screen_name
                    return
            screens.append(UPDATEOFFERScreen())
            screens[screens_len].init_offer(offer, photo_list)
            App.get_running_app().root.current = screen_name
            #craete update_offer_screen
        else:
            screen_name = 'offer_screen'+str(offer_id)
            # check if there is a screen for this offer
            for screen in screens:
                if screen.name == screen_name:
                    App.get_running_app().root.current = screen_name
                    return
            # open new screen for this offer
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
