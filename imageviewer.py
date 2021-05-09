'''
sticky is used to make our label sticked in specific direction
relief =SUNKEN is used to make special type of border box with a line over it
anchor is used with sticky to make text move in specific direction according to sticky  
'''

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Akash Image Viewer")


my_image=ImageTk.PhotoImage(Image.open("Capture.PNG"))
my_image1=ImageTk.PhotoImage(Image.open("1.png"))
my_image2=ImageTk.PhotoImage(Image.open("3.png"))
my_image3=ImageTk.PhotoImage(Image.open("4.jpg"))
l=[my_image,my_image1,my_image2,my_image3]
labl=Label(root,image=l[0])
labl.grid(row=0,column=0,columnspan=3)

status=Label(root,text="Image 1 of "+str(len(l)),relief=SUNKEN,anchor=E)#sunken means like border down,anchor is used to place it in one side


def frwrd(image_number):
    global lab1
    global btn_bckwrd1
    global btn_frwrd1
    
    labl.grid_forget()#used to delete the existing pic
    lab2=Label(root,image=l[image_number-1])
    lab2.grid(row=0,column=0,columnspan=3)
    status=Label(root,text="Image {} of ".format(image_number)+str(len(l)),relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    btn_frwrd1=Button(root,text=">>",command=lambda:frwrd(image_number+1))
    btn_bckwrd1=Button(root,text="<<",command=lambda:bckwrd(image_number-1))
        
    if image_number==4:
        btn_frwrd1=Button(root,text=">>",state=DISABLED)
    btn_frwrd1.grid(row=1,column=2)
    btn_bckwrd1.grid(row=1,column=0)




def bckwrd(image_number):
    global lab1
    global btn_bckwrd1
    global btn_frwrd1
    
    labl.grid_forget()#used to delete the existing pic
    lab2=Label(root,image=l[image_number-1])
    lab2.grid(row=0,column=0,columnspan=3)
    status=Label(root,text="Image {} of ".format(image_number)+str(len(l)),relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    btn_bckwrd1=Button(root,text="<<",command=lambda:bckwrd(image_number-1))
    btn_frwrd1=Button(root,text=">>",command=lambda:frwrd(image_number+1))
    if image_number==1:
        btn_bckwrd1=Button(root,text="<<",state=DISABLED)

    btn_frwrd1.grid(row=1,column=2)
    btn_bckwrd1.grid(row=1,column=0)






    
    
    


    

btn_exit=Button(root,text="Exit Button",command=root.quit)
btn_exit.grid(row=1,column=1)
btn_frwrd=Button(root,text=">>",command=lambda:frwrd(2))
btn_frwrd.grid(row=1,column=2,pady=10)
btn_bckwrd=Button(root,text="<<",state=DISABLED)
btn_bckwrd.grid(row=1,column=0)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)#sticky is used to streched out
root.mainloop()