from tkinter import *
root=Tk()
r=StringVar()
r.set("1")
def clicked(value):
    global lab1
    lab1.grid_forget()
    lab1=Label(root,text=" You selected {} !!".format(value))
    lab1.grid(row=3,column=0)


Radiobutton(root,text="Chai",variable=r,value="chai",command=lambda:clicked(r.get())).grid(row=0,column=0)
Radiobutton(root,text="Colddrink",variable=r,value="Colddrink",command=lambda:clicked(r.get())).grid(row=1,column=0)
Radiobutton(root,text="Coffee",variable=r,value="coffee",command=lambda:clicked(r.get())).grid(row=2,column=0)
global lab1
lab1=Label(root,text="You selected Nothing!!")
lab1.grid(row=3,column=0)
root.mainloop()