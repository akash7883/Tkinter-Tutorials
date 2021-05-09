from tkinter import * 
from tkinter import messagebox
root=Tk()
def click_me():
    messagebox.showwarning("Alert","HEllo")#used to show warning
    messagebox.showinfo("Inforamtion","HEllo")#used to show info
    messagebox.showerror("Alert","HEllo")#used to show error
    messagebox.askquestion("Ask QUestion","CHai needed?")
    messagebox.askretrycancel("canc","wanna contnue?")

btn=Button(root,text="CLick me",command=click_me).pack()
root.mainloop()