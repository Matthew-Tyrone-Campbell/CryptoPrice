from backend import Crypto, get_api_key, menu

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class DisplayCrypto(GridLayout):
     def __init__(self, **kwargs):
        super(DisplayCrypto, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="bitcoin"))
        self.add_widget(Label(text="Doge"))
class MyApp(App):

    def build(self):
        return DisplayCrypto()


if __name__ == '__main__':
    MyApp().run()