from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
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
from Utils.Utils import Utils
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.textfield import MDTextFieldRound
from windows.SideBar import SideBar
from Utils.Utils import Utils
from Service.Object.OfferService import OfferService
from Service.Object.ProductService import ProductService
from kivymd.uix.picker import MDDatePicker


from Service.Object.StepService import StepService

from Utils.CheckValidity import CheckValidity


class ADDOFFERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'

        super(ADDOFFERScreen, self).__init__(**kwargs)
#---------------------------------------------------





class Category_box(BoxLayout):
    pass
MIN_DIFFERNCE_LIMIT = 10
MIN_DIFFERNCE_PRICE = 100

class BoxLayout_helper(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayout_helper, self).__init__(**kwargs)
    #     Clock.schedule_once(self.insert_color, 0)
    #     self.bind(pos=self.update_rect, size=self.update_rect)
    #     self.rect = Rectangle(pos=self.pos, size=self.size)
    #
    # def update_rect(self, instance, value):
    #     self.rect.pos = self.pos
    #     self.rect.size = self.size
    #
    #     # listen to size and position changes
    #
    #     # self.insert_offers()
    #
    # def insert_color(self, num):
    #     with self.canvas.before:
    #         Color(0, 0, 0)
    #         self.rect = Rectangle(pos=self.pos, size=self.size)
    #         print('done')


class Add_offer_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Add_offer_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        # self.choose = Color_choose()
        # self.color_box = BoxLayout(orientation= 'horizontal')
        # self.add_widget(self.color_box)
        self.chosen_cat_name = None
        self.sub_cat12 = None
        self.gender = 0
        self.num_of_added_step = 0
        self.next_step = []
        self.price = []
        self.limit = []
        self.color_list = []
        self.color_dropdown = DropDown()
        self.dialog=None
        colors = ['green','black', 'blue', 'white']
        for color in colors:
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
        Clock.schedule_once(self.add_color_start, 0)
        Clock.schedule_once(self.add_size_start, 0)





    def add_color_start(self,  num):
        self.ids.colors.add_widget(self.color_mainbutton)
        # self.ids.colors.remove_widget(self.ids.color)

    def add_size_start(self, num):
        self.size_input = TextInput(hint_text= "choose size")
        self.ids['sizes'] = self.size_input
        self.ids.size_box.add_widget(self.size_input)
        self.insert_size = Button(text='add size')
        self.insert_size.bind(on_press=lambda tex: self.add_size_(tex))
        # self.ids.size_box.remove_widget(self.ids.add_size)
        self.ids.size_box.add_widget(self.insert_size)
        self.ids.size_box.add_widget(self.size_mainbutton)
        # self.ids.add_size.bind(on_press= lambda tex: self.add_size_(tex))

    def add_size_(self, instance):
        # self.size_dropdown.dismiss()
        text = self.ids.sizes.text
        btn = Button(text='%s' % text, size_hint=(None, None), height=40)
        btn.bind(on_release=lambda btn: self.remove_size(btn))

        if text not in self.size_list:
            self.size_list.append(text)
            self.size_dropdown.add_widget(btn)
        #self.size_dropdown.open(self.ids.sizes)
        # if instance.text in self.size_list:
        #     instance.background_color = (1, 1, 1, 1)
        #     self.size_list.remove(instance.text)
        # else:
        #     self.size_list.append(instance.text)
        #     self.size_dropdown.add_widget(instance)
        #     instance.background_color = (.34, 1, 1, 1)

    def remove_size(self, btn):
        self.size_dropdown.remove_widget(btn)
#        self.size_list.remove(btn.text)

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

    def add_offer(self):
        list = [v for k,v in self.ids.choose.photo_list.items()]
        # list = self.ids.choose.photo_list.values() #convert dict to list
        if not self.check_steps_validity():
            return
        if self.size_list == []:
            Utils.pop(self, f'have to add size', 'alert')
            #toast("have to add size")
            return
        if self.color_list == []:
            Utils.pop(self, f'have to add color', 'alert')
            #toast("have to add color")
            return
        if self.sub_cat12 is None:
            Utils.pop(self, f'have to chose sub category', 'alert')
            #toast("have to chose sub category")
            return
        if self.ids.end_date.text == "":
            Utils.pop(self, f'have to chose end date', 'alert')
            #toast("have to chose end date")
            return
        if not CheckValidity.checkValidityName(self,self.ids.product_name.text):
            return
        if not CheckValidity.checkValidityName(self,self.ids.company.text):
            return
        if not CheckValidity.checkEndDate(self, self.ids.end_date.text):
             return
        name = self.ids.product_name.text
        category_name = self.chosen_cat_name
        sub_category_name = self.sub_cat12
        company = self.ids.company.text
        description = self.ids.description.text
        sizes = self.build_string_from_list(self.size_list)
        colors = self.build_string_from_list(self.color_list)
        end_date = self.ids.end_date.text
        end_date = '2021-12-15'
        step1 = StepService(0, self.ids.price1.text, 1, self.ids.limit1.text)
        step2 = StepService(0, self.ids.price2.text, 2, self.ids.limit2.text)
        step3 = StepService(0, self.ids.price3.text, 3, self.ids.limit3.text)
        # more Steps - optional, CHECK INPUT
        steps = [vars(step1), vars(step2),vars(step3)]
        if self.num_of_added_step > 0:
            for i in range(0, self.num_of_added_step):
                steps.append(vars(StepService(0, self.price[i].text, i+4, self.limit[i].text)))
        ans = App.get_running_app().controller.add_active_sell_offer(name, company, colors, sizes, description, list, category_name,
                              sub_category_name, steps, end_date)

        #toast(ans.message)
        if ans.res is True:
            Utils.pop(self, ans.message, 'succes')
            Utils.pop(self, 'your offer is waiting for approve by admin', 'succes')
            self.clear_fields()
            App.get_running_app().root.current = 'menu_screen'
        else:
            Utils.pop(self, ans.message, 'alert')




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
            Utils.pop(self, f'limit should be greater then her following limit {str(limit1)} {str(limit2)}', 'alert')
            #toast('limit should be greater then her following limit '+str(limit1)+" "+str(limit2))
            return False

        if (limit2 - limit1) < MIN_DIFFERNCE_LIMIT:
            Utils.pop(self, f'the differnce between your limit is too short ->  {str(limit1)} {str(limit2)} this is the min differnce: {str(MIN_DIFFERNCE_LIMIT)}', 'alert')
            #toast('the differnce between your limit is too short -> '+ str(limit1) + " "+str(limit2)+ 'this is the min differnce: '+str(MIN_DIFFERNCE_LIMIT))
            return False
        return True

    def check_prices(self,price1,price2 ):
        if price2>price1:
            Utils.pop(self, f'price should be smaller then his following price {str(price1)} {str(price2)}', 'alert')
            #toast('price should be smaller then his following price '+str(price1) + " " + str(price2))
            return False

        if (price1 - price2) < MIN_DIFFERNCE_PRICE:
            Utils.pop(self, f'the differnce between your price is too short -> {str(price1)} {str(price2)} this is the min differnce: {str(MIN_DIFFERNCE_PRICE)}', 'alert')
            #toast('the differnce between your price is too short -> '+ str(price1) +" "+str(price2)+'this is the min differnce: '+str(MIN_DIFFERNCE_PRICE))
            return False
        return True

    def clear_fields(self):
        self.ids.product_name.text = ""
        self.ids.company.text = ""
        self.ids.description.text = ""
        self.ids.end_date.text = ""
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
        date_dialog = MDDatePicker(year=2022, month=12, day=15)
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
        answer = []
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
            # image.close()
        self.photo_list[im] = f
        self.i+=1
        self.manager.exit_manager()
        Utils.pop(self, 'picture add succesfully', 'succes')
        #toast("picture add succesfully")

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