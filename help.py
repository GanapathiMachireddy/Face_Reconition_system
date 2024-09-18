from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

         #title section
        title_lb1 = Label(self.root,text="Help Disk",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=50)


# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\GANESH\Downloads\devloper.jpg")
        img=img.resize((1530,640),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=50,width=1530,height=640)

        dev_label = Label(f_lb1,text = "Contact info:",font = ('times new roman',18,'bold'),bg = 'white')
        dev_label.place(x = 550,y = 180)

        dev_label = Label(f_lb1,text = "Email:ganesh.energetic456@gmail.com",font = ('times new roman',18,'bold'),bg = 'white')
        dev_label.place(x = 550,y = 220)

        dev_label = Label(f_lb1,text = "9553461236",font = ('times new roman',18,'bold'),bg = 'white')
        dev_label.place(x = 550,y = 260)

        

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()