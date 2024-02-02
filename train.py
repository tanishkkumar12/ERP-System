from tkinter import*
from tkinter import messagebox
import os
import tkinter as ttk
from tkinter import PhotoImage, Toplevel
import cv2
from PIL import Image, ImageTk
import numpy as np


class Trains:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Background Example")

        # Load video using OpenCV
        self.video_capture = cv2.VideoCapture("img5.jpg")
        self.current_frame = None

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Create a Canvas widget that fills the entire window
        self.canvas = ttk.Canvas(root, width=screen_width, height=screen_height)
        self.canvas.pack()

        self.title_label = ttk.Label(root, text="Data Training", font=("Helvetica", 26),bg="brown", fg="black")
        self.title_label.place(relx=0.5, rely=0.1, anchor=ttk.CENTER)

        # Load an image to use as a button
        
        # Create a Button widget using the image
        # self.button = tk.Button(root, bd=0, bg="white")
        # self.button.place(x=100, y=130)
        
        self.button_n = ttk.Button(root, text="Train Data",command=self.train_classifier,font=("times of roman",20,"bold"), bg="red")
        self.button_n.place(x=1070, y=680,width=202)
        
         
        self.update_video()
        
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
        ids=np.array(ids)
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data completed")
        

   
    def update_video(self):
        ret, frame = self.video_capture.read()

        if ret:
            # Resize the frame to fit the screen
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            resized_frame = cv2.resize(frame, (screen_width, screen_height))

            self.current_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.current_frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=ttk.NW)
            self.root.after(10, self.update_video)  # Update every 10 milliseconds
        else:
            # Reset video to the beginning for looping
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.update_video()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = ttk.Tk()
    root.attributes("-fullscreen", True)
    app = Trains(root)
    app.run()
