from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from assets.Utils.Utils import Utils


class CONTACTScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'contact_us_screen'
        super(CONTACTScreen, self).__init__(**kwargs)

class Contact_box1(BoxLayout):
    def __init__(self,**kwargs):
        super(Contact_box1, self).__init__(**kwargs)

    def exit(self):
        App.get_running_app().controller.exit()


class Desc_Subject_Box(BoxLayout):
    drop_down = ObjectProperty()

    def __init__(self, **kwargs):
        super(Desc_Subject_Box, self).__init__(**kwargs)
        self.controller = App.get_running_app().controller
        self.label = MDLabel(text="")
        self.dialog = None

    def back(self):
        App.get_running_app().root.change_screen("menu_screen")

    def send_contact_us(self):
        if self.controller.guest is True:
            Utils.pop(self, 'have to log in or register to contact us', 'alert')
            return
        subject = self.ids.subject.text
        description = self.ids.description.text
        self.label.text = ""
        if subject == "":
            Utils.pop(self, 'please write a subject', 'alert')
            return
        if description == "":
            Utils.pop(self, 'please write a description', 'alert')
            return

        ans = App.get_running_app().controller.contact_us(subject, description)
        if ans.res is True:
            Utils.pop(self, 'thank you for contact us, we will answer you soon via your mail', 'success')
            self.ids.subject.text = ""
            self.ids.description.text = ""
            App.get_running_app().root.change_screen("menu_screen")


