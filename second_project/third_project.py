import tkinter as tk
from tkinter import Checkbutton, ttk
from typing import Text
win = tk.Tk()
win.title('this is 3rd project')

# ---------------------  make labels --------------------

first_name_label = ttk.Label(win, text="first name" , padding = 20)
last_name_label = ttk.Label(win, text="last name" , padding = 20)
age_label = ttk.Label(win, text="age" , padding = 20)
gender_label = ttk.Label(win, text="select your gender" , padding = 20)

# ---------------------  make entries --------------------

first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
age_var = tk.IntVar()

first_name_entry = ttk.Entry(win , width=16 , textvariable = first_name_var)
first_name_entry.focus()
last_name_entry = ttk.Entry(win , width=16 , textvariable = last_name_var)
age_entry = ttk.Entry(win , width=16 , textvariable = age_var)

# ----------------------- combobox here-----------------------
gender_combobox = ttk.Combobox(win, width = 14)
gender_combobox['values'] = ('male','female','other')
gender_combobox.current(0)
gender_combobox.grid(row = 3 , column = 1)


# - --------------------- grid or pack here  ---------------------

first_name_label.grid(row=0 , column=0)
last_name_label.grid(row=1 , column=0)
age_label.grid(row=2 , column=0)
gender_label.grid(row = 3 , column = 0)

first_name_entry.grid(row=0 , column=1)
last_name_entry.grid(row=1 , column=1)
age_entry.grid(row=2 , column=1)


# ---------------------- cheackbox --------------------------------

Check_box = ttk.Checkbutton(win, text="if you are agree with term and conditions" , padding = 20)
Check_box.grid(row=4 , column=0)

# =========================== radio button -------------------------
get_radio1 = ttk.Radiobutton(win , text= 'student' , value = 'studemt' , name = '')
get_radio1.grid(row=5 ,column=0)
get_radio2 = ttk.Radiobutton(win , text = 'teacher' , value='teacher' , name = '')
get_radio2.grid(row=5 ,column=1)
# --------------------- submit button here --------------------------

def func():
    pass
submit_btn = ttk.Button(win , text = 'submit', command = func)
submit_btn.grid(row =6 , column=0)








win.mainloop()