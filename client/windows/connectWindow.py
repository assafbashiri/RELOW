from datetime import datetime
from kivymd.uix.picker import MDDatePicker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from Utils.CheckValidity import CheckValidity
from Utils.Utils import Utils
from windows.SideBar import SideBar


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty, ReferenceListProperty
from kivy.properties import NumericProperty
from kivy.graphics import Line, Color
class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class CONNECTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'connect_screen'
        super(CONNECTScreen, self).__init__(**kwargs)


class Category_box(BoxLayout):
    pass

class Sub_Category_box(BoxLayout):
    pass

class Connect_box(BoxLayout):

    def exit(self):
        self.ids.recycle1.insert_offers(list=App.get_running_app().controller.get_hot_deals())

    def __init__(self, **kwargs):
        super(Connect_box, self).__init__(**kwargs)
        self.cat = Category_box()
        self.sub_cat = Sub_Category_box()
        self.gender = 0

    def register_new(self):
        App.get_running_app().root.current = 'register_screen'

    def login_new(self):
        App.get_running_app().root.current = 'login_screen'

    def change_to_cat(self):
        SideBar.change_to_cat(self)


    def clear_register(self):
        self.ids.phone.text=""
        self.ids.first_name.text=""
        self.ids.last_name.text=""
        self.ids.email.text=""
        self.ids.password.text=""
        self.ids.birth_date.text=""

    def unregister(self):
        ans = App.get_running_app().controller.unregister()

        if ans.res is True:
            self.parent.parent.back_to_main()

    def register(self):
        controller = App.get_running_app().controller
        if controller.user_service is not None:
            if controller.guest is False:
                Utils.pop(self, 'you need to logout first', 'alert')
                #toast('you need to logout first')
                return
        phone = self.ids.phone.text
        phone_bool = CheckValidity.checkValidityPhone(self, phone)

        if not phone_bool:
            return


        first_name = self.ids.first_name.text
        bool_ans=self.validate_name(first_name)
        if not bool_ans:
            return

        last_name = self.ids.last_name.text
        bool_ans = self.validate_name(last_name)
        if not bool_ans:
            return

        email = self.ids.email.text
        email_bool = CheckValidity.checkValidityEmail(self,email)
        if not email_bool:
            return

        password = self.ids.password.text
        password_bool = CheckValidity.checkValidityPassword(self,password)
        if not password_bool:
            return

        birth_date_str = self.ids.birth_date.text
        birth_date = Utils.string_to_datetime_without_hour(self, birth_date_str)
        gender = self.gender
        ans = App.get_running_app().controller.register(first_name, last_name, phone, email, password, birth_date,
                                                        gender)
        if ans.res is True:
            self.parent.parent.back_to_main()

    def validate_name(self,name):
        name_bool = CheckValidity.checkValidityName(self,name)
        return name_bool


    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # click OK
    def on_save(self, instance, value, date_range):
        self.ids.birth_date.text = str(value)
        # birth_date = value

    # click Cancel
    def on_cancel(self, instance, value):
        pass

    def show_dropdown(self):

        menu_items = [
            {
                "text": "male",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=1: self.menu_callback(x,"male"),
            } ,
            {
                "text": "female",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=2: self.menu_callback(x, "female"),
            }
        ]
        self.drop_down = MDDropdownMenu(
            caller=self.ids.drop,
            items=menu_items,
            width_mult=4,
        )
        self.drop_down.open()

    def menu_callback(self, gender_int, gender_string):
        self.gender = gender_int
        self.ids.drop.text = gender_string
        self.drop_down.dismiss()


    def back_to_menu(self):
        App.get_running_app().root.current = 'menu_screen'



class BorderBehavior(Widget):
    borders = ObjectProperty(None)
    border_origin_x = NumericProperty(0.)
    border_origin_y = NumericProperty(0.)
    border_origin = ReferenceListProperty(border_origin_x, border_origin_y)

    left_border_points = []
    top_border_points = []
    right_border_points = []
    bottom_border_points = []

    CAP = 'square'
    JOINT = 'none'

    dash_styles = {
        'dashed':
        {
            'dash_length': 10,
            'dash_offset': 5
        },
        'dotted':
        {
            'dash_length': 1,
            'dash_offset': 1
        },
        'solid':
        {
            'dash_length': 1,
            'dash_offset': 0
        }
    }

    def draw_border(self):
        line_kwargs = {
            'points': [],
            'width': self.line_width,
            'cap': self.CAP,
            'joint': self.JOINT,
            'dash_length': self.cur_dash_style['dash_length'],
            'dash_offset': self.cur_dash_style['dash_offset']
        }

        with self.canvas.after:
            self.border_color = Color(*self.line_color)
            # left border
            self.border_left = Line(**line_kwargs)

            # top border
            self.border_top = Line(**line_kwargs)

            # right border
            self.border_right = Line(**line_kwargs)

            # bottom border
            self.border_bottom = Line(**line_kwargs)

    def update_borders(self):
        if hasattr(self, 'border_left'):
            # test for one border is enough so we know that the borders are
            # already drawn
            width = self.line_width
            dbl_width = 2 * width

            self.border_left.points = [
                self.border_origin_x,
                self.border_origin_y,
                self.border_origin_x,
                self.border_origin_y +
                self.size[1] - dbl_width
            ]

            self.border_top.points = [
                self.border_origin_x,
                self.border_origin_y + self.size[1] - dbl_width,
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y + self.size[1] - dbl_width
            ]

            self.border_right.points = [
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y + self.size[1] - dbl_width,
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y
            ]

            self.border_bottom.points = [
                self.border_origin_x + self.size[0] - dbl_width,
                self.border_origin_y,
                self.border_origin_x,
                self.border_origin_y
            ]

    def set_border_origin(self):
        self.border_origin_x = self.pos[0] + self.line_width
        self.border_origin_y = self.pos[1] + self.line_width

    def on_border_origin(self, instance, value):
        self.update_borders()

    def on_size(self, instance, value):
        # not sure if it's really needed, but if size is changed
        # programatically the border have to be updated
        # --> needs further testing
        if hasattr(self, 'line_width'):
            self.set_border_origin()
            self.pos = self.border_origin

    def on_pos(self, instance, value):
        # print instance, value, "pos changed"
        if hasattr(self, 'line_width'):
            self.set_border_origin()

    def on_borders(self, instance, value):
        self.line_width, self.line_style, self.line_color = value
        self.cur_dash_style = self.dash_styles[self.line_style]
        # print self.cur_dash_style, "dash_style selected"
        self.set_border_origin()
        self.draw_border()

    # touch events for testing
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
                touch.grab(self)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            # I received my grabbed touch
            self.pos = (touch.x, touch.y)
        # else:
        #     print "only touched"
        #     # it's a normal touch

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            # I receive my grabbed touch, I must ungrab it!
            touch.ungrab(self)
        # else:
        #     # it's a normal touch
        #     print "normal touch up"
        #     pass

