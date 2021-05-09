from tkinter import *
from PIL import ImageTk,Image
import requests#used to call out api's
import json#toimport json files
#to change root window background color use root.configure("name")
root=Tk()
root.configure(background="grey")
#api.openweathermap.org/data/2.5/weather?q=Auraiya&appid=b69aff293372bae47456cc6fd70bc635
def get_weather(pincode):
    try:
        api_request=requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+ pincode + ",IN&appid=4e79ea238ea43ff5cf28f58c3409ffe1")
        api=json.loads(api_request.content)
        mylabl=Label(frame,text="Weather in "+api["name"]+" "+api["weather"][0]["description"])
        mylabl.grid(row=2,column=0)
    except Exception as e:
        api=e
        mylabl=Label(frame,text=api)
        mylabl.grid(row=3,column=0,pady=20)

frame=LabelFrame(root,text="My Weather Forecast",padx=20,pady=20)
frame.grid(padx=100,pady=100)
search_label=Label(frame,text="Enter Your Zip Code")
search_label.grid(row=0,column=0,padx=50,pady=50)
search=Entry(frame,relief=SUNKEN)
search.grid(row=0,column=1,padx=50,pady=50)
search_btn=Button(frame,text="Search",command=lambda:get_weather(search.get()))
search_btn.grid(row=1,column=0,pady=25)
root.mainloop()