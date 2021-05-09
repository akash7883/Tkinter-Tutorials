from tkinter import *
root=Tk()
def open():
    top=Toplevel()#used to create new window
    top.title("Second Window")
    btn=Button(top,text="Close This Window",command=top.destroy).pack()

btn=Button(root,text="Open Second Window",command=open).pack()
root.mainloop()