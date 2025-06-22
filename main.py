from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime   
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')  # Make the window fullscreen
        pass
       

        #first image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\download.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\facial recogniton.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\sdu.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\background.jpg")
        img3=img3.resize((1500,650))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=650)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=30)

        #================time=====================
        def time():
             string= strftime('%H:%M:%S %p')  
             lbl.config(text=string)  
             lbl.after(1000,time)

        lbl = Label(title_lbl,font=('times new roman',15,'bold'),background='white',foreground='red')
        lbl.place(x=0,y=0,width=110,height=40)

        time()     
      

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate scaling factors
        img_size = int(screen_width * 0.13)
        btn_width = img_size
        btn_height = int(screen_height * 0.05)
        x_gap = int(screen_width * 0.18)
        y_img = int(screen_height * 0.1)
        y_btn = y_img + img_size + 14
        y_img_train = y_btn + btn_height + 20
        y_btn_train = y_img_train + img_size + 10
        
        # Student Button
        img4 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\student.jpg")
        img4 = img4.resize((img_size, img_size))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=x_gap, y=y_img, width=img_size, height=img_size)
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap, y=y_btn, width=btn_width, height=btn_height)

        # Train Data Button (Below Student Details)
        img11 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\download.jpeg")
        img11 = img11.resize((img_size, img_size))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.train_data)
        b1.place(x=x_gap, y=y_btn + btn_height + 20, width=img_size, height=img_size) 

        # Adjusted Y position for Train Data image
        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap, y=y_btn + btn_height + img_size + 30, width=btn_width, height=btn_height)  # Adjusted Y position for Train Data text


        # Detect Face Button
        img5 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Face.jpg")
        img5 = img5.resize((img_size, img_size))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=x_gap * 2, y=y_img, width=img_size, height=img_size)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap * 2, y=y_btn, width=btn_width, height=btn_height)

        # Attendance Face Button
        img6 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Attendance.jpg")
        img6 = img6.resize((img_size, img_size))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=x_gap * 3, y=y_img, width=img_size, height=img_size)
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap * 3, y=y_btn, width=btn_width, height=btn_height)

        # Help Desk Button
        img7 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Help.jpg")
        img7 = img7.resize((img_size, img_size))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=x_gap * 4, y=y_img, width=img_size, height=img_size)
        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap * 4, y=y_btn, width=btn_width, height=btn_height)

       # PhotoFace Button (Below Face Detector)
        img8 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Photos.jpeg")
        img8 = img8.resize((img_size, img_size))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.open_img)
        b1.place(x=x_gap * 2, y=y_img_train, width=img_size, height=img_size)  # Adjusted Y position

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap * 2, y=y_btn_train, width=btn_width, height=btn_height)  # Adjusted Y position
        
         # Developer Button (Below Attendance)
        img9 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Developer.jpeg")
        img9 = img9.resize((img_size, img_size))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.dev_data)
        b1.place(x=x_gap * 3, y=y_img_train, width=img_size, height=img_size)  # Adjusted Y position
        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.dev_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap * 3, y=y_btn_train, width=btn_width, height=btn_height)  # Adjusted Y position

         # Exit Face Button (Below Help Desk)
        img10 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Exit.jpeg")
        img10 = img10.resize((img_size, img_size))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.iExit)
        b1.place(x=x_gap * 4, y=y_img_train, width=img_size, height=img_size)  # Adjusted Y position
        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=x_gap * 4, y=y_btn_train, width=btn_width, height=btn_height)  # Adjusted Y position

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this Project?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return        



        
    # define the method at the class level (NOT inside __init__)
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

     
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def dev_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)    

    
         

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop() 