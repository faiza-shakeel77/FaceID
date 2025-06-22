from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x790+0+0")  # Slightly increased height
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",25,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=0,width=1400,height=30)

        img_top=Image.open(r"colleges_images\desk.jpg")
        img_top=img_top.resize((1400,750))
        
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1400,height=750)

        
        help_label=Label(f_lbl,text="Email:faizashakeel095@gmail.com",font=("times new roman",20,"bold"),bg="white")
        help_label.place(x=500,y=40)
        







if __name__ == "__main__":
        root=Tk()
        obj=Help(root)
        root.mainloop() 