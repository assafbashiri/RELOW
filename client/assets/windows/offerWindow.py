import io
# import pandas as pd
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout

from assets.Utils.Utils import Utils
from kivy.app import App
from kivy.uix.image import Image, CoreImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField
from kivy.graphics import Color, Rectangle

# from Backend_controller import Backend_controller

from assets.windows.paymentWindow import PAYMENTScreen
from assets.windows.updateOfferWindow import UPDATEOFFERScreen


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class OfferScreen(Screen):
    def __init__(self, **kwargs):
        super(OfferScreen, self).__init__(**kwargs)
        self.name = "offer_screen"

    def init_offer(self, offer, photo_lis):
        self.photo_lis = photo_lis
        self.name = self.name + str(offer.offer_id)
        self.controller = App.get_running_app().controller
        self.offer = offer  # Offer Service
        self.offer_id = self.offer.offer_id
        self.color = 0
        self.num_of_quantity = 0
        self.change = False
        self.new_address = None
        # buyer/seller/viewer/user
        self.user = self.controller.user_service

        if self.controller.guest is True:
            self.show_as_guest(photo_lis)
        elif self.user.is_a_seller(self.offer.offer_id):
            self.show_as_seller(photo_lis)
        elif self.user.is_a_buyer(self.offer.offer_id):
            self.show_as_buyer(photo_lis)
        else:
            self.show_as_viewer(photo_lis)
        return

    def show_as_guest(self, photo_lis):
        print('as a guest')
        self.scroll = ScrollView(do_scroll_y = True, size_hint = (1,1))
        self.add_widget(self.scroll)
        self.box = BoxLayout(orientation='vertical', size_hint_y = 1.5)

        # title box
        self.title = BoxLayout(orientation = 'horizontal',size_hint_y = .1)
        self.back = MDIconButton(icon="assets/windows/images/back_btn.png", pos_hint={'top':.6})
        self.back.bind(on_press=lambda x: self.out())
        self.product_name = MDLabel(text=" " + self.offer.product.name, pos_hint={'top':.3})
        self.product_name.bold = True
        self.product_name.font_size = 45
        self.product_name.color = (0, 0, 0, 1)
        self.product_name.halign = 'center'
        self.product_name.valign = 'bottom'
        self.title.add_widget(self.back)
        self.title.add_widget(self.product_name)

        # label_spacing1 = MDLabel(text='', size_hint_x = .4)
        # self.title.add_widget(label_spacing1)

        self.box.add_widget(self.title)
        # photo_box
        self.picture_box = BoxLayout(orientation='horizontal')
        self.carousel = Carousel(size_hint_y=1, direction='right')
        self.left_arr = MDIconButton(icon = "assets/windows/images/left.png", pos_hint ={'top':.6})
        self.left_arr.bind(on_press = lambda x:self.carousel.load_previous())
        self.right_arr = MDIconButton(icon = "assets/windows/images/right.png", pos_hint = {'top': .6})
        self.right_arr.bind(on_press=self.carousel.load_next)
        self.insert_photos(self.carousel, photo_lis)
        self.box.add_widget(self.picture_box)
        self.picture_box.add_widget(self.left_arr)
        self.picture_box.add_widget(self.carousel)
        self.picture_box.add_widget(self.right_arr)
        # steps
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        steps = self.offer.steps
        self.steps_box = BoxLayout(orientation='vertical', size_hint_y=.4)
        self.steps_box.padding = [0, 15, 0, 0]
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.5)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(
                MDLabel(text='people:' + str(step.get_buyers_amount()) + "/" + str(step.get_limit())))
        self.steps_box.add_widget(self.people_per_step)
        self.steps_box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            x = MDCheckbox(group="price")
            x.bind(active=self.set_total_price)
            self.price_per_step.add_widget(x)
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))
        self.steps_box.add_widget(self.price_per_step)
        self.box.add_widget(self.steps_box)

        # labels box
        self.labels_box = BoxLayout(orientation='vertical')
        self.labels_box.size_hint_y = 1
        self.labels_box.padding = [0, 40, 0, 0]

        self.company_name = MDLabel(text="  " + self.offer.product.company, size_hint_y = .2)
        self.company_name.color = (0, 0, 0, 0.27)
        self.company_name.halign = 'center'
        self.company_name.valign = 'bottom'
        self.labels_box.add_widget(self.company_name)

        self.description = MDLabel(text="  " + self.offer.product.description, size_hint_y = 1)
        self.description.color = (0, 0, 0, 0.27)
        self.description.halign = 'center'
        self.description.valign = 'top'
        self.labels_box.add_widget(self.description)

        self.box.add_widget(self.labels_box)
        # colors and sizes
        self.color_size = BoxLayout(orientation='vertical')
        self.color_size.size_hint_y = 0.1
        # self.color_size.spacing= 25
        self.box.add_widget(self.color_size)
        self.chosen_colors = {}
        self.chosen_sizes = {}
        # icons box

        self.icons_box = BoxLayout()
        self.icons_box.padding = [20,0,20,0]
        self.icons_box.size_hint_y = .1
        self.another_item = MDIconButton(icon="assets/windows/images/add.png")
        self.another_item.bind(on_press=lambda x: print(self.add_item()))

        self.icons_box.add_widget(self.another_item)

        label_spacing1 = MDLabel(text='')
        self.icons_box.add_widget(label_spacing1)

        self.remove = MDIconButton(icon="assets/windows/images/minus.png")
        self.remove.bind(on_press=lambda x: self.remove_item())
        self.icons_box.add_widget(self.remove)

        label_spacing2 = MDLabel(text='')
        self.icons_box.add_widget(label_spacing2)

        if self.user.is_a_liker(self.offer_id):
            self.like = MDIconButton(icon="assets/windows/images/unlike.png")
        else:
            self.like = MDIconButton(icon="assets/windows/images/like.png")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.icons_box.add_widget(self.like)

        self.box.add_widget(self.icons_box)

        # price
        self.curr_price = MDLabel(text="price")
        self.curr_price.size_hint_y = 0.2
        self.curr_price.valign = 'center'
        self.curr_price.halign = 'center'
        self.box.add_widget(self.curr_price)

        self.add_item()

        # join button
        self.join_offer = BoxLayout(orientation='vertical')
        self.join_offer.size_hint_y = .4
        self.join_offer.padding = [40,40,40,40]
        self.join = Button(text="JOIN")
        self.join.background_normal =''
        self.join.background_color = (24 / 255, 211 / 255, 199 / 255, 1)


        self.join.bind(on_press=lambda x: self.guest_try_to_join())
        self.join_offer.add_widget(self.join)

        self.box.add_widget(self.join_offer)

        self.scroll.add_widget(self.box)

    def show_as_seller(self, photo_lis):
        print("as a seller")
        self.scroll = ScrollView(do_scroll_y=True, size_hint=(1, 1))
        self.add_widget(self.scroll)
        self.box = BoxLayout(orientation='vertical', size_hint_y=1.5)

        # title box
        self.title = BoxLayout(orientation='horizontal', size_hint_y=.1)
        self.back = MDIconButton(icon="assets/windows/images/back_btn.png", pos_hint={'top': .6})
        self.back.bind(on_press=lambda x: self.out())
        self.product_name = MDLabel(text=" " + self.offer.product.name, pos_hint={'top': .3})
        self.product_name.bold = True
        self.product_name.font_size = 45
        self.product_name.color = (0, 0, 0, 1)
        self.product_name.halign = 'center'
        self.product_name.valign = 'bottom'
        self.title.add_widget(self.back)
        self.title.add_widget(self.product_name)

        # label_spacing1 = MDLabel(text='', size_hint_x = .4)
        # self.title.add_widget(label_spacing1)

        self.box.add_widget(self.title)
        # photo_box
        self.picture_box = BoxLayout(orientation='horizontal')
        self.carousel = Carousel(size_hint_y=1, direction='right')
        self.left_arr = MDIconButton(icon="assets/windows/images/left.png", pos_hint={'top': .6})
        self.left_arr.bind(on_press=lambda x: self.carousel.load_previous())
        self.right_arr = MDIconButton(icon="assets/windows/images/right.png", pos_hint={'top': .6})
        self.right_arr.bind(on_press=self.carousel.load_next)
        self.insert_photos(self.carousel, photo_lis)
        self.box.add_widget(self.picture_box)
        self.picture_box.add_widget(self.left_arr)
        self.picture_box.add_widget(self.carousel)
        self.picture_box.add_widget(self.right_arr)
        # steps
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        steps = self.offer.steps
        self.steps_box = BoxLayout(orientation='vertical', size_hint_y=.4)
        self.steps_box.padding = [0, 15, 0, 0]
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.5)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(
                MDLabel(text='people:' + str(step.get_buyers_amount()) + "/" + str(step.get_limit())))
        self.steps_box.add_widget(self.people_per_step)
        self.steps_box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            x = MDCheckbox(group="price")
            x.bind(active=self.set_total_price)
            self.price_per_step.add_widget(x)
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))
        self.steps_box.add_widget(self.price_per_step)
        self.box.add_widget(self.steps_box)

        # labels box
        self.labels_box = BoxLayout(orientation='vertical')
        self.labels_box.size_hint_y = 1
        self.labels_box.padding = [0, 40, 0, 0]

        self.company_name = MDLabel(text="  " + self.offer.product.company, size_hint_y=.2)
        self.company_name.color = (0, 0, 0, 0.27)
        self.company_name.halign = 'center'
        self.company_name.valign = 'bottom'
        self.labels_box.add_widget(self.company_name)

        self.description = MDLabel(text="  " + self.offer.product.description, size_hint_y=1)
        self.description.color = (0, 0, 0, 0.27)
        self.description.halign = 'center'
        self.description.valign = 'top'
        self.labels_box.add_widget(self.description)

        self.box.add_widget(self.labels_box)
        # colors and sizes
        self.color_size = BoxLayout(orientation='vertical')
        self.color_size.size_hint_y = 0.1
        # self.color_size.spacing= 25
        self.box.add_widget(self.color_size)
        self.chosen_colors = {}
        self.chosen_sizes = {}
        # icons box

        self.icons_box = BoxLayout()
        self.icons_box.padding = [20, 0, 20, 0]
        self.icons_box.size_hint_y = .1
        self.another_item = MDIconButton(icon="assets/windows/images/add.png")
        self.another_item.bind(on_press=lambda x: print(self.add_item()))

        self.icons_box.add_widget(self.another_item)

        label_spacing1 = MDLabel(text='')
        self.icons_box.add_widget(label_spacing1)

        self.remove = MDIconButton(icon="assets/windows/images/minus.png")
        self.remove.bind(on_press=lambda x: self.remove_item())
        self.icons_box.add_widget(self.remove)

        label_spacing2 = MDLabel(text='')
        self.icons_box.add_widget(label_spacing2)

        if self.user.is_a_liker(self.offer_id):
            self.like = MDIconButton(icon="assets/windows/images/unlike.png")
        else:
            self.like = MDIconButton(icon="assets/windows/images/like.png")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.icons_box.add_widget(self.like)

        self.box.add_widget(self.icons_box)

        # price
        self.curr_price = MDLabel(text="price")
        self.curr_price.size_hint_y = 0.2
        self.curr_price.valign = 'center'
        self.curr_price.halign = 'center'
        self.box.add_widget(self.curr_price)

        self.add_item()

        # join button
        self.join_offer = BoxLayout(orientation='vertical')
        self.join_offer.size_hint_y = .4
        self.join_offer.padding = [40, 40, 40, 40]
        self.join = Button(text="JOIN")
        self.join.background_normal = ''

        self.join.bind(on_press=lambda x: self.guest_try_to_join())
        self.join_offer.add_widget(self.join)

        self.box.add_widget(self.join_offer)

        self.scroll.add_widget(self.box)
        # self.size_mainbutton = Button(text='sizes', size_hint=(None, None), pos=(400, 300))
        # self.size_mainbutton.bind(on_release=self.size_dropdown.open)
        # # self.box.add_widget(self.size_mainbutton)
        # self.size_dropdown.bind(on_select=lambda instance, x: setattr(self.size_mainbutton, 'text', x))
        # self.join_offer = BoxLayout(orientation='horizontal')
        # # self.quantity = MDTextField(hint_text='QUANTITY')
        self.update1 = Button(text="UPDATE")
        self.update1.bind(on_press=lambda x: self.update_offer())
        self.join_offer.add_widget(self.update1)
        # # self.join_offer.add_widget(self.quantity)
        # self.join_offer.add_widget(self.update)
        # self.remove_offer_bt = Button(text="REMOVE OFFER")
        # self.remove_offer_bt.bind(on_press=lambda x: self.remove_offer())
        # # self.join_offer.add_widget(self.quantity)
        # self.join_offer.add_widget(self.remove_offer_bt)
        # self.box.add_widget(self.join_offer)
        # self.back = Button(text="BACK")
        # self.back.bind(on_press=lambda x: self.out())
        # self.box.add_widget(self.back)
        # self.add_widget(self.box)

    def show_as_buyer(self, photo_lis):
        print('as a buyer')
        purchases = self.offer.get_current_buyers()
        for purch in purchases:
            p = purchases[purch]
            if p.buyer_id == self.user.user_id:
                self.purchase = p
                break
        self.scroll = ScrollView(do_scroll_y=True, size_hint=(1, 1))
        self.add_widget(self.scroll)
        self.box = BoxLayout(orientation='vertical', size_hint_y=1.5)
        # title box
        self.title = BoxLayout(orientation='horizontal', size_hint_y=.1)
        self.back = MDIconButton(icon="assets/windows/images/back_btn.png", pos_hint={'top': .6})
        self.back.bind(on_press=lambda x: self.out())
        self.product_name = MDLabel(text=" " + self.offer.product.name, pos_hint={'top': .3})
        self.product_name.bold = True
        self.product_name.font_size = 45
        self.product_name.color = (0, 0, 0, 1)
        self.product_name.halign = 'center'
        self.product_name.valign = 'bottom'
        self.title.add_widget(self.back)
        self.title.add_widget(self.product_name)
        self.box.add_widget(self.title)
        # photo list
        self.picture_box = BoxLayout(orientation='horizontal')
        self.carousel = Carousel(size_hint_y=1, direction='right')
        self.left_arr = MDIconButton(icon="assets/windows/images/left.png", pos_hint={'top': .6})
        self.left_arr.bind(on_press=lambda x: self.carousel.load_previous())
        self.right_arr = MDIconButton(icon="assets/windows/images/right.png", pos_hint={'top': .6})
        self.right_arr.bind(on_press=self.carousel.load_next)
        self.insert_photos(self.carousel, photo_lis)
        self.box.add_widget(self.picture_box)
        self.picture_box.add_widget(self.left_arr)
        self.picture_box.add_widget(self.carousel)
        self.picture_box.add_widget(self.right_arr)
        # steps
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        steps = self.offer.steps
        self.steps_box = BoxLayout(orientation='vertical', size_hint_y=.4)
        self.steps_box.padding = [0, 15, 0, 0]
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.5)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(
                MDLabel(text='people:' + str(step.get_buyers_amount()) + "/" + str(step.get_limit())))
        self.steps_box.add_widget(self.people_per_step)
        self.steps_box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            if self.purchase.step_id == step.step_number:
                self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1, active=True))
            else:
                self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1))
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))
        self.steps_box.add_widget(self.price_per_step)
        self.box.add_widget(self.steps_box)
        # steps
        # self.slider = MDSlider()
        # self.slider.min = 0
        # self.slider.max = 100  # steps[-1][1]
        # self.slider.value = 10  # self.offer.current_buyers
        # steps = self.offer.steps
        # self.progress = MDProgressBar()
        # self.progress.size_hint_y = 0.2
        # self.progress.value = self.slider.value
        # self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        # self.people_per_step.size_hint_y = 0.2
        # for step_id in steps:
        #     step = steps[step_id]
        #     self.people_per_step.add_widget(
        #         MDLabel(text='people:' + str(step.get_buyers_amount()) + "/" + str(step.get_limit())))
        # self.box.add_widget(self.people_per_step)
        # self.box.add_widget(self.progress)
        # self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        # for step_id in steps:
        #     step = steps[step_id]
        #     if self.purchase.step_id == step.step_number:
        #         self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1, active=True))
        #     else:
        #         self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1))
        #     self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))

        # self.box.add_widget(self.price_per_step)

        # labels box
        self.labels_box = BoxLayout(orientation='vertical')
        self.labels_box.size_hint_y = 1
        self.labels_box.padding = [0, 40, 0, 0]

        self.company_name = MDLabel(text="  " + self.offer.product.company, size_hint_y=.2)
        self.company_name.color = (0, 0, 0, 0.27)
        self.company_name.halign = 'center'
        self.company_name.valign = 'bottom'
        self.labels_box.add_widget(self.company_name)

        self.description = MDLabel(text="  " + self.offer.product.description, size_hint_y=1)
        self.description.color = (0, 0, 0, 0.27)
        self.description.halign = 'center'
        self.description.valign = 'top'
        self.labels_box.add_widget(self.description)

        self.box.add_widget(self.labels_box)


        # price


        # colors and sizes
        self.color_size = BoxLayout(orientation='vertical', size_hint_y=.1)
        self.color_size.pos_hint = {'top': 1}
        self.box.add_widget(self.color_size)

        size_lis = self.split_str(self.purchase.size)
        color_lis = self.split_str(self.purchase.color)

        self.chosen_colors = {}
        self.chosen_sizes = {}

        # icons box
        self.icons_box = BoxLayout()
        self.icons_box.padding = [20, 0, 20, 0]
        self.icons_box.size_hint_y = .1
        self.another_item = MDIconButton(icon="assets/windows/images/add.png")
        self.another_item.bind(on_press=lambda x: print(self.add_item()))

        self.icons_box.add_widget(self.another_item)

        label_spacing1 = MDLabel(text='')
        self.icons_box.add_widget(label_spacing1)

        self.remove = MDIconButton(icon="assets/windows/images/minus.png")
        self.remove.bind(on_press=lambda x: self.remove_item())
        self.icons_box.add_widget(self.remove)

        label_spacing2 = MDLabel(text='')
        self.icons_box.add_widget(label_spacing2)

        if self.user.is_a_liker(self.offer_id):
            self.like = MDIconButton(icon="assets/windows/images/unlike.png")
        else:
            self.like = MDIconButton(icon="assets/windows/images/like.png")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.icons_box.add_widget(self.like)

        self.box.add_widget(self.icons_box)

        self.curr_price = MDLabel(text="price")
        self.curr_price.size_hint_y = 0.2
        self.curr_price.valign = 'center'
        self.curr_price.halign = 'center'
        self.box.add_widget(self.curr_price)

        quan = self.purchase.quantity
        for i in range(0, quan):
            self.add_item_for_update(color_lis[i], size_lis[i], i+1)




        # cancel & update buttons
        self.cancel_update = BoxLayout(orientation='vertical', size_hint_y = .4)

        self.cancel_update.spacing = 10
        # update button
        self.update = Button(text="UPDATE")
        self.update.background_normal = ''
        self.update.background_color = (24 / 255, 211 / 255, 199 / 255, 1)
        self.update.bind(on_press=lambda x: self.update_purchase())
        # cancel button
        self.cancel = Button(text='CANCEL')
        self.cancel.bind(on_press=lambda x: self.cancel_purchase())
        self.cancel.background_normal = ''
        self.cancel.background_color = (24 / 255, 211 / 255, 199 / 255, 1)

        self.cancel_update.add_widget(self.update)
        self.cancel_update.add_widget(self.cancel)
        self.box.add_widget(self.cancel_update)
        self.scroll.add_widget(self.box)

    def show_as_viewer(self, photo_lis):
        print('as a viewer')
        self.scroll = ScrollView(do_scroll_y=True, size_hint=(1, 1))
        self.add_widget(self.scroll)
        self.box = BoxLayout(orientation='vertical', size_hint_y=1.5)
        # title box
        self.title = BoxLayout(orientation='horizontal', size_hint_y=.1)
        self.back = MDIconButton(icon="assets/windows/images/back_btn.png", pos_hint={'top': .6})
        self.back.bind(on_press=lambda x: self.out())
        self.product_name = MDLabel(text=" " + self.offer.product.name, pos_hint={'top':.3})
        self.product_name.bold = True
        self.product_name.font_size = 45
        self.product_name.color = (0, 0, 0, 1)
        self.product_name.halign = 'left'
        self.product_name.valign = 'bottom'
        self.title.add_widget(self.back)
        self.title.add_widget(self.product_name)
        self.box.add_widget(self.title)
        # photo_box
        self.picture_box = BoxLayout(orientation='horizontal')
        self.carousel = Carousel(size_hint_y=1, direction='right')
        self.left_arr = MDIconButton(icon="assets/windows/images/left.png", pos_hint={'top': .6})
        self.left_arr.bind(on_press=lambda x: self.carousel.load_previous())
        self.right_arr = MDIconButton(icon="assets/windows/images/right.png", pos_hint={'top': .6})
        self.right_arr.bind(on_press=self.carousel.load_next)
        self.insert_photos(self.carousel, photo_lis)
        self.box.add_widget(self.picture_box)
        self.picture_box.add_widget(self.left_arr)
        self.picture_box.add_widget(self.carousel)
        self.picture_box.add_widget(self.right_arr)
        # steps
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        steps = self.offer.steps
        self.steps_box = BoxLayout(orientation='vertical', size_hint_y=.4)
        self.steps_box.padding = [0, 15, 0, 0]
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.5)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(
                MDLabel(text='people:' + str(step.get_buyers_amount()) + "/" + str(step.get_limit())))
        self.steps_box.add_widget(self.people_per_step)
        self.steps_box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            x = MDCheckbox(group="price")
            x.bind(active=self.set_total_price)
            self.price_per_step.add_widget(x)
            self.price_per_step.add_widget(MDLabel(text="price: " + str(step.get_price())))
        self.steps_box.add_widget(self.price_per_step)
        self.box.add_widget(self.steps_box)

        # labels box
        self.labels_box = BoxLayout(orientation='vertical')
        self.labels_box.size_hint_y = 1
        self.labels_box.padding = [0, 40, 0, 0]

        self.company_name = MDLabel(text="  " + self.offer.product.company, size_hint_y=.2)
        self.company_name.color = (0, 0, 0, 0.27)
        self.company_name.halign = 'center'
        self.company_name.valign = 'bottom'
        self.labels_box.add_widget(self.company_name)

        self.description = MDLabel(text="  " + self.offer.product.description, size_hint_y=1)
        self.description.color = (0, 0, 0, 0.27)
        self.description.halign = 'center'
        self.description.valign = 'top'
        self.labels_box.add_widget(self.description)

        self.box.add_widget(self.labels_box)
        # colors and sizes
        self.color_size = BoxLayout(orientation='vertical')
        self.color_size.size_hint_y = 0.1
        # self.color_size.spacing= 25
        self.box.add_widget(self.color_size)
        self.chosen_colors = {}
        self.chosen_sizes = {}
        # icons box

        self.icons_box = BoxLayout()
        self.icons_box.padding = [20, 0, 20, 0]
        self.icons_box.size_hint_y = .1
        self.another_item = MDIconButton(icon="assets/windows/images/add.png")
        self.another_item.bind(on_press=lambda x: print(self.add_item()))

        self.icons_box.add_widget(self.another_item)
        label_spacing1 = MDLabel(text='')

        self.icons_box.add_widget(label_spacing1)
        self.remove = MDIconButton(icon="assets/windows/images/minus.png")
        self.remove.bind(on_press=lambda x: self.remove_item())
        self.icons_box.add_widget(self.remove)

        label_spacing2 = MDLabel(text='')
        self.icons_box.add_widget(label_spacing2)
        if self.user.is_a_liker(self.offer_id):
            self.like = MDIconButton(icon="assets/windows/images/unlike.png")
        else:
            self.like = MDIconButton(icon="assets/windows/images/like.png")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.icons_box.add_widget(self.like)

        self.box.add_widget(self.icons_box)

        # price
        self.curr_price = MDLabel(text="price")
        self.curr_price.size_hint_y = 0.2
        self.curr_price.valign = 'center'
        self.curr_price.halign = 'center'
        self.box.add_widget(self.curr_price)

        self.add_item()

        # join button
        self.join_offer = BoxLayout(orientation='vertical')
        self.join_offer.size_hint_y = .6
        self.join_offer.padding = [40,40,40,40]
        self.join_offer.spacing = 20
        self.join = Button(text="JOIN")
        self.join.background_normal = ''
        self.join.background_color = (24 / 255, 211 / 255, 199 / 255, 1)
        self.join.bind(on_press=lambda x: self.join_())
        # another address button
        self.other_address = Button(text='NEW ADDRESS FOR THIS PRODUCT')
        self.other_address.bind(on_press=lambda x: self.add_address())
        self.other_address.background_normal = ''
        self.other_address.background_color = (24 / 255, 211 / 255, 199 / 255, 1)
        self.join_offer.add_widget(self.other_address)
        self.join_offer.add_widget(self.join)
        self.box.add_widget(self.join_offer)
        self.scroll.add_widget(self.box)

    # as a guest
    def guest_try_to_join(self):
        Utils.pop(self, 'Hello! guest have to register before buy', 'alert')

    # as a viewer

    def set_total_price(self, a, b):
        step_id = self.get_step()
        if step_id == -1:
            total_price = 0
        else:
            step = self.offer.steps[step_id]
            price_per_step = step.get_price()
            total_price = self.num_of_quantity * price_per_step
        self.curr_price.text = "  price : " + str(total_price)

    def chose_color(self, btn, text, num_of_quantity, color_num):
        print("chosen color:"+str(text)+"\n"+"num_of_quantity:"+str(num_of_quantity)+"\n")
        # change color of all the other button to the regular color
        y = btn.parent
        for ch in y.children:
            ch.icon = f'assets/windows/images/colors/un_{self.get_btn_color(ch)}.png'
        # change color of the selected button
        btn.icon = f'assets/windows/images/colors/{str(text)}.png'
        # chosen colors for add offer
        self.chosen_colors[num_of_quantity] = text
        x = 5

    def chose_size(self, btn, text, num_of_quantity, size_num):
        # change color of all the other button to the regular button color
        y = btn.parent
        for ch in y.children:
            ch.background_color = [1, 1, 1, 1]
        # change size of the selected button
        btn.background_color = (24 / 255, 211 / 255, 199 / 255, 1)
        # chosen sizes for add offer
        self.chosen_sizes[num_of_quantity] = text

    def get_btn_color(self, btn):
        str = btn.icon
        ans = str[29:len(str)-4]
        if ans[0:3] =="un_":
            ans = ans[3:len(ans)]
        return ans

    def remove_item(self):
        if self.num_of_quantity == 1:
            Utils.pop(self, '1 item is the minimal', 'alert')
            return
        for child in self.color_size.children[:1]:
            self.color_size.remove_widget(child)
        if len(self.chosen_colors) == self.num_of_quantity:
            self.chosen_colors.pop(self.num_of_quantity)
        if len(self.chosen_sizes) == self.num_of_quantity:
            self.chosen_sizes.pop(self.num_of_quantity)
        self.num_of_quantity -= 1
        self.set_total_price(None, None)
        self.box.size_hint_y -= .1
        self.color_size.size_hint_y -= .3

    def add_item(self):
        if self.num_of_quantity == 3:
            Utils.pop(self, '3 items is the max', 'alert')
            return
        if self.num_of_quantity > 0:
            if len(self.chosen_colors) != self.num_of_quantity:
                Utils.pop(self, 'have to chose color', 'alert')
                return
            if len(self.chosen_sizes) != self.num_of_quantity:
                Utils.pop(self, 'have to chose size', 'alert')
                return
        self.box.size_hint_y +=.1
        self.color_size.size_hint_y += .3


        self.num_of_quantity += 1
        # BOX
        colors_sizes2 = BoxLayout(orientation='horizontal')
        colors2 = BoxLayout(orientation='horizontal')
        sizes2 = BoxLayout(orientation='horizontal')
        colors_sizes2.add_widget(colors2)
        colors_sizes2.add_widget(sizes2)
        self.color_size.add_widget(colors_sizes2)
        # colors
        colors_counter = 0
        colors = self.offer.product.colors
        for color in colors:
            ip = "assets/windows/images/colors/un_" + color + ".png"
            btn = MDIconButton(icon=ip)
            btn.text = color
            btn.pos_hint = {'top': 0.95}
            # btn.size_hint_x = 0.1
            # btn.size_hint_y = 0.1
            btn.bind(on_press=lambda item_number=self.num_of_quantity, color_chosen=color,
                                     item_number1=self.num_of_quantity, color_num=colors_counter: self.chose_color(
                item_number, color_chosen,
                item_number1, color_num)),
            colors2.add_widget(btn)
            colors_counter = colors_counter + 1

        # sizes
        sizes_counter = 0
        sizes = self.offer.product.sizes
        for size in sizes:
            btn = Button(text=size)
            btn.pos_hint = {'top': 0.9}
            btn.size_hint_y = 0.5
            btn.bind(on_press=lambda item_number=self.num_of_quantity, size11=size,
                                     item_number1=self.num_of_quantity, size_num=sizes_counter: self.chose_size(
                item_number, size11,
                item_number1, size_num))
            sizes2.add_widget(btn)
            sizes_counter = sizes_counter + 1

        self.set_total_price(None, None)

    def add_address(self):
        if hasattr(self, 'm'):
            self.m = Add_address(title='address', size_hint=(None, None), size=(400, 400))
            self.m.open()
        else:
            self.m = Add_address(title='address', size_hint=(None, None), size=(400, 400))
            self.m.open()

    def join_(self):
        # check buying details
        step = self.get_step()
        if step == -1:
            toast("you need to choose step ")
            return
        offer_id = self.offer_id
        quantity = self.num_of_quantity
        # check Validity Quantity Per Step
        if quantity > self.offer.steps[step].limit - self.offer.steps[step].buyers_amount:
            toast("there is not enough items for this step")
            return

        if len(self.chosen_colors) != self.num_of_quantity:
            toast("you have to choose color")
            return
        if len(self.chosen_sizes) != self.num_of_quantity:
            toast("you have to choose size")
            return

        colors = ""
        sizes = ""
        for color in self.chosen_colors:
            colors = colors + self.chosen_colors[color] + ','
        for size in self.chosen_sizes:
            sizes = sizes + self.chosen_sizes[size] + ','
        colors = colors[0:len(colors) - 1]
        sizes = sizes[0:len(sizes) - 1]

        # move to payment screen
        # self.PaymentScreen = PAYMENTScreen(offer_id, int(quantity), step, colors, sizes, self.new_address, self.user,
        #                                    self.offer).open()
        self.PaymentScreen = PAYMENTScreen(offer_id, int(quantity), step, colors, sizes, "new address s", self.user,
                                           self.offer, self.name, self.photo_lis).open()

    # as a buyer

    def add_item_for_update(self, color, size, item_count):
        self.add_item()
        len_of_colors = len(self.offer.product.colors)
        len_of_sizes = len(self.offer.product.sizes)
        for i in range(0, len_of_colors):
            if self.get_btn_color(self.color_size.children[item_count-1].children[1].children[i]) == color:
                color_btn = self.color_size.children[item_count-1].children[1].children[i]
        for i in range(0, len_of_sizes):
            if self.color_size.children[item_count-1].children[0].children[i].text == size:
                size_btn = self.color_size.children[item_count-1].children[0].children[i]
        self.chose_color(color_btn, color, item_count, 0)
        self.chose_size(size_btn, size, item_count, 0)

    def update_purchase(self):
        sizez = ",".join(self.chosen_sizes.values())
        colorz = ",".join(self.chosen_colors.values())
        print(str(self.chosen_sizes.values()))
        print(type(str(self.chosen_sizes.values())))
        step = self.get_step()
        if step == -1:
            toast("you need to choose step")
            return
        ans = self.controller.update_purchase(self.offer_id, self.num_of_quantity, step, colorz, sizez,
                                                      self.purchase.address, self.user)
        if ans != False:
            self.remove_widget(self.box)
            Utils.pop(self, 'your purchase has been changed', 'change')
            self.init_offer(ans, self.photo_lis)
        else:
            Utils.pop(self, 'error, please try again', 'error')

    def cancel_purchase(self):
        ans = self.controller.cancel_purchase(self.offer_id, self.user)
        if ans != False:
            self.remove_widget(self.box)
            Utils.pop(self, 'your purchase has been canceled', 'cancel')
            # have to close the screen and open a new one - as a viewer, with the offer without this buyer
            self.init_offer(ans, self.photo_lis)
        else:
            Utils.pop(self, 'error, please try again', 'error')

    # as a seller

    def remove_offer(self):
        self.dismiss()
        ans = self.controller.remove_offer(self.offer_id)
        if ans.res is True:
            pass

    def update_offer(self):
        offer = self.offer
        offer_id = offer.offer_id
        screens_len = len(App.get_running_app().root.screens)
        screens = App.get_running_app().root.screens
        screen_name = 'update_offer_screen' + str(offer_id)
        for screen in screens:
            if screen.name == screen_name:
                # screen.init_offer(offer, photo_list)
                App.get_running_app().root.current = screen_name
                return
        screens.append(UPDATEOFFERScreen())
        screens[screens_len].init_offer(offer, self.photo_lis)
        App.get_running_app().root.current = screen_name
        # App.get_running_app().root.change_screen("update_offer")
        # c = self.offer
        # f = App.get_running_app().root.screens[6].update_offer(self.offer)

    def out(self):

        App.get_running_app().root.change_screen("menu_screen")
        #App.get_running_app().root.current = 'menu_screen'


    def like_unlike(self):
        if self.user.is_a_liker(self.offer_id):
            self.controller.remove_liked_offer(self.offer_id)
            self.like.icon="assets/windows/images/like.png"

        else:
            self.controller.add_liked_offer(self.offer_id)
            self.like.icon="assets/windows/images/unlike.png"

    def get_step(self):
        step = len(self.offer.steps)
        for checkbox in self.price_per_step.children:
            if type(checkbox) is MDCheckbox:
                if checkbox.active:
                    return step
                step -= 1
        return -1

    def split_list(self, lis):
        x = lis.split(',')
        return x[:-1]

    def split_str(self, str):
        to_return = str.split(',')
        if to_return[-1] == '':
            to_return = to_return[:-1]
        return to_return

    def list_to_dict(self, lis):
        i = 1
        dict = {}
        for val in lis:
            dict[i] = val
            i += 1
        return dict

    def insert_photos(self, car, photos):
        for photo in photos:
            if photo is not None:
                image = photo
                data = io.BytesIO(image)
                data.seek(0)
                img = CoreImage(data, ext="png").texture

                new_img = Image()
                new_img.texture = img
                new_img.allow_stretch = True
                # new_img.size_hint = 1.5,1
                car.add_widget(new_img)


class Add_address(Popup):
    def __init__(self, **kwargs):
        super(Add_address, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.address = MDTextField(hint_text='ADDRESS')
        self.box.add_widget(self.address)
        self.insert = Button(text="INSERT")
        self.insert.bind(on_press=lambda x: self.insert_add())
        self.box.add_widget(self.insert)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x: self.out())
        self.box.add_widget(self.back)
        self.add_widget(self.box)

    def out(self):
        self.dismiss()

    def insert_add(self):
        return 1
        self.parent.children[0].new_address = self.address.text
        self.parent.children[0].other_address.text = self.address.text
        self.parent.children[0].change = True
        self.dismiss()
