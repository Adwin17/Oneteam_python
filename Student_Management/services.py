import pickle
class Student:
    id=1
    def __init__(self,fname,lname,email,no,dob,gender,course,address,ad_date,status):
        self.id=Student.id
        Student.id+=1
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
    

def add_student():

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
    l=[std.id,fname,lname,email,no,dob,gender,course,address,ad_date,status]
    with open("Student_data.pkl","ab") as f:
        pickle.dump(std,f)

    print(f"Student with Student Id{std.id} Added Successfully !")

def view_all():
    with open ("Student_data.pkl","rb") as f:
        try:
            while True:
                s=pickle.load(f)
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

