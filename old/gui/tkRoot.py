#desenvolvimento de código para o trabalho da faculdade
#Alan Hideyuki Shishido

import tkinter as tk

root = tk.Tk()
root.title('create window')
root.geometry("300x300+10+10")

lb = tk.Label(root,
    text="Olá, Mundo!",
    fg="white",
    bg="blue",
    width=10,
    height=10,
    font=("Roboto", 24)
)

lb.pack()

root.mainloop()