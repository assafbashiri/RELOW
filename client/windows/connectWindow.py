from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class CONNECTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'connect_screen'
        super(CONNECTScreen, self).__init__(**kwargs)

class Category_box(BoxLayout):
    pass

class Connect_box(BoxLayout):

    def __init__(self, **kwargs):
        super(Connect_box, self).__init__(**kwargs)
        self.cat = Category_box()

    def change(self):
        print(self.parent)
        self.side = self.ids.side_box
        self.remove_widget(self.side)
        print(self.parent)
        self.add_widget(self.cat)
        # self.parent.parent.ids.menu_box.remove_widget(self.parent.ids.side_box)
        # print(self.parent)
        # self.parent.parent.ids.menu_box.add_widget(self.parent.ids.side1_box)

    def back(self):
        # self.remove_widget(self.ids.category_box)
        self.add_widget(self.side)
        self.remove_widget(self.cat)

    def unregister(self):
        user_id = App.get_running_app().store.get('user')
        ans = App.get_running_app().controller.unregister(user_id['user_id'])
        res = Struct(**ans)
        print(res.message)

    def register(self):
        user_name = self.ids.user_name.text
        first_name = "top"  # self.ids.first_name.text
        last_name = "top"  # self.ids.last_name.text
        email = self.ids.email.text
        password = "top"  # self.ids.password.text
        birth_date = datetime.today()  # self.ids.birth_date.text
        gender = 1  # int(self.ids.gender.text)
        ans = App.get_running_app().controller.register(first_name, last_name, user_name, email, password, birth_date,
                                                        gender)
        if ans.res is True:
            self.parent.parent.back_to_main()

        print(ans.message)
        App.get_running_app().store.put("user", user_info=ans.data)

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # click OK
    def on_save(self, instance, value, date_range):
        print(self.root)
        print(self.root.ids)
        print(self.root.ids.bolo)
        print(self.root.ids.bolo.ids)
        print(self.root.ids.bolo.ids.bolo2)
        print(self.root.ids.bolo.ids.bolo2.ids.birth_date)
        self.root.ids.bolo.ids.bolo2.ids.birth_date.text = str(value)
        # birth_date = value

    # click Cancel
    def on_cancel(self, instance, value):
        print("")

    def login(self):
        username = self.ids.user_name.text
        password = self.ids.password.text
        ans = App.get_running_app().controller.login(username, password)
        res = Struct(**ans)
        if ans.res is True:
            self.parent.parent.back_to_main()

    def logout(self):
        user_id = App.get_running_app().store.get('user')
        ans = App.get_running_app().controller.logout(user_id['user_id'])
        res = Struct(**ans)
        print(res.message)
