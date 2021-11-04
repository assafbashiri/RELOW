from kivy.app import App
from kivy.uix.screenmanager import Screen

from assets.Utils.Utils import Utils


class CONFIRMATIONScreen(Screen):
    def __init__(self, **kwargs):
        self.name = 'confirmation_screen'
        super(CONFIRMATIONScreen, self).__init__(**kwargs)

    def complete_register(self):
        email = App.get_running_app().root.screens[8].children[0].children[1].ids.email.text
        password = App.get_running_app().root.screens[8].children[0].children[1].ids.password.text
        code = self.ids.code.text
        if code == '':
            Utils.pop(self, 'you need to insert code', 'alert')
            return
        else:
            ans = App.get_running_app().controller.complete_register(code, email)
            if ans.res is True:
                App.get_running_app().root.change_screen("menu_screen")
                App.get_running_app().controller.login_from_exist_user(email, password)
                self.update_hello_name("        Hello, " + App.get_running_app().controller.user_service.first_name)
            else:
                Utils.pop(self, "Incorrect code", 'alert')
                return

    def update_hello_name(self, msg):
        pass
        # menu screen 0
        # App.get_running_app().root.screens[0].ids.menu_box.ids.side_box.ids.hello.text = msg
        # # connect screen 1
        # App.get_running_app().root.screens[1].children[0].ids.side_box.ids.hello.text = msg
        # # account screen 2
        # App.get_running_app().root.screens[2].children[0].ids.side_box.ids.hello.text = msg
        # # search screen 3
        # App.get_running_app().root.screens[3].children[0].ids.side_box.ids.hello.text = msg
        # # add offer screen 4
        # App.get_running_app().root.screens[4].children[0].ids.side_box.ids.hello.text = msg
        # # my offers screen 5
        # # App.get_running_app().root.screens[5].children[0].ids.side_box.ids.hello.text = msg
        #
        # # update offers screen 6
        # App.get_running_app().root.screens[6].children[0].ids.side_box.ids.hello.text = msg
        # # register screen 7
        # App.get_running_app().root.screens[7].ids.side_box.ids.hello.text = msg
        # # login screen 8
        # App.get_running_app().root.screens[8].ids.side_box.ids.hello.text = msg
        # # # contact screen 9
        # # App.get_running_app().root.screens[9].children[0].ids.side_box.ids.hello.text = msg
        # # # confirmation screen 10
        # # z = App.get_running_app().root.screens[10].children[0].ids.side_box.ids.hello.text = msg
        # # # password screen 11
        # # z = App.get_running_app().root.screens[11].children[0].ids.side_box.ids.hello.text = msg
        # # seller screen 12
        # App.get_running_app().root.screens[12].ids.side_box.ids.hello.text = msg
