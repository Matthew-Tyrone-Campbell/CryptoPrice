from backend import Crypto, get_api_key
from tkinter import *
from PIL import Image, ImageTk

class CryptoWidget(Frame):
    parameters = {
    'highlightthickness':1,
    'highlightcolor':'black',
    'highlightbackground':'black',
    'width':800
    }
    
    def __init__(self,cryptocurrency,master):
        super().__init__(master=master,**CryptoWidget.parameters)
        self.pack(fill=BOTH)
        self.cryptocurrency = cryptocurrency
        y_padding = 10
        x_padding = 40
        resize_dimensions = (200,200)
        font_size = 20
        font_family = 'Times New Roman'

        self.price = DoubleVar()
        self.price_change = DoubleVar()
        self.update_price()

        #crypto image
        self.logo_image = Image.open(f"logos/{self.cryptocurrency.lower()}.png")
        self.logo_image = self.logo_image.resize(resize_dimensions)
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = Label(master=self,image=self.logo_image,padx=x_padding,pady=y_padding,font=(font_family,font_size))
        self.logo_label.grid(row= 0, column= 0)
        
        #crypto name
        self.crypto_name_frame = Frame(self,padx=x_padding)
        self.crypto_name_frame.grid(row=0,column=1)
        self.crypto_name_label = Label(master=self.crypto_name_frame,text=cryptocurrency,pady=y_padding,font=(font_family,font_size))
        self.crypto_name_label.grid(row=0,column=0)

        self.crypto_initials_label = Label(master=self.crypto_name_frame,text=crypto.get_crypto_initials(cryptocurrency),pady=y_padding,font=(font_family,font_size))
        self.crypto_initials_label.grid(row=1, column=0)

        #crypto price
        self.crypto_price_label = Label(master=self,textvariable=self.price,padx=x_padding,font=(font_family,font_size))
        self.crypto_price_label.grid(row=0,column=2)

        #change in crypto price
        self.change_in_price_label = Label(master=self,padx=x_padding,textvariable=self.price_change,font=(font_family,font_size))
        self.change_in_price_label.grid(row=0,column=3)

    def update_price(self):
        self.price.set(f"${crypto.get_crypto_price(self.cryptocurrency)}")
        self.price_change.set(f"{crypto.get_crypto_change(self.cryptocurrency)}%")

class CryptoWidgetsFrame(Frame):
    def __init__(self,master):
        super().__init__(master=master)

    def add_crypto_widgets(self):
        for x in crypto.crypto_data:
            CryptoWidget(master=self,cryptocurrency=x)

class RefreshButton(Button):
    def __init__(self, master, crypto_widgets_frame, refresh_image):
        super().__init__(master=master,image=refresh_image)
        self.crypto_widgets_frame = crypto_widgets_frame
        self.config(command=self.refresh_crypto)

    def refresh_crypto(self):
        crypto.assign_crypto_data()
        for widget in self.crypto_widgets_frame.winfo_children():
            widget.update_price()

window = Tk()
crypto = Crypto(get_api_key())
crypto.assign_crypto_data()

cryptowidgetsframe = CryptoWidgetsFrame(master=window)

refresh_image = Image.open('logos/restart.png')
refresh_image = refresh_image.resize((50,50))
refresh_image = ImageTk.PhotoImage(refresh_image)
refresh_button = RefreshButton(master=window,crypto_widgets_frame=cryptowidgetsframe,refresh_image=refresh_image)

refresh_button.pack()
cryptowidgetsframe.pack()
cryptowidgetsframe.add_crypto_widgets()

window.mainloop()