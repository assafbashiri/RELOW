from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast

from Utils.Utils import Utils


class CONFIRMATIONScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'confirmation_screen'
        super(CONFIRMATIONScreen, self).__init__(**kwargs)

    def complete_register(self):
        a = App.get_running_app()
        email = App.get_running_app().controller.user_service.email
        code = self.ids.code.text
        if code == '':
            Utils.pop(self, 'you need to insert code', 'alert')
            return
        else:
            ans = App.get_running_app().controller.complete_register(code, email)
            if ans.res is True:
                App.get_running_app().root.current = 'menu_screen'
            else:
                Utils.pop(self, ans.message, 'alert')
                return
