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
    

