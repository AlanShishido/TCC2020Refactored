import tkinter as tk
from tkinter import Menu

window = tk.Tk()
window.title("Using Menu")

menu = Menu(window)

new_item = Menu(menu)
new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.mainloop()