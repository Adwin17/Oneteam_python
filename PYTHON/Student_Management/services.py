import pickle
class Student:
   
    def __init__(self,fname,lname,email,no,dob,gender,course,address,ad_date,status):
        self.id=Student.id
        
        self.fname=fname
        self.lname=lname
        self.email=email
        self.no=no
        self.dob=dob
        self.gender=gender
        self.course=course
        self.address=address
        self.ad_date=ad_date
        self.status=status
    
def next_id():
   
        try:
            with open('Student_data.pkl','rb') as f:
                k=0
                while True:
                
                    k=pickle.load(f)

        except(EOFError,FileNotFoundError):
            pass
        if k==0:
            Student.id=1
        else:
            Student.id=k.id+1

def add_student():
    next_id()
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    email = input("Enter Email: ")
    no    = input("Enter Phone Number: ")
    dob   = input("Enter Date of Birth: ")
    gender = input("Enter Gender: ")
    course = input("Enter Course: ")
    address = input("Enter Address: ")
    ad_date = input("Enter Admission Date: ")
    status = input("Enter Status (Active/Inactive): ")
    std=Student(fname,lname,email,no,dob,gender,course,address,ad_date,status)
    # l=[,fname,lname,email,no,dob,gender,course,address,ad_date,status]
    with open("Student_data.pkl","ab") as f:
        pickle.dump(std,f)

    print(f"Student with Student Id {std.id} Added Successfully !")

def view_all():
    with open ("Student_data.pkl","rb") as f:
        found=False
        
        try:
            while True:
                s=pickle.load(f)
                found=True
                print("-"*40)
                print("ID:", s.id)
                print("Name:", s.fname, s.lname)
                print("Email:", s.email)
                print("Phone:", s.no)
                print("DOB:",s.dob)
                print("Gender:", s.gender)
                print("Course:", s.course)
                print("Address:", s.address)
                print("Admission Date:", s.ad_date)
                print("Status:", s.status)
                print("-"*40)
        except EOFError:
            if not found:
                print("No student Records Found")

def search_student():

    n=input("Enter the name to search :").lower()
    with open ("Student_data.pkl","rb") as f:
        try:
            while True:
                s=pickle.load(f)
                if n== (s.fname.lower()+' '+s.lname.lower()):
                    print("-"*40)
                    print("ID:", s.id)
                    print("Name:", s.fname, s.lname)
                    print("Email:", s.email)
                    print("Phone:", s.no)
                    print("DOB:",s.dob)
                    print("Gender:", s.gender)
                    print("Course:", s.course)
                    print("Address:", s.address)
                    print("Admission Date:", s.ad_date)
                    print("Status:", s.status)
                    print("-"*40)
            
                elif n==s.fname.lower() or n==s.lname.lower():
                    print("-"*40)
                    print("ID:", s.id)
                    print("Name:", s.fname, s.lname)
                    print("Email:", s.email)
                    print("Phone:", s.no)
                    print("DOB:",s.dob)
                    print("Gender:", s.gender)
                    print("Course:", s.course)
                    print("Address:", s.address)
                    print("Admission Date:", s.ad_date)
                    print("Status:", s.status)
                    print("-"*40)
                    
        except EOFError:
            pass

def delete_student():
    n=input("Enter the name to delete :").lower()
    l=[]
    found=False
    try:
        with open('Student_data.pkl','rb') as f:
            while True:
                k=pickle.load(f)
                if n==k.fname.lower()+" "+k.lname.lower():
                    found=True
                    print(k)
                    continue
                elif n==k.fname.lower() or n==k.lname.lower():
                    found=True
                    print(k)
                    continue
                else:
                    l.append(k)
    except(EOFError,FileNotFoundError):
        pass

    with open('Student_data.pkl','wb') as f1:
        for i in l:
            pickle.dump(i,f1)
    if found:
        print("Student deleted Succesfully")
    else:
        print("Student not found")  

def update_student():
    n=int(input("Enter the student id to update the details :"))
    found=False
    l=[]
    try:
        with open('Student_data.pkl','rb') as f:
            while True:
                k=pickle.load(f)
                if n==k.id:
                    found=True
                    k.fname = input("Enter First Name: ")
                    k.lname = input("Enter Last Name: ")
                    k.email = input("Enter Email: ")
                    k.no = input("Enter Phone Number: ")
                    k.dob = input("Enter Date of Birth: ")
                    k.gender = input("Enter Gender: ")
                    k.course = input("Enter Course: ")
                    k.address = input("Enter Address: ")
                    k.ad_date = input("Enter Admission Date: ")
                    k.status = input("Enter Status (Active/Inactive): ")
                    l.append(k)
                    continue
                    

                else:
                    l.append(k)
    except(EOFError,FileNotFoundError):
        pass
    with open('Student_data.pkl','wb') as f1:
        for i in l:
            pickle.dump(i,f1)
    if found:
        print("Student details Updated Succesfully")
    else:
        print("Student not found") 
        
def view_students():
     with open ("Student_data.pkl","rb") as f:
        found=False
        
        try:
            while True:
                s=pickle.load(f)
                found=True
                print("-"*40)
                print("ID:", s.id, "Name:", s.fname, s.lname)
                
        except EOFError:
            if not found:
                print("No student Records Found")

     
    

    
   

        