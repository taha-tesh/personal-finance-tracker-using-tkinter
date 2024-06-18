from customtkinter import *
import tkinter as tk
from PIL import Image
from backend import *
from data_analysis import *
from CurrencyConversionApp import *
from datetime import date
import csv
# import ui

class App:

    def __init__(self, user_name):
        self.use_name = user_name
        
    def open_main_app(self):

        app = CTk(fg_color="black")
        app.geometry("350x650")
        app.title("Personal Finance Traker")
        app.iconbitmap("./images/icon.png")

        main_color = "black"
        font = CTkFont(family='PoetsenOne', size=30)
        median_font = CTkFont(family='PoetsenOne', size=25)
        small_font = CTkFont(family='PoetsenOne', size=18)
        data_file_path = "data.csv"

        def AddButton():
            #add_form.pack(side=BOTTOM, fill=X, expand=False, anchor="center")
            for y in range(-31, -21, 1):
                add_form.update()
                add_form.place(relx=0.5, rely=0.1, y=y**2, anchor="center", relwidth=0.85)

        def CancelButton():
            for y in range(21, 31, 1):
                add_form.update()
                add_form.place(relx=0.5, y=y**2, anchor="center")
            
            # clear the content of the form
            description.delete(0, END)
            amount.delete(0, END)
            catigory.set("Select type...")

        def SubmitButton():
            enterd_description = description.get()
            entred_amount = amount.get()
            entred_catigory = catigory.get()

            # sava date to the csv file
            data = [[self.use_name, enterd_description, entred_amount, entred_catigory, date.today()]]
            with open(data_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)

            #print the data to consol
            print("User Name: ", self.use_name)
            print("Description: ", enterd_description)
            print("Amount: ", entred_amount)
            print('Type: ', entred_catigory)

            db = IncertData(self.use_name, enterd_description, entred_amount, entred_catigory)
            db.SubmitData()

            Calculate_Balance()
            Get_Income()
            Get_Expenses()

            # clear the content of the form
            description.delete(0, END)
            amount.delete(0, END)
            catigory.set("Select type...")

        def SettingsButton():
            Convert_Currency = CurrencyConvertor()
            Convert_Currency.OpenCurrencyConvertor()


        Button = CTkButton(master=app, 
                        text="+", 
                        fg_color="blue", 
                        corner_radius=50, 
                        width=30,
                        height=30,
                        hover=False,
                        command=AddButton)

        Button.pack(side=BOTTOM, expand=False, pady=20, ipady=10, ipadx=10)

        # View numbers section 
        frame_top = CTkFrame(master=app, fg_color=main_color, width=10, corner_radius=0)
        frame_top.pack(side=TOP, expand=False, fill=X)

        frame_right = CTkFrame(master=app, fg_color=main_color, width=20, corner_radius=0)
        frame_right.pack(side=RIGHT, expand=False, fill=Y)

        frame_left = CTkFrame(master=app, fg_color=main_color, width=20, corner_radius=0)
        frame_left.pack(side=LEFT, expand=False, fill=Y)

        nameframe = CTkFrame(master=frame_top, fg_color=main_color)
        nameframe.pack(side=LEFT, expand=False, fill=X, pady=10)

        name_label = CTkLabel(master=nameframe, text="    Hi, " + self.use_name + "👋", font=font)
        name_label.pack(side=LEFT, fill=BOTH, expand=False)

        image = CTkImage(Image.open("./images/CurrencyConvertor.png"))

        setting_Button = CTkButton(master=frame_top,
                        text="", 
                        image=image, 
                        fg_color="blue", 
                        corner_radius=5, 
                        width=30,
                        height=30,
                        hover=False,
                        command=SettingsButton)
        setting_Button.pack(side=RIGHT, expand=False, fill=X, pady=10, padx=20)

        space = CTkFrame(master=app, fg_color=main_color, height=10, corner_radius=0)
        space.pack(side=TOP, fill=X, expand=False)

        info_frame = CTkFrame(master=app, fg_color="blue")
        info_frame.pack(side=TOP, fill=BOTH, expand=False)

        space = CTkFrame(master=info_frame, fg_color="blue", height=20)
        space.pack(side=TOP, fill=X, expand=False, pady=3, padx=3)

        balance_frame = CTkFrame(master=info_frame, height=60, width=60, fg_color="blue")
        balance_frame.pack(side=TOP, fill=X, expand=False, padx=10)
        balance_label = CTkLabel(master=balance_frame, text="BALANCE", text_color="white", font=("",15))
        balance_label.pack(side=LEFT, padx=10)

        balance_frame = CTkFrame(master=info_frame, height=60, width=60, fg_color="blue")
        balance_frame.pack(side=TOP, fill=X, expand=False, padx=10)
        balance = CTkLabel(master=balance_frame, text="$1,234.56", text_color="white", font=median_font)
        balance.pack(side=LEFT, padx=10)

        space = CTkFrame(master=info_frame, fg_color="blue", height=20)
        space.pack(side=TOP, fill=X, expand=False, pady=3, padx=3)

        income_frame = CTkFrame(master=info_frame, height=60, width=60, fg_color="blue")
        income_frame.pack(side=TOP, fill=X, expand=False, padx=10)
        income_label = CTkLabel(master=income_frame, text="INCOME", text_color="white", font=("",12))
        income_label.pack(side=LEFT, padx=10)

        income_frame_v = CTkFrame(master=info_frame, height=60, width=60, fg_color="blue")
        income_frame_v.pack(side=TOP, fill=X, expand=False, padx=10)
        income = CTkLabel(master=income_frame_v, text="+$234.56", text_color="white", font=small_font)
        income.pack(side=LEFT, padx=10)

        out_frame = CTkFrame(master=income_frame, height=60, width=0, fg_color="blue")
        out_frame.pack(side=TOP, fill=X, expand=False, padx=5)
        expenses_label = CTkLabel(master=out_frame, text="     EXPENSES", text_color="white", font=("",12))
        expenses_label.pack(side=TOP, padx=10)

        out_frame = CTkFrame(master=income_frame_v, height=60, width=0, fg_color="blue")
        out_frame.pack(side=TOP, fill=X, expand=False, padx=1)
        expenses = CTkLabel(master=out_frame, text="-$678", text_color="white", font=small_font)
        expenses.pack(side=TOP, padx=1)

        space = CTkFrame(master=info_frame, fg_color="blue", height=10)
        space.pack(side=TOP, fill=X, expand=False, pady=3, padx=3)

        space = CTkFrame(master=app, fg_color=main_color, height=10)
        space.pack(side=TOP, fill=X, expand=False, pady=3, padx=3)

        # analysis section
        button_frame = CTkFrame(master=app, fg_color=main_color)
        button_frame.pack(side=TOP, fill=X, expand=False)

        button_top = CTkFrame(master=button_frame, fg_color="dark blue", height=50)
        button_top.pack(side=TOP, fill=X, expand=False)

        expenses_label = CTkLabel(master=button_top, text="Incomes", text_color="dark blue", font=("PoetsenOne",12), bg_color=main_color, fg_color=main_color)
        expenses_label.pack(side=LEFT,fill=BOTH, expand=True)

        transactions_label = CTkLabel(master=button_top, text="Expenses", font=("PoetsenOne",12), bg_color=main_color, fg_color=main_color)
        transactions_label.pack(side=RIGHT,fill=BOTH, expand=True)

        line_frame = CTkFrame(master=button_frame, fg_color=main_color, height=20)
        line_frame.pack(side=TOP, fill=X, expand=False)

        in_frame = CTkFrame(master=line_frame, fg_color=main_color, width=0, height=20)
        in_frame.pack(side=LEFT, fill=X, expand=True)

        expenses_line = CTkFrame(master=in_frame, fg_color="dark blue", height=2, width=0)
        expenses_line.pack(side=LEFT, fill=X, expand=True, pady=10)

        in_frame1 = CTkFrame(master=line_frame, fg_color=main_color, width=0, height=20)
        in_frame1.pack(side=RIGHT, fill=X, expand=True)

        transactions_line = CTkFrame(master=in_frame1, fg_color="#bbbbbb", width=0, height=2)
        transactions_line.pack(side=LEFT, fill=X, expand=True, pady=10)

        balance_plot_frame = CTkFrame(master=app, fg_color=main_color)
        balance_plot_frame.pack(side=TOP, fill=BOTH, expand=False)

        Data_Analysis = DataAnalysis()
        Data_Analysis.Show_Balance(balance_plot_frame, self.use_name)

        income_plot_frame = CTkFrame(master=app, fg_color=main_color)

        expenses_plot_frame = CTkFrame(master=app, fg_color=main_color)
        


        #Add form
        add_form = CTkFrame(master=app, fg_color="dark blue", corner_radius=10)

        botton_space = CTkFrame(master=add_form, fg_color="dark blue", height=50)
        botton_space.pack(side=BOTTOM, expand=False)

        button_frame_form = CTkFrame(master=add_form, fg_color="dark blue", corner_radius=10)
        button_frame_form.pack(side=BOTTOM, fill=X, expand=False)

        left_space = CTkFrame(master=button_frame_form, fg_color="dark blue", width=43, height=20)
        left_space.pack(side=LEFT, expand=False)

        left_space = CTkFrame(master=button_frame_form, fg_color="dark blue", width=43, height=20)
        left_space.pack(side=RIGHT, expand=False)

        Add_Button = CTkButton(master=button_frame_form, 
                        text="Add", 
                        fg_color="#000064", 
                        corner_radius=50, 
                        width=30,
                        height=30,
                        hover=False,
                        command=SubmitButton
                        )
        Add_Button.pack(side=LEFT, expand=False, pady=15, ipadx=30)

        cancel_Button = CTkButton(master=button_frame_form, 
                        text="Cancel", 
                        fg_color="#000064", 
                        corner_radius=50, 
                        width=30,
                        height=30,
                        hover=False,
                        command=CancelButton
                        )
        cancel_Button.pack(side=RIGHT, expand=False, pady=15, ipadx=20)

        description = CTkEntry(master=add_form, placeholder_text="Description", width=300, fg_color="#000064")
        description.pack(expand=True, pady=15, padx=20)

        amount = CTkEntry(master=add_form, placeholder_text="Amount", width=300, fg_color="#000064")
        amount.pack(expand=True, pady=10, padx=20)

        catigory = CTkOptionMenu(master=add_form, width=300, state="readonly", values=["Income", "Expensis"], fg_color="#000064", button_color="#000078")
        catigory.pack(expand=True, pady=10, padx=40)
        catigory.set("Select type...")

        def KeyBindings():
            transactions_label.bind("<Button-1>", lambda e: MoveRight(e))
            expenses_label.bind("<Button-1>", lambda e: MoveLeft(e))

        def MoveLeft(e):
            transactions_line.configure(fg_color="#bbbbbb")
            transactions_label.configure(text_color="#bbbbbb")
            expenses_line.configure(fg_color="dark blue")
            expenses_label.configure(text_color="dark blue")

            balance_plot_frame.pack_forget()
            expenses_plot_frame.pack_forget()
            income_plot_frame.pack(side=TOP, fill=BOTH, expand=False)
            DataAnalysis.Income_analyze(income_plot_frame, self.use_name)

        def MoveRight(e):
            transactions_line.configure(fg_color="dark blue")
            transactions_label.configure(text_color="dark blue")
            expenses_line.configure(fg_color="#bbbbbb")
            expenses_label.configure(text_color="#bbbbbb")
            
            balance_plot_frame.pack_forget()
            income_plot_frame.pack_forget()
            expenses_plot_frame.pack(side=TOP, fill=BOTH, expand=False)
            DataAnalysis.Expenses_analyze(expenses_plot_frame, self.use_name)

        KeyBindings()

        def Calculate_Balance():

            db = Balance(self.use_name, 0)

            calculated_balance = db.CalculatBalace()

            balance.configure(text="$" + str(calculated_balance))

            # sava the balance to the csv file
            data = [[self.use_name, calculated_balance, date.today()]]
            with open("balance.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)

        Calculate_Balance()

        def Get_Income():

            db = CalculateTotal(self.use_name, "Income")

            total = db.Calculate()

            income.configure(text="+$" + str(total))

        Get_Income()

        def Get_Expenses():

            db = CalculateTotal(self.use_name, "Expensis")

            total = db.Calculate()

            expenses.configure(text="-$" + str(total))

        Get_Expenses()

        def on_closing(): 
           
            app.withdraw()
            app.quit()

        
        app.protocol("WM_DELETE_WINDOW", on_closing)

        app.mainloop()

# app = App("taha")
# app.open_main_app()
