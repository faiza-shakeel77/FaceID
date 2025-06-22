from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x790+0+0")  # Slightly increased height
        self.root.title("Face Recognition System")


        #==============Variables==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()








        #first image
        img=Image.open(r"colleges_images\uni.jpg")
        img=img.resize((800,200))  # Reduced image size
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second image
        img1=Image.open(r"colleges_images\suley.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #background image
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Face Recognization System\colleges_images\background.jpg")
        img3=img3.resize((1500,650))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1500,height=650)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1400,height=30)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=60,width=1500,height=710) 

        #left labeL frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Detail",font=("times new roman",10,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=710) 

        img_Left=Image.open(r"colleges_images\att.jpg")
        img_Left=img_Left.resize((580,100))
        self.photoimg_Left=ImageTk.PhotoImage(img_Left)

        f_lbl=Label(Left_frame,image=self.photoimg_Left)
        f_lbl.place(x=5,y=0,width=580,height=100)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=590,height=400) 

        #Attendance Id
        studentId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",10,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)

        studentId_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("times new roman",10,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,sticky=W)

        #roll
        Rolllabel=Label(left_inside_frame,text="Roll:",font=("times new roman",10,"bold"),bg="white")
        Rolllabel.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("times new roman",10,"bold"))
        roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

         #Name
        namelabel=Label(left_inside_frame,text="Name:",font=("times new roman",10,"bold"),bg="white")
        namelabel.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("times new roman",10,"bold"))
        name_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        #Department
        deplabel=Label(left_inside_frame,text="Department:",font=("times new roman",10,"bold"),bg="white")
        deplabel.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_department,font=("times new roman",10,"bold"))
        dep_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)


        #Time
        timelabel=Label(left_inside_frame,text="Time:",font=("times new roman",10,"bold"),bg="white")
        timelabel.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("times new roman",10,"bold"))
        time_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #Date
        datelabel=Label(left_inside_frame,text="Date:",font=("times new roman",10,"bold"),bg="white")
        datelabel.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("times new roman",10,"bold"))
        date_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #Attendance Status
        status_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",10,"bold"),bg="white")
        status_label.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        status_combo=ttk.Combobox(left_inside_frame,width=15,textvariable=self.var_atten_attendance,font=("times new roman",8,"bold"))
        status_combo["values"]=("Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=5,column=1,padx=5,pady=5,sticky=W)

         #Button frame for Save, Update, Delete, Reset
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=3, y=270, width=1600, height=30)

        # Create the save button
        import_btn = Button(btn_frame, text="Import csv",command=self.importCsv,width=20, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, padx=1)

        export_btn = Button(btn_frame, text="Export csv",command=self.exportCsv,width=20, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, padx=1)

        update_btn = Button(btn_frame, text="Update",command=self.update_data,width=20, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=1)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=20, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=1)


         #right labeL frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Detail",font=("times new roman",10,"bold"))
        Right_frame.place(x=620,y=15,width=1600,height=920)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=720, height=400)


        #================scroll bar table==========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #=============fetch Data===========

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)   

            #=======Import CSV======== 
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    


             #=======Export CSV======== 

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False    
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exported to" +os.path.basename(fln)+"successfully")    
        except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_id.set(rows[0])
         self.var_atten_roll.set(rows[1])
         self.var_atten_name.set(rows[2])
         self.var_atten_department.set(rows[3])
         self.var_atten_date.set(rows[4])
         self.var_atten_time.set(rows[5])
         self.var_atten_attendance.set(rows[6])

         #=======Reset Data=========

    def reset_data(self):
         self.var_atten_id.set("")
         self.var_atten_roll.set("")
         self.var_atten_name.set("")
         self.var_atten_department.set("")
         self.var_atten_date.set("")
         self.var_atten_time.set("")
         self.var_atten_attendance.set("")



         #===========update data========

    def update_data(self):
        selected = self.AttendanceReportTable.focus()
        if selected == "":
            messagebox.showerror("Error", "Please select a row to update.", parent=self.root)
            return

        updated_values = (
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_department.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        )

        if "" in updated_values:
            messagebox.showerror("Error", "All fields must be filled before updating.", parent=self.root)
            return

        # Update data in Treeview
        self.AttendanceReportTable.item(selected, values=updated_values)

        # Update mydata list
        selected_index = self.AttendanceReportTable.index(selected)
        mydata[selected_index] = list(updated_values)

        messagebox.showinfo("Success", "Record updated successfully.", parent=self.root)

                





                   






    

if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop() 