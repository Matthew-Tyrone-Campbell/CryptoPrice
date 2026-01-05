from backend import Crypto, get_api_key
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
crypto = Crypto(get_api_key())
title = Label(window,text="crypto")
title.pack()

class CryptoWidget(Frame):
    def __init__(self,cryptocurrency,screen,**kwargs):
        super().__init__(screen,**kwargs)
        self.pack()
        self.cryptocurrency = cryptocurrency
        y_padding = 10
        x_padding = 40
        resize_dimensions = (200,200)

        #crypto image
        self.logo_image = Image.open(f"logos/{self.cryptocurrency.lower()}.png")
        self.logo_image = self.logo_image.resize(resize_dimensions)
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = Label(master=self,image=self.logo_image,padx=x_padding)
        self.logo_label.grid(row= 0, column= 0)
        
        #crypto name
        self.crypto_name_frame = Frame(self,padx=x_padding)
        self.crypto_name_frame.grid(row=0,column=1)
        self.crypto_name = Label(master=self.crypto_name_frame,text=cryptocurrency,pady=y_padding)
        self.crypto_name.grid(row=0,column=0)

        self.crypto_initials = Label(master=self.crypto_name_frame,text=crypto.get_crypto_initials(cryptocurrency),pady=y_padding)
        self.crypto_initials.grid(row=1, column=0)

        #crypto price
        self.crypto_price = Label(master=self,text=f"${crypto.get_crypto_price(cryptocurrency)}",padx=x_padding)
        self.crypto_price.grid(row=0,column=2)

        #change in crypto price
        self.change_in_price = Label(master=self,padx=x_padding,text=f"{crypto.get_crypto_change(cryptocurrency)}%")
        self.change_in_price.grid(row=0,column=3)
        
def add_crypto_widgets():
    for x in crypto.crypto_data:
        CryptoWidget(screen=window,cryptocurrency=x)

add_crypto_widgets()
window.mainloop()