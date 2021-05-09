from tkinter import * 
from tkinter import messagebox
root=Tk()
varr=StringVar()
varr.set("your Dish")
l=["Chai","Samosa","Pizza","Burger"]
def order():
    
    labl=Label(root,text="You Selected {}".format(varr.get()))
    labl.pack()
opt=OptionMenu(root, varr,*l)
opt.pack()
btn=Button(root,text="Order",command=order).pack()


root.mainloop()