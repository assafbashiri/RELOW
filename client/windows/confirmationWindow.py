from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast


class CONFIRMATIONScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'confirmation_screen'
        super(CONFIRMATIONScreen, self).__init__(**kwargs)

    def complete_register(self):
        code = self.ids.code.text
        if code == '':
            toast('you need to insert code')
            return
        else:
            ans = App.get_running_app().controller.complete_register(code)
            if ans.res is True:
                toast('lets start')
                App.get_running_app().root.current = 'menu_screen'
            else:
                toast(ans.message)
                return
