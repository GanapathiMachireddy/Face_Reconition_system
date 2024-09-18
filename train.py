from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=('times new roman', 35, "bold"), bg='black', fg='blue')
        title_lbl.place(x=0, y=0, width=1366, height=60)

        img_top = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic4.jpeg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=300)

        b1_btn = Button(self.root, text="TRAIN DATA",command=self.train_classifier,font=("times new roman", 30, "bold"), bg="black", fg="blue", width=5)
        b1_btn.place(x = 0, y = 350,width = 1366,height = 50)


        img_bottom = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic15.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=400, width=1530, height=325)
    
    def train_classifier(self):
        data_dir = r"A:\Python\Python_Projects\data"
        path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # Gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        #================================== Train the classifier And Save====================================
        clf = cv2.face.LBPHFaceRecognizer_create()  # Ensure opencv-contrib-python is installed
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")










#main block
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
