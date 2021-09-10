from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivymd.uix.menu import MDDropdownMenu

from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from Service.Object.OfferService import OfferService
from Service.Object.ProductService import ProductService
from kivymd.uix.picker import MDDatePicker


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

    def add_offer(self):
        list = self.ids.choose.photo_list
        name = self.ids.product_name.text
        category_name = "sport"
        # category_name = self.ids.category.text
        sub_category_name = "swim"
        # sub_category_name = self.ids.sub_category.text
        company = self.ids.company.text
        description = self.ids.description.text
        sizes = self.ids.sizes.text(",")
        colors = self.ids.colors.text.split(",")
        end_date = "19/04/2022"
        # end_date = self.ids.end_date
        steps = {}
        ans = App.get_running_app().controller.add_active_sell_offer(name, company, colors, sizes, description, list, category_name,
                              sub_category_name, steps, end_date)
        ans1 = ans
        ans2 = ans

    def change_to_cat(self):
        self.side = self.ids.side_box
        self.remove_widget(self.side)
        self.add_widget(self.cat)

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
                "on_release": lambda x=cat.get_sub_categories_names(): self.show_dropdown_sub_category(x),
                }
            )

        self.drop_down_category = MDDropdownMenu(
            caller=self.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_category.open()

    def show_dropdown_sub_category(self, sub_categories_names):
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

    def change_to_sub_cat(self):
        self.remove_widget(self.cat)
        self.add_widget(self.sub_cat)

    def back_to_cat(self):
        self.add_widget(self.cat)
        self.remove_widget(self.sub_cat)

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