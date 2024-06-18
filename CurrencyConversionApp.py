from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from forex_python.converter import CurrencyRates

class CurrencyConvertor:

    def OpenCurrencyConvertor(self):

        app = CTk(fg_color="white")
        app.geometry("350x650")
        app.title("Currency Convertor")

        def Covert():

            from_currency = currensy_1.get()
            to_currency = currensy_2.get()
            Amount = amount.get()

            if (from_currency == "TL") and (to_currency == "USD"):
                Amount = float(Amount) / 32
                ResultLabel.configure(text= "  " + str(Amount) + " USD")
            elif (from_currency == "TL") and (to_currency == "Euro"):
                Amount = float(Amount) / 35
                ResultLabel.configure(text= "  " + str(Amount) + " Euro")
            elif (to_currency == "TL") and (from_currency == "USD"):
                Amount = float(Amount) * 32
                ResultLabel.configure(text= "  " + str(Amount) + " TL")
            elif (to_currency == "TL") and (from_currency == "Euro"):
                Amount = float(Amount) * 35
                ResultLabel.configure(text= "  " + str(Amount) + " TL")
            elif (to_currency == "Euro") and (from_currency == "USD"):
                Amount = float(Amount) * 1.09
                ResultLabel.configure(text= "  " + str(Amount) + " Euro")
            elif (to_currency == "USD") and (from_currency == "Euro"):
                Amount = float(Amount) / 1.09
                ResultLabel.configure(text= "  " + str(Amount) + " USD")
            else:
                ResultLabel.configure(text= "  " + str(Amount) + " " + to_currency)

        def ChangeButton():

            temp = currensy_1.get()
            currensy_1.set(currensy_2.get())
            currensy_2.set(temp)

        frame_top = CTkFrame(master=app, fg_color="white", width=10, height=15, corner_radius=0)
        frame_top.pack(side=TOP, expand=False, fill=X)

        frame_right = CTkFrame(master=app, fg_color="white", width=20, corner_radius=0)
        frame_right.pack(side=RIGHT, expand=False, fill=Y)

        frame_left = CTkFrame(master=app, fg_color="white", width=20, corner_radius=0)
        frame_left.pack(side=LEFT, expand=False, fill=Y)

        mainlabel = CTkLabel(master=app, text="Currency Convertor", font=CTkFont(family='PoetsenOne', size=30), text_color="dark blue")
        mainlabel.pack(side=TOP, fill=BOTH, expand=False)

        space = CTkFrame(master=app, fg_color="white", height=60, corner_radius=0)
        space.pack(side=TOP, fill=X, expand=False)

        mainframe = CTkFrame(master=app, fg_color="white", corner_radius=10, height=300)
        mainframe.pack(side=TOP, expand=False, fill=BOTH)
    
        currensy_1 = CTkOptionMenu(master=mainframe, width=400, height=35, state="readonly", values=["TL", "USD", "Euro"], fg_color="#EBEBEB", button_color="#EBEBEB", text_color="gray")
        currensy_1.pack(expand=True, pady=20, padx=40)
        currensy_1.set("From Currency")

        image = CTkImage(Image.open("./images/change.png"), size=(25, 25))
        

        change_button = CTkButton(master=mainframe,
                        text="", 
                        image=image, 
                        fg_color="#EBEBEB", 
                        corner_radius=5, 
                        width=30,
                        height=30,
                        hover=False,
                        command=ChangeButton)
        change_button.pack(side=TOP, expand=False, pady=10, padx=20)

        currensy_2 = CTkOptionMenu(master=mainframe, width=300, height=35, state="readonly", values=["TL", "USD", "Euro"], fg_color="#EBEBEB", button_color="#EBEBEB", text_color="gray")
        currensy_2.pack(expand=True, pady=20, padx=40)
        currensy_2.set("To Currency")

        space = CTkFrame(master=mainframe, fg_color="white", height=40, corner_radius=0)
        space.pack(side=TOP, fill=X, expand=False)

        amount = CTkEntry(master=mainframe, placeholder_text="Amount", width=235, height=35, fg_color="#EBEBEB", border_color="#EBEBEB", text_color="black")
        amount.pack(expand=True, pady=15, padx=20)

        space = CTkFrame(master=mainframe, fg_color="white", height=40, corner_radius=0)
        space.pack(side=TOP, fill=X, expand=False)

        convert_button = CTkButton(master=mainframe,
                        text="Convert",
                        font= CTkFont(family='PoetsenOne', size=20), 
                        fg_color="#6FBF4A", 
                        corner_radius=15, 
                        width=240,
                        height=50,
                        hover=False,
                        command=Covert)
        convert_button.pack(side=TOP, expand=False, pady=10, padx=20)

        space = CTkFrame(master=mainframe, fg_color="white", height=30, corner_radius=0)
        space.pack(side=TOP, fill=X, expand=False)

        ResultFrame = CTkFrame(master=app, width=235, height=60, fg_color="#EBEBEB", corner_radius=10)
        ResultFrame.pack(side=TOP, expand=False, ipadx= 110, ipady= 5)

        ResultLabel = CTkLabel(master=ResultFrame, text=" ", font=CTkFont(family='PoetsenOne', size=20), text_color="black")
        ResultLabel.pack(side=TOP,  expand=False)

        app.mainloop()


# CurrencyConvertor_1 = CurrencyConvertor()
# CurrencyConvertor_1.OpenCurrencyConvertor()