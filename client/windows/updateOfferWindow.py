from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.textfield import MDTextFieldRound
from windows.SideBar import SideBar

from Service.Object.OfferService import OfferService
from Service.Object.ProductService import ProductService
from kivymd.uix.picker import MDDatePicker


from Service.Object.StepService import StepService


class UPDATEOFFERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(UPDATEOFFERScreen, self).__init__(**kwargs)
#---------------------------------------------------
    def update_offer(self, offer):
        print('TODOO')

        #self.init_text_fields_with_offer_details(offer)
        add_offer_box = self.ids.add_offer_box
        #add_offer_box.init_fields()
        add_offer_box.init_text_fields_with_offer_details(offer)
        add_offer_button= self.ids.add_offer_box.ids.add_offer_button


        b=8
        #we recieved an offer and we need to insert our offer values to the fileds in this window
        # we need to change the button from add offer to update offer and at the end to change it back




class Category_box(BoxLayout):
    pass
MIN_DIFFERNCE_LIMIT = 10
MIN_DIFFERNCE_PRICE = 100
class Update_offer_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Update_offer_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        self.gender = 0
        self.num_of_added_step = 0
        self.next_step = []
        self.price = []
        self.limit = []
        self.color_list = []
        self.color_dropdown = DropDown()
        self.colors = ['green','black', 'blue', 'white']
        for color in self.colors:
            btn = Button(text=' % s' % color, size_hint=(None, None), height=40)
            btn.bind(on_release=lambda btn: self.add_color(btn))
            self.color_dropdown.add_widget(btn)

        self.color_mainbutton = Button(text='colors')
        self.color_mainbutton.bind(on_release=self.color_dropdown.open)

        self.size_list = []
        self.size_dropdown = DropDown()
        btn.bind(on_release=lambda btn: self.remove_size(btn))
        self.size_mainbutton = Button(text='sizes')
        self.size_mainbutton.bind(on_press = self.size_dropdown.open)

        self.chosen_cat_name = 'fix this name'


    def init_text_fields_with_offer_details(self, offer):
        #(self, offer_id, user_id, product, category_id, sub_category_id, status, steps, start_date, end_date,
           #      current_step, current_buyers)
        #self.offer = OfferService(offer['offer_id'])
        self.sub_cat12 = 'change this name'
        self.offer=offer
        self.ids.product_name.text = offer.product.name
        self.ids.company.text = offer.product.company
        self.ids.description.text = offer.product.description
        self.ids.end_date.text = str(offer.end_date)
        # self.ids.end_date.text = ""
        # self.ids.size_box.text = ""
        #self.size_input.text = ""


        self.ids.limit1.text = str(offer.steps[1].limit)
        self.ids.limit2.text = str(offer.steps[2].limit)
        self.ids.limit3.text = str(offer.steps[3].limit)
        self.ids.price1.text = str(offer.steps[1].price)
        self.ids.price2.text = str(offer.steps[2].price)
        self.ids.price3.text = str(offer.steps[3].price)
        #cat_name = App.get_running_app().controller.get_category_by_id(offer.category_id).name
        self.ids.drop_category.text = 'cat_name'
        #self.ids.drop_category.text = offer.product.sub_category_name

        self.size_dropdown = DropDown()
        self.add_size_start()
        for size in offer.product.sizes:
            self.ids.sizes.text = size
            self.add_size(size)
            self.ids.sizes.text = ""
        self.size_mainbutton.bind(on_press=self.size_dropdown.open)
        #self.color_list
        # for color in offer.product.colors:
        #     self.ids.sizes.text = size
        #     self.add_color(color)
        #     self.ids.sizes.text = ""
        for btn in self.color_dropdown.children[0].children:
            if btn.text in self.offer.product.colors:
                self.add_color(btn)



        # for limit in self.limit:
        #     limit.text = ""
        #
        # for price in self.price:
        #     price.text = ""

    def init_text_fields_after_update(self, offer):
        #(self, offer_id, user_id, product, category_id, sub_category_id, status, steps, start_date, end_date,
           #      current_step, current_buyers)

        #offer_product = offer[product]
        #self.offer = OfferService(offer['offer_id'])
        self.sub_cat12 = 'change this name'
        self.offer=offer
        self.ids.product_name.text = offer.product.name
        self.ids.company.text = offer.product.company
        self.ids.description.text = offer.product.description
        self.ids.end_date.text = str(offer.end_date)
        # self.ids.end_date.text = ""
        # self.ids.size_box.text = ""
        #self.size_input.text = ""


        self.ids.limit1.text = str(offer.steps[1].limit)
        self.ids.limit2.text = str(offer.steps[2].limit)
        self.ids.limit3.text = str(offer.steps[3].limit)
        self.ids.price1.text = str(offer.steps[1].price)
        self.ids.price2.text = str(offer.steps[2].price)
        self.ids.price3.text = str(offer.steps[3].price)
        #cat_name = App.get_running_app().controller.get_category_by_id(offer.category_id).name
        self.ids.drop_category.text = 'cat_name'
        #self.ids.drop_category.text = offer.product.sub_category_name

        for size in offer.product.sizes:
            self.ids.sizes.text = size
            self.add_size(size)
            self.ids.sizes.text = ""
        self.size_mainbutton.bind(on_press=self.size_dropdown.open)
        # self.size_dropdown = DropDown()
        # btn.bind(on_release=lambda btn: self.remove_size(btn))
        # self.size_mainbutton = Button(text='sizes')

        # for color in offer.product.colors:
        #     self.ids.sizes.text = size
        #     self.add_color(color)
        #     self.ids.sizes.text = ""



        # for limit in self.limit:
        #     limit.text = ""
        #
        # for price in self.price:
        #     price.text = ""

    def init_fields(self):
        self.next_step = []
        self.price = []
        self.limit = []
        self.color_list = []
    def add_color_start(self):
        self.ids.colors.add_widget(self.color_mainbutton)
        self.ids.colors.remove_widget(self.ids.color)

    def add_size_start(self):
        self.size_input = TextInput(hint_text= "choose size")
        self.ids['sizes'] = self.size_input
        self.ids.size_box.add_widget(self.size_input)
        self.insert_size = Button(text='add size')
        self.insert_size.bind(on_press=lambda tex: self.add_size(tex))
        self.ids.size_box.remove_widget(self.ids.add_size)
        self.ids.size_box.add_widget(self.insert_size)
        self.ids.size_box.add_widget(self.size_mainbutton)
        text = self.ids.sizes.text

        self.ids.add_size.bind(on_press= lambda tex: self.add_size(tex))

    def add_size(self, instance):
        text = self.ids.sizes.text
        btn = Button(text='%s' % text, size_hint=(None, None), height=40)
        btn.bind(on_release=lambda btn: self.remove_size(btn))
        self.size_dropdown.add_widget(btn)
        if text not in self.size_list:
            self.size_list.append(text)
        # if instance.text in self.size_list:
        #     instance.background_color = (1, 1, 1, 1)
        #     self.size_list.remove(instance.text)
        # else:
        #     self.size_list.append(instance.text)
        #     self.size_dropdown.add_widget(instance)
        #     instance.background_color = (.34, 1, 1, 1)

    def remove_size(self, btn):
        self.size_dropdown.remove_widget(btn)
        self.size_list.remove(btn.text)

    def add_color(self, instance):
        if instance.text in self.color_list:
            instance.background_color = (1,1,1,1)
            self.color_list.remove(instance.text)
        else:
            self.color_list.append(instance.text)
            instance.background_color =(.34, 1, 1, 1)

    def add_step(self):
        self.num_of_added_step = self.num_of_added_step + 1
        num_of_step = self.num_of_added_step + 3
        help = str(num_of_step)
        temp1 = MDLabel(text="step " + help)
        temp2 = MDTextField(hint_text= "limit")
        temp3 = MDTextField(hint_text= "price")
        self.next_step.append(temp1)
        self.ids.stepi.add_widget(MDLabel(text="step " + help))
        self.limit.append(temp2)
        self.ids.stepi.add_widget(temp2)
        self.price.append(temp3)
        self.ids.stepi.add_widget(temp3)

    def final_update_offer(self):

        if not self.check_steps_validity():
            return
        if not self.check_empty_fields():
            return
        list = [v for k, v in self.ids.choose.photo_list.items()]
        # list = self.ids.choose.photo_list.values() #convert dict to list
        name = self.ids.product_name.text
        category_name = self.chosen_cat_name
        sub_category_name = self.sub_cat12
        company = self.ids.company.text
        description = self.ids.description.text
        sizes = self.build_string_from_list(self.size_list)
        colors = self.build_string_from_list(self.color_list)
        end_date = self.ids.end_date.text
        step1 = StepService(0, self.ids.price1.text, 1, self.ids.limit1.text)
        step2 = StepService(0, self.ids.price2.text, 2, self.ids.limit2.text)
        step3 = StepService(0, self.ids.price3.text, 3, self.ids.limit3.text)
        # more Steps - optional, CHECK INPUT
        steps = [vars(step1), vars(step2),vars(step3)]
        if self.num_of_added_step > 0:
            for i in range(0, self.num_of_added_step):
                steps.append(vars(StepService(0, self.price[i].text, i+4, self.limit[i].text)))
        ans = App.get_running_app().controller.update_offer(self.offer.offer_id, self.chosen_cat_name, self.sub_cat12,
                                                            self.offer.user_id, name, company, colors, sizes,
                                                            description, steps, end_date)

        # have to change the fields of this offer
        if ans.res is True:
            updated_offer = ans.data

            self.offer = OfferService(updated_offer['offer_id'], updated_offer['user_id'], updated_offer['product'], updated_offer['category_id'], updated_offer['sub_category_id'], updated_offer['status'],
                         updated_offer['steps'],updated_offer['start_date'],updated_offer['end_date'],updated_offer['current_step'],updated_offer['current_buyers'])
            self.init_text_fields_after_update(self.offer)

    def check_empty_fields(self):
        if self.ids.end_date.text == "":
            toast("have to chose end date")
            return False
        if self.size_list == []:
            toast("have to add size")
            return False
        if self.color_list == []:
            toast("have to add color")
            return False
        return True

    def check_steps_validity(self):
        step1limit = int(self.ids.limit1.text)
        step2limit = int(self.ids.limit2.text)
        step3limit = int(self.ids.limit3.text)
        step1price = int(self.ids.price1.text)
        step2price = int(self.ids.price2.text)
        step3price = int(self.ids.price3.text)

        #limits
        flag = self.check_limits(step1limit, step2limit)
        if not flag:
            return False
        flag = self.check_limits(step2limit, step3limit)
        if not flag:
            return False

        # prices
        flag = self.check_prices(step1price, step2price)
        if not flag:
            return False
        flag = self.check_prices(step2price, step3price)
        if not flag:
            return False

        #check between the third step and the first added step
        if len(self.limit)>0:
            flag = self.check_limits(step3limit, int(self.limit[0].text))
            if not flag:
                return False
            flag = self.check_prices(step3price, int(self.price[0].text))
            if not flag:
                return False


        for i in range(0, len(self.limit)-1):
            flag = self.check_limits(int(self.limit[i].text),int(self.limit[i+1].text))
            if not flag:
                return False

        for i in range(0, len(self.price)-1):
            flag = self.check_prices(int(self.price[i].text),int(self.price[i+1].text) )
            if not flag:
                return False

        return True

    def check_limits(self,limit1,limit2):
        if limit1>limit2:
            toast('limit should be greater then her following limit '+str(limit1)+" "+str(limit2))
            return False

        if (limit2 - limit1) < MIN_DIFFERNCE_LIMIT:
            toast('the differnce between your limit is too short -> '+ str(limit1) + " "+str(limit2)+ 'this is the min differnce: '+str(MIN_DIFFERNCE_LIMIT))
            return False
        return True

    def check_prices(self,price1,price2 ):
        if price2>price1:
            toast('price should be smaller then his following price '+str(price1) + " " + str(price2))
            return False

        if (price1 - price2) < MIN_DIFFERNCE_PRICE:
            toast('the differnce between your price is too short -> '+ str(price1) +" "+str(price2)+'this is the min differnce: '+str(MIN_DIFFERNCE_PRICE))
            return False
        return True

    def clear_fields(self):
        self.ids.product_name.text = ""
        self.ids.company.text = ""
        self.ids.description.text = ""
        self.ids.end_date.text = "11/11/22"
        #self.ids.end_date.text = ""
        #self.ids.size_box.text = ""
        self.size_input.text = ""
        self.ids.limit1.text = ""
        self.ids.limit2.text = ""
        self.ids.limit3.text = ""
        self.ids.price1.text = ""
        self.ids.price2.text = ""
        self.ids.price3.text = ""
        self.ids.drop_category.text='Category'
        for limit in self.limit:
            limit.text = ""

        for price in self.price:
            price.text = ""


    def change_to_cat(self):
        SideBar.change_to_cat(self)

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def show_dropdown_category(self):
        categories = App.get_running_app().controller.get_categories()
        menu_items=[]
        for cat in categories:
            menu_items.append(
                {"text": cat.name,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=cat.get_sub_categories_names(), y=cat.name: self.show_dropdown_sub_category(x,y),
                }
            )

        self.drop_down_category = MDDropdownMenu(
            caller=self.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_category.open()

    def build_string_from_list(self, list):
        if len(list)>0:
            answer = list[0]
            i = 0
            for item in list:
                if i != 0:
                    answer = answer + ", " + item
                i = i + 1
            return answer

    def show_dropdown_sub_category(self, sub_categories_names, cat_name):
        self.chosen_cat_name = cat_name
        menu_items = []
        for sub_cat in sub_categories_names:
            menu_items.append(
                {"text": sub_cat,
                 "viewclass": "OneLineListItem",
                 # here we have to open page or the offers of this sub categories ya sharmutut
                 "on_release": lambda x=sub_cat: self.on_save_sub_category(x), }
            )
        self.drop_down_sub_category = MDDropdownMenu(
            caller=self.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_sub_category.open()
        self.drop_down_category.dismiss()

    def on_save_sub_category(self, sub_cat):
        self.sub_cat12 = sub_cat
        self.ids.drop_category.text = sub_cat
        self.drop_down_sub_category.dismiss()


    def on_save(self, instance, value, date_range):
        self.ids.end_date.text = str(value)
        # birth_date = value

    # click Cancel
    def on_cancel(self, instance, value):
        pass

    def back_to_menu(self):
        self.add_widget(self.side)
        self.remove_widget(self.cat)


    def exit(self):
        App.get_running_app().controller.exit()


class Sub_Category_box(BoxLayout):
    pass

class choose_photo_layout(MDBoxLayout):
    def __init__(self, **kwargs):
        super(choose_photo_layout, self).__init__(**kwargs)
        self.carousel = None
        self.i = 0
        self.photo_list = {}


    def remove_photo(self):
        if self.i == 0:
            return
        # self.photo_list.remove(self.carousel.current_slide)
        del self.photo_list[self.carousel.current_slide]
        self.carousel.remove_widget(self.carousel.current_slide)
        self.i -=1
        if self.i == 0:
            self.remove_widget(self.carousel)
            self.size_hint_y = 0.2

    def file_manager_open(self):
        path = '/'  # path to the directory that will be opened in the file manager
        self.manager  = MDFileManager(
            exit_manager=self.exit_manager,  # function called when the user reaches directory tree root
            select_path=self.select_path,  # function called when selecting a file/directory
        )
        self.manager.show(path)

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        print('path      '+path)
        self.size_hint_y = 1.5
        im = Image(source = path)
        if self.i == 0:
            self.carousel = Carousel()
            self.add_widget(self.carousel)
        self.carousel.add_widget(im,self.i)
        with open(path, "rb") as image:
            f = image.read()
            image.close()
        self.photo_list[im] = f
        self.i+=1
        self.manager.exit_manager()

        toast("picture add succesfully")

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager.close()
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device..'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            pass


class CustomDropDown(DropDown):
    pass

dropdown = CustomDropDown()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

# <CustomDropDown>
#     Button:
#         text: 'My first Item'
#         size_hint_y: None
#         height: 44
#         on_release: root.select('item1')
#     Label:
#         text: 'Unselectable item'
#         size_hint_y: None
#         height: 44
#     Button:
#         text: 'My second Item'
#         size_hint_y: None
#         height: 44
#         on_release: root.select('item2')