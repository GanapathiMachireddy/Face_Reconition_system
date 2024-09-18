from tkinter import *
from tkinter import ttk
from train import Train
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

        # Title Section
        title_lb1 = Label(self.root, text="Developer Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Image Labels Setting Start
        # First Header Image
        img = Image.open(r"C:\Users\GANESH\Downloads\devloper.jpg")
        img = img.resize((1530, 640), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Set Image as Label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1530, height=640)

        main_frame = Frame(f_lb1, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=520)

        # Developer Image
        img_top1 = Image.open(r"C:\Users\GANESH\Downloads\Pre-Masters Programme In UK.jpeg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        # Developer Info
        dev_label1 = Label(main_frame, text="Hello, my name is Ganesh", font=('times new roman', 18, 'bold'), bg='white')
        dev_label1.place(x=0, y=50)

        dev_label2 = Label(main_frame, text="I am a Python developer", font=('times new roman', 18, 'bold'), bg='white')
        dev_label2.place(x=0, y=100)

        # Skills Section
        skills_label = Label(main_frame, text="Skills:", font=('times new roman', 18, 'bold'), bg='white')
        skills_label.place(x=0, y=160)

        skills_content = Label(main_frame, text="• Python\n• Java\n• Machine Learning\n• Web Development", font=('times new roman', 16), bg='white')
        skills_content.place(x=0, y=200)

        # Contact Section
        contact_label = Label(main_frame, text="Contact Me:", font=('times new roman', 18, 'bold'), bg='white')
        contact_label.place(x=0, y=300)

        contact_info = Label(main_frame, text="Email: ganesh.energetic456@gmail.com\nPhone: +91-9553461236", font=('times new roman', 13), bg='white')
        contact_info.place(x=0, y=340)

        # Social Media Buttons
        img_social = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic13.jpeg")
        img_social = img_social.resize((150, 100), Image.LANCZOS)
        self.photoimg_social = ImageTk.PhotoImage(img_social)

        social_label = Label(main_frame, text="Follow Me:", font=('times new roman', 18, 'bold'), bg='white')
        social_label.place(x=0, y=400)

        f_lbl_social = Label(main_frame, image=self.photoimg_social)
        f_lbl_social.place(x=0, y=440, width=100, height=50)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
