from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
def open():
    global img_1
    filename=filedialog.askopenfilename(initialdir="/D:/", title="open")
    img_1=ImageTk.PhotoImage(Image.open(filename))
    img_label=Label(root,image=img_1).pack()
    

btn=Button(root,text="Open File Explorer",comman=open).pack()

root.mainloop() 