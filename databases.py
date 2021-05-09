from tkinter import *
import sqlite3#database library
root=Tk()
#create a database or connect it with
conn=sqlite3.connect('akash_database.db')
#creatioin of cursor to perfomrm task
cursr=conn.cursor()
'''
#creating our table using cursor
cursr.execute(""" CREATE TABLE userprofile(
first_name text,
last_name text,
address text,
city text,
phone_no integer
)""")'''
cursr.execute("""
insert into userprofile values ("Akash","Porwal","72 Bidhicandra","Auraiya",12345678)
""")
cursr.execute("SELECT DISTINCT * FROM userprofile")

labl=Label(root,text=cursr.fetchall()).pack()
#commiting changes to our database
conn.commit()
#closing our database
conn.close()
root.mainloop()