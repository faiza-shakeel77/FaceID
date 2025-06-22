from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from register import Register
from main import Face_Recognition_System



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        #first image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\three.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

               # Second image (Facial Recognition)
        facial_img = Image.open(r"colleges_images/facial.jpg").convert("RGB")
        facial_img = facial_img.resize((500, 130))
        self.photo_facial = ImageTk.PhotoImage(facial_img)

        f_lbl1 = Label(root, image=self.photo_facial)
        f_lbl1.place(x=500, y=0, width=500, height=130)

          # Third image (SDU)
        sdu_img = Image.open(r"colleges_images/third.jpg").convert("RGB")
        sdu_img = sdu_img.resize((500, 130))
        self.photo_sdu = ImageTk.PhotoImage(sdu_img)

        f_lbl2 = Label(root, image=self.photo_sdu)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Ai.jpg")
        img3=img3.resize((1500,650))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=650)

        title_lbl=Label(bg_img,text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1370,height=30)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=175,width=300,height=450)

        get_str=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=60,y=100)

        user_label=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        user_label.place(x=60,y=165)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=20,y=195,width=220)


        password_label=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_label.place(x=60,y=240)
        
        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=20,y=270,width=220)


        #================Icon Image===========

        img1=Image.open(r"colleges_images\username.jpg")
        img1=img1.resize((40,40))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(image=self.photoimg1,bg="black",borderwidth=0)
        f_lbl.place(x=520,y=325,width=40,height=40)

        img2=Image.open(r"colleges_images\pass.png")
        img2=img2.resize((40,40))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(image=self.photoimg2,bg="black",borderwidth=0)
        f_lbl.place(x=520,y=400,width=40,height=40)

        loginbtn = Button(frame,command=self.login,text="Login", width=14, font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        loginbtn.place(x=70,y=310,width=120,height=35)

        registerbtn = Button(frame, text="New User Register",command=self.register_window, width=14, font=("times new roman", 10, "bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        registerbtn.place(x=25,y=360,width=130)


        passbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, width=14, font=("times new roman", 10, "bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        passbtn.place(x=20,y=390,width=140)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
           

    def login(self):
            if self.txtuser.get()=="" or self.txtpassword.get()=="":
                 messagebox.showerror("Error","Enter Your Password")
            elif self.txtuser.get()=="kapu" and self.txtpassword.get()=="ashu":
                 messagebox.showinfo("Success","Welcome")
            else:
               conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
               my_cursor=conn.cursor()   
               my_cursor.execute("select * from register where email=%s and password=%s",( 
                                                                                               self.txtuser.get(),
                                                                                               self.txtpassword.get()

                                                                             ))
               row=my_cursor.fetchone()
               if row==None:
                    messagebox.showerror("Error","Invalid username & Password") 
               else:
                    open_main=messagebox.askyesno("YesNo","Access only admin")  
                    if open_main>0:
                         self.new_window=Toplevel(self.root)
                         self.app=Face_Recognition_System(self.new_window)
                    else:
                         if not open_main:     
                             return
               conn.commit()
               conn.close()

               #=================Reset Password==========
    def reset_pass(self):
     if self.txtuser.get() == "":
          messagebox.showerror("Error", "Please enter your email",parent=self.root2)
     elif self.combo_security_Q.get() == "Select":
          messagebox.showerror("Error", "Select a Security Question",parent=self.root2)
     elif self.txt_security.get() == "":
          messagebox.showerror("Error", "Please enter the Answer",parent=self.root2)
     elif self.txt_newpass.get() == "":
          messagebox.showerror("Error", "Please enter a new password",parent=self.root2)
     else:
          try:
               conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="7758",
                    database="face_recognizer"
               )
               my_cursor = conn.cursor()

               email = self.txtuser.get().strip()
               sec_q = self.combo_security_Q.get().strip()
               sec_a = self.txt_security.get().strip()

               print("DEBUG VALUES -->")
               print("Email:", email)
               print("Security Question:", sec_q)
               print("Security Answer:", sec_a)

               query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
               value = (email, sec_q, sec_a)
               my_cursor.execute(query, value)
               row = my_cursor.fetchone()

               if row is None:
                    messagebox.showerror("Error", "Incorrect details. Please check your email, question, or answer.",parent=self.root2)
               else:
                    new_pass = self.txt_newpass.get().strip()
                    update_query = "UPDATE register SET password=%s WHERE email=%s"
                    update_value = (new_pass, email)
                    my_cursor.execute(update_query, update_value)
                    conn.commit()
                    messagebox.showinfo("Success", "Password has been reset successfully.",parent=self.root2)
          except Exception as e:
               messagebox.showerror("Database Error", f"Error: {str(e)}")
          finally:
               if conn.is_connected():
                    conn.close()
                    self.root2.destroy()

                    
                    

               #==================forget======================

    def forgot_password_window(self):
         if self.txtuser.get()=="":
              messagebox.showerror("Error","Please Enter the Email Address to reset Password")
         else:
              conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
              my_cursor=conn.cursor()   
              query=("select * from register where email=%s")
              value=(self.txtuser.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              #print(row)

              if row==None:
                   messagebox.showerror("My Error","Please enter the valid User Name")
              else:
                   conn.close()
                   self.root2=Toplevel()
                   self.root2.title("Forget Password")
                   self.root2.geometry("340x450+610+170")     

                   l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"),fg="green",bg="white")
                   l.place(x=0,y=10,relwidth=1)


                   
                   security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                   security_Q.place(x=50,y=80)

                   self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                   self.combo_security_Q["values"]=("Select","Your Birth Place","Your University Name","IT","Your City","Address")
                   self.combo_security_Q.place(x=50,y=110,width=200)
                   self.combo_security_Q.current(0)

                   security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                   security_A.place(x=50,y=150)

                   self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                   self.txt_security.place(x=50,y=180,width=165)

                   new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                   new_password.place(x=50,y=220)

                   self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                   self.txt_newpass.place(x=50,y=250,width=250)

                   btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                   btn.place(x=100,y=290)

                              
                              


                              



if __name__ == "__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()    
        

