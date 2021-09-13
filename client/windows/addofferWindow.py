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


class ADDOFFERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(ADDOFFERScreen, self).__init__(**kwargs)

class Category_box(BoxLayout):
    pass

class Add_offer_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Add_offer_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        # self.choose = Color_choose()
        # self.color_box = BoxLayout(orientation= 'horizontal')
        # self.add_widget(self.color_box)
        self.gender = 0
        self.num_of_added_step = 0
        self.next_step = []
        self.price = []
        self.limit = []
        self.color_list = []
        self.color_dropdown = DropDown()
        colors = ['green','black']
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
        self.size_mainbutton.bind(on_release= self.size_dropdown.open)

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

    # def size_drop(self, size):
    #     if len(self.size_list) == 0:
    #         self.ids.size_box.add_widget(self.size_dropdown)
    #         self.size_dropdown.add_widget((MDLabel(text= 'my sizes')))
    #
    #     btn = Button(text='%s' %size, size_hint=(None, None), height=40, on_press= lambda btn: self.remove_size(btn))
    #     self.size_list.append(size)
    #     self.size_dropdown.add_widget(btn)
    #     # self.size_dropdown.open(self.size_dropdown)
    #     self.ids.sizes.text = ''



    def add_size(self, instance):
        text = self.ids.sizes.text
        print("fuck you man")
        btn = Button(text='%s' % text, size_hint=(None, None), height=40)
        btn.bind(on_release=lambda btn: self.remove_size(btn))
        self.size_dropdown.add_widget(btn)
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
        list = self.ids.choose.photo_list
        name = self.ids.product_name.text
        category_name = self.cat_name12
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
        ans = App.get_running_app().controller.add_active_sell_offer(name, company, colors, sizes, description, list, category_name,
                              sub_category_name, steps, end_date)


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
        answer = list[0]
        i = 0
        for item in list:
            if i != 0:
                answer = answer + ", " + item
            i = i + 1
        return answer

    def show_dropdown_sub_category(self, sub_categories_names, cat_name):
        self.cat_name12 = cat_name
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

class choose_photo_layout(BoxLayout):
    def __init__(self, **kwargs):
        super(choose_photo_layout, self).__init__(**kwargs)
        self.carousel = Carousel()
        self.add_widget(self.carousel)
        self.i = 0
        self.photo_list = []

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
        print(path)
        self.im = Image(source = path)
        self.carousel.add_widget(self.im,self.i)
        self.photo_list.insert(self.i, self.im)
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