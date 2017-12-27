import sqlite3
import tkinter as tk
from tkinter import  ttk
# Create instance
win1 = tk.Tk()

def ins():
            
            #win2.mainloop()
    win3=tk.Tk()
    win3.title("Add Details")
    aLabel = ttk.Label(win3, text="Fname")
    aLabel.grid(column=0, row=0)
    aLabel = ttk.Label(win3, text="Lname")
    aLabel.grid(column=0, row=1)
    aLabel = ttk.Label(win3, text="Semester")
    aLabel.grid(column=0, row=2)
    aLabel = ttk.Label(win3, text="Branch")
    aLabel.grid(column=0, row=3)
    aLabel = ttk.Label(win3, text="Admno")
    aLabel.grid(column=0, row=4)
    aLabel = ttk.Label(win3, text="Permanant Address")
    aLabel.grid(column=0, row=5)
    aLabel = ttk.Label(win3, text="Present Address")
    aLabel.grid(column=0, row=6)
    aLabel = ttk.Label(win3, text="GPA")
    aLabel.grid(column=2, row=0)
    aLabel = ttk.Label(win3, text="Class Roll")
    aLabel.grid(column=2, row=1)
    aLabel = ttk.Label(win3, text="dob")
    aLabel.grid(column=2 , row=2)
    aLabel = ttk.Label(win3, text="doj")
    aLabel.grid(column=2, row=3)
    aLabel = ttk.Label(win3, text="Family details")
    aLabel.grid(column=1, row=8)
    aLabel = ttk.Label(win3, text="Father's Name")
    aLabel.grid(column=1, row=10)
    aLabel = ttk.Label(win3, text="Mother's Name")
    aLabel.grid(column=1, row=11)
    aLabel = ttk.Label(win3, text="Siblings(if any)")
    aLabel.grid(column=3, row=11)
    aLabel = ttk.Label(win3, text="Advisor details")
    aLabel.grid(column=1, row=13)
    aLabel = ttk.Label(win3, text="facultid")
    aLabel.grid(column=1, row=15)
    aLabel = ttk.Label(win3, text="Qualification")
    aLabel.grid(column=1, row=16)
    aLabel = ttk.Label(win3, text="position")
    aLabel.grid(column=3, row=15)
    aLabel = ttk.Label(win3, text="Studentid")
    aLabel.grid(column=3, row=16)
    
    # Adding a Textbox Entry widget
    Fname = tk.StringVar()
    FnameEntered = ttk.Entry(win3, width=12, textvariable=Fname)
    FnameEntered.grid(column=1, row=0)
    Lname = tk.StringVar()
    LnameEntered = ttk.Entry(win3, width=12, textvariable=Lname)
    LnameEntered.grid(column=1, row=1)
    semester = tk.StringVar()
    semesterEntered = ttk.Entry(win3, width=12, textvariable=semester)
    semesterEntered.grid(column=1, row=2)
    branch= tk.StringVar()
    branchEntered = ttk.Entry(win3, width=12, textvariable=branch)
    branchEntered.grid(column=1, row=3)
    admno= tk.StringVar()
    admnoEntered = ttk.Entry(win3, width=12, textvariable=admno)
    admnoEntered.grid(column=1, row=4)
    pemanantaddress= tk.StringVar()
    permanantaddressEntered = ttk.Entry(win3, width=12, textvariable=pemanantaddress)
    permanantaddressEntered.grid(column=1, row=5)
    presentaddress = tk.StringVar()
    presentaddressEntered = ttk.Entry(win3, width=12, textvariable=presentaddress )
    presentaddressEntered.grid(column=1, row=6)
    gpa = tk.StringVar()
    gpaEntered = ttk.Entry(win3, width=12, textvariable=gpa )
    gpaEntered.grid(column=3, row=0)
    classroll = tk.StringVar()
    classrollEntered = ttk.Entry(win3, width=12, textvariable=classroll)
    classrollEntered.grid(column=3, row=1)
    dob = tk.StringVar()
    dobEntered = ttk.Entry(win3, width=12, textvariable=dob)
    dobEntered.grid(column=3, row=2)
    doj = tk.StringVar()
    dojEntered = ttk.Entry(win3, width=12, textvariable=doj)
    dojEntered.grid(column=3, row=3)
    Fathername = tk.StringVar()
    FathernameEntered = ttk.Entry(win3, width=12, textvariable=Fathername )
    FathernameEntered.grid(column=2, row=10)
    Mothername = tk.StringVar()
    MothernameEntered = ttk.Entry(win3, width=12, textvariable=Mothername)
    MothernameEntered.grid(column=2, row=11)
    Siblings= tk.StringVar()
    SiblingsEntered = ttk.Entry(win3, width=12, textvariable=Siblings)
    SiblingsEntered.grid(column=4, row=11)
    fid=tk.StringVar()
    F1=ttk.Entry(win3, width=12, textvariable=fid)
    F1.grid(column=2,  row=15)
    qu=tk.StringVar()
    Q1=ttk.Entry(win3, width=12, textvariable=qu)
    Q1.grid(column=2,  row=16)
    po=tk.StringVar()
    P1=ttk.Entry(win3,  width=12, textvariable=po)
    P1.grid(column=4, row=15)
    st=tk.StringVar()
    S1=ttk.Entry(win3, width=12, textvariable=st)
    S1.grid(column=4,  row=16)
    
    def ex():
        
        
        fname=FnameEntered.get()
        lname=LnameEntered.get()
        sem=semesterEntered.get()
        branch=branchEntered.get()
        admno=admnoEntered.get()
        pa=permanantaddressEntered.get()
        pa1=presentaddressEntered.get()
        gpa=gpaEntered.get()
        roll=classrollEntered.get()
        dob=dobEntered.get()
        doj=dojEntered.get()
        fatn=FathernameEntered()
        motn=MothernameEntered()
        sibn=SiblingsEntered()
        fid=F1.get()
        qu=Q1.get()
        po=P1.get()
        st=S1.get()
   
        conn=sqlite3.connect("Studentdatabase.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO STUDENTS(FNAME,LNAME, BRANCH, SEMESTER, ADMNO, PERMANANTADD,PRESENTADD, CGPA, CLASSROLL,DOB,DOJ )VALUES(?, ?,?,?,?,?,?,?,?,?,?);",  (fname, lname,  branch,  sem,  admno,  pa, pa1,  gpa,  roll,  dob,  doj)) 
        cur.execute("INSERT INTO FAMILY(FATHERNAME, MOTHERNAME, SIBLINGS)VALUES(?,?,?);", (fatn, motn, sibn))
        cur.execute("INSERT INTO FACULTY(FACID,QUALIFICATION, POSITION, STUDID)VALUES(?, ?, ?, ?);", (fid,  qu,  po,  st))
        FnameEntered.bind('<Return>',  ex) 
        LnameEntered.bind('<Return>', ex) 
        semesterEntered.bind('<Return>',  ex) 
        branchEntered.bind('<Return>',  ex)  
        admnoEntered.bind('<Return>',  ex) 
        permanantaddressEntered.bind('<Return>',  ex) 
        presentaddressEntered.bind('<Return>',  ex) 
        gpaEntered.bind('<Return>',  ex) 
        classrollEntered.bind('<Return>',  ex) 
        dobEntered.bind('<Return>',  ex) 
        dojEntered.bind('<Return>',  ex)
        FathernameEntered.bind('<Return>',  ex) 
        MothernameEntered.bind('<Return>',  ex) 
        SiblingsEntered.bind('<Return>',  ex) 
        F1.bind('<Return>',  ex) 
        Q1.bind('<Return>',  ex) 
        P1.bind('<Return>',  ex) 
        S1.bind('<Return>',  ex) 
    
    
    b9= ttk.Button(win3, text="OK",  width=12,  command=ex)   
    b9.grid(column=4, row=25)        
    
    
    
            

   
    
    
    
    win3.mainloop()

def connecto():
    content=e1.get()
    content1=e2.get()
    if( content=='admin' and content1=='pass'):
        #e1.bind('<Return>', connecto)
        #e2.bind('<Return>',  connecto)
        #win1.mainloop()
        # Create instance
        win2 = tk.Tk()   

        # Add a title       
        win2.title("Options")
        
        b2= ttk.Button(win2, text="Add Record",  width=12,command=ins)   
        b2.grid(column=1, row=0)
        
        b3= ttk.Button(win2, text="View Record",  width=12)   
        b3.grid(column=1, row=1)

        b4= ttk.Button(win2, text="Delete Record",  width=12)   
        b4.grid(column=1, row=2)

        b5= ttk.Button(win2, text="Update Record",  width=12)   
        b5.grid(column=1, row=3)

        b6= ttk.Button(win2, text="Exit",  width=12)   
        b6.grid(column=1, row=4)

        win2.mainloop()
        
        # Add a title       
win1.title("Student Record Database System")
#win1.resizable(0, 0)
aLabel=ttk.Label(win1,  text="Welcome to Student Database Record System")
aLabel.configure(foreground='red')
aLabel.grid(column=0,  row=0)

#Label2
aLabel=ttk.Label(win1, text="username")
aLabel.grid(column=0, row=1)

#Label3
aLabel=ttk.Label(win1, text="password")
aLabel.grid(column=0, row=2)

#define entries for each label
username_text=tk.StringVar()
e1=ttk.Entry(win1, textvariable=username_text)
e1.grid(row=1, column=1)


password_text=tk.StringVar()
e2=ttk.Entry(win1, textvariable=password_text)
e2.grid(row=2, column=1)
#y=password_text.get()
#button
b1=ttk.Button(win1, text="Enter",  width=12, command=connecto)
b1.grid(row=3, column=1)



e1.bind('<Return>', connecto)
e2.bind('<Return>',  connecto)
win1.mainloop()
