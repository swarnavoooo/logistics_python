#=====================Video-5========================#

from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By Name")
        self.root.config(bg="white")
        self.root.focus_force()
        

        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        lbl_title=Label(self.root,text="Manage Product Category",fonts=("new roman style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=x,padx=10,pady=20)


        lbl_name=Label(self.root,text="Enter Category Name",fonts=("new roman style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,fonts=("new roman style",18),bg="lightyellow").place(x=50,y=170,width=300)
        btn_add=Button(self.root,text="ADD",fonts=("new roman style",30),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",fonts=("new roman style",30),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)





        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=120,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)


        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand= sc)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly,config(command=self.category_table.yview)


        self.category_table.heading("cid",text="C ID")
        self.category_table.heading("name",text="Name")
        self.category_table["show"]="headings"
        self.category_table.column("cid",width=90)
        self.category_table.column("name",width=100)
        self.category_table.pack(fill=BOTH,expand=1)



        self.im1=Image.open("images/logistic-management-3.jpg")
        self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)


        self.im2=Image.open("images/logistic-management-3.Logistic-Management-Hero.jpg")
        self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)



        #==============Copy from Supplier ============#









if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()


    