from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #==============Variables=============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # Background
        img4 = Image.open(r"colleges_images\background.jpg").resize((1500, 1000))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=5, width=1500, height=1000)

        # Side image
        image = Image.open(r"colleges_images\register.jpg")
        image = Image.open(r"colleges_images\register.jpg").resize((500, 550))
        self.bg1 = ImageTk.PhotoImage(image)

        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=500,height=550)

        # Main frame
        frame_L = Frame(self.root, bg="white")
        frame_L.place(x=520, y=100, width=500, height=550)

        self.txtuser=ttk.Entry(frame_L,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=120,width=165)

        get_str=Label(frame_L,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        get_str.place(x=20,y=20)

        label=Label(frame_L,text="First Name",font=("times new roman",15,"bold"),bg="white")
        label.place(x=50,y=90)


        F_label=Label(frame_L,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        F_label.place(x=300,y=90)

        self.txt=ttk.Entry(frame_L,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt.place(x=300,y=120,width=165)


        C_label=Label(frame_L,text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="black")
        C_label.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame_L,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=165)

        E_label=Label(frame_L,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        E_label.place(x=300,y=170)

        self.txt_email=ttk.Entry(frame_L,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=300,y=200,width=165)

        S_label=Label(frame_L,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        S_label.place(x=50,y=240)

        dep_combo=ttk.Combobox(frame_L,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        dep_combo["values"]=("Select","Your Birth Place","Your University Name","IT","Your City","Address")
        dep_combo.place(x=50,y=270,width=200)
        dep_combo.current(0)





        Se_label=Label(frame_L,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        Se_label.place(x=300,y=240)

        self.txt_security=ttk.Entry(frame_L,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=300,y=270,width=165)


        P_label=Label(frame_L,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        P_label.place(x=50,y=310)

        self.txt_pass=ttk.Entry(frame_L,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pass.place(x=50,y=340,width=165)

        Co_label=Label(frame_L,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        Co_label.place(x=300,y=310)

        self.txt_confirm=ttk.Entry(frame_L,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm.place(x=300,y=340,width=165)


        #================checkbutton===============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame_L,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0,borderwidth=0)
        checkbtn.place(x=50,y=380)


        #=================Buttons===============

        img1=Image.open(r"colleges_images\registernow.png")
        img1=img1.resize((200,140))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Button(frame_L,image=self.photoimg1,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        f_lbl.place(x=10,y=400,width=200)

        
        img2=Image.open(r"colleges_images\log.png")
        img2=img2.resize((200,150))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Button(frame_L,image=self.photoimg2,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        f_lbl.place(x=250,y=400,width=200)


        #=================Function Decleration==========
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)  
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Passwords must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions")
        else:
           conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
           my_cursor=conn.cursor()   
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
               messagebox.showerror("Error","User already Registered Try again with another Email")
           else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get(),
                                                                                       

                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
            self.root.destroy()           
            
               















if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()    