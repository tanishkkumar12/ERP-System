import os
import tkinter as tk
from tkinter import PhotoImage, Toplevel
import cv2
from PIL import Image, ImageTk
from student import Student
from train import Trains
from face_recognition import Face_recognition

class VideoBackgroundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Background Example")

        # Load video using OpenCV
        self.video_capture = cv2.VideoCapture("video.mov")
        self.current_frame = None

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Create a Canvas widget that fills the entire window
        self.canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        self.canvas.pack()

        self.title_label = tk.Label(root, text="AI Smart EYE System", font=("Helvetica", 16),bg="red", fg="black")
        self.title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Load an image to use as a button
        self.button_image = Image.open("stuimg.jpg")
        self.button_image = self.button_image.resize((200, 200), Image.ANTIALIAS)  
        self.button_image_tk = ImageTk.PhotoImage(self.button_image)

        # Create a Button widget using the image
        self.button = tk.Button(root, image=self.button_image_tk, command=self.Student_details, bd=0, bg="white")
        self.button.place(x=100, y=130)
        
        self.button = tk.Button(root, text="Student Portal",  command=self.Student_details, bd=0, bg="white")
        self.button.place(x=100, y=310,width=202)
        
        self.button0_image = Image.open("facere.jpg")
        self.button0_image = self.button0_image.resize((200, 200), Image.ANTIALIAS)  
        self.button0_image_tk = ImageTk.PhotoImage(self.button0_image)

        self.button0 = tk.Button(root, image=self.button0_image_tk,command=self.face_data, bd=0, bg="white")
        self.button0.place(x=100, y=360)
        
        self.button_0 = tk.Button(root, text="Face Recognizer",command=self.face_data, bd=0, bg="white")
        self.button_0.place(x=100, y=540,width=202)

        self.button1_image = Image.open("attimg.jpeg")
        self.button1_image = self.button1_image.resize((200, 200), Image.ANTIALIAS)  
        self.button1_image_tk = ImageTk.PhotoImage(self.button1_image)

        self.button1 = tk.Button(root, image=self.button1_image_tk, bd=0, bg="white")
        self.button1.place(x=100, y=590)  # Adjust the position as needed
        
        self.button_1 = tk.Button(root, text="Attendance", bd=0, bg="white")
        self.button_1.place(x=100, y=770,width=202)
        
        self.button2_image = Image.open("image1.jpg")
        self.button2_image = self.button2_image.resize((200, 200), Image.ANTIALIAS)
        self.button2_image_tk = ImageTk.PhotoImage(self.button2_image)

        self.button2 = tk.Button(root, image=self.button2_image_tk, bd=0, bg="white")
        self.button2.place(x=1250, y=130)  # Adjust the position as needed
        
        self.button_2 = tk.Button(root, text="Help desk", bd=0, bg="white")
        self.button_2.place(x=1250, y=310,width=202)
        
        self.button3_image = Image.open("trainimg.webp")
        self.button3_image = self.button3_image.resize((200, 200), Image.ANTIALIAS) 
        self.button3_image_tk = ImageTk.PhotoImage(self.button3_image)

        self.button3 = tk.Button(root, image=self.button3_image_tk,command=self.train_d, bd=0, bg="white")
        self.button3.place(x=1250, y=360)  # Adjust the position as needed
        
        self.button_3 = tk.Button(root, text="Train Data",command=self.train_d, bd=0, bg="white")
        self.button_3.place(x=1250, y=540,width=202)

        self.button4_image = Image.open("img3.jpg")
        self.button4_image = self.button4_image.resize((200, 200), Image.ANTIALIAS)  # Resize the image
        self.button4_image_tk = ImageTk.PhotoImage(self.button4_image)

        self.button4 = tk.Button(root, image=self.button4_image_tk,command=self.open_img, bd=0, bg="white")
        self.button4.place(x=1250, y=590)  # Adjust the position as needed
        
        self.button_4 = tk.Button(root, text="Photos",command=self.open_img, bd=0, bg="white")
        self.button_4.place(x=1250, y=770,width=202)
        
        self.button_n = tk.Button(root, text="Exit",font=("times of roman", 12, "bold"), bg="white")
        self.button_n.place(x=1440, y=20,width=70)


        self.update_video()
    #----------------------------------------------------------------    
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_d(self):
        self.new_window=Toplevel(self.root)
        self.app=Trains(self.new_window)
        
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
   #----------------------------------------------------------------
        
    def open_img(self):
        os.startfile("data")
        
   #----------------------------------------------------------------
    def update_video(self):
        ret, frame = self.video_capture.read()

        if ret:
            # Resize the frame to fit the screen
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            resized_frame = cv2.resize(frame, (screen_width, screen_height))

            self.current_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.current_frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.root.after(10, self.update_video)  # Update every 10 milliseconds
        else:
            # Reset video to the beginning for looping
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.update_video()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Set the window to full screen
    app = VideoBackgroundApp(root)
    app.run()
