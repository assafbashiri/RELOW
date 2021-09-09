from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior


from windows.offerWindow import OfferWindow


class Offers_Screen(RecycleView):
    def __init__(self, **kwargs):
        super(Offers_Screen, self).__init__(**kwargs)
        # self.insert_offers()

    def insert_offers(self, **kwargs):
        # get the offer liat from the user
        # loop all the offer and add them to the recycl
        offers_list = []
        for offer in kwargs['list']:
            name = offer.product.name
            company = offer.product.company
            description = offer.product.description
            product_size = offer.product.size
            color = offer.product.color
            photo_lis = []
            for photo in offer.product.photos:
                photo_lis.append(photo)
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
            photo_lis.append(AsyncImage(source='windows/images/a.png'))
            offers_list.append({'offer': [offer],
                                'photo_lis': photo_lis})
        # for on offers lis
        # create oofer
        # add offer to lis
        # set data to be lis
        self.data = offers_list
        # self.data[0]['more_details'].text = "bolo"


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
    offer = ListProperty()
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

    def www(self,offer, photo_list):
        if hasattr(self, 'm'):
            self.m = OfferWindow(offer, photo_list)
            self.m.open()
        else:
            self.m = OfferWindow(offer, photo_list)
            self.m.open()


class Carousel2(Carousel):
    sourc = StringProperty()
    def __init__(self,**kwargs):
        super(Carousel2, self).__init__(**kwargs)



    def insert(self,  text):
        im = AsyncImage(source="windows/images/e.png")
        im1 = AsyncImage(source="windows/images/c.png")
        self.add_widget(im)
