from tkinter import*
from tkinter import messagebox
import os
import mysql.connector 
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import numpy as np


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition")
        self.root.geometry("1530x790+0+0")
        
        title_label = Label(self.root, text="Face Recognition Mode", font=("Helvetica", 26),bg="lightsteelblue", fg="brown")
        title_label.place(x=0,y=0,width=1530,height=55)
        
        img_top = Image.open("image3.jpeg")
        img_top = img_top.resize((1530,735),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=735)
        
        b1_1=Button(f_lbl,text="Recognize",cursor="hand2",command=self.face_recog,font=("Helvetica",20,"bold"),bg="dimgrey",fg="black")
        b1_1.place(x=1200,y=600,width=200,height=40)
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="@Tani6399",database="facerecog")
                my_cursor=conn.cursor()
                    
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                if confidence > 77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
                 
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Facial Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                    
        
        
if __name__ == "__main__":
    root = Tk()
    obj=Face_recognition(root)
    root.mainloop()