#=====================Video-6========================#

from tkinter import*
from PIL import Image,ImageTGk
from tkinter import ttk,messagebox
import sqlite3


class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100*500+220+130")
        self.root.tiltle("Inventory Management System | Developed By Name")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()



        product_Frame=Frame(self.root,bd=2,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=450,height=480)

        title=Label(self.root,text="Manage Product Detail",fonts=("goudy old style",18),bg="#0f4d78",fg="white").pack(side=TOP,fill=X)

        lbl_category=Label(self.root,text="Category",fonts=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(self.root,text="Supplier",fonts=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product_name=Label(self.root,text="Name",fonts=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(self.root,text="Price",fonts=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_quantity=Label(self.root,text="Quantity",fonts=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(self.root,text="Status",fonts=("goudy old style",18),bg="white").place(x=30,y=310)


        
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)


        txt_name=Entry(product_Frame,textvariable==self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable==self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable==self.var_qty,font=("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)


        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)



        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=40,height=40)
        btn_update=Button(product_Frame,text="Udpate",command=self.add,font=("goudy old style",15),bg="#4fcf50",fg="white",cursor="hand2").place(x=120,y=400,width=40,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.add,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=40,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.add,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=40,height=40)


        #===============COPY SREARCH frame options just before title===========#


        #======================================================================#


        #===============COPY Employee Deatil===========#


        #======================================================================#

    #=============== Copy from Employee tree ============#



if __name__=="__main__":
    root=TK()
    obj=productClass(root)
    root.mainloop()