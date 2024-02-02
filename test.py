from gettext import npgettext
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Trains:
    def __init__(self,root):
        self.root = root
        self.root.title("Student")
        self.root.geometry("1980x1080+0+0")
        
        
        img=Image.open("image1.jpg")
        img=img.resize((1600,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0)
        
        title_lbl=Label(self.root,text="Data Training Centre",font=("Roman",35,"bold"),bg = "blue",fg ="white")
        title_lbl.place(x=0,y=0,width=1520,height=70)
        
        main_frame=Frame(f_lbl,bd=2,bg="Red")
        main_frame.place(x=100,y=400,width=300,height=50)
        
        btn_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=300,height=50)
        
        save_btn=Button(btn_frame,text="Save",command=self.train_classifier,width=201,font=("times of roman",10,"bold"),bg="blue",fg="black")
        save_btn.grid(row=0,column=0)
        
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=npgettext.array(ids)
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data completed")
        
if __name__ == "__main__":
    root=Tk()
    obj=Trains(root)
    root.mainloop()     