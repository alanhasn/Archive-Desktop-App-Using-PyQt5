# import customtkinter as ctk

# class main_class():
	
# 	def init_ui():
# 		window=ctk.CTk()
# 		window.geometry('400x400+800+200')
# 		window.resizable(False,False)
# 		window.title('Offline web Saver')
# 		ctk.set_appearance_mode('dark')
# 		ctk.set_default_color_theme('blue')

# 		label=ctk.CTkLabel(window,text='Name')
# 		label.place(x=50,y=100)
# 		Entry = ctk.CTkEntry(window,width=200)
# 		Entry.place(x=100,y=100)

# 		label1=ctk.CTkLabel(window,text='History')
# 		label1.place(x=50,y=150)
# 		Entry2 = ctk.CTkEntry(window,width=200)
# 		Entry2.place(x=100,y=150)

# 		label2=ctk.CTkLabel(window,text='URL')
# 		label2.place(x=50,y=200)
# 		Entry2 = ctk.CTkEntry(window,width=200)
# 		Entry2.place(x=100,y=200)

# 		Entry2 = ctk.CTkEntry(window,width=200)
# 		Entry2.place(x=100,y=250)

# 		save = ctk.CTkButton(window,text='Save',width=200)
# 		save.place(x=100,y=250)
# 		save = ctk.CTkButton(window,text='Show the Webpage',width=200)
# 		save.place(x=100,y=290)

# 		window.mainloop()

# main_class.init_ui()


from tkinter import Tk, Menu


# root window
root = Tk()
root.geometry('320x150')
root.title('Menu Demo')


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

root.mainloop()
