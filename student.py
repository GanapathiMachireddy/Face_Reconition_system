from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")


        #================variable==================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # First image
        img1 = Image.open(r"C:\Users\GANESH\Downloads\Premium Photo _ College students studying on digital tablet preparing for exam or working on group project.jpeg")
        img1 = img1.resize((450, 120), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=450, height=120)
     
        # Second image
        img2 = Image.open(r"C:\Users\GANESH\Downloads\Pre-Masters Programme In UK.jpeg")
        img2 = img2.resize((470, 120), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=450, y=0, width=470, height=120)

        # Third image
        img3 = Image.open(r"C:\Users\GANESH\Downloads\Group of college student laughing and studying togetherness.jpeg")
        img3 = img3.resize((470, 120), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=920, y=0, width=470, height=120) 
        # Background image
        img4 = Image.open(r"C:\Users\GANESH\OneDrive\Pictures\Saved Pictures\background_man.jpeg")
        img4 = img4.resize((1366, 768), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        Bg_img = Label(self.root, image=self.photoimg4)
        Bg_img.place(x=0, y=130, width=1366, height=768)

        title_lbl = Label(Bg_img, text="Student Management System", font=('times new roman', 35, "bold"), bg='white', fg='darkgreen')
        title_lbl.place(x=0, y=0, width=1366, height=50)

        main_frame = Frame(Bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1355, height=520)
        
        # Left side label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=500)   
 
        # Image inside left frame
        #img_left = Image.open(r"C:\Users\GANESH\Downloads\Pre-Masters Programme In UK.jpeg")
        #img_left = img_left.resize((620, 120), Image.LANCZOS)
        #self.photoimg_left = ImageTk.PhotoImage(img_left)

        #f_lbl = Label(Left_frame, image=self.photoimg_left)
        #f_lbl.place(x=5, y=0, width=650, height=120)

        # Current Course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"),fg='navyblue')
        current_course_frame.place(x=10, y=3, width=635, height=120) 

        # Department
        dep_label = Label(current_course_frame, text="Department", font=('verdana', 12, 'bold'), bg="white",fg = 'navyblue')  
        dep_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        #cambo box
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=('verdana', 12, 'bold'), width=15,state = 'readonly')
        dep_combo['values'] = ("Select Department", "Computers", "IT", "MCA", "MBA", "Mechanical", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Course
        course_label = Label(current_course_frame, text="Course", font=("verdana", 12, "bold"), bg="white",fg='navyblue')
        course_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,width = 15,font=("verrdana", 12, "bold"),state = 'readonly')
        course_combo['values'] = ("Select Course", "AI", "ML", "Data Science", "Cyber Security")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        year_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,width = 15,font=("verdana", 12, "bold"),state = 'readonly')
        year_combo['values'] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        semester_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester ,width = 15,font=('verdana', 12, "bold"),state = 'readonly')
        semester_combo['values'] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=10, sticky=W)
        
        # Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("verdana", 12, "bold"),fg = "navyblue")
        class_Student_frame.place(x=10, y=130, width=635, height=280) 

        # Student ID
        studentId_label = Label(class_Student_frame, text="StudentID:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15, font=("verdana", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        # Student Name 
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable = self.var_std_name, width=15, font=("verdana", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        
        # Class Division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue' )
        class_div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_div,width = 13,font=("verdana", 12, "bold"),state = 'readonly')
        div_combo['values'] = ("Select class division","A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)


        # Roll No 
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("verdana", 12, "bold"), bg="white",fg='navyblue')
        roll_no_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15, font=("verdana", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender 
        gender_label = Label(class_Student_frame, text="Gender:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width = 13,font=("verdana", 12, "bold"),state = 'readonly')
        gender_combo['values'] = ("Select Gender","Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # DOB 
        dob_label = Label(class_Student_frame, text="DOB:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15, font=("verdana", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email 
        email_label = Label(class_Student_frame, text="Email:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15, font=("verdana", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone 
        phone_label = Label(class_Student_frame, text="Phone No:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        phone_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=15, font=("verdana", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address 
        address_label = Label(class_Student_frame, text="Address:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address, width=15, font=("verdana", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher Name 
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("verdana", 12, "bold"), bg="white",fg = "navyblue")
        teacher_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15, font=("verdana", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)
        
        #radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,text = "Take Photo Sample",variable=self.var_radio1,value = "Yes")
        radionbtn1.grid(row=5,column=0,padx = 5,pady = 5,sticky=W)

        
        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text = "No photo Sample",value = "No")
        radionbtn2.grid(row = 5,column = 1)
        # Button Frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=200, width=630, height=50)

        save_btn = Button(btn_frame, text="Save",command=self.add_data,font=("verdana", 12, "bold"), bg="blue", fg="white", width=5)
        save_btn.grid(row=0, column=0,padx = 15,pady = 10,sticky = W)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, font=("verdana", 12, "bold"), bg="blue", fg="white", width=5)
        update_btn.grid(row=0, column=1,padx = 15,pady = 10,sticky=W)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, font=("verdana", 12, "bold"), bg="blue", fg="white", width=5)
        delete_btn.grid(row=0, column=2,padx = 15,pady = 10,sticky=W)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, font=("verdana", 12, "bold"), bg="blue", fg="white", width=5)
        reset_btn.grid(row=0, column=3,padx = 15,pady = 10,sticky=W)

        #btn_frame1 = Frame(class_Student_frame,bd = 2,relief = RIDGE,bg = "white")
        #btn_frame1.place(x = 10,y = 1,width = 630,height = 50)

        take_photo_btn = Button(btn_frame,command = self.generate_dataset,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="blue")
        take_photo_btn.grid(row=0,column=4,padx=10,pady=10,sticky=W)


        update_photo_btn = Button(btn_frame,text="Update Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="blue")
        update_photo_btn.grid(row=0,column=5,padx=10,pady=10,sticky=W)




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("verdana", 12, "bold"),fg = 'navyblue')
        Right_frame.place(x=680, y=10, width=660, height=500)

        # Search System
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("verdana", 12, "bold"),fg = 'navyblue')
        Search_frame.place(x=10, y=5, width=570, height=80)

        search_label = Label(Search_frame,text="Search By:", font=("verdana", 12, "bold"), bg="white", fg="navyblue")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("verdana", 12, "bold"), width=10, state="readonly")
        search_combo['values'] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=10, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        search_btn = Button(Search_frame, text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        search_btn.grid(row=0, column=3, padx=5,pady=10, sticky=W)

        showAll_btn = Button(Search_frame, text="Show All", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=10)
        showAll_btn.grid(row=0, column=4, padx=5,pady=10, sticky=W)


    
#------------------------------------------------------------------------------------------------------------------------------------------------------


        # Table Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=90, width=560, height=315)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("ID", "Name", "Dep", "Course", "Year", "Sem", "Div", "Roll", "Gender", "DOB", "Email", "Phone", "Address", "Teacher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="StudentID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Roll", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table["show"] = "headings"

        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        


    #=====================================Function Declaration=================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='Ganesh@12',host='localhost',database='face_recognizer',port=3306)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                 self.var_std_id.get(),
                 self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Sucessfully!",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    #=========================================Fetch data===========================================================
    def fetch_data(self): 
        conn = mysql.connector.connect(username='root', password='Ganesh@12',host='localhost',database='face_recognizer',port=3306)
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
   
    #======================================get cursor==================================================================================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data =content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #=============================update function=========================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)

                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='Ganesh@12',host='localhost',database='face_recognizer',port=3306)
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name= %s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                           
                                                                                                                                                                                           self.var_dep.get(),
                                                                                                                                                                                           self.var_course.get(),
                                                                                                                                                                                           self.var_year.get(),
                                                                                                                                                                                           self.var_semester.get(),
                                                                                                                                                                                           self.var_std_name.get(),
                                                                                                                                                                                           self.var_div.get(),
                                                                                                                                                                                           self.var_roll.get(),
                                                                                                                                                                                           self.var_gender.get(),
                                                                                                                                                                                           self.var_dob.get(),
                                                                                                                                                                                           self.var_email.get(),
                                                                                                                                                                                           self.var_phone.get(),
                                                                                                                                                                                           self.var_address.get(),
                                                                                                                                                                                           self.var_teacher.get(),
                                                                                                                                                                                           self.var_radio1.get(),
                                                                                                                                                                                           self.var_std_id.get()

                                                                                                                                                                                                           ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details succesfully update completed",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


    

# ======================================Delete function=============================================================================

    def delete_data(self):
        if self.var_std_id.get()== "":
            messagebox.showerror("Error","studet id must be required",parent = self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student",parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(username='root', password='Ganesh@12',host='localhost',database='face_recognizer',port=3306)
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    

#===============================Reset===============================================================================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

   
#======================================= Generate data set Or Take photo samples=============================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='Ganesh@12',host='localhost',database='face_recognizer',port=3306)
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name= %s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                           
                                                                                                                                                                                           self.var_dep.get(),
                                                                                                                                                                                           self.var_course.get(),
                                                                                                                                                                                           self.var_year.get(),
                                                                                                                                                                                           self.var_semester.get(),
                                                                                                                                                                                           self.var_std_name.get(),
                                                                                                                                                                                           self.var_div.get(),
                                                                                                                                                                                           self.var_roll.get(),
                                                                                                                                                                                           self.var_gender.get(),
                                                                                                                                                                                           self.var_dob.get(),
                                                                                                                                                                                           self.var_email.get(),
                                                                                                                                                                                           self.var_phone.get(),
                                                                                                                                                                                           self.var_address.get(),
                                                                                                                                                                                           self.var_teacher.get(),
                                                                                                                                                                                           self.var_radio1.get(),
                                                                                                                                                                                           self.var_std_id.get()

                                                                                                                                                                                                           ))

                    

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

            except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}")        
            #======================Load predefined data on face frontals from Opencv==============


                    # Load the Haarcascade classifier
        face_classifier = cv2.CascadeClassifier(r"A:\Python\Python_Projects\Face_reconigition_system.py\haarcascade_frontalface_default.xml")
                    
                    # Ensure the classifier was loaded properly
        if face_classifier.empty():
            raise Exception("Error loading haarcascade_frontalface_default.xml file.")
                    
        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
            if len(faces) == 0:
                return None
            
            for (x, y, w, h) in faces:
                face_cropped = img[y:y+h, x:x+w]
                return face_cropped
        
        try:
            cap = cv2.VideoCapture(0)
            img_id = 0
        
            while True:
                ret, my_frame = cap.read()
        
                if not ret:
                    break  # If the frame is not captured properly, break the loop
                
                cropped_face = face_cropped(my_frame)
        
                # Check if a face was detected
                if cropped_face is not None:
                    img_id += 1
                    face = cv2.resize(cropped_face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    
                    file_name_path = f"data/user.{str(id)}.{str(img_id)}.jpg"
                    cv2.imwrite(file_name_path, face)
                    
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                else:
                    print("No face detected in this frame.")
        
                # Exit on pressing 'Enter' or after saving 100 images
                if cv2.waitKey(1) == 13 or img_id == 100:
                    break
        
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating datasets completed!!!")
        
        except Exception as es:
           messagebox.showerror("Error", f"Due To: {str(es)}")      


#main block
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()