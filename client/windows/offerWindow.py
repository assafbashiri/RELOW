import io
from Utils.Utils import Utils
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
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
# from Backend_controller import Backend_controller
from Service.Object.OfferService import OfferService

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class OfferWindow(Popup):
    def __init__(self, offer, photo_lis, **kwargs):
        super(OfferWindow, self).__init__(**kwargs)
        self.controller = App.get_running_app().controller
        self.offer = offer[0]  # Offer Service
        self.offer_id = self.offer.offer_id
        self.color = 0
        self.num_of_quantity = 0
        self.change = False
        self.new_address = None
        # buyer/seller/viewer/user
        if (self.controller.user_service is None):
            Utils.pop(self,"not log in", 'alert')
            return
        self.user = self.controller.user_service

        if self.controller.guest is True:
            self.show_as_guest(photo_lis)
        elif self.offer.is_a_seller(self.user.user_id):
            self.show_as_seller(photo_lis)
        elif self.user.is_a_buyer(self.offer.offer_id):
            self.show_as_buyer(photo_lis)
        else:
            self.show_as_viewer(photo_lis)
        return

    def show_as_guest(self, photo_lis):
        print('as a guest')
        self.title = self.offer.product.name
        self.box = BoxLayout(orientation='vertical')
        self.carousel = Carousel(size_hint_y=6)
        self.insert_photos(self.carousel, photo_lis)
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
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step.get_buyers_amount())+"/"+str(step.get_limit())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
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
        self.insert_photos(self.carousel, photo_lis)
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
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step.get_buyers_amount())+"/"+str(step.get_limit())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
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
        # self.box.add_widget(self.color_box)

        self.color_dropdown.bind(on_select=lambda instance, x: setattr(self.color_mainbutton, 'text', x))

        self.size_dropdown = DropDown()
        sizes = self.offer.product.sizes
        for size in sizes:
            btn = Button(text=' % s' % size, size_hint=(None, None), height=40)
            btn.bind(on_release=lambda btn: self.size_dropdown.select(btn.text))
            self.size_dropdown.add_widget(btn)
        self.size_mainbutton = Button(text='sizes', size_hint=(None, None), pos=(400, 300))
        self.size_mainbutton.bind(on_release=self.size_dropdown.open)
        # self.box.add_widget(self.size_mainbutton)
        self.size_dropdown.bind(on_select=lambda instance, x: setattr(self.size_mainbutton, 'text', x))
        self.join_offer = BoxLayout(orientation='horizontal')
        # self.quantity = MDTextField(hint_text='QUANTITY')
        self.update = Button(text="UPDATE")
        self.update.bind(on_press=lambda x: self.update_offer())
        # self.join_offer.add_widget(self.quantity)
        self.join_offer.add_widget(self.update)
        self.remove_offer_bt = Button(text="REMOVE OFFER")
        self.remove_offer_bt.bind(on_press=lambda x: self.remove_offer())
        # self.join_offer.add_widget(self.quantity)
        self.join_offer.add_widget(self.remove_offer_bt)
        self.box.add_widget(self.join_offer)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x: self.out())
        self.box.add_widget(self.back)
        self.add_widget(self.box)

    def show_as_buyer(self, photo_lis):
        print('as a buyer')
        purchases = self.offer.get_current_buyers()
        purchase = None
        for purch in purchases:
            p = purchases[purch]
            if p.buyer_id == self.user.user_id:
                self.purchase = p
                break
        self.title = self.offer.product.name
        self.box = BoxLayout(orientation='vertical')
        self.carousel = Carousel(size_hint_y=6)
        # for photo in photo_lis:
        #     self.carousel.add_widget(photo)
        #image = AsyncImage(source="windows/images/a.png")
        #self.carousel.add_widget(image)
        self.insert_photos(self.carousel, photo_lis)
        self.box.add_widget(self.carousel)
        self.slider = MDSlider()
        self.slider.min = 0
        self.slider.max = 150
        self.slider.value = 15
        steps = self.offer.steps

        self.slider.min = 0
        self.slider.max = 100  # steps[-1][1]
        self.slider.value = 10  # self.offer.current_buyers
        self.progress = MDProgressBar()
        self.progress.value = self.slider.value
        self.people_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step.get_buyers_amount())+"/"+str(step.get_limit())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
            step = steps[step_id]
            if self.purchase.step_id == step.step_number:
                self.price_per_step.add_widget(MDCheckbox(group="price", size_hint_x=.1, active=True))
            else:
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

        size_lis = self.split_str(self.purchase.size)
        color_lis = self.split_str(self.purchase.color)
        self.color_mainbutton = {}
        self.size_mainbutton = {}
        self.chosen_colors = self.list_to_dict(color_lis)
        self.chosen_sizes = self.list_to_dict(size_lis)

        for i in range(1,len(color_lis)+1):
            self.chosen_colors[i] = color_lis[i-1]
            self.chosen_sizes[i] = size_lis[i-1]
        self.color_dropdown = {}
        self.size_dropdown = {}
        self.another_item = Button(text="another item")
        self.another_item.bind(on_press=lambda x: self.add_item())
        self.box.add_widget(self.another_item)
        self.remove = Button(text="less item")
        self.remove.bind(on_press=lambda x: self.remove_item())
        self.box.add_widget(self.remove)
        quan = self.purchase.quantity
        for i in range (0,quan):
            self.add_item_for_update(color_lis[i],size_lis[i])

        self.join_offer = BoxLayout(orientation='horizontal')
        self.unjoin = Button(text="CANCEL")
        self.unjoin.bind(on_press=lambda x: self.cancel_purchase())
        self.update = Button(text="UPDATE")
        self.update.bind(on_press=lambda x: self.update_purchase())
        self.join_offer.add_widget(self.unjoin)
        self.join_offer.add_widget(self.update)
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
        #- image = AsyncImage(source="windows/images/a.png")
        # self.carousel.add_widget(image)
        self.insert_photos(self.carousel, photo_lis)
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
            self.people_per_step.add_widget(MDLabel(text='people:' + str(step.get_buyers_amount())+"/"+str(step.get_limit())))
        self.box.add_widget(self.people_per_step)
        self.box.add_widget(self.progress)
        self.price_per_step = BoxLayout(orientation='horizontal', size_hint_y=.2)
        for step_id in steps:
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

        self.color_mainbutton = {}
        self.size_mainbutton = {}

        self.chosen_colors={}
        self.chosen_sizes={}




        self.color_dropdown = {}

        self.size_dropdown = {}
        self.add_item()

        self.join_offer = BoxLayout(orientation='horizontal')

        self.another_item = Button(text="another item")
        self.another_item.bind(on_press=lambda x: print(self.add_item()))
        self.box.add_widget(self.another_item)

        self.remove = Button(text="less item")
        self.remove.bind(on_press=lambda x: self.remove_item())
        self.box.add_widget(self.remove)

        self.join = Button(text="JOIN")
        self.join.bind(on_press=lambda x: self.join_())
        self.other_address = Button(text='NEW ADDRESS FOR THIS PRODUCT')
        self.other_address.bind(on_press=lambda x: self.add_address())

        self.join_offer.add_widget(self.other_address)
        self.box.add_widget(self.join_offer)
        self.box.add_widget(self.join)
        if self.user.is_a_liker(self.offer_id):
            self.like = Button(text="UNLIKE")
        else:
            self.like = Button(text="LIKE")
        self.like.bind(on_press=lambda x: self.like_unlike())
        self.box.add_widget(self.like)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x: self.out())
        self.box.add_widget(self.back)

        self.add_widget(self.box)

    def save_color_first(self, btn, text,num_of_quantity):
        self.color_mainbutton[num_of_quantity].text=text
        self.color_dropdown[num_of_quantity].dismiss()
        self.chosen_colors[num_of_quantity] = text

    def save_size_first(self, btn, text,num_of_quantity):
        self.size_mainbutton[num_of_quantity].text=text
        self.size_dropdown[num_of_quantity].dismiss()
        self.chosen_sizes[num_of_quantity] = text


    def register(self):
        self.dismiss()
        a = App.get_running_app()
        a.root.current = 'connect_screen'
        Utils.pop("you need to register first", 'alert')

    def out(self):
        self.dismiss()

    def dismiss(self):
        Popup.dismiss(self)

    def like_unlike(self):
        if self.user.is_a_liker(self.offer_id):
            self.controller.remove_liked_offer(self.offer_id)
            self.like.text = 'LIKE'

        else:
            self.controller.add_liked_offer(self.offer_id)
            self.like.text = 'UNLIKE'

    def add_item_for_update(self,colorz,sizez):
        self.num_of_quantity += 1

        #self.color_size = BoxLayout(orientation='horizontal')
        #self.box.add_widget(self.color_size)

        self.color_dropdown[self.num_of_quantity] = DropDown()
        colors = self.offer.product.colors
        for color in colors:
            btn = Button(text='%s' % color, size_hint=(None,None))
            btn.bind(on_release=lambda btn=self.num_of_quantity,color_chosen=btn.text, quant=self.num_of_quantity: self.save_color_first(btn, color_chosen,quant))
            self.color_dropdown[self.num_of_quantity].add_widget(btn)
        self.color_mainbutton[self.num_of_quantity] = Button(text=colorz)
        self.color_mainbutton[self.num_of_quantity].bind(on_release=self.color_dropdown[self.num_of_quantity].open)

        self.color_size.add_widget(self.color_mainbutton[self.num_of_quantity])
        self.color_dropdown[self.num_of_quantity].bind(on_select=lambda a=self.num_of_quantity, instance=self.color_mainbutton[self.num_of_quantity]: self.save_color_first(a,instance))

        #------------------------------------------size-----------------

        self.size_dropdown[self.num_of_quantity] = DropDown()
        sizes = self.offer.product.sizes
        for size in sizes:
            btn = Button(text='%s' % size, size_hint=(None, None))
            btn.bind(on_release=lambda btn=self.num_of_quantity, size_chosen=btn.text,
                                       quant=self.num_of_quantity: self.save_size_first(btn, size_chosen, quant))
            self.size_dropdown[self.num_of_quantity].add_widget(btn)
        self.size_mainbutton[self.num_of_quantity] = Button(text=sizez)
        self.size_mainbutton[self.num_of_quantity].bind(on_release=self.size_dropdown[self.num_of_quantity].open)

        self.color_size.add_widget(self.size_mainbutton[self.num_of_quantity])
        self.size_dropdown[self.num_of_quantity].bind(on_select=lambda a=self.num_of_quantity,
                                                                       instance=self.size_mainbutton[
                                                                           self.num_of_quantity]: self.save_size_first(a, instance))

    def remove_item(self):
        if self.num_of_quantity == 1:
            Utils.pop(self, '1 item is the minimal', 'alert')
            return
        for child in self.color_size.children[:2]:
            self.color_size.remove_widget(child)
        if self.color_dropdown:
            self.color_dropdown.popitem()
        if self.size_dropdown:
            self.size_dropdown.popitem()
        if self.chosen_sizes:
            self.chosen_sizes.popitem()
        if self.chosen_colors:
            self.chosen_colors.popitem()
        self.num_of_quantity -=1
        for off in self.user.active_buy_offers:
            a = 8

    def add_item(self):
        if self.num_of_quantity == 3:
            Utils.pop(self, '1 item is the max', 'alert')
            return
        self.num_of_quantity += 1

        #self.color_size = BoxLayout(orientation='horizontal')
        #self.box.add_widget(self.color_size)

        self.color_dropdown[self.num_of_quantity] = DropDown()
        colors = self.offer.product.colors
        for color in colors:
            btn = Button(text='%s' % color, size_hint=(None,None))
            btn.bind(on_release=lambda btn=self.num_of_quantity,color_chosen=btn.text, quant=self.num_of_quantity: self.save_color_first(btn, color_chosen,quant))
            self.color_dropdown[self.num_of_quantity].add_widget(btn)
        self.color_mainbutton[self.num_of_quantity] = Button(text='colors')
        self.color_mainbutton[self.num_of_quantity].bind(on_release=self.color_dropdown[self.num_of_quantity].open)

        self.color_size.add_widget(self.color_mainbutton[self.num_of_quantity])
        self.color_dropdown[self.num_of_quantity].bind\
            (on_select=lambda a=self.num_of_quantity, instance=self.color_mainbutton[self.num_of_quantity]: self.save_color_first(a,instance))



        #------------------------------------------size-----------------

        self.size_dropdown[self.num_of_quantity] = DropDown()
        sizes = self.offer.product.sizes
        for size in sizes:
            btn = Button(text='%s' % size, size_hint=(None, None))
            btn.bind(on_release=lambda btn=self.num_of_quantity, size_chosen=btn.text,
                                       quant=self.num_of_quantity: self.save_size_first(btn, size_chosen, quant))
            self.size_dropdown[self.num_of_quantity].add_widget(btn)
        self.size_mainbutton[self.num_of_quantity] = Button(text='sizes')
        self.size_mainbutton[self.num_of_quantity].bind(on_release=self.size_dropdown[self.num_of_quantity].open)

        self.color_size.add_widget(self.size_mainbutton[self.num_of_quantity])
        self.size_dropdown[self.num_of_quantity].bind(on_select=lambda a=self.num_of_quantity,
                                                                       instance=self.size_mainbutton[
                                                                           self.num_of_quantity]: self.save_size_first(a, instance))



        #self.color_size.add_widget(self.size_mainbutton[self.num_of_quantity])
        #self.size_dropdown.bind(on_select=lambda instance, x: setattr(self.size_mainbutton[self.num_of_quantity], 'text', x))

    def open_drop(self, a, num_of_quantity):
        self.color_dropdown[num_of_quantity].open

    def join_(self):
        step = len(self.offer.steps)
        for checkbox in self.price_per_step.children:
            if type(checkbox) is MDCheckbox:
                if checkbox.active:
                    offer_id = self.offer_id
                    quantity = self.num_of_quantity
                    # check Validity Quantity Per Step
                    if quantity > self.offer.steps[step].limit - self.offer.steps[step].buyers_amount:
                        toast("there is not enough items for this step")
                        return
                        # loop for all the selected colors & sizes
                    colors = ""
                    sizes = ""
                    j =0
                    for i in range(1, self.num_of_quantity+1):
                        # check validity colors and sizes
                        if self.color_mainbutton[i].text == "" or self.size_mainbutton[i].text == "":
                            toast("you have to choose color & size for item number "+str(i))
                            return
                        colors = colors+self.color_mainbutton[i].text+','
                        sizes = sizes+self.size_mainbutton[i].text+','
                        j = i
                    if self.color_mainbutton[j].text == "" or self.size_mainbutton[j].text == "":
                        toast("you have to choose color & size for item number " + str(j))
                        return
                    # colors = colors + self.color_mainbutton[i].text
                    # sizes = sizes + self.size_mainbutton[i].text
                    ans = App.get_running_app().controller.add_active_buy_offer(offer_id, int(quantity), step, colors,
                                                                                sizes, self.new_address)
                    if ans.res is True:
                        self.user.get_active_buy_offers().append(self.offer)
                        self.offer = ans.data
                        data = App.get_running_app().root.current_screen.ids.menu_box.children[1].data
                        for object in data:
                            offer = object['offer']
                            if offer[0].offer_id == self.offer_id:
                                a = ans.data.current_buyers
                                to_return = {}
                                for buyer in ans.data.current_buyers:
                                    to_return[buyer['buyer_id']] = Struct(**buyer)
                                offer[0].current_buyers = to_return
                        self.dismiss()
                        return
                step -= 1
                if step == 0:
                    toast("you nקed to choose step ")

    def update_purchase(self):
        sizez = ",".join(self.chosen_sizes.values())
        colorz = ",".join(self.chosen_colors.values())
        print(str(self.chosen_sizes.values()))
        print(type(str(self.chosen_sizes.values())))
        step = len(self.offer.steps)
        # self.controller.remove_active_buy_offer(self.offer_id)
        for checkbox in self.price_per_step.children:
            if type(checkbox) is MDCheckbox:
                if checkbox.active:
                    offer_id = self.offer_id
                    quantity = self.num_of_quantity
                    ans = self.controller.update_active_buy_offer(self.offer_id, quantity, step, colorz, sizez, self.purchase.address)
                    if ans.res is True:
                        for item in self.user.active_buy_offers:
                            if item.offer_id == self.offer_id:
                                self.user.active_buy_offers.remove(item)
                        self.user.get_active_buy_offers().append(self.offer)
                        self.offer = ans.data
                        data = App.get_running_app().root.current_screen.ids.menu_box.children[1].data
                        for object in data:
                            offer = object['offer']
                            if offer[0].offer_id == self.offer_id:
                                a = ans.data.current_buyers
                                to_return = {}
                                for buyer in ans.data.current_buyers:
                                    to_return[buyer['buyer_id']] = Struct(**buyer)
                                offer[0].current_buyers = to_return
                        self.dismiss()
                        return
                step -= 1

    def cancel_purchase(self):
        ans = self.controller.remove_active_buy_offer(self.offer_id)
        if ans.res is True:
            # self.user.get_active_buy_offers().append(self.offer)
            cc = self.user.get_active_buy_offers()
            self.offer = ans.data
            for offerz in self.user.active_buy_offers:
                if offerz.offer_id == self.offer_id:
                    self.user.active_buy_offers.remove(offerz)
            data = App.get_running_app().root.current_screen.ids.menu_box.children[1].data
            for object in data:
                offer = object['offer']
                if offer[0].offer_id == self.offer_id:
                    a = ans.data.current_buyers
                    to_return = {}
                    for buyer in ans.data.current_buyers:
                        to_return[buyer['buyer_id']] = Struct(**buyer)
                    offer[0].current_buyers = to_return
            # self.user.active_buy_offers.remove(ans.data)
        self.dismiss()
    def remove_offer(self):
        self.dismiss()
        ans = self.controller.remove_active_sell_offer(self.offer_id)
        if ans.res is True:
            pass

    def update_offer(self):
        self.dismiss()
        App.get_running_app().root.current = 'update_offer'
        c = App.get_running_app().root
        e = App.get_running_app().root.screens
        f = App.get_running_app().root.screens[6]
        c = self.offer
        f = App.get_running_app().root.screens[6].update_offer(self.offer)
    def add_address(self):
        if hasattr(self, 'm'):
            self.m =Add_address(title = 'address', size_hint=(None,None), size = (400,400))
            self.m.open()
        else:
            self.m = Add_address(title='address', size_hint=(None, None), size=(400, 400))
            self.m.open()
    def split_list(self, lis):
        x = lis.split(',')
        return x[:-1]

    def split_str(self, str):
        to_return = str.split(',')
        if to_return[-1] == '':
            to_return = to_return[:-1]
        return  to_return

    def list_to_dict(self,lis):
        i = 1
        dict = {}
        for val in lis:
            dict[i] = val
            i +=1
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
                car.add_widget(new_img)

class Add_address(Popup):
    def __init__(self, **kwargs):
        super(Add_address, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.address = MDTextField(hint_text='ADDRESS')
        self.box.add_widget(self.address)
        self.insert = Button(text="INSERT")
        self.insert.bind(on_press=lambda x:self.insert_add())
        self.box.add_widget(self.insert)
        self.back = Button(text="BACK")
        self.back.bind(on_press=lambda x:self.out())
        self.box.add_widget(self.back)
        self.add_widget(self.box)

    def out(self):
        self.dismiss()

    def insert_add(self):
        self.parent.children[1].new_address = self.address.text
        self.parent.children[1].other_address.text = self.address.text
        self.parent.children[1].change = True
        self.dismiss()


