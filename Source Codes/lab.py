import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

root = customtkinter.CTk()
root.title('Job Application Tracking System')
root.geometry('1350x590')
root.config(bg='#d3d7f5')
root.resizable(FALSE, FALSE)

font1 = ('Helvetica', 20, 'bold')
font2 = ('Arial', 12, 'bold')


def add_to_treeview():
    applicants = database.fetch_applicants()
    my_tree.delete(*my_tree.get_children())
    for applicant in applicants:
        my_tree.insert('', END, values=applicant)
def clear(*clicked):
    if clicked:
        my_tree.selection_remove(my_tree.focus())
        my_tree.focus('')
    number_entry.delete(0, END)
    name_entry.delete(0, END)
    variable1.set('Male')
    job_title_entry.delete(0, END)
    company_entry.delete(0, END)
    status_entry.set('Pending')
    date_entry.delete(0, END)

def display_data(event):
    picked_item = my_tree.focus()
    if picked_item:
        row = my_tree.item(picked_item)['values']
        clear()
        number_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        variable1.set(row[2])
        job_title_entry.insert(0, row[3])
        company_entry.insert(0, row[4])
        status_entry.set(row[5])
        date_entry.insert(0, row[6])
    else:
        pass

def delete():
    picked_item = my_tree.focus()
    if not picked_item:
        messagebox.showerror('ERROR', 'Select an applicant to delete')
    else:
        number = number_entry.get()
        database.delete_applicant(number)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Data has been deleted')

def update():
    picked_item = my_tree.focus()
    if not picked_item:
        messagebox.showerror('Error', 'Select an applicant to update')
    else:
        number = number_entry.get()
        name = name_entry.get()
        gender = variable1.get()
        job_title = job_title_entry.get()
        company = company_entry.get()
        status = status_entry.get()
        date_applied = date_entry.get()
        database.update_applicant(name, gender, job_title, company, status, date_applied, number)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Data has been updated')

def insert():
    number = number_entry.get()
    name = name_entry.get()
    gender = variable1.get()
    job_title = job_title_entry.get()
    company = company_entry.get()
    status = status_entry.get()
    date_applied = date_entry.get()

    if not (number and name and gender and job_title and company and status and date_applied):
        messagebox.showerror('Error', 'Complete all fields.')
    elif database.number_exists(number):
        messagebox.showerror('Error', 'No. is already exists.')
    else:
        database.insert_applicant(number, name, gender, job_title, company, status, date_applied)
        add_to_treeview()
        messagebox.showinfo('Success', 'Data has been inserted.')

def search():
    search_window = tk.Toplevel(root)
    search_window.title('Search Applicant')
    search_window.geometry('400x200')
    search_window.config(bg='#d3d7f5')

    search_label = customtkinter.CTkLabel(search_window, font=font1, text='Search by No. :', text_color='#000000', bg_color='#d3d7f5')
    search_label.place(x=20, y=50)

    search_entry = customtkinter.CTkEntry(search_window, font=font1, text_color='#000', fg_color='#fff', border_width=1, width=180, border_color='#000')
    search_entry.place(x=200, y=50)

    def perform_search():
        search_term = search_entry.get().strip()
        if search_term:
            if search_term.isdigit():
                applicants = database.fetch_applicants()
                my_tree.delete(*my_tree.get_children())
                found = False
                for applicant in applicants:
                    if search_term == applicant[0]:
                        my_tree.insert('', END, values=applicant)
                        found = True
                if not found:
                    messagebox.showinfo('Search Result', 'There are no applicants registered with the entered No.')
                search_window.destroy()
            else:
                messagebox.showerror('Invalid Entry', 'Please enter a valid No.')
        else:
            messagebox.showerror('Invalid Entry', 'Please enter an No. to search.')

    search_button = customtkinter.CTkButton(search_window, command=perform_search, font=font1, text_color='#fff', text='Search', fg_color='#104ec9', hover_color='#0b3280', bg_color='#d3d7f5', cursor='hand2', corner_radius=15, width=150)
    search_button.place(x=125, y=120)

#Data List
number_label = customtkinter.CTkLabel(root, font=font1, text='APPLICATION No. ', text_color='#000000', bg_color='#d3d7f5')
number_label.place(x=20, y=60)

number_entry = customtkinter.CTkEntry(root, font=font1, text_color='#000', fg_color='#fff', border_width=1, width=180, border_color='#000', placeholder_text='4 DIGITS', placeholder_text_color='#a3a3a3')
number_entry.place(x=220, y=60)

name_label = customtkinter.CTkLabel(root, font=font1, text='NAME:', text_color='#000000', bg_color='#d3d7f5')
name_label.place(x=20, y=110)

name_entry = customtkinter.CTkEntry(root, font=font1, text_color='#000', fg_color='#fff', border_width=1, width=180, border_color='#000')
name_entry.place(x=220, y=110)

gender_label = customtkinter.CTkLabel(root, font=font1, text='GENDER:', text_color='#000000', bg_color='#d3d7f5')
gender_label.place(x=20, y=160)

options = ['Male', 'Female', 'Others']
variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(root, font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#c8d0ff', button_hover_color='#fff', width=180, variable=variable1, values=options, state='readonly', border_color='#000', border_width=1)
gender_options.set('Male')
gender_options.place(x=220, y=160)

job_title_label = customtkinter.CTkLabel(root, font=font1, text='JOB TITLE:', text_color='#000000', bg_color='#d3d7f5')
job_title_label.place(x=20, y=210)

job_title_entry = customtkinter.CTkEntry(root, font=font1, text_color='#000', fg_color='#fff', border_width=1, width=180, border_color='#000')
job_title_entry.place(x=220, y=210)

company_label = customtkinter.CTkLabel(root, font=font1, text='COMPANY:', text_color='#000000', bg_color='#d3d7f5')
company_label.place(x=20, y=260)

company_entry = customtkinter.CTkEntry(root, font=font1, text_color='#000', fg_color='#fff', border_width=1, width=180, border_color='#000')
company_entry.place(x=220, y=260)

status_label = customtkinter.CTkLabel(root, font=font1, text='STATUS:', text_color='#000000', bg_color='#d3d7f5')
status_label.place(x=20, y=310)

status_options = ['Pending', 'Interviewed', 'Accepted', 'Rejected']
status_entry = StringVar()

status_combobox = customtkinter.CTkComboBox(root, font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#c8d0ff', button_hover_color='#fff', width=180, variable=status_entry, values=status_options, state='readonly', border_color='#000', border_width=1)
status_combobox.set('Pending')
status_combobox.place(x=220, y=310)

date_label = customtkinter.CTkLabel(root, font=font1, text='DATE APPLIED:', text_color='#000000', bg_color='#d3d7f5')
date_label.place(x=20, y=360)

date_entry = customtkinter.CTkEntry(root, font=font1, text_color='#000', fg_color='#fff', border_width=1, width=180, border_color='#000', placeholder_text='MM-DD-YYYY', placeholder_text_color='#a3a3a3')
date_entry.place(x=220, y=360)

saved_button = customtkinter.CTkButton(root, command=insert, font=(font1, 20, 'bold'), text_color='#fff', text='Save Applicant', fg_color='#104ec9', hover_color='#0b3280', bg_color='#d3d7f5', cursor='hand2', corner_radius=20, width=380)
saved_button.place(x=20, y=410)

update_button = customtkinter.CTkButton(root, command=update, font=(font1, 20, 'bold'), text_color='#fff', text='Update Applicant', fg_color='#05A312', hover_color='#00850B', bg_color='#d3d7f5', cursor='hand2', corner_radius=20, width=380)
update_button.place(x=20, y=445)

search_button = customtkinter.CTkButton(root, command=search, font=(font1, 18, 'bold'), text_color='#fff', text='Search Applicant', fg_color='#FFA500', hover_color='#FF8C00', bg_color='#d3d7f5', cursor='hand2', corner_radius=15, width=275)
search_button.place(x=445, y=500)

clear_button = customtkinter.CTkButton(root, command=lambda: clear(True), font=(font1, 18, 'bold'), text_color='#fff', text='Add New Applicant', fg_color='#3498DB', hover_color='#428bca', bg_color='#d3d7f5', cursor='hand2', corner_radius=15, width=275)
clear_button.place(x=730, y=500)

delete_button = customtkinter.CTkButton(root, command=delete, font=(font1, 18, 'bold'), text_color='#fff', text='Delete Applicant', fg_color='#E40404', hover_color='#AE0000', bg_color='#d3d7f5', cursor='hand2', corner_radius=15, width=275)
delete_button.place(x=1020, y=500)


style = ttk.Style(root)

style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#000000', background='#ffffff', fieldbackground='#ffffff')
style.map('Treeview', background=[('selected', '#d3d7f5')])

my_tree = ttk.Treeview(root, height=20)

my_tree['columns'] = ('No.', 'Name', 'Gender', 'Job Title', 'Company', 'Status', 'Date Applied')

my_tree.column('#0', width=0, stretch=tk.NO)
my_tree.column('No.', anchor=tk.CENTER, width=100)
my_tree.column('Name', anchor=tk.CENTER, width=150)
my_tree.column('Gender', anchor=tk.CENTER, width=100)
my_tree.column('Job Title', anchor=tk.CENTER, width=150)
my_tree.column('Company', anchor=tk.CENTER, width=150)
my_tree.column('Status', anchor=tk.CENTER, width=100)
my_tree.column('Date Applied', anchor=tk.CENTER, width=120)

my_tree.heading('No.', text='No.')
my_tree.heading('Name', text='Name')
my_tree.heading('Gender', text='Gender')
my_tree.heading('Job Title', text='Job Title')
my_tree.heading('Company', text='Company')
my_tree.heading('Status', text='Status')
my_tree.heading('Date Applied', text='Date Applied')

my_tree.place(x=430, y=50)

add_to_treeview()

my_tree.bind('<ButtonRelease>', display_data)

root.mainloop()

