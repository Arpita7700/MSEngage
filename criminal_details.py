from email.mime import message
from optparse import Values
from tkinter import*
from tkinter import ttk
from turtle import up, update
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2


class Criminal_Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry('18000x1050')
        self.root.title("Criminal Details")

        #Variables
        self.var_Nation=StringVar()
        self.var_Age=StringVar()
        self.var_Criminal_No=StringVar()
        self.var_Name=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Address=StringVar()
        self.var_Contact=StringVar()
        self.var_Charges=StringVar()
        self.var_Ay=StringVar()
        self.var_Ry=StringVar()
        



        #First image
        img=Image.open(r"images\detail.jpg")
        img=img.resize((550,250),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=550,height=250)

        #Second image
        img1=Image.open(r"images\images (3).jpg")
        img1=img1.resize((550,250),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=550,height=250)

        #Third image
        img2=Image.open(r"images\images (10).jpg")
        img2=img2.resize((575,250),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=575,height=250)

        #Fourth image
        img3=Image.open(r"images\images (13).jpg")
        img3=img3.resize((550,250),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1400,y=0,width=550,height=250)


        # background image
        img4=Image.open(r"images\download (8).jpg")
        img4=img4.resize((18000,1080),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=250,width=18000,height=1080)

        title_lbl=Label(bg_img,text="||Criminal Record||",font=("times new roman",45,"bold"),bg="white",fg="black") 
        title_lbl.place(x=0,y=0,width=1910,height=75)


        #Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=100,y=150,width=1700,height=530)

        #Left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Criminal Details",font=("times new roman",22,"bold")) 
        Left_frame.place(x=20,y=10,width=820,height=510)

        img_left=Image.open(r"images\detail.jpg")
        img_left=img_left.resize((820,50),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=820,height=55)

        #Essentials
        Essentials_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Essentials",font=("times new roman",22,"bold")) 
        Essentials_frame.place(x=10,y=55,width=780,height=100)

        Nation_label=Label(Essentials_frame,text="Nationality     ",font=("times new roman",18,"bold")) 
        Nation_label.grid(row=0,column=0,padx=10)

        Nation_combo=ttk.Combobox(Essentials_frame,textvariable=self.var_Nation,font=("times new roman",18,"bold"),state="readonly",width=14)  
        Nation_combo["values"]=("Australia","Bangladesh","China","England","India","Japan","Nepal","Pakistan")
        Nation_combo.current() 
        Nation_combo.grid(row=0,column=1,padx=10,pady=10)

        #Age
        
        Age_label=Label(Essentials_frame,text="Age Status      ",font=("times new roman",18,"bold")) 
        Age_label.grid(row=0,column=5,padx=10)

        Age_combo=ttk.Combobox(Essentials_frame,textvariable=self.var_Age,font=("times new roman",18,"bold"),state="readonly",width=14)  
        Age_combo["values"]=("Adult","Minor")
        Age_combo.current() 
        Age_combo.grid(row=0,column=7,padx=10,pady=10)


        #Basic Information
        Basic_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Basic Details",font=("times new roman",18,"bold")) 
        Basic_frame.place(x=10,y=160,width=780,height=315)

        #Criminal No.
        Criminal_No_label=Label(Basic_frame,text="Criminal No.",font=("times new roman",18,"bold")) 
        Criminal_No_label.grid(row=0,column=0,padx=10)

        Criminal_No_entry=ttk.Entry(Basic_frame,textvariable=self.var_Criminal_No,width=20,font=("times new roman",13,"bold"))
        Criminal_No_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        Name_label=Label(Basic_frame,text="Name             ",font=("times new roman",18,"bold")) 
        Name_label.grid(row=1,column=0,padx=10)

        Name_entry=ttk.Entry(Basic_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        Name_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        Gender_label=Label(Basic_frame,text="Gender          ",font=("times new roman",18,"bold")) 
        Gender_label.grid(row=2,column=0,padx=10)

        Gender_combo=ttk.Combobox(Basic_frame,textvariable=self.var_Gender,font=("times new roman",18,"bold"),state="readonly",width=14)  
        Gender_combo["values"]=("Male","Female","Others")
        Gender_combo.current() 
        Gender_combo.grid(row=2,column=3,padx=10,pady=5)


        #DOB
        DOB_label=Label(Basic_frame,text="Date of Birth",font=("times new roman",18,"bold")) 
        DOB_label.grid(row=3,column=0,padx=10)

        DOB_entry=ttk.Entry(Basic_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        Address_label=Label(Basic_frame,text="Address          ",font=("times new roman",18,"bold")) 
        Address_label.grid(row=4,column=0,padx=10)

        Address_entry=ttk.Entry(Basic_frame,textvariable=self.var_Address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #Contact Details
        Contact_label=Label(Basic_frame,text="Contact(if any) ",font=("times new roman",18,"bold")) 
        Contact_label.grid(row=0,column=4,padx=10)

        Contact_entry=ttk.Entry(Basic_frame,textvariable=self.var_Contact,width=20,font=("times new roman",13,"bold"))
        Contact_entry.grid(row=0,column=6,padx=10,pady=5,sticky=W)

        #Charges
        Charges_label=Label(Basic_frame,text="Charges            ",font=("times new roman",18,"bold")) 
        Charges_label.grid(row=1,column=4,padx=10)

        Charges_entry=ttk.Entry(Basic_frame,textvariable=self.var_Charges,width=20,font=("times new roman",13,"bold"))
        Charges_entry.grid(row=1,column=6,padx=10,pady=5,sticky=W)

        #Year of Arrest
        Ay_label=Label(Basic_frame,text="Year of Arrest ",font=("times new roman",18,"bold")) 
        Ay_label.grid(row=2,column=4,padx=10)

        Ay_entry=ttk.Entry(Basic_frame,textvariable=self.var_Ay,width=20,font=("times new roman",13,"bold"))
        Ay_entry.grid(row=2,column=6,padx=10,pady=5,sticky=W)

        #Year of Release
        Ry_label=Label(Basic_frame,text="Year of Release",font=("times new roman",18,"bold")) 
        Ry_label.grid(row=3,column=4,padx=10)

        Ry_entry=ttk.Entry(Basic_frame,textvariable=self.var_Ry,width=20,font=("times new roman",13,"bold"))
        Ry_entry.grid(row=3,column=6,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(Basic_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)

        radionbtn2=ttk.Radiobutton(Basic_frame,variable=self.var_radio1,text="N0 Photo Sample",value="No")
        radionbtn2.grid(row=5,column=3)
        

        #buttons frame 1
        btn_frame=Frame(Basic_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=770,height=37)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
                                       

        delete_btn=Button(btn_frame,text="Delete",width=19,command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        #buttons frame 2
        btn1_frame=Frame(Basic_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=237,width=770,height=37)

        Take_photo_btn=Button(btn1_frame,text="Take Photo",command=self.generate_data,width=76,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=1,column=3)

    


                                       
                                       
                                        
         #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Query",font=("times new roman",22,"bold")) 
        Right_frame.place(x=860,y=10,width=830,height=510)

        img_right=Image.open(r"C:\Users\Arpita\Desktop\MS Engage\images\detail.jpg")
        img_right=img_right.resize((830,50),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=830,height=50)

        #Query System
        Query_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",22,"bold")) 
        Query_frame.place(x=10,y=55,width=780,height=100)

        Search_label=Label(Query_frame,text="Search By:",font=("times new roman",18,"bold"),bg="blue") 
        Search_label.grid(row=0,column=0,padx=10)

        Search_combo=ttk.Combobox(Query_frame,font=("times new roman",12,"bold"),state="readonly",width=10)  
        Search_combo["values"]=("Criminal_No","Name","Charges")
        Search_combo.current() 
        Search_combo.grid(row=0,column=1,padx=10,pady=10)

        Search_entry=ttk.Entry(Query_frame,width=20,font=("times new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        Search_btn=Button(Query_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=2)

        Show_all_btn=Button(Query_frame,text="Show All",command=self.fetch_data,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Show_all_btn.grid(row=0,column=4,padx=2)

        #Table
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE) 
        Table_frame.place(x=10,y=160,width=780,height=300)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.criminaldatabase_table=ttk.Treeview(Table_frame,column=("Nation","Age","Criminal_No","Name","Gender","DOB","Address","Contact","Charges","Ay","Ry"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.criminaldatabase_table.xview)
        scroll_y.config(command=self.criminaldatabase_table.yview)

        self.criminaldatabase_table.heading("Nation",text="Nation")
        self.criminaldatabase_table.heading("Age",text="Age Status")
        self.criminaldatabase_table.heading("Criminal_No",text="Criminal_No")
        self.criminaldatabase_table.heading("Name",text="Name")
        self.criminaldatabase_table.heading("Gender",text="Gender")
        self.criminaldatabase_table.heading("DOB",text="DOB")
        self.criminaldatabase_table.heading("Address",text="Address")
        self.criminaldatabase_table.heading("Charges",text="Charges")
        self.criminaldatabase_table.heading("Ay",text="Year of Arrest")
        self.criminaldatabase_table.heading("Ry",text="Year of Release")
        self.criminaldatabase_table.heading("Contact",text="Contact")
        
        self.criminaldatabase_table["show"]="headings"

        self.criminaldatabase_table.column("Nation",width=100)
        self.criminaldatabase_table.column("Age",width=100)
        self.criminaldatabase_table.column("Criminal_No",width=100)
        self.criminaldatabase_table.column("Name",width=100)
        self.criminaldatabase_table.column("Gender",width=100)
        self.criminaldatabase_table.column("DOB",width=100)
        self.criminaldatabase_table.column("Address",width=100)
        self.criminaldatabase_table.column("Contact",width=100)
        self.criminaldatabase_table.column("Charges",width=100)
        self.criminaldatabase_table.column("Ay",width=100)
        self.criminaldatabase_table.column("Ry",width=100)




        self.criminaldatabase_table.pack(fill=BOTH,expand=1)
        self.criminaldatabase_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Function Declaration
    def add_data(self):
        if self.var_Criminal_No.get() == "" or self.var_Name.get() == "" or self.var_Charges.get() == "" or self.var_Age.get() == "" or self.var_Nation.get() == "":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:  
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="7700", database="msengage")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into criminaldatabase Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                            self.var_Nation.get(),
                                                                                                            self.var_Age.get(),                                                                                               
                                                                                                            self.var_Criminal_No.get(),
                                                                                                            self.var_Name.get(),
                                                                                                            self.var_Gender.get(),
                                                                                                            self.var_DOB.get(),
                                                                                                            self.var_Address.get(),
                                                                                                            self.var_Contact.get(),
                                                                                                            self.var_Charges.get(),
                                                                                                            self.var_Ay.get(),
                                                                                                            self.var_Ry.get()                                                                                                            
                                                                                                            
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Information successfully added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #Fetch Data Function
    def fetch_data(self):
                conn = mysql.connector.connect(host="localhost", username="root", password="7700", database="msengage")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from criminaldatabase")
                data=my_cursor.fetchall()

                if len(data)!=0:
                    self.criminaldatabase_table.delete(*self.criminaldatabase_table.get_children())
                    for i in data:
                        self.criminaldatabase_table.insert("",END,values=i)
                    conn.commit()
                conn.close()   
    

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.criminaldatabase_table.focus()
        content=self.criminaldatabase_table.item(cursor_focus)
        data=content["values"]

        self.var_Nation.set(data[0]),
        self.var_Age.set(data[1]),
        self.var_Criminal_No.set(data[2]),
        self.var_Name.set(data[3]),
        self.var_Gender.set(data[4]),
        self.var_DOB.set(data[5]),
        self.var_Address.set(data[6]),
        self.var_Contact.set(data[7]),
        self.var_Charges.set(data[8]),
        self.var_Ay.set(data[9]),
        self.var_Ry.set(data[10])


    #Update Function
    def update_data(self):
        if self.var_Criminal_No.get() == "" or self.var_Name.get() == "" or self.var_Charges.get() == "" or self.var_Age.get() == "" or self.var_Nation.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("update","Do you want to update the information?",parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="7700", database="msengage")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update Criminaldatabase set Nation=%s,Age=%s,Name=%s,Gender=%s,DOB=%s,Address=%s,Contact=%s,Charges=%s,Ay=%s,Ry=%s where Criminal_No=%s",(
                                                                                                                                                                                            
                                                                                                                                                                                    self.var_Nation.get(),
                                                                                                                                                                                    self.var_Age.get(),
                                                                                                                                                                                    self.var_Criminal_No.get(),
                                                                                                                                                                                    self.var_Name.get(),
                                                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                                                    self.var_Address.get(),
                                                                                                                                                                                    self.var_Contact.get(),
                                                                                                                                                                                    self.var_Charges.get(),
                                                                                                                                                                                    self.var_Ay.get(),
                                                                                                                                                                                    self.var_Ry.get()
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                ))
                else:
                    if not Upadate:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_Criminal_No.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete the information?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="7700", database="msengage")                             
                    sql="delete from criminaldatabase where Criminal_No=%s"
                    val=(self.var_Criminal_No.get(),)
                    my_cursor = conn.cursor()
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #Reset Function
    def reset_data(self):
        self.var_Nation.set("")
        self.var_Age.set("")
        self.var_Criminal_No.set("")
        self.var_Name.set("")
        self.var_Gender.set("")
        self.var_DOB.set("")
        self.var_Address.set("")
        self.var_Contact.set("")
        self.var_Charges.set("")
        self.var_Ay.set("")
        self.var_Ry.set("")

    #Image Data Generation
    def generate_data(self):
        if self.var_Criminal_No.get() == "" or self.var_Name.get() == "" or self.var_Charges.get() == "" or self.var_Age.get() == "" or self.var_Nation.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="7700",database="msengage")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from criminaldatabase")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update Criminaldatabase set Nation=%s,Age=%s,Name=%s,Gender=%s,DOB=%s,Address=%s,Contact=%s,Charges=%s,Ay=%s,Ry=%s where Criminal_No=%s",(
                                                                                                                                                                                            
                                                                                                                                                                                    self.var_Nation.get(),
                                                                                                                                                                                    self.var_Age.get(),                                                                                                                                                                                    
                                                                                                                                                                                    self.var_Name.get(),
                                                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                                                    self.var_Address.get(),
                                                                                                                                                                                    self.var_Contact.get(),
                                                                                                                                                                                    self.var_Charges.get(),
                                                                                                                                                                                    self.var_Ay.get(),
                                                                                                                                                                                    self.var_Ry.get(),
                                                                                                                                                                                    self.var_Criminal_No.get()==id+1
                                                                                                                                                                                ))                                                                                                                                                                                                      
                                                                                                                                                                            
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #Load Predefined data on face frontals

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h)in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)is not None:
                        img_id+=1  
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data")
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)





if __name__ == "__main__":
     root=Tk()
     obj=Criminal_Details(root)
     root.mainloop()

