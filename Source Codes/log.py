import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

window = customtkinter.CTk()
window.title('user log in')
window.geometry('500x400')
window.config(bg='#dbe7ff')
window.resizable(FALSE, FALSE)

conn = sqlite3.connect('log_in_window.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')
def log_in():
    username = user_username_entry.get()
    password = user_password_entry.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Success', 'Login successful')
                window.quit()
            else:
                messagebox.showerror('Error', 'Incorrect password')
        else:
            messagebox.showerror('Error', 'Incorrect username')
    else:
        messagebox.showerror('Error', 'Input all data!')

def display_log_in():
    user_sign_up_frame.pack_forget()
    user_log_in_frame.pack(fill='both', expand=True)

def sign_up():
    username = user_username_entry2.get()
    password = user_password_entry2.get()
    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username is already taken')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username, hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Account successfully created.')
            display_log_in()
    else:
        messagebox.showerror('Error', 'Input all data!')

def display_sign_up():
    user_log_in_frame.pack_forget()
    user_sign_up_frame.pack(fill='both', expand=True)

#1st window for log in
user_log_in_frame = customtkinter.CTkFrame(window, bg_color='#dbe7ff', fg_color='#dbe7ff', width=600, height=450)
user_log_in_frame.place(x=0, y=0)

user_log_in_label = customtkinter.CTkLabel(user_log_in_frame, font=("Arial",50,"bold"), text='Log In', text_color='#0923e8', bg_color='#dbe7ff')
user_log_in_label.place(x=160, y=45)

user_username_entry = customtkinter.CTkEntry(user_log_in_frame, font=("Arial",18), text_color='#000', fg_color='#fff', border_width=1, height=40,width=355, border_color='#aaacbd',placeholder_text='Username', placeholder_text_color='#b1b2b5')
user_username_entry.place(x=70, y=130)

user_password_entry = customtkinter.CTkEntry(user_log_in_frame, font=("Arial",18), show="•", text_color='#000', fg_color='#fff', border_width=1, height=40,width=355, border_color='#aaacbd',placeholder_text='Password', placeholder_text_color='#b1b2b5')
user_password_entry.place(x=70, y=185)

user_log_in_button = customtkinter.CTkButton(user_log_in_frame, command=log_in, font=("Arial",18), text_color='#fff', text='Log In', fg_color='#0c43b0', hover_color='#4375d9', bg_color='#dbe7ff', cursor='hand2', corner_radius=20, width=345, height=35)
user_log_in_button.place(x=75, y=240)

sign_up_phrase = customtkinter.CTkLabel(user_log_in_frame, font=("Arial",15), text='Don\'t have an account?', text_color='#01060f', bg_color='#dbe7ff')
sign_up_phrase.place(x=120, y=330)

sign_up_switch = customtkinter.CTkButton(user_log_in_frame, command=display_sign_up, font=("Arial",13,"underline"), text='Sign up', text_color='#01060f', bg_color='#dbe7ff', width=10)
sign_up_switch.place(x=280, y=330)


#2nd window for sign up
user_sign_up_frame = customtkinter.CTkFrame(window, bg_color='#dbe7ff', fg_color='#dbe7ff', width=470, height=360)

user_sign_up_label = customtkinter.CTkLabel(user_sign_up_frame, font=("Arial",50,"bold"), text='Sign Up', text_color='#0923e8', bg_color='#dbe7ff')
user_sign_up_label.place(x=155, y=45)

user_username_entry2 = customtkinter.CTkEntry(user_sign_up_frame, font=("Arial",18), text_color='#000', fg_color='#fff', border_width=1, height=40,width=355, border_color='#aaacbd',placeholder_text='Username', placeholder_text_color='#b1b2b5')
user_username_entry2.place(x=70, y=130)

user_password_entry2 = customtkinter.CTkEntry(user_sign_up_frame, font=("Arial",18), show="•", text_color='#000', fg_color='#fff', border_width=1, height=40,width=355, border_color='#aaacbd',placeholder_text='Password', placeholder_text_color='#b1b2b5')
user_password_entry2.place(x=70, y=185)

user_sign_up_button = customtkinter.CTkButton(user_sign_up_frame, command=sign_up, font=("Arial",18), text_color='#fff', text='Sign Up', fg_color='#0c43b0', hover_color='#4375d9', bg_color='#dbe7ff', cursor='hand2', corner_radius=20, width=345, height=35)
user_sign_up_button.place(x=75, y=240)

log_in_phrase = customtkinter.CTkLabel(user_sign_up_frame, font=("Arial",15), text='Already have an account?', text_color='#01060f', bg_color='#dbe7ff')
log_in_phrase.place(x=120, y=330)

log_in_switch = customtkinter.CTkButton(user_sign_up_frame, command=display_log_in, font=("Arial",13,"underline"), text='Log in', text_color='#01060f', bg_color='#dbe7ff', width=10)
log_in_switch.place(x=295, y=330)

window.mainloop()
