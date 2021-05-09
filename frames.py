from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Frames TKinter")
#to create a frame widget
frame=LabelFrame(root,text="This is My Frame.........",padx=70,pady=70)#this padding is used for inside the frame
frame.pack(padx=10,pady=10)#this padding is used to make padding from outside the frame wrt to the screen
btn=Button(frame,text="Don't Click",)
btn.pack()
root.mainloop()