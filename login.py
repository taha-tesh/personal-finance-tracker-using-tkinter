import tkinter
from customtkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from MyApp import App


window = tkinter.Tk()
window.title("Login form") 
window.geometry('350x600')
window.configure(bg='black') 

def login():

    user_name_entred = username_entry.get()
    password_entred = password_entry.get()

    conn = sqlite3.connect('data.db')
    select_data_query = '''SELECT * FROM users WHERE user_name = ?'''
    select_data_tupele = (user_name_entred,)
    cursor = conn.cursor()
    cursor.execute(select_data_query, select_data_tupele)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    # print(data[0][0])
    # print(data[0][1])
    
    for ptr in data:
        if str(ptr[0]) == user_name_entred:
            if password_entred == str(ptr[1]):
                window.destroy()
                app = App(user_name_entred)
                app.open_main_app()
                return
                
    messagebox.showerror(title="Error", message="User name or password is wrong or user doesn't exist.")   # badal message ta3 print


def sign_up():
    user_name_entred = username_entry.get()
    password_entred = password_entry.get()

    if (user_name_entred) and (password_entred): 
        conn = sqlite3.connect('data.db')
        create_table_query = '''CREATE TABLE IF NOT EXISTS users (user_name VARCHAR(10), password INT)'''
        conn.execute(create_table_query)

        data_insert_query = '''INSERT INTO users VALUES (?, ?)'''
        data_insert_tupele = (user_name_entred, password_entred)

        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tupele)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror(title="Error", message="Pleas fill the recuired feilds.")   # badal message ta3 print

    
frame = tkinter.Frame(bg='black')  # hada couleur tani badlah kima drt fi line 8


login_label = tkinter.Label(frame, text="", bg='black', fg="dark blue", font=("PoetsenOne", 30))
image_path = "./images/welcome.png"
image = Image.open(image_path) 
image = image.resize((200, 100))
photo = ImageTk.PhotoImage(image) 

CTkLabel(master=login_label, image=photo).pack(expand=True)

text_label = tkinter.Label(frame, text="use this form to login \nif don't have an acount \nyou can use the same form to sign up",
                             bg='black', fg="white", font=("PoetsenOne", 11))
username_label = tkinter.Label(frame, text="Username", bg='black', fg="#FFFFFF", font=("PoetsenOne", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='black', fg="#FFFFFF", font=("PoetsenOne", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="dark blue", fg="white", font=("PoetsenOne", 16), command=login)

signup_button = tkinter.Button(
    frame, text="Sign Up", bg="dark blue", fg="white", font=("PoetsenOne", 16), command=sign_up)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
text_label.grid(row=1, column=0, columnspan=2, sticky="news", pady=20)
username_label.grid(row=2, column=0)
username_entry.grid(row=3, column=0, pady=20)
password_label.grid(row=4, column=0)
password_entry.grid(row=5, column=0, pady=20)
login_button.grid(row=6, column=0, columnspan=1, pady=10, ipadx=50)
signup_button.grid(row=7, column=0, pady=20, ipadx=40)

frame.pack()

window.mainloop()