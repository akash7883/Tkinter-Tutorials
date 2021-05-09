from tkinter import *
root=Tk()
#to fix size of our root
root.geometry("400x400")
horizontal=Scale(root,from_=0,to=400)
horizontal.pack()
def get_slider():
    label=Label(root,text=horizontal.get()).pack()
btn=Button(root,text="GET VALUE",command=get_slider).pack()
root.mainloop()