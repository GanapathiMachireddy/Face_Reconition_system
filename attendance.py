from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog


my_data = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #=================================Variable=============================
        
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

         # First image
        img1 = Image.open(r"C:\Users\GANESH\Downloads\Premium Photo _ College students studying on digital tablet preparing for exam or working on group project.jpeg")
        img1 = img1.resize((700, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=700, height=200)
     
        # Second image
        img2 = Image.open(r"C:\Users\GANESH\Downloads\Pre-Masters Programme In UK.jpeg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=700, y=0, width=800, height=200)

        # Background image
        img4 = Image.open(r"C:\Users\GANESH\OneDrive\Pictures\Saved Pictures\background_man.jpeg")
        img4 = img4.resize((1366, 768), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        Bg_img = Label(self.root, image=self.photoimg4)
        Bg_img.place(x=0, y=200, width=1366, height=768)

        title_lbl = Label(Bg_img, text="ATTENDANCE MANGEMENT SYSTEM", font=('times new roman', 35, "bold"), bg='white', fg='darkgreen')
        title_lbl.place(x=0, y=0, width=1366, height=50)

        main_frame = Frame(Bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1355, height=520)
        

         # Left side label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=630, height=370)   


          #Image inside left frame
        img_left = Image.open(r"C:\Users\GANESH\Downloads\Pre-Masters Programme In UK.jpeg")
        img_left = img_left.resize((620, 120), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=620, height=150)

        left_inside_frame = Frame(Left_frame,bd = 2,relief = RIDGE,bg = "white")
        left_inside_frame.place(x = 0,y =125 ,width = 625,height = 400)

        #labeland and entry

        #attendance id
        AttendanceId_label = Label(left_inside_frame, text="Attendance Id:", font=("verdana", 12, "bold"), bg="white",fg = 'navyblue')
        AttendanceId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        AttendanceId_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend, font=("verdana", 12, "bold"))
        AttendanceId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

         #Student Roll
        student_roll_label = Label(left_inside_frame,text="Roll.No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_roll,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_inside_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_name,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #Department
        #dep_label = Label(left_inside_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        #dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        #dep_entry = ttk.Entry(left_inside_frame,width=15,font=("verdana",12,"bold"))
        #dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)


        
         #time
        time_label = Label(left_inside_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_time,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_inside_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_date,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_inside_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_inside_frame,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=160, width=630, height=50)

        import_btn = Button(btn_frame, text="Import csv",command=self.importCsv,font=("verdana", 12, "bold"), bg="blue", fg="white", width=10)
        import_btn.grid(row=0, column=0,padx = 15,pady = 10,sticky = W)

        export_btn = Button(btn_frame, text="Export csv",command=self.exportCsv,font=("verdana", 12, "bold"), bg="blue", fg="white", width=10)
        export_btn.grid(row=0, column=1,padx = 15,pady = 10,sticky=W)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, font=("verdana", 12, "bold"), bg="blue", fg="white", width=10)
        update_btn.grid(row=0, column=2,padx = 15,pady = 10,sticky=W)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, font=("verdana", 12, "bold"), bg="blue", fg="white", width=10)
        reset_btn.grid(row=0, column=3,padx = 15,pady = 10,sticky=W)

        


         # Right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("verdana", 12, "bold"),fg = 'navyblue')
        Right_frame.place(x=650, y=10, width=600, height=500)

         # Button Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=580, height=330)

        #==================================Scrollbar table====================================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text = "Attendance ID")
        self.AttendanceReportTable.heading("roll",text = "Roll")
        self.AttendanceReportTable.heading("name",text = "Name")
        #self.AttendanceReportTable.heading("department",text = "Department")
        self.AttendanceReportTable.heading("time",text = "Time")
        self.AttendanceReportTable.heading("date",text = "Date")
        self.AttendanceReportTable.heading("attendance", text="Attend-status")
        self.AttendanceReportTable["show"] = "headings"


         # Set Width of Colums 
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)



        self.AttendanceReportTable.pack(fill=BOTH,expand = 1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor_left)


    #=============================Fetch data===============================================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,value=i)
    # import csv
    def importCsv(self):
        global my_data
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter= ",")
            for i in csvread:
                my_data.append(i)
            self.fetchData(my_data)
    
    #export csv
    def exportCsv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("NO Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

    
    def get_cursor_left(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]

        self.var_id.set(rows[0]),
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_time.set(rows[3]),
        self.var_date.set(rows[4]),
        self.var_attend.set(rows[5])  

    #=============================Update==================================

    def update_data(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



    def reset_data(self):
        self.var_id.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_attend.set("")  


            
     



        
        






        

 




































#main block
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
