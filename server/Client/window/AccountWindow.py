from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class KivyButton(BoxLayout):
    def clear(self):
        print("H")
class Grid(GridLayout):
    pass
class Button1(Button):
    def aa(self):
        print("H")



class SearchApp(App):
    def build(self):
        self.grid = GridLayout(cols=1,spacing=20, pos=(1,500))
        self.box = BoxLayout(orientation='horizontal', spacing=20, pos=(5,500))
        self.txt = TextInput(hint_text='Write here', size_hint=(.5, .1))
        self.btn = Button(text='Search item', on_press=self.search_item, size_hint=(.1, .1))
        self.btn1 = Button(text='Search category', on_press=self.search_category, size_hint=(.1, .1))
        self.btn2 = Button(text='Clear', on_press=self.clear, size_hint=(.1, .1))
        self.box.add_widget(self.txt)
        self.box.add_widget(self.btn)
        self.box.add_widget(self.btn1)
        self.box.add_widget(self.btn2)
        self.grid.add_widget(self.box)
        return self.grid

    def search_item(self, instance):
        print(self.txt.text)
        self.txt.text = 'amit the king'
        #items = backend_controller.search_offer_by_name()
        # build and show items
        btn22 = Button(text='fffff', size_hint=(.1, .1))
        print("%")
        self.box.add_widget(btn22)
        print("Done srearch item")


    def search_category(self, instance):
        print(self.txt.text)
        self.txt.text = 'amit the king'
        #categories = backend_controller.search_category_by_name()
        # build and show categories

    def clear(self, instance):
        self.txt.text = ''

    def show_item(self, item):
        self.close()
        #new_window = OfferWindow(item)

    def show_category(self):
        pass

    def close(self):
        print("Doaaa")


SearchApp().run()
SearchApp().stop()