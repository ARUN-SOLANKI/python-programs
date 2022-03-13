import tkinter as tk
from tkinter import Grid, Scrollbar, ttk
from tkinter import font , colorchooser , filedialog , messagebox
import os
from tkinter.constants import LEFT, WORD

main_app = tk.Tk()
main_app.geometry('1200x800')
main_app.title('A.S Pad editor')

# ---------------------------------------- main manu- - - - - - - - - - - - - - -    --
main_manu = tk.Menu()

#  adding of image icons to sub menu bars
#  file icons 
new_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/new.png')
open_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/open.png')
save_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/save.png')
save_as_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/save_as.png')
exit_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/exit.png')

#  edit icons -------

copy_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/copy.png')
paste_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/paste.png')
cut_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/clear_all.png')
find_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/find.png')

#  toolbar icons -------

tool_bar_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/status_bar.png')

# color theme icons -----------
light_default_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/dark.png')
red_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/red.png')
monokai_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/night_blue.png')


# ------------------- menu items -----------------------------------------------------------------

file = tk.Menu(main_manu , tearoff=False)
edit = tk.Menu(main_manu , tearoff=False)
view = tk.Menu(main_manu , tearoff=False)

color_theme  =tk.Menu(main_manu , tearoff=False)
theme_choice = tk.StringVar()
color_icon = (light_default_icon , light_plus_icon , dark_icon , red_icon , monokai_icon , night_blue_icon)
color_dict = {
        'light default' : ('#000000' , '#ffffff'),
        'light plus' : ('#474747' , '#e0e0e0'),
        'dark' : ('#c4c4c4' , '#2d2d2d'),
        'red' : ('#2d2d2d' , '#ffe8e8'),
        'monokai' : ('#d3b774' , '#474747'),
        'night blue' : ('#ededed' , '#6b9dc2')

}

#  cascade main menu file,view,edit,color_theme
main_manu.add_cascade(label='file' , menu = file)
main_manu.add_cascade(label='edit' , menu = edit)
main_manu.add_cascade(label='view' , menu = view)
main_manu.add_cascade(label='color' , menu = color_theme)


# ------------------------------------- end main menu -----------------------------


# ---------------------------------------- tool bar- - - - - - - - - - - - - - -    --
tool_bar = ttk.Label(main_app)
tool_bar.pack(side=tk.TOP , fill=tk.X)



# font families

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable = font_family ,  state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0)


#  font size 
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=16, state='readonly' , textvariable=size_var)
font_size['values'] = tuple(range(0,81))
font_size.current(10)
font_size.grid(row=0 , column=1)

#  bold buttons
bold_icon = tk.PhotoImage(file = 'C:/Users/other/Desktop/first_application/icons2/bold.png')
bold_btn = ttk.Button(tool_bar , image=bold_icon)
bold_btn.grid(row=0 , column=2 ,  padx=5)


#  itelic button
italic_icon = tk.PhotoImage(file = 'C:/Users/other/Desktop/first_application/icons2/italic.png')
italic_btn = ttk.Button(tool_bar , image=italic_icon)
italic_btn.grid(row=0 , column=3 , padx=5)

#  underline button
underline_icon = tk.PhotoImage(file = 'C:/Users/other/Desktop/first_application/icons2/underline.png')
underline_btn = ttk.Button(tool_bar , image=underline_icon)
underline_btn.grid(row=0 , column=4 , padx=5)

# font color
font_color_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar , image=font_color_icon)
font_color_btn.grid(row=0 ,column=6 , padx=5)


# alingn left
align_left_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar , image=align_left_icon)
align_left_btn.grid(row=0 , column=7 , padx= 5)

# align center
align_center_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar , image=align_center_icon)
align_center_btn.grid(row=0 , column=8 , padx= 5)

# align right
align_right_icon = tk.PhotoImage(file='C:/Users/other/Desktop/first_application/icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar , image=align_right_icon)
align_right_btn.grid(row=0 , column=9 , padx= 5)

# ------------------------------------- end tool bar -----------------------------

# -------------------------------- text edittor ---------------------------------------
text_editor = tk.Text(main_app)
text_editor.config(wrap='word' , relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT , fill=tk.Y)
text_editor.pack(fill = tk.BOTH ,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)



#  font family functionality
current_font_family = 'Arial'
current_font_size = 12

def change_font(main_app):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family , current_font_size))


#  font family functionality

def change_font_size(main_app):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family , current_font_size))

font_box.bind("<<ComboboxSelected>>" , change_font)
font_size.bind("<<ComboboxSelected>>" , change_font_size)

#  buttons functionality --------

#  bold button functionality
def change_bold():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
 
#  italic button functionality
def change_italic():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

#  italic button functionality
def change_underline():
    text_property =tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size, 'underline' ))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))

# print(tk.font.Font(font=text_editor['font']).actual())

# font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

# align items functionality

#  align left
def align_left():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0 , 'end')
    text_editor.insert(tk.INSERT , text_content , 'left')

align_left_btn.configure(command=align_left)

#  align center
def align_center():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0 , 'end')
    text_editor.insert(tk.INSERT , text_content , 'center')

align_center_btn.configure(command=align_center)

#  align right
def align_right():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0 , 'end')
    text_editor.insert(tk.INSERT , text_content , 'right')

align_right_btn.configure(command=align_right)



font_color_btn.configure(command=change_font_color)   
underline_btn.configure(command=change_underline)   
italic_btn.configure(command=change_italic)   
bold_btn.configure(command=change_bold)   
text_editor.configure(font = ('Arial' , 12))
# -------------------------------- end text edittor ---------------------------------------

# --------------------------------status bar -------------------------------------------
status_bar = tk.Label(main_app , text = '-------- status bar ----')
status_bar.pack(side = tk.BOTTOM , fill = tk.X)


text_changed = False
def changed():
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0 , 'end-1c').splite)

# -------------------------------end of status bar =-------------------------------------




# ---------------------------------------- main manu functionality- - - - - - - - - - - - - - -    --

#  file comands
file.add_command(label='NEW', image=new_icon , compound = tk.LEFT ,accelerator = 'ctrl + n')
file.add_command(label='OPEN' , image=open_icon , compound = tk.LEFT , accelerator = 'ctrl + o')
file.add_command(label='SAVE' , image=save_icon , compound = tk.LEFT , accelerator = 'ctrl + s')
file.add_command(label='SAVE AS' , image= save_as_icon , compound = tk.LEFT , accelerator = 'ctrl + alt + x')
file.add_command(label='EXIT' , image=exit_icon , compound = tk.LEFT ,accelerator = 'ctrl + x')

#  edit commands

edit.add_command(label='copy', image=copy_icon , compound = tk.LEFT ,accelerator = 'ctrl + c')
edit.add_command(label='paste' , image=paste_icon , compound = tk.LEFT , accelerator = 'ctrl + v')
edit.add_command(label='cut' , image=cut_icon , compound = tk.LEFT , accelerator = 'ctrl + x')
edit.add_command(label='clear all' , image= clear_all_icon , compound = tk.LEFT , accelerator = 'ctrl + alt + delete')
edit.add_command(label='find' , image=find_icon , compound = tk.LEFT ,accelerator = 'ctrl + f')

#  view cheakbox
view.add_checkbutton(label='tool bar' , image= tool_bar_icon , compound=tk.LEFT)
view.add_checkbutton(label='status bar' , image= status_bar_icon , compound=tk.LEFT)

# clolor theme
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label= i , image=color_icon[count] , variable = theme_choice , compound=tk.LEFT)
    count += 1

# ---------------------------------------- main manu- - - - - - - - - - - - - - -    --


main_app.config(menu = main_manu)
main_app.mainloop()