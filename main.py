from tkinter import *
from tkinter import ttk     #to display better
import sqlite3
from tkinter import messagebox
import re             #re- regular expression

root=Tk()
root.geometry("500x500+100+100")
root.config(bg='maroon')


# working with frame to display output in same window

frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)
frame5=Frame(root)
frame6=Frame(root)
frame1.config(bg='maroon')
frame2.config(bg='maroon')
frame3.config(bg='maroon')
frame4.config(bg='maroon')
frame5.config(bg='maroon')
frame6.config(bg='maroon')
frame1.grid(row=0,column=0,padx=90, pady=40)
frame2.grid(row=0,column=0,padx=90, pady=40)
frame3.grid(row=0,column=0,padx=90, pady=40)
frame4.grid(row=0,column=0,padx=90, pady=40)
frame5.grid(row=0,column=0,padx=90, pady=40)
frame6.grid(row=0,column=0,padx=90, pady=40)


#to store the value that is entered in the ENTRY box
str1=StringVar()
str2=StringVar()

#funciton to raise the tkinter or frame window
def dashboard(frame):
    frame.tkraise()
    
#looping throug frame
for frame in (frame1,frame2,frame3,frame4,frame5,frame6):
    frame.grid(row=0,column=0,sticky='news')

#connecting to the sql data bse
db = sqlite3.connect("D:\my_project\mprescribe.db")    
cursor1 =db.cursor()                  

#creating the cursor

cursor1.execute("DROP TABLE PATIENT")
cursor1.execute("DROP TABLE DETAILS")
cursor1.execute("DROP TABLE USER")
#cursor1.execute("DROP TABLE SYMPTOMS")
#cursor1.execute("DROP TABLE TEXTSEARCH")

#creatingn the table USER
cursor1.execute("CREATE TABLE IF NOT EXISTS 'USER'(UID INTEGER PRIMARY KEY AUTOINCREMENT,UNAME VARCHAR(20) NOT NULL,PASSWORD VARCHAR(20) NOT NULL)")
db.commit()


label1=Label(frame1,text="UserName")
label1.grid(row=1,column=1,pady=10)

label2=Label(frame1,text="Password")
label2.grid(row=5,column=1,pady=10)

entry1=ttk.Entry(frame1)   #entry for user
entry1.grid(row=1,column=5,pady=10)

entry2=ttk.Entry(frame1,show="*")     #entry for password
entry2.grid(row=5,column=5,pady=10)


#function to check that user we enter is in the dataabse and its password is correct.also to raise the frame2
def dashboard2(frame):
    x=entry1.get()
    y=entry2.get()
    if(x=="" or y=="" ):
        messagebox.showinfo("ERROR","PLEASE ENTER ALL THE REQUIRED FIELD")
    else: 
        cursor1.execute("SELECT * FROM USER")
        records = cursor1.fetchall()   #fetching all the data from USER table
        temp=0     #temp as temporary variable
        for row in records:
            if(x==row[1] and y==row[2]):
                frame.tkraise()
                temp=temp+1
                #cursor1.execute("INSERT INTO 'USER'(UNAME,PASSWORD) VALUES(?,?)",(x,y))
                #db.commit()

        if(temp==0):
            messagebox.showinfo("ERROR","WRONG INPUT")
            
#creating button SIGNIN
button1=ttk.Button(frame1,text="SIGNIN",command=lambda:dashboard2(frame2))
button1.grid(row=20,column=1,pady=10)

#creating GUI for frame 2

frame2_button1=ttk.Button(frame2,text="BACK",command=lambda:dashboard(frame1))
frame2_button1.grid(row=1,column=1,sticky="W",pady=10)

frame2_label1=Label(frame2,text="ENTER PATIENT DETAIL")
frame2_label1.grid(row=5,column=5)

frame2_entry1=ttk.Entry(frame2)
frame2_entry1.grid(row=10,column=5)

frame2_label1=Label(frame2,text="NAME")
frame2_label1.grid(row=10,column=1,sticky="W")

frame2_label2=Label(frame2,text="PHONE_NO")
frame2_label2.grid(row=15,column=1,sticky="W")

frame2_entry2=ttk.Entry(frame2)
frame2_entry2.grid(row=15,column=5)

frame2_label3=Label(frame2,text="EMAIL")
frame2_label3.grid(row=20,column=1,sticky="W")

frame2_entry3=ttk.Entry(frame2)
frame2_entry3.grid(row=20,column=5)

frame2_label4=Label(frame2,text="AGE")
frame2_label4.grid(row=25,column=1,sticky="W")

frame2_entry4=ttk.Entry(frame2)
frame2_entry4.grid(row=25,column=5)

frame2_label5=Label(frame2,text="GENDER")
frame2_label5.grid(row=30,column=1,sticky="W")

frame2_entry5=ttk.Entry(frame2)
frame2_entry5.grid(row=30,column=5)

cursor1.execute("CREATE TABLE IF NOT EXISTS 'PATIENT'(PID INTEGER PRIMARY KEY AUTOINCREMENT,PNAME VARCHAR(20) NOT NULL,PHONE INTEGER NOT NULL,EMAIL VARCHAR(20) NOT NULL,AGE INTEGER NOT NULL,GENDER CHAR(2) NOT NULL)")
db.commit()
#funciton to get the patient input
def dashboard5(frame):
    x=frame2_entry1.get()
    y=frame2_entry2.get()
    z=frame2_entry3.get()
    a=frame2_entry4.get()
    b=frame2_entry5.get()
    if(x=="" or y=="" or z=="" or a=="" or b==""):
        messagebox.showinfo("ERROR","PLEASE ENTER ALL THE REQUIRED FIELD")
    else:   
        frame.tkraise()
        #cursor1.execute("INSERT INTO 'USER'(UNAME,PASSWORD) VALUES(?,?)",(x,y))
        cursor1.execute("INSERT INTO 'PATIENT'(PNAME,PHONE,EMAIL,AGE,GENDER) VALUES(?,?,?,?,?)",(x,y,z,a,b))
        db.commit()



frame2_button2=ttk.Button(frame2,text="ENTER",command=lambda:dashboard5(frame4))
frame2_button2.grid(row=40,column=10)

#defining the farme 4
def frame_Label1():
    for i in range(50):
        frame_Label1(frame,text=i).grid(row=i,column=0)
        frame_Label1(frame,text="my text"+str(i)).grid(row=i,column=1)
        frame_Label1(frame,text="..........").grid(row=i,column=2)



frame4_label1=Label(frame4,text="WELCOME TO MEDICINE PRESCRIBTION")
frame4_label1.grid(row=1,column=5)

frame4_button1=Button(frame4,text="BACK",command=lambda:dashboard(frame2))
frame4_button1.grid(row=5,column=1)

f = open("symptom.txt", "r")    #reading a file from text file
x=19
y=1
count=1

#logic to form the label using loop
for i in f:
    frame4_label2=Label(frame4,text=str(count)+" "+i)
    frame4_label2.grid(row=x,column=y,sticky="W")
    x= x+5
    count = count+1

    
    
#making GUI for frame5

frame5_label1=Label(frame5,text="CONSULTING DOCTOR")
frame5_label1.grid(row=1,column=5)

frame5_label1=Label(frame5,text="TIME")
frame5_label1.grid(row=5,column=1,sticky="W")

frame5_entry1=Entry(frame5,textvariable=str2)
frame5_entry1.grid(row=5,column=5)


def click2():
    w2 = Tk()
    w2.title("DETAILS")
    w2.geometry("500x500+100+100")
    w2_label1=Label(w2,text="PATIENT REPORT")
    w2_label1.grid(row=1,column=5)
        
    cursor1.execute("SELECT * FROM PATIENT")
    records = cursor1.fetchall()   #fetching all the data from USER table
    x=1     #temp as temporary variable
    for row in records:
        w2_label2=Label(w2,text=row)
        w2_label2.grid(row=x+5,column=1)
        db.commit()

    
    
frame5_button1=Button(frame5,text="ENTER",command=click2)
frame5_button1.grid(row=10,column=1)


frame4_entry1=Entry(frame4,textvariable=str1)
frame4_entry1.grid(row=x+5,column=1,sticky="W")

#function to display the prevention table
def click1():
    x=str1.get()
    if(re.findall(r'[a-z]',x)):
        messagebox.showinfo("ERROR","SORRY NO CHARATER INPUT IS ALLOWED")
    else:    
        w1= Tk()
        w1.title("PREVENTION")
        w1.geometry("500x500+100+100")
        b=str1.get()
        list1 = []
        list1 = b.split()
        x=1
        y=1
        w1_label=Label(w1,text="PREVENTION:")
        w1_label.grid(row=x ,column=y)
        x=x+19

        for i in list1:
            if(i==1):
                w1_label1=Label(w1,text="TREAT YOUR ALLERGIES OR PROTECT YOURSELF FROM ENVIRONMENTAL HAZARD AND TRY A HOMEOPATHIC NASAL SPRAY")
                w1_label1.grid(row=x ,column=y)
                x=x+5

            elif(i==2):
                w1_label2=Label(w1,text="AVOID ITRRITANTS INCLUDING SMOKE AND DUST OR KEEP HYDRAITED BY DRINKING PLENTY OF WATER AND GARGLE WITH WARM SALT REGULARLY")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==3):
                w1_label2=Label(w1,text="MAINTAIN GOOD HYGINE,AVOID CONTACT WITH SICK PEOPLE,MAKE SURE IMMUNIZATION ARE UPTO DATE")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==4):
                w1_label2=Label(w1,text="APPLY VICKS ON HEAD OR SLEEP AT LEAST 8 HRS PER DAY AND AVOID STRESS")
                w1_label2.grid(row=x ,column=y)
                x=x+5
            elif(i==5):
                w1_label2=Label(w1,text="EAT SLOWLY,AVAOID HARD TO DIGEST FOOD,USE VICKS THROAT")
                w1_label2.grid(row=x ,column=y)
                x=x+5
            elif(i==6):
                w1_label2=Label(w1,text="DON'T SMOKE,USE PAPER TOWEL,USE VICKS,KEEP CLEAN HOUSE SURFACE")
                w1_label2.grid(row=x ,column=y)
                x=x+5
            elif(i==7):
                w1_label2=Label(w1,text="EXERCISE WITH FINGER GRIP TOOLS DAILY,EAT NUTRISIOUS FOOD")
                w1_label2.grid(row=x ,column=y)
                x=x+5
            elif(i==8):
                w1_label2=Label(w1,text="SLEEP WELL,DRINK LESS ALCOHAL,LOSE WEIGHT TO GAIN ENERGY")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==9):
                w1_label2=Label(w1,text="EATING FRESH GINGER,DRINK BLACK COFFE,INHALING STREAM")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==10):
                w1_label2=Label(w1,text="EXERCISE,MASHAGE,STRESS REDUCTION,")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==11):
                w1_label2=Label(w1,text="EXERCISE YOUR LEG,WEAR SUPPORT STOCKING,FOLLOW A LOW SALT DIET")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==12):
                w1_label2=Label(w1,text="AVOID FRIED OR SWEET FOOD, DONOT MIX HOT AND COLD FOODS,AVOID BRUSHING YOUR TEETH AFTER EATING")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==13):
                w1_label2=Label(w1,text="FOLLOW A BALANCE DIET,QUIT SMOKING AND ALCOHOL")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==14):
                w1_label2=Label(w1,text="AVOIDING USE OF DIFFICULT TO DIGESTFOOD,TAKING A WARM BATH OR USING A HEATING BAG")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==15):
                w1_label2=Label(w1,text="TRY TO REDUCE THE AMOUNT STRESS IN YOUR LIFE,DRINK PLENTY OF WATER OR AVOID SALT ALCOHOL TOBBACO")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==16):
                w1_label2=Label(w1,text="EAT MORE HIGH FIBER FOOD OR EXERCISE BEFORE A MEAL OR DRINK WATER BEFORE EVERY MEAL OR SWITCH TOO DARK CHOCKLATE")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==17):
                w1_label2=Label(w1,text="STOP TOBACCO USE OR CHEW SUGAR FEE GUM")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            elif(i==18):
                w1_label2=Label(w1,text="BRUDER MOIST HEAT DRY EYE COMPRESS")
                w1_label2.grid(row=x ,column=y)
                x=x+5

            else:
                w1_label2=Label(w1,text="EAT AND DRINK VITAMIN C REACH FOOD AND DRINK OR AVOID DRINKING TEA AND COFEE WITH YOUR MEALS ")
                w1_label2.grid(row=x ,column=y)
                x=x+5

        w1_button1=ttk.Button(w1,text="NEXT",command=lambda:dashboard5(frame5))
        w1_button1.grid(row=x+5,column=1)

    


frame4_button=Button(frame4,text="NEXT",command= click1)
frame4_button.grid(row=x+10,column=1,sticky="W")

#if we click quit

button2=ttk.Button(frame1,text="QUIT",command=lambda:root.destroy())
button2.grid(row=20,column=5)


button3=ttk.Button(frame1,text="SIGNUP",command=lambda:dashboard(frame3))
button3.grid(row=20,column=10)

#defining frame3

frame3_label1=Label(frame3,text="New Regristration")
frame3_label1.grid(row=1,column=5)

cursor1.execute("CREATE TABLE IF NOT EXISTS 'DETAILS'(PID INTEGER PRIMARY KEY AUTOINCREMENT,NAME VARCHAR(20) NOT NULL,ADDRESS VARCHAR(20) NOT NULL,EMAIL VARCHAR(20) NOT NULL,PHONE_NO INTEGER)")


frame3_button1=ttk.Button(frame3,text="BACK",command=lambda:dashboard(frame1))
frame3_button1.grid(row=5,column=1,sticky="W")

frame3_label1=Label(frame3,text="NAME")
frame3_label1.grid(row=10,column=1,sticky="W")

frame3_entry1=ttk.Entry(frame3)
frame3_entry1.grid(row=10,column=5)

frame3_label2=Label(frame3,text="PHONE_NO")
frame3_label2.grid(row=15,column=1,sticky="W")

frame3_entry2=ttk.Entry(frame3)
frame3_entry2.grid(row=15,column=5)

frame3_label3=Label(frame3,text="EMAIL")
frame3_label3.grid(row=20,column=1,sticky="W")

frame3_entry3=ttk.Entry(frame3)
frame3_entry3.grid(row=20,column=5)

frame3_label4=Label(frame3,text="ADDRESS")
frame3_label4.grid(row=25,column=1,sticky="W")

frame3_entry4=ttk.Entry(frame3)
frame3_entry4.grid(row=25,column=5)

frame3_label5=Label(frame3,text="PASSWORD")
frame3_label5.grid(row=30,column=1,sticky="W")

frame3_entry5=ttk.Entry(frame3,show="*")
frame3_entry5.grid(row=30,column=5)

def dashboard4(frame):
    x=frame3_entry1.get()
    y=frame3_entry2.get()
    z=frame3_entry3.get()
    a=frame3_entry4.get()
    b=frame3_entry5.get()
    if(x=="" or y=="" or z=="" or a=="" or b=="" ):
        messagebox.showinfo("ERROR","PLEASE ENTER ALL THE FIELD")
        
    else:
        frame.tkraise()
        cursor1.execute("INSERT INTO 'DETAILS'(NAME,ADDRESS,EMAIL,PHONE_NO) VALUES(?,?,?,?)",(x,a,z,y))
        cursor1.execute("INSERT INTO 'USER'(UNAME,PASSWORD) VALUES(?,?)",(x,b))
        messagebox.showinfo("SUCCESS","SUCCESSFULL ENTERED")
        db.commit()

frame3_button2=ttk.Button(frame3,text="REGISTER",command=lambda:dashboard4(frame1))
frame3_button2.grid(row=35,column=1)


frame3_button3=ttk.Button(frame3,text="CANCEL",command=lambda:dashboard(frame1))
frame3_button3.grid(row=35,column=5)

dashboard(frame1)
root.mainloop()
