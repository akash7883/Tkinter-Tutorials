from tkinter import *
root=Tk()
inpt=Entry(root,width=50,fg="black")
inpt.pack()
#to get the output we have typed into it is by using .get() method
#to make placeholder use .insert() mehtod
inpt.insert(0,"Enter ur name")
def meclick():
    label1=Label(root,text="Welcome "+inpt.get())
    label1.pack()
    
    

btn=Button(root,text="Enter your name",command=meclick)
btn.pack()
root.mainloop()