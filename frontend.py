from backend import Crypto, get_api_key
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

crypto_object = Crypto(get_api_key())
crypto_object.process_data(crypto_object.get_crypto_data())
class Cryptowidget(BoxLayout):
    def __init__(self,cryptocurrency, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='horizontal',size_hint=(1,0.1), padding=([5, 5,5,5]))
        self.cryptocurrency = cryptocurrency

        self.logo = Image(
            source=f'logos/{cryptocurrency.lower()}.png',
            fit_mode='scale-down'
        )
        self.crypto_name_widget = BoxLayout(orientation='vertical')
        self.crypto_name_widget.add_widget(Label(text=cryptocurrency))      
        self.crypto_name_widget.add_widget(Label(text=crypto_object.get_crypto_initials(cryptocurrency)))
        
        self.price_widget = BoxLayout(orientation="horizontal")
        self.price_widget.add_widget(Label(text=crypto_object.get_crypto_price(cryptocurrency)))
        self.price_widget.add_widget(Label(text=crypto_object.get_crypto_change(cryptocurrency)))

        self.layout.add_widget(self.logo)
        self.layout.add_widget(self.crypto_name_widget)
        self.layout.add_widget(self.price_widget)
        
class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.surface_color = (0.28, 0.28, 0.30, 1)
        self.background_colour = (0.18, 0.18, 0.18, 1)
        self.primary_colour = (0, 0.122, 0.255, 1)
        self.text_colour = (0.220, 0.220, 0.220, 0.1)
        self.accent_color = (0.255, 0.204, 0, 1) 
    def build(self):
        layout = BoxLayout(orientation='vertical')
        top = BoxLayout(orientation='horizontal',size_hint=(1,0.1))
        body = BoxLayout(orientation='vertical', padding=([5, 5,5,5]))
        title = Button(text="Crypto Prices", 
                        background_color=self.surface_color, 
                        size_hint=(1,1), font_size = 50)
        refresh_button = Button(text="Refresh", 
                        background_color=self.primary_colour, 
                        size_hint=(1,1), font_size = 50)
        for crypto in crypto_object.crypto_data:
            body.add_widget(Cryptowidget(crypto).layout)
        top.add_widget(refresh_button)
        top.add_widget(title)
        layout.add_widget(top)
        layout.add_widget(body)
        
        return layout
if __name__ == '__main__':
    MyApp().run()