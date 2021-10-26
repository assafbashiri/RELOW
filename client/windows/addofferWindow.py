from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
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
from kivymd.uix.menu import MDDropdownMenu

from Service.Object.StepService import StepService

from Utils.CheckValidity import CheckValidity


class ADDOFFERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'add_offer_screen'

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
        self.chosen_cat_name = None
        self.sub_cat12 = None
        self.dialog = None
        self.step = 0

        self.next_step = []
        self.price = []
        self.limit = []
        self.color_list = []
        self.size_list = []


        #for photos
        self.carousel = None
        self.i = 0
        self.photo_list = {}
        self.dialog = None

#------------------------COLOR DROPDOWN---------------------------#

        self.color_dropdown = MDDropdownMenu()
        self.color_mainbutton = MyButton(text='colors')
        self.ids['color_mainbutton'] =self.color_mainbutton
        self.color_mainbutton.bind(on_press=lambda x:self.show_dropdown_colors())

# ------------------------SIZE NUM DROPDOWN---------------------------#

        size_num = ['1', '2', '3', '4']
        self.size_num_dropdown = DropDown()
        for size in size_num:
            btn = MyButton(text=' % s' % size)
            btn.bind(on_release=lambda btn: self.add_size_num(btn))
            self.size_num_dropdown.add_widget(btn)
        self.size_num_mainbutton = MyButton(text='sizes')
        self.size_num_mainbutton.bind(on_press=lambda x :self.size_num_dropdown.open(x))

# ------------------------SIZE KIND DROPDOWN---------------------------#

        size_kind = ['inch', 'cm', 'kg', 'pond']
        self.size_kind_dropdown = DropDown()
        for size_kind in size_kind:
            btn = MyButton(text=' % s' % size_kind)
            btn.bind(on_release=lambda btn: self.add_size_kind(btn))
            self.size_kind_dropdown.add_widget(btn)
        self.size_kind_mainbutton = Button(text='size kind')
        self.size_kind_mainbutton.bind(on_press =lambda x : self.size_kind_dropdown.open(x))

# ------------------------SIZE RES DROPDOWN---------------------------#

        self.size_dropdown = DropDown()
        self.size_mainbutton = Button(text='My Sizes')
        self.size_mainbutton.bind(on_press=self.size_dropdown.open)
        self.add_size = Button(text='Add')
        self.add_size.bind(on_press=lambda tex: self.add_size_(tex))

# ---------------------------------------------------#
        Clock.schedule_once(self.init_colors, 0)
        #Clock.schedule_once(self.add_size_start, 0)

    def show_dropdown_colors(self):
        menu_items = []
        colors = ['green', 'black', 'blue', 'white']
        for color in colors:
            menu_items.append(
                {
                    'text': color,
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=color: self.save_color(x),
                }
            )

        self.drop_down_colors = MDDropdownMenu(
            caller=self.color_mainbutton,
            items=menu_items,
            width_mult=4,

        )
        self.drop_down_colors.open()

    def save_color(self, color):
        self.color_list.append(color)
        # self.drop_down_colors.dismiss()

    def tr(self,x):
        self.color_dropdown.open()
        a =5
    def back(self):
        App.get_running_app().root.current = "menu_screen"


    def add_color_start(self,  num):
        self.ids.color_box.add_widget(self.color_mainbutton)

    def add_size_start(self, num):
        #self.ids.size_drop_box.add_widget(self.size_num_mainbutton)
        #self.ids['size_num'] = self.size_num_mainbutton
        #self.ids.size_drop_box.add_widget(self.size_kind_mainbutton)
        #self.ids['size_kind'] = self.size_kind_mainbutton
        #self.ids.size_drop_box.add_widget(self.add_size)
        #self.ids['add_size'] = self.add_size
        self.ids.size_drop_box.add_widget(self.size_mainbutton)
        self.ids['my_sizes'] = self.size_mainbutton

        # self.size_input = TextInput(hint_text= "choose size")
        # self.ids['sizes'] = self.size_input
        # self.ids.size_box.add_widget(self.size_input)


        # self.ids.size_box.remove_widget(self.ids.add_size)
        # self.ids.size_box.add_widget(self.insert_size)
        # self.ids.size_box.add_widget(self.size_num_mainbutton)
        # self.ids.add_size.bind(on_press= lambda tex: self.add_size_(tex))

    def add_size_(self):
        # self.size_dropdown.dismiss()
        text = self.ids.size_num_input.text+' '+self.ids.size_type_input.text
        if text not in self.size_list:
            self.size_list.append(text)
        # self.show_dropdown_size()
        #self.drop_down_size.menu_items.append(text)


            #self.size_dropdown.add_widget(btn)
        #self.size_dropdown.open(self.ids.sizes)
        # if instance.text in self.size_list:
        #     instance.background_color = (1, 1, 1, 1)
        #     self.size_list.remove(instance.text)
        # else:
        #     self.size_list.append(instance.text)
        #     self.size_dropdown.add_widget(instance)
        #     instance.background_color = (.34, 1, 1, 1)

    def remove_size(self):
        if len(self.size_list) == 0:
            return
        # self.size_dropdown.remove_widget(btn)
#        self.size_list.remove(btn.text)
        size = self.ids.size_out.text
        if size == 'My Sizes':
            return
        self.size_list.remove(size)

        if len(self.size_list) == 0:
            self.ids.size_out.text = 'My Sizes'
        else:
            self.ids.size_out.text = self.size_list[0]


    def init_colors(self, num):
        colors = ['red', 'black','blue', 'yellow','white']
        colors_counter = 0
        for color in colors:
            ip = "windows/images/colors/un_" + color + ".png"
            btn = MDIconButton(icon=ip)
            btn.text = color
            btn.bind(on_press=lambda instance=1,color_name=color: self.chose_color(
                instance, color_name))
            self.ids.color_grid.add_widget(btn)
            colors_counter = colors_counter + 1

    def chose_color(self, btn, text):
        if text in self.color_list:
            self.color_list.remove(text)
            btn.icon ="windows/images/colors/un_" + text + ".png"
        # change color of all the other button to the regular color
        # change color of the selected button
        else:
            btn.icon = "windows/images/colors/" + text + ".png"
        # chosen colors for add offer
            self.color_list.append(text)


    def get_btn_color(self, btn):
        str = btn.icon
        ans = str[22:len(str)-4]
        if ans[0:3] =="un_":
            ans = ans[3:len(ans)]
        return ans


    def add_color(self, instance):
        if instance.text in self.color_list:
            instance.background_color = (1,1,1,1)
            self.color_list.remove(instance.text)
        else:
            self.color_list.append(instance.text)
            instance.background_color =(.34, 1, 1, 1)
    def get_step(self): #only for the kivy- dont use it!!!!
        self.step+=1
        return self.step
    def add_step(self):
        if self.step == 4:
            Utils.pop(self, f'4 steps is the maximum steps for offer', 'alert')
            return
        self.ids.steps_box.size_hint_y += .3
        self.ids.cover.size_hint_y += .3
        self.step += 1
        self.step_to_add = StepLayout(str(self.step))
        self.ids[str(self.step)] = self.step_to_add
        self.ids.steps_box.add_widget(self.step_to_add, 1)
        #self.ids.add_step.size_hint_y += .5
        #self.ids.cover.size_hint_y +=.33 #increment the scrollview

    def remove_step(self):
        if self.step == 2:
            Utils.pop(self, f'2 steps is the minimum for offer', 'alert')
            return
        a = len(self.ids.steps_box.children)
        self.ids.steps_box.remove_widget(self.ids.steps_box.children[1])
        self.ids.steps_box.size_hint_y -= .3
        self.ids.cover.size_hint_y -= .4
        self.step -=1




    def add_offer(self):
        list = [v for k,v in self.photo_list.items()]
        # list = self.ids.choose.photo_list.values() #convert dict to list
        name = self.ids.product_name_input.text
        category_name = self.chosen_cat_name
        sub_category_name = self.sub_cat12
        company = self.ids.company_name_input.text
        description = self.ids.description_input.text
        sizes = self.build_string_from_list(self.size_list)
        colors = self.build_string_from_list(self.color_list)
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
        end_date = self.ids.day_input.text+'/'+self.ids.month_input.text+'/'+self.ids.year_input.text
        if end_date == "":
            Utils.pop(self, f'have to chose end date', 'alert')
            #toast("have to chose end date")
            return
        if not CheckValidity.checkValidityName(self,name):
            return
        if not CheckValidity.checkValidityName(self,company):
            return
        # if not CheckValidity.checkEndDate(self, end_date):
        #      return
        end_date = '2021-12-15'
        steps = []
        for i in range(1, self.step+1):
            price = self.ids[str(i)].ids.price_input.text
            limit = self.ids[str(i)].ids.max_input.text
            step = StepService(0, price, i, limit)
            steps.append(vars(step))
        ans = App.get_running_app().controller.add_offer(name, company, colors, sizes, description, list, category_name,
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
        for i in range(1,self.step):

            step_prev = self.ids[str(i)]
            step_next = self.ids[str(i+1)]
            flag = self.check_limits(int(step_prev.ids.max_input.text),
                                     int(step_next.ids.max_input.text))
            if not flag:
                return False
            flag = self.check_prices(int(step_prev.ids.price_input.text),
                                     int(step_next.ids.price_input.text))

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
        self.ids.product_name_input.text = ""
        self.ids.company_name_input.text = ""
        self.ids.description_input.text = ""
        self.ids.year_input.text = "Year"
        self.ids.month_input.text = "Month"
        self.ids.day_input.text = "Day"
        # self.ids.size_input.text = ""
        for i in range(1, self.step+1):
            self.clear_step(i)
        self.clear_colors()
        self.color_list = []
        self.size_list = []
        self.ids.size_num_input.text = ''
        self.ids.size_type_input.text = 'Size Type'
        self.ids.size_out.text = 'My Sizes'
        self.size_list = []
        # self.ids.limit1.text = ""
        # self.ids.limit2.text = ""
        # self.ids.limit3.text = ""
        # self.ids.price1.text = ""
        # self.ids.price2.text = ""
        # self.ids.price3.text = ""
        # self.ids.drop_category.text='Category'
        # for limit in self.limit:
        #     limit.text = ""
        # for price in self.price:
        #     price.text = ""
    def clear_step(self, num):
        self.ids[str(num)].ids.min_input.text = ''
        self.ids[str(num)].ids.max_input.text = ''
        self.ids[str(num)].ids.price_input.text = ''

    def clear_colors(self):
        for child in self.ids.color_grid.children:
            if 'un_' not in child.icon:
                child.icon = child.icon[:22] + 'un_' + child.icon[22:]

    def change_to_cat(self):
        SideBar.change_to_cat(self)

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=2022, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

#------------------------------DROPDOWN----------------------------------
    def show_dropdown_size_num(self):
        menu_items = []
        for number in range(0, 100, 1):
            menu_items.append(
                {
                    'text': str(number),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(number): self.save_size_num(x),
                }
            )
            menu_items.append(
                {
                    'text': str(number+.5),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(number+.5): self.save_size_num(x),
                }
            )

        self.drop_down_size_num = MDDropdownMenu(
            caller=self.ids.size_num_input,
            items=menu_items,
            width_mult=4,

        )

        self.drop_down_size_num.open()
    def save_size_num(self, number):
        self.ids.size_num_input.text = number
        self.drop_down_size_num.dismiss()

#----------------------------------------------------------------------------------------------------

    def show_dropdown_size(self):
        menu_items = []
        for size in self.size_list:
            menu_items.append(
                {
                    'text': str(size),
                    "viewclass": "OneLineListItem",
                    "on_release":lambda x=str(size): self.save_size(x),
                }
            )

        self.drop_down_size = MDDropdownMenu(
            caller=self.ids.size_out,
            items=menu_items,
            width_mult=4,


        )

        self.drop_down_size.open()
    def save_size(self, size):
        self.ids.size_out.text = size
        self.drop_down_size.dismiss()

#----------------------------------------------------------------------------------------------------
    def show_dropdown_size_type(self):
        menu_items = []
        for type in ['cm', 'm', 'kg', 'g']:
            menu_items.append(
                {
                    'text': type,
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=type: self.save_size_type(x),
                }
            )

        self.drop_down_size_type = MDDropdownMenu(
            caller=self.ids.size_type_input,
            items=menu_items,
            # width_mult=4,
            size_hint=(1, 1),
        )

        self.drop_down_size_type.open()
    def save_size_type(self, type):
        self.ids.size_type_input.text = type
        self.drop_down_size_type.dismiss()

#----------------------------------------------------------------------------------------------------

    def show_dropdown_year(self):
        menu_items = []
        for year in range(2021, 1900, -1):
            menu_items.append(
                {
                    'text': str(year),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(year): self.save_year(x),
                }
            )

        self.drop_down_years = MDDropdownMenu(
            caller=self.ids.year_input,
            items=menu_items,
            width_mult=4,

        )
        self.drop_down_years.open()
    def save_year(self, year):
        self.ids.year_input.text = year
        self.drop_down_years.dismiss()

    def show_dropdown_month(self):
        menu_items = []
        for month in range(12, 1, -1):
            menu_items.append(
                {
                    'text': str(month),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(month): self.save_month(x),
                }
            )

        self.drop_down_months = MDDropdownMenu(
            caller=self.ids.month_input,
            items=menu_items,
            width_mult=4,

        )
        self.drop_down_months.open()
    def save_month(self, month):
        self.ids.month_input.text = month
        self.drop_down_months.dismiss()

#----------------------------------------------------------------------------------------------------

    def show_dropdown_day(self):
        menu_items = []
        for day in range(31, 1, -1):
            menu_items.append(
                {
                    'text': str(day),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(day): self.save_day(x),
                }
            )

        self.drop_down_days = MDDropdownMenu(
            caller=self.ids.day_input,
            items=menu_items,
            width_mult=4,

        )

        self.drop_down_days.open()
    def save_day(self, day):
        self.ids.day_input.text = day
        self.drop_down_days.dismiss()

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

#------------------------------------------PHOTOS-------------------------------------------------

    def remove_photo(self):
        if self.i == 0:
            return
        # self.photo_list.remove(self.carousel.current_slide)
        del self.photo_list[self.carousel.current_slide]
        self.carousel.remove_widget(self.carousel.current_slide)
        self.i -=1
        if self.i == 0:
            self.ids.choose1.size_hint_y -= .4
            self.ids.cover.size_hint_y -= .3
            self.ids.photo_title.size_hint_y += .09
            self.ids.choose.remove_widget(self.carousel)
            self.ids.choose.remove_widget(self.righttt)
            self.ids.choose.remove_widget(self.left)
    def move_right(self):
        self.carousel.load_next(mode='next')

    def move_left(self):
        self.carousel.load_previous()

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
        #self.size_hint_y = 1.5
        im = Image(source = path)
        if self.i == 0:
            self.left = Left()
            self.left.bind(on_press=lambda x:self.move_left())
            self.carousel = Car()
            self.righttt = Right()
            self.righttt.bind(on_press=lambda x: self.move_right())
            self.ids.choose.add_widget(self.left,1)
            self.ids.choose.add_widget(self.carousel,1)
            self.ids.choose.add_widget(self.righttt, 1)
            self.ids.choose1.size_hint_y += .4
            self.ids.cover.size_hint_y += .3
            self.ids.photo_title.size_hint_y -= .07
            self.height = '350dp'
        self.carousel.add_widget(im,self.i)
        #self.size_hint_y += .5
        with open(path, "rb") as image:
            f = image.read()
            # image.close()
        self.photo_list[im] = f
        self.i+=1
        #self.size_hint_y+= 10
        #self.bind(minimum_height = self.setter('height'))
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


class Sub_Category_box(BoxLayout):
    pass


class CustomDropDown(DropDown):
    pass

dropdown = CustomDropDown()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

class MyButton(Button):
    pass

class MyStepInput(TextInput):
    pass

class MyStepLabel(MDLabel):
    pass

class StepLayout(GridLayout):
    step = StringProperty()
    def __init__(self,step, **kwargs):
        super(StepLayout, self).__init__(**kwargs)
        self.step = step
    def get_step(self):
        return self.step

class StepLayoutStart(GridLayout):
    def __init__(self,**kwargs):
        super(StepLayoutStart, self).__init__(**kwargs)

    def get_step(self):
        return self.parent.parent.parent.parent.get_step()


class Right(MDIconButton):
    pass

class Left(MDIconButton):
    pass

class Car(Carousel):
    pass

class Btn(Button):
    pass
