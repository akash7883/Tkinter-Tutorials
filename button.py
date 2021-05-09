from tkinter import *
root=Tk()
def clickme():
    res=Label(root,text="Submitted sucessfully").pack()
    button3=Button(root,bg="Yellow").pack()
mybutton=Button(root,text="CLick Me!",state=DISABLED).pack()
mybutton2=Button(root,text="Sbmit!",command=clickme).pack()#warning while using command just write the func name only

#changing foreground color of our button
button3=Button(root,text="Foreground button",fg="blue").pack()



root.mainloop()