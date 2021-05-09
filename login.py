from tkinter import *
from tkinter import messagebox
import matplotlib as plt
from calculatorfunc import new_module
from weather_find_func import weather_find
root=Tk()
root.geometry("500x500")
root.configure(background="grey")
frame=LabelFrame(root,text="User Login Portal",padx=10,pady=10)
frame.grid(padx=100,pady=150)
def calci():
    new_module()
def weather():
    weather_find()

def login_me():
    if user_name_entry.get()=="admin":
        if password_entry.get()=="akash":
            messagebox.showinfo("Sucess","Login Successfull")
            frame.destroy()
            label=Label(root,text="Welcome to the portal")
            label.pack()
            btn1=Button(root,text="Calculator",command=calci)
            btn1.pack(pady=10)
            btn2=Button(root,text="Weather",command=weather)
            btn2.pack(pady=10)

user_name=Label(frame,text="Username")
user_name.grid(row=0,column=0,padx=50)
password=Label(frame,text="Password")
password.grid(row=1,column=0,padx=50)

user_name_entry=Entry(frame)
user_name_entry.grid(row=0,column=1,pady=5)
password_entry=Entry(frame)
password_entry.grid(row=1,column=1,pady=5)

login=Button(frame,text="LogIn",relief=SUNKEN,command=login_me)
login.grid(row=2,column=0,columnspan=2,pady=20,sticky=W+E)

root.mainloop()