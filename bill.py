#====================================video-8=================================#


from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class BillClass:
    def __init__(self,root):
        def __init__(self,root):
         self.root=root
         self.root.geometry("1350*700+0+0")
         self.root.tiltle("Inventory Management System | Developed By Name")
         self.root.config(bg="white")


#============ Copy from start to clock of dashboard=========#






self.var_search=StringVar()
ProductFrame1=Frame(self.root,bd=4,relief=RIDGE)
ProductFrame1.place(x=6,y=110,width=410,height=550)


pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)



ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg='white')
ProductFrame1.place(x=2,y=42,width=398,height=90)


lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=2,y=5)


lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=128,y=47,width=150,height=22)
btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)







#=================Copy from Employee Detail in supplier======================#














































if __name__=="__main__":
    root=TK()
    obj=BillClass(root)
    root.mainloop()