from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Face Recognition System")

        # First image
        img1 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic1.jpeg")
        img1 = img1.resize((550, 120), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=450, height=120)

        # Second image
        img2 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic2.gif")
        img2 = img2.resize((500, 120), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=450, y=0, width=470, height=120)

        # Third image
        img3 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic3.jpeg")
        img3 = img3.resize((500, 120), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=850, y=0, width=470, height=120)

        # Background image
        img4 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic4.jpeg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        Bg_img = Label(self.root, image=self.photoimg4)
        Bg_img.place(x=0, y=100, width=1530, height=710)

        title_lbl = Label(Bg_img, text="Face Recognition System", font=('times new roman', 35, "bold"), bg='blue', fg='white')
        title_lbl.place(x=100, y=0, width=1050, height=75)

        #======================================Time=========================================================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_lbl,font = ('times new roman',14,'bold'),background = 'white',foreground = 'blue')
        lbl.place(x = 0, y =0,width = 110,height = 70)
        time()






        # Student button
        img5 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic5.jpg")
        img5 = img5.resize((200,200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(Bg_img, image=self.photoimg5, command=self.student_details, cursor="hand1")
        b1.place(x=100, y=125, width=185, height=185)
        
        b1_1 = Button(Bg_img, cursor='hand2', text='Student Details', command=self.student_details, font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        b1_1.place(x=100, y=125, width=185, height=30)

        # Face Detection button
        img6 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic6.jpeg")
        img6 = img6.resize((200,200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b2 = Button(Bg_img, image=self.photoimg6, cursor="hand1",command=self.face_data)
        b2.place(x=380, y=125, width=185, height=185)
        
        b2_2 = Button(Bg_img, cursor='hand2', text='Face Detector', font=('times new roman', 15, "bold"), bg='darkblue', fg='white',command=self.face_data)
        b2_2.place(x=380, y=125, width=185, height=30)

        # Attendance button
        img7 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic8.jpg")
        img7 = img7.resize((200,200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b2 = Button(Bg_img, image=self.photoimg7, cursor="hand1",command=self.attendance_data)
        b2.place(x=675, y=125, width=185, height=185)
        
        b2_2 = Button(Bg_img, cursor='hand2', text='Attendance',command=self.attendance_data, font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        b2_2.place(x=675, y=125, width=185, height=30)

        # Help Desk button
        img12 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic10.jpg")
        img12 = img12.resize((200,200), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        
        b2 = Button(Bg_img, image=self.photoimg12, cursor="hand1")
        b2.place(x=975, y=125, width=185, height=185)
        
        b2_2 = Button(Bg_img, cursor='hand2', text='Help Desk',command=self.help_data,font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        b2_2.place(x=975, y=125, width=185, height=30)

        # Train Data Button
        img8 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic9.jpg")
        img8 = img8.resize((200,200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b2 = Button(Bg_img, image=self.photoimg8, cursor="hand1",command=self.train_data)
        b2.place(x=100, y=350, width=185, height=185)
        
        b2_2 = Button(Bg_img, cursor='hand2', text='Train Data', font=('times new roman', 15, "bold"), bg='darkblue', fg='white',command=self.train_data)
        b2_2.place(x=100, y=350, width=185, height=30)

        # Photos Button
        img9 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic12.jpeg")
        img9 = img9.resize((200,200), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b2 = Button(Bg_img, image=self.photoimg9, cursor="hand1",command=self.open_img)
        b2.place(x=380, y=350, width=185, height=185)
        
        b2_2 = Button(Bg_img, cursor='hand2',command=self.open_img, text='Photos', font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        b2_2.place(x=380, y=350, width=185, height=30)

        # Developer Button
        img10 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic13.jpeg")
        img10 = img10.resize((200,200), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b2 = Button(Bg_img, image=self.photoimg10, cursor="hand1",command=self.developer_data)
        b2.place(x=675, y=350, width=185, height=185)
        
        b2_2 = Button(Bg_img, cursor='hand2', text='Developer',command=self.developer_data, font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        b2_2.place(x=675, y=350, width=185, height=30)

        # Exit face Button
        img11 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic14.jpeg")
        img11 = img11.resize((200,200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b2 = Button(Bg_img, image=self.photoimg11, cursor="hand1",command=self.iExit)
        b2.place(x=975, y=350, width=185, height=185)
        
        b2_2 = Button(Bg_img, cursor='hand2', text='Exit',command=self.iExit,font=('times new roman', 15, "bold"), bg='darkblue', fg='white')
        b2_2.place(x=975, y=350, width=185, height=30)
        
    def open_img(self):
        os.startfile("data")


    # Method to handle student details
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # Method to handle student details
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

     
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition","Are you sure to Exit",parent = self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()
