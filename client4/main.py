from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

Builder.load_file('Main.kv')
Builder.load_file('maneger.kv')
Builder.load_file('conn.kv')
Builder.load_file('register.kv')

class MENUScreen(Screen):
    def __init__(self, **kwargs):
        self.name='home'
        super(MENUScreen,self).__init__(**kwargs)

class CONNECTScreen(Screen):
    def __init__(self, **kwargs):
        self.name='home'
        super(CONNECTScreen,self).__init__(**kwargs)

class ACCOUNTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'home'
        super(ACCOUNTScreen, self).__init__(**kwargs)


class Manager(ScreenManager):
    pass


class MessageBox(Popup):
    message = StringProperty()

class RecycleViewRow(BoxLayout):
    text = StringProperty()

class Connect_box(BoxLayout):
    pass

class Register(BoxLayout):
    pass

class Menu_box(BoxLayout):
    def message_box(self, message):
        p = MessageBox()
        p.message = message
        p.open()
        print('test press: ', message)

class Offers_Screen(RecycleView):
    def __init__(self, **kwargs):
        super(Offers_Screen, self).__init__(**kwargs)
        self.data = [{'text': "Button " + str(x), 'id': str(x)} for x in range(20)]



class TestApp(MDApp):
    title = "RecycleView Direct Test"

    def build(self):
        return Manager()

    def login(self):
        #self.root.ids.login_label.text = f'hi {self.root.ids.user.text}'
        username = self.root.ids.user.text
        password = self.root.ids.password.text
        # call to log in with username and password

    def clear_login(self):
        #self.root.ids.login_label.text="Log In"
        self.root.ids.user.text=""
        self.root.ids.password.text=""

    def register(self):
        username = self.root.ids.user_name.text
        first_name = self.root.ids.first_name.text
        last_name = self.root.ids.last_name.text
        user_name = self.root.ids.user_name.text
        email = self.root.ids.email.text
        password = self.root.ids.password.text
        #birth_date = datetime(self.root.ids.birth_date.text)
        gender = self.root.ids.gender.text
        # call to log in with username and password

    def clear_register(self):
        #self.root.ids.login_label.text="Log In"
        self.root.ids.first_name.text = ""
        self.root.ids.last_name.text = ""
        self.root.ids.user_name.text=""
        self.root.ids.email.text=""
        self.root.ids.password.text=""
        self.root.ids.birth_date.text=""
        self.root.ids.gender.text=""

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=1996, month=12, day=15)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    #click OK
    def on_save(self,instance, value, date_range):
        print(self.root)
        print(self.root.ids)
        print(self.root.ids.bolo)
        print(self.root.ids.bolo.ids)
        print(self.root.ids.bolo.ids.bolo2)
        print(self.root.ids.bolo.ids.bolo2.ids.birth_date)
        self.root.ids.bolo.ids.bolo2.ids.birth_date.text = str(value)
        # birth_date = value


    #click Cancel
    def on_cancel(self,instance, value):
        print("")

if __name__ == "__main__":
    TestApp().run()