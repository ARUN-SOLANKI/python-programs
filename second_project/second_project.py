import tkinter as tk 
from tkinter import mainloop, ttk
from typing import Text

# import tkinter 
# from tkinter import * 

win = tk.Tk()
win.title('this is arun solanki')

# --------- create labels ----------------
# ttk.Label(win , text='enter first name').pack()
first_name_label  = ttk.Label(win , text='enter first name') 
first_name_label.grid(row=0 , column=0 , sticky=tk.W)

last_name_label = ttk.Label(win , text="enter last name")
last_name_label.grid(row=1 , column=0 , sticky=tk.W)

email_label = ttk.Label(win, text="enter email address")
email_label.grid(row=2 , column=0 , sticky=tk.W)

age_label = ttk.Label(win, text="enter your age")
age_label.grid(row=3 , column=0 , sticky=tk.W)

gender_label = ttk.Label(win , text = "select your gender")
gender_label.grid(row=4 , column=0)

#  ------------ create entry box ------
first_name_var = tk.StringVar()
first_name_entrybox = ttk.Entry(win , width=16 , textvariable=first_name_var)
first_name_entrybox.grid(row=0 , column=1)
first_name_entrybox.focus()

last_name_var = tk.StringVar()
last_name_entrybox = ttk.Entry(win , width=16 , textvariable=last_name_var)
last_name_entrybox.grid(row=1 , column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win , width=16 , textvariable=email_var)
email_entrybox.grid(row=2 , column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win , width=16 , textvariable=age_var)
age_entrybox.grid(row=3 , column=1)

# --------------- create combobox - ------------------------
gendrer_var = tk.StringVar()
gender_combobox  = ttk.Combobox(win, width=14 , textvariable=gendrer_var , state='readonly')
gender_combobox['values'] = ('male' , 'female' , 'other')
gender_combobox.current(0)
gender_combobox.grid(row=4 , column=1)


# ------------- create button ----------------
# def action():
#     first_name = first_name_var.get()
#     last_name = last_name_var.get()
#     email = email_var.get()
#     age = age_var.get()
#     print(f'{first_name},{last_name},{email},{age}')

# submit_button = ttk.Button(win, text='submit' , command = action)
# submit_button.grid(row=5 , column=0)

win.mainloop()