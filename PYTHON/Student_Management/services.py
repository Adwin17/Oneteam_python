import pickle
import validation
from models import Student
    
def next_id():
        last_id=0
        try:
            with open('Student_data.pkl','rb') as f:
                while True:
                    k=pickle.load(f)
                    last_id=k.id

        except(EOFError,FileNotFoundError):
            pass
        Student.id=last_id+1
def display_student(s):
    print("-" * 40)
    print("ID:", s.id)
    print("Name:", s.fname.title(), s.lname.title())
    print("Email:", s.email)
    print("Phone:", s.no)
    print("DOB:", s.dob)
    print("Gender:", s.gender.title())
    print("Course:", s.course.upper())
    print("Place:", s.place.title())
    print("Admission Date:", s.ad_date)
    print("Status:", s.status.title())
    print("-" * 40)

def add_student():
    next_id()
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    while True:
        email = input("Enter Email: ")
        if validation.validate_mail(email):
            break
        print("Invalid email. Try again.")
   
    while True:
        no = input("Enter Mobile No. without Country Code: ")
        if validation.validate_phone(no):
            break
        print("Invalid Number. Try again.")
    dob   = input("Enter Date of Birth: ")
    while True:
        gender = input("Enter Gender (Male/Female/Other): ")
        if validation.validate_gender(gender):
            break
        print("Invalid Gender. Try again.")
    course = input("Enter Course: ")
    place = input("Enter your place: ")
    ad_date = input("Enter Admission Date: ")
    while True:
        status = input("Enter Status (Active/Inactive): ")
        if validation.validate_status(status):
            break
        print("Invalid Status. Try again.")
    
    std=Student(fname,lname,email,no,dob,gender,course,place,ad_date,status)
    # l=[,fname,lname,email,no,dob,gender,course,address,ad_date,status]
    with open("Student_data.pkl","ab") as f:
        pickle.dump(std,f)

    print(f"Student with Student Id {std.id} Added Successfully !")

def view_all():
        found=False
        try:
            with open ("Student_data.pkl","rb") as f:
                while True:
                    s=pickle.load(f)
                    found=True
                    display_student(s)
        except (EOFError,FileNotFoundError):
            if not found:
                print("No student Records Found")
                
def view_students():
        found=False
        try:
            with open ("Student_data.pkl","rb") as f:
                while True:
                    s=pickle.load(f)
                    found=True
                    print("-"*40)
                    print("ID:", s.id, "Name:", s.fname, s.lname)
                    print("-" * 40)
                
        except (EOFError,FileNotFoundError):
            if not found:
                print("No student Records Found")
                
def search_name(n):
    found=False
    try:
        with open ("Student_data.pkl","rb") as f:
            while True:
                s=pickle.load(f)
                if n== (s.fname.lower()+' '+s.lname.lower()):
                    found=True
                    display_student(s)
            
                elif n==s.fname.lower() or n==s.lname.lower():
                    found=True
                    display_student(s)
                
    except (EOFError,FileNotFoundError):
        if not found:
            print("Student not found")
            
def search_id(n):
    found=False
    try:
        with open ("Student_data.pkl","rb") as f:
            while True:
                s=pickle.load(f)
                if n==s.id:
                    found=True
                    display_student(s)
                
    except (EOFError,FileNotFoundError):
        if not found:
            print("Student not found")
def search_course(n):
    found=False
    try:
        with open ("Student_data.pkl","rb") as f:
            while True:
                s=pickle.load(f)
                if n.lower()== s.course.lower():
                    found=True
                    display_student(s)
                
    except (EOFError,FileNotFoundError):
        if not found:
            print("Student not found")
            
def search_student():
    while True:
        print('-'*40)
        print('1.Search by Name')
        print('2.Search by ID')
        print('3.Search by Course')
        print('4.Exit to main menu')
        print('-'*40)
        try:
            option=int(input('Enter your choice: '))
        except ValueError:
            print("Please enter a valid number")
            continue
        match option:
            case 1:
                n=input("Enter the name to search: ").lower()
                search_name(n)
            case 2:
                n=int(input("Enter the ID: "))
                search_id(n)
                
            case 3:
                n=input("Enter the Course: ")
                search_course(n)
            case 4:
                break
            case _:
                print("Invalid Choice")

            
            
        
        

def delete_student():
    n=int(input("Enter the Student ID to delete :"))
    l=[]
    found=False
    deleted=False
    try:
        with open('Student_data.pkl','rb') as f:
            while True:
                k=pickle.load(f)
                if n==k.id:
                    found=True
                    display_student(k)
                    confirm=input("Are you sure you want to delete this student (yes/no) : ")
                    if confirm.lower()=='yes':
                        deleted=True
                    else:
                        l.append(k)
                        continue
                    
                else:
                    l.append(k)
    except(EOFError,FileNotFoundError):
        pass

    with open('Student_data.pkl','wb') as f1:
        for i in l:
            pickle.dump(i,f1)
    if deleted:
        print("Student deleted Succesfully")
    elif found:
        print("Deletion Cancelled")
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
                    while True:
                        k.email = input("Enter Email: ")
                        if validation.validate_mail(k.email):
                            break
                        print("Invalid email. Try again.")
                    while True:
                        k.no = input("Enter Phone Number without country code: ")
                        if validation.validate_phone(k.no):
                            break
                        print("Invalid Phone Number. Try again.")
                    k.dob = input("Enter Date of Birth: ")
                    while True:
                        k.gender = input("Enter Gender (Male/Female/Other): ")
                        if validation.validate_gender(k.gender):
                            break
                        print("Invalid Gender. Try again.")
                    k.course = input("Enter Course: ")
                    k.place = input("Enter place: ")
                    k.ad_date = input("Enter Admission Date: ")
                    while True:
                        k.status = input("Enter Status (Active/Inactive): ")
                        if validation.validate_status(k.status):
                            break
                        print("Invalid Status. Try again.")
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
        


     
    

    
   

        