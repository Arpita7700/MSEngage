from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk 
from criminal_details import Criminal_Details
from train import Training
from facedataa import Fr
import os



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry('18000x1050')
        self.root.title("Face Recognition System")


        #First image
        img4=Image.open(r"images\download (4).jpg")
        img4=img4.resize((650,250),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=650,height=250)

        #Second image
        img5=Image.open(r"images\download (2).jpg")
        img5=img5.resize((750,250),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_lbl=Label(self.root,image=self.photoimg5)
        f_lbl.place(x=650,y=0,width=750,height=250)

        #Third image
        img6=Image.open(r"images\img1.jpg")
        img6=img6.resize((750,250),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        f_lbl=Label(self.root,image=self.photoimg6)
        f_lbl.place(x=1350,y=0,width=750,height=250)
        

        # background image
        img=Image.open(r"images\download (8).jpg")
        img=img.resize((18000,1080),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=250,width=18000,height=1080)

        title_lbl=Label(bg_img,text="||Welcome to Security Data Center||",font=("times new roman",45,"bold"),bg="white",fg="black") 
        title_lbl.place(x=0,y=0,width=1910,height=75)

        # button1
        img1=Image.open(r"images\images (2).jpg")
        img1=img1.resize((330,220),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,command=self.criminal_details,cursor="hand2")
        b1.place(x=250,y=200,width=330,height=220)

        b1_1=Button(bg_img,text="Criminal Details",cursor="hand2",command=self.criminal_details,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=250,y=420,width=330,height=40)

        # button2
        img2=Image.open(r"images\images (11).jpg")
        img2=img2.resize((330,220),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_recog)
        b1.place(x=800,y=200,width=330,height=220)

        b1_1=Button(bg_img,text="Face Detection",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=420,width=330,height=40)

         # button3
        img3=Image.open(r"images\Face-recognition-technology.png")
        img3=img3.resize((330,220),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.train)
        b1.place(x=1380,y=200,width=330,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1380,y=420,width=330,height=40)


        # button4
        b1_1=Button(bg_img,text="Image Stock",cursor="hand2",command=self.open_img,font=("times new roman",25,"bold"),bg="black",fg="white")
        b1_1.place(x=1680,y=610,width=260,height=55)

        # button5
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",25,"bold"),bg="black",fg="red")
        b1_1.place(x=1680,y=665,width=260,height=55)

    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()

        else:
            return

    #funtion key
    def criminal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Criminal_Details(self.new_window)

    
    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Fr(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Training(self.new_window)





        




         



if __name__ == "__main__":
     root=Tk()
     obj=Face_Recognition_System(root)
     root.mainloop()

     