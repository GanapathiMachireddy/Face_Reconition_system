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

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=('times new roman', 35, "bold"), bg='black', fg='blue')
        title_lbl.place(x=0, y=0, width=1366, height=50)

        img_top = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\pic8.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom1 = Image.open(r"A:\Python\Python_Projects\Face_reconigition_system.py\Project_img\px.jpg")
        img_bottom1 = img_bottom1.resize((680, 700), Image.LANCZOS)
        self.photoimg_bottom1 = ImageTk.PhotoImage(img_bottom1)

        f_lbl = Label(self.root, image=self.photoimg_bottom1)
        f_lbl.place(x=650, y=55, width=680, height=700)

        b1_btn = Button(command=self.face_recog, text="Face Recognition", cursor="hand2", font=("verdana", 18, "bold"), bg="white", fg="navyblue", width=5)
        b1_btn.place(x=840, y=560, width=300, height=40)

    #============================= Attendance Marking ======================================
    def mark_attendance(self, i, d, n, r):
        with open("ganesh.csv", "r+", newline="\n") as f:
            my_data_list = f.readlines()
            name_list = []
            for line in my_data_list:
                entry = line.split(",")
                name_list.append(entry[0])

            if i not in name_list and d not in name_list and n not in name_list and r not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")  # Corrected time format
                f.writelines(f"\n{i},{d},{n},{r},{dtString},{d1},Present")

    #============================= Face Recognition =========================================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict/300))

                # DB Connection once, then query
                conn = mysql.connector.connect(username='root', password='Ganesh@12', host='localhost', database='face_recognizer', port=3306)
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id = " + str(id))
                n = "+".join(my_cursor.fetchone())

                my_cursor.execute("select Roll from student where Student_id = " + str(id))
                r = "+".join(my_cursor.fetchone())

                my_cursor.execute("select Dept from student where Student_id = " + str(id))
                d = "+".join(my_cursor.fetchone())

                my_cursor.execute("select Student_id from student where Student_id = " + str(id))
                i = "+".join(my_cursor.fetchone())

                # Close DB connection after use
                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Department: {d}", (x, y-50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name: {n}", (x, y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll-No: {r}", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, d, n, r)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_Cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_Cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_Cap.release()
        cv2.destroyAllWindows()

# Main block
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
