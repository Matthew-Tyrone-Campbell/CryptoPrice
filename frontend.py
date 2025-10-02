from backend import Crypto, get_api_key, menu

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

crypto_object = Crypto(get_api_key())
crypto_prices = crypto_object.get_crypto_prices()
class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        for x in crypto_prices:
            layout.add_widget(Button(text=f"{x}: ${crypto_prices[x]}", background_color=(18, 94, 145, 0.37)))
        return layout


if __name__ == '__main__':
    MyApp().run()