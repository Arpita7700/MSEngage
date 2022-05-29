from tkinter import*
from tkinter import ttk
from turtle import up, update
from PIL import Image, ImageTk 
from tkinter import messagebox
from cv2 import waitKey
import mysql.connector
import cv2
import os
import numpy as np


class Training:
    def __init__(self,root):
        self.root=root
        self.root.geometry('18000x1050')
        self.root.title("Face Recognition")

        title_lbl=Label(self.root,text="||Train Data||",font=("times new roman",70,"bold"),bg="white",fg="blue") 
        title_lbl.place(x=0,y=0,width=1910,height=75)

        
        
        
        img1=Image.open(r"images\images (23).jpg")
        img1=img1.resize((650,250),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=75,width=650,height=250)

        img2=Image.open(r"images\images (23).jpg")
        img2=img2.resize((650,250),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=680,y=75,width=650,height=250)
        
        
        img3=Image.open(r"images\images (23).jpg")
        img3=img3.resize((650,250),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1360,y=75,width=650,height=250)

        img4=Image.open(r"images\download (8).jpg")
        img4=img4.resize((18000,1080),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=250,width=18000,height=1080)

        b1_1=Button(self.root,text="Train Data",cursor="hand2",command=self.train_class,font=("times new roman",35,"bold"),bg="white",fg="blue")
        b1_1.place(x=800,y=420,width=330,height=200)

    def train_class(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] 


        faces=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L')   #Gray Scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1]) 


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #Train Classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Successfully trained data",parent=self.root)

        







if __name__ == "__main__":
     root=Tk()
     obj=Training(root)
     root.mainloop()