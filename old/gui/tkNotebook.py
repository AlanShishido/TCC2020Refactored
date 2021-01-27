# Notebook widget (TAB CONTROL)

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("300x300")

window.title("Using 2 Tab Control")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

lbl1 = tk.Label(tab1, text= 'label1')

lbl1.grid(column=0, row=0)

lbl2 = tk.Label(tab2, text= 'label2')

lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()