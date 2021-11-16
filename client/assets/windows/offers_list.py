import io

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image, CoreImage
from kivy.core.image import Image as imm
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView

from kivymd.uix.button import MDIconButton
from kivymd.uix.imagelist import SmartTileWithLabel
from assets.windows.offerWindow import OfferScreen
from assets.windows.updateOfferWindow import UPDATEOFFERScreen


class Offers_Screen(ScrollView):
    def __init__(self, **kwargs):
        super(Offers_Screen, self).__init__(**kwargs)



    def insert_offers(self, offers):
        # get the offer list from the user
        # loop all the offer and add them to the recycle
        # child_len = len(self.ids.scroll_box.children)
        # for i in range (0, child_len):
        #     self.ids.scroll_box.children.pop()

        photos_index = App.get_running_app().controller.photos_index
        offers_list = []
        for offer in offers:
            self.ids.scroll_box.size_hint_y +=.8
            photo_lis = []
            lis = offer.product.photos
            for photo in lis:
                photo_lis.append(photo)
            offers_list.append({'offer': offer,
                                'photo_lis': photo_lis})
            offer_to_add = RecycleViewRow(offer, photo_lis, photos_index)
            self.ids.scroll_box.add_widget(offer_to_add)
            self.ids.scroll_box.size_hint_y +=1
            photos_index += 1

        #put in controller field "photo_index" the last index
        App.get_running_app().controller.photos_index = photos_index



class RecycleViewRow(SmartTileWithLabel):
    # caro = ObjectProperty()
    # name = StringProperty()
    # company = StringProperty()
    # description = StringProperty()
    # product_size = StringProperty()
    # color = StringProperty()
    # photo_lis = ListProperty()
    # steps = ListProperty()
    # current_buyers = NumericProperty()
    # offer_id = NumericProperty()
    # offer = ObjectProperty()

    def __init__(self,offer, photo_list, index, **kwargs):
        super(RecycleViewRow, self).__init__(**kwargs)
        # Clock.schedule_once(self.insert, 0)
        self.offer = offer
        self.photo_list = photo_list
        # self.overlap = False
        self.allow_stretch = True
        self.keep_ratio = False
        self.text = self.offer.product.name + "\n"+ self.offer.product.description
        self.box_color = (0, 0, 0, 0.2)
        self.size_hint_y = 0.2
        photo_main = self.insert2(photo_list[0])
        if photo_main is None:
            return

        address = f"assets/windows/images/test{index}.png"
        photo_main.save(address)
        self.source = address
        self.on_press= self.check


        btn = MDIconButton()
        btn.icon = "assets/windows/images/like.png"
        # self.add_widget(btn)
        #btn1 = Button(text='bolo')
        # btn1.size_hint = (.1,.1)
        # btn1.background_active = "assets/windows/images/like.png"
        # btn1.pos_hint = {'x':.8}
        # btn1.icon = "assets/windows/images/like.png"
        # btn1.padding = [200,0,0,0]
        # btn.padding = [450,100,0,0]
        # btn1.bind(on_press= lambda x:print('bolo'))
        # btn1.background_color = (0,0,0,0)
        # self.add_widget(btn1)
        # self.add_widget(btn, 2)
        self.lines = 2

        # self.insert()

    def check(self):
        print('wow')
    def insert(self):
        self.ids.car.insert(self.photo_list)

    def insert2(self,  photo):
        if photo is not None:
            image = photo
            data = io.BytesIO(image)
            data.seek(0)
            img = CoreImage(data, ext="png").texture

            new_img = imm(arg=img)
            # new_img.texture = img
            # new_img.allow_stretch = False
            return new_img


    def www(self):
        offer = self.offer
        offer_id = offer.offer_id
        screens_len = len(App.get_running_app().root.screens)
        screens = App.get_running_app().root.screens
        # if offer.is_a_seller(App.get_running_app().controller.user_service.user_id):
        #     screen_name = 'update_screen' + str(offer_id)
        #     for screen in screens:
        #         if screen.name == screen_name:
        #             # screen.init_offer(offer, photo_list)
                      #App.get_running_app().root.change_screen(screen_name)
        #             return
        #     screens.append(UPDATEOFFERScreen())
        #     screens[screens_len].init_offer(offer, self.photo_list)
        #    App.get_running_app().root.change_screen(screen_name)
        #     #craete update_screen
        # else:
        screen_name = 'offer_screen'+str(offer_id)
        # check if there is a screen for this offer
        for screen in screens:
            if screen.name == screen_name:
                App.get_running_app().root.change_screen(screen_name)
                return
            # open new screen for this offer
        screens.append(OfferScreen())
        screens[screens_len].init_offer(offer, self.photo_list)
        App.get_running_app().root.change_screen(screen_name)

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
                new_img.allow_stretch = False
                self.add_widget(new_img)


