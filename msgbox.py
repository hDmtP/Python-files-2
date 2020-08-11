from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")

messagebox.showinfo("pip install pip","slim")
messagebox.showwarning("pip install pip","slim")
messagebox.showerror("pip install pip","slim")
messagebox.askquestion("pip install pip","slim?")
messagebox.askokcancel("pip install pip","slim?")
messagebox.askyesno("pip install pip","slim?")
messagebox.askretrycancel("pip install pip","slim?")
top.mainloop()