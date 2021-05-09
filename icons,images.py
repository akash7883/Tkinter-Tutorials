from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Akash Tkinter")
#set icon for my project
root.iconbitmap('2.ico')

#use of images in tkinter
'''
to use images in tkinter we need to use pillow package
'''
my_image=ImageTk.PhotoImage(Image.open("Capture.PNG"))
labl=Label(root,image=my_image)
labl.pack()


#create a exit button
btn_exit=Button(root,text="Exit Button",command=root.quit).pack()

root.mainloop()