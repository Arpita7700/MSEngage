from tkinter import*
from tkinter import ttk
from turtle import up, update
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Fr:
    def __init__(self,root):
        self.root=root
        self.root.geometry('18000x1050')
        self.root.title("Face Recognition")

        title_lbl=Label(self.root,text="||Face Recognition||",font=("times new roman",70,"bold"),bg="white",fg="blue") 
        title_lbl.place(x=0,y=0,width=1910,height=75)

        img1=Image.open(r"images\images (5).jpg")
        img1=img1.resize((650,250),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=75,width=650,height=250)

        img2=Image.open(r"images\images (5).jpg")
        img2=img2.resize((650,250),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=680,y=75,width=650,height=250)
        
        
        img3=Image.open(r"images\images (5).jpg")
        img3=img3.resize((650,250),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1360,y=75,width=650,height=250)

        img4=Image.open(r"images\images (19).jpg")
        img4=img4.resize((1000,800),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        img4=Label(self.root,image=self.photoimg4)
        img4.place(x=0,y=325,width=1000,height=800)

        img5=Image.open(r"images\images (21).jpg")
        img5=img5.resize((1000,800),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        img5=Label(self.root,image=self.photoimg5)
        img5.place(x=950,y=325,width=1000,height=800)

        b1_1=Button(self.root,text="Face Recognition",cursor="hand2",command=self.face_recognition,font=("times new roman",35,"bold"),bg="black",fg="blue")
        b1_1.place(x=750,y=800,width=400,height=200)

       

    #Function
    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) 
                confidence=int((100*(1-predict/300)))


                conn = mysql.connector.connect(host="localhost", username="root", password="7700", database="msengage")
                my_cursor = conn.cursor()


                my_cursor.execute("select Name from criminaldatabase where Criminal_No="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Nation from criminaldatabase where Criminal_No="+str(id))
                j=my_cursor.fetchone()
                j="+".join(j)

                my_cursor.execute("select Charges from criminaldatabase where Criminal_No="+str(id))
                k=my_cursor.fetchone()
                k="+".join(k)

                

        

                if confidence>75:
                    cv2.putText(img,f"Name:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Nation:{j}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Charges:{k}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   
                
                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create() 
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)


        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognizer",img)


            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Fr(root)
    root.mainloop()