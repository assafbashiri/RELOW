from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivymd.app import MDApp

Builder.load_file('Main.kv')


class MessageBox(Popup):
    message = StringProperty()

class RecycleViewRow(BoxLayout):
    text = StringProperty()

class MmainScreen(BoxLayout):
    def message_box(self, message):
        p = MessageBox()
        p.message = message
        p.open()
        print('test press: ', message)

class MainScreen(RecycleView):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.data = [{'text': "Button " + str(x), 'id': str(x)} for x in range(20)]



class TestApp(MDApp):
    title = "RecycleView Direct Test"

    def build(self):
        return MmainScreen()

if __name__ == "__main__":
    TestApp().run()