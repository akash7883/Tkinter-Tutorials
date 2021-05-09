from tkinter import * 
from tkinter import messagebox
root=Tk()
vr=IntVar()
def chck():
    labl=Label(root,text=vr.get()).pack()

c=Checkbutton(root,text="Check Box 1",variable=vr)
c.pack()
btn=Button(root,text="Check Selection",command=chck).pack()

root.mainloop()