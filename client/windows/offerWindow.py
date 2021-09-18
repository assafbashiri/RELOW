import io

from kivy.app import App
from kivy.uix.image import Image, CoreImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField

# from Backend_controller import Backend_controller
from Service.Object.OfferService import OfferService


class OfferWindow(Popup):
    def __init__(self, offer, photo_lis, **kwargs):
        super(OfferWindow, self).__init__(**kwargs)
        self.controller = App.get_running_app().controller
        self.offer = offer[0]  # Offer Service
        self.offer_id = self.offer.offer_id
        self.color = 0
        # buyer/seller/viewer/user
        self.user = self.controller.user_service
        if self.controller.guest is True:
            self.show_as_guest(photo_lis)
        elif self.offer.is_a_seller(self.user.user_id):
            self.show_as_seller(photo_lis)
        elif self.user.is_a_buyer(self.offer.offer_id):
            self.show_as_buyer(photo_lis)
        else:
            self.show_as_viewer(photo_lis)

    def show_as_guest(self, photo_lis):
        print('as a guest')
        self.title = self.offer.product.name
        self.box = BoxLayout(orientation='vertical')
        self.carousel = Carousel(size_hint_y=6)
        # for photo in photo_lis:
        #     self.carousel.add_widget(photo)
        image = AsyncImage(source="windows/images/a.png")
        self.carousel.add_widget(image)
        self.box.add_widget(self.carousel)
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 150
        self.slider.value = 15
        steps = self.offer.steps
        # for step in steps:
        #     pass
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step.get_buyers_amount())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)


        for step in steps:
            step = steps[step_id]
            # self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1))
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))
        self.box.add_widget(self.price_per_step)
        self.name = Label(text=self.offer.product.name)
        self.box.add_widget(self.name)
        self.company = Label(text=self.offer.product.company)
        self.box.add_widget(self.company)
        self.description = Label(text=self.offer.product.description)
        self.box.add_widget(self.description)

        self.color_size = BoxLayout(orientation='horizontal')
        self.box.add_widget(self.color_size)

        self.color_dropdown = DropDown()
        colors = self.offer.product.colors
        for color in colors:
            btn = Button(text=' % s' % color, size_hint=(None, None), height=40)
            btn.bind(on_release=lambda btn: self.color_dropdown.select(btn.text))
            self.color_dropdown.add_widget(btn)
        self.color_mainbutton = Button(text='colors')
        self.color_mainbutton.bind(on_release=self.color_dropdown.open)
        self.color_size.add_widget(self.color_mainbutton)
        self.color_dropdown.bind(on_select=lambda instance, x: setattr(self.color_mainbutton, 'text', x))

        self.size_dropdown = DropDown()
        sizes = self.offer.product.sizes
        for size in sizes:
            btn = Button(text=' % s' % size, size_hint=(None, None), height=40)
            btn.bind(on_release=lambda btn: self.size_dropdown.select(btn.text))
            self.size_dropdown.add_widget(btn)
        self.size_mainbutton = Button(text='sizes')
        self.size_mainbutton.bind(on_release=self.size_dropdown.open)
        self.color_size.add_widget(self.size_mainbutton)
        self.size_dropdown.bind(on_select=lambda instance, x: setattr(self.size_mainbutton, 'text', x))
        self.join_offer = BoxLayout(orientation='horizontal')
        self.quantity = MDTextField(hint_text='QUANTITY')
        self.join = Button(text="JOIN")
        self.join.bind(on_press=lambda x: self.register())
        self.join_offer.add_widget(self.quantity)
        self.join_offer.add_widget(self.join)
        # self.box.add_widget(self.join_offer)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x: self.out())
        self.box.add_widget(self.back)
        if self.user.is_a_liker(self.offer_id):
            self.like = Button(text="UNLIKE")
        else:
            self.like = Button(text="LIKE")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.box.add_widget(self.like)
        self.add_widget(self.box)

    def show_as_seller(self, photo_lis):
        print("as a seller")
        self.title = self.offer.product.name
        self.box = BoxLayout(orientation='vertical')
        self.carousel = Carousel(size_hint_y=6)
        # for photo in photo_lis:
        #     self.carousel.add_widget(photo)
        for photo in photo_lis:
            image = photo
            # f = open("img.jpg", 'rb')
            #
            # binary_data = f.read()  # image opened in binary mode

            data = io.BytesIO(image)
            data.seek(0)
            img = CoreImage(data, ext="png").texture

            new_img = Image()
            new_img.texture = img
            self.carousel.add_widget(new_img)
        self.box.add_widget(self.carousel)
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 150
        self.slider.value = 15
        steps = self.offer.steps
        # for step in steps:
        #     pass
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(MDLabel(text='people:' +str(step.get_buyers_amount())+'/'+str(step.get_limit())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step in steps:
            step = steps[step_id]
            self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1))
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))
        self.box.add_widget(self.price_per_step)
        self.name = Label(text=self.offer.product.name)
        self.box.add_widget(self.name)
        self.company = Label(text=self.offer.product.company)
        self.box.add_widget(self.company)
        self.description = Label(text=self.offer.product.description)
        self.box.add_widget(self.description)
        self.color_dropdown = DropDown()
        colors = self.offer.product.colors
        for color in colors:
            btn = Button(text=' % s' % color, size_hint=(None, None), height=40)
            btn.bind(on_release=lambda btn: self.color_dropdown.select(btn.text))
            self.color_dropdown.add_widget(btn)
        self.color_mainbutton = Button(text='colors', size_hint=(None, None), pos=(350, 300))
        self.color_mainbutton.bind(on_release=self.color_dropdown.open)
        self.color_mainbutton = Button(text='colors', size_hint=(None, None), pos=(350, 300))
        self.color_mainbutton.bind(on_release=self.color_dropdown.open)
        self.color_box = BoxLayout(orientation='horizontal')
        self.color_box.add_widget(self.color_mainbutton)
        self.box.add_widget(self.color_box)
        self.add_color = Button(text='add color')
        self.color_box.add_widget(self.add_color)
        self.color_dropdown.bind(on_select=lambda instance, x: setattr(self.color_mainbutton, 'text', x))

        self.size_dropdown = DropDown()
        sizes = self.offer.product.sizes
        for size in sizes:
            btn = Button(text=' % s' % size, size_hint=(None, None), height=40)
            btn.bind(on_release=lambda btn: self.size_dropdown.select(btn.text))
            self.size_dropdown.add_widget(btn)
        self.size_mainbutton = Button(text='sizes', size_hint=(None, None), pos=(400, 300))
        self.size_mainbutton.bind(on_release=self.size_dropdown.open)
        self.box.add_widget(self.size_mainbutton)
        self.size_dropdown.bind(on_select=lambda instance, x: setattr(self.size_mainbutton, 'text', x))
        self.join_offer = BoxLayout(orientation='horizontal')
        # self.quantity = MDTextField(hint_text='QUANTITY')
        self.update = Button(text="UPDATE")
        self.update.bind(on_press=lambda x: print(self.update_offer()))
        # self.join_offer.add_widget(self.quantity)
        self.join_offer.add_widget(self.update)
        self.box.add_widget(self.join_offer)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x: self.out())
        self.box.add_widget(self.back)
        self.add_widget(self.box)

    def show_as_buyer(self, photo_lis):
        print('as a buyer')
        purchases = self.offer.get_current_buyers()
        purchase =  None
        for purch in purchases:
            p = purchases[purch]
            if p.buyer_id == self.user.user_id:
                purchase = p
        print("bolo2")
        self.title = self.offer.product.name
        self.box = BoxLayout(orientation='vertical')
        self.carousel = Carousel(size_hint_y=6)
        # for photo in photo_lis:
        #     self.carousel.add_widget(photo)
        image = AsyncImage(source="windows/images/a.png")
        self.carousel.add_widget(image)
        self.box.add_widget(self.carousel)
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 150
        self.slider.value = 15
        steps = self.offer.steps
        # for step in steps:
        #     pass
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step.get_buyers_amount())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step in steps:
            step = steps[step_id]
            self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1))
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))


        self.box.add_widget(self.price_per_step)
        self.name = Label(text=self.offer.product.name)
        self.box.add_widget(self.name)
        self.company = Label(text=self.offer.product.company)
        self.box.add_widget(self.company)
        self.description = Label(text=self.offer.product.description)
        self.box.add_widget(self.description)
        self.product_size = MDTextField(hint_text=purchase.size)
        self.box.add_widget(self.product_size)
        self.color = MDTextField(hint_text=purchase.color)
        self.box.add_widget(self.color)
        self.join_offer = BoxLayout(orientation='horizontal')
        self.quantity = MDTextField(hint_text='QUANTITY')
        self.unjoin = Button(text="UPDATE")
        self.unjoin.bind(on_press=lambda x: print(self.update_purchase()))
        self.join_offer.add_widget(self.quantity)
        self.join_offer.add_widget(self.unjoin)
        self.box.add_widget(self.join_offer)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x: self.out())
        self.box.add_widget(self.back)

        if self.user.is_a_liker(self.offer_id):
            self.like = Button(text="UNLIKE")
        else:
            self.like = Button(text="LIKE")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.box.add_widget(self.like)
        self.add_widget(self.box)

    def show_as_viewer(self, photo_lis):
        print('as a viewer')
        self.title = self.offer.product.name
        self.box = BoxLayout(orientation='vertical')
        self.carousel = Carousel(size_hint_y=6)
        # for photo in photo_lis:
        #     self.carousel.add_widget(photo)
        image = AsyncImage(source="windows/images/a.png")
        self.carousel.add_widget(image)
        self.box.add_widget(self.carousel)
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 150
        self.slider.value = 15
        steps = self.offer.steps
        # for step in steps:
        #     pass
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step.get_buyers_amount())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step in steps:
            step = steps[step_id]
            self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1))
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))
        self.box.add_widget(self.price_per_step)
        self.name = Label(text=self.offer.product.name)
        self.box.add_widget(self.name)
        self.company = Label(text=self.offer.product.company)
        self.box.add_widget(self.company)
        self.description = Label(text=self.offer.product.description)
        self.box.add_widget(self.description)

        self.color_size = BoxLayout(orientation='horizontal')
        self.box.add_widget(self.color_size)

        self.color_dropdown = DropDown()
        colors = self.offer.product.colors
        for color in colors:
            btn = Button(text='%s' % color, size_hint=(None,None))
            btn.bind(on_release=lambda btn: self.color_dropdown.select(btn.text))
            self.color_dropdown.add_widget(btn)
        self.color_mainbutton = Button(text='colors')
        self.color_mainbutton.bind(on_release=self.color_dropdown.open)

        self.color_size.add_widget(self.color_mainbutton)
        self.color_dropdown.bind(on_select=lambda instance, x: setattr(self.color_mainbutton, 'text', x))

        self.size_dropdown = DropDown()
        sizes = self.offer.product.sizes
        for size in sizes:
            btn = Button(text='%s' % size, size_hint=(None, None))
            btn.bind(on_release=lambda btn: self.size_dropdown.select(btn.text))
            self.size_dropdown.add_widget(btn)
        self.size_mainbutton = Button(text='sizes')
        self.size_mainbutton.bind(on_release=self.size_dropdown.open)
        self.color_size.add_widget(self.size_mainbutton)
        self.size_dropdown.bind(on_select=lambda instance, x: setattr(self.size_mainbutton, 'text', x))

        self.join_offer = BoxLayout(orientation='horizontal')
        self.quantity = MDTextField(hint_text='QUANTITY')
        self.join = Button(text="JOIN")
        self.join.bind(on_press=lambda x: print(self.join_()))
        self.join_offer.add_widget(self.quantity)
        self.join_offer.add_widget(self.join)
        self.box.add_widget(self.join_offer)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x: self.out())
        self.box.add_widget(self.back)
        if self.user.is_a_liker(self.offer_id):
            self.like = Button(text="UNLIKE")
        else:
            self.like = Button(text="LIKE")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.box.add_widget(self.like)
        self.add_widget(self.box)

    def register(self):
        self.dismiss()
        a = App.get_running_app()
        a.root.current = 'connect_screen'
        toast(' you need to register first')
        b= 2

    # def open(self, offer, photo_lis):
    #     print('bolo4')
    #     if offer == 'just':f
    #         Popup.open(self)
    #     else:
    #         if self.offer.is_a_seller(self.user.user_id):
    #             self.show_as_seller(photo_lis)
    #         elif self.user.is_a_buyer(self.user.user_id):
    #             self.show_as_buyer(photo_lis)
    #         else:
    #             self.show_as_viewer(photo_lis)
    #         Popup.open(self)
    def out(self):
        self.dismiss()

    def dismiss(self):
        print('bolo10')
        Popup.dismiss(self)

    def like_unlike(self):
        print('in like')
        if self.user.is_a_liker(self.offer_id):
            self.controller.remove_liked_offer(self.offer_id)
            self.like.text = 'LIKE'

        else:
            self.controller.add_liked_offer(self.offer_id)
            self.like.text = 'UNLIKE'

    def join_(self):
        step = 0
        for checkbox in self.price_per_step.children:
            if type(checkbox) is MDCheckbox:
                if checkbox.active:
                    a = self.offer_id
                    b = self.quantity.text
                    c = step
                    d = self.color_mainbutton.text
                    e = self.size_mainbutton.text
                    f = 5
                    ans = App.get_running_app().controller.add_active_buy_offer(self.offer_id, int(self.quantity.text), int(step), self.color_mainbutton.text, self.size_mainbutton.text)
                    if ans.res is True:
                        self.user.get_active_buy_offers().append(self.offer)
                        self.offer = ans.data
                        x = 5
                        return
                step += 1

    def update_purchase(self):
        self.controller.update_purchase(self.offer_id, self.quantity.text, self.step.text, self.color.text,
                                        self.size.text)

    def update_offer(self):
        self.dismiss()
        App.get_running_app().root.current = 'add_offer_screen'
        c = App.get_running_app().root
        e = App.get_running_app().root.screens
        f = App.get_running_app().root.screens[4]
        f = App.get_running_app().root.screens[4].update_offer(self.offer)

        d = 5
        print('bolo- need to update offer for seller')


# class offerWindow(Screen):
#     def __init__(self, controller):
#         self.controller = Backend_controller()
#         self.offer = OfferService()
#         # self.controller = controller
#
#     # seller methods
#
#     def update_sub_category_for_offer(self):
#         offer_id = self.offer.get_offer_id()
#         sub_category_id = ""
#         ans = self.controller.update_sub_category_for_offer(offer_id, sub_category_id)
#         res = Struct(**ans)
#
#     def update_end_date(self):
#         end_date = ""
#         offer_id = self.offer.get_offer_id()
#         ans = self.controller.update_end_date(offer_id, end_date)
#         res = Struct(**ans)
#
#     def update_product_company(self):
#         company = ""
#         offer_id = self.offer.get_offer_id()
#         ans = self.controller.update_product_company(offer_id, company)
#         res = Struct(**ans)
#
#     def update_product_name(self):
#         offer_id = self.offer.get_offer_id()
#         name = ""
#         ans = self.controller.update_product_name(offer_id, name)
#         res = Struct(**ans)
#
#     def update_product_color(self):
#         offer_id = self.offer.get_offer_id()
#         color = ""
#         ans = self.controller.update_product_color(offer_id, color)
#         res = Struct(**ans)
#
#     def update_product_size(self):
#         offer_id = self.offer.get_offer_id()
#         size = ""
#         ans = self.controller.update_product_size(offer_id, size)
#         res = Struct(**ans)
#
#     def update_product_description(self):
#         offer_id = self.offer.get_offer_id()
#         description = ""
#         ans = self.controller.update_product_description(offer_id, description)
#         res = Struct(**ans)
#
#     def add_photo(self):
#         offer_id = self.offer.get_offer_id()
#         photo = ""
#         ans = self.controller.add_photo(offer_id, photo)
#         res = Struct(**ans)
#
#     def remove_photo(self):
#         offer_id = self.offer.get_offer_id()
#         photo = ""
#         ans = self.controller.remove_photo(offer_id, photo)
#         res = Struct(**ans)
#
#     # buyer methods
#
#     def update_step(self):
#         offer_id = self.offer.get_offer_id()
#         step = ""
#         ans = self.controller.update_step(offer_id, step)
#         res = Struct(**ans)
#
#     def add_liked_offer(self):
#         offer_id = self.offer.get_offer_id()
#         ans = self.controller.add_liked_offer(offer_id)
#         res = Struct(**ans)
#
#     def remove_liked_offer(self):
#         offer_id = self.offer.get_offer_id()
#         ans = self.controller.remove_liked_offer(offer_id)
#         res = Struct(**ans)
#
#
