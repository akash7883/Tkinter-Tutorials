#updation part is left
from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.geometry("620x620")
#creaing a frame for my address book
frame=LabelFrame(root,text="My Address Book",padx=5,pady=5,bg="grey")
frame.grid(padx=20,pady=20)
#defining of functions
'''def create_database():
    conn=sqlite3.connect('AddressBook.db')
    curs=conn.cursor()
    curs.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address_name text,
        zipcode_name integer,
        mobile_name integer
    )""")
    conn.commit()
    conn.close()
    created=1'''
#this func is to add data to database
def submit():
    messagebox.showinfo("SucessFull!","Name Added to Database Successfully")
    conn=sqlite3.connect('AddressBook.db')
    curs=conn.cursor()
    curs.execute( " INSERT INTO addresses VALUES (:first_name,:last_name,:address_name,:zipcode_name,:phone_name)",
        {
            'first_name':f_name.get(),
            'last_name':l_name.get(),
            'address_name':address.get(),
            'zipcode_name':zipcode.get(),
            'phone_name':phone.get(),
        }
    )
    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    zipcode.delete(0,END)
    phone.delete(0,END)
#this func is used to view the record
def query():
    conn=sqlite3.connect('AddressBook.db')
    curs=conn.cursor()
    curs.execute(" SELECT *,oid FROM addresses ")
    p=curs.fetchall()
    res=""
    for each in p:
        if each[0]=="":
            continue
        res+=(str(each[0])+"  "+str(each[1])+" :->"+str(each[5])+"\n")

    labl=Label(frame,text=res)
    labl.grid(row=8,column=0,columnspan=2)
    conn.commit()
    conn.close()
def edit(idi):
    global record_id
    global f_name_editor
    global l_name_editor
    global address_editor
    global zipcode_editor
    global phone_editor
    record_id=idi
    new_window=Toplevel()
    #creating the Labels for my Address Book
    f_name_lbl=Label(new_window,text="First Name :")
    f_name_lbl.grid(row=0,column=0,padx=15,pady=15)
    l_name_lbl=Label(new_window,text="Last Name :")
    l_name_lbl.grid(row=1,column=0,padx=15,pady=15)
    address_lbl=Label(new_window,text="Address :")
    address_lbl.grid(row=2,column=0,padx=15,pady=15)
    zipcode_lbl=Label(new_window,text="ZipCode :")
    zipcode_lbl.grid(row=3,column=0,padx=15,pady=15)
    phone_lbl=Label(new_window,text="Mobile No. :")
    phone_lbl.grid(row=4,column=0,padx=15,pady=15)
    #creation of entries for the labels above
    f_name_editor=Entry(new_window)
    f_name_editor.grid(row=0,column=1,padx=25,pady=15)
    l_name_editor=Entry(new_window)
    l_name_editor.grid(row=1,column=1,padx=25,pady=15)
    address_editor=Entry(new_window)
    address_editor.grid(row=2,column=1,padx=25,pady=15)
    zipcode_editor=Entry(new_window)
    zipcode_editor.grid(row=3,column=1,padx=25,pady=15)
    phone_editor=Entry(new_window)
    phone_editor.grid(row=4,column=1,padx=25,pady=15)
    submit_btn=Button(new_window,text="Update Record",relief=SUNKEN,command=update_me)
    submit_btn.grid(row=5,column=0,columnspan=2,padx=25,pady=10)
    conn=sqlite3.connect('AddressBook.db')
    curs=conn.cursor()
    curs.execute("SELECT * FROM addresses WHERE oid="+idi)
    res=curs.fetchall()
    l=[]
    for each in res[0]:
        l.append(each)
    f_name_editor.insert(0,l[0])
    l_name_editor.insert(0,l[1])
    address_editor.insert(0,l[2])
    zipcode_editor.insert(0,l[3])
    phone_editor.insert(0,l[4])
    conn.commit()
    conn.close()

#left one
def update_me():
    record_id=select_name.get()
    print(record_id)
    conn=sqlite3.connect('AddressBook.db')
    curs=conn.cursor()
    curs.execute("""UPDATE addresses SET 
        first_name=:first,
        last_name=:last,
        address_name=:address,
        zipcode_name=:zipcode,
        mobile_name=:phone
        WHERE oid= :oidi""",
        {
            'first':f_name_editor.get(),
            'last':l_name_editor.get(),
            'address':address_editor.get(),
            'zipcode':zipcode_editor.get(),
            'phone':phone_editor.get(),
            'oidi':record_id
        }
        )
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucess","Update Successfullly")
#creating the Labels for my Address Book
f_name_lbl=Label(frame,text="First Name :")
f_name_lbl.grid(row=0,column=0,padx=15,pady=15)
l_name_lbl=Label(frame,text="Last Name :")
l_name_lbl.grid(row=1,column=0,padx=15,pady=15)
address_lbl=Label(frame,text="Address :")
address_lbl.grid(row=2,column=0,padx=15,pady=15)
zipcode_lbl=Label(frame,text="ZipCode :")
zipcode_lbl.grid(row=3,column=0,padx=15,pady=15)
phone_lbl=Label(frame,text="Mobile No. :")
phone_lbl.grid(row=4,column=0,padx=15,pady=15)
#creation of entries for the labels above
f_name=Entry(frame)
f_name.grid(row=0,column=1,padx=25,pady=15)
l_name=Entry(frame)
l_name.grid(row=1,column=1,padx=25,pady=15)
address=Entry(frame)
address.grid(row=2,column=1,padx=25,pady=15)
zipcode=Entry(frame)
zipcode.grid(row=3,column=1,padx=25,pady=15)
phone=Entry(frame)
phone.grid(row=4,column=1,padx=25,pady=15)
#creation of input for updation
select_name_label=Label(frame,text="Enter Name",relief=SUNKEN)
select_name_label.grid(row=9,column=0,padx=15,pady=15)
select_name=Entry(frame,relief=SUNKEN)
select_name.grid(row=9,column=1,padx=25,pady=15)
#creation of buttons
#submit button
submit_btn=Button(frame,text="Submit Record",relief=SUNKEN,command=submit)
submit_btn.grid(row=5,column=0,columnspan=2,padx=25,pady=10)
#query button
query_btn=Button(frame,text="View Record",relief=SUNKEN,command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=25,pady=10)
# update button
update_btn=Button(frame,text="Update Record",relief=SUNKEN,command=lambda:edit(select_name.get()))
update_btn.grid(row=10,column=0,columnspan=2,padx=25,pady=10)
status=Label(frame,text="Copyright@Akash Porwal ",relief=SUNKEN,anchor=E,bg="black",fg="white")
status.grid(row=11,column=0,columnspan=2,sticky=W+E,pady=100)
root.mainloop()