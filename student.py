from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import glob
import os



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x790+0+0")  # Slightly increased height
        self.root.title("Face Recognition System")
    

      
        
        #===============variables===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_std_div=StringVar()
        self.var_std_roll=StringVar()
        self.var_std_gender=StringVar()
        self.var_std_dob=StringVar()
        self.var_std_email=StringVar()
        self.var_std_phone=StringVar()
        self.var_std_address=StringVar()
        self.var_std_teacher=StringVar()

       

        #first image
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\picture.jpeg")
        img=img.resize((500,130))  # Reduced image size
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\image.jpeg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\selfie.jpeg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=400,height=100)
       

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\background.jpg")
        img3=img3.resize((1500,650))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=650)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1400,height=30)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=40,width=1500,height=670)  # Increased main frame height

         #left labeL frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",10,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=620)  # Increased left frame height

        img_Left=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Attendance.jpeg")
        img_Left=img_Left.resize((580,100))
        self.photoimg_Left=ImageTk.PhotoImage(img_Left)

        f_lbl=Label(Left_frame,image=self.photoimg_Left)
        f_lbl.place(x=5,y=0,width=580,height=100)

        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",10,"bold"))
        current_course_frame.place(x=5,y=105,width=580,height=120)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly",width=15)
        dep_combo["values"]=("Select Department","Computer Science","Computer Engineering","IT","Software Engineering","Biology","Civil Engineering","Mechanical Engineering","Chemistry","Physics","Nursing","Law")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly",width=15)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly",width=15)
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

         #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly",width=15)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",10,"bold"))
        class_student_frame.place(x=5,y=230,width=580,height=350)  # Increased height to accommodate buttons
        
      
        #Student Id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",10,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=15,font=("times new roman",10,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,sticky=W)

        #Student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",10,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",10,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
       
        #Class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",10,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_std_div,width=15,font=("times new roman",8,"bold"))
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_roll,width=15,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_std_gender,width=15,font=("times new roman",8,"bold"))
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)


        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_dob,width=15,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_email,width=15,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_phone,width=15,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",10,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_address,width=15,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_teacher,width=15,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)
        
        #Radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)

       
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=5,column=1)

       #Button frame for Save, Update, Delete, Reset
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=4, y=200, width=420, height=30)

        # Create the save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=14, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=1)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=14, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,width=14, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=1)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=14, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=1)

       #Photo buttons frame (below the first frame)
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=4, y=240, width=420, height=30)  # Adjusted y position

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample", width=28, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=1)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample",command=self.update_photo_sample, width=30, font=("times new roman", 9, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=1)

        #right labeL frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",10,"bold"))
        Right_frame.place(x=620,y=15,width=1600,height=920)

        img_Right=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\Student.jpeg")
        img_Right=img_Right.resize((750,100))
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)

        f_lbl=Label(Right_frame,image=self.photoimg_Right)
        f_lbl.place(x=5,y=0,width=750,height=100)

       # ========Search System=========
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                text="Search System", font=("times new roman", 10, "bold"))
        Search_frame.place(x=5, y=105, width=750, height=70)  # Increased height to accommodate buttons

        search_label = Label(Search_frame, text="Search By:", font=(
            "times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.search_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 10, "bold"), state="readonly", width=15)
        self.search_combo["values"] = ("Select", "Roll No", "Phone No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        self.search_entry = ttk.Entry(Search_frame, width=14, font=(
            "times new roman", 10, "bold"))
        self.search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.search_btn = Button(Search_frame, text="Search", command=self.search_data, width=18, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        self.search_btn.grid(row=0, column=3, padx=4)

        self.showAll_btn = Button(Search_frame, text="Show All", command=self.show_all_data, width=18, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        self.showAll_btn.grid(row=0, column=4, padx=4)

         #============table frame=========

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=750,height=360)  # Increased height to accommodate buttons

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


       
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division") 
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        
        self.fetch_data()

        #=======ADD DATA=======
        
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_std_div.get(),
                                                                                                                self.var_std_roll.get(),
                                                                                                                self.var_std_gender.get(),
                                                                                                                self.var_std_dob.get(),
                                                                                                                self.var_std_email.get(),
                                                                                                                self.var_std_phone.get(),
                                                                                                                self.var_std_address.get(),
                                                                                                                self.var_std_teacher.get(),
                                                                                                                self.var_radio1.get()

                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)

    # ==========================Fetch==========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data) !=0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
               self.student_table.insert("",END,values=i)
           conn.commit()
           conn.close()
    
         #===================get cursor==========
    def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]
                if data and len(data) >= 15:  # assuming 15 columns expected

                    self.var_dep.set(data[0]),
                    self.var_course.set(data[1]),
                    self.var_year.set(data[2]),
                    self.var_semester.set(data[3]),
                    self.va_std_id.set(data[4]),
                    self.var_std_name.set(data[5]),
                    self.var_std_div.set(data[6]),
                    self.var_std_roll.set(data[7]),
                    self.var_std_gender.set(data[8]),
                    self.var_std_dob.set(data[9]),
                    self.var_std_email.set(data[10]),
                    self.var_std_phone.set(data[11]),
                    self.var_std_address.set(data[12]),
                    self.var_std_teacher.set(data[13]),
                    self.var_radio1.set(data[14])

                else:
                    messagebox.showwarning("Warning", "No valid data selected", parent=self.root)

        
        # ==========================updat==================
    def update_data(self):       
         if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
         else:
              try:
                   Update=messagebox.askyesno("Update","Do you want to update Students Details?",parent=self.root)
                   if Update>0:
                       conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
                       my_cursor=conn.cursor()
                       my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_std_div.get(),
                                                                                                                self.var_std_roll.get(),
                                                                                                                self.var_std_gender.get(),
                                                                                                                self.var_std_dob.get(),
                                                                                                                self.var_std_email.get(),
                                                                                                                self.var_std_phone.get(),
                                                                                                                self.var_std_address.get(),
                                                                                                                self.var_std_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.va_std_id.get()

                                                                                                         ))
                   else:
                       if not Update:
                          return
                   messagebox.showinfo("Success","Students details successfully Updated",parent=self.root) 
                   conn.commit()   
                   self.fetch_data()
                   conn.close()
              except Exception as es:
                   messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
                       
                           
    #delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
             try:
                  delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Students Details?",parent=self.root)
                  if delete>0:
                       conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
                       my_cursor=conn.cursor()
                       sql="delete from student where Student_id=%s"
                       val=(self.va_std_id.get(),)
                       my_cursor.execute(sql,val)
                  else:
                       if not delete:
                            return
                  conn.commit()   
                  self.fetch_data()
                  conn.close()    
                  messagebox.showinfo("Delete","Students details successfully Deleted",parent=self.root) 
             except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
    #Reset Button
    def reset_data(self):
            self.var_dep.set("Select Department"),
            self.var_course.set("Select Course"),
            self.var_year.set("Select Year"),
            self.var_semester.set("Select Semester"),
            self.va_std_id.set(""),
            self.var_std_name.set(""),
            self.var_std_div.set("Select Division"),
            self.var_std_roll.set(""),
            self.var_std_gender.set("Male"),
            self.var_std_dob.set(""),
            self.var_std_email.set(""),
            self.var_std_phone.set(""),
            self.var_std_address.set(""),
            self.var_std_teacher.set(""),
            self.var_radio1.set("")

    #========Generate data set or take a photo sample=======
    def generate_dataset(self):
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",user = "root",password="7758",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                         id+=1
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_std_div.get(),
                                                                                                                self.var_std_roll.get(),
                                                                                                                self.var_std_gender.get(),
                                                                                                                self.var_std_dob.get(),
                                                                                                                self.var_std_email.get(),
                                                                                                                self.var_std_phone.get(),
                                                                                                                self.var_std_address.get(),
                                                                                                                self.var_std_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.va_std_id.get()==id+1

                                                                                                             ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close() 

#=========load predefined data on face frontals from opencv====== 

                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                    def face_cropped(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifier.detectMultiScale(gray,1.3,5)
                         #Scaling factor=1.3
                         #Minimum neighbor=5
                         for(x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                         ret,my_frame=cap.read()
                         if face_cropped(my_frame) is not None:
                              img_id+=1
                              face=cv2.resize(face_cropped(my_frame),(450,450))
                              face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                              file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("Cropped Face",face)

                         if cv2.waitKey(1)==13 or int(img_id)==100:
                              break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets Completed!!")

                except Exception as es:
                    messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)


    def update_photo_sample(self):
        if self.va_std_id.get() == "":
            messagebox.showerror("Error", "Please enter a valid Student ID to update photo", parent=self.root)
            return

        try:
            student_id = self.va_std_id.get()

            # Connect to database and check if student exists
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="7758",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student WHERE Student_id=%s", (student_id,))
            result = my_cursor.fetchone()
            conn.close()

            if result is None:
                messagebox.showerror("Error", "Student ID not found in database", parent=self.root)
                return

            # ============================
            # Delete old face images
            # ============================
            image_files = glob.glob(f"data/user.{student_id}.*.jpg")
            for file in image_files:
                try:
                    os.remove(file)
                except Exception as e:
                    print(f"Could not delete file {file}: {e}")

            # ============================
            # Load face detector
            # ============================
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]
                return None

            # ============================
            # Open webcam and capture faces
            # ============================
            cap = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break
                cropped = face_cropped(my_frame)
                if cropped is not None:
                    img_id += 1
                    face = cv2.resize(cropped, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Updating Face Sample", face)

                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Success", "Photo sample has been updated successfully!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Error while updating photo sample:\n{str(e)}", parent=self.root)



    def search_data(self):
        search_by = self.search_combo.get()
        search_value = self.search_entry.get()

        if search_by == "Select" or search_value == "":
            messagebox.showerror("Error", "Please select a search criteria and enter a value", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="7758",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()

            if search_by == "Roll No":
                query = "SELECT * FROM student WHERE Roll LIKE %s"
            elif search_by == "Phone No":
                query = "SELECT * FROM student WHERE Phone LIKE %s"
            else:
                messagebox.showerror("Error", "Invalid Search Option", parent=self.root)
                return

            my_cursor.execute(query, (f"%{search_value}%",))
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("No Result", "No matching records found", parent=self.root)

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    def show_all_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="7758",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)




                                                

            
                                                                                                            
         



         
         
                            
                       
              
          












if __name__ == "__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop() 

























