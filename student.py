from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student")
        self.root.geometry("1980x1080+0+0")
        
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_branch=StringVar()
        self.var_std_id=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_std_name=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_radiobtn1=StringVar()

        
        img=Image.open("img2.jpg")
        img=img.resize((1980,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0)
        
        title_lbl=Label(self.root,text="Student Portal",font=("Roman",35,"bold"),bg = "black",fg ="white")
        title_lbl.place(x=0,y=0,width=1520,height=70)
        
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=15,y=80,width=1500,height=650)
        
        img_frame=Image.open("img2.jpg")
        img_frame=img.resize((1980,1080),Image.ANTIALIAS)
        self.photoimg_frame=ImageTk.PhotoImage(img_frame)
        
        f_lbl=Label(main_frame,image=self.photoimg)
        f_lbl.place(x=0,y=0, width= 1500, height=650)
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Details",font=("times of roman",25,"bold"),fg="white")
        Left_frame.place(x=10,y=20,width=720,height=580)
        
        img_left=Image.open("eye.jpg")
        img_left=img_left.resize((720,160),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl_left=Label(Left_frame,image=self.photoimg_left)
        f_lbl_left.place(x=5,y=0, width= 710, height=130)
        
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="black",relief=RIDGE,text="Course Details",font=("times of roman",15,"bold"),fg="white")
        current_course_frame.place(x=5,y=135,width=700,height=130)
        
        dep_label = Label(current_course_frame,text="Department",font=("times of roman",10,"bold"),width=10,bg="black",fg="white")
        dep_label.grid(row=0,column=0)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times of roman",10,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department", "B.Tech", "BBA", "BCA", "MBA","Pharmacy")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=40,pady=10)
        
        cou_label = Label(current_course_frame,text="Branch",font=("times of roman",10,"bold"),width=10,bg="black",fg="white")
        cou_label.grid(row=0,column=2)
        
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_branch,font=("times of roman",10,"bold"),width=20,state="readonly")
        cou_combo["values"]=("Select Course", "CSE", "EE", "EC", "ME","Civil","Biotech")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=40,pady=10,sticky=W)
        
        year_label = Label(current_course_frame,text="Year",font=("times of roman",10,"bold"),width=10,bg="black",fg="white")
        year_label.grid(row=1,column=0)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times of roman",10,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year", "1st", "2nd", "3rd", "4rth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=40,pady=10,sticky=W)
        
        sem_label = Label(current_course_frame,text="Semester",font=("times of roman",10,"bold"),width=10,bg="black",fg="white")
        sem_label.grid(row=1,column=2,sticky=W)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times of roman",10,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=40,pady=10,sticky=W)
        
        student_info_frame=LabelFrame(Left_frame,bd=2,bg="black",relief=RIDGE,text="Student information",font=("times of roman",15,"bold"),fg="white")
        student_info_frame.place(x=5,y=270,width=700,height=260)
        
        student_label = Label(student_info_frame,text="Student ID",font=("times of roman",10,"bold"),bg="black",fg="white")
        student_label.grid(row=0,column=0,padx=40,sticky=W)
        
        student_entry=ttk.Entry(student_info_frame,textvariable=self.var_std_id,width=20,font=("times of roman",10,"bold"))
        student_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        class_div_label = Label(student_info_frame,text="Enrollment No.",font=("times of roman",10,"bold"),bg="black",fg="white")
        class_div_label.grid(row=1,column=0,padx=40,pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(student_info_frame,textvariable=self.var_roll,width=20,font=("times of roman",10,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,sticky=W)
        
        email_label = Label(student_info_frame,text="Email ID",font=("times of roman",10,"bold"),bg="black",fg="white")
        email_label.grid(row=2,column=0,padx=40,sticky=W)
        
        email_entry=ttk.Entry(student_info_frame,textvariable=self.var_email,width=20,font=("times of roman",10,"bold"))
        email_entry.grid(row=2,column=1,padx=10,sticky=W)
        
        phone_label = Label(student_info_frame,text="Phone No.",font=("times of roman",10,"bold"),bg="black",fg="white")
        phone_label.grid(row=3,column=0,padx=40,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(student_info_frame,textvariable=self.var_phone,width=20,font=("times of roman",10,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,sticky=W)
        
        
        
        studentname_label = Label(student_info_frame,text="Student Name",font=("times of roman",10,"bold"),bg="black",fg="white")
        studentname_label.grid(row=0,column=2,padx=40,sticky=W)
        
        studentname_entry=ttk.Entry(student_info_frame,textvariable=self.var_std_name,width=20,font=("times of roman",10,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        dob_label = Label(student_info_frame,text="DOB",font=("times of roman",10,"bold"),bg="black",fg="white")
        dob_label.grid(row=1,column=2,padx=40,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(student_info_frame,textvariable=self.var_dob,width=20,font=("times of roman",10,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        gender_label = Label(student_info_frame,text="Gender",font=("times of roman",10,"bold"),bg="black",fg="white")
        gender_label.grid(row=2,column=2,padx=40,sticky=W)
        
        # gender_entry=ttk.Entry(student_info_frame,textvariable=self.var_gender,width=20,font=("times of roman",10,"bold"))
        # gender_entry.grid(row=2,column=3,padx=10,sticky=W)
        
        gender_combo=ttk.Combobox(student_info_frame,textvariable=self.var_gender,font=("times of roman",10,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=10,sticky=W)
        
        address_label = Label(student_info_frame,text="Address",font=("times of roman",10,"bold"),bg="black",fg="white")
        address_label.grid(row=3,column=2,padx=40,sticky=W)
        
        address_entry=ttk.Entry(student_info_frame,textvariable=self.var_address,width=20,font=("times of roman",10,"bold"))
        address_entry.grid(row=3,column=3,padx=10,sticky=W)
        
        
        radiobtn1=ttk.Radiobutton(student_info_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(student_info_frame,text="No Sample",variable=self.var_radiobtn1,value="No")
        radiobtn2.grid(row=5,column=1)
        
        btn_frame=Frame(student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=695,height=32)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=21,font=("times of roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=20,command=self.update_data,font=("times of roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",width=21,command=self.delete_data,font=("times of roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=21,command=self.reset_data,font=("times of roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=183,width=695,height=32)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo",command=self.generate_dataset,width=42,font=("times of roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo",width=42,font=("times of roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
         
        
        
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Details",font=("times of roman",25,"bold"),fg="white")
        Right_frame.place(x=760,y=20,width=720,height=580)
        
        img_right=Image.open("eye.jpg")
        img_right=img_right.resize((720,160),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_left)
        
        f_lbl_left=Label(Right_frame,image=self.photoimg_right)
        f_lbl_left.place(x=5,y=0, width= 710, height=130)
        
        
        Search_frame=LabelFrame(Right_frame,bd=2,bg="black",relief=RIDGE,text="Student Search",font=("times of roman",15,"bold"),fg="white")
        Search_frame.place(x=5,y=135,width=700,height=70)
        
        search_label = Label(Search_frame,text="Search by using :",font=("times of roman",10,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=20,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times of roman",10,"bold"),width=20,state="readonly")
        search_combo["values"]=("Select","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=20,font=("times of roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=5,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",width=10,font=("times of roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="Show All",width=10,font=("times of roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)
        
        table_frame=Frame(Right_frame,bd=2,bg="black",relief=RIDGE)
        table_frame.place(x=5,y=200,width=700,height=330)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","branch","year","sem","id","name","roll","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("branch",text="Branch")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")       
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo Sample")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("branch",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=200)        
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=250)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=250)
        self.student_table.column("photo",width=100)       
        self.student_table.pack(fill=BOTH,expand=1) 
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
        
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Tani6399",database="facerecog")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_branch.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_sem.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_radiobtn1.get()
                                                                                                                        
                    
                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Tani6399",database="facerecog")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_branch.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])    
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radiobtn1.set(data[12])
        
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@Tani6399",database="facerecog")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s, Branch=%s, Year=%s, Semester=%s, Name=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, PhotoSample=%s where Student_id=%s",(
                        
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_branch.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_radiobtn1.get(),
                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
            
    def delete_data(self):
        if self.var_std_id.get() =="":
            messagebox.showerror("Error", "Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete","Are you sure you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@Tani6399",database="facerecog")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
                    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_branch.set("Select Branch")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radiobtn1.set("")
        
        
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Tani6399",database="facerecog")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+1
                my_cursor.execute("Update student set Dep=%s, Branch=%s, Year=%s, Semester=%s, Name=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, PhotoSample=%s where Student_id=%s",(
                        
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_branch.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_radiobtn1.get(),
                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face=cv2.resize(face_cropped(my_frame),(450, 450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1) == 13 or int(img_id) ==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Dataset Generated Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
                            
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()     