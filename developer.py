from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x790+0+0")  # Slightly increased height
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="pink",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=30)

        img_top=Image.open(r"colleges_images\develop.jpg")
        img_top=img_top.resize((1530,720))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=500,height=570)

        img_top2=Image.open(r"colleges_images\Faiza.jpg")
        img_top2=img_top2.resize((200,200))
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=260,y=0,width=200,height=200)

        #Developer info

        dev_label=Label(main_frame,text="Hello my name is Faiza",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am Full Stack Developer",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="I work with technologies",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=80)

        dev_label=Label(main_frame,text="I enjoy solving complex errors",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=120)

        
        dev_label=Label(main_frame,text="Always excited to collaborate",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=160)


        img_top1=Image.open(r"colleges_images\full.jpg")
        img_top1=img_top1.resize((500,380))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=210,width=500,height=380)




if __name__ == "__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop() 


    