from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager
from assets.Utils.Utils import Utils
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import platform
# from android.permissions import request_permissions, Permission
# from android.storage import primary_external_storage_path
from assets.Service.Object.StepService import StepService

from assets.Utils.CheckValidity import CheckValidity


class ADDOFFERScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'add_screen'
        super(ADDOFFERScreen, self).__init__(**kwargs)


# ---------------------------------------------------


class Category_box(BoxLayout):
    pass


MIN_difference_LIMIT = 10
MIN_difference_PRICE = 100


class BoxLayout_helper(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayout_helper, self).__init__(**kwargs)


class Add_offer_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Add_offer_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        self.chosen_cat_name = None
        self.sub_cat12 = None
        self.dialog = None
        self.step = 2

        self.next_step = []
        self.price = []
        self.limit = []
        self.color_list = []
        self.size_list = []

        # for photos
        self.carousel = None
        self.i = 0
        self.photo_list = {}
        self.dialog = None

        # ------------------------SIZE NUM DROPDOWN---------------------------#

        size_num = ['1', '2', '3', '4']
        self.size_num_dropdown = DropDown()
        for size in size_num:
            btn = MyButton(text=' % s' % size)
            btn.bind(on_release=lambda btn: self.add_size_num(btn))
            self.size_num_dropdown.add_widget(btn)
        self.size_num_mainbutton = MyButton(text='sizes')
        self.size_num_mainbutton.bind(on_press=lambda x: self.size_num_dropdown.open(x))

        # ------------------------SIZE KIND DROPDOWN---------------------------#

        size_kind = ['inch', 'cm', 'kg', 'pond']
        self.size_kind_dropdown = DropDown()
        for size_kind in size_kind:
            btn = MyButton(text=' % s' % size_kind)
            btn.bind(on_release=lambda btn: self.add_size_kind(btn))
            self.size_kind_dropdown.add_widget(btn)
        self.size_kind_mainbutton = Button(text='size kind')
        self.size_kind_mainbutton.bind(on_press=lambda x: self.size_kind_dropdown.open(x))

        # ------------------------SIZE RES DROPDOWN---------------------------#

        self.size_dropdown = DropDown()
        self.size_mainbutton = Button(text='My Sizes')
        self.size_mainbutton.bind(on_press=self.size_dropdown.open)
        self.add_size = Button(text='Add')
        self.add_size.bind(on_press=lambda tex: self.add_size_(tex))

        # ---------------------------------------------------#
        Clock.schedule_once(self.init_colors, 0)
        # Clock.schedule_once(self.add_size_start, 0)
        self.steps_pointers = {}
        self.first_time_pointers = True

    def back(self):
        App.get_running_app().root.change_screen("menu_screen")

    def add_size_start(self, num):
        self.ids.size_drop_box.add_widget(self.size_mainbutton)
        self.ids['my_sizes'] = self.size_mainbutton

    def add_size_(self):
        if self.ids.size_num_input.text == "":
            Utils.pop(self, f'please enter size number', 'alert')
            return
        elif self.ids.size_type_input.text == "Size Type":
            Utils.pop(self, f'please enter size type', 'alert')
            return

        text = self.ids.size_num_input.text + ' ' + self.ids.size_type_input.text
        text = text.replace(",", "-")

        if text not in self.size_list:
            self.size_list.append(text)

    def remove_size(self):
        if len(self.size_list) == 0:
            return
        size = self.ids.size_out.text
        if size == 'My Sizes':
            return
        self.size_list.remove(size)

        if len(self.size_list) == 0:
            self.ids.size_out.text = 'My Sizes'
        else:
            self.ids.size_out.text = self.size_list[0]

    def init_colors(self, num):
        colors = ['argaman', 'azure', 'brown', 'green', 'grey', 'orange', 'pink', 'purple',
                  'softblue', 'softgreen', 'softgrey', 'red', 'black', 'blue', 'yellow', 'white']
        colors_counter = 0
        for color in colors:
            ip = "assets/windows/images/colors/un_" + color + ".png"
            btn = MDIconButton(icon=ip)
            btn.text = color
            btn.bind(on_press=lambda instance=1, color_name=color: self.chose_color(
                instance, color_name))
            self.ids.color_grid.add_widget(btn)
            colors_counter = colors_counter + 1

    def chose_color(self, btn, text):
        if text in self.color_list:
            self.color_list.remove(text)
            btn.icon = "assets/windows/images/colors/un_" + text + ".png"
        # change color of all the other button to the regular color
        # change color of the selected button
        else:
            btn.icon = "assets/windows/images/colors/" + text + ".png"
            # chosen colors for add offer
            self.color_list.append(text)

    def init_steps_pointers(self):
        if self.first_time_pointers is True:
            x = self.ids.steps_box.children
            self.steps_pointers[1] = x[2]
            self.steps_pointers[2] = x[1]
            self.first_time_pointers = False

    def add_step(self):
        self.init_steps_pointers()
        if self.step == 4:
            Utils.pop(self, f'4 steps is the maximum steps for offer', 'alert')
            return
        self.ids.steps_box.size_hint_y += .3
        self.ids.cover.size_hint_y += .3
        self.step += 1
        self.step_to_add = StepLayout(str(self.step))
        self.ids[str(self.step)] = self.step_to_add
        self.ids.steps_box.add_widget(self.step_to_add, 1)
        self.steps_pointers[self.step] = self.step_to_add
        self.set_next_minimum(self.step - 1)

    def remove_step(self):
        if self.step == 2:
            Utils.pop(self, f'2 steps is the minimum for offer', 'alert')
            return
        a = len(self.ids.steps_box.children)
        self.ids.steps_box.remove_widget(self.steps_pointers[self.step])
        self.ids.steps_box.size_hint_y -= .3
        self.ids.cover.size_hint_y -= .4
        self.steps_pointers.pop(self.step, None)
        self.step -= 1

    def add_offer(self):
        list = [v for k, v in self.photo_list.items()]
        product_name = self.ids.product_name_input.text
        category_name = self.chosen_cat_name
        sub_category_name = self.sub_cat12
        company = self.ids.company_name_input.text
        description = self.ids.description_input.text
        sizes = self.build_string_from_list(self.size_list)
        colors = self.build_string_from_list(self.color_list)
        if not CheckValidity.check_validity_product_company_name(self, product_name):
            return
        if not CheckValidity.check_validity_product_company_name(self, company):
            return
        if not CheckValidity.check_validity_description(self, description):
            return
        # photos check
        if len(list) == 0:
            Utils.pop(self, f'at least 1 photo for offer', 'alert')
            return
        if not self.check_steps_validity():
            return
        if self.size_list == []:
            Utils.pop(self, f'at least 1 size for offer', 'alert')
            return
        if self.color_list == []:
            Utils.pop(self, f'at least 1 color for offer', 'alert')
            return
        if self.sub_cat12 is None:
            Utils.pop(self, f'please chose sub category', 'alert')
            return
        if self.ids.year_input.text == "Year":
            Utils.pop(self, f'please chose year', 'alert')
            return
        if self.ids.month_input.text == "Month":
            Utils.pop(self, f'please chose month', 'alert')
            return
        if self.ids.day_input.text == "Day":
            Utils.pop(self, f'please chose day', 'alert')
            return

        end_date = self.ids.year_input.text + '-' + self.ids.month_input.text + '-' + self.ids.day_input.text
        if not CheckValidity.checkEndDate(self, end_date):
            return

        steps = []
        for i in range(1, self.step + 1):
            price = self.steps_pointers[i].ids.price_input.text
            limit = self.steps_pointers[i].ids.max_input.text
            step = StepService(0, price, i, limit)
            steps.append(vars(step))
        ans = App.get_running_app().controller.add_offer(product_name, company, colors, sizes, description, list, category_name,
                                                         sub_category_name, steps, end_date)

        if ans.res is True:
            Utils.pop(self, 'your offer is waiting for approve by admin', 'success')
            screens = App.get_running_app().root.screens
            index = 0
            for screen in screens:
                if screen.name == 'add_screen':
                    screens[index] = ADDOFFERScreen()
                index = index + 1
            App.get_running_app().root.change_screen("menu_screen")
        else:
            Utils.pop(self, "we are sorry, add offer is failed", 'alert')

    def check_steps_validity(self):
        self.init_steps_pointers()
        for i in range(2, self.step + 1):
            step_prev = self.steps_pointers[i - 1]
            step_next = self.steps_pointers[i]
            # prices & limit checks
            if step_prev.ids.max_input.text == "":
                Utils.pop(self, f'please enter maximum BuyFriends amount for step {i - 1}')
                return
            if step_next.ids.max_input.text == "":
                Utils.pop(self, f'please enter maximum BuyFriends amount for step {i}')
                return
            if step_prev.ids.price_input.text == "":
                Utils.pop(self, f'please enter price for step {i - 1}')
                return
            if step_next.ids.price_input.text == "":
                Utils.pop(self, f'please enter price for step {i}')
                return
            flag = self.check_limits(int(step_prev.ids.max_input.text),
                                     int(step_next.ids.max_input.text))
            if not flag:
                return False
            flag = self.check_prices(int(step_prev.ids.price_input.text),
                                     int(step_next.ids.price_input.text))
            if not flag:
                return False
        return True

    def check_limits(self, limit1, limit2):
        if limit1 > limit2:
            Utils.pop(self, f'limit should be more then his following limit {str(limit1)} {str(limit2)}', 'alert')
            return False

        if (limit2 - limit1) < MIN_difference_LIMIT:
            Utils.pop(self,
                      f'the difference between your limit is too small ->  {str(limit1)} {str(limit2)} '
                      f'this is the min difference: {str(MIN_difference_LIMIT)}',
                      'alert')
            return False
        return True

    def check_prices(self, price1, price2):
        if price2 > price1:
            Utils.pop(self, f'price should be smaller then his following price {str(price1)} {str(price2)}', 'alert')
            return False

        if (price1 - price2) < MIN_difference_PRICE:
            Utils.pop(self,
                      f'the difference between your price is too short -> {str(price1)} {str(price2)}'
                      f' this is the min difference: {str(MIN_difference_PRICE)}',
                      'alert')
            return False
        return True



    # ------------------------------DROPDOWN----------------------------------
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
                    'text': str(number + .5),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(number + .5): self.save_size_num(x),
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

    def show_dropdown_size(self):
        menu_items = []
        for size in self.size_list:
            menu_items.append(
                {
                    'text': str(size),
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=str(size): self.save_size(x),
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

    # ----------------------------------------------------------------------------------------------------

    def show_dropdown_year(self):
        menu_items = []
        today_year = datetime.today().year
        today_month = datetime.today().month
        limit_year = today_year
        if today_month == 12:
            limit_year = today_year + 1
        for year in range(limit_year, today_year - 1, -1):
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
        today_month = datetime.today().month
        next_month = today_month + 1
        if today_month == 12:
            next_month = 1
        for month in range(next_month, today_month-1, -1):
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

    def show_dropdown_day(self):
        if self.ids.month_input.text == "Month":
            month = "1"
        else:
            month = self.ids.month_input.text
        if month == "2":
            max_day = 28
        if month == "1" or month == "3" or month == "5" or month == "7" or month == "8" or month == "10" or month == "12":
            max_day = 31
        if month == "4" or month == "6" or month == "9" or month == "11":
            max_day = 30
        menu_items = []
        min_day = 0
        if int(month) == datetime.today().month:
            min_day = datetime.today().day - 1

        for day in range(max_day, min_day, -1):
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

    # ----------------------------------------------------------------------------------------------------

    def show_dropdown_category(self):
        categories = App.get_running_app().controller.get_categories()
        menu_items = []
        for cat in categories:
            menu_items.append(
                {"text": cat.name,
                 "viewclass": "OneLineListItem",
                 "on_release": lambda x=cat.get_sub_categories_names(), y=cat.name: self.show_dropdown_sub_category(x,
                                                                                                                    y),
                 }
            )

        self.drop_down_category = MDDropdownMenu(
            caller=self.ids.drop_category,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down_category.open()

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

    def build_string_from_list(self, list):
        answer = []
        if len(list) > 0:
            answer = list[0]
            i = 0
            for item in list:
                if i != 0:
                    answer = answer + "," + item
                i = i + 1
        return answer

    def set_prev_maximum(self, step):
        self.init_steps_pointers()
        step = int(step)
        # if step = 1 -> nothing to do -> never happened
        # if step = 2 -> have to change step 1 maximum
        # if step = 3 -> have to change step 2 maximum
        # if step = 4 -> have to change step 3 maximum
        temp = self.steps_pointers[step].children[0].children[4].text
        if temp == '':
            temp = 0
        temp = int(temp)
        temp = temp - 1
        temp = str(temp)
        self.steps_pointers[step - 1].children[0].children[2].text = temp

    def set_next_minimum(self, step):
        self.init_steps_pointers()
        step = int(step)
        # if step = 1 -> have to change step 2 minimum
        # if step = 2 -> have to check if there is step 3
        # if step = 3 -> have to check if there is step 4
        # if step = 4 -> nothing to do -> never happened
        temp = self.steps_pointers[step].children[0].children[2].text
        if temp == '':
            temp = 0
        temp = int(temp) + 1
        temp = str(temp)
        if step + 1 in self.steps_pointers.keys():
            self.steps_pointers[step + 1].children[0].children[4].text = temp

    def exit(self):
        App.get_running_app().controller.exit()

    # ------------------------------------------PHOTOS-------------------------------------------------

    def remove_photo(self):
        if self.i == 0:
            return
        # self.photo_list.remove(self.carousel.current_slide)
        del self.photo_list[self.carousel.current_slide]
        self.carousel.remove_widget(self.carousel.current_slide)
        self.i -= 1
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
        print("wooooooooow")
        # request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
        #              Permission.READ_EXTERNAL_STORAGE])
        path = '/'
        if platform == 'android':
            # path =  primary_external_storage_path()
            path = '/'
        #path = os.getenv('EXTERNAL_STORAGE')
        #path = '"/storage/"'  # path to the directory that will be opened in the file manager
        self.photo_popup = Popup()
        self.photo_popup_box = BoxLayout(orientation = 'vertical')
        self.manager = FileChooserIconView(
            # exit_manager=self.exit_manager,  # function called when the user reaches directory tree root
            # select_path=self.select_path,  # function called when selecting a file/directory
        )
        self.manager.bind(on_submit = self.photo_helper)
        # self.manager.bind(on_selection= lambda *args:self.photo_helper2(self.manager.selection))
        # self.manager.bind(on_subentry_to_entry= self.photo_helper2)
        # self.manager.bind(on_press= lambda *args:self.photo_helper2(self.manager.selection))
        add_photo_btn = Button(text = 'Add photo')
        add_photo_btn.bind(on_press = self.select_path)
        add_photo_btn.size_hint_y = .1
        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.photo_popup.dismiss)
        back_btn.size_hint_y = .1
        self.popup_current_photo = Image(source = "")

        self.photo_popup_box.add_widget(self.manager)
        self.photo_popup_box.add_widget(add_photo_btn)
        self.photo_popup_box.add_widget(back_btn)
        self.photo_popup.add_widget(self.photo_popup_box)
        self.photo_popup.open()
        self.photo_first_time = True
        # self.ids.choose.add_widget(self.manager)
        # self.ids.choose.size_hint_y += 3
    def photo_choose(self, path):
        a = 8

    def photo_helper(self,a,b,c):
        # if self.popup_current_photo.source != "":
        if self.photo_first_time is True:
            self.photo_popup_box.add_widget(self.popup_current_photo, 3)
            self.photo_first_time = False
        self.popup_current_photo.source = b[0]



    def select_path(self, a):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        path = self.manager.selection[0]
        print('path      ' + path)
        # self.size_hint_y = 1.5
        im = Image(source=path)
        if self.i == 0:
            self.left = Left()
            self.left.bind(on_press=lambda x: self.move_left())
            self.carousel = Car()
            self.righttt = Right()
            self.righttt.bind(on_press=lambda x: self.move_right())
            self.ids.choose.add_widget(self.left, 1)
            self.ids.choose.add_widget(self.carousel, 1)
            self.ids.choose.add_widget(self.righttt, 1)
            self.ids.choose1.size_hint_y += .4
            self.ids.cover.size_hint_y += .3
            self.ids.photo_title.size_hint_y -= .07
            self.height = '350dp'
        self.carousel.add_widget(im, self.i)
        # self.size_hint_y += .5
        with open(path, "rb") as image:
            f = image.read()
            # image.close()
        self.photo_list[im] = f
        self.i += 1
        # self.size_hint_y+= 10
        # self.bind(minimum_height = self.setter('height'))
        # self.manager.exit_manager()
        Utils.pop(self, 'picture add succesfully', 'succes')
        # toast("picture add succesfully")

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
    def __init__(self, step, **kwargs):
        self.step = step
        super(StepLayout, self).__init__(**kwargs)

    def get_step(self):
        return self.step


class StepLayoutStart1(GridLayout):
    def __init__(self, **kwargs):
        super(StepLayoutStart1, self).__init__(**kwargs)

    def get_step(self):
        return self.parent.parent.parent.parent.get_step()

    def change_first_min_buyfriends(self):
        self.children[0].children[4].text = "0"


class StepLayoutStart2(GridLayout):
    def __init__(self, **kwargs):
        super(StepLayoutStart2, self).__init__(**kwargs)

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
