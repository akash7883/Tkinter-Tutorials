
from tkinter import *
def new_module():
    

    root=Tk()
    root.title("My Calci")
    #creation of input dispay area
    input_text=Entry(root,width=35,borderwidth=5)
    input_text.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    #creation of func
    def button_click(number):
        curr=input_text.get()
        input_text.delete(0,END)
        input_text.insert(0,str(curr)+str(number)) 
    def button_clear():
        input_text.delete(0,END)
    def equal():
        global result
        p=(input_text.get())
        if(m=="addition"):
            result=int(f_num)+int(p)
        elif m=="subtraction":
            result=int(f_num)-int(p)
        elif m=="multiplication":
            result=int(f_num)*int(p)
        elif m=="division":
            result=int(f_num)/int(p)
        elif m=="power":
            result=int(f_num)**int(p)
        input_text.delete(0,END)
        input_text.insert(0,result)
    def add():
        current_number_a=(input_text.get())
        global f_num
        f_num=current_number_a
        global m
        m="addition"
        input_text.delete(0,END)
    def subtract():
        
        current_number_a=(input_text.get())
        global f_num
        f_num=current_number_a
        global m
        m="subtraction"
        input_text.delete(0,END)
    def multiply():
        current_number_a=(input_text.get())
        global f_num
        f_num=current_number_a
        global m
        m="multiplication"
        input_text.delete(0,END)
    def power():
        current_number_a=(input_text.get())
        global f_num
        f_num=current_number_a
        global m
        m="power"
        input_text.delete(0,END)
    def division():
        current_number_a=(input_text.get())
        global f_num
        f_num=current_number_a
        global m
        m="division"
        input_text.delete(0,END)


    #craetion of button widgets
    button_1=Button(root,text="1",padx=40,pady=25,command=lambda:button_click(1),bg="grey",fg="white")
    button_2=Button(root,text="2",padx=40,pady=25,command=lambda:button_click(2),fg="black")
    button_3=Button(root,text="3",padx=40,pady=25,command=lambda:button_click(3),bg="grey",fg="white")

    button_4=Button(root,text="4",padx=40,pady=25,command=lambda:button_click(4),fg="black")
    button_5=Button(root,text="5",padx=40,pady=25,command=lambda:button_click(5),bg="skyblue",fg="black")
    button_6=Button(root,text="6",padx=40,pady=25,command=lambda:button_click(6),fg="black")

    button_7=Button(root,text="7",padx=40,pady=25,command=lambda:button_click(7),bg="grey",fg="white")
    button_8=Button(root,text="8",padx=40,pady=25,command=lambda:button_click(8),fg="black")
    button_9=Button(root,text="9",padx=40,pady=25,command=lambda:button_click(9),bg="grey",fg="white")



    button_0=Button(root,text="0",padx=40,pady=25,command=lambda:button_click(0),fg="black")
    button_subtract=Button(root,text="-",padx=40,pady=25,command=subtract,bg="skyblue",fg="black")
    button_add=Button(root,text="+",padx=40,pady=25,command=add,fg="black")


    button_multiplication=Button(root,text="*",padx=40,pady=25,command=multiply,bg="grey",fg="white")
    button_division=Button(root,text="/",padx=40,pady=25,command=division,fg="black")
    button_power=Button(root,text="^",padx=40,pady=25,command=power,bg="grey",fg="white")

    button_equals=Button(root,text="=",padx=90,pady=25,command=equal,fg="black")
    button_clear=Button(root,text="Clear",padx=30,pady=25,command=button_clear,fg="black")
    #packing up the buttons on the screen

    button_equals.grid(row=6,column=1,columnspan=2)
    button_clear.grid(row=6,column=0)

    button_multiplication.grid(row=5,column=0)
    button_division.grid(row=5,column=1)
    button_power.grid(row=5,column=2)

    button_0.grid(row=4,column=0)
    button_subtract.grid(row=4,column=1)
    button_add.grid(row=4,column=2)

    button_1.grid(row=3,column=0)
    button_2.grid(row=3,column=1)
    button_3.grid(row=3,column=2)

    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)

    button_7.grid(row=1,column=0)
    button_8.grid(row=1,column=1)
    button_9.grid(row=1,column=2)

    root.mainloop()