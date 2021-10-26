from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


class TERMSScreen(Screen):
    def __init__(self, **kwargs):
        super(TERMSScreen, self).__init__(**kwargs)
        self.name = 'terms_screen'

class Terms_box(BoxLayout):
    def __init__(self, **kwargs):
        super(Terms_box, self).__init__(**kwargs)
